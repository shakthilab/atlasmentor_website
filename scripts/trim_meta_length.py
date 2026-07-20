"""
One-off pass to bring scraped WordPress titles/descriptions under Google's
practical SERP display limits (~60 chars title, ~160 chars description),
so search results stop truncating them mid-word. Preserves meaning/keywords;
does not invent new facts.
"""
import json
import re
import glob

TITLE_LIMIT = 60
DESC_LIMIT = 160

# Titles that need more than just dropping the " - Atlas Mentor" suffix.
TITLE_OVERRIDES = {
    "data/pages/international-higher-school-of-medicine.json": "International Higher School of Medicine, Kyrgyzstan",
    "data/pages/mbbs-abroad.json": "MBBS Abroad for Indian Students | Fees & Eligibility",
    "data/pages/study-mbbs-in-kazakhstan-for-indian-students.json": "MBBS in Kazakhstan for Indians | Fees & Eligibility",
    "data/pages/study-mbbs-in-kyrgyzstan-for-indian-students.json": "MBBS in Kyrgyzstan for Indians | Fees & Eligibility",
    "data/pages/study-mbbs-in-uzbekistan-for-indian-students.json": "MBBS in Uzbekistan for Indians | Fees & Eligibility",
}

# Descriptions with unique facts that need bespoke shortening (not just the
# templated boilerplate below). Grammar slips in the original scrape
# ("Nursring", "it's quality", "helm medical institutes") are fixed in passing.
DESC_OVERRIDES = {
    "data/pages/al-farabi-kazakh-national-university.json": "KazNU, founded in 1934, is one of Kazakhstan's oldest and most respected universities, located in Almaty, the country's largest city.",
    "data/pages/andijan-state-medical-institute-ranking.json": "Andijan State Medical Institute, established in 1955, is one of Uzbekistan's oldest and most respected medical institutes.",
    "data/pages/astana-medical-university.json": "Astana Medical University (AMU), established in 1997 in Nur-Sultan, Kazakhstan, is known for quality training in medicine, dentistry, pharmacy, and nursing.",
    "data/pages/bashkir-state-medical-university.json": "Founded in 1932 in Ufa, Russia, Bashkir State Medical University (BSMU) is one of the country's oldest medical schools.",
    "data/pages/kazan-federal-university.json": "Founded in 1804 in Kazan, one of Russia's oldest cities, Kazan Federal University is among the country's largest and oldest universities.",
    "data/pages/kuban-state-medical-university.json": "Kuban State Medical University (KSMU), founded in 1920 in Krasnodar, is a prominent Russian university for medicine, pharmacy, and dentistry.",
    "data/pages/north-kazakhstan-state-university.json": "North Kazakhstan State University (NKSU), founded 1937 in Petropavlovsk, Kazakhstan, offers undergraduate and postgraduate medicine programs.",
    "data/pages/samarkand-state-medical-institute.json": "Founded in 1930 in Samarkand, Samarkand State Medical Institute is known for quality medical education and modern infrastructure.",
    "data/pages/south-kazakh-medical-academy.json": "South Kazakh Medical Academy (SKMA), founded 1979 in Shymkent, Kazakhstan, offers programs in medicine, dentistry, pharmacy, and nursing.",
    "data/pages/volgograd-state-medical-university-vsmu.json": "Founded in 1935, Volgograd State Medical University (VSMU) is one of Russia's leading medical institutes.",
    "data/pages/fergana-medical-institute-of-public-health.json": "Fergana Medical Institute of Public Health, established in 1991 as a medical center of Fergana State University, is located in Uzbekistan.",
    "data/pages/international-medical-university.json": "Explore International Medical University (IMU) in Kyrgyzstan for MBBS abroad — admissions, eligibility, and guidance from Atlas Mentor.",
    "data/pages/contact-us.json": "Get in touch with Atlas Mentor for free MBBS abroad counselling — universities, fees, eligibility, and the admission process.",
    "data/pages/index.json": "Expert guidance to study MBBS abroad in Russia, Georgia, Kazakhstan, Uzbekistan, Kyrgyzstan, Moldova, and Vietnam — free counselling from Atlas Mentor.",
    "data/pages/mbbs-abroad.json": "A complete guide to MBBS abroad: eligibility, NEET requirements, choosing a country, real costs, and practicing in India after you graduate.",
}

BOILERPLATE_LEAD_INS = [
    "Atlas Mentor specializes in guiding students through their MBBS study abroad journey",
    "Atlas Mentor specializes in providing comprehensive guidance and support to students navigating their MBBS study abroad journey",
]

DESC_ENDINGS = [
    " — personalized support from application through enrollment.",
    " — personalized support through admissions and enrollment.",
    " — Atlas Mentor supports your admission and enrollment.",
]

STUDY_MBBS_TEMPLATE = "Study MBBS in {country} with Atlas Mentor — top universities, fees, eligibility, and free counselling for Indian students."
COUNTRY_HUB_TEMPLATE = "Compare top MBBS universities in {country} — rankings, fees, and eligibility for Indian students. Free expert guidance from Atlas Mentor."


def entity_from_title(title: str) -> str:
    return title.split(" – Atlas Mentor")[0].split(" - Atlas Mentor")[0]


def fix_title(path: str, title: str) -> str:
    if len(title) <= TITLE_LIMIT:
        return title
    if path in TITLE_OVERRIDES:
        return TITLE_OVERRIDES[path]
    stripped = entity_from_title(title)
    if len(stripped) <= TITLE_LIMIT:
        return stripped
    return title  # no safe rule matched — leave for manual follow-up


def fix_boilerplate_desc(path: str, title: str) -> str | None:
    entity = entity_from_title(title)
    entity_no_abbrev = re.sub(r"\s*\([^)]*\)", "", entity)
    base = f"Atlas Mentor guides MBBS aspirants applying to {entity_no_abbrev}"
    for ending in DESC_ENDINGS:
        candidate = base + ending
        if len(candidate) <= DESC_LIMIT:
            return candidate
    return None


def fix_desc(path: str, title: str, desc: str) -> str:
    if len(desc) <= DESC_LIMIT:
        return desc
    if path in DESC_OVERRIDES:
        return DESC_OVERRIDES[path]

    m = re.search(r"^Study MBBS in (\w+)", desc)
    if m:
        return STUDY_MBBS_TEMPLATE.format(country=m.group(1))
    m = re.search(r"^Compare the top MBBS universities in (\w+)", desc)
    if m:
        return COUNTRY_HUB_TEMPLATE.format(country=m.group(1))

    if any(desc.startswith(b) for b in BOILERPLATE_LEAD_INS):
        fixed = fix_boilerplate_desc(path, title)
        if fixed:
            return fixed

    return desc  # no safe rule matched — leave for manual follow-up


def process_file(path: str) -> bool:
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    had_trailing_newline = raw.endswith("\n")
    data = json.loads(raw)

    title = (data.get("title") or "").strip()
    desc = (data.get("description") or "").strip()
    new_title = fix_title(path, title)
    new_desc = fix_desc(path, title, desc)

    if new_title == title and new_desc == desc:
        return False

    data["title"] = new_title
    data["description"] = new_desc
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        if had_trailing_newline:
            f.write("\n")
    return True


def main():
    changed = 0
    still_over = []
    for path in sorted(glob.glob("data/pages/*.json")) + sorted(glob.glob("data/pages/mbbs-university/*.json")):
        if process_file(path):
            changed += 1
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        if len((data.get("title") or "")) > TITLE_LIMIT or len((data.get("description") or "")) > DESC_LIMIT:
            still_over.append(path)

    print(f"Updated {changed} files.")
    if still_over:
        print("Still over limit (needs manual attention):")
        for p in still_over:
            print(f"  {p}")


if __name__ == "__main__":
    main()

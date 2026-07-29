import os
import json
from glob import glob

pages_dir = "data/pages"
all_json_files = glob(f"{pages_dir}/*.json") + glob(f"{pages_dir}/*/*.json")

count_updated = 0

for filepath in sorted(all_json_files):
    rel = os.path.relpath(filepath, pages_dir)
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    title = data.get("title", "").strip()
    desc = data.get("description", "").strip()
    
    modified = False

    # Homepage
    if rel == "index.json":
        data["title"] = "Study MBBS Abroad 2026: Top NMC Approved Universities – Atlas Mentor"
        data["description"] = "Guiding Indian students for MBBS Abroad in Georgia, Russia, Uzbekistan, Kazakhstan & Kyrgyzstan. Check 2026 fees, NMC gazette rules & direct admissions."
        modified = True
    elif rel == "mbbs-abroad.json":
        data["title"] = "Study MBBS Abroad for Indian Students 2026: Fees, Eligibility & Colleges – Atlas Mentor"
        data["description"] = "Explore MBBS Abroad options for Indian medical aspirants in 2026. Compare tuition fees, NMC gazette compliance, hostel costs, and entry requirements."
        modified = True
    elif rel == "contact-us.json":
        data["title"] = "Contact Atlas Mentor: Free MBBS Abroad Admission Counseling – Atlas Mentor"
        data["description"] = "Get in touch with expert medical admission counselors at Atlas Mentor. Call +91-7859033144 for free guidance on studying MBBS abroad in 2026."
        modified = True
    elif rel.startswith("study-mbbs-in-") and rel.endswith("-for-indian-students.json"):
        # e.g. study-mbbs-in-georgia-for-indian-students.json
        country_slug = rel.replace("study-mbbs-in-", "").replace("-for-indian-students.json", "").capitalize()
        data["title"] = f"Study MBBS in {country_slug} for Indian Students 2026: Fees, NMC Colleges & Admission – Atlas Mentor"
        data["description"] = f"Complete 2026 guide for studying MBBS in {country_slug} for Indian students. Check tuition fees in INR, NMC gazette approval, NEET cutoff, and admission process."
        modified = True
    elif rel.startswith("mbbs-university/"):
        # e.g. mbbs-university/georgia.json
        country_name = rel.replace("mbbs-university/", "").replace(".json", "").capitalize()
        data["title"] = f"Top MBBS Medical Universities in {country_name} 2026: Fees & Rankings – Atlas Mentor"
        data["description"] = f"Discover top-ranked NMC approved medical colleges for MBBS in {country_name}. Detailed 2026 fee structure, hostel facilities, FMGE pass rates & admissions."
        modified = True
    else:
        # University Pages (e.g. caucasus-international-university.json)
        # Check if title doesn't already have 2026 or Fees
        if "– Atlas Mentor" in title or "- Atlas Mentor" in title:
            clean_title = title.split(" – Atlas Mentor")[0].split(" - Atlas Mentor")[0].strip()
            # If university title contains Ranking or comma
            if "2026" not in clean_title and "Fees" not in clean_title:
                new_title = f"{clean_title}: Fees 2026, Admission & Ranking – Atlas Mentor"
                data["title"] = new_title
                modified = True
        
        if desc and "2026" not in desc:
            # Enhance description with 2026 fees & NMC mention
            if not desc.endswith("."):
                desc += "."
            new_desc = f"{desc} Check 2026 tuition fees, NMC gazette approval & direct admission process."
            if len(new_desc) <= 165:
                data["description"] = new_desc
                modified = True

    if modified:
        count_updated += 1
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Updated metadata for {count_updated} pages.")

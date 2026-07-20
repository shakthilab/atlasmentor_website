"""
One-off backfill for <img alt=""> left empty by the WordPress scrape.
Derives alt text from the image filename (e.g. Alte-Medical-University-Georgia.jpg
-> "Alte Medical University Georgia") and skips images that are decorative:
plugin/UI-chrome assets, nav icons paired with visible menu text, tiny icons,
and the repeated Atlas Mentor circle badge used as a bullet in image-box widgets.
"""
import json
import os
import re
import glob
import html

REPEATED_DECORATIVE_BADGES = {"Atlas-Mentor-Circle-White-New.png"}

KNOWN_LOGOS = {
    "Atlas-Mentor-Pvt-Ltd.png": "Atlas Mentor",
    "Atlas-Mentor-Pvt-Ltd-White.png": "Atlas Mentor",
}

IMG_TAG_RE = re.compile(r"<img\b[^>]*>")
SRC_RE = re.compile(r'src="([^"]*)"')
CLASS_RE = re.compile(r'class="([^"]*)"')
ALT_RE = re.compile(r'alt="([^"]*)"')


def humanize(basename: str) -> str:
    stem = re.sub(r"\.(jpe?g|png|webp|gif)$", "", basename, flags=re.I)
    stem = re.sub(r"-\d+x\d+$", "", stem)  # WP size suffix, e.g. -300x171
    stem = re.sub(r"-\d{1,2}$", "", stem)  # WP re-upload dedup suffix, e.g. -1
    stem = stem.replace("_", " ").replace("-", " ")
    return re.sub(r"\s+", " ", stem).strip()


def decide_alt(img_tag: str, src: str) -> str | None:
    """Returns new alt text, or None if the image should stay decorative (alt="")."""
    basename = os.path.basename(src)

    if basename in KNOWN_LOGOS:
        return KNOWN_LOGOS[basename]
    if "/wp-content/plugins/" in src:
        return None
    if basename in REPEATED_DECORATIVE_BADGES:
        return None
    cls_match = CLASS_RE.search(img_tag)
    if cls_match and "menu-image" in cls_match.group(1):
        return None
    size_match = re.search(r"-(\d+)x(\d+)\.\w+$", basename)
    if size_match and int(size_match.group(1)) <= 48 and int(size_match.group(2)) <= 48:
        return None

    return humanize(basename)


def process_html(text: str) -> tuple[str, int]:
    filled = 0

    def replace_tag(match: re.Match) -> str:
        nonlocal filled
        tag = match.group(0)
        alt_match = ALT_RE.search(tag)
        if not alt_match or alt_match.group(1).strip() != "":
            return tag  # no alt attr, or already has real alt text — leave alone

        src_match = SRC_RE.search(tag)
        src = src_match.group(1) if src_match else ""
        new_alt = decide_alt(tag, src)
        if new_alt is None:
            return tag

        filled += 1
        escaped = html.escape(new_alt, quote=True)
        start, end = alt_match.span(1)
        return tag[: start - len('alt="')] + f'alt="{escaped}"' + tag[end + 1 :]

    return IMG_TAG_RE.sub(replace_tag, text), filled


def process_json_file(path: str) -> int:
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    had_trailing_newline = raw.endswith("\n")
    data = json.loads(raw)
    if "body" not in data:
        return 0
    new_body, filled = process_html(data["body"])
    if filled:
        data["body"] = new_body
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
            if had_trailing_newline:
                f.write("\n")
    return filled


def process_html_file(path: str) -> int:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    new_content, filled = process_html(content)
    if filled:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
    return filled


def main():
    total = 0
    for path in sorted(glob.glob("data/pages/*.json")) + sorted(glob.glob("data/pages/mbbs-university/*.json")):
        total += process_json_file(path)
    for path in ["data/globals/header.html", "data/globals/footer.html"]:
        if os.path.exists(path):
            total += process_html_file(path)
    print(f"Filled alt text on {total} images.")


if __name__ == "__main__":
    main()

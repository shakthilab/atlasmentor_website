import os
import json
import re
from glob import glob

pages_dir = "data/pages"
all_json_files = glob(f"{pages_dir}/*.json") + glob(f"{pages_dir}/*/*.json")

total_links_fixed = 0
total_alts_fixed = 0
files_modified = 0

for filepath in sorted(all_json_files):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    body = data.get("body", "")
    page_title = data.get("title", "").split("–")[0].split("-")[0].strip()
    if not page_title:
        page_title = "MBBS Study Abroad"

    modified = False

    # 1. Fix internal hrefs missing trailing slash
    def fix_href(match):
        global total_links_fixed, modified
        full_match = match.group(0)
        quote = match.group(1)
        url = match.group(2)
        
        # Exclude anchor links, query params, files, or external URLs
        if any(url.endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.pdf', '.css', '.js']):
            return full_match
        if '#' in url or '?' in url:
            return full_match
        if not (url.startswith('/') or 'atlasmentor.com' in url):
            return full_match
        if url.endswith('/'):
            return full_match

        # Add trailing slash
        new_url = url + '/'
        total_links_fixed += 1
        modified = True
        return f'href={quote}{new_url}{quote}'

    new_body = re.sub(r'href=(["\'])(/?[^"\'\s>]+)\1', fix_href, body)

    # 2. Fix images missing alt attributes
    def fix_img_alt(match):
        global total_alts_fixed, modified
        img_tag = match.group(0)
        
        # Check if alt attribute exists
        alt_match = re.search(r'alt=["\']([^"\']*)["\']', img_tag, re.IGNORECASE)
        if not alt_match or not alt_match.group(1).strip():
            # Extract src or title if available to form a good alt
            src_match = re.search(r'src=["\']([^"\']*)["\']', img_tag, re.IGNORECASE)
            src_name = ""
            if src_match:
                filename = os.path.basename(src_match.group(1)).split('.')[0].replace('-', ' ').replace('_', ' ')
                src_name = filename.title()
            
            alt_text = f"{page_title} - {src_name}".strip(" - ")
            
            if not alt_match:
                # Insert alt before closing tag
                new_img = img_tag[:-1] + f' alt="{alt_text}">'
            else:
                # Replace empty alt
                new_img = re.sub(r'alt=["\']([^"\']*)["\']', f'alt="{alt_text}"', img_tag)

            total_alts_fixed += 1
            modified = True
            return new_img

        return img_tag

    new_body = re.sub(r'<img[^>]+>', fix_img_alt, new_body)

    if modified:
        data["body"] = new_body
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        files_modified += 1

print(f"=== LINK & ALT FIX SUMMARY ===")
print(f"Files Modified: {files_modified}")
print(f"Total Internal Links Fixed: {total_links_fixed}")
print(f"Total Image Alts Fixed: {total_alts_fixed}")

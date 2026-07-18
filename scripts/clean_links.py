import os
import re
import json

def build_id_map(root_dir):
    id_to_slug = {}
    for dirpath, dirnames, filenames in os.walk(root_dir):
        rel_dir = os.path.relpath(dirpath, root_dir)
        if rel_dir == '.' or any(x in rel_dir for x in ['wp-includes', 'wp-content', 'wp-json', 'comments', 'feed']):
            continue
            
        for filename in filenames:
            if filename == 'index.html':
                filepath = os.path.join(dirpath, filename)
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    text = f.read()
                
                post_ids = re.findall(r'data-elementor-id=\"([0-9]+)\"', text)
                if post_ids:
                    for pid in post_ids:
                        if pid not in ['61', '64', '664', '370', '685']:
                            id_to_slug[pid] = rel_dir
                            break
    return id_to_slug

def clean_href(href, id_to_slug):
    if not href:
        return href
        
    # Check anchor on homepage
    # e.g., 'index.html#mbbs-atlas' -> '/#mbbs-atlas'
    # e.g., '../index.html#mbbs-atlas' -> '/#mbbs-atlas'
    if 'index.html#' in href:
        parts = href.split('#')
        return '/#' + parts[1]
        
    # Remove query params or trailing .html from local links
    # E.g., 'index.html%3Fp=1318.html' -> 'p=1318'
    # E.g., '../index.html?p=1318' -> 'p=1318'
    match_p = re.search(r'(?:\?|%3F)p=([0-9]+)', href)
    if match_p:
        pid = match_p.group(1)
        if pid in id_to_slug:
            return '/' + id_to_slug[pid]
            
    # Check if it points to index.html at root (the homepage)
    if href in ['index.html', '../index.html', '../../index.html']:
        return '/'
        
    # Clean folder-based links:
    # E.g., 'contact-us/index.html' -> '/contact-us'
    # E.g., '../contact-us/index.html' -> '/contact-us'
    # E.g., 'mbbs-university/russia/index.html' -> '/mbbs-university/russia'
    # E.g., '../../mbbs-university/russia/index.html' -> '/mbbs-university/russia'
    if href.endswith('/index.html'):
        clean = href[:-11].strip('/')
        # Remove any leading relative paths like '../' or '../../'
        clean = re.sub(r'^(\.\./)+', '', clean)
        return '/' + clean
        
    if href.endswith('.html') and 'index.html%3Fp=' not in href:
        # Some general html pages, e.g. contact-us.html (if any)
        clean = href[:-5].strip('/')
        clean = re.sub(r'^(\.\./)+', '', clean)
        return '/' + clean
        
    return href

def replace_links_in_html(html_content, id_to_slug):
    # Regex to find all href="..."
    def replacer(match):
        href = match.group(1)
        # Avoid external links
        if href.startswith(('http://', 'https://', 'tel:', 'mailto:', '#', 'javascript:')):
            # But replace absolute atlasmentor.com links with relative ones!
            if 'atlasmentor.com' in href:
                parts = href.split('atlasmentor.com')
                sub_path = parts[-1]
                if sub_path.endswith('/index.html'):
                    sub_path = sub_path[:-11]
                if sub_path.endswith('/'):
                    sub_path = sub_path.rstrip('/')
                return f'href="{sub_path or "/"}"'
            return match.group(0)
            
        new_href = clean_href(href, id_to_slug)
        return f'href="{new_href}"'
        
    return re.sub(r'href="([^"]*)"', replacer, html_content)

def main():
    root_dir = 'mirrored-site/atlasmentor.com'
    id_to_slug = build_id_map(root_dir)
    print(f"Loaded {len(id_to_slug)} ID-to-Slug mappings.")

    # 1. Clean globals
    globals_dir = 'data/globals'
    for item in os.listdir(globals_dir):
        if item.endswith('.html'):
            filepath = os.path.join(globals_dir, item)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            cleaned = replace_links_in_html(content, id_to_slug)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(cleaned)
            print(f"Cleaned links in global: {item}")

    # 2. Clean pages
    pages_dir = 'data/pages'
    cleaned_pages_count = 0
    for dirpath, dirnames, filenames in os.walk(pages_dir):
        for filename in filenames:
            if filename.endswith('.json'):
                filepath = os.path.join(dirpath, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                # Clean page body
                if 'body' in data:
                    data['body'] = replace_links_in_html(data['body'], id_to_slug)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2)
                cleaned_pages_count += 1

    print(f"Cleaned links in {cleaned_pages_count} pages.")

if __name__ == '__main__':
    main()

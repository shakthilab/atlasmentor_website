import os
import re
import json
from html.parser import HTMLParser

# Helper function to extract a nested HTML tag block by matching nesting depth
def extract_nested_tag(html, tag_name, attr_indicator):
    start_idx = html.find(attr_indicator)
    if start_idx == -1:
        return ""
    # Find the tag start before the attribute indicator
    tag_start = html.rfind("<" + tag_name, 0, start_idx)
    if tag_start == -1:
        return ""
    
    # Find matching closing tag by tracking depth
    depth = 0
    pattern = re.compile(rf'<(/?{tag_name})\b[^>]*>', re.IGNORECASE)
    
    for match in pattern.finditer(html, tag_start):
        tag = match.group(1).lower()
        if tag.startswith('/'):
            depth -= 1
        else:
            depth += 1
        
        if depth == 0:
            return html[tag_start:match.end()]
            
    return ""

def clean_css_url(url):
    # Remove query string parameters and normalize paths
    clean = url.split('?')[0].split('%3F')[0]
    if clean.startswith('../'):
        clean = '/' + clean.replace('../', '')
    if not clean.startswith('/'):
        clean = '/' + clean
    return clean

class HeadParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.description = ""
        self.robots = ""
        self.stylesheets = []
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == "title":
            self.in_title = True
        elif tag == "link" and attrs_dict.get("rel") == "stylesheet":
            href = attrs_dict.get("href", "")
            if href:
                self.stylesheets.append(clean_css_url(href))
        elif tag == "meta":
            name = attrs_dict.get("name", "").lower()
            if name == "description":
                self.description = attrs_dict.get("content", "")
            elif name == "robots":
                self.robots = attrs_dict.get("content", "")

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data

def parse_html_page(filepath, clean_canonical):
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None

    # Parse Head
    head_match = re.search(r'<head[^>]*>(.*?)</head>', content, re.DOTALL | re.IGNORECASE)
    head_content = head_match.group(1) if head_match else ""
    
    parser = HeadParser()
    parser.feed(head_content)

    title = parser.title.strip()
    description = parser.description.strip()
    robots = parser.robots.strip()
    stylesheets = parser.stylesheets

    # Extract Page content
    header_end = content.find("</header>")
    if header_end != -1:
        header_end += len("</header>")
    else:
        header_end = 0

    footer_start = content.find('data-elementor-type="footer"')
    if footer_start != -1:
        footer_tag_start = content.rfind("<div", 0, footer_start)
        if footer_tag_start == -1:
            footer_tag_start = footer_start
    else:
        footer_tag_start = len(content)

    page_body = content[header_end:footer_tag_start].strip()

    # Clean up page_body links pointing to local index.html%3Fp=... files
    # E.g., href="../index.html%3Fp=1318.html"
    # We will replace them with their clean relative paths in Next.js.
    # To keep this safe and simple, we can do it dynamically or in the static pages.
    # We can write a dynamic router or map them in the Next.js Link component.
    # But cleaning them up in the static extraction is extremely helpful!
    # Let's clean them up in Next.js dynamically or do a regex replace. Let's do it in Next.js to make it robust,
    # or replace relative links to index.html%3Fp=1318.html with /slug or appropriate.
    
    return {
        "title": title,
        "description": description,
        "canonical": clean_canonical,
        "robots": robots,
        "stylesheets": stylesheets,
        "body": page_body
    }

def main():
    root_dir = "mirrored-site/atlasmentor.com"
    pages_data_dir = "data/pages"
    os.makedirs(pages_data_dir, exist_ok=True)

    # Extract global components from homepage
    homepage_file = os.path.join(root_dir, "index.html")
    if not os.path.exists(homepage_file):
        print("Homepage index.html not found! Make sure you are in the correct CWD.")
        return

    with open(homepage_file, "r", encoding="utf-8", errors="ignore") as f:
        home_html = f.read()

    # Extract header
    header_html = extract_nested_tag(home_html, "header", 'data-elementor-type="header"')
    # Extract footer
    footer_html = extract_nested_tag(home_html, "div", 'data-elementor-type="footer"')
    # Extract popup
    popup_html = extract_nested_tag(home_html, "div", 'data-elementor-type="popup"')

    # Save globals
    globals_dir = "data/globals"
    os.makedirs(globals_dir, exist_ok=True)
    with open(os.path.join(globals_dir, "header.html"), "w", encoding="utf-8") as f:
        f.write(header_html)
    with open(os.path.join(globals_dir, "footer.html"), "w", encoding="utf-8") as f:
        f.write(footer_html)
    with open(os.path.join(globals_dir, "popup.html"), "w", encoding="utf-8") as f:
        f.write(popup_html)
    
    print("Global layout components extracted successfully!")

    # Iterate files
    parsed_pages = {}
    
    # 1. Handle Homepage
    homepage_canonical = "https://atlasmentor.com/"
    parsed_home = parse_html_page(homepage_file, homepage_canonical)
    if parsed_home:
        with open(os.path.join(pages_data_dir, "index.json"), "w", encoding="utf-8") as out_f:
            json.dump(parsed_home, out_f, indent=2)
        parsed_pages["index"] = "index.html"

    # 2. Walk directories for subpages
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Exclude system folders
        rel_dir = os.path.relpath(dirpath, root_dir)
        if rel_dir == "." or any(x in rel_dir for x in ["wp-includes", "wp-content", "wp-json", "comments", "feed"]):
            continue
            
        for filename in filenames:
            if filename == "index.html":
                filepath = os.path.join(dirpath, filename)
                slug = rel_dir
                
                clean_canonical = f"https://atlasmentor.com/{slug}/"
                parsed = parse_html_page(filepath, clean_canonical)
                if not parsed:
                    continue
                
                parsed_pages[slug] = os.path.join(rel_dir, filename)
                
                # If slug has folders, create directory inside data/pages
                slug_dir = os.path.dirname(os.path.join(pages_data_dir, slug))
                os.makedirs(slug_dir, exist_ok=True)
                
                page_data_file = os.path.join(pages_data_dir, f"{slug}.json")
                with open(page_data_file, "w", encoding="utf-8") as out_f:
                    json.dump(parsed, out_f, indent=2)

    print(f"Processed {len(parsed_pages)} unique pages successfully!")

if __name__ == "__main__":
    main()

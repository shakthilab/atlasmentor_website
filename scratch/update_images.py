import json
import re
import os

def replace_img_tags(html):
    keywords = ['Namangan', 'Khiva', 'Navoi', 'Bukhara & Samarkand', 'Qarshi', 'Guliston']
    
    def replacer(match):
        img_tag = match.group(0)
        if any(kw in img_tag for kw in keywords):
            # Replace src attribute
            new_tag = re.sub(r'src=\"[^\"]+\"', 'src="../wp-content/uploads/2025/02/Study-MBBS-in-Uzbekistan.png"', img_tag)
            # Remove srcset attribute
            new_tag = re.sub(r'\s+srcset=\"[^\"]+\"', '', new_tag)
            return new_tag
        return img_tag
        
    return re.sub(r'<img[^>]+>', replacer, html)

def process_file(fpath):
    print(f"Processing {fpath}...")
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    body = data.get('body', '')
    new_body = replace_img_tags(body)
    
    if new_body != body:
        data['body'] = new_body
        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Updated {fpath}")
    else:
        print(f"No changes in {fpath}")

if __name__ == '__main__':
    files = [
        'data/pages/study-mbbs-in-uzbekistan-for-indian-students.json',
        'data/pages/namangan-state-medical-university.json',
        'data/pages/mamun-university.json',
        'data/pages/navoi-state-medical-university.json',
        'data/pages/zarmed-university.json',
        'data/pages/karshi-state-medical-university.json',
        'data/pages/gulistan-state-medical-university.json'
    ]
    for f in files:
        process_file(f)

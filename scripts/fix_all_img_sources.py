import json
import re

geo_slugs = [
    'caucasus-university',
    'caucasus-international-university',
    'east-european-university',
    'european-university',
    'kutaisi-university',
    'tbilisi-state-medical-university'
]

uzb_slugs = [
    'namangan-state-medical-university',
    'mamun-university',
    'navoi-state-medical-university',
    'zarmed-university',
    'karshi-state-medical-university',
    'gulistan-state-medical-university'
]

def fix_images(slug, default_img):
    filepath = f'data/pages/{slug}.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    body = data['body']

    # Replace any broken src or srcset attributes in img tags
    def img_replacer(match):
        img_tag = match.group(0)
        # If image is logo or icon, keep it
        if 'Atlas-Mentor-Circle' in img_tag or 'icon' in img_tag or 'avatar' in img_tag:
            return img_tag
        
        # Replace src attribute with default valid country image
        new_tag = re.sub(r'src=\"[^\"]+\"', f'src="../..{default_img}"', img_tag)
        # Remove srcset attribute to prevent missing srcset errors
        new_tag = re.sub(r'\s+srcset=\"[^\"]+\"', '', new_tag)
        return new_tag

    new_body = re.sub(r'<img[^>]+>', img_replacer, body)

    if new_body != body:
        data['body'] = new_body
        with open(filepath, 'w', encoding='utf-8') as f_out:
            json.dump(data, f_out, indent=2, ensure_ascii=False)
        print(f"Successfully cleaned image tags in {filepath}")

if __name__ == '__main__':
    for slug in geo_slugs:
        fix_images(slug, '/wp-content/uploads/2025/02/Study-MBBS-in-Georgia.png')
    for slug in uzb_slugs:
        fix_images(slug, '/wp-content/uploads/2025/02/Study-MBBS-in-Uzbekistan.png')

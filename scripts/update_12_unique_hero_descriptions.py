import json
import re

descriptions = {
    # Georgia Universities
    "caucasus-university": "Founded in partnership with Georgia State University (USA), Caucasus University in Tbilisi features state-of-the-art 3D virtual anatomy labs, OSCE simulation suites, and high FMGE & USMLE pass rates for Indian medical aspirants.",
    "caucasus-international-university": "Established in 1995, Caucasus International University (CIU) in Tbilisi is home to students from over 40 countries, featuring world-class phantom simulation centers and bedside clinical clerkships across leading Georgian university hospitals.",
    "east-european-university": "Located in Tbilisi, East European University (EEU) boasts an eco-friendly smart green campus, WFME accreditation, problem-based learning (PBL) modules, and structured USMLE/NExT coaching for Indian students.",
    "european-university": "European University in Tbilisi stands out by owning and operating its own super-specialty teaching facility, Jo Ann University Hospital, offering direct hands-on clinical rotations in cardiology, surgery, and emergency care.",
    "kutaisi-university": "As the first private higher education institution established in Georgia (1991), Kutaisi University (UNIK) offers top-tier European medical education at highly affordable tuition fees with a 30-40% lower cost of living in Kutaisi.",
    "tbilisi-state-medical-university": "Established in 1918, Tbilisi State Medical University (TSMU) is the premier flagship public medical university in the Caucasus region, featuring century-old academic prestige, Emory University US exchange programs, and top FMGE pass rates.",

    # Uzbekistan Universities
    "namangan-state-medical-university": "Situated in the vibrant city of Namangan, Namangan State Medical University offers modern digital anatomy dissection labs, extensive bedside rotations in municipal teaching hospitals, and low tuition fees of $3,500 USD/year.",
    "mamun-university": "Named after the historic 11th-century Mamun Academy of Khwarazm, Mamun University in Khiva offers modern medical simulation facilities, small-group clinical clerkships, and rich cultural student heritage.",
    "navoi-state-medical-university": "Navoi State Medical University is a high-tech state institution featuring clinical skill simulation centers, 3D anatomical dissection tables, and extensive bedside patient exposure across regional state hospitals in Navoi.",
    "zarmed-university": "Zarmed University is a premier private medical institution with state-of-the-art campuses in both Bukhara and Samarkand, featuring Zarmed's own affiliated multi-specialty hospitals and robotic mannequin simulation suites.",
    "karshi-state-medical-university": "Located in the Kashkadarya region, Karshi State Medical University offers affordable European-standard medical education, high patient inflow during clinical rotations, and secure campus hostels with Indian mess facilities.",
    "gulistan-state-medical-university": "Located in the Syrdarya region, Gulistan State Medical University provides high-quality 6-year English-medium medical training with advanced pre-clinical laboratories, dedicated faculty mentorship, and low living expenses."
}

def update_hero_description(slug, text):
    filepath = f"data/pages/{slug}.json"
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    body = data['body']

    # Replace elementor-image-box-description content
    pattern = r'(<p class="elementor-image-box-description">)([\s\S]*?)(</p>)'
    match = re.search(pattern, body)
    if match:
        new_body = body[:match.start(2)] + text + body[match.end(2):]
        data['body'] = new_body
        with open(filepath, 'w', encoding='utf-8') as f_out:
            json.dump(data, f_out, indent=2, ensure_ascii=False)
        print(f"Successfully updated unique hero description in {filepath}")
    else:
        print(f"Failed to locate elementor-image-box-description in {filepath}")

if __name__ == '__main__':
    for slug, text in descriptions.items():
        update_hero_description(slug, text)

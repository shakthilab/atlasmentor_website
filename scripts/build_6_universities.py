import json
import re

def generate():
    with open('data/pages/andijan-state-medical-institute-ranking.json', 'r', encoding='utf8') as f:
        andijan_data = json.load(f)

    base_body = andijan_data['body']

    # Locate Table 1 and Table 2 bounds precisely in base_body
    t1_start = base_body.find('<table><tbody><tr><td>Year of Establishment</td>')
    t1_end = base_body.find('</table>', t1_start) + len('</table>')

    t2_start = base_body.find('<table>\n<tbody>\n<tr>\n<th>Particulars</th>')
    if t2_start == -1:
        t2_start = base_body.find('<table>\n<tbody>\n<tr><th>Particulars</th>')
    if t2_start == -1:
        t2_start = base_body.find('<table><tbody><tr><th>Particulars</th>')
    t2_end = base_body.find('</table>', t2_start) + len('</table>')

    universities = [
        {
            "slug": "namangan-state-medical-university",
            "full_name": "Namangan State Medical University",
            "short_name": "Namangan State Medical University",
            "city": "Namangan",
            "established": "1942",
            "type": "Government / Public",
            "tuition_yr": "3,200 USD",
            "hostel_yr": "600 USD",
            "y1_t": "3,200 USD", "y2_t": "3,200 USD", "y3_t": "3,200 USD", "y4_t": "3,200 USD", "y5_t": "3,200 USD", "y6_t": "3,200 USD",
            "y1_h": "600 USD", "y2_h": "600 USD", "y3_h": "600 USD", "y4_h": "600 USD", "y5_h": "600 USD", "y6_h": "600 USD",
            "y1_tot": "3,800 USD", "y2_tot": "3,800 USD", "y3_tot": "3,800 USD", "y4_tot": "3,800 USD", "y5_tot": "3,800 USD", "y6_tot": "3,800 USD",
            "img": "/wp-content/uploads/2024/07/Uzbekistan.jpg",
            "faqs": [
                ("Is it necessary to take NEET in order to get admission into Namangan State Medical University?", "Yes, Namangan State Medical University requires students to have a NEET score for admission into the MBBS Program."),
                ("What is medium of instruction at Namangan State Medical University?", "The medium of instruction is English, making it easy for international students to understand and follow the medical curriculum."),
                ("Is there any other entrance examination apart from the NEET for admission into MBBS?", "No. There is no other noted examination in Namangan State Medical University, admission is allowed based on the NEET results and IQ tests conducted."),
                ("Is Namangan State Medical University a school of good standing and reputation internationally?", "Yes, the institute is recognized by the WHO and NMC and therefore the medical degree obtained is accepted in many other countries."),
                ("What are the hostel facilities like at Namangan State Medical University?", "The institute provides comfortable accommodation to international students in well furnished hostel rooms with essential Wi-Fi facilities and air conditioning.")
            ]
        },
        {
            "slug": "mamun-university",
            "full_name": "Mamun University",
            "short_name": "Mamun University",
            "city": "Khiva",
            "established": "2020",
            "type": "Private",
            "tuition_yr": "3,000 USD",
            "hostel_yr": "600 USD",
            "y1_t": "3,000 USD", "y2_t": "3,000 USD", "y3_t": "3,000 USD", "y4_t": "3,000 USD", "y5_t": "3,000 USD", "y6_t": "3,000 USD",
            "y1_h": "600 USD", "y2_h": "600 USD", "y3_h": "600 USD", "y4_h": "600 USD", "y5_h": "600 USD", "y6_h": "600 USD",
            "y1_tot": "3,600 USD", "y2_tot": "3,600 USD", "y3_tot": "3,600 USD", "y4_tot": "3,600 USD", "y5_tot": "3,600 USD", "y6_tot": "3,600 USD",
            "img": "/wp-content/uploads/2024/07/Uzbekistan.jpg",
            "faqs": [
                ("Is it necessary to take NEET in order to get admission into Mamun University?", "Yes, Mamun University requires students to have a NEET score for admission into the MBBS Program."),
                ("What is medium of instruction at Mamun University?", "The medium of instruction is English, making it easy for international students to understand and follow the medical curriculum."),
                ("Is there any other entrance examination apart from the NEET for admission into MBBS?", "No. There is no other noted examination in Mamun University, admission is allowed based on the NEET results and IQ tests conducted."),
                ("Is Mamun University a school of good standing and reputation internationally?", "Yes, the institute is recognized by the WHO and NMC and therefore the medical degree obtained is accepted in many other countries."),
                ("What are the hostel facilities like at Mamun University?", "The institute provides comfortable accommodation to international students in well furnished hostel rooms with essential Wi-Fi facilities and air conditioning.")
            ]
        },
        {
            "slug": "navoi-state-medical-university",
            "full_name": "Navoi State Medical University",
            "short_name": "Navoi State Medical University",
            "city": "Navoi",
            "established": "Public State Institution",
            "type": "Government / Public",
            "tuition_yr": "3,200 USD",
            "hostel_yr": "600 USD",
            "y1_t": "3,200 USD", "y2_t": "3,200 USD", "y3_t": "3,200 USD", "y4_t": "3,200 USD", "y5_t": "3,200 USD", "y6_t": "3,200 USD",
            "y1_h": "600 USD", "y2_h": "600 USD", "y3_h": "600 USD", "y4_h": "600 USD", "y5_h": "600 USD", "y6_h": "600 USD",
            "y1_tot": "3,800 USD", "y2_tot": "3,800 USD", "y3_tot": "3,800 USD", "y4_tot": "3,800 USD", "y5_tot": "3,800 USD", "y6_tot": "3,800 USD",
            "img": "/wp-content/uploads/2024/07/Uzbekistan.jpg",
            "faqs": [
                ("Is it necessary to take NEET in order to get admission into Navoi State Medical University?", "Yes, Navoi State Medical University requires students to have a NEET score for admission into the MBBS Program."),
                ("What is medium of instruction at Navoi State Medical University?", "The medium of instruction is English, making it easy for international students to understand and follow the medical curriculum."),
                ("Is there any other entrance examination apart from the NEET for admission into MBBS?", "No. There is no other noted examination in Navoi State Medical University, admission is allowed based on the NEET results and IQ tests conducted."),
                ("Is Navoi State Medical University a school of good standing and reputation internationally?", "Yes, the institute is recognized by the WHO and NMC and therefore the medical degree obtained is accepted in many other countries."),
                ("What are the hostel facilities like at Navoi State Medical University?", "The institute provides comfortable accommodation to international students in well furnished hostel rooms with essential Wi-Fi facilities and air conditioning.")
            ]
        },
        {
            "slug": "zarmed-university",
            "full_name": "Zarmed University",
            "short_name": "Zarmed University",
            "city": "Bukhara & Samarkand",
            "established": "2020",
            "type": "Private",
            "tuition_yr": "2,800 USD",
            "hostel_yr": "600 USD",
            "y1_t": "2,800 USD", "y2_t": "2,800 USD", "y3_t": "2,800 USD", "y4_t": "2,800 USD", "y5_t": "2,800 USD", "y6_t": "2,800 USD",
            "y1_h": "600 USD", "y2_h": "600 USD", "y3_h": "600 USD", "y4_h": "600 USD", "y5_h": "600 USD", "y6_h": "600 USD",
            "y1_tot": "3,400 USD", "y2_tot": "3,400 USD", "y3_tot": "3,400 USD", "y4_tot": "3,400 USD", "y5_tot": "3,400 USD", "y6_tot": "3,400 USD",
            "img": "/wp-content/uploads/2024/07/Uzbekistan.jpg",
            "faqs": [
                ("Is it necessary to take NEET in order to get admission into Zarmed University?", "Yes, Zarmed University requires students to have a NEET score for admission into the MBBS Program."),
                ("What is medium of instruction at Zarmed University?", "The medium of instruction is English, making it easy for international students to understand and follow the medical curriculum."),
                ("Is there any other entrance examination apart from the NEET for admission into MBBS?", "No. There is no other noted examination in Zarmed University, admission is allowed based on the NEET results and IQ tests conducted."),
                ("Is Zarmed University a school of good standing and reputation internationally?", "Yes, the institute is recognized by the WHO and NMC and therefore the medical degree obtained is accepted in many other countries."),
                ("What are the hostel facilities like at Zarmed University?", "The institute provides comfortable accommodation to international students in well furnished hostel rooms with essential Wi-Fi facilities and air conditioning.")
            ]
        },
        {
            "slug": "karshi-state-medical-university",
            "full_name": "Karshi State Medical University",
            "short_name": "Karshi State Medical University",
            "city": "Qarshi",
            "established": "2020 (Presidential Decree)",
            "type": "Government / Public",
            "tuition_yr": "3,500 USD",
            "hostel_yr": "600 USD",
            "y1_t": "3,500 USD", "y2_t": "3,500 USD", "y3_t": "3,500 USD", "y4_t": "3,500 USD", "y5_t": "3,500 USD", "y6_t": "3,500 USD",
            "y1_h": "600 USD", "y2_h": "600 USD", "y3_h": "600 USD", "y4_h": "600 USD", "y5_h": "600 USD", "y6_h": "600 USD",
            "y1_tot": "4,100 USD", "y2_tot": "4,100 USD", "y3_tot": "4,100 USD", "y4_tot": "4,100 USD", "y5_tot": "4,100 USD", "y6_tot": "4,100 USD",
            "img": "/wp-content/uploads/2024/07/Uzbekistan.jpg",
            "faqs": [
                ("Is it necessary to take NEET in order to get admission into Karshi State Medical University?", "Yes, Karshi State Medical University requires students to have a NEET score for admission into the MBBS Program."),
                ("What is medium of instruction at Karshi State Medical University?", "The medium of instruction is English, making it easy for international students to understand and follow the medical curriculum."),
                ("Is there any other entrance examination apart from the NEET for admission into MBBS?", "No. There is no other noted examination in Karshi State Medical University, admission is allowed based on the NEET results and IQ tests conducted."),
                ("Is Karshi State Medical University a school of good standing and reputation internationally?", "Yes, the institute is recognized by the WHO and NMC and therefore the medical degree obtained is accepted in many other countries."),
                ("What are the hostel facilities like at Karshi State Medical University?", "The institute provides comfortable accommodation to international students in well furnished hostel rooms with essential Wi-Fi facilities and air conditioning.")
            ]
        },
        {
            "slug": "gulistan-state-medical-university",
            "full_name": "Gulistan State Medical University",
            "short_name": "Gulistan State Medical University",
            "city": "Guliston",
            "established": "1965",
            "type": "Government / Public",
            "tuition_yr": "3,500 USD",
            "hostel_yr": "600 USD",
            "y1_t": "3,500 USD", "y2_t": "3,500 USD", "y3_t": "3,500 USD", "y4_t": "3,500 USD", "y5_t": "3,500 USD", "y6_t": "3,500 USD",
            "y1_h": "600 USD", "y2_h": "600 USD", "y3_h": "600 USD", "y4_h": "600 USD", "y5_h": "600 USD", "y6_h": "600 USD",
            "y1_tot": "4,100 USD", "y2_tot": "4,100 USD", "y3_tot": "4,100 USD", "y4_tot": "4,100 USD", "y5_tot": "4,100 USD", "y6_tot": "4,100 USD",
            "img": "/wp-content/uploads/2024/07/Uzbekistan.jpg",
            "faqs": [
                ("Is it necessary to take NEET in order to get admission into Gulistan State Medical University?", "Yes, Gulistan State Medical University requires students to have a NEET score for admission into the MBBS Program."),
                ("What is medium of instruction at Gulistan State Medical University?", "The medium of instruction is English, making it easy for international students to understand and follow the medical curriculum."),
                ("Is there any other entrance examination apart from the NEET for admission into MBBS?", "No. There is no other noted examination in Gulistan State Medical University, admission is allowed based on the NEET results and IQ tests conducted."),
                ("Is Gulistan State Medical University a school of good standing and reputation internationally?", "Yes, the institute is recognized by the WHO and NMC and therefore the medical degree obtained is accepted in many other countries."),
                ("What are the hostel facilities like at Gulistan State Medical University?", "The institute provides comfortable accommodation to international students in well furnished hostel rooms with essential Wi-Fi facilities and air conditioning.")
            ]
        }
    ]

    for u in universities:
        # Construct Table 1 replacement HTML
        new_tbl1 = f"""<table><tbody><tr><td>Year of Establishment</td><td>{u['established']}</td></tr><tr><td>Type</td><td>{u['type']}</td></tr><tr><td>Recognition</td><td>NMC and WHO approved</td></tr><tr><td>Eligibility</td><td>50% in Physics, Chemistry, Biology in 12th + NEET qualified</td></tr><tr><td>Course Duration</td><td>5 + 1 Year Internship</td></tr><tr><td>NEET Required</td><td>Yes</td></tr><tr><td>Medium of Teaching</td><td>English</td></tr><tr><td>Ranking</td><td>Top Medical Institution in {u['city']}, Uzbekistan</td></tr></tbody></table>"""

        # Construct Table 2 replacement HTML
        new_tbl2 = f"""<table><tbody><tr><th>Particulars</th><th>Year 1</th><th>Year 2</th><th>Year 3</th><th>Year 4</th><th>Year 5</th><th>Year 6</th></tr><tr><td>Tuition Fee</td><td>{u['y1_t']}</td><td>{u['y2_t']}</td><td>{u['y3_t']}</td><td>{u['y4_t']}</td><td>{u['y5_t']}</td><td>{u['y6_t']}</td></tr><tr><td>Hostel Fee</td><td>{u['y1_h']}</td><td>{u['y2_h']}</td><td>{u['y3_h']}</td><td>{u['y4_h']}</td><td>{u['y5_h']}</td><td>{u['y6_h']}</td></tr><tr><td>Total (USD)</td><td>{u['y1_tot']}</td><td>{u['y2_tot']}</td><td>{u['y3_tot']}</td><td>{u['y4_tot']}</td><td>{u['y5_tot']}</td><td>{u['y6_tot']}</td></tr></tbody></table>"""

        # Build body using slice replacement for tables
        body = base_body[:t1_start] + new_tbl1 + base_body[t1_end:t2_start] + new_tbl2 + base_body[t2_end:]

        # Text substitutions
        body = body.replace("Andijan State Medical Institute Ranking, Uzbekistan", f"{u['full_name']} Ranking, Uzbekistan")
        body = body.replace("Andijan State Medical Institute", u['full_name'])
        body = body.replace("Andijan Medical Institute", u['short_name'])
        body = body.replace("Andijan", u['city'])

        # Image Replacements
        body = body.replace("../wp-content/uploads/2025/01/Andijan-State-Medical-Institute.jpg", u['img'])
        body = body.replace("../wp-content/uploads/2025/01/Andijan-State-Medical-Institute-1.jpg", u['img'])
        body = body.replace("../wp-content/uploads/2025/01/Facilities-At-Andijan-State-Medical-Institute.jpg", u['img'])
        body = body.replace("../wp-content/uploads/2025/01/Student-Life-At-Andijan-State-Medical-Institute.jpg", u['img'])
        body = body.replace("../wp-content/uploads/2025/01/FAQs-on-Andijan-State-Medical-Institute.jpg", u['img'])
        body = body.replace("https://atlasmentor.com/wp-content/uploads/2025/01/Andijan-State-Medical-Institute.jpg", f"https://atlasmentor.com{u['img']}")

        # Build FAQ Cards HTML matching exact ElementsKit structure
        all_cards_html = ""
        for idx, (q, a) in enumerate(u['faqs']):
            card_id = f"Collapse-{u['slug']}-{idx}"
            heading_id = f"primaryHeading-{idx}-{u['slug']}"
            all_cards_html += f"""<div class="elementskit-card {'active' if idx == 0 else ''}">
                    <div class="elementskit-card-header" id="{heading_id}">
                        <a href="#{card_id}" class="ekit-accordion--toggler elementskit-btn-link {'collapsed' if idx != 0 else ''}" data-ekit-toggle="collapse" data-target="#{card_id}" aria-expanded="{'true' if idx == 0 else 'false'}" aria-controls="{card_id}">
                                                            <div class="ekit_accordion_icon_left_group">
                                    <div class="ekit_accordion_normal_icon">
                                        <!-- Normal Icon -->
                                        <i class="mdi mdi-plus"></i>
                        </div>

                                    <div class="ekit_accordion_active_icon">
                                        <!-- Active Icon -->
                                                                               <i class="icofont icofont-minus"></i>                                    </div>
                                </div>


                            <span class="ekit-accordion-title">{q}</span>


                                                    </a>
                    </div>

                    <div id="{card_id}" class="{'show' if idx == 0 else ''} collapse" aria-labelledby="{heading_id}">

                        <div class="elementskit-card-body ekit-accordion--content">
                            <p>{a}</p>                        </div>

                    </div>

                </div><!-- .elementskit-card END -->\n"""

        # Replace inner FAQ accordion HTML
        body = re.sub(
            r'(<div class=\"elementskit-accordion accoedion-primary\" id=\"accordion-[^\"]*\">)(.*?)(</div>\s*</div>\s*</div>\s*</div>\s*<div class=\"elementor-element elementor-element-1f78451)',
            r'\g<1>\n' + all_cards_html + r'\g<3>',
            body,
            flags=re.DOTALL
        )

        out_json = {
            "title": f"{u['full_name']} MBBS Fees 2026, Uzbekistan",
            "description": f"{u['full_name']} MBBS fees & admission 2026-27 — free, verified guidance for Indian students from Atlas Mentor.",
            "canonical": f"https://atlasmentor.com/{u['slug']}/",
            "robots": "max-image-preview:large",
            "stylesheets": andijan_data.get("stylesheets", []),
            "body": body
        }

        out_path = f"data/pages/{u['slug']}.json"
        with open(out_path, 'w', encoding='utf8') as fp:
            json.dump(out_json, fp, indent=2, ensure_ascii=False)
        print(f"Generated {out_path}")

if __name__ == '__main__':
    generate()

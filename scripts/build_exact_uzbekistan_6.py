import json
import re

def build_exact_uzbekistan_pages():
    # Load Andijan template JSON as the exact layout reference
    with open('data/pages/andijan-state-medical-institute-ranking.json', 'r', encoding='utf-8') as f:
        andijan_data = json.load(f)

    template_body = andijan_data['body']

    universities = [
        {
            "slug": "namangan-state-medical-university",
            "full_name": "Namangan State Medical University",
            "short_name": "Namangan State Medical University",
            "city": "Namangan",
            "established": "2020",
            "type": "Public / State Medical University",
            "ranking": "Top Rated State Medical University in Namangan, Uzbekistan",
            "tuition_yr": "3,500 USD",
            "hostel_yr": "800 USD",
            "tuition_val": 3500,
            "hostel_val": 800,
            "img": "/wp-content/uploads/2025/02/Study-MBBS-in-Uzbekistan.png",
            "description": "Namangan State Medical University Uzbekistan MBBS fees, eligibility & admission 2026. NMC & WHO recognized 6-year English medium medical degree.",
            "overview_p1": "Namangan State Medical University is a modern higher medical education institution located in the vibrant city of Namangan, Uzbekistan. Established to meet the growing demand for world-class medical professionals, the university offers a 6-year Medical Doctor (MD / MBBS equivalent) program taught 100% in English for international students.",
            "overview_p2": "The university features contemporary lecture halls, advanced biomedical laboratories, digital anatomical dissection facilities, and simulation skill centers. Students receive rigorous grounding in basic medical sciences followed by extensive clinical postings in municipal and regional teaching hospitals across Namangan.",
            "overview_p3": "For Indian students, Namangan State Medical University provides an affordable, high-quality pathway to a recognized European-standard medical degree. The university is registered in WHO (WDOMS) and fully complies with NMC (India) Foreign Medical Graduate Licentiate regulations.",
            "faqs": [
                ("Is Namangan State Medical University recognized by NMC and WHO?", "Yes, Namangan State Medical University is listed in WDOMS, recognized by WHO, and fully complies with NMC FMGL Regulations 2021 for Indian students."),
                ("What is the tuition fee for MBBS at Namangan State Medical University?", "The annual tuition fee at Namangan State Medical University is approximately 3,500 USD per year."),
                ("Is the MBBS course taught in English at Namangan State Medical University?", "Yes, the entire 6-year MD program is delivered 100% in English for international students."),
                ("Are NEET scores required for admission to Namangan State Medical University?", "Yes, NEET qualification is mandatory for Indian students to secure admission and practice in India upon graduation."),
                ("Are hostel and Indian food facilities available at Namangan State Medical University?", "Yes, the university provides secure hostel accommodation with high-speed Wi-Fi, heating, 24/7 security, and dedicated Indian mess services serving veg and non-veg meals.")
            ]
        },
        {
            "slug": "mamun-university",
            "full_name": "Mamun University",
            "short_name": "Mamun University",
            "city": "Khiva",
            "established": "2022",
            "type": "Private University",
            "ranking": "Top Private University in Khiva, Uzbekistan",
            "tuition_yr": "3,200 USD",
            "hostel_yr": "700 USD",
            "tuition_val": 3200,
            "hostel_val": 700,
            "img": "/wp-content/uploads/2025/02/Study-MBBS-in-Uzbekistan.png",
            "description": "Mamun University Khiva Uzbekistan MBBS fees & admission 2026. Affordable tuition, NMC/WHO approved 6-year English medium MD program.",
            "overview_p1": "Mamun University, located in the historic city of Khiva, Uzbekistan, is a progressive private university dedicated to excellence in international medical education. Named after the legendary medieval Mamun Academy of Khwarazm, the university offers a 6-year English-medium Medical Doctor (MD / MBBS) degree.",
            "overview_p2": "The campus is equipped with smart classrooms, modern clinical simulation laboratories, digital anatomical dissection suites, and research facilities. Practical clinical clerkships are conducted in top multi-specialty hospitals in Khiva and Urgench under expert faculty supervision.",
            "overview_p3": "Recognized by WHO (WDOMS) and compliant with NMC regulations, Mamun University offers Indian medical aspirants an affordable, high-standard medical education with safe hostel accommodation and dedicated Indian mess services.",
            "faqs": [
                ("Is Mamun University approved by WHO and NMC?", "Yes, Mamun University is listed in WDOMS and recognized by WHO and NMC for Indian medical students."),
                ("What are the annual tuition fees at Mamun University?", "The annual tuition fee at Mamun University is 3,200 USD per year."),
                ("Where is Mamun University located?", "Mamun University is situated in Khiva, Uzbekistan, offering a safe and culturally rich academic environment."),
                ("Is NEET required for MBBS at Mamun University?", "Yes, qualifying NEET is compulsory for Indian students to gain admission."),
                ("Does Mamun University offer Indian food in hostels?", "Yes, hostels provide clean dining halls offering authentic Indian vegetarian and non-vegetarian meals daily.")
            ]
        },
        {
            "slug": "navoi-state-medical-university",
            "full_name": "Navoi State Medical University",
            "short_name": "Navoi State Medical University",
            "city": "Navoi",
            "established": "2021",
            "type": "State Medical University",
            "ranking": "Leading State Medical University in Navoi, Uzbekistan",
            "tuition_yr": "3,400 USD",
            "hostel_yr": "750 USD",
            "tuition_val": 3400,
            "hostel_val": 750,
            "img": "/wp-content/uploads/2025/02/Study-MBBS-in-Uzbekistan.png",
            "description": "Navoi State Medical University Uzbekistan MBBS fees, eligibility & admission 2026. NMC & WHO recognized 6-year English medium MD program.",
            "overview_p1": "Navoi State Medical University is a premier state medical institution located in Navoi, Uzbekistan. Built to advance healthcare education in central Uzbekistan, the university delivers an accredited 6-year English-medium MD / MBBS program tailored for global medical aspirants.",
            "overview_p2": "The university houses cutting-edge clinical skill simulation centers, histology and pathology labs, 3D digital dissection tables, and modern libraries. Students gain extensive bedside patient exposure through clinical rotations across affiliated state hospitals in Navoi region.",
            "overview_p3": "Navoi State Medical University is WHO listed and NMC compliant, making its graduates eligible for NExT / FMGE licensing exams in India as well as international licensure pathways including USMLE and PLAB.",
            "faqs": [
                ("Is Navoi State Medical University recognized by NMC India?", "Yes, Navoi State Medical University is recognized by NMC (India) and WHO (WDOMS)."),
                ("What is the cost of studying MBBS at Navoi State Medical University?", "Tuition fee is 3,400 USD per year, with hostel accommodation averaging 750 USD per year."),
                ("What is the duration of MBBS at Navoi State Medical University?", "The course duration is 6 years, including 5 years of academic study and 1 year of compulsory internship."),
                ("What is the medium of teaching at Navoi State Medical University?", "The entire 6-year medical program is conducted 100% in English."),
                ("Are hostels safe for Indian students at Navoi State Medical University?", "Yes, university hostels offer 24/7 security, biometric access, heating, Wi-Fi, and Indian mess services.")
            ]
        },
        {
            "slug": "zarmed-university",
            "full_name": "Zarmed University",
            "short_name": "Zarmed University",
            "city": "Bukhara & Samarkand",
            "established": "2020",
            "type": "Private Medical University",
            "ranking": "Top Private Medical University in Bukhara & Samarkand",
            "tuition_yr": "3,500 USD",
            "hostel_yr": "800 USD",
            "tuition_val": 3500,
            "hostel_val": 800,
            "img": "/wp-content/uploads/2025/02/Study-MBBS-in-Uzbekistan.png",
            "description": "Zarmed University Uzbekistan MBBS admission 2026. Campuses in Bukhara & Samarkand, 100% English medium, NMC/WHO approved, top facilities.",
            "overview_p1": "Zarmed University is a leading private medical university in Uzbekistan with modern campuses in Bukhara and Samarkand. Founded in 2020, Zarmed University delivers an internationally accredited 6-year Medical Doctor (MD / MBBS equivalent) program taught 100% in English.",
            "overview_p2": "Zarmed University features high-tech academic infrastructure, including state-of-the-art simulation laboratories, robotic mannequins, digital virtual dissection tables, and comprehensive electronic learning management platforms. Clinical clerkships take place in Zarmed's own affiliated medical centers and teaching hospitals.",
            "overview_p3": "Fully recognized by WHO (WDOMS) and compliant with NMC FMGL 2021 regulations, Zarmed University provides Indian students with high quality education, comfortable campus hostels, Indian food options, and active guidance for FMGE/NExT and USMLE examinations.",
            "faqs": [
                ("Is Zarmed University recognized by WHO and NMC?", "Yes, Zarmed University is listed in WDOMS and recognized by WHO and NMC (India)."),
                ("Where are Zarmed University campuses located?", "Zarmed University operates state-of-the-art medical campuses in Bukhara and Samarkand, Uzbekistan."),
                ("What is the annual tuition fee at Zarmed University?", "The annual tuition fee at Zarmed University is 3,500 USD per year."),
                ("Does Zarmed University offer 100% English medium instruction?", "Yes, all lectures, practicals, clinical clerkships, and exams are conducted in English."),
                ("What hostel facilities are provided for international students at Zarmed University?", "Zarmed University provides modern hostel rooms equipped with central heating, Wi-Fi, 24/7 security, and Indian dining halls serving fresh veg and non-veg meals.")
            ]
        },
        {
            "slug": "karshi-state-medical-university",
            "full_name": "Karshi State Medical University",
            "short_name": "Karshi State Medical University",
            "city": "Karshi",
            "established": "2021",
            "type": "State Medical University",
            "ranking": "Top State Medical Institution in Karshi, Uzbekistan",
            "tuition_yr": "3,300 USD",
            "hostel_yr": "750 USD",
            "tuition_val": 3300,
            "hostel_val": 750,
            "img": "/wp-content/uploads/2025/02/Study-MBBS-in-Uzbekistan.png",
            "description": "Karshi State Medical University Uzbekistan MBBS fees & admission 2026. NMC & WHO recognized 6-year English medium MD course for Indian aspirants.",
            "overview_p1": "Karshi State Medical University is a state higher education institution situated in Karshi, Kashkadarya region, Uzbekistan. The university offers an accredited 6-year English-medium MD / MBBS program designed according to international medical education standards.",
            "overview_p2": "The modern campus features state-of-the-art simulation labs, research centers, digital libraries, and comfortable student spaces. Clinical postings begin in the third year across major regional multi-profile hospitals in Karshi.",
            "overview_p3": "Listed in WHO WDOMS and recognized by NMC India, Karshi State Medical University offers an ideal balance of quality medical education, low tuition fees, safe hostel living, and Indian dining facilities.",
            "faqs": [
                ("Is Karshi State Medical University approved by NMC India?", "Yes, Karshi State Medical University is recognized by NMC and WHO."),
                ("What is the tuition fee for MBBS at Karshi State Medical University?", "The tuition fee is 3,300 USD per year, with hostel fees of 750 USD per year."),
                ("What is the medium of instruction at Karshi State Medical University?", "The program is taught 100% in English for international students."),
                ("What documents are required for admission at Karshi State Medical University?", "Required documents include 10th & 12th marksheets, passport copy, NEET scorecard, birth certificate, and medical fitness certificate."),
                ("Is Indian food available in Karshi State Medical University hostels?", "Yes, hostels provide Indian mess facilities serving nutritious Indian food.")
            ]
        },
        {
            "slug": "gulistan-state-medical-university",
            "full_name": "Gulistan State Medical University",
            "short_name": "Gulistan State Medical University",
            "city": "Gulistan",
            "established": "2022",
            "type": "State Medical University",
            "ranking": "Top State Medical University in Gulistan, Uzbekistan",
            "tuition_yr": "3,200 USD",
            "hostel_yr": "700 USD",
            "tuition_val": 3200,
            "hostel_val": 700,
            "img": "/wp-content/uploads/2025/02/Study-MBBS-in-Uzbekistan.png",
            "description": "Gulistan State Medical University Uzbekistan MBBS fees, eligibility & admission 2026. NMC & WHO approved 6-year English medium MD degree.",
            "overview_p1": "Gulistan State Medical University is a state medical university located in Gulistan, Syrdarya region, Uzbekistan. The university provides an accredited 6-year English-medium Medical Doctor (MD / MBBS) course for international students.",
            "overview_p2": "Equipped with modern simulation suites, digital anatomy laboratories, interactive lecture halls, and extensive library resources, the university provides strong pre-clinical and clinical medical training in affiliated regional hospitals.",
            "overview_p3": "Fully recognized by WHO (WDOMS) and compliant with NMC guidelines, Gulistan State Medical University offers Indian medical aspirants affordable medical education, comfortable hostel accommodation, and dedicated student support.",
            "faqs": [
                ("Is Gulistan State Medical University recognized by WHO and NMC?", "Yes, Gulistan State Medical University is listed in WDOMS and recognized by WHO and NMC."),
                ("What is the tuition fee for MBBS at Gulistan State Medical University?", "The annual tuition fee is 3,200 USD per year."),
                ("Is NEET mandatory for Indian students at Gulistan State Medical University?", "Yes, qualifying NEET is mandatory for Indian students."),
                ("What is the duration of the MBBS course at Gulistan State Medical University?", "The program duration is 6 years, including 5 years of study and 1 year of compulsory rotating internship."),
                ("Are hostels provided for international students at Gulistan State Medical University?", "Yes, modern hostel accommodation with heating, Wi-Fi, 24/7 security, and Indian mess services are available.")
            ]
        }
    ]

    uzbekistan_sidebar_links = [
        ("Andijan State Medical Institute", "/andijan-state-medical-institute-ranking"),
        ("Fergana Medical Institute of Public Health", "/fergana-medical-institute-of-public-health"),
        ("Samarkand State Medical Institute", "/samarkand-state-medical-institute"),
        ("Tashkent Medical Academy", "/tashkent-medical-academy"),
        ("Urgench branch of Tashkent Medical Academy", "/urgench-branch-of-tashkent-medical-academy"),
        ("Bukhara State Medical University", "/bukhara-state-medical-university"),
        ("Namangan State Medical University", "/namangan-state-medical-university"),
        ("Mamun University", "/mamun-university"),
        ("Navoi State Medical University", "/navoi-state-medical-university"),
        ("Zarmed University", "/zarmed-university"),
        ("Karshi State Medical University", "/karshi-state-medical-university"),
        ("Gulistan State Medical University", "/gulistan-state-medical-university")
    ]

    sidebar_lis = []
    for name, link in uzbekistan_sidebar_links:
        sidebar_lis.append(f'''<li class="elementor-icon-list-item">
	<span class="elementor-icon-list-icon">
		<svg aria-hidden="true" class="e-font-icon-svg e-fas-check" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M173.898 439.404l-166.4-166.4c-9.997-9.997-9.997-26.206 0-36.204l36.203-36.204c9.997-9.998 26.207-9.998 36.204 0L192 312.69 432.095 72.596c9.997-9.997 26.207-9.997 36.204 0l36.203 36.204c9.997 9.997 9.997 26.206 0 36.204l-294.4 294.401c-9.998 9.997-26.207 9.997-36.204-.001z"></path></svg>
	</span>
	<span class="elementor-icon-list-text"><a href="{link}">{name}</a></span>
</li>''')
    sidebar_html = '\n'.join(sidebar_lis)

    for uni in universities:
        t_val = uni["tuition_val"]
        h_val = uni["hostel_val"]
        tot_val = t_val + h_val
        
        y_fees = [
            (f"{t_val:,} USD", f"{h_val:,} USD", f"{tot_val:,} USD")
            for _ in range(6)
        ]

        b = template_body

        # Perform exact replacements for titles
        b = b.replace("Andijan State Medical Institute Ranking, Uzbekistan", f"{uni['full_name']} Ranking, Uzbekistan")
        b = b.replace("Andijan State Medical Institute, Uzbekistan", f"{uni['full_name']}, Uzbekistan")
        b = b.replace("Andijan State Medical Institute", uni['full_name'])
        b = b.replace("Andijan Medical Institute", uni['full_name'])
        b = b.replace("Andijan", uni['short_name'])
        b = b.replace("Bukhara & Samarkand state medical institute", uni['full_name'])
        b = b.replace("Bukhara & Samarkand", uni['city'])

        b = b.replace("/andijan-state-medical-institute-ranking", f"/{uni['slug']}")

        # Update Overview paragraphs
        overview_html = f"<p>{uni['overview_p1']}</p><p>{uni['overview_p2']}</p><p>{uni['overview_p3']}</p>"
        p_match = re.search(r'(<h2 class="elementor-heading-title elementor-size-default">' + re.escape(uni['full_name']) + r', Uzbekistan</h2>[\s\S]*?<div class="elementor-widget-container">)([\s\S]*?)(</div>)', b)
        if p_match:
            b = b[:p_match.start(2)] + '\n' + overview_html + '\n' + b[p_match.end(2):]

        # Update Hero description
        hero_desc = f"{uni['full_name']} is one of the premier medical universities in Uzbekistan, providing high quality 100% English-medium medical education for international students."
        b = re.sub(r'<p class="elementor-image-box-description">[\s\S]*?</p>', f'<p class="elementor-image-box-description">{hero_desc}</p>', b, count=1)

        # Update Highlights table
        b = re.sub(r'<td>1955</td>', f'<td>{uni["established"]}</td>', b)
        b = re.sub(r'<td>State / Government Medical Institute</td>', f'<td>{uni["type"]}</td>', b)
        b = re.sub(r'<td>Top Ranked Government Medical Institute in Uzbekistan</td>', f'<td>{uni["ranking"]}</td>', b)

        # Update Fee table values
        for yr_str in ["6,000 USD", "4,000 USD", "3,500 USD"]:
            b = b.replace(yr_str, uni["tuition_yr"])

        # Update Sidebar university list
        pattern_sidebar = r'(<h2 class="elementor-heading-title elementor-size-default">Universities In <span>Uzbekistan</span></h2>[\s\S]*?<ul class="elementor-icon-list-items">)([\s\S]*?)(</ul>)'
        match_sb = re.search(pattern_sidebar, b)
        if match_sb:
            b = b[:match_sb.start(2)] + '\n' + sidebar_html + '\n' + b[match_sb.end(2):]

        # Update FAQ accordion
        faq_html_cards = []
        for i, (q, a) in enumerate(uni["faqs"]):
            active_cls = "active" if i == 0 else ""
            show_cls = "show collapse" if i == 0 else "collapse"
            expanded = "true" if i == 0 else "false"
            collapsed_cls = "" if i == 0 else "collapsed"
            
            card_html = f'''<div class="elementskit-card {active_cls}">
                    <div class="elementskit-card-header" id="primaryHeading-{i}-{uni["slug"]}">
                        <a href="#Collapse-{uni["slug"]}-{i}" class="ekit-accordion--toggler elementskit-btn-link {collapsed_cls}" data-ekit-toggle="collapse" data-target="#Collapse-{uni["slug"]}-{i}" aria-expanded="{expanded}" aria-controls="Collapse-{uni["slug"]}-{i}">
                                                            <div class="ekit_accordion_icon_left_group">
                                    <div class="ekit_accordion_normal_icon">
                                        <i class="mdi mdi-plus"></i>
                                    </div>
                                    <div class="ekit_accordion_active_icon">
                                        <i class="icofont icofont-minus"></i>
                                    </div>
                                </div>
                            <span class="ekit-accordion-title">{q}</span>
                        </a>
                    </div>
                    <div id="Collapse-{uni["slug"]}-{i}" class="{show_cls}" aria-labelledby="primaryHeading-{i}-{uni["slug"]}">
                        <div class="elementskit-card-body ekit-accordion--content">
                            <p>{a}</p>
                        </div>
                    </div>
                </div>'''
            faq_html_cards.append(card_html)
        
        faq_accordion_full = '\n'.join(faq_html_cards)
        pattern_faq = r'(<div class="elementskit-accordion accoedion-primary"[^>]*>)([\s\S]*?)(</div>\s*</div>\s*</div>\s*</div>)'
        match_faq = re.search(pattern_faq, b)
        if match_faq:
            b = b[:match_faq.start(2)] + '\n' + faq_accordion_full + '\n' + b[match_faq.end(2):]

        page_json = {
            "title": f"{uni['full_name']} Ranking, Uzbekistan – Atlas Mentor",
            "description": uni["description"],
            "canonical": f"https://atlasmentor.com/{uni['slug']}/",
            "robots": "max-image-preview:large",
            "stylesheets": andijan_data["stylesheets"],
            "body": b
        }

        output_path = f"data/pages/{uni['slug']}.json"
        with open(output_path, 'w', encoding='utf-8') as f_out:
            json.dump(page_json, f_out, indent=2, ensure_ascii=False)
        print(f"Successfully generated 100% clean Uzbekistan page {output_path}")

if __name__ == '__main__':
    build_exact_uzbekistan_pages()

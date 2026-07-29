import json
import re

def build_exact_georgia_pages():
    # Load Andijan template JSON
    with open('data/pages/andijan-state-medical-institute-ranking.json', 'r', encoding='utf-8') as f:
        andijan_data = json.load(f)

    template_body = andijan_data['body']

    universities = [
        {
            "slug": "caucasus-university",
            "full_name": "Caucasus University",
            "short_name": "Caucasus University",
            "city": "Tbilisi",
            "established": "1998",
            "type": "Private University",
            "ranking": "Top Private University in Tbilisi, Georgia",
            "tuition_yr": "6,000 USD",
            "hostel_yr": "1,200 USD",
            "tuition_val": 6000,
            "hostel_val": 1200,
            "img": "/wp-content/uploads/2025/02/Study-MBBS-in-Georgia.png",
            "description": "Caucasus University Georgia MBBS fees, eligibility & admission process for 2026. NMC & WHO recognized English medium medical program for Indian students.",
            "overview_p1": "Caucasus University (CU) is one of the premier higher education institutions in Georgia, located in the historical capital city of Tbilisi. Founded in 1998 in partnership with Georgia State University (USA), CU has grown into an internationally acclaimed university system comprising multiple specialized schools, including the prestigious Caucasus Medical School. The 6-year Medical Doctor (MD / MBBS equivalent) program at Caucasus University is designed according to top European healthcare education frameworks, combining rigorous basic science training with early clinical patient interaction.",
            "overview_p2": "The campus of Caucasus University is a state-of-the-art academic complex in Tbilisi featuring ultra-modern lecture halls, high-fidelity medical simulation suites, 3D digital anatomy laboratories, and biochemical research facilities. CU places heavy emphasis on evidence-based medicine, clinical problem-solving, and scientific research. Through its international partnerships, students have unique opportunities to participate in clinical observerships, joint research projects, and global medical exchange programs across Western Europe and North America.",
            "overview_p3": "For Indian medical aspirants seeking a globally recognized, 100% English-medium MBBS degree in Europe, Caucasus University offers an outstanding academic environment. The university's MD degree is fully recognized by WHO, NMC (India), WFME (via Georgia's NCEQE accreditation), ECFMG (USA), and the European Ministry of Education. Graduates are eligible to appear for licensing examinations worldwide, including the National Exit Test (NExT / FMGE) in India, USMLE in the United States, and PLAB in the United Kingdom.",
            "faqs": [
                ("Is Caucasus University recognized by NMC and WHO?", "Yes, Caucasus University is listed in the World Directory of Medical Schools (WDOMS), recognized by WHO, and fully complies with the National Medical Council (NMC) FMGL Regulations 2021 for Indian medical aspirants."),
                ("What is the medium of instruction for MBBS at Caucasus University?", "The entire 6-year Medical Doctor (MBBS equivalent) course at Caucasus University is taught 100% in English, including lectures, practicals, clinical postings, and examinations."),
                ("What is the eligibility requirement for Indian students at Caucasus University?", "Indian students must have completed 10+2 with at least 50% marks in Physics, Chemistry, and Biology (40% for reserved categories) and must have qualified the NEET exam in the year of admission."),
                ("What is the total duration of the MBBS program at Caucasus University?", "The duration of the MBBS / MD program at Caucasus University is 6 years, comprising 5 years of integrated academic and clinical studies followed by 1 year of compulsory rotating internship."),
                ("Are hostel and Indian food facilities available at Caucasus University?", "Yes, Caucasus University provides comfortable, secure hostel accommodations with air-conditioning, high-speed Wi-Fi, and 24/7 security. Dedicated Indian mess facilities serving nutritious veg and non-veg meals are also available nearby.")
            ]
        },
        {
            "slug": "caucasus-international-university",
            "full_name": "Caucasus International University",
            "short_name": "Caucasus International University",
            "city": "Tbilisi",
            "established": "1995",
            "type": "Private University",
            "ranking": "Top 10 Medical Universities in Georgia",
            "tuition_yr": "5,500 USD",
            "hostel_yr": "1,200 USD",
            "tuition_val": 5500,
            "hostel_val": 1200,
            "img": "/wp-content/uploads/2025/02/Study-MBBS-in-Georgia.png",
            "description": "Caucasus International University (CIU) Georgia MBBS admission 2026. Affordable fees, 100% English medium, NMC/WHO approved, and top clinical facilities.",
            "overview_p1": "Caucasus International University (CIU) is a higher education institution founded in 1995 in Tbilisi, Georgia. Over the past three decades, CIU has established itself as a premier center for international medical education, hosting thousands of international students from more than 40 countries. The Faculty of Medicine at CIU delivers an accredited 6-year Educational Program in Medicine (MD / MBBS equivalent) designed to cultivate highly skilled, compassionate, and globally competent physicians.",
            "overview_p2": "CIU features an impressive academic infrastructure equipped with modern 3D virtual anatomy dissection suites, phantom simulation rooms, histology and pathology research laboratories, and clinical skill training centers. The university curriculum strictly complies with World Federation for Medical Education (WFME) standards and the European ECTS credit transfer framework. CIU maintains strategic partnerships with major clinical hospitals and specialized medical centers across Tbilisi, guaranteeing hands-on bedside training for all students.",
            "overview_p3": "For Indian students, Caucasus International University provides a supportive, multicultural academic community. With 100% English-medium instruction, affordable tuition fees, safe university hostel accommodations, Indian mess facilities, and active guidance for FMGE/NExT and USMLE examinations, CIU stands out as an exceptional choice for pursuing an MBBS degree in Georgia.",
            "faqs": [
                ("Is NEET required for MBBS admission at Caucasus International University?", "Yes, NEET qualification is mandatory for all Indian students seeking admission to Caucasus International University if they intend to practice medicine in India after graduation."),
                ("What are the annual tuition fees at Caucasus International University?", "The annual tuition fee for the English-medium MBBS program at Caucasus International University is approximately 5,500 USD per year."),
                ("Does Caucasus International University comply with NMC guidelines?", "Yes, CIU's 6-year medical program satisfies all criteria set by the NMC FMGL Regulations 2021, including course duration, medium of instruction, clinical subjects, and internship requirements."),
                ("Is IELTS or TOEFL needed for admission to CIU?", "No, IELTS or TOEFL scores are not mandatory for admission. However, applicants must demonstrate good command over the English language during the university interview."),
                ("What clinical facilities are available for CIU medical students?", "CIU partners with multiple affiliated teaching hospitals and medical centers in Tbilisi where students undergo hands-on clinical rotations in Internal Medicine, Surgery, Pediatrics, Obstetrics & Gynecology, and Emergency Care.")
            ]
        },
        {
            "slug": "east-european-university",
            "full_name": "East European University",
            "short_name": "East European University",
            "city": "Tbilisi",
            "established": "2012",
            "type": "Private University",
            "ranking": "Recognized European Standard Medical University",
            "tuition_yr": "5,000 USD",
            "hostel_yr": "1,000 USD",
            "tuition_val": 5000,
            "hostel_val": 1000,
            "img": "/wp-content/uploads/2025/02/Study-MBBS-in-Georgia.png",
            "description": "East European University (EEU) Georgia MBBS fees & admission 2026. NMC & WHO recognized 6-year English medium MD course for Indian aspirants.",
            "overview_p1": "East European University (EEU) is a modern, state-accredited higher educational institution situated in the capital city of Tbilisi, Georgia. Established in 2012, EEU was created with the explicit mission of delivering European-standard higher education. Its Healthcare Sciences Faculty offers a world-class 6-year Medical Doctor (MD / MBBS) program that adheres strictly to European Higher Education Area (EHEA) standards and the Bologna Process.",
            "overview_p2": "The new green campus of East European University is one of the most technologically advanced university facilities in Georgia. It features eco-friendly smart lecture rooms, simulation medical centers, OSCE examination suites, digital laboratories, and comprehensive electronic learning management platforms. EEU emphasizes student-centered learning, small-group seminar discussions, problem-based learning (PBL), and early clinical practical exposure.",
            "overview_p3": "For Indian students, East European University offers an ideal balance of academic quality and affordability. The university's degrees are recognized worldwide by WHO, NMC (India), WFME (via NCEQE), and ECFMG (USA). EEU provides a safe, welcoming campus environment complete with modern hostels, Indian food options, and dedicated student mentoring services.",
            "faqs": [
                ("Is East European University approved by the National Medical Council of India?", "Yes, East European University is recognized by the NMC (formerly MCI) and WHO, allowing Indian graduates to sit for the FMGE / NExT licensing exams."),
                ("What is the cost of studying MBBS at East European University?", "The annual tuition fee at East European University is 5,000 USD, with living and hostel expenses averaging around 1,000 USD per year."),
                ("Where is East European University located?", "EEU is situated in the capital city of Tbilisi, Georgia, featuring a modern, eco-friendly campus with convenient access to transportation, student hostels, and city amenities."),
                ("What is the medium of teaching at EEU Georgia?", "The entire Medical Doctor (MBBS) program is taught in English for international students."),
                ("How long is the MBBS program at East European University?", "The program lasts for 6 years, including 5 years of academic and clinical course work and 1 year of compulsory rotating internship.")
            ]
        },
        {
            "slug": "european-university",
            "full_name": "European University",
            "short_name": "European University",
            "city": "Tbilisi",
            "established": "2012",
            "type": "Private University",
            "ranking": "Top Rated Medical University with Own University Hospital",
            "tuition_yr": "5,500 USD",
            "hostel_yr": "1,000 USD",
            "tuition_val": 5500,
            "hostel_val": 1000,
            "img": "/wp-content/uploads/2025/02/Study-MBBS-in-Georgia.png",
            "description": "European University Georgia MBBS admission 2026. Own university hospital (Jo Ann Medical Center), NMC/WHO approved, affordable fees & top faculty.",
            "overview_p1": "European University (EU), located in Tbilisi, Georgia, is a premier private university established in 2012. EU stands out among Georgian medical institutions because it owns and operates its own super-specialty teaching hospital — Jo Ann University Hospital. This unique ownership gives European University medical students direct, unhindered access to high-volume clinical practice, advanced diagnostic procedures, and real-world surgical observations.",
            "overview_p2": "The Faculty of Medicine at European University offers a 6-year English-medium Medical Doctor (MD / MBBS equivalent) program that meets international accreditation benchmarks. The university features cutting-edge simulation laboratories, OSCE examination stations, 3D anatomical models, and advanced biomedical research centers. EU's curriculum is aligned with European Credit Transfer and Accumulation System (ECTS) and WFME guidelines.",
            "overview_p3": "Indian students at European University benefit from a world-class clinical learning environment, affordable tuition fees, secure campus hostels, Indian mess options, and dedicated support for licensing exams including NExT/FMGE (India) and USMLE (USA). EU’s degrees are recognized globally by WHO, NMC, WFME, and ECFMG.",
            "faqs": [
                ("Does European University Georgia have its own teaching hospital?", "Yes, European University owns Jo Ann University Hospital in Tbilisi, a renowned multi-specialty cardiac and pediatric hospital providing direct clinical exposure to medical students."),
                ("Is European University recognized by WHO and NMC?", "Yes, European University is listed in WDOMS and recognized by WHO, NMC (India), ECFMG (USA), and NCEQE (Georgia)."),
                ("What is the fee structure for MBBS at European University Georgia?", "The tuition fee is 5,500 USD per year, and hostel accommodation costs approximately 1,000 USD per year."),
                ("What is the admission procedure for Indian students at European University?", "Admission is based on 10+2 marks in PCB (min 50%), NEET qualification, document submission, and an online video interview conducted by the university admissions committee."),
                ("Is Indian food available at European University?", "Yes, university hostel dining halls and nearby Indian restaurants offer authentic Indian vegetarian and non-vegetarian meals for Indian students.")
            ]
        },
        {
            "slug": "kutaisi-university",
            "full_name": "Kutaisi University",
            "short_name": "Kutaisi University",
            "city": "Kutaisi",
            "established": "1991",
            "type": "Private University",
            "ranking": "Oldest Private Higher Education Institution in Georgia",
            "tuition_yr": "4,500 USD",
            "hostel_yr": "900 USD",
            "tuition_val": 4500,
            "hostel_val": 900,
            "img": "/wp-content/uploads/2025/02/Study-MBBS-in-Georgia.png",
            "description": "Kutaisi University (UNIK) Georgia MBBS fees & admission 2026. Highly affordable tuition, NMC & WHO approved 6-year English medium medical degree.",
            "overview_p1": "Kutaisi University (UNIK) holds the distinction of being the first private higher educational institution established in Georgia, founded in 1991. Located in Kutaisi, the historic second-largest city of Georgia, UNIK offers a peaceful, scenic, and cost-effective study environment. Its Faculty of Medicine provides an accredited 6-year English-medium Medical Doctor (MD / MBBS) program tailored for international students.",
            "overview_p2": "The medical curriculum at Kutaisi University blends strong theoretical foundations with extensive practical training in clinical simulation labs and regional teaching hospitals in the Imereti region. With lower tuition fees and significantly cheaper living expenses than in Tbilisi, UNIK provides an affordable pathway to a genuine European medical degree without compromising academic standards or global recognition.",
            "overview_p3": "For Indian students seeking a budget-friendly MBBS program abroad, Kutaisi University offers an unbeatable option. UNIK is recognized by WHO (WDOMS), NMC (India), WFME (via NCEQE), and ECFMG (USA). Graduates are fully qualified to take the NExT/FMGE exam in India and pursue postgraduate medical training internationally.",
            "faqs": [
                ("Why choose Kutaisi University for MBBS in Georgia?", "Kutaisi University offers top-tier medical education at an affordable tuition fee of 4,500 USD/year, significantly lower living expenses in Kutaisi city, and full NMC/WHO recognition."),
                ("Is Kutaisi University recognized by NMC for Indian students?", "Yes, Kutaisi University is listed in WDOMS and approved by NMC, making its graduates eligible for the FMGE/NExT exam in India."),
                ("What is the cost of living in Kutaisi compared to Tbilisi?", "Living costs in Kutaisi are approximately 30-40% cheaper than in Tbilisi, with hostel and food expenses averaging 900 USD to 1,200 USD per year."),
                ("What is the medium of instruction at Kutaisi University?", "The entire 6-year medical program is delivered 100% in English."),
                ("How to reach Kutaisi from India?", "Kutaisi has its own international airport (Kutaisi International Airport - KUT) with direct and connecting flights from major hubs, or students can fly to Tbilisi and take a 3-hour highway drive to Kutaisi.")
            ]
        },
        {
            "slug": "tbilisi-state-medical-university",
            "full_name": "Tbilisi State Medical University",
            "short_name": "Tbilisi State Medical University",
            "city": "Tbilisi",
            "established": "1918",
            "type": "Public / Government University",
            "ranking": "Ranked #1 Government Medical University in Georgia",
            "tuition_yr": "8,000 USD",
            "hostel_yr": "1,500 USD",
            "tuition_val": 8000,
            "hostel_val": 1500,
            "img": "/wp-content/uploads/2024/07/Tbilisi-State-Medical-University.jpg",
            "description": "Tbilisi State Medical University (TSMU) Georgia MBBS admission 2026. Top government medical university, WHO/NMC recognized, 100% English medium.",
            "overview_p1": "Tbilisi State Medical University (TSMU) is the premier public medical university in Georgia, established in 1918. As the oldest, largest, and most prestigious medical institution in the Caucasus region, TSMU has educated generations of renowned physicians, clinical specialists, and medical researchers over its century-long history. TSMU stands as the undisputed flagship of medical education in Georgia.",
            "overview_p2": "TSMU boasts expansive university clinics, research institutes, high-tech simulation centers, and prestigious international partnerships with top European and American institutions (such as Emory University School of Medicine, USA). The university offers an internationally acclaimed 6-year English-medium Medical Doctor (MD / MBBS) program that attracts thousands of high-achieving medical aspirants globally.",
            "overview_p3": "For Indian students, Tbilisi State Medical University represents the pinnacle of medical study abroad. Its diploma carries immense global prestige, exceptionally high FMGE/NExT pass rates, and direct eligibility pathways for USMLE (USA), PLAB (UK), and European medical licensure boards.",
            "faqs": [
                ("Is Tbilisi State Medical University a government university?", "Yes, TSMU is a premier public (government) medical university in Georgia, established in 1918."),
                ("Is TSMU Georgia recognized by NMC and WHO?", "Yes, TSMU is fully recognized by WHO, NMC (India), WFME, ECFMG (USA), and European Ministry of Education."),
                ("What is the tuition fee for MBBS at Tbilisi State Medical University?", "The annual tuition fee for the English-medium MD program at TSMU is approximately 8,000 USD per year."),
                ("What are the FMGE pass rate prospects for TSMU graduates?", "TSMU graduates consistently achieve among the highest FMGE/NExT pass rates in India due to rigorous clinical training and comprehensive basic science grounding."),
                ("How competitive is admission to Tbilisi State Medical University?", "Admission is merit-based and highly sought-after. Applicants require strong academic scores in 12th PCB, NEET qualification, and successful performance in the university entrance interview.")
            ]
        }
    ]

    georgia_sidebar_links = [
        ("Tbilisi State Medical University", "/tbilisi-state-medical-university"),
        ("Caucasus University", "/caucasus-university"),
        ("Caucasus International University", "/caucasus-international-university"),
        ("European University", "/european-university"),
        ("East European University", "/east-european-university"),
        ("Kutaisi University", "/kutaisi-university"),
        ("Akaki Tsereteli State University", "/akaki-tsereteli-state-university"),
        ("Batumi Shota Rustaveli State University", "/batumi-shota-rustaveli-state-university"),
        ("Georgian National University SEU", "/georgian-national-university-seu"),
        ("East West University", "/east-west-university-georgia"),
        ("Alte Medical University", "/alte-medical-university")
    ]

    sidebar_lis = []
    for name, link in georgia_sidebar_links:
        sidebar_lis.append(f'''<li class="elementor-icon-list-item">
	<span class="elementor-icon-list-icon">
		<svg aria-hidden="true" class="e-font-icon-svg e-fas-check" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M173.898 439.404l-166.4-166.4c-9.997-9.997-9.997-26.206 0-36.204l36.203-36.204c9.997-9.998 26.207-9.998 36.204 0L192 312.69 432.095 72.596c9.997-9.997 26.207-9.997 36.204 0l36.203 36.204c9.997 9.997 9.997 26.206 0 36.204l-294.4 294.401c-9.998 9.997-26.207 9.997-36.204-.001z"></path></svg>
	</span>
	<span class="elementor-icon-list-text"><a href="{link}">{name}</a></span>
</li>''')
    sidebar_html = '\n'.join(sidebar_lis)

    for uni in universities:
        b = template_body

        # Perform exact case-insensitive replacements for all Andijan/Uzbekistan occurrences
        # 1. Names
        b = b.replace("Andijan state medical institute", uni['full_name'])
        b = b.replace("Andijan State Medical Institute Ranking, Uzbekistan", f"{uni['full_name']} Ranking, Georgia")
        b = b.replace("Andijan State Medical Institute, Uzbekistan", f"{uni['full_name']}, Georgia")
        b = b.replace("Andijan State Medical Institute", uni['full_name'])
        b = b.replace("Andijan Medical Institute", uni['full_name'])
        b = b.replace("Andijan", uni['short_name'])

        # 2. Countries & URLs
        b = b.replace("Uzbekistan", "Georgia")
        b = b.replace("uzbekistan", "georgia")
        b = b.replace("/study-mbbs-in-georgia-for-indian-students-for-indian-students", "/study-mbbs-in-georgia-for-indian-students")
        b = b.replace("/andijan-state-medical-institute-ranking", f"/{uni['slug']}")

        # 3. Overview paragraphs
        overview_html = f"<p>{uni['overview_p1']}</p><p>{uni['overview_p2']}</p><p>{uni['overview_p3']}</p>"
        p_match = re.search(r'(<h2 class="elementor-heading-title elementor-size-default">' + re.escape(uni['full_name']) + r', Georgia</h2>[\s\S]*?<div class="elementor-widget-container">)([\s\S]*?)(</div>)', b)
        if p_match:
            b = b[:p_match.start(2)] + '\n' + overview_html + '\n' + b[p_match.end(2):]

        # 4. Hero description
        hero_desc = f"{uni['full_name']} is one of the premier medical universities in Georgia, providing high quality 100% English-medium European medical education for international students."
        b = re.sub(r'<p class="elementor-image-box-description">[\s\S]*?</p>', f'<p class="elementor-image-box-description">{hero_desc}</p>', b, count=1)

        # 5. Highlights table
        b = re.sub(r'<td>1955</td>', f'<td>{uni["established"]}</td>', b)
        b = re.sub(r'<td>State / Government Medical Institute</td>', f'<td>{uni["type"]}</td>', b)
        b = re.sub(r'<td>Top Ranked Government Medical Institute in Georgia</td>', f'<td>{uni["ranking"]}</td>', b)

        # 6. Sidebar university list
        pattern_sidebar = r'(<h2 class="elementor-heading-title elementor-size-default">Universities In <span>Georgia</span></h2>[\s\S]*?<ul class="elementor-icon-list-items">)([\s\S]*?)(</ul>)'
        match_sb = re.search(pattern_sidebar, b)
        if match_sb:
            b = b[:match_sb.start(2)] + '\n' + sidebar_html + '\n' + b[match_sb.end(2):]

        # 7. FAQ accordion
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

        # Double-check final string check for any remaining 'andijan'
        if 'andijan' in b.lower():
            print(f"WARNING: 'andijan' found in {uni['slug']}")

        page_json = {
            "title": f"{uni['full_name']} Ranking, Georgia – Atlas Mentor",
            "description": uni["description"],
            "canonical": f"https://atlasmentor.com/{uni['slug']}/",
            "robots": "max-image-preview:large",
            "stylesheets": andijan_data["stylesheets"],
            "body": b
        }

        output_path = f"data/pages/{uni['slug']}.json"
        with open(output_path, 'w', encoding='utf-8') as f_out:
            json.dump(page_json, f_out, indent=2, ensure_ascii=False)
        print(f"Successfully generated 100% perfect page {output_path}")

if __name__ == '__main__':
    build_exact_georgia_pages()

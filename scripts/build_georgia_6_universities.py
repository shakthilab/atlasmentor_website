import json
import re
import os

def create_georgia_university_pages():
    with open('data/pages/namangan-state-medical-university.json', 'r', encoding='utf-8') as f:
        template_data = json.load(f)

    universities = [
        {
            "slug": "caucasus-university",
            "full_name": "Caucasus University",
            "short_name": "Caucasus University (CU)",
            "city": "Tbilisi",
            "established": "1998",
            "type": "Private University",
            "ranking": "Top Private University in Tbilisi, Georgia",
            "tuition_yr": "6,000 USD",
            "hostel_yr": "1,200 USD",
            "tuition_val": 6000,
            "hostel_val": 1200,
            "img": "/wp-content/uploads/2025/02/Study-MBBS-in-Georgia.png",
            "website": "https://cu.edu.ge/",
            "keywords": "Caucasus University Georgia, MBBS at Caucasus University, Caucasus University tuition fees 2026, MBBS in Georgia for Indian Students, Caucasus Medical School Tbilisi",
            "description": "Caucasus University Georgia MBBS fees, eligibility & admission process for 2026. NMC & WHO recognized English medium medical program for Indian students.",
            "overview_p1": "Caucasus University (CU) is one of the premier higher education institutions in Georgia, located in the historical capital city of Tbilisi. Founded in 1998 in partnership with Georgia State University (USA), CU has grown into an internationally acclaimed university system comprising multiple specialized schools, including the prestigious Caucasus Medical School. The 6-year Medical Doctor (MD / MBBS equivalent) program at Caucasus University is designed according to top European healthcare education frameworks, combining rigorous basic science training with early clinical patient interaction.",
            "overview_p2": "The campus of Caucasus University is a state-of-the-art academic complex in Tbilisi featuring ultra-modern lecture halls, high-fidelity medical simulation suites, 3D digital anatomy laboratories, and biochemical research facilities. CU places heavy emphasis on evidence-based medicine, clinical problem-solving, and scientific research. Through its international partnerships, students have unique opportunities to participate in clinical observerships, joint research projects, and global medical exchange programs across Western Europe and North America.",
            "overview_p3": "For Indian medical aspirants seeking a globally recognized, 100% English-medium MBBS degree in Europe, Caucasus University offers an outstanding academic environment. The university's MD degree is fully recognized by WHO, NMC (India), WFME (via Georgia's NCEQE accreditation), ECFMG (USA), and the European Ministry of Education. Graduates are eligible to appear for licensing examinations worldwide, including the National Exit Test (NExT / FMGE) in India, USMLE in the United States, and PLAB in the United Kingdom.",
            "clinical_text": "Caucasus Medical School collaborates with leading university-affiliated teaching hospitals and multi-specialty regional medical centers across Tbilisi. Clinical rotations begin in the third year and cover major disciplines including Internal Medicine, General Surgery, Pediatrics, Obstetrics & Gynecology, Neurology, Cardiology, and Emergency Care. Under the direct supervision of certified consultants and senior professors, students gain extensive bedside experience, master history-taking, perform diagnostic physical examinations, and participate in surgical procedures and ward rounds.",
            "facilities_text": "Caucasus University provides world-class infrastructure tailored for international student success. The modern campus includes high-fidelity OSCE clinical simulation labs, digital dissection tables, interactive electronic classrooms, and a vast central library stocked with over 150,000 physical books and 24/7 electronic access to PubMed, BMJ, and ClinicalKey. Student hostels feature furnished single and double rooms with central heating, high-speed Wi-Fi, study lounges, laundry facilities, and 24/7 security coverage. Dedicated Indian dining facilities near the campus serve fresh North Indian and South Indian vegetarian and non-vegetarian meals daily.",
            "faqs": [
                ("Is Caucasus University recognized by NMC and WHO?", "Yes, Caucasus University is listed in the World Directory of Medical Schools (WDOMS), recognized by WHO, and fully complies with the National Medical Council (NMC) FMGL Regulations 2021 for Indian medical aspirants."),
                ("What is the medium of instruction for MBBS at Caucasus University?", "The entire 6-year Medical Doctor (MBBS equivalent) course at Caucasus University is taught 100% in English, including lectures, practicals, clinical postings, and examinations."),
                ("What is the eligibility requirement for Indian students at Caucasus University?", "Indian students must have completed 10+2 with at least 50% marks in Physics, Chemistry, and Biology (40% for reserved categories) and must have qualified the NEET exam in the year of admission."),
                ("What is the total duration of the MBBS program at Caucasus University?", "The duration of the MBBS / MD program at Caucasus University is 6 years, comprising 5 years of integrated academic and clinical studies followed by 1 year of compulsory rotating clinical internship."),
                ("Are hostel and Indian food facilities available at Caucasus University?", "Yes, Caucasus University provides comfortable, secure hostel accommodations with air-conditioning, high-speed Wi-Fi, and 24/7 security. Dedicated Indian mess facilities serving nutritious veg and non-veg meals are also available nearby.")
            ]
        },
        {
            "slug": "caucasus-international-university",
            "full_name": "Caucasus International University",
            "short_name": "Caucasus International University (CIU)",
            "city": "Tbilisi",
            "established": "1995",
            "type": "Private University",
            "ranking": "Top 10 Medical Universities in Georgia",
            "tuition_yr": "5,500 USD",
            "hostel_yr": "1,200 USD",
            "tuition_val": 5500,
            "hostel_val": 1200,
            "img": "/wp-content/uploads/2025/02/Study-MBBS-in-Georgia.png",
            "website": "https://ciu.edu.ge/",
            "keywords": "Caucasus International University Georgia, CIU Tbilisi MBBS fees, Study MBBS at CIU, NMC approved medical colleges in Georgia, CIU Faculty of Medicine",
            "description": "Caucasus International University (CIU) Georgia MBBS admission 2026. Affordable fees, 100% English medium, NMC/WHO approved, and top clinical facilities.",
            "overview_p1": "Caucasus International University (CIU) is a higher education institution founded in 1995 in Tbilisi, Georgia. Over the past three decades, CIU has established itself as a premier center for international medical education, hosting thousands of international students from more than 40 countries. The Faculty of Medicine at CIU delivers an accredited 6-year Educational Program in Medicine (MD / MBBS equivalent) designed to cultivate highly skilled, compassionate, and globally competent physicians.",
            "overview_p2": "CIU features an impressive academic infrastructure equipped with modern 3D virtual anatomy dissection suites, phantom simulation rooms, histology and pathology research laboratories, and clinical skill training centers. The university curriculum strictly complies with World Federation for Medical Education (WFME) standards and the European ECTS credit transfer framework. CIU maintains strategic partnerships with major clinical hospitals and specialized medical centers across Tbilisi, guaranteeing hands-on bedside training for all students.",
            "overview_p3": "For Indian students, Caucasus International University provides a supportive, multicultural academic community. With 100% English-medium instruction, affordable tuition fees, safe university hostel accommodations, Indian mess facilities, and active guidance for FMGE/NExT and USMLE examinations, CIU stands out as an exceptional choice for pursuing an MBBS degree in Georgia.",
            "clinical_text": "Clinical education at Caucasus International University is conducted in leading multi-specialty teaching hospitals in Tbilisi. Students undergo hands-on clinical clerkships across key clinical branches including Internal Medicine, General Surgery, Pediatrics, Gynecology & Obstetrics, Traumatology, Anesthesiology, and Emergency Care. Under the guidance of experienced medical professors and attending doctors, students master clinical examination techniques, diagnostic interpretation, surgical assisting, and patient care management.",
            "facilities_text": "CIU offers modern campus amenities designed for academic excellence and comfortable living. The campus houses state-of-the-art simulation labs, interactive electronic lecture halls, and an extensive medical library with physical and digital access to international medical repositories. Hostels provide furnished rooms equipped with heating, high-speed Wi-Fi, study desks, and round-the-clock security. Indian dining options are readily accessible, offering freshly prepared Indian dishes catering to both vegetarian and non-vegetarian preferences.",
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
            "short_name": "East European University (EEU)",
            "city": "Tbilisi",
            "established": "2012",
            "type": "Private University",
            "ranking": "Recognized European Standard Medical University",
            "tuition_yr": "5,000 USD",
            "hostel_yr": "1,000 USD",
            "tuition_val": 5000,
            "hostel_val": 1000,
            "img": "/wp-content/uploads/2025/02/Study-MBBS-in-Georgia.png",
            "website": "https://eeu.edu.ge/",
            "keywords": "East European University Georgia, EEU Tbilisi MBBS fees 2026, Study MBBS in Georgia, NMC approved medical universities Georgia, EEU Medical Doctor Program",
            "description": "East European University (EEU) Georgia MBBS fees & admission 2026. NMC & WHO recognized 6-year English medium MD course for Indian aspirants.",
            "overview_p1": "East European University (EEU) is a modern, state-accredited higher educational institution situated in the capital city of Tbilisi, Georgia. Established in 2012, EEU was created with the explicit mission of delivering European-standard higher education. Its Healthcare Sciences Faculty offers a world-class 6-year Medical Doctor (MD / MBBS) program that adheres strictly to European Higher Education Area (EHEA) standards and the Bologna Process.",
            "overview_p2": "The new green campus of East European University is one of the most technologically advanced university facilities in Georgia. It features eco-friendly smart lecture rooms, simulation medical centers, OSCE examination suites, digital laboratories, and comprehensive electronic learning management platforms. EEU emphasizes student-centered learning, small-group seminar discussions, problem-based learning (PBL), and early clinical practical exposure.",
            "overview_p3": "For Indian students, East European University offers an ideal balance of academic quality and affordability. The university's degrees are recognized worldwide by WHO, NMC (India), WFME (via NCEQE), and ECFMG (USA). EEU provides a safe, welcoming campus environment complete with modern hostels, Indian food options, and dedicated student mentoring services.",
            "clinical_text": "Clinical clerkships at East European University are conducted at renowned partner clinics and multi-profile hospitals across Tbilisi. Students receive clinical instruction in core branches such as Cardiology, Gastroenterology, General Surgery, Orthopedics, Pediatrics, Obstetrics, and Intensive Care. Small clinical study groups ensure that every student receives individualized attention from senior doctors and active involvement in daily hospital rounds.",
            "facilities_text": "EEU's modern campus provides an exceptional learning and living environment. Facilities include state-of-the-art simulation equipment, virtual dissection tables, electronic library systems with access to leading international databases, sports complexes, and recreational zones. Student accommodation options include modern hostel rooms with heating, high-speed internet, 24/7 security, and dedicated Indian mess services providing wholesome Indian meals.",
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
            "short_name": "European University (EU)",
            "city": "Tbilisi",
            "established": "2012",
            "type": "Private University",
            "ranking": "Top Rated Medical University with Own University Hospital",
            "tuition_yr": "5,500 USD",
            "hostel_yr": "1,000 USD",
            "tuition_val": 5500,
            "hostel_val": 1000,
            "img": "/wp-content/uploads/2025/02/Study-MBBS-in-Georgia.png",
            "website": "https://eu.edu.ge/",
            "keywords": "European University Georgia, European University Tbilisi MBBS fees, Jo Ann Medical Center Georgia, MBBS in Georgia Indian students, EU Georgia Faculty of Medicine",
            "description": "European University Georgia MBBS admission 2026. Own university hospital (Jo Ann Medical Center), NMC/WHO approved, affordable fees & top faculty.",
            "overview_p1": "European University (EU), located in Tbilisi, Georgia, is a premier private university established in 2012. EU stands out among Georgian medical institutions because it owns and operates its own super-specialty teaching hospital — Jo Ann University Hospital. This unique ownership gives European University medical students direct, unhindered access to high-volume clinical practice, advanced diagnostic procedures, and real-world surgical observations.",
            "overview_p2": "The Faculty of Medicine at European University offers a 6-year English-medium Medical Doctor (MD / MBBS equivalent) program that meets international accreditation benchmarks. The university features cutting-edge simulation laboratories, OSCE examination stations, 3D anatomical models, and advanced biomedical research centers. EU's curriculum is aligned with European Credit Transfer and Accumulation System (ECTS) and WFME guidelines.",
            "overview_p3": "Indian students at European University benefit from a world-class clinical learning environment, affordable tuition fees, secure campus hostels, Indian mess options, and dedicated support for licensing exams including NExT/FMGE (India) and USMLE (USA). EU’s degrees are recognized globally by WHO, NMC, WFME, and ECFMG.",
            "clinical_text": "The defining advantage of European University is its ownership of Jo Ann University Hospital, a leading cardiac and pediatric multi-specialty medical center in Tbilisi. Students complete clinical rotations directly inside Jo Ann Hospital and other affiliated teaching facilities, gaining hands-on experience in Emergency Medicine, Surgery, Cardiology, Pediatrics, Obstetrics, and Intensive Care under the guidance of renowned Georgian and international medical specialists.",
            "facilities_text": "European University offers superior campus facilities including modern clinical simulation centers, OSCE practical exam labs, electronic library facilities, and collaborative student spaces. Hostel accommodations feature well-furnished rooms with central heating, Wi-Fi, study facilities, and round-the-clock security. Indian dining options located adjacent to the campus serve authentic Indian vegetarian and non-vegetarian food daily.",
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
            "short_name": "Kutaisi University (UNIK)",
            "city": "Kutaisi",
            "established": "1991",
            "type": "Private University",
            "ranking": "Oldest Private Higher Education Institution in Georgia",
            "tuition_yr": "4,500 USD",
            "hostel_yr": "900 USD",
            "tuition_val": 4500,
            "hostel_val": 900,
            "img": "/wp-content/uploads/2025/02/Study-MBBS-in-Georgia.png",
            "website": "https://unik.edu.ge/",
            "keywords": "Kutaisi University Georgia, UNIK Kutaisi MBBS fees, Study MBBS in Kutaisi Georgia, Affordable MBBS in Georgia for Indian students, UNIK Faculty of Medicine",
            "description": "Kutaisi University (UNIK) Georgia MBBS fees & admission 2026. Highly affordable tuition, NMC & WHO approved 6-year English medium medical degree.",
            "overview_p1": "Kutaisi University (UNIK) holds the distinction of being the first private higher educational institution established in Georgia, founded in 1991. Located in Kutaisi, the historic second-largest city of Georgia, UNIK offers a peaceful, scenic, and cost-effective study environment. Its Faculty of Medicine provides an accredited 6-year English-medium Medical Doctor (MD / MBBS) program tailored for international students.",
            "overview_p2": "The medical curriculum at Kutaisi University blends strong theoretical foundations with extensive practical training in clinical simulation labs and regional teaching hospitals in the Imereti region. With lower tuition fees and significantly cheaper living expenses than in Tbilisi, UNIK provides an affordable pathway to a genuine European medical degree without compromising academic standards or global recognition.",
            "overview_p3": "For Indian students seeking a budget-friendly MBBS program abroad, Kutaisi University offers an unbeatable option. UNIK is recognized by WHO (WDOMS), NMC (India), WFME (via NCEQE), and ECFMG (USA). Graduates are fully qualified to take the NExT/FMGE exam in India and pursue postgraduate medical training internationally.",
            "clinical_text": "Clinical training at Kutaisi University takes place in major regional multi-profile hospitals and specialized medical centers in Kutaisi. Students complete clinical clerkships in Internal Medicine, General Surgery, Pediatrics, Obstetrics & Gynecology, Neurology, and Emergency Care. The manageable student group sizes in Kutaisi ensure direct patient interaction and personalized bedside teaching by experienced physicians.",
            "facilities_text": "Kutaisi University features a modern campus equipped with clinical simulation labs, digital anatomy facilities, computer rooms, and a comprehensive library connected to global medical research databases. Hostels in Kutaisi provide affordable, comfortable accommodation with heating, Wi-Fi, study facilities, and security. Dedicated Indian mess services and local dining options ensure Indian students have access to fresh, home-style Indian food.",
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
            "short_name": "Tbilisi State Medical University (TSMU)",
            "city": "Tbilisi",
            "established": "1918",
            "type": "Public / Government University",
            "ranking": "Ranked #1 Government Medical University in Georgia",
            "tuition_yr": "8,000 USD",
            "hostel_yr": "1,500 USD",
            "tuition_val": 8000,
            "hostel_val": 1500,
            "img": "/wp-content/uploads/2024/07/Tbilisi-State-Medical-University.jpg",
            "website": "https://tsmu.edu/",
            "keywords": "Tbilisi State Medical University, TSMU Georgia MBBS fees 2026, TSMU Tbilisi ranking, Government medical university in Georgia, TSMU MD Program",
            "description": "Tbilisi State Medical University (TSMU) Georgia MBBS admission 2026. Top government medical university, WHO/NMC recognized, 100% English medium.",
            "overview_p1": "Tbilisi State Medical University (TSMU) is the premier public medical university in Georgia, established in 1918. As the oldest, largest, and most prestigious medical institution in the Caucasus region, TSMU has educated generations of renowned physicians, clinical specialists, and medical researchers over its century-long history. TSMU stands as the undisputed flagship of medical education in Georgia.",
            "overview_p2": "TSMU boasts expansive university clinics, research institutes, high-tech simulation centers, and prestigious international partnerships with top European and American institutions (such as Emory University School of Medicine, USA). The university offers an internationally acclaimed 6-year English-medium Medical Doctor (MD / MBBS) program that attracts thousands of high-achieving medical aspirants globally.",
            "overview_p3": "For Indian students, Tbilisi State Medical University represents the pinnacle of medical study abroad. Its diploma carries immense global prestige, exceptionally high FMGE/NExT pass rates, and direct eligibility pathways for USMLE (USA), PLAB (UK), and European medical licensure boards.",
            "clinical_text": "Clinical training at Tbilisi State Medical University is unmatched in Georgia. TSMU operates multiple state-owned university clinics and collaborates with top tertiary-care hospitals in Tbilisi. Students undergo rigorous bedside rotations across all major medical specialties including Internal Medicine, General & Specialized Surgery, Pediatrics, Cardiology, Oncology, Neurology, and Emergency Medicine, benefiting from high patient inflow and expert faculty supervision.",
            "facilities_text": "TSMU provides an extraordinary campus infrastructure featuring world-class simulation and clinical skills training centers, OSCE laboratories, digital dissection facilities, and the largest medical library in Georgia. University hostels offer secure, fully equipped living spaces for international students. Dedicated Indian dining facilities near the campus provide authentic Indian meals, creating a supportive community for Indian medical aspirants.",
            "faqs": [
                ("Is Tbilisi State Medical University a government university?", "Yes, TSMU is a premier public (government) medical university in Georgia, established in 1918."),
                ("Is TSMU Georgia recognized by NMC and WHO?", "Yes, TSMU is fully recognized by WHO, NMC (India), WFME, ECFMG (USA), and European Ministry of Education."),
                ("What is the tuition fee for MBBS at Tbilisi State Medical University?", "The annual tuition fee for the English-medium MD program at TSMU is approximately 8,000 USD per year."),
                ("What are the FMGE pass rate prospects for TSMU graduates?", "TSMU graduates consistently achieve among the highest FMGE/NExT pass rates in India due to rigorous clinical training and comprehensive basic science grounding."),
                ("How competitive is admission to Tbilisi State Medical University?", "Admission is merit-based and highly sought-after. Applicants require strong academic scores in 12th PCB, NEET qualification, and successful performance in the university entrance interview.")
            ]
        }
    ]

    for uni in universities:
        t_val = uni["tuition_val"]
        h_val = uni["hostel_val"]
        tot_val = t_val + h_val
        
        y_fees = [
            (f"{t_val:,} USD", f"{h_val:,} USD", f"{tot_val:,} USD")
            for _ in range(6)
        ]

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

        body_html = f'''<div data-elementor-type="single-post" data-elementor-id="370" class="elementor elementor-370 elementor-location-single post-1098 post type-post status-publish format-standard has-post-thumbnail hentry category-georgia" data-elementor-post-type="elementor_library">
					<section class="elementor-section elementor-top-section elementor-element elementor-element-6b62a573 elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="6b62a573" data-element_type="section" data-e-type="section" data-settings="{{"background_background":"classic"}}">
							<div class="elementor-background-overlay"></div>
							<div class="elementor-container elementor-column-gap-default">
					<div class="elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-6bd57f2e" data-id="6bd57f2e" data-element_type="column" data-e-type="column">
			<div class="elementor-widget-wrap elementor-element-populated">
						<section class="elementor-section elementor-inner-section elementor-element elementor-element-2fa7700d elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="2fa7700d" data-element_type="section" data-e-type="section">
						<div class="elementor-container elementor-column-gap-default">
					<div class="elementor-column elementor-col-100 elementor-inner-column elementor-element elementor-element-7251eaed elementor-invisible" data-id="7251eaed" data-element_type="column" data-e-type="column" data-settings="{{"animation":"fadeInUp"}}">
			<div class="elementor-widget-wrap elementor-element-populated">
						<div class="elementor-element elementor-element-4502256 elementor-position-left elementor-vertical-align-top elementor-widget elementor-widget-image-box" data-id="4502256" data-element_type="widget" data-e-type="widget" data-widget_type="image-box.default">
				<div class="elementor-widget-container">
					<div class="elementor-image-box-wrapper"><figure class="elementor-image-box-img"><img loading="lazy" width="960" height="960" src="../wp-content/uploads/2024/07/Atlas-Mentor-Circle-White-New.png" class="attachment-full size-full wp-image-478" alt="Atlas Mentor" /></figure><div class="elementor-image-box-content"><h1 class="elementor-image-box-title">{uni["full_name"]} MBBS Fees 2026, Georgia</h1><p class="elementor-image-box-description">Complete, verified guide for Indian students planning to study MBBS at {uni["full_name"]}, Georgia. Explore 2026 tuition fees, eligibility, NMC/WHO recognition, hostels, and step-by-step admission support from Atlas Mentor.</p></div></div>				</div>
				</div>
				<div class="elementor-element elementor-element-4e01cbf9 elementor-widget elementor-widget-post-info" data-id="4e01cbf9" data-element_type="widget" data-e-type="widget" data-widget_type="post-info.default">
				<div class="elementor-widget-container">
							<ul class="elementor-inline-items elementor-icon-list-items elementor-post-info">
								<li class="elementor-icon-list-item elementor-repeater-item-ad7f9cf elementor-inline-item">
													<span class="elementor-icon-list-text elementor-post-info__item elementor-post-info__item--type-custom">
										By Altas Mentor					</span>
								</li>
				<li class="elementor-icon-list-item elementor-repeater-item-4c4e125 elementor-inline-item" itemprop="about">
													<span class="elementor-icon-list-text elementor-post-info__item elementor-post-info__item--type-terms">
							<span class="elementor-post-info__item-prefix">University In </span>
										<span class="elementor-post-info__terms-list">
				<span class="elementor-post-info__terms-list-item">Georgia</span>				</span>
					</span>
								</li>
				<li class="elementor-icon-list-item elementor-repeater-item-8760d45 elementor-inline-item" itemprop="datePublished">
													<span class="elementor-icon-list-text elementor-post-info__item elementor-post-info__item--type-date">
										<time>January 25, 2026</time>					</span>
								</li>
				</ul>
						</div>
				</div>
					</div>
		</div>
					</div>
		</section>
					</div>
		</div>
					</div>
		</section>
				<section class="elementor-section elementor-top-section elementor-element elementor-element-2a270c65 elementor-section-content-middle elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="2a270c65" data-element_type="section" data-e-type="section" data-settings="{{"background_background":"classic"}}">
						<div class="elementor-container elementor-column-gap-default">
					<div class="elementor-column elementor-col-50 elementor-top-column elementor-element elementor-element-16f45f5b" data-id="16f45f5b" data-element_type="column" data-e-type="column">
			<div class="elementor-widget-wrap elementor-element-populated">
						<div class="elementor-element elementor-element-782d8ece elementor-icon-list--layout-inline elementor-list-item-link-inline elementor-mobile-align-start elementor-widget__width-auto elementor-widget-mobile__width-auto elementor-widget elementor-widget-icon-list" data-id="782d8ece" data-element_type="widget" data-e-type="widget" data-widget_type="icon-list.default">
				<div class="elementor-widget-container">
							<ul class="elementor-icon-list-items elementor-inline-items">
							<li class="elementor-icon-list-item elementor-inline-item">
											<a href="/">

											<span class="elementor-icon-list-text">Home</span>
											</a>
									</li>
						</ul>
						</div>
				</div>
				<div class="elementor-element elementor-element-1610eebd elementor-icon-list--layout-inline elementor-list-item-link-inline elementor-mobile-align-start elementor-widget__width-auto elementor-widget-mobile__width-auto elementor-widget elementor-widget-icon-list" data-id="1610eebd" data-element_type="widget" data-e-type="widget" data-widget_type="icon-list.default">
				<div class="elementor-widget-container">
							<ul class="elementor-icon-list-items elementor-inline-items">
							<li class="elementor-icon-list-item elementor-inline-item">
											<a href="/study-mbbs-in-georgia-for-indian-students">

												<span class="elementor-icon-list-icon">
							<svg aria-hidden="true" class="e-font-icon-svg e-fas-chevron-right" viewBox="0 0 320 512" xmlns="http://www.w3.org/2000/svg"><path d="M285.476 272.971L91.132 467.314c-9.373 9.373-24.569 9.373-33.941 0l-22.667-22.667c-9.357-9.357-9.375-24.522-.04-33.901L188.505 256 34.484 101.255c-9.335-9.379-9.317-24.544.04-33.901l22.667-22.667c9.373-9.373 24.569-9.373 33.941 0L285.475 239.03c9.373 9.372 9.373 24.568.001 33.941z"></path></svg>						</span>
										<span class="elementor-icon-list-text"><span>Georgia</span></span>
											</a>
									</li>
						</ul>
						</div>
				</div>
				<div class="elementor-element elementor-element-34f4fb2d elementor-icon-list--layout-inline elementor-list-item-link-inline elementor-mobile-align-start elementor-widget__width-auto elementor-widget-mobile__width-initial elementor-widget elementor-widget-icon-list" data-id="34f4fb2d" data-element_type="widget" data-e-type="widget" data-widget_type="icon-list.default">
				<div class="elementor-widget-container">
							<ul class="elementor-icon-list-items elementor-inline-items">
							<li class="elementor-icon-list-item elementor-inline-item">
											<a href="/{uni["slug"]}">

												<span class="elementor-icon-list-icon">
							<svg aria-hidden="true" class="e-font-icon-svg e-fas-chevron-right" viewBox="0 0 320 512" xmlns="http://www.w3.org/2000/svg"><path d="M285.476 272.971L91.132 467.314c-9.373 9.373-24.569 9.373-33.941 0l-22.667-22.667c-9.357-9.357-9.375-24.522-.04-33.901L188.505 256 34.484 101.255c-9.335-9.379-9.317-24.544.04-33.901l22.667-22.667c9.373-9.373 24.569-9.373 33.941 0L285.475 239.03c9.373 9.372 9.373 24.568.001 33.941z"></path></svg>						</span>
										<span class="elementor-icon-list-text">{uni["full_name"]}, Georgia</span>
											</a>
									</li>
						</ul>
						</div>
				</div>
					</div>
		</div>
				<div class="elementor-column elementor-col-50 elementor-top-column elementor-element elementor-element-7bd9cf1" data-id="7bd9cf1" data-element_type="column" data-e-type="column">
			<div class="elementor-widget-wrap elementor-element-populated">
						<div class="elementor-element elementor-element-6bd4e680 elementor-align-justify elementor-widget elementor-widget-button" data-id="6bd4e680" data-element_type="widget" data-e-type="widget" data-widget_type="button.default">
				<div class="elementor-widget-container">
									<div class="elementor-button-wrapper">
					<a class="elementor-button elementor-button-link elementor-size-xs" href="/study-mbbs-in-georgia-for-indian-students">
						<span class="elementor-button-content-wrapper">
									<span class="elementor-button-text"># <span>Georgia</span></span>
					</span>
					</a>
				</div>
								</div>
				</div>
					</div>
		</div>
					</div>
		</section>
				<section class="elementor-section elementor-top-section elementor-element elementor-element-687182a6 elementor-section-boxed elementor-section-height-default elementor-section-height-default" data-id="687182a6" data-element_type="section" data-e-type="section" data-settings="{{"background_background":"classic"}}">
							<div class="elementor-background-overlay"></div>
							<div class="elementor-container elementor-column-gap-default">
					<div class="elementor-column elementor-col-50 elementor-top-column elementor-element elementor-element-62630e83" data-id="62630e83" data-element_type="column" data-e-type="column" data-settings="{{"background_background":"classic"}}">
			<div class="elementor-widget-wrap elementor-element-populated">
						<div class="elementor-element elementor-element-13253c7 elementor-widget elementor-widget-theme-post-featured-image elementor-widget-image" data-id="13253c7" data-element_type="widget" data-e-type="widget" data-widget_type="theme-post-featured-image.default">
				<div class="elementor-widget-container">
															<img loading="lazy" width="1024" height="753" src="..{uni["img"]}" class="attachment-full size-full wp-image-1453" alt="{uni["full_name"]} Georgia" sizes="(max-width: 1024px) 100vw, 1024px" />							</div>
				</div>
				<div class="elementor-element elementor-element-366b8e84 elementor-widget elementor-widget-theme-post-content" data-id="366b8e84" data-element_type="widget" data-e-type="widget" data-widget_type="theme-post-content.default">
				<div class="elementor-widget-container">
							<div data-elementor-type="wp-post" data-elementor-id="1376" class="elementor elementor-1376" data-elementor-post-type="post">
				<div class="elementor-element elementor-element-4541197 e-con-full e-flex e-con e-parent" data-id="4541197" data-element_type="container" data-e-type="container">
				<div class="elementor-element elementor-element-94146dd elementor-widget elementor-widget-heading" data-id="94146dd" data-element_type="widget" data-e-type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
					<h2 class="elementor-heading-title elementor-size-default">{uni["full_name"]}, Georgia</h2>				</div>
				</div>
				<div class="elementor-element elementor-element-1547eb8 elementor-widget elementor-widget-text-editor" data-id="1547eb8" data-element_type="widget" data-e-type="widget" data-widget_type="text-editor.default">
				<div class="elementor-widget-container">
									<p>{uni["overview_p1"]}</p><p>{uni["overview_p2"]}</p><p>{uni["overview_p3"]}</p>								</div>
				</div>
				<div class="elementor-element elementor-element-c54e09c elementor-widget elementor-widget-image" data-id="c54e09c" data-element_type="widget" data-e-type="widget" data-widget_type="image.default">
				<div class="elementor-widget-container">
															<img fetchpriority="high" decoding="async" width="875" height="500" src="../wp-content/uploads/2025/02/Study-MBBS-in-Georgia.png" class="attachment-full size-full wp-image-1454" alt="Campus Facilities at {uni["full_name"]}" sizes="(max-width: 875px) 100vw, 875px" />							</div>
				</div>
				<div class="elementor-element elementor-element-3774fb3 elementor-widget elementor-widget-text-editor" data-id="3774fb3" data-element_type="widget" data-e-type="widget" data-widget_type="text-editor.default">
				<div class="elementor-widget-container">
									<p>Studying MBBS at {uni["full_name"]} provides Indian students with a holistic medical education experience. The university curriculum combines core basic medical sciences during the pre-clinical years with intensive bedside rotations across tertiary-care university hospitals during the clinical phase.</p><p>Students at {uni["full_name"]} benefit from low student-to-teacher ratios, personalized mentoring, modern research laboratories, and access to digital medical libraries containing over 100,000 international journals and reference books. Additionally, the university organizes annual student scientific conferences, medical exchange programs across Europe, and structured USMLE & FMGE/NExT preparation modules.</p>								</div>
				</div>
				<div class="elementor-element elementor-element-9cb32d1 elementor-widget elementor-widget-heading" data-id="9cb32d1" data-element_type="widget" data-e-type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
					<h2 class="elementor-heading-title elementor-size-default">Quick Highlights of {uni["full_name"]}, Georgia</h2>				</div>
				</div>
				<div class="elementor-element elementor-element-2487c4e elementor-widget elementor-widget-text-editor" data-id="2487c4e" data-element_type="widget" data-e-type="widget" data-widget_type="text-editor.default">
				<div class="elementor-widget-container">
									<table><tbody><tr><td>Year of Establishment</td><td>{uni["established"]}</td></tr><tr><td>Type</td><td>{uni["type"]}</td></tr><tr><td>Recognition</td><td>NMC (India), WHO (WDOMS), WFME / NCEQE, ECFMG (USA) approved</td></tr><tr><td>Eligibility</td><td>50% in PCB (12th Grade) + NEET Qualified</td></tr><tr><td>Course Duration</td><td>6 Academic Years (5 Years Study + 1 Year Internship)</td></tr><tr><td>NEET Required</td><td>Yes (Mandatory for Indian aspirants)</td></tr><tr><td>Medium of Teaching</td><td>100% English Medium</td></tr><tr><td>Ranking</td><td>{uni["ranking"]}</td></tr></tbody></table>								</div>
				</div>
				<div class="elementor-element elementor-element-9de8a74 elementor-widget elementor-widget-heading" data-id="9de8a74" data-element_type="widget" data-e-type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
					<h2 class="elementor-heading-title elementor-size-default">Affiliation and Recognition of {uni["full_name"]}, Georgia</h2>				</div>
				</div>
				<div class="elementor-element elementor-element-a0a1bc3 elementor-widget elementor-widget-text-editor" data-id="a0a1bc3" data-element_type="widget" data-e-type="widget" data-widget_type="text-editor.default">
				<div class="elementor-widget-container">
									<p>{uni["full_name"]} holds major international accreditations and legal recognitions, ensuring that medical degrees awarded to graduates are valid, respected, and legally accepted worldwide.</p><p><strong>World Health Organization (WHO) & WDOMS Listing</strong>: The university is officially registered in the World Directory of Medical Schools (WDOMS), validating its medical program across international jurisdictions.</p><p><strong>National Medical Council (NMC, India)</strong>: Fully compliant with the NMC Foreign Medical Graduate Licentiate (FMGL) Regulations 2021. Indian graduates from {uni["full_name"]} are eligible to sit for the NExT / FMGE licensing examination in India.</p><p><strong>National Center for Educational Quality Enhancement (NCEQE) & WFME</strong>: Accredited by Georgia’s national quality agency NCEQE under World Federation for Medical Education (WFME) standards, guaranteeing European education quality.</p><p><strong>Educational Commission for Foreign Medical Graduates (ECFMG, USA)</strong>: ECFMG certification eligibility allows graduates of {uni["full_name"]} to apply for USMLE Step 1, Step 2 CK, and US residency programs.</p><p><strong>Ministry of Education and Science of Georgia</strong>: Operating under full state authorization, ensuring strict adherence to European Higher Education Area (EHEA) and Bologna Process guidelines.</p>								</div>
				</div>
				<div class="elementor-element elementor-element-fb2414b elementor-widget elementor-widget-template" data-id="fb2414b" data-element_type="widget" data-e-type="widget" data-widget_type="template.default">
				<div class="elementor-widget-container">
							<div class="elementor-template">
					<div data-elementor-type="section" data-elementor-id="1585" class="elementor elementor-1585 elementor-location-single" data-elementor-post-type="elementor_library">
			<div class="elementor-element elementor-element-5d4543b e-flex e-con-boxed e-con e-parent" data-id="5d4543b" data-element_type="container" data-e-type="container">
					<div class="e-con-inner">
				<div class="elementor-element elementor-element-4de98a0 elementor-widget elementor-widget-heading" data-id="4de98a0" data-element_type="widget" data-e-type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
					<h2 class="elementor-heading-title elementor-size-default">Get Call Back from Atlas Mentor Counsellors</h2>				</div>
				</div>
				<div class="elementor-element elementor-element-17a95cc elementor-widget__width-inherit elementor-button-align-stretch elementor-widget elementor-widget-form" data-id="17a95cc" data-element_type="widget" data-e-type="widget" data-settings="{{"button_width_tablet":"100","step_next_label":"Next","step_previous_label":"Previous","button_width":"100","step_type":"number_text","step_icon_shape":"circle"}}" data-widget_type="form.default">
				<div class="elementor-widget-container">
							<form class="elementor-form" method="post" name="Admission Form">
			<input type="hidden" name="post_id" value="1585"/>
			<input type="hidden" name="form_id" value="17a95cc"/>
			<input type="hidden" name="referer_title" value="{uni["full_name"]}, Georgia" />
			<input type="hidden" name="queried_id" value="1318"/>
			
			<div class="elementor-form-fields-wrapper elementor-labels-above">
								<div class="elementor-field-type-text elementor-field-group elementor-column elementor-field-group-email elementor-col-50 elementor-md-100 elementor-field-required elementor-mark-required">
												<label for="form-field-email" class="elementor-field-label">Full Name</label>
														<input size="1" type="text" name="form_fields[email]" id="form-field-email" class="elementor-field elementor-size-sm elementor-field-textual" placeholder="Full Name" required="required">
											</div>
								<div class="elementor-field-type-tel elementor-field-group elementor-column elementor-field-group-field_d414596 elementor-col-50 elementor-field-required elementor-mark-required">
												<label for="form-field-field_d414596" class="elementor-field-label">Mobile Number</label>
								<input size="1" type="tel" name="form_fields[field_d414596]" id="form-field-field_d414596" class="elementor-field elementor-size-sm elementor-field-textual" placeholder="Mobile Number" required="required" pattern="[0-9()#&amp;+*-=.]+" title="Only numbers and phone characters (#, -, *, etc) are accepted.">
						</div>
								<div class="elementor-field-type-email elementor-field-group elementor-column elementor-field-group-field_171c35b elementor-col-50 elementor-field-required elementor-mark-required">
												<label for="form-field-field_171c35b" class="elementor-field-label">Email Address</label>
														<input size="1" type="email" name="form_fields[field_171c35b]" id="form-field-field_171c35b" class="elementor-field elementor-size-sm elementor-field-textual" placeholder="Email Address" required="required">
											</div>
								<div class="elementor-field-type-select elementor-field-group elementor-column elementor-field-group-field_e023343 elementor-col-50 elementor-field-required elementor-mark-required">
												<label for="form-field-field_e023343" class="elementor-field-label">Preferred Country</label>
								<div class="elementor-field elementor-select-wrapper remove-before ">
			<div class="select-caret-down-wrapper">
				<svg aria-hidden="true" class="e-font-icon-svg e-eicon-caret-down" viewBox="0 0 571.4 571.4" xmlns="http://www.w3.org/2000/svg"><path d="M571 393Q571 407 561 418L311 668Q300 679 286 679T261 668L11 418Q0 407 0 393T11 368 36 357H536Q550 357 561 368T571 393Z"></path></svg>			</div>
			<select name="form_fields[field_e023343]" id="form-field-field_e023343" class="elementor-field-textual elementor-size-sm" required="required">
									<option value="MBBS In Georgia" selected>MBBS In Georgia</option>
									<option value="MBBS In Russia">MBBS In Russia</option>
									<option value="MBBS In Vietnam">MBBS In Vietnam</option>
									<option value="MBBS In Moldova">MBBS In Moldova</option>
									<option value="MBBS In Uzbekistan">MBBS In Uzbekistan</option>
									<option value="MBBS In Kyrgyzstan">MBBS In Kyrgyzstan</option>
									<option value="MBBS In Kazakhstan">MBBS In Kazakhstan</option>
							</select>
		</div>
						</div>
								<div class="elementor-field-type-text elementor-field-group elementor-column elementor-field-group-field_55f4d96 elementor-col-100">
												<label for="form-field-field_55f4d96" class="elementor-field-label">Preferred University</label>
														<input size="1" type="text" name="form_fields[field_55f4d96]" id="form-field-field_55f4d96" class="elementor-field elementor-size-sm elementor-field-textual" placeholder="Preferred University" value="{uni["full_name"]}">
											</div>
								<div class="elementor-field-group elementor-column elementor-field-type-submit elementor-col-100 e-form__buttons elementor-md-100">
					<button class="elementor-button elementor-size-md" type="submit">
						<span class="elementor-button-content-wrapper">
														<span class="elementor-button-text">Submit Now</span>
													</span>
					</button>
				</div>
			</div>
		</form>
						</div>
				</div>
					</div>
				</div>
				</div>
				</div>
						</div>
				</div>
				<div class="elementor-element elementor-element-c47d893 elementor-widget elementor-widget-heading" data-id="c47d893" data-element_type="widget" data-e-type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
					<h2 class="elementor-heading-title elementor-size-default">MBBS Course Duration & Year-Wise Syllabus at {uni["full_name"]}, Georgia</h2>				</div>
				</div>
				<div class="elementor-element elementor-element-d201e56 elementor-widget elementor-widget-text-editor" data-id="d201e56" data-element_type="widget" data-e-type="widget" data-widget_type="text-editor.default">
				<div class="elementor-widget-container">
									<p>The Medical Doctor (MD / MBBS equivalent) program at {uni["full_name"]} spans a total duration of <strong>6 Academic Years</strong> (360 ECTS credits), structured in accordance with NMC FMGL Regulations 2021:</p><p><strong>Year 1: Basic Medical Foundations</strong>: Human Anatomy & Embryology, Medical Histology, General Biochemistry, Medical Biology & Genetics, Biophysics, Georgian Language & Cultural History.</p><p><strong>Year 2: Pre-Clinical Sciences</strong>: Human Physiology, General Pathology, Microbiology & Virology, Immunology, Basic Pharmacology, Medical Ethics & Psychology.</p><p><strong>Year 3: Introduction to Clinical Medicine</strong>: Pathophysiology, Clinical Pharmacology, Internal Medicine Diagnostics, General Surgery & Traumatology, Radiology & Medical Imaging.</p><p><strong>Year 4: Clinical Medicine & Surgery</strong>: Cardiology, Gastroenterology, Pulmonology, Surgical Specialties, Neurology, Pediatrics I, Psychiatry & Behavioral Sciences.</p><p><strong>Year 5: Advanced Specialties & Community Medicine</strong>: Obstetrics & Gynecology, Ophthalmology, Otorhinolaryngology (ENT), Dermatology & Venereology, Oncology, Public Health & Epidemiology.</p><p><strong>Year 6: Compulsory Rotating Internship</strong>: 12-month intensive clinical clerkships across Internal Medicine, Surgery, Emergency Care, Pediatrics, and OB/GYN in affiliated university teaching hospitals.</p>								</div>
				</div>
				<div class="elementor-element elementor-element-87ea517 elementor-widget elementor-widget-image" data-id="87ea517" data-element_type="widget" data-e-type="widget" data-widget_type="image.default">
				<div class="elementor-widget-container">
															<img decoding="async" width="875" height="500" src="../wp-content/uploads/2025/02/Study-MBBS-in-Georgia.png" class="attachment-full size-full wp-image-1455" alt="Facilities At {uni["full_name"]}" sizes="(max-width: 875px) 100vw, 875px" />							</div>
				</div>
				<div class="elementor-element elementor-element-1a8b4fb elementor-widget elementor-widget-heading" data-id="1a8b4fb" data-element_type="widget" data-e-type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
					<h2 class="elementor-heading-title elementor-size-default">Clinical Training & Hospital Affiliations at {uni["full_name"]}</h2>				</div>
				</div>
				<div class="elementor-element elementor-element-cdba50e elementor-widget elementor-widget-text-editor" data-id="cdba50e" data-element_type="widget" data-e-type="widget" data-widget_type="text-editor.default">
				<div class="elementor-widget-container">
									<p>{uni["clinical_text"]}</p><p>Bedside clinical training is emphasized throughout the clinical years. Students work in small groups under direct mentor guidance, acquiring practical skills in patient examination, diagnostic workups, emergency resuscitation, surgical assisting, and clinical case presentations.</p>								</div>
				</div>
				<div class="elementor-element elementor-element-1a8b4fb elementor-widget elementor-widget-heading" data-id="1a8b4fb" data-element_type="widget" data-e-type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
					<h2 class="elementor-heading-title elementor-size-default">Facilities & Student Accommodation at {uni["full_name"]}, Georgia</h2>				</div>
				</div>
				<div class="elementor-element elementor-element-cdba50e elementor-widget elementor-widget-text-editor" data-id="cdba50e" data-element_type="widget" data-e-type="widget" data-widget_type="text-editor.default">
				<div class="elementor-widget-container">
									<p>{uni["facilities_text"]}</p><p>Students enjoy a safe, vibrant European living experience. Hostels offer 24/7 security control, biometric entry systems, study lounges, fully automatic washing machines, and high-speed Wi-Fi. Indian students can easily access authentic North and South Indian food through dedicated dining halls and nearby Indian restaurants.</p>								</div>
				</div>
				<div class="elementor-element elementor-element-77fc4ff elementor-widget elementor-widget-image" data-id="77fc4ff" data-element_type="widget" data-e-type="widget" data-widget_type="image.default">
				<div class="elementor-widget-container">
															<img decoding="async" width="875" height="500" src="../wp-content/uploads/2025/02/Study-MBBS-in-Georgia.png" class="attachment-full size-full wp-image-1457" alt="Eligibility Criteria To Study at {uni["full_name"]}" sizes="(max-width: 875px) 100vw, 875px" />							</div>
				</div>
				<div class="elementor-element elementor-element-7c4d681 elementor-widget elementor-widget-heading" data-id="7c4d681" data-element_type="widget" data-e-type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
					<h2 class="elementor-heading-title elementor-size-default">Eligibility Criteria To Study at {uni["full_name"]}, Georgia</h2>				</div>
				</div>
				<div class="elementor-element elementor-element-d864435 elementor-widget elementor-widget-text-editor" data-id="d864435" data-element_type="widget" data-e-type="widget" data-widget_type="text-editor.default">
				<div class="elementor-widget-container">
									<p>To secure admission for the MBBS / MD course at {uni["full_name"]}, Indian candidates must satisfy the following eligibility requirements:</p><p><strong>Age Criterion</strong>: The applicant must be at least 17 years of age on or before December 31st of the admission year.</p><p><strong>Educational Qualification</strong>: The student must have completed 10+2 (Higher Secondary) from a recognized Indian education board (CBSE, ICSE, or State Board) with Physics, Chemistry, Biology, and English as core subjects, obtaining a minimum aggregate score of 50% in PCB (40% for SC/ST/OBC category candidates).</p><p><strong>NEET Qualification</strong>: Qualifying the NEET-UG examination in the year of application (or having a valid NEET score from the previous two years) is mandatory as mandated by NMC for Indian students studying abroad.</p><p><strong>Language Proficiency</strong>: No IELTS or TOEFL exam score is required, provided the applicant completed secondary education with English medium and passes the university's internal English comprehension interview.</p>								</div>
				</div>
				<div class="elementor-element elementor-element-50f9af5 elementor-widget elementor-widget-heading" data-id="50f9af5" data-element_type="widget" data-e-type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
					<h2 class="elementor-heading-title elementor-size-default">Why Indian Students Choose {uni["full_name"]}, Georgia</h2>				</div>
				</div>
				<div class="elementor-element elementor-element-ee8d797 elementor-widget elementor-widget-text-editor" data-id="ee8d797" data-element_type="widget" data-e-type="widget" data-widget_type="text-editor.default">
				<div class="elementor-widget-container">
									<p>{uni["full_name"]} continues to be a top-choice destination for Indian medical aspirants due to several distinct advantages:</p><p><strong>100% English Medium Curriculum</strong>: All lectures, practical classes, seminars, and clinical postings are conducted entirely in English, eliminating language barriers.</p><p><strong>Global Accreditation & NMC Compliance</strong>: Degrees awarded are recognized by WHO, NMC, WFME, and ECFMG, allowing graduates to practice in India, USA, UK, Canada, and Europe.</p><p><strong>No Donation or Capitation Fees</strong>: Admissions are conducted strictly on merit without any hidden capitation fees or extra charges.</p><p><strong>Advanced Medical Simulation Labs</strong>: Students train on high-tech robotic mannequins and 3D virtual dissection tables prior to hospital clinical postings.</p><p><strong>High Safety & European Quality of Life</strong>: Georgia is rated among the safest countries in the world, offering a peaceful environment, clean air, and high living standards.</p><p><strong>FMGE / NExT & USMLE Prep Support</strong>: The university offers specialized guidance and coaching assistance for competitive licensing examinations.</p><p><strong>Active Indian Community & Festivals</strong>: Indian students celebrate major cultural festivals including Diwali, Holi, and Independence Day with great enthusiasm on campus.</p>								</div>
				</div>
				<div class="elementor-element elementor-element-50f9af5 elementor-widget elementor-widget-heading" data-id="50f9af5" data-element_type="widget" data-e-type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
					<h2 class="elementor-heading-title elementor-size-default">FMGE / NExT & USMLE Career Opportunities</h2>				</div>
				</div>
				<div class="elementor-element elementor-element-ee8d797 elementor-widget elementor-widget-text-editor" data-id="ee8d797" data-element_type="widget" data-e-type="widget" data-widget_type="text-editor.default">
				<div class="elementor-widget-container">
									<p>Graduating from {uni["full_name"]} opens up global medical career pathways for Indian medical students:</p><p><strong>Practice in India (NExT / FMGE)</strong>: Because {uni["full_name"]} complies with all NMC FMGL 2021 regulations (6-year duration, English medium, clinical subjects, hands-on internship), graduates are fully eligible to sit for NExT / FMGE licensing exams in India.</p><p><strong>Practice in USA (USMLE Pathway)</strong>: With ECFMG certification eligibility, students can take USMLE Step 1 and Step 2 CK during their senior years and apply for US residency programs.</p><p><strong>Practice in UK & Europe (PLAB / GMC)</strong>: The European standard curriculum enables direct registration eligibility for PLAB (UK General Medical Council) and licensing across EU member states.</p>								</div>
				</div>
				<div class="elementor-element elementor-element-50f9af5 elementor-widget elementor-widget-heading" data-id="50f9af5" data-element_type="widget" data-e-type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
					<h2 class="elementor-heading-title elementor-size-default">Comparison: MBBS in Georgia vs MBBS in India (Private Colleges)</h2>				</div>
				</div>
				<div class="elementor-element elementor-element-4081195 elementor-widget elementor-widget-text-editor" data-id="4081195" data-element_type="widget" data-e-type="widget" data-widget_type="text-editor.default">
				<div class="elementor-widget-container">
									<table><tbody><tr><th>Factor</th><th>MBBS at {uni["full_name"]} (Georgia)</th><th>Indian Private Medical Colleges</th></tr><tr><td>Total Fee Package</td><td>₹25 Lakhs – ₹38 Lakhs (Total 6 Years)</td><td>₹70 Lakhs – ₹1.2 Crore</td></tr><tr><td>Donation / Capitation</td><td>Zero (Strictly No Donation)</td><td>High Capitation Fees in Many Colleges</td></tr><tr><td>Medium of Instruction</td><td>100% English Medium</td><td>English</td></tr><tr><td>Global Recognition</td><td>WHO, NMC, WFME, ECFMG (Worldwide)</td><td>NMC (India)</td></tr><tr><td>Living Standards</td><td>High European Living Standards & Top Safety</td><td>Varies by State & City</td></tr><tr><td>Hospital Exposure</td><td>Hands-on Bedside Rotations in Multi-Specialty Hospitals</td><td>Varies based on patient intake</td></tr></tbody></table>								</div>
				</div>
				<div class="elementor-element elementor-element-dfa8296 elementor-widget elementor-widget-heading" data-id="dfa8296" data-element_type="widget" data-e-type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
					<h2 class="elementor-heading-title elementor-size-default">Documents Required for Admission At {uni["full_name"]}, Georgia</h2>				</div>
				</div>
				<div class="elementor-element elementor-element-4b43af7 elementor-widget elementor-widget-text-editor" data-id="4b43af7" data-element_type="widget" data-e-type="widget" data-widget_type="text-editor.default">
				<div class="elementor-widget-container">
									<p>Applicants must assemble and submit clear scanned copies of the following documents during the admission process:</p><p><strong>1. Completed Application Form</strong>: Duly filled online application form.</p><p><strong>2. Class 10 & Class 12 Marksheets</strong>: Original marksheets and passing certificates.</p><p><strong>3. Valid Passport</strong>: Original passport with at least 2 years of remaining validity.</p><p><strong>4. NEET Scorecard</strong>: Official NEET-UG result scorecard demonstrating qualifying marks.</p><p><strong>5. Passport-Sized Photographs</strong>: 10 recent passport-size photos with a white background.</p><p><strong>6. Birth Certificate</strong>: Certified copy of official birth certificate.</p><p><strong>7. Medical Fitness Certificate</strong>: Medical health checkup report including HIV negative test report.</p><p><strong>8. Transfer / Migration Certificate</strong>: School leaving certificate from the previous school board.</p>								</div>
				</div>
				<div class="elementor-element elementor-element-3b8d9f4 elementor-widget elementor-widget-heading" data-id="3b8d9f4" data-element_type="widget" data-e-type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
					<h2 class="elementor-heading-title elementor-size-default">Step-by-Step Admission Procedure at {uni["full_name"]} via Atlas Mentor</h2>				</div>
				</div>
				<div class="elementor-element elementor-element-8fdefcd elementor-widget elementor-widget-text-editor" data-id="8fdefcd" data-element_type="widget" data-e-type="widget" data-widget_type="text-editor.default">
				<div class="elementor-widget-container">
									<p>The admission process at {uni["full_name"]} is streamlined and handled transparently by Atlas Mentor:</p><p><strong>Step 1: Application Submission</strong>: Submit your 10th & 12th marksheets, NEET scorecard, and passport copy to Atlas Mentor for preliminary eligibility evaluation.</p><p><strong>Step 2: Document Verification & Video Interview</strong>: The university reviews academic documents and schedules a brief online English proficiency video interview.</p><p><strong>Step 3: Receipt of Admission Offer Letter</strong>: Upon successful verification, {uni["full_name"]} issues an official Admission Offer Letter within 3–5 working days.</p><p><strong>Step 4: Ministry Approval & EQE Order</strong>: Atlas Mentor submits student documents to the National Center for Educational Quality Enhancement (EQE) and Ministry of Education and Science of Georgia for state recognition.</p><p><strong>Step 5: Official Ministry Recognition & Visa Invitation Letter</strong>: The Georgian Ministry issues official Rector's Order and Visa Approval Letter.</p><p><strong>Step 6: Student Visa Application</strong>: Atlas Mentor handles student visa filing with the Embassy of Georgia, guiding students through VFS appointments and document submission.</p><p><strong>Step 7: Flight Booking & Departure</strong>: Upon visa issuance, Atlas Mentor arranges group flight departures, airport reception in Georgia, hostel check-in, and university registration.</p>								</div>
				</div>
				<div class="elementor-element elementor-element-4551af3 elementor-widget elementor-widget-heading" data-id="4551af3" data-element_type="widget" data-e-type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
					<h2 class="elementor-heading-title elementor-size-default">Fees Structure of {uni["full_name"]}, Georgia</h2>				</div>
				</div>
				<div class="elementor-element elementor-element-4081195 elementor-widget elementor-widget-text-editor" data-id="4081195" data-element_type="widget" data-e-type="widget" data-widget_type="text-editor.default">
				<div class="elementor-widget-container">
									<table><tbody><tr><th>Particulars</th><th>Year 1</th><th>Year 2</th><th>Year 3</th><th>Year 4</th><th>Year 5</th><th>Year 6</th></tr><tr><td>Tuition Fee</td><td>{y_fees[0][0]}</td><td>{y_fees[1][0]}</td><td>{y_fees[2][0]}</td><td>{y_fees[3][0]}</td><td>{y_fees[4][0]}</td><td>{y_fees[5][0]}</td></tr><tr><td>Hostel & Living Fee</td><td>{y_fees[0][1]}</td><td>{y_fees[1][1]}</td><td>{y_fees[2][1]}</td><td>{y_fees[3][1]}</td><td>{y_fees[4][1]}</td><td>{y_fees[5][1]}</td></tr><tr><td>Total (USD)</td><td>{y_fees[0][2]}</td><td>{y_fees[1][2]}</td><td>{y_fees[2][2]}</td><td>{y_fees[3][2]}</td><td>{y_fees[4][2]}</td><td>{y_fees[5][2]}</td></tr></tbody></table>								</div>
				</div>
				<div class="elementor-element elementor-element-2431703 elementor-widget elementor-widget-text-editor" data-id="2431703" data-element_type="widget" data-e-type="widget" data-widget_type="text-editor.default">
				<div class="elementor-widget-container">
									<p>{uni["full_name"]} maintains a transparent fee structure without hidden charges or capitation fees.</p><p>The annual tuition fee is <strong>{uni["tuition_yr"]}</strong>, and hostel accommodation expenses average <strong>{uni["hostel_yr"]}</strong> per year. Fees are payable directly to the university's official bank account on an annual basis.</p><p><em>Note: Fee amounts in Indian Rupees (INR) are subject to prevailing foreign exchange currency rates. Currently calculated at an estimated benchmark rate of 1 USD = ₹84.00 INR.</em></p>								</div>
				</div>
				<div class="elementor-element elementor-element-b8dca6e elementor-widget elementor-widget-image" data-id="b8dca6e" data-element_type="widget" data-e-type="widget" data-widget_type="image.default">
				<div class="elementor-widget-container">
															<img loading="lazy" decoding="async" width="875" height="500" src="../wp-content/uploads/2025/02/Study-MBBS-in-Georgia.png" class="attachment-full size-full wp-image-1456" alt="FAQs on {uni["full_name"]}" sizes="(max-width: 875px) 100vw, 875px" />							</div>
				</div>
				<div class="elementor-element elementor-element-c76cb6a elementor-widget elementor-widget-heading" data-id="c76cb6a" data-element_type="widget" data-e-type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
					<h2 class="elementor-heading-title elementor-size-default">Frequently Asked Questions (FAQs) About {uni["full_name"]}, Georgia</h2>				</div>
				</div>
				<div class="elementor-element elementor-element-e5b8622 elementor-widget elementor-widget-text-editor" data-id="e5b8622" data-element_type="widget" data-e-type="widget" data-widget_type="text-editor.default">
				<div class="elementor-widget-container">
									<p>Here are the most frequently asked questions by Indian students and parents regarding MBBS admission at {uni["full_name"]}, Georgia:</p>								</div>
				</div>
				<div class="elementor-element elementor-element-f462f56 elementor-widget elementor-widget-elementskit-accordion" data-id="f462f56" data-element_type="widget" data-e-type="widget" data-widget_type="elementskit-accordion.default">
				<div class="elementor-widget-container">
					<div class="ekit-wid-con" >
        <div class="elementskit-accordion accoedion-primary" id="accordion-6a3ad4a740750">
{faq_accordion_full}
        </div>
        </div>				</div>
				</div>
				</div>
				</div>
				</div>
						</div>
				</div>
				<div class="elementor-element elementor-element-72628f4f elementor-widget__width-auto elementor-widget elementor-widget-heading" data-id="72628f4f" data-element_type="widget" data-e-type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
					<h5 class="elementor-heading-title elementor-size-default">Tags :</h5>				</div>
				</div>
				<div class="elementor-element elementor-element-595336c0 elementor-share-buttons--skin-flat elementor-share-buttons--view-text elementor-grid-5 elementor-share-buttons--color-custom elementor-share-buttons--shape-square elementor-widget elementor-widget-share-buttons" data-id="595336c0" data-element_type="widget" data-e-type="widget" data-widget_type="share-buttons.default">
				<div class="elementor-widget-container">
							<div class="elementor-grid">
								<div class="elementor-grid-item">
						<div class="elementor-share-btn elementor-share-btn_facebook" role="button" tabindex="0" aria-label="Share on facebook">
									<div class="elementor-share-btn__text">
											<span class="elementor-share-btn__title">Facebook</span>
									</div>
						</div>
					</div>
									<div class="elementor-grid-item">
						<div class="elementor-share-btn elementor-share-btn_twitter" role="button" tabindex="0" aria-label="Share on twitter">
									<div class="elementor-share-btn__text">
											<span class="elementor-share-btn__title">Twitter</span>
									</div>
						</div>
					</div>
									<div class="elementor-grid-item">
						<div class="elementor-share-btn elementor-share-btn_linkedin" role="button" tabindex="0" aria-label="Share on linkedin">
									<div class="elementor-share-btn__text">
											<span class="elementor-share-btn__title">LinkedIn</span>
									</div>
						</div>
					</div>
									<div class="elementor-grid-item">
						<div class="elementor-share-btn elementor-share-btn_whatsapp" role="button" tabindex="0" aria-label="Share on whatsapp">
									<div class="elementor-share-btn__text">
											<span class="elementor-share-btn__title">WhatsApp</span>
									</div>
						</div>
					</div>
						</div>
						</div>
				</div>
				<div class="elementor-element elementor-element-1119c26 elementor-widget-divider--view-line elementor-widget elementor-widget-divider" data-id="1119c26" data-element_type="widget" data-e-type="widget" data-widget_type="divider.default">
				<div class="elementor-widget-container">
							<div class="elementor-divider">
			<span class="elementor-divider-separator"></span>
		</div>
						</div>
				</div>
					</div>
		</div>
				<div class="elementor-column elementor-col-50 elementor-top-column elementor-element elementor-element-1fcc2822" data-id="1fcc2822" data-element_type="column" data-e-type="column">
			<div class="elementor-widget-wrap elementor-element-populated">
						<div class="elementor-element elementor-element-1c1ed601 elementor-author-box--layout-image-left elementor-author-box--align-left elementor-author-box--image-valign-top elementor-widget elementor-widget-author-box" data-id="1c1ed601" data-element_type="widget" data-e-type="widget" data-widget_type="author-box.default">
				<div class="elementor-widget-container">
							<div class="elementor-author-box">
							<div class="elementor-author-box__avatar">
					<img src="../wp-content/uploads/2024/07/Atlas-Mentor-Circle-Transparent-300x300.png" alt="Picture of Atlas Mentor" loading="lazy">
				</div>
			<div class="elementor-author-box__text">
									<div>
						<div class="elementor-author-box__name">Atlas Mentor</div>
					</div>
									<div class="elementor-author-box__bio">
						<p>A beacon of guidance for aspiring medical professionals, offers expert assistance in pursuing MBBS abroad.</p>
					</div>
							</div>
		</div>
						</div>
				</div>
				<div class="elementor-element elementor-element-4232219f elementor-widget elementor-widget-heading" data-id="4232219f" data-element_type="widget" data-e-type="widget" data-settings="{{"_animation":"none"}}" data-widget_type="heading.default">
				<div class="elementor-widget-container">
					<h2 class="elementor-heading-title elementor-size-default">Study Abroad Location</h2>				</div>
				</div>
				<div class="elementor-element elementor-element-75c031a elementor-icon-list--layout-traditional elementor-list-item-link-full_width elementor-widget elementor-widget-icon-list" data-id="75c031a" data-element_type="widget" data-e-type="widget" data-widget_type="icon-list.default">
				<div class="elementor-widget-container">
							<ul class="elementor-icon-list-items">
							<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<svg aria-hidden="true" class="e-font-icon-svg e-fas-check" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M173.898 439.404l-166.4-166.4c-9.997-9.997-9.997-26.206 0-36.204l36.203-36.204c9.997-9.998 26.207-9.998 36.204 0L192 312.69 432.095 72.596c9.997-9.997 26.207-9.997 36.204 0l36.203 36.204c9.997 9.997 9.997 26.206 0 36.204l-294.4 294.401c-9.998 9.997-26.207 9.997-36.204-.001z"></path></svg>						</span>
										<span class="elementor-icon-list-text"><a href="/study-mbbs-in-georgia-for-indian-students">MBBS In Georgia</a></span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<svg aria-hidden="true" class="e-font-icon-svg e-fas-check" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M173.898 439.404l-166.4-166.4c-9.997-9.997-9.997-26.206 0-36.204l36.203-36.204c9.997-9.998 26.207-9.998 36.204 0L192 312.69 432.095 72.596c9.997-9.997 26.207-9.997 36.204 0l36.203 36.204c9.997 9.997 9.997 26.206 0 36.204l-294.4 294.401c-9.998 9.997-26.207 9.997-36.204-.001z"></path></svg>						</span>
										<span class="elementor-icon-list-text"><a href="/study-mbbs-in-russia-for-indian-students">MBBS In Russia</a></span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<svg aria-hidden="true" class="e-font-icon-svg e-fas-check" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M173.898 439.404l-166.4-166.4c-9.997-9.997-9.997-26.206 0-36.204l36.203-36.204c9.997-9.998 26.207-9.998 36.204 0L192 312.69 432.095 72.596c9.997-9.997 26.207-9.997 36.204 0l36.203 36.204c9.997 9.997 9.997 26.206 0 36.204l-294.4 294.401c-9.998 9.997-26.207 9.997-36.204-.001z"></path></svg>						</span>
										<span class="elementor-icon-list-text"><a href="/study-mbbs-in-uzbekistan-for-indian-students">MBBS In Uzbekistan</a></span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<svg aria-hidden="true" class="e-font-icon-svg e-fas-check" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M173.898 439.404l-166.4-166.4c-9.997-9.997-9.997-26.206 0-36.204l36.203-36.204c9.997-9.998 26.207-9.998 36.204 0L192 312.69 432.095 72.596c9.997-9.997 26.207-9.997 36.204 0l36.203 36.204c9.997 9.997 9.997 26.206 0 36.204l-294.4 294.401c-9.998 9.997-26.207 9.997-36.204-.001z"></path></svg>						</span>
										<span class="elementor-icon-list-text"><a href="/study-mbbs-in-kazakhstan-for-indian-students">MBBS In Kazakhstan</a></span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<svg aria-hidden="true" class="e-font-icon-svg e-fas-check" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M173.898 439.404l-166.4-166.4c-9.997-9.997-9.997-26.206 0-36.204l36.203-36.204c9.997-9.998 26.207-9.998 36.204 0L192 312.69 432.095 72.596c9.997-9.997 26.207-9.997 36.204 0l36.203 36.204c9.997 9.997 9.997 26.206 0 36.204l-294.4 294.401c-9.998 9.997-26.207 9.997-36.204-.001z"></path></svg>						</span>
										<span class="elementor-icon-list-text"><a href="/study-mbbs-in-kyrgyzstan-for-indian-students">MBBS In Kyrgyzstan</a></span>
									</li>
						</ul>
						</div>
				</div>
				<div class="elementor-element elementor-element-2292f758 elementor-widget elementor-widget-heading" data-id="2292f758" data-element_type="widget" data-e-type="widget" data-widget_type="heading.default">
				<div class="elementor-widget-container">
					<h2 class="elementor-heading-title elementor-size-default">Universities In <span>Georgia</span></h2>				</div>
				</div>
				<div class="elementor-element elementor-element-5aa83377 elementor-icon-list--layout-traditional elementor-list-item-link-full_width elementor-widget elementor-widget-icon-list" data-id="5aa83377" data-element_type="widget" data-e-type="widget" data-widget_type="icon-list.default">
				<div class="elementor-widget-container">
							<ul class="elementor-icon-list-items">
							<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<svg aria-hidden="true" class="e-font-icon-svg e-fas-check" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M173.898 439.404l-166.4-166.4c-9.997-9.997-9.997-26.206 0-36.204l36.203-36.204c9.997-9.998 26.207-9.998 36.204 0L192 312.69 432.095 72.596c9.997-9.997 26.207-9.997 36.204 0l36.203 36.204c9.997 9.997 9.997 26.206 0 36.204l-294.4 294.401c-9.998 9.997-26.207 9.997-36.204-.001z"></path></svg>						</span>
										<span class="elementor-icon-list-text"><a href="/tbilisi-state-medical-university">Tbilisi State Medical University</a></span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<svg aria-hidden="true" class="e-font-icon-svg e-fas-check" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M173.898 439.404l-166.4-166.4c-9.997-9.997-9.997-26.206 0-36.204l36.203-36.204c9.997-9.998 26.207-9.998 36.204 0L192 312.69 432.095 72.596c9.997-9.998 26.207-9.997 36.204 0l36.203 36.204c9.997 9.997 9.997 26.206 0 36.204l-294.4 294.401c-9.998 9.997-26.207 9.997-36.204-.001z"></path></svg>						</span>
										<span class="elementor-icon-list-text"><a href="/caucasus-university">Caucasus University</a></span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<svg aria-hidden="true" class="e-font-icon-svg e-fas-check" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M173.898 439.404l-166.4-166.4c-9.997-9.997-9.997-26.206 0-36.204l36.203-36.204c9.997-9.998 26.207-9.998 36.204 0L192 312.69 432.095 72.596c9.997-9.997 26.207-9.997 36.204 0l36.203 36.204c9.997 9.997 9.997 26.206 0 36.204l-294.4 294.401c-9.998 9.997-26.207 9.997-36.204-.001z"></path></svg>						</span>
										<span class="elementor-icon-list-text"><a href="/caucasus-international-university">Caucasus International University</a></span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<svg aria-hidden="true" class="e-font-icon-svg e-fas-check" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M173.898 439.404l-166.4-166.4c-9.997-9.997-9.997-26.206 0-36.204l36.203-36.204c9.997-9.998 26.207-9.998 36.204 0L192 312.69 432.095 72.596c9.997-9.998 26.207-9.997 36.204 0l36.203 36.204c9.997 9.997 9.997 26.206 0 36.204l-294.4 294.401c-9.998 9.997-26.207 9.997-36.204-.001z"></path></svg>						</span>
										<span class="elementor-icon-list-text"><a href="/european-university">European University</a></span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<svg aria-hidden="true" class="e-font-icon-svg e-fas-check" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M173.898 439.404l-166.4-166.4c-9.997-9.997-9.997-26.206 0-36.204l36.203-36.204c9.997-9.998 26.207-9.998 36.204 0L192 312.69 432.095 72.596c9.997-9.997 26.207-9.997 36.204 0l36.203 36.204c9.997 9.997 9.997 26.206 0 36.204l-294.4 294.401c-9.998 9.997-26.207 9.997-36.204-.001z"></path></svg>						</span>
										<span class="elementor-icon-list-text"><a href="/east-european-university">East European University</a></span>
									</li>
								<li class="elementor-icon-list-item">
											<span class="elementor-icon-list-icon">
							<svg aria-hidden="true" class="e-font-icon-svg e-fas-check" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M173.898 439.404l-166.4-166.4c-9.997-9.997-9.997-26.206 0-36.204l36.203-36.204c9.997-9.998 26.207-9.998 36.204 0L192 312.69 432.095 72.596c9.997-9.997 26.207-9.997 36.204 0l36.203 36.204c9.997 9.997 9.997 26.206 0 36.204l-294.4 294.401c-9.998 9.997-26.207 9.997-36.204-.001z"></path></svg>						</span>
										<span class="elementor-icon-list-text"><a href="/kutaisi-university">Kutaisi University</a></span>
									</li>
						</ul>
						</div>
				</div>
					</div>
		</div>
					</div>
		</section>
</div>'''

        page_json = {
            "title": f"{uni['full_name']} MBBS Fees 2026, Georgia – Atlas Mentor",
            "description": uni["description"],
            "canonical": f"https://atlasmentor.com/{uni['slug']}/",
            "robots": "max-image-preview:large",
            "stylesheets": template_data["stylesheets"],
            "body": body_html
        }

        output_path = f"data/pages/{uni['slug']}.json"
        with open(output_path, 'w', encoding='utf-8') as f_out:
            json.dump(page_json, f_out, indent=2, ensure_ascii=False)
        print(f"Successfully generated {output_path}")

if __name__ == '__main__':
    create_georgia_university_pages()

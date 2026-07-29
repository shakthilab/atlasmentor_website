import json
import re

def build_georgia_listing_page():
    # Load Uzbekistan listing page as baseline template
    with open('data/pages/mbbs-university/uzbekistan.json', 'r', encoding='utf-8') as f:
        uzb_data = json.load(f)

    # 11 Georgia Universities (Existing Top 6, New Below 5)
    georgia_unis = [
        {
            "slug": "akaki-tsereteli-state-university",
            "title": "Akaki Tsereteli State University, Georgia",
            "img": "../../wp-content/uploads/2024/07/Akaki-Tsereteli-State-University.jpg",
            "excerpt": "Atlas Mentor specializes in guiding students through their MBBS study abroad journey, particularly at Akaki Tsereteli State University, Georgia ensuring personalized and comprehensive support throughout the application and enrollment process."
        },
        {
            "slug": "batumi-shota-rustaveli-state-university",
            "title": "Batumi Shota Rustaveli State University, Georgia",
            "img": "../../wp-content/uploads/2024/07/Batumi-Shota-Rustaveli-State-University.jpg",
            "excerpt": "Atlas Mentor specializes in guiding students through their MBBS study abroad journey, particularly at Batumi Shota Rustaveli State University, Georgia ensuring personalized and comprehensive support throughout the application and enrollment process."
        },
        {
            "slug": "tbilisi-state-medical-university",
            "title": "Tbilisi State Medical University (TSMU), Georgia",
            "img": "../../wp-content/uploads/2024/07/Tbilisi-State-Medical-University.jpg",
            "excerpt": "Atlas Mentor specializes in guiding students through their MBBS study abroad journey, particularly at Tbilisi State Medical University (TSMU), Georgia ensuring personalized and comprehensive support throughout the application and enrollment process."
        },
        {
            "slug": "georgian-national-university-seu",
            "title": "Georgian National University SEU, Georgia",
            "img": "../../wp-content/uploads/2024/07/Georgian-National-University-Georgia.jpg",
            "excerpt": "Atlas Mentor specializes in guiding students through their MBBS study abroad journey, particularly at Georgian National University SEU, Georgia ensuring personalized and comprehensive support throughout the application and enrollment process."
        },
        {
            "slug": "east-west-university-georgia",
            "title": "East West University, Georgia",
            "img": "../../wp-content/uploads/2024/07/East-West-Teaching-University.webp",
            "excerpt": "Atlas Mentor specializes in guiding students through their MBBS study abroad journey, particularly at the East West University, Georgia"
        },
        {
            "slug": "alte-medical-university",
            "title": "Alte Medical University, Georgia",
            "img": "../../wp-content/uploads/2024/07/Alte-Medical-University-Georgia.jpg",
            "excerpt": "Atlas Mentor specializes in providing comprehensive guidance and support to students navigating their MBBS study abroad journey, with a particular focus on the Alte Medical University in Georgia."
        },
        {
            "slug": "caucasus-university",
            "title": "Caucasus University, Georgia",
            "img": "../../wp-content/uploads/2025/02/Study-MBBS-in-Georgia.png",
            "excerpt": "Caucasus University offers an internationally recognized 6-year English medium Medical Doctor (MD / MBBS) program in Tbilisi, Georgia with state-of-the-art simulation labs and top hospital affiliations."
        },
        {
            "slug": "caucasus-international-university",
            "title": "Caucasus International University, Georgia",
            "img": "../../wp-content/uploads/2025/02/Study-MBBS-in-Georgia.png",
            "excerpt": "Caucasus International University (CIU) in Tbilisi provides high-quality European medical education, 100% English instruction, and direct clinical rotations for Indian medical aspirants."
        },
        {
            "slug": "east-european-university",
            "title": "East European University, Georgia",
            "img": "../../wp-content/uploads/2025/02/Study-MBBS-in-Georgia.png",
            "excerpt": "East European University (EEU) features a modern eco-friendly campus in Tbilisi, WFME accreditation, affordable tuition fees, and comprehensive NExT / USMLE guidance."
        },
        {
            "slug": "european-university",
            "title": "European University, Georgia",
            "img": "../../wp-content/uploads/2025/02/Study-MBBS-in-Georgia.png",
            "excerpt": "European University in Tbilisi owns and operates Jo Ann University Hospital, giving medical students direct hands-on clinical exposure in cardiology and multi-specialty care."
        },
        {
            "slug": "kutaisi-university",
            "title": "Kutaisi University, Georgia",
            "img": "../../wp-content/uploads/2025/02/Study-MBBS-in-Georgia.png",
            "excerpt": "Kutaisi University is the oldest private higher education institution in Georgia, offering highly affordable tuition, low living costs, and NMC/WHO approved MBBS degrees."
        }
    ]

    cards_html_list = []
    for u in georgia_unis:
        card = f'''<article class="elementor-post elementor-grid-item post-1105 post type-post status-publish format-standard has-post-thumbnail hentry category-georgia">
	<div class="elementor-post__card">
		<a class="elementor-post__thumbnail__link" href="/{u['slug']}" tabindex="-1" ><div class="elementor-post__thumbnail"><img loading="lazy" width="875" height="500" src="{u['img']}" class="attachment-full size-full wp-image-1959" alt="{u['title']}" decoding="async" /></div></a>
		<div class="elementor-post__badge">Georgia</div>
		<div class="elementor-post__avatar">
			<img loading="lazy" width="128" height="128" src="../../wp-content/uploads/2024/07/Atlas-Mentor-Circle-White-New-150x150.png" class="avatar avatar-128 photo" alt="atlasmentor" decoding="async" />
		</div>
		<div class="elementor-post__text">
			<h3 class="elementor-post__title">
				<a href="/{u['slug']}" >{u['title']}</a>
			</h3>
			<div class="elementor-post__excerpt">
				<p>{u['excerpt']}</p>
			</div>
			<div class="elementor-post__read-more-wrapper">
				<a class="elementor-post__read-more" href="/{u['slug']}" aria-label="Read more about {u['title']}" tabindex="-1" >Read More »</a>
			</div>
		</div>
	</div>
</article>'''
        cards_html_list.append(card)

    all_cards_html = '\n'.join(cards_html_list)

    body = uzb_data['body']

    # Find start of container and end of container
    start_tag = '<div class="elementor-posts-container elementor-has-item-ratio elementor-posts elementor-posts--skin-cards elementor-grid">'
    end_tag = '</div>\n\t\t\n\t\t\t\t\t\t</div>'

    start_idx = body.find(start_tag)
    end_idx = body.find(end_tag, start_idx)

    if start_idx != -1 and end_idx != -1:
        new_body = body[:start_idx + len(start_tag)] + '\n' + all_cards_html + '\n' + body[end_idx:]
    else:
        print("Error locating container bounds!")
        return

    # Replace Uzbekistan -> Georgia
    new_body = new_body.replace('Uzbekistan', 'Georgia').replace('uzbekistan', 'georgia')
    new_body = new_body.replace('12 Top MBBS Universities in Georgia', '11 Top MBBS Universities in Georgia')

    geo_page_json = {
        "title": "11 Top MBBS Universities in Georgia 2026 | Fees & Rankings",
        "description": "Compare 11 MBBS universities in Georgia for Indian students — fees, NEET eligibility & 2026-27 admission. Free expert guidance from Atlas Mentor.",
        "canonical": "https://atlasmentor.com/mbbs-university/georgia/",
        "robots": "max-image-preview:large",
        "stylesheets": uzb_data["stylesheets"],
        "body": new_body
    }

    with open('data/pages/mbbs-university/georgia.json', 'w', encoding='utf-8') as f_out:
        json.dump(geo_page_json, f_out, indent=2, ensure_ascii=False)

    print("Successfully built clean data/pages/mbbs-university/georgia.json with 11 cards!")

if __name__ == '__main__':
    build_georgia_listing_page()

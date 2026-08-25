import json
import re

# Old universities FIRST, New universities BELOW existing ones
all_georgia_unis = [
    # 1. Existing / Old Universities
    {
        "slug": "akaki-tsereteli-state-university",
        "title": "Akaki Tsereteli State University, Georgia",
        "img": "/wp-content/uploads/2024/07/Akaki-Tsereteli-State-University.jpg",
        "excerpt": "Atlas Mentor specializes in guiding students through their MBBS study abroad journey, particularly at Akaki Tsereteli State University, Georgia ensuring personalized and comprehensive support throughout the application and enrollment process."
    },
    {
        "slug": "batumi-shota-rustaveli-state-university",
        "title": "Batumi Shota Rustaveli State University, Georgia",
        "img": "/wp-content/uploads/2024/07/Batumi-Shota-Rustaveli-State-University.jpg",
        "excerpt": "Atlas Mentor specializes in guiding students through their MBBS study abroad journey, particularly at Batumi Shota Rustaveli State University, Georgia ensuring personalized and comprehensive support throughout the application and enrollment process."
    },
    {
        "slug": "tbilisi-state-medical-university",
        "title": "Tbilisi State Medical University (TSMU), Georgia",
        "img": "/wp-content/uploads/2024/07/Tbilisi-State-Medical-University.jpg",
        "excerpt": "Atlas Mentor specializes in guiding students through their MBBS study abroad journey, particularly at Tbilisi State Medical University (TSMU), Georgia ensuring personalized and comprehensive support throughout the application and enrollment process."
    },
    {
        "slug": "georgian-national-university-seu",
        "title": "Georgian National University SEU, Georgia",
        "img": "/wp-content/uploads/2024/07/Georgian-National-University-Georgia.jpg",
        "excerpt": "Atlas Mentor specializes in guiding students through their MBBS study abroad journey, particularly at Georgian National University SEU, Georgia ensuring personalized and comprehensive support throughout the application and enrollment process."
    },
    {
        "slug": "east-west-university-georgia",
        "title": "East West University, Georgia",
        "img": "/wp-content/uploads/2024/07/East-West-Teaching-University.webp",
        "excerpt": "Atlas Mentor specializes in guiding students through their MBBS study abroad journey, particularly at the East West University, Georgia"
    },
    {
        "slug": "alte-medical-university",
        "title": "Alte Medical University, Georgia",
        "img": "/wp-content/uploads/2024/07/Alte-Medical-University-Georgia.jpg",
        "excerpt": "Atlas Mentor specializes in providing comprehensive guidance and support to students navigating their MBBS study abroad journey, with a particular focus on the Alte Medical University in Georgia."
    },
    # 2. New Universities Below Existing Ones
    {
        "slug": "caucasus-university",
        "title": "Caucasus University, Georgia",
        "img": "/wp-content/uploads/2025/02/Caucasus-University-1.jpg",
        "excerpt": "Caucasus University offers an internationally recognized 6-year English medium Medical Doctor (MD / MBBS) program in Tbilisi, Georgia with state-of-the-art simulation labs and top hospital affiliations."
    },
    {
        "slug": "caucasus-international-university",
        "title": "Caucasus International University, Georgia",
        "img": "/wp-content/uploads/2025/02/Study-MBBS-in-Georgia.png",
        "excerpt": "Caucasus International University (CIU) in Tbilisi provides high-quality European medical education, 100% English instruction, and direct clinical rotations for Indian medical aspirants."
    },
    {
        "slug": "east-european-university",
        "title": "East European University, Georgia",
        "img": "/wp-content/uploads/2025/02/Study-MBBS-in-Georgia.png",
        "excerpt": "East European University (EEU) features a modern eco-friendly campus in Tbilisi, WFME accreditation, affordable tuition fees, and comprehensive NExT / USMLE guidance."
    },
    {
        "slug": "european-university",
        "title": "European University, Georgia",
        "img": "/wp-content/uploads/2025/02/Study-MBBS-in-Georgia.png",
        "excerpt": "European University in Tbilisi owns and operates Jo Ann University Hospital, giving medical students direct hands-on clinical exposure in cardiology and multi-specialty care."
    },
    {
        "slug": "kutaisi-university",
        "title": "Kutaisi University, Georgia",
        "img": "/wp-content/uploads/2025/02/Study-MBBS-in-Georgia.png",
        "excerpt": "Kutaisi University is the oldest private higher education institution in Georgia, offering highly affordable tuition, low living costs, and NMC/WHO approved MBBS degrees."
    }
]

def make_perfect_card(u):
    return f'''<article class="elementor-post elementor-grid-item post-1105 post type-post status-publish format-standard has-post-thumbnail hentry category-georgia">
	<div class="elementor-post__card">
		<a class="elementor-post__thumbnail__link" href="/{u['slug']}" tabindex="-1" ><div class="elementor-post__thumbnail"><img loading="lazy" decoding="async" width="875" height="500" src="..{u['img']}" class="attachment-full size-full wp-image-1959" alt="{u['title']}" sizes="(max-width: 875px) 100vw, 875px" /></div></a>
		<div class="elementor-post__badge">Georgia</div>
		<div class="elementor-post__avatar">
			<img loading="lazy" decoding="async" width="128" height="128" src="../wp-content/uploads/2024/07/Atlas-Mentor-Circle-White-New-150x150.png" class="avatar avatar-128 photo" alt="atlasmentor" sizes="(max-width: 128px) 100vw, 128px" />
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

def update_page_grid(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    body = data['body']

    # Generate all cards
    cards_html = '\n'.join([make_perfect_card(u) for u in all_georgia_unis])

    # Find elementor-posts-container and replace its internal content
    pattern = r'(<div class="elementor-posts-container[^>]*>)([\s\S]*?)(</div>\s*</div>\s*</div>)'
    match = re.search(pattern, body)
    if match:
        new_body = body[:match.start(2)] + '\n' + cards_html + '\n' + body[match.end(2):]
        data['body'] = new_body
        with open(filepath, 'w', encoding='utf-8') as f_out:
            json.dump(data, f_out, indent=2, ensure_ascii=False)
        print(f"Successfully updated card order in {filepath}")
    else:
        print(f"Failed to find elementor-posts-container in {filepath}")

if __name__ == '__main__':
    update_page_grid('data/pages/mbbs-university/georgia.json')
    update_page_grid('data/pages/study-mbbs-in-georgia-for-indian-students.json')

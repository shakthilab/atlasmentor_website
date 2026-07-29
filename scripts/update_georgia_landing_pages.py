import json
import re

new_unis = [
    {
        "slug": "caucasus-university",
        "title": "Caucasus University, Georgia",
        "img": "../wp-content/uploads/2025/02/Study-MBBS-in-Georgia.png"
    },
    {
        "slug": "caucasus-international-university",
        "title": "Caucasus International University, Georgia",
        "img": "../wp-content/uploads/2025/02/Study-MBBS-in-Georgia.png"
    },
    {
        "slug": "east-european-university",
        "title": "East European University, Georgia",
        "img": "../wp-content/uploads/2025/02/Study-MBBS-in-Georgia.png"
    },
    {
        "slug": "european-university",
        "title": "European University, Georgia",
        "img": "../wp-content/uploads/2025/02/Study-MBBS-in-Georgia.png"
    },
    {
        "slug": "kutaisi-university",
        "title": "Kutaisi University, Georgia",
        "img": "../wp-content/uploads/2025/02/Study-MBBS-in-Georgia.png"
    }
]

def make_card_html(u):
    return f'''<article class="elementor-post elementor-grid-item post-1105 post type-post status-publish format-standard has-post-thumbnail hentry category-georgia">
	<div class="elementor-post__card">
		<a class="elementor-post__thumbnail__link" href="/{u['slug']}" tabindex="-1" ><div class="elementor-post__thumbnail"><img loading="lazy" decoding="async" width="875" height="500" src="{u['img']}" class="attachment-full size-full wp-image-1959" alt="{u['title']}" sizes="(max-width: 875px) 100vw, 875px" /></div></a>
		<div class="elementor-post__badge">Georgia</div>
		<div class="elementor-post__avatar">
			<img loading="lazy" decoding="async" width="128" height="128" src="../wp-content/uploads/2024/07/Atlas-Mentor-Circle-White-New-150x150.png" class="avatar avatar-128 photo" alt="atlasmentor" sizes="(max-width: 128px) 100vw, 128px" />
		</div>
		<div class="elementor-post__text">
			<h3 class="elementor-post__title">
				<a href="/{u['slug']}" >{u['title']}</a>
			</h3>
			<div class="elementor-post__read-more-wrapper">
				<a class="elementor-post__read-more" href="/{u['slug']}" aria-label="Read more about {u['title']}" tabindex="-1" >Read More »</a>
			</div>
		</div>
	</div>
</article>'''

def update_landing_page(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    body = data['body']

    # Check which cards are missing
    cards_to_add = []
    for u in new_unis:
        if f'href="/{u["slug"]}"' not in body:
            cards_to_add.append(make_card_html(u))

    if not cards_to_add:
        print(f"No missing cards for {filepath}")
        return

    # Insert new cards before the end of elementor-posts-container
    container_marker = '<div class="elementor-posts-container elementor-has-item-ratio elementor-posts elementor-posts--skin-cards elementor-grid">'
    if container_marker in body:
        idx = body.find(container_marker) + len(container_marker)
        inserted_html = '\n'.join(cards_to_add) + '\n'
        new_body = body[:idx] + '\n' + inserted_html + body[idx:]
        data['body'] = new_body
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Successfully updated {filepath} with {len(cards_to_add)} new university cards.")
    else:
        print(f"Could not locate post container marker in {filepath}")

if __name__ == '__main__':
    update_landing_page('data/pages/study-mbbs-in-georgia-for-indian-students.json')
    update_landing_page('data/pages/mbbs-university/georgia.json')

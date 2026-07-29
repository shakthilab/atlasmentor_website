import json
import re
import os

def make_card(slug, img_name, img_alt, title):
    return f"""		<article class="elementor-post elementor-grid-item post-1376 post type-post status-publish format-standard has-post-thumbnail hentry category-uzbekistan">
			<div class="elementor-post__card">
				<a class="elementor-post__thumbnail__link" href="/{slug}" tabindex="-1" ><div class="elementor-post__thumbnail"><img loading="lazy" decoding="async" width="1024" height="753" src="../wp-content/uploads/2025/01/{img_name}.jpg" class="attachment-full size-full wp-image-1453" alt="{img_alt}" srcset="../wp-content/uploads/2025/01/{img_name}.jpg 1024w, ../wp-content/uploads/2025/01/{img_name}-300x221.jpg 300w, ../wp-content/uploads/2025/01/{img_name}-768x565.jpg 768w, ../wp-content/uploads/2025/01/{img_name}-24x18.jpg 24w, ../wp-content/uploads/2025/01/{img_name}-36x26.jpg 36w, ../wp-content/uploads/2025/01/{img_name}-48x35.jpg 48w" sizes="(max-width: 1024px) 100vw, 1024px" /></div></a>
				<div class="elementor-post__badge">Uzbekistan</div>
				<div class="elementor-post__avatar">
			<img loading="lazy" decoding="async" width="128" height="128" src="../wp-content/uploads/2024/07/Atlas-Mentor-Circle-White-New-150x150.png" class="avatar avatar-128 photo" alt="atlasmentor" srcset="../wp-content/uploads/2024/07/Atlas-Mentor-Circle-White-New-150x150.png 150w, ../wp-content/uploads/2024/07/Atlas-Mentor-Circle-White-New-300x300.png 300w, ../wp-content/uploads/2024/07/Atlas-Mentor-Circle-White-New-768x768.png 768w, ../wp-content/uploads/2024/07/Atlas-Mentor-Circle-White-New-24x24.png 24w, ../wp-content/uploads/2024/07/Atlas-Mentor-Circle-White-New-36x36.png 36w, ../wp-content/uploads/2024/07/Atlas-Mentor-Circle-White-New-48x48.png 48w, ../wp-content/uploads/2024/07/Atlas-Mentor-Circle-White-New.png 960w" sizes="(max-width: 128px) 100vw, 128px" />		</div>
				<div class="elementor-post__text">
				<h3 class="elementor-post__title">
			<a href="/{slug}" >
				{title}			</a>
		</h3>
					<div class="elementor-post__read-more-wrapper">
		
		<a class="elementor-post__read-more" href="/{slug}" aria-label="Read more about {title}" tabindex="-1" >
			Read More »		</a>

					</div>
				</div>
					</div>
		</article>
"""

def make_sidebar_item(slug, title):
    return f"""                                <article class="elementor-post elementor-grid-item post-1376 post type-post status-publish format-standard has-post-thumbnail hentry category-uzbekistan">
                                <div class="elementor-post__text">
                                <div class="elementor-post__title">
                        <a href="/{slug}" >
                                {title}                  </a>
                </div>
                                </div>
                                </article>
"""

def update_main_page():
    fpath = 'data/pages/study-mbbs-in-uzbekistan-for-indian-students.json'
    print(f"=== Updating {fpath} ===")
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    body = data['body']
    
    heading = 'Universities For MBBS in Uzbekistan'
    h_idx = body.find(heading)
    if h_idx == -1:
        print("Error: Heading 'Universities For MBBS in Uzbekistan' not found in main page")
        return
        
    container_start_class = 'elementor-posts-container elementor-has-item-ratio elementor-posts'
    div_start = body.find(container_start_class, h_idx)
    if div_start == -1:
        print("Error: Cards container not found in main page")
        return
        
    sub_body = body[div_start:div_start+35000]
    articles = re.findall(r'<article[^>]*>.*?</article>', sub_body, re.DOTALL)
    if len(articles) < 6:
        print(f"Error: Found only {len(articles)} cards in main page instead of 6")
        return
        
    last_art = articles[-1]
    last_art_idx = body.find(last_art, div_start)
    if last_art_idx == -1:
        print("Error: Could not find 6th article position")
        return
        
    insert_pos = last_art_idx + len(last_art)
    
    new_unis = [
        {"slug": "namangan-state-medical-university", "img_name": "Namangan-State-Medical-Institute", "img_alt": "Namangan State Medical University", "title": "Namangan State Medical University, Uzbekistan"},
        {"slug": "mamun-university", "img_name": "Khiva-State-Medical-Institute", "img_alt": "Mamun University", "title": "Mamun University, Uzbekistan"},
        {"slug": "navoi-state-medical-university", "img_name": "Navoi-State-Medical-Institute", "img_alt": "Navoi State Medical University", "title": "Navoi State Medical University, Uzbekistan"},
        {"slug": "zarmed-university", "img_name": "Bukhara & Samarkand-State-Medical-Institute", "img_alt": "Zarmed University", "title": "Zarmed University, Uzbekistan"},
        {"slug": "karshi-state-medical-university", "img_name": "Qarshi-State-Medical-Institute", "img_alt": "Karshi State Medical University", "title": "Karshi State Medical University, Uzbekistan"},
        {"slug": "gulistan-state-medical-university", "img_name": "Guliston-State-Medical-Institute", "img_alt": "Gulistan State Medical University", "title": "Gulistan State Medical University, Uzbekistan"}
    ]
    
    new_cards_html = ""
    for uni in new_unis:
        if f'href="/{uni["slug"]}"' in body or f'href="/{uni["slug"]}/"' in body:
            print(f"Card for {uni['slug']} already exists, skipping")
            continue
        new_cards_html += make_card(uni["slug"], uni["img_name"], uni["img_alt"], uni["title"])
        
    if not new_cards_html:
        print("No new cards added")
        return
        
    new_body = body[:insert_pos] + "\n" + new_cards_html + body[insert_pos:]
    data['body'] = new_body
    
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Success: Main page updated successfully")

def update_sidebar(fpath):
    print(f"=== Updating sidebar of {fpath} ===")
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    body = data['body']
    
    heading = 'Universities In <span>Uzbekistan</span>'
    h_idx = body.find(heading)
    if h_idx == -1:
        print(f"Warning: Heading '{heading}' not found in {fpath}")
        return
        
    div_start = body.find('<div class="elementor-posts-container', h_idx)
    if div_start == -1:
        print(f"Warning: Container not found in {fpath}")
        return
        
    art_start = body.find('<article', div_start)
    if art_start == -1:
        print(f"Warning: No articles found in {fpath}")
        return
        
    sub_body = body[div_start:div_start+15000]
    articles = re.findall(r'<article[^>]*>.*?</article>', sub_body, re.DOTALL)
    if not articles:
        print(f"Warning: Could not parse articles in {fpath}")
        return
        
    uz_articles = []
    for art in articles:
        if 'category-uzbekistan' in art:
            uz_articles.append(art)
            
    if not uz_articles:
        for art in articles:
            h = re.search(r'href=\"([^\"]+)\"', art)
            if h and any(k in h.group(1) for k in ['fergana', 'samarkand', 'tashkent', 'andijan', 'bukhara', 'urgench', 'gulistan', 'navoi', 'namangan', 'zarmed', 'karshi', 'mamun']):
                uz_articles.append(art)
                
    if not uz_articles:
        print(f"Warning: No Uzbekistan articles found in {fpath} to group with")
        return
        
    last_uz_art = uz_articles[-1]
    last_uz_idx = body.find(last_uz_art, div_start)
    if last_uz_idx == -1:
        print(f"Warning: Could not find last Uzbekistan article position in {fpath}")
        return
        
    insert_pos = last_uz_idx + len(last_uz_art)
    
    existing_hrefs = set()
    for art in articles:
        h = re.search(r'href=\"([^\"]+)\"', art)
        if h:
            existing_hrefs.add(h.group(1).rstrip('/'))
            
    new_unis = [
        {"slug": "namangan-state-medical-university", "title": "Namangan State Medical University, Uzbekistan"},
        {"slug": "mamun-university", "title": "Mamun University, Uzbekistan"},
        {"slug": "navoi-state-medical-university", "title": "Navoi State Medical University, Uzbekistan"},
        {"slug": "zarmed-university", "title": "Zarmed University, Uzbekistan"},
        {"slug": "karshi-state-medical-university", "title": "Karshi State Medical University, Uzbekistan"},
        {"slug": "gulistan-state-medical-university", "title": "Gulistan State Medical University, Uzbekistan"}
    ]
    
    new_items_html = ""
    inserted_slugs = []
    current_slug = os.path.basename(fpath).replace('.json', '')
    
    for uni in new_unis:
        slug_check = "/" + uni["slug"]
        is_current_page = (uni["slug"] in current_slug) or (current_slug in uni["slug"])
        if is_current_page:
            continue
            
        if slug_check in existing_hrefs:
            continue
            
        new_items_html += make_sidebar_item(uni["slug"], uni["title"])
        inserted_slugs.append(uni["slug"])
        
    if not new_items_html:
        print(f"No new items to add to {fpath}")
        return
        
    new_body = body[:insert_pos] + "\n" + new_items_html + body[insert_pos:]
    data['body'] = new_body
    
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Success: Updated sidebar. Added: {inserted_slugs}")

if __name__ == '__main__':
    update_main_page()
    
    files = [
      'data/pages/gulistan-state-medical-university.json',
      'data/pages/samarkand-state-medical-institute.json',
      'data/pages/navoi-state-medical-university.json',
      'data/pages/namangan-state-medical-university.json',
      'data/pages/zarmed-university.json',
      'data/pages/tashkent-medical-academy.json',
      'data/pages/karshi-state-medical-university.json',
      'data/pages/bukhara-state-medical-university.json',
      'data/pages/andijan-state-medical-institute-ranking.json',
      'data/pages/urgench-branch-of-tashkent-medical-academy.json',
      'data/pages/fergana-medical-institute-of-public-health.json',
      'data/pages/mamun-university.json'
    ]
    
    for f in files:
        update_sidebar(f)

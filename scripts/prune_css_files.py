import glob, json, re, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PUBLIC = os.path.join(ROOT, "public")

# 1. Prune font CSS files to latin subset only
font_css_files = [
    'wp-content/uploads/elementor/google-fonts/css/montserrat.css',
    'wp-content/uploads/elementor/google-fonts/css/opensans.css',
    'wp-content/uploads/elementor/google-fonts/css/raleway.css',
    'wp-content/uploads/elementor/google-fonts/css/roboto.css'
]

for rel_p in font_css_files:
    full_p = os.path.join(PUBLIC, rel_p)
    if os.path.exists(full_p):
        content = open(full_p, encoding='utf-8', errors='replace').read()
        # Keep only latin block definitions
        blocks = content.split('/*')
        latin_blocks = []
        for b in blocks:
            if not b.strip(): continue
            if 'latin ' in b or b.strip().startswith('latin') or 'font-family' in b and 'cyrillic' not in b and 'vietnamese' not in b and 'greek' not in b and 'hebrew' not in b:
                # Exclude latin-ext if latin is present
                if 'latin-ext' not in b:
                    latin_blocks.append('/*' + b)
        if latin_blocks:
            new_content = ''.join(latin_blocks)
            with open(full_p, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Pruned font CSS {rel_p}: {len(content)/1024:.1f} KB -> {len(new_content)/1024:.1f} KB")

# 2. Extract all exact class names in project
all_classes = set()

for p in glob.glob(os.path.join(ROOT, 'data/**/*.json'), recursive=True):
    try:
        d = json.load(open(p, encoding='utf-8', errors='replace'))
        content = d.get('body', '') + ' ' + d.get('headerHtml', '') + ' ' + d.get('footerHtml', '')
        for f in re.findall(r'class=[\"\']([^\"\']+)[\"\']', content):
            for cls in f.split():
                all_classes.add(cls)
    except: pass

for p in glob.glob(os.path.join(ROOT, 'data/globals/*.html')):
    content = open(p, encoding='utf-8', errors='replace').read()
    for f in re.findall(r'class=[\"\']([^\"\']+)[\"\']', content):
        for cls in f.split():
            all_classes.add(cls)

for p in glob.glob(os.path.join(ROOT, 'app/**/*.tsx'), recursive=True) + glob.glob(os.path.join(ROOT, 'components/**/*.tsx'), recursive=True):
    content = open(p, encoding='utf-8', errors='replace').read()
    for f in re.findall(r'class(?:Name)?=[\"\']([^\"\']+)[\"\']', content):
        for cls in f.split():
            all_classes.add(cls)

dynamic_classes = {'show', 'collapsed', 'active', 'animated', 'fadeInUp', 'fadeInLeft', 'fadeInRight', 'swiper-slide', 'swiper-wrapper', 'swiper', 'elementor-active', 'elementor-invisible'}
all_classes.update(dynamic_classes)

# 3. Prune widget-styles.css
css_widget_path = os.path.join(PUBLIC, 'wp-content/plugins/elementskit-lite/widgets/init/assets/css/widget-styles.css')
if os.path.exists(css_widget_path):
    css_widget = open(css_widget_path, encoding='utf-8', errors='replace').read()

    generic_wrapper_classes = {
        'elementor', 'elementor-widget', 'elementor-widget-container', 'elementor-element',
        'elementor-section', 'elementor-column', 'elementor-container', 'elementor-row',
        'elementor-widget-wrap', 'ekit-wid-con', 'ekit-wid-con-inner', 'elementor-widget-elementskit-back-to-top',
        'show', 'collapsed', 'active', 'animated', 'fadeInUp', 'fadeInLeft', 'fadeInRight'
    }

    def is_widget_rule_used(rule_str):
        if rule_str.startswith('@font-face') or rule_str.startswith('@keyframes') or rule_str.startswith(':root'):
            return True
        if '{' not in rule_str: return False
        
        sel = rule_str[:rule_str.find('{')].strip()
        classes = set(re.findall(r'\.([a-zA-Z0-9_-]+)', sel))
        if not classes:
            return True
        
        specific_classes = classes - generic_wrapper_classes
        if not specific_classes:
            return True
        
        for c in specific_classes:
            if c in all_classes:
                return True
        return False

    rules = re.split(r'\}\s*', css_widget)
    kept = []
    for r in rules:
        r = r.strip()
        if not r: continue
        if '{' in r:
            if is_widget_rule_used(r):
                kept.append(r + '}')

    pruned_widget_css = '\n'.join(kept)
    with open(css_widget_path, 'w', encoding='utf-8') as f:
        f.write(pruned_widget_css)
    print(f"Pruned widget-styles.css: {len(css_widget)/1024:.1f} KB -> {len(pruned_widget_css)/1024:.1f} KB")

# 4. Prune ekiticons.css
css_icon_path = os.path.join(PUBLIC, 'wp-content/plugins/elementskit-lite/modules/elementskit-icon-pack/assets/css/ekiticons.css')
if os.path.exists(css_icon_path):
    css_icon = open(css_icon_path, encoding='utf-8', errors='replace').read()

    icon_rules = css_icon.split('}')
    kept_icons = []
    for r in icon_rules:
        r = r.strip()
        if not r: continue
        if '{' in r:
            sel = r[:r.find('{')].strip()
            if sel.startswith('@font-face') or 'font-family:elementskit' in r:
                kept_icons.append(r + '}')
                continue
            icons = re.findall(r'icon-([a-zA-Z0-9_-]+)', sel)
            if not icons:
                kept_icons.append(r + '}')
                continue
            if any(f'icon-{ic}' in all_classes for ic in icons):
                kept_icons.append(r + '}')

    pruned_icon_css = '\n'.join(kept_icons)
    with open(css_icon_path, 'w', encoding='utf-8') as f:
        f.write(pruned_icon_css)
    print(f"Pruned ekiticons.css: {len(css_icon)/1024:.1f} KB -> {len(pruned_icon_css)/1024:.1f} KB")

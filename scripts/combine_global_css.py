import os
import re
import posixpath

ROOT = "/home/shakthi/Desktop/freelancer/atlasmentor_website"
PUBLIC = os.path.join(ROOT, "public")

GLOBAL_STYLES = [
    "/wp-content/plugins/metronet-profile-picture/dist/blocks.style.build.css",
    "/wp-content/plugins/menu-image/includes/css/menu-image.css",
    "/wp-includes/css/dashicons.min.css",
    "/wp-content/themes/hello-elementor/style.min.css",
    "/wp-content/themes/hello-elementor/theme.min.css",
    "/wp-content/plugins/elementor/assets/css/frontend.min.css",
    "/wp-content/plugins/elementor/assets/css/widget-icon-list.min.css",
    "/wp-content/plugins/elementor/assets/css/widget-social-icons.min.css",
    "/wp-content/plugins/elementor/assets/css/conditionals/apple-webkit.min.css",
    "/wp-content/plugins/elementor/assets/css/widget-image.min.css",
    "/wp-content/plugins/pro-elements/assets/css/widget-nav-menu.min.css",
    "/wp-content/plugins/elementor/assets/css/widget-heading.min.css",
    "/wp-content/plugins/pro-elements/assets/css/widget-form.min.css",
    "/wp-content/plugins/pro-elements/assets/css/conditionals/popup.min.css",
    "/wp-content/uploads/elementor/css/post-9.css",
    "/wp-content/plugins/elementor/assets/lib/animations/styles/fadeInUp.min.css",
    "/wp-content/plugins/elementor/assets/lib/animations/styles/fadeInLeft.min.css",
    "/wp-content/plugins/elementor/assets/lib/animations/styles/fadeInRight.min.css",
    "/wp-content/plugins/elementor/assets/css/widget-divider.min.css",
    "/wp-content/plugins/elementor/assets/css/widget-video.min.css",
    "/wp-content/plugins/elementor/assets/css/widget-icon-box.min.css",
    "/wp-content/plugins/pro-elements/assets/css/widget-blockquote.min.css",
    "/wp-content/plugins/elementor/assets/lib/animations/styles/e-animation-float.min.css",
    "/wp-content/plugins/elementor/assets/lib/swiper/v8/css/swiper.min.css",
    "/wp-content/plugins/elementor/assets/css/conditionals/e-swiper.min.css",
    "/wp-content/plugins/pro-elements/assets/css/widget-testimonial-carousel.min.css",
    "/wp-content/plugins/pro-elements/assets/css/widget-carousel-module-base.min.css",
    "/wp-content/uploads/elementor/css/post-61.css",
    "/wp-content/uploads/elementor/css/post-64.css",
    "/wp-content/uploads/elementor/css/post-664.css",
    "/wp-content/plugins/elementskit-lite/widgets/init/assets/css/widget-styles.css",
    "/wp-content/plugins/elementskit-lite/widgets/init/assets/css/responsive.css",
    "/wp-content/uploads/elementor/google-fonts/css/montserrat.css",
    "/wp-content/uploads/elementor/google-fonts/css/raleway.css",
    "/wp-content/uploads/elementor/google-fonts/css/roboto.css",
    "/wp-content/plugins/elementskit-lite/modules/elementskit-icon-pack/assets/css/ekiticons.css",
]

URL_RE = re.compile(r"url\(\s*(['\"]?)([^'\")]+)\1\s*\)")


def rewrite_urls(css: str, base_dir: str) -> str:
    def repl(m):
        quote, value = m.group(1), m.group(2)
        if value.startswith(("data:", "http://", "https://", "//", "/")):
            return m.group(0)
        resolved = posixpath.normpath(posixpath.join(base_dir, value))
        return f"url({quote}{resolved}{quote})"

    return URL_RE.sub(repl, css)


chunks = []
total_before = 0
for href in GLOBAL_STYLES:
    fs_path = os.path.join(PUBLIC, href.lstrip("/"))
    with open(fs_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
    total_before += len(content.encode("utf-8"))
    base_dir = posixpath.dirname(href)
    rewritten = rewrite_urls(content, base_dir)
    chunks.append(f"/* --- {href} --- */\n{rewritten.strip()}\n")

combined = "\n".join(chunks)
out_path = os.path.join(PUBLIC, "wp-content", "combined-global.css")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(combined)

print(f"Combined {len(GLOBAL_STYLES)} files -> {out_path}")
print(f"Before: {total_before/1024:.1f} KB across {len(GLOBAL_STYLES)} requests")
print(f"After:  {len(combined.encode('utf-8'))/1024:.1f} KB in 1 request")

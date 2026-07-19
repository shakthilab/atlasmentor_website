import fs from 'fs';
import path from 'path';
import { Metadata } from 'next';
import { buildPageMetadata, extractAccordionFAQs, faqPageSchema } from '@/lib/seo';
import RichHtml from '@/components/RichHtml';

const GLOBAL_STYLES = [
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
  "/wp-content/plugins/elementskit-lite/modules/elementskit-icon-pack/assets/css/ekiticons.css"
];

function getHomepageData() {
  const filePath = path.join(process.cwd(), 'data/pages/index.json');
  if (!fs.existsSync(filePath)) {
    return null;
  }
  const fileContent = fs.readFileSync(filePath, 'utf8');
  return JSON.parse(fileContent);
}

export async function generateMetadata(): Promise<Metadata> {
  const data = getHomepageData();
  return buildPageMetadata(data, '/');
}

export default function Home() {
  const data = getHomepageData();

  if (!data) {
    return (
      <div style={{ padding: '100px', textAlign: 'center' }}>
        <h1>404 - Homepage Not Found</h1>
        <p>Ensure that data extraction has run successfully.</p>
      </div>
    );
  }

  // Filter page-specific stylesheets
  const pageStyles = (data.stylesheets || []).filter(
    (href: string) => !GLOBAL_STYLES.includes(href)
  );

  // Process paths in body content
  const processedBody = data.body
    .replace(/(?:\.\.\/)+wp-content\//g, '/wp-content/')
    .replace(/(?:\.\.\/)+wp-includes\//g, '/wp-includes/')
    .replace(/https:\/\/atlasmentor\.com\/wp-content\//g, '/wp-content/')
    .replace(/https:\/\/atlasmentor\.com\/wp-includes\//g, '/wp-includes/');

  const faqSchema = faqPageSchema(extractAccordionFAQs(data.body));

  return (
    <main>
      {/* Page specific stylesheets hoisted to head with precedence for React resource management */}
      {pageStyles.map((href: string) => (
        <link rel="stylesheet" href={href} key={href} precedence="default" />
      ))}

      {/* Structured Schemas */}
      {data.schemas && data.schemas.map((schemaStr: string, idx: number) => (
        <script
          key={idx}
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: schemaStr }}
        />
      ))}
      {faqSchema && (
        <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: faqSchema }} />
      )}

      {/* Page Content */}
      <RichHtml html={processedBody} />
    </main>
  );
}

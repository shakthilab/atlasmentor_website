import type { Metadata } from "next";
import fs from 'fs';
import path from 'path';
import Script from "next/script";
import { Analytics } from "@vercel/analytics/next";
import "./globals.css";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Popup from "@/components/Popup";
import BodyClassManager from "@/components/BodyClassManager";
import FormHandlerClient from "@/components/FormHandlerClient";
import ElementorInteractions from "@/components/ElementorInteractions";
import HeroTransition from "@/components/HeroTransition";


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

const SITE_URL = "https://atlasmentor.com";
const SITE_DESCRIPTION = "Guiding students through their MBBS study abroad journey";
const DEFAULT_OG_IMAGE = "/wp-content/uploads/2024/07/MBBS-Dream-With-Atlas-Mentor.jpg";

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  title: {
    default: "Atlas Mentor",
    template: "%s | Atlas Mentor",
  },
  description: SITE_DESCRIPTION,
  icons: {
    icon: [
      { url: "/icon-32.png", sizes: "32x32", type: "image/png" },
      { url: "/icon-192.png", sizes: "192x192", type: "image/png" },
    ],
    apple: [
      { url: "/apple-icon.png", sizes: "180x180", type: "image/png" },
    ],
  },
  openGraph: {
    title: "Atlas Mentor",
    description: SITE_DESCRIPTION,
    url: SITE_URL,
    siteName: "Atlas Mentor",
    type: "website",
    images: [DEFAULT_OG_IMAGE],
  },
  twitter: {
    card: "summary_large_image",
    title: "Atlas Mentor",
    description: SITE_DESCRIPTION,
    images: [DEFAULT_OG_IMAGE],
  },
};


export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  // Read Popup HTML
  const popupHtmlPath = path.join(process.cwd(), 'data/globals/popup.html');
  const popupHtml = fs.readFileSync(popupHtmlPath, 'utf8');

  return (
    <html lang="en">
      <head>
        {GLOBAL_STYLES.map((href) => (
          <link rel="stylesheet" href={href} key={href} precedence="default" />
        ))}
      </head>
      <body suppressHydrationWarning>
        <BodyClassManager />
        <ElementorInteractions />
        <FormHandlerClient />
        <div id="page" className="hfeed site">
          <Header />
          <HeroTransition>
            {children}
          </HeroTransition>
          <Footer />
        </div>
        <Popup html={popupHtml} />

        {/* Load Swiper.js dynamically on the client side */}
        <Script
          src="/wp-content/plugins/elementor/assets/lib/swiper/v8/swiper.min.js"
          strategy="lazyOnload"
        />
        <Analytics />
      </body>
    </html>
  );
}

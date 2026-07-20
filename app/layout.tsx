import type { Metadata } from "next";
import fs from 'fs';
import path from 'path';
import Script from "next/script";
import { GoogleAnalytics } from "@next/third-parties/google";
import { Analytics } from "@vercel/analytics/next";
import { SpeedInsights } from "@vercel/speed-insights/next";
import "./globals.css";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Popup from "@/components/Popup";
import BodyClassManager from "@/components/BodyClassManager";
import ClarityAnalytics from "@/components/ClarityAnalytics";
import FormHandlerClient from "@/components/FormHandlerClient";
import ElementorInteractions from "@/components/ElementorInteractions";
import HeroTransition from "@/components/HeroTransition";
import { organizationSchema, SITE_URL, SITE_NAME, DEFAULT_OG_IMAGE } from "@/lib/seo";

const SITE_DESCRIPTION = "Guiding students through their MBBS study abroad journey";

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  // Plain string, not a { default, template } object: every page's own title
  // (data/pages/*.json) already ends in "– Atlas Mentor", so a template suffix
  // here previously doubled up on every non-homepage page
  // (e.g. "...Kazakhstan – Atlas Mentor | Atlas Mentor").
  title: SITE_NAME,
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
    title: SITE_NAME,
    description: SITE_DESCRIPTION,
    url: SITE_URL,
    siteName: SITE_NAME,
    type: "website",
    images: [DEFAULT_OG_IMAGE],
  },
  twitter: {
    card: "summary_large_image",
    title: SITE_NAME,
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
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: organizationSchema() }}
        />
        {/* Bundles the ~36 legacy WordPress/Elementor stylesheets (still listed as
            GLOBAL_STYLES in app/page.tsx, app/[slug]/page.tsx, etc. for the per-page
            de-dupe filter) into one request. Regenerate with scripts/combine_global_css.py
            if that list ever changes. */}
        <link rel="stylesheet" href="/wp-content/combined-global.css" precedence="default" />
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
        <SpeedInsights />
        <ClarityAnalytics />
      </body>
      {process.env.NEXT_PUBLIC_GA_MEASUREMENT_ID && (
        <GoogleAnalytics gaId={process.env.NEXT_PUBLIC_GA_MEASUREMENT_ID} />
      )}
    </html>
  );
}

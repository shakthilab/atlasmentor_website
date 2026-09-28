import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  trailingSlash: true,
  experimental: {
    webpackMemoryOptimizations: true,
  },
  async redirects() {
    return [
      // Old WordPress static front page — content now lives at the homepage.
      { source: "/atlas-mentor", destination: "/", permanent: true },
      // Old WordPress placeholder/event pages with no new-site equivalent.
      { source: "/sample-page", destination: "/", permanent: true },
      { source: "/seminar", destination: "/", permanent: true },
      // Old WordPress author archive pages.
      { source: "/author/:author", destination: "/", permanent: true },
    ];
  },
  async headers() {
    // Content-Security-Policy: allowlists only the third-party origins this
    // site actually loads (GTM, GA4, Microsoft Clarity, Ahrefs analytics,
    // Vercel Analytics/Speed Insights — the last two call same-origin
    // /_vercel/* paths so they need no extra entry here). 'unsafe-inline' on
    // script-src is required because Google Tag Manager's own snippet is an
    // inline <script>, and GTM can inject further inline tags configured in
    // its container at runtime; adopting a stricter nonce-based policy would
    // need those inline scripts wired through Next's nonce mechanism. If a
    // new analytics/marketing tag is added later, its domain needs adding
    // to connect-src/script-src here or the browser will silently block it.
    const csp = [
      "default-src 'self'",
      // Razorpay's payment-button script is embedded on the homepage; GTM,
      // Clarity and Ahrefs are the analytics/tag scripts.
      "script-src 'self' 'unsafe-inline' https://www.googletagmanager.com https://analytics.ahrefs.com https://www.clarity.ms https://*.clarity.ms https://checkout.razorpay.com https://*.razorpay.com",
      "style-src 'self' 'unsafe-inline'",
      "img-src 'self' data: blob: https:",
      "font-src 'self' data:",
      "connect-src 'self' https://*.googletagmanager.com https://*.google-analytics.com https://*.analytics.google.com https://stats.g.doubleclick.net https://analytics.ahrefs.com https://www.clarity.ms https://*.clarity.ms https://*.razorpay.com",
      // YouTube testimonial videos (homepage) and Razorpay's checkout frame.
      "frame-src https://www.googletagmanager.com https://www.youtube.com https://www.youtube-nocookie.com https://api.razorpay.com https://checkout.razorpay.com",
      "media-src 'self' https:",
      "object-src 'none'",
      "base-uri 'self'",
    ].join('; ');

    return [
      {
        source: "/:path*",
        headers: [
          { key: "X-Content-Type-Options", value: "nosniff" },
          { key: "X-Frame-Options", value: "SAMEORIGIN" },
          { key: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
          { key: "Content-Security-Policy", value: csp },
        ],
      },
      {
        // Content-hashed filename (scripts/combine_global_css.py) — safe to
        // cache forever since a content change always ships under a new hash.
        source: "/wp-content/combined-global-:hash([a-f0-9]+).css",
        headers: [
          { key: "Cache-Control", value: "public, max-age=31536000, immutable" },
        ],
      },
    ];
  },
};

export default nextConfig;

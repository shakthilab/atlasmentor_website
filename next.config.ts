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
    return [
      {
        source: "/:path*",
        headers: [
          { key: "X-Content-Type-Options", value: "nosniff" },
          { key: "X-Frame-Options", value: "SAMEORIGIN" },
          { key: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
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

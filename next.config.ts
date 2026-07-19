import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  trailingSlash: true,
  experimental: {
    webpackMemoryOptimizations: true,
  },
  async redirects() {
    return [
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
    ];
  },
};

export default nextConfig;

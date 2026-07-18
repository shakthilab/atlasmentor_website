import type { Metadata } from "next";

export const SITE_URL = "https://atlasmentor.com";
const SITE_NAME = "Atlas Mentor";
const DEFAULT_OG_IMAGE = "/wp-content/uploads/2024/07/MBBS-Dream-With-Atlas-Mentor.jpg";

interface ScrapedPageData {
  title?: string;
  description?: string;
  canonical?: string;
  robots?: string;
}

// Maps the scraped WordPress "robots" meta string (e.g. "max-image-preview:large")
// onto Next's typed Metadata.robots shape. Only directives we've actually seen are handled.
function parseRobots(robots: string | undefined): Metadata["robots"] {
  if (!robots) return undefined;

  const result: NonNullable<Metadata["robots"]> = {};
  if (robots.includes("noindex")) result.index = false;
  if (robots.includes("nofollow")) result.follow = false;
  if (robots.includes("max-image-preview:large")) result["max-image-preview"] = "large";

  return Object.keys(result).length > 0 ? result : undefined;
}

export function buildPageMetadata(data: ScrapedPageData | null, pathname: string): Metadata {
  if (!data) return {};

  const canonical = data.canonical || `${SITE_URL}${pathname}`;
  const description = data.description || undefined;

  return {
    title: data.title,
    description,
    alternates: { canonical },
    robots: parseRobots(data.robots),
    openGraph: {
      title: data.title,
      description,
      url: canonical,
      siteName: SITE_NAME,
      type: "website",
      images: [DEFAULT_OG_IMAGE],
    },
    twitter: {
      card: "summary_large_image",
      title: data.title,
      description,
      images: [DEFAULT_OG_IMAGE],
    },
  };
}

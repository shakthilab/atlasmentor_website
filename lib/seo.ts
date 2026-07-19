import type { Metadata } from "next";

export const SITE_URL = "https://atlasmentor.com";
export const SITE_NAME = "Atlas Mentor";
export const DEFAULT_OG_IMAGE = "/wp-content/uploads/2024/07/MBBS-Dream-With-Atlas-Mentor.jpg";

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

// --- Structured data (schema.org) helpers -------------------------------
// Countries the site covers, keyed both ways since callers sometimes have
// the URL slug (route param) and sometimes the display name (parsed title).
export const COUNTRY_NAMES: Record<string, string> = {
  russia: "Russia",
  georgia: "Georgia",
  kazakhstan: "Kazakhstan",
  kyrgyzstan: "Kyrgyzstan",
  moldova: "Moldova",
  uzbekistan: "Uzbekistan",
  vietnam: "Vietnam",
};

export const COUNTRY_SLUGS: Record<string, string> = Object.fromEntries(
  Object.entries(COUNTRY_NAMES).map(([slug, name]) => [name, slug])
);

// Individual university pages carry a scraped title shaped like
// "University Name, Country – Atlas Mentor". Only pages matching that
// shape (and a known country) are treated as university pages.
export function parseUniversityTitle(title: string): { name: string; country: string } | null {
  const core = title.split(" – Atlas Mentor")[0].split(" - Atlas Mentor")[0];
  const idx = core.lastIndexOf(",");
  if (idx === -1) return null;

  const name = core.slice(0, idx).trim();
  const country = core.slice(idx + 1).trim();
  if (!(country in COUNTRY_SLUGS)) return null;

  return { name, country };
}

export interface BreadcrumbItem {
  name: string;
  url: string;
}

export function breadcrumbSchema(items: BreadcrumbItem[]): string {
  return JSON.stringify({
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    itemListElement: items.map((item, i) => ({
      "@type": "ListItem",
      position: i + 1,
      name: item.name,
      item: item.url,
    })),
  });
}

export function collegeSchema(opts: {
  name: string;
  country: string;
  url: string;
  description?: string;
}): string {
  return JSON.stringify({
    "@context": "https://schema.org",
    "@type": "CollegeOrUniversity",
    name: opts.name,
    url: opts.url,
    description: opts.description || undefined,
    address: { "@type": "PostalAddress", addressCountry: opts.country },
  });
}

function stripTags(html: string): string {
  return html.replace(/<[^>]+>/g, "").replace(/&#8217;/g, "’").replace(/&amp;/g, "&").replace(/\s+/g, " ").trim();
}

// Pulls real Q&A pairs out of the existing ElementsKit accordion markup so
// FAQPage schema always matches what's actually visible on the page.
export function extractAccordionFAQs(body: string): { question: string; answer: string }[] {
  const titles = [...body.matchAll(/<span class="ekit-accordion-title">([\s\S]*?)<\/span>/g)].map((m) =>
    stripTags(m[1])
  );
  const answers = [
    ...body.matchAll(/<div class="elementskit-card-body ekit-accordion--content">\s*<p>([\s\S]*?)<\/p>/g),
  ].map((m) => stripTags(m[1]));

  const count = Math.min(titles.length, answers.length);
  const faqs = [];
  for (let i = 0; i < count; i++) {
    faqs.push({ question: titles[i], answer: answers[i] });
  }
  return faqs;
}

export function faqPageSchema(faqs: { question: string; answer: string }[]): string | null {
  if (faqs.length === 0) return null;

  return JSON.stringify({
    "@context": "https://schema.org",
    "@type": "FAQPage",
    mainEntity: faqs.map((f) => ({
      "@type": "Question",
      name: f.question,
      acceptedAnswer: { "@type": "Answer", text: f.answer },
    })),
  });
}

export function organizationSchema(): string {
  return JSON.stringify({
    "@context": "https://schema.org",
    "@type": "Organization",
    name: SITE_NAME,
    alternateName: "Elitestudy Abroad Pvt. Ltd.",
    url: `${SITE_URL}/`,
    logo: `${SITE_URL}/wp-content/uploads/2024/07/Atlas-Mentor-Pvt-Ltd.png`,
    description:
      "Atlas Mentor guides Indian students through their MBBS study-abroad journey — university selection, admissions, visa assistance, and pre-departure support.",
    email: "info@atlasmentor.com",
    contactPoint: [
      {
        "@type": "ContactPoint",
        telephone: "+91-7859033144",
        contactType: "customer service",
        areaServed: "IN",
        email: "info@atlasmentor.com",
      },
    ],
    sameAs: ["https://www.instagram.com/atlasmentors/"],
  });
}

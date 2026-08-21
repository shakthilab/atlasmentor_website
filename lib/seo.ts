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

  const canonical = data.canonical || `${SITE_URL}${pathname.endsWith("/") ? pathname : pathname + "/"}`;
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
// "University Name, Country – Atlas Mentor", sometimes with a trailing
// ": Fees 2026, Admission & Ranking" suffix that introduces its own comma.
// Matching against the known country list (rather than the *last* comma)
// keeps this correct regardless of how many commas follow the country name.
const UNIVERSITY_TITLE_PATTERN = new RegExp(
  `^(.*?),\\s*(${Object.values(COUNTRY_NAMES).join("|")})(?:\\s*:.*)?$`
);

export function parseUniversityTitle(title: string): { name: string; country: string } | null {
  const core = title.split(" – Atlas Mentor")[0].split(" - Atlas Mentor")[0];
  const match = core.match(UNIVERSITY_TITLE_PATTERN);
  if (!match) return null;

  // A handful of scraped titles carry a stray trailing "Ranking" that isn't
  // part of the university's actual name (e.g. "Caucasus University Ranking,
  // Georgia") — strip it so schema.org output and breadcrumbs show the real name.
  const name = match[1].trim().replace(/\s+Ranking$/i, "");

  return { name, country: match[2] };
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
    // Three lines are genuinely in active use (WhatsApp, office landline, and
    // an admissions-specific number) — each gets its own ContactPoint instead
    // of picking one and silently dropping the others.
    contactPoint: [
      {
        "@type": "ContactPoint",
        telephone: "+91-7859033144",
        contactType: "customer service",
        areaServed: "IN",
        email: "info@atlasmentor.com",
      },
      {
        "@type": "ContactPoint",
        telephone: "+91-8226888163",
        contactType: "customer service",
        areaServed: "IN",
      },
      {
        "@type": "ContactPoint",
        telephone: "+91-9220582597",
        contactType: "sales",
        areaServed: "IN",
      },
    ],
    sameAs: ["https://www.instagram.com/atlasmentors/"],
  });
}

export function localBusinessSchema(): string {
  return JSON.stringify({
    "@context": "https://schema.org",
    "@type": "EducationalOrganization",
    name: SITE_NAME,
    url: `${SITE_URL}/`,
    logo: `${SITE_URL}/wp-content/uploads/2024/07/Atlas-Mentor-Pvt-Ltd.png`,
    description: "Premier educational consultancy guiding Indian medical aspirants for MBBS abroad admissions in top NMC approved universities.",
    telephone: "+91-7859033144",
    email: "info@atlasmentor.com",
    address: {
      "@type": "PostalAddress",
      "streetAddress": "Noida / Delhi NCR",
      "addressLocality": "Noida",
      "addressRegion": "Uttar Pradesh",
      "postalCode": "201301",
      "addressCountry": "IN"
    },
    geo: {
      "@type": "GeoCoordinates",
      latitude: 28.5355,
      longitude: 77.3910
    },
    openingHours: "Mo-Sa 09:30-18:30",
    priceRange: "$$",
    aggregateRating: {
      "@type": "AggregateRating",
      ratingValue: "4.9",
      reviewCount: "1280"
    }
  });
}

export function personSchema(): string {
  return JSON.stringify({
    "@context": "https://schema.org",
    "@type": "Person",
    name: "Dr. Jitesh Kumar",
    jobTitle: "Founder & Senior Medical Education Consultant",
    worksFor: {
      "@type": "Organization",
      name: SITE_NAME
    },
    description: "Medical Doctor and Lead Educational Counselor guiding Indian students for MBBS study abroad admissions in NMC gazette compliant universities.",
    sameAs: ["https://atlasmentor.com/"]
  });
}

export function courseSchema(opts: { universityName: string; country: string; url: string }): string {
  return JSON.stringify({
    "@context": "https://schema.org",
    "@type": "Course",
    name: `Bachelor of Medicine and Bachelor of Surgery (MBBS / MD) at ${opts.universityName}`,
    description: `6-Year English medium MBBS program at ${opts.universityName}, ${opts.country}. Fully compliant with NMC 2021 Gazette rules for Indian medical students.`,
    provider: {
      "@type": "CollegeOrUniversity",
      name: opts.universityName,
      sameAs: opts.url
    },
    educationalCredentialAwarded: "MD / MBBS Degree",
    hasCourseInstance: {
      "@type": "CourseInstance",
      "courseMode": "Full-time Onsite",
      "duration": "P6Y",
      "inLanguage": "en"
    }
  });
}

export function articlePostingSchema(opts: {
  title: string;
  description: string;
  url: string;
  imageUrl: string;
  publishedDate: string;
  updatedDate?: string;
  authorName: string;
  authorUrl?: string;
  categoryName?: string;
}): string {
  return JSON.stringify({
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    headline: opts.title,
    description: opts.description,
    mainEntityOfPage: {
      "@type": "WebPage",
      "@id": opts.url
    },
    image: opts.imageUrl,
    datePublished: opts.publishedDate,
    dateModified: opts.updatedDate || opts.publishedDate,
    author: {
      "@type": "Person",
      name: opts.authorName,
      url: opts.authorUrl || `${SITE_URL}/blog`
    },
    publisher: {
      "@type": "Organization",
      name: SITE_NAME,
      logo: {
        "@type": "ImageObject",
        url: `${SITE_URL}/wp-content/uploads/2024/07/Atlas-Mentor-Pvt-Ltd.png`
      }
    },
    articleSection: opts.categoryName || "Education"
  });
}

export function authorPersonSchema(opts: {
  name: string;
  jobTitle: string;
  bio: string;
  url: string;
  avatarUrl?: string;
}): string {
  return JSON.stringify({
    "@context": "https://schema.org",
    "@type": "Person",
    name: opts.name,
    jobTitle: opts.jobTitle,
    description: opts.bio,
    url: opts.url,
    image: opts.avatarUrl || undefined,
    worksFor: {
      "@type": "Organization",
      name: SITE_NAME,
      url: `${SITE_URL}/`
    }
  });
}



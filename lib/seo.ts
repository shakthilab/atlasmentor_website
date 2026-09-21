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
    sameAs: [
      "https://www.instagram.com/atlasmentors/",
      "https://www.youtube.com/@Atlasmentor",
    ],
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
    // NOTE: aggregateRating intentionally omitted. Google's structured-data
    // guidelines require rating/review markup to reflect content that is
    // genuinely visible on the page (see schema.org Review/AggregateRating
    // policy). Re-add this only once a real, visible reviews section exists
    // that the numbers can be traced back to — see reviewSchema() below,
    // which is built from the actual testimonials shown on the homepage.
  });
}

// Built from the real, visible testimonials on the homepage. Each entry here
// must have a matching visible testimonial on the page — do not add entries
// that aren't shown to visitors, and do not hand-adjust the numbers without
// updating the visible copy to match.
export const HOMEPAGE_TESTIMONIALS: {
  author: string;
  location: string;
  rating: number;
  reviewBody: string;
}[] = [
  {
    author: "Rahul",
    location: "Mumbai",
    rating: 5,
    reviewBody:
      "Atlas Mentor made my dream of studying MBBS in Russia a reality. Their personalized support and guidance throughout the application process were invaluable. I'm grateful for their expertise and dedication.",
  },
  {
    author: "Priya",
    location: "Delhi",
    rating: 5,
    reviewBody:
      "Choosing Atlas Mentor was the best decision for my MBBS journey in Georgia. They provided comprehensive assistance, from visa applications to pre-departure preparations. I couldn't have asked for a better support system.",
  },
  {
    author: "Karan",
    location: "Bangalore",
    rating: 5,
    reviewBody:
      "Thanks to Atlas Mentor, I secured admission to a top medical university in Kazakhstan. Their team's knowledge and commitment ensured a smooth transition, and I'm excited for the opportunities ahead.",
  },
];

export function reviewSchema(): string {
  const ratings = HOMEPAGE_TESTIMONIALS.map((t) => t.rating);
  const avg = ratings.reduce((a, b) => a + b, 0) / ratings.length;

  return JSON.stringify({
    "@context": "https://schema.org",
    "@type": "EducationalOrganization",
    name: SITE_NAME,
    url: `${SITE_URL}/`,
    aggregateRating: {
      "@type": "AggregateRating",
      ratingValue: avg.toFixed(1),
      reviewCount: ratings.length,
    },
    review: HOMEPAGE_TESTIMONIALS.map((t) => ({
      "@type": "Review",
      author: { "@type": "Person", name: t.author },
      reviewRating: {
        "@type": "Rating",
        ratingValue: t.rating,
        bestRating: 5,
      },
      reviewBody: t.reviewBody,
    })),
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
    url: `${SITE_URL}/dr-jitesh-kumar/`,
    // /dr-jitesh-kumar/ is a real, on-site bio page (see data/pages/dr-jitesh-kumar.json)
    // and legitimately belongs here. Still TODO: add a real, independently
    // verifiable *external* profile (LinkedIn, a registered medical/education
    // council listing, etc.) once one exists — an on-site bio alone still
    // carries less trust weight with search/AI systems than third-party
    // corroboration. Do not fill this with a guessed or unverified URL.
    sameAs: [`${SITE_URL}/dr-jitesh-kumar/`]
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

// The reviewer/author identity shown in the visible byline on guide and
// university pages, and reused in articleSchema()'s author/reviewedBy
// fields so the visible byline and the structured data always agree. Kept
// in one place deliberately: if this ever changes, both the schema and the
// on-page text update together instead of drifting apart the way the old
// aggregateRating did.
export const CONTENT_REVIEWER = {
  name: "Dr. Jitesh Kumar",
  jobTitle: "Founder & Senior Medical Education Consultant",
  bioUrl: `${SITE_URL}/dr-jitesh-kumar/`,
};

// Last time the guide/university content itself was substantively reviewed,
// not a build timestamp. Update this string when the underlying content
// (fees, eligibility, NMC status) is actually re-checked, so the visible
// date and the dateModified schema stay honest rather than auto-incrementing
// on every deploy.
export const CONTENT_LAST_REVIEWED = "2026-09-05";

export function articleSchema(opts: { headline: string; url: string; datePublished?: string }): string {
  return JSON.stringify({
    "@context": "https://schema.org",
    "@type": "Article",
    headline: opts.headline,
    url: opts.url,
    dateModified: CONTENT_LAST_REVIEWED,
    datePublished: opts.datePublished || CONTENT_LAST_REVIEWED,
    author: {
      "@type": "Person",
      name: CONTENT_REVIEWER.name,
      jobTitle: CONTENT_REVIEWER.jobTitle,
      url: CONTENT_REVIEWER.bioUrl,
    },
    reviewedBy: {
      "@type": "Person",
      name: CONTENT_REVIEWER.name,
      jobTitle: CONTENT_REVIEWER.jobTitle,
      url: CONTENT_REVIEWER.bioUrl,
    },
    publisher: {
      "@type": "Organization",
      name: SITE_NAME,
      url: `${SITE_URL}/`,
    },
  });
}


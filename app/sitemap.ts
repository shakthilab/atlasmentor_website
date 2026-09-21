import fs from 'fs';
import path from 'path';
import type { MetadataRoute } from 'next';
import { SITE_URL } from '@/lib/seo';

interface ScrapedPageData {
  canonical?: string;
  robots?: string;
}

function readPageData(filePath: string): ScrapedPageData | null {
  if (!fs.existsSync(filePath)) return null;
  return JSON.parse(fs.readFileSync(filePath, 'utf8'));
}

function isIndexable(data: ScrapedPageData | null): boolean {
  return !data?.robots?.includes('noindex');
}

function getFileLastModified(filePath: string): Date {
  if (!fs.existsSync(filePath)) return new Date();
  return fs.statSync(filePath).mtime;
}

export default function sitemap(): MetadataRoute.Sitemap {
  const entries: MetadataRoute.Sitemap = [];

  const indexFile = path.join(process.cwd(), 'data/pages/index.json');
  const homepageData = readPageData(indexFile);
  if (isIndexable(homepageData)) {
    entries.push({
      url: homepageData?.canonical || `${SITE_URL}/`,
      lastModified: getFileLastModified(indexFile),
      changeFrequency: 'weekly',
      priority: 1
    });
  }

  // Top-level pillar/hub pages (e.g. "study-mbbs-in-georgia-for-indian-students",
  // "mbbs-abroad") sit one level higher in the site's own information
  // architecture than an individual university page, so they carry more
  // internal link equity from global nav and deserve a higher sitemap
  // priority than a leaf-level university page.
  const HUB_SLUG_PATTERN = /^study-mbbs-in-.+-for-indian-students$/;
  const HUB_SLUGS = new Set(['mbbs-abroad', 'contact-us']);
  const LEGAL_SLUGS = new Set(['privacy-policy', 'terms-of-service', 'cookie-policy']);

  const pagesDir = path.join(process.cwd(), 'data/pages');
  for (const file of fs.readdirSync(pagesDir)) {
    if (!file.endsWith('.json') || file === 'index.json') continue;
    const slug = file.replace('.json', '');
    const filePath = path.join(pagesDir, file);
    const data = readPageData(filePath);
    if (isIndexable(data)) {
      const isHub = HUB_SLUG_PATTERN.test(slug) || HUB_SLUGS.has(slug);
      const isLegal = LEGAL_SLUGS.has(slug);
      entries.push({
        url: data?.canonical || `${SITE_URL}/${slug}/`,
        lastModified: getFileLastModified(filePath),
        changeFrequency: isLegal ? 'yearly' : 'weekly',
        priority: isLegal ? 0.3 : isHub ? 0.9 : 0.8
      });
    }
  }

  const countryDir = path.join(process.cwd(), 'data/pages/mbbs-university');
  if (fs.existsSync(countryDir)) {
    for (const file of fs.readdirSync(countryDir)) {
      if (!file.endsWith('.json')) continue;
      const country = file.replace('.json', '');
      const filePath = path.join(countryDir, file);
      const data = readPageData(filePath);
      if (isIndexable(data)) {
        entries.push({
          url: data?.canonical || `${SITE_URL}/mbbs-university/${country}/`,
          lastModified: getFileLastModified(filePath),
          // Country directory pages are a hub one level above individual
          // university pages in the site's IA (see comment above).
          changeFrequency: 'weekly',
          priority: 0.9
        });
      }
    }
  }

  return entries;
}

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

export default function sitemap(): MetadataRoute.Sitemap {
  const entries: MetadataRoute.Sitemap = [];

  const homepageData = readPageData(path.join(process.cwd(), 'data/pages/index.json'));
  if (isIndexable(homepageData)) {
    entries.push({ url: homepageData?.canonical || `${SITE_URL}/`, changeFrequency: 'monthly', priority: 1 });
  }

  const pagesDir = path.join(process.cwd(), 'data/pages');
  for (const file of fs.readdirSync(pagesDir)) {
    if (!file.endsWith('.json') || file === 'index.json') continue;
    const slug = file.replace('.json', '');
    const data = readPageData(path.join(pagesDir, file));
    if (isIndexable(data)) {
      entries.push({ url: data?.canonical || `${SITE_URL}/${slug}`, changeFrequency: 'monthly', priority: 0.8 });
    }
  }

  const countryDir = path.join(process.cwd(), 'data/pages/mbbs-university');
  if (fs.existsSync(countryDir)) {
    for (const file of fs.readdirSync(countryDir)) {
      if (!file.endsWith('.json')) continue;
      const country = file.replace('.json', '');
      const data = readPageData(path.join(countryDir, file));
      if (isIndexable(data)) {
        entries.push({ url: data?.canonical || `${SITE_URL}/mbbs-university/${country}`, changeFrequency: 'monthly', priority: 0.8 });
      }
    }
  }

  return entries;
}

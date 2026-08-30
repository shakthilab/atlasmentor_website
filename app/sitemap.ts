import fs from 'fs';
import path from 'path';
import type { MetadataRoute } from 'next';
import { SITE_URL } from '@/lib/seo';
import { getAllPosts, getAllCategories, getAllAuthors } from '@/lib/blog-data';

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

  const pagesDir = path.join(process.cwd(), 'data/pages');
  for (const file of fs.readdirSync(pagesDir)) {
    if (!file.endsWith('.json') || file === 'index.json') continue;
    const slug = file.replace('.json', '');
    const filePath = path.join(pagesDir, file);
    const data = readPageData(filePath);
    if (isIndexable(data)) {
      entries.push({
        url: data?.canonical || `${SITE_URL}/${slug}/`,
        lastModified: getFileLastModified(filePath),
        changeFrequency: 'weekly',
        priority: 0.8
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
          changeFrequency: 'weekly',
          priority: 0.8
        });
      }
    }
  }

  entries.push({
    url: `${SITE_URL}/blog/`,
    changeFrequency: 'daily',
    priority: 0.9,
  });

  for (const post of getAllPosts()) {
    entries.push({
      url: `${SITE_URL}/blog/${post.slug}/`,
      lastModified: new Date(post.updatedDate || post.publishedDate),
      changeFrequency: 'monthly',
      priority: 0.7,
    });
  }

  for (const category of getAllCategories()) {
    entries.push({
      url: `${SITE_URL}/blog/category/${category.slug}/`,
      changeFrequency: 'weekly',
      priority: 0.6,
    });
  }

  for (const author of getAllAuthors()) {
    entries.push({
      url: `${SITE_URL}/blog/author/${author.id}/`,
      changeFrequency: 'monthly',
      priority: 0.5,
    });
  }

  return entries;
}

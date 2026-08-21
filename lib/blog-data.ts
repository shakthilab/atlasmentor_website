import fs from 'fs';
import path from 'path';
import { BlogPost, BlogCategory, BlogAuthor, PaginatedPosts, BlogFilterOptions } from './blog-types';

const BLOG_DIR = path.join(process.cwd(), 'data/blog');

export function getAllPosts(): BlogPost[] {
  try {
    const filePath = path.join(BLOG_DIR, 'posts.json');
    if (!fs.existsSync(filePath)) return [];
    const fileData = fs.readFileSync(filePath, 'utf8');
    const posts: BlogPost[] = JSON.parse(fileData);
    
    // Attach full author object and categoryName if missing
    const authors = getAllAuthors();
    const categories = getAllCategories();
    
    return posts.map((post) => {
      const author = authors.find((a) => a.id === post.authorId);
      const categoryObj = categories.find((c) => c.slug === post.category);
      return {
        ...post,
        author: author || undefined,
        categoryName: categoryObj ? categoryObj.name : post.categoryName || post.category,
      };
    });
  } catch (error) {
    console.error('Error reading blog posts:', error);
    return [];
  }
}

export function getAllCategories(): BlogCategory[] {
  try {
    const filePath = path.join(BLOG_DIR, 'categories.json');
    if (!fs.existsSync(filePath)) return [];
    const fileData = fs.readFileSync(filePath, 'utf8');
    const categories: BlogCategory[] = JSON.parse(fileData);
    
    // Calculate post count for each category dynamically
    const posts = getAllRawPosts();
    return categories.map((cat) => ({
      ...cat,
      count: posts.filter((p) => p.category === cat.slug).length,
    }));
  } catch (error) {
    console.error('Error reading blog categories:', error);
    return [];
  }
}

export function getAllAuthors(): BlogAuthor[] {
  try {
    const filePath = path.join(BLOG_DIR, 'authors.json');
    if (!fs.existsSync(filePath)) return [];
    const fileData = fs.readFileSync(filePath, 'utf8');
    return JSON.parse(fileData);
  } catch (error) {
    console.error('Error reading blog authors:', error);
    return [];
  }
}

function getAllRawPosts(): BlogPost[] {
  try {
    const filePath = path.join(BLOG_DIR, 'posts.json');
    if (!fs.existsSync(filePath)) return [];
    return JSON.parse(fs.readFileSync(filePath, 'utf8'));
  } catch {
    return [];
  }
}

export function getFeaturedPost(): BlogPost | null {
  const posts = getAllPosts();
  return posts.find((p) => p.featured) || posts[0] || null;
}

export function getPopularPosts(limit = 4): BlogPost[] {
  const posts = getAllPosts();
  return posts.filter((p) => p.popular).slice(0, limit);
}

export function getPostBySlug(slug: string): BlogPost | null {
  const posts = getAllPosts();
  return posts.find((p) => p.slug === slug) || null;
}

export function getPostsByCategory(categorySlug: string): BlogPost[] {
  const posts = getAllPosts();
  return posts.filter((p) => p.category === categorySlug);
}

export function getPostsByAuthor(authorId: string): BlogPost[] {
  const posts = getAllPosts();
  return posts.filter((p) => p.authorId === authorId);
}

export function getAuthorById(authorId: string): BlogAuthor | null {
  const authors = getAllAuthors();
  return authors.find((a) => a.id === authorId) || null;
}

export function getCategoryBySlug(categorySlug: string): BlogCategory | null {
  const categories = getAllCategories();
  return categories.find((c) => c.slug === categorySlug) || null;
}

export function getRelatedPosts(currentSlug: string, category: string, limit = 3): BlogPost[] {
  const posts = getAllPosts();
  const currentPost = posts.find((p) => p.slug === currentSlug);
  
  if (currentPost && currentPost.relatedSlugs && currentPost.relatedSlugs.length > 0) {
    const explicitRelated = posts.filter((p) => currentPost.relatedSlugs?.includes(p.slug));
    if (explicitRelated.length >= limit) return explicitRelated.slice(0, limit);
  }

  // Fallback to same category excluding current post
  const sameCategory = posts.filter((p) => p.slug !== currentSlug && p.category === category);
  if (sameCategory.length >= limit) return sameCategory.slice(0, limit);

  // Fallback to latest posts excluding current
  return posts.filter((p) => p.slug !== currentSlug).slice(0, limit);
}

export function searchPosts(query: string): BlogPost[] {
  if (!query || query.trim() === '') return [];
  const posts = getAllPosts();
  const q = query.toLowerCase().trim();

  return posts.filter((post) => {
    const titleMatch = post.title.toLowerCase().includes(q);
    const excerptMatch = post.excerpt.toLowerCase().includes(q);
    const contentMatch = post.content.toLowerCase().includes(q);
    const categoryMatch = post.categoryName?.toLowerCase().includes(q) || post.category.toLowerCase().includes(q);
    const tagMatch = post.tags.some((t) => t.toLowerCase().includes(q));

    return titleMatch || excerptMatch || contentMatch || categoryMatch || tagMatch;
  });
}

export function getFilteredPosts(options: BlogFilterOptions): PaginatedPosts {
  let posts = getAllPosts();

  if (options.category && options.category !== 'all') {
    posts = posts.filter((p) => p.category === options.category);
  }

  if (options.authorId) {
    posts = posts.filter((p) => p.authorId === options.authorId);
  }

  if (options.searchQuery) {
    const q = options.searchQuery.toLowerCase().trim();
    posts = posts.filter((p) =>
      p.title.toLowerCase().includes(q) ||
      p.excerpt.toLowerCase().includes(q) ||
      p.content.toLowerCase().includes(q) ||
      p.tags.some((t) => t.toLowerCase().includes(q))
    );
  }

  if (options.featuredOnly) {
    posts = posts.filter((p) => p.featured);
  }

  if (options.popularOnly) {
    posts = posts.filter((p) => p.popular);
  }

  const page = options.page || 1;
  const limit = options.limit || 6;
  const totalPosts = posts.length;
  const totalPages = Math.ceil(totalPosts / limit) || 1;
  const startIndex = (page - 1) * limit;
  const paginatedPosts = posts.slice(startIndex, startIndex + limit);

  return {
    posts: paginatedPosts,
    totalPosts,
    currentPage: page,
    totalPages,
  };
}

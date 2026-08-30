export interface BlogAuthor {
  id: string;
  name: string;
  role: string;
  avatar: string;
  bio: string;
  socials?: {
    linkedin?: string;
    twitter?: string;
    instagram?: string;
    website?: string;
  };
}

export interface BlogCategory {
  slug: string;
  name: string;
  description: string;
  icon?: string;
  count?: number;
}

export interface FAQItem {
  question: string;
  answer: string;
}

export interface SEOConfig {
  metaTitle: string;
  metaDescription: string;
  canonicalUrl?: string;
  keywords?: string[];
}

export interface BlogPost {
  slug: string;
  title: string;
  excerpt: string;
  content: string;
  coverImage: string;
  imageAlt: string; // Descriptive, SEO-friendly alt text for coverImage
  category: string; // Slug of category
  categoryName?: string; // Display name
  authorId: string;
  author?: BlogAuthor;
  publishedDate: string; // e.g. "2026-07-25" or "July 25, 2026"
  updatedDate?: string;
  readingTime: string; // e.g. "6 min read"
  tags: string[];
  featured?: boolean;
  popular?: boolean;
  seo?: SEOConfig;
  relatedSlugs?: string[];
  faq?: FAQItem[];
}

export interface BlogFilterOptions {
  category?: string;
  tag?: string;
  authorId?: string;
  searchQuery?: string;
  featuredOnly?: boolean;
  popularOnly?: boolean;
  page?: number;
  limit?: number;
}

export interface PaginatedPosts {
  posts: BlogPost[];
  totalPosts: number;
  currentPage: number;
  totalPages: number;
}

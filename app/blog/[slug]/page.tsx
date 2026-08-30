import { Metadata } from 'next';
import { notFound } from 'next/navigation';
import Image from 'next/image';
import Link from 'next/link';
import { getPostBySlug, getAllPosts, getRelatedPosts, getAuthorById } from '@/lib/blog-data';
import ReadingProgressBar from '@/components/blog/ReadingProgressBar';
import TableOfContents from '@/components/blog/TableOfContents';
import SocialShareButtons from '@/components/blog/SocialShareButtons';
import AuthorBox from '@/components/blog/AuthorBox';
import CallToActionBanner from '@/components/blog/CallToActionBanner';
import RelatedArticles from '@/components/blog/RelatedArticles';
import NewsletterCard from '@/components/blog/NewsletterCard';
import {
  SITE_NAME,
  SITE_URL,
  breadcrumbSchema,
  articlePostingSchema,
  authorPersonSchema,
  faqPageSchema,
} from '@/lib/seo';

interface BlogDetailProps {
  params: Promise<{ slug: string }>;
}

export async function generateStaticParams() {
  const posts = getAllPosts();
  return posts.map((post) => ({
    slug: post.slug,
  }));
}

export async function generateMetadata({ params }: BlogDetailProps): Promise<Metadata> {
  const resolvedParams = await params;
  const post = getPostBySlug(resolvedParams.slug);

  if (!post) {
    return {
      title: `Article Not Found – ${SITE_NAME}`,
    };
  }

  const pageTitle = post.seo?.metaTitle || `${post.title} – ${SITE_NAME}`;
  const pageDescription = post.seo?.metaDescription || post.excerpt;
  const canonicalUrl = `${SITE_URL}/blog/${post.slug}`;

  return {
    title: pageTitle,
    description: pageDescription,
    keywords: post.seo?.keywords,
    alternates: {
      canonical: canonicalUrl,
    },
    openGraph: {
      title: pageTitle,
      description: pageDescription,
      url: canonicalUrl,
      siteName: SITE_NAME,
      type: 'article',
      publishedTime: post.publishedDate,
      modifiedTime: post.updatedDate || post.publishedDate,
      authors: post.author ? [post.author.name] : ['Atlas Mentor'],
      images: [
        {
          url: post.coverImage,
          width: 1200,
          height: 630,
          alt: post.imageAlt || post.title,
        },
      ],
    },
    twitter: {
      card: 'summary_large_image',
      title: pageTitle,
      description: pageDescription,
      images: [post.coverImage],
    },
  };
}

export default async function BlogDetailPage({ params }: BlogDetailProps) {
  const resolvedParams = await params;
  const post = getPostBySlug(resolvedParams.slug);

  if (!post) {
    notFound();
  }

  const relatedPosts = getRelatedPosts(post.slug, post.category, 3);
  const articleUrl = `${SITE_URL}/blog/${post.slug}`;

  const breadcrumbs = [
    { name: 'Home', url: `${SITE_URL}/` },
    { name: 'Blog', url: `${SITE_URL}/blog` },
    { name: post.categoryName || post.category, url: `${SITE_URL}/blog/category/${post.category}` },
    { name: post.title, url: articleUrl },
  ];

  const jsonLdArticle = articlePostingSchema({
    title: post.title,
    description: post.excerpt,
    url: articleUrl,
    imageUrl: post.coverImage,
    publishedDate: post.publishedDate,
    updatedDate: post.updatedDate,
    authorName: post.author?.name || 'Atlas Mentor',
    authorUrl: post.author ? `${SITE_URL}/blog/author/${post.author.id}` : `${SITE_URL}/blog`,
    categoryName: post.categoryName,
  });

  const jsonLdAuthor = post.author
    ? authorPersonSchema({
        name: post.author.name,
        jobTitle: post.author.role,
        bio: post.author.bio,
        url: `${SITE_URL}/blog/author/${post.author.id}`,
        avatarUrl: post.author.avatar,
      })
    : null;

  const jsonLdFaq = post.faq && post.faq.length > 0 ? faqPageSchema(post.faq) : null;

  return (
    <>
      <ReadingProgressBar />

      {/* Structured Data Schemas */}
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: breadcrumbSchema(breadcrumbs) }}
      />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: jsonLdArticle }}
      />
      {jsonLdAuthor && (
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: jsonLdAuthor }}
        />
      )}
      {jsonLdFaq && (
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: jsonLdFaq }}
        />
      )}

      <main className="min-h-screen bg-slate-50/60 pb-20 pt-32 sm:pt-36 lg:pt-40">
        {/* Top Hero Container */}
        <header className="bg-white border-b border-slate-200/80 py-10 sm:py-14 px-4 sm:px-6 lg:px-8">
          <div className="max-w-4xl mx-auto">
            {/* Breadcrumb Navigation */}
            <nav className="flex items-center space-x-2 text-xs text-slate-500 mb-6 flex-wrap gap-y-1">
              <Link href="/" className="hover:text-[#DE8017] transition-colors">Home</Link>
              <span>/</span>
              <Link href="/blog" className="hover:text-[#DE8017] transition-colors">Blog</Link>
              <span>/</span>
              <Link href={`/blog/category/${post.category}`} className="hover:text-[#DE8017] transition-colors font-medium">
                {post.categoryName || post.category}
              </Link>
            </nav>

            {/* Category Pill */}
            <Link
              href={`/blog/category/${post.category}`}
              className="inline-block bg-[#DE8017] text-white text-xs font-bold px-3.5 py-1.5 rounded-full mb-4 shadow-sm hover:bg-[#c97112] transition-colors"
            >
              {post.categoryName || post.category}
            </Link>

            {/* Article Main Heading */}
            <h1 className="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-[#00267C] tracking-tight leading-tight mb-6">
              {post.title}
            </h1>

            {/* Author Meta Line & Social Share */}
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pt-4 border-t border-slate-100">
              {post.author && (
                <div className="flex items-center space-x-3">
                  <div className="relative w-11 h-11 rounded-full overflow-hidden border-2 border-[#DE8017]">
                    <Image
                      src={post.author.avatar}
                      alt={post.author.name}
                      fill
                      sizes="44px"
                      className="object-cover"
                    />
                  </div>
                  <div>
                    <Link
                      href={`/blog/author/${post.author.id}`}
                      className="block text-sm font-bold text-[#00267C] hover:text-[#DE8017] transition-colors"
                    >
                      {post.author.name}
                    </Link>
                    <div className="flex items-center text-xs text-slate-500 space-x-2">
                      <span>{post.publishedDate}</span>
                      <span>•</span>
                      <span>{post.readingTime}</span>
                    </div>
                  </div>
                </div>
              )}

              <SocialShareButtons title={post.title} url={articleUrl} />
            </div>
          </div>
        </header>

        {/* Hero Cover Image Container */}
        <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 -mt-6 sm:-mt-8 mb-12">
          <div className="relative aspect-[16/9] w-full rounded-3xl overflow-hidden shadow-2xl bg-slate-200 border border-white">
            <Image
              src={post.coverImage}
              alt={post.imageAlt || post.title}
              fill
              priority
              className="object-cover"
            />
          </div>
        </div>

        {/* Main Article Content & Table of Contents Sidebar */}
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-12">
            {/* Table of Contents Column (Desktop Left / 3 cols) */}
            <div className="hidden lg:block lg:col-span-3">
              <TableOfContents contentHtml={post.content} />
            </div>

            {/* Main Article Body Column (9 cols or centered) */}
            <div className="lg:col-span-9 max-w-4xl">
              {/* Article Typography Prose */}
              <article
                className="blog-prose bg-white p-6 sm:p-10 rounded-3xl border border-slate-200/80 shadow-sm"
                dangerouslySetInnerHTML={{ __html: post.content }}
              />

              {/* Tags List */}
              {post.tags && post.tags.length > 0 && (
                <div className="mt-8 flex items-center flex-wrap gap-2">
                  <span className="text-xs font-bold text-slate-400 uppercase mr-2">Tags:</span>
                  {post.tags.map((tag) => (
                    <span
                      key={tag}
                      className="bg-slate-100 text-slate-600 text-xs font-medium px-3 py-1.5 rounded-lg border border-slate-200"
                    >
                      #{tag}
                    </span>
                  ))}
                </div>
              )}

              {/* Author Box */}
              {post.author && <AuthorBox author={post.author} />}

              {/* High-Converting CTA Banner */}
              <CallToActionBanner />

              {/* Related Articles */}
              <RelatedArticles posts={relatedPosts} />

              {/* Newsletter Subscription Card */}
              <NewsletterCard />
            </div>
          </div>
        </div>
      </main>
    </>
  );
}

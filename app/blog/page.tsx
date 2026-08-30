import { Metadata } from 'next';
import {
  getAllCategories,
  getFeaturedPost,
  getPopularPosts,
  getFilteredPosts,
} from '@/lib/blog-data';
import BlogHero from '@/components/blog/BlogHero';
import FeaturedArticleCard from '@/components/blog/FeaturedArticleCard';
import ArticleCard from '@/components/blog/ArticleCard';
import BlogSidebar from '@/components/blog/BlogSidebar';
import BlogPagination from '@/components/blog/BlogPagination';
import { SITE_NAME, SITE_URL, breadcrumbSchema } from '@/lib/seo';

export const metadata: Metadata = {
  title: `Study Abroad & MBBS Abroad Blog – ${SITE_NAME}`,
  description:
    'Latest updates, admission guides, university comparisons, scholarships, visa information, student success stories, and expert advice for Indian medical aspirants.',
  alternates: {
    canonical: `${SITE_URL}/blog`,
  },
  openGraph: {
    title: `Study Abroad & MBBS Abroad Blog – ${SITE_NAME}`,
    description:
      'Latest updates, admission guides, university comparisons, scholarships, visa information, student success stories, and expert advice.',
    url: `${SITE_URL}/blog`,
    siteName: SITE_NAME,
    type: 'website',
  },
};

interface BlogPageProps {
  searchParams: Promise<{ page?: string }>;
}

export default async function BlogPage({ searchParams }: BlogPageProps) {
  const resolvedParams = await searchParams;
  const currentPage = parseInt(resolvedParams.page || '1', 10);

  const categories = getAllCategories();
  const featuredPost = getFeaturedPost();
  const popularPosts = getPopularPosts(4);

  // Exclude featured post from latest grid if on page 1
  const filterLimit = 6;
  const filteredResult = getFilteredPosts({
    page: currentPage,
    limit: filterLimit,
  });

  const breadcrumbs = [
    { name: 'Home', url: `${SITE_URL}/` },
    { name: 'Blog', url: `${SITE_URL}/blog` },
  ];

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: breadcrumbSchema(breadcrumbs) }}
      />

      <main className="min-h-screen bg-slate-50/60 pb-20">
        {/* Hero Section */}
        <BlogHero categories={categories} activeCategory="all" />

        {/* Main Content Area */}
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-12 sm:pt-16">
          {/* Featured Article Section (Visible on Page 1) */}
          {currentPage === 1 && featuredPost && (
            <section className="mb-12">
              <div className="flex items-center justify-between mb-6">
                <div>
                  <span className="text-xs font-bold uppercase tracking-wider text-[#DE8017]">
                    Editor's Choice
                  </span>
                  <h2 className="text-2xl font-extrabold text-[#00267C]">
                    Featured Article
                  </h2>
                </div>
              </div>
              <FeaturedArticleCard post={featuredPost} />
            </section>
          )}

          {/* Grid + Sidebar Layout */}
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-10">
            {/* Main Articles Grid (8 Cols) */}
            <div className="lg:col-span-8">
              <div className="flex items-center justify-between mb-8 pb-4 border-b border-slate-200">
                <h2 className="text-2xl font-extrabold text-[#00267C]">
                  Latest Articles
                </h2>
                <span className="text-xs text-slate-500 font-medium">
                  Showing {filteredResult.posts.length} of {filteredResult.totalPosts} articles
                </span>
              </div>

              {filteredResult.posts.length > 0 ? (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                  {filteredResult.posts.map((post, idx) => (
                    <ArticleCard key={post.slug} post={post} priority={idx < 2} />
                  ))}
                </div>
              ) : (
                <div className="bg-white p-12 rounded-3xl text-center border border-slate-200 shadow-sm">
                  <p className="text-slate-600 text-base">No articles found on this page.</p>
                </div>
              )}

              {/* Pagination */}
              <BlogPagination
                currentPage={filteredResult.currentPage}
                totalPages={filteredResult.totalPages}
                baseUrl="/blog"
              />
            </div>

            {/* Sidebar (4 Cols) */}
            <div className="lg:col-span-4">
              <BlogSidebar
                categories={categories}
                popularPosts={popularPosts}
                currentCategory="all"
              />
            </div>
          </div>
        </div>
      </main>
    </>
  );
}

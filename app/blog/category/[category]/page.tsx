import { Metadata } from 'next';
import { notFound } from 'next/navigation';
import Link from 'next/link';
import {
  getCategoryBySlug,
  getAllCategories,
  getFilteredPosts,
  getPopularPosts,
  getAllPosts,
} from '@/lib/blog-data';
import ArticleCard from '@/components/blog/ArticleCard';
import BlogSidebar from '@/components/blog/BlogSidebar';
import BlogPagination from '@/components/blog/BlogPagination';
import { SITE_NAME, SITE_URL, breadcrumbSchema } from '@/lib/seo';

interface CategoryPageProps {
  params: Promise<{ category: string }>;
  searchParams: Promise<{ page?: string }>;
}

export async function generateStaticParams() {
  const categories = getAllCategories();
  return categories.map((c) => ({
    category: c.slug,
  }));
}

export async function generateMetadata({ params }: CategoryPageProps): Promise<Metadata> {
  const resolvedParams = await params;
  const category = getCategoryBySlug(resolvedParams.category);

  if (!category) {
    return {
      title: `Category Not Found – ${SITE_NAME}`,
    };
  }

  const title = `${category.name} Articles & Guides – ${SITE_NAME}`;
  const description = category.description;
  const canonical = `${SITE_URL}/blog/category/${category.slug}`;

  return {
    title,
    description,
    alternates: { canonical },
    openGraph: {
      title,
      description,
      url: canonical,
      siteName: SITE_NAME,
      type: 'website',
    },
  };
}

export default async function BlogCategoryPage({ params, searchParams }: CategoryPageProps) {
  const resolvedParams = await params;
  const resolvedSearchParams = await searchParams;
  const categorySlug = resolvedParams.category;
  const currentPage = parseInt(resolvedSearchParams.page || '1', 10);

  const category = getCategoryBySlug(categorySlug);
  if (!category) {
    notFound();
  }

  const categories = getAllCategories();
  const popularPosts = getPopularPosts(4);
  const allPosts = getAllPosts();
  const latestPosts = allPosts.slice(0, 4);

  const filterLimit = 6;
  const paginatedData = getFilteredPosts({
    category: categorySlug,
    page: currentPage,
    limit: filterLimit,
  });

  const breadcrumbs = [
    { name: 'Home', url: `${SITE_URL}/` },
    { name: 'Blog', url: `${SITE_URL}/blog` },
    { name: category.name, url: `${SITE_URL}/blog/category/${category.slug}` },
  ];

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: breadcrumbSchema(breadcrumbs) }}
      />

      <main className="min-h-screen bg-slate-50/60 pb-20">
        {/* Category Hero Banner */}
        <section className="bg-gradient-to-b from-[#0B192C] via-[#0f243f] to-[#0B192C] text-white pt-36 sm:pt-40 pb-16 sm:pb-20 px-4 sm:px-6 lg:px-8 text-center relative overflow-hidden">
          <div className="max-w-4xl mx-auto relative z-10">
            {/* Breadcrumb */}
            <nav className="flex items-center justify-center space-x-2 text-xs text-slate-300 mb-6">
              <Link href="/" className="hover:text-[#DE8017]">Home</Link>
              <span>/</span>
              <Link href="/blog" className="hover:text-[#DE8017]">Blog</Link>
              <span>/</span>
              <span className="text-[#DE8017] font-semibold">{category.name}</span>
            </nav>

            <span className="inline-block bg-[#DE8017] text-white text-xs font-bold uppercase tracking-wider px-3.5 py-1.5 rounded-full mb-4 shadow-md">
              Category
            </span>

            <h1 className="text-3xl sm:text-4xl lg:text-5xl font-extrabold tracking-tight mb-4">
              {category.name}
            </h1>

            <p className="text-slate-300 text-base sm:text-lg max-w-2xl mx-auto leading-relaxed">
              {category.description}
            </p>
          </div>
        </section>

        {/* Content Area */}
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-12 sm:pt-16">
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-10">
            {/* Main Articles Grid (8 Cols) */}
            <div className="lg:col-span-8">
              <div className="flex items-center justify-between mb-8 pb-4 border-b border-slate-200">
                <h2 className="text-xl font-extrabold text-[#0B192C]">
                  {category.name} Articles ({paginatedData.totalPosts})
                </h2>
              </div>

              {paginatedData.posts.length > 0 ? (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                  {paginatedData.posts.map((post) => (
                    <ArticleCard key={post.slug} post={post} />
                  ))}
                </div>
              ) : (
                <div className="bg-white p-12 rounded-3xl text-center border border-slate-200 shadow-sm">
                  <p className="text-slate-600 text-base">No articles found in this category yet.</p>
                </div>
              )}

              {/* Pagination */}
              <BlogPagination
                currentPage={paginatedData.currentPage}
                totalPages={paginatedData.totalPages}
                baseUrl={`/blog/category/${category.slug}`}
              />
            </div>

            {/* Sidebar (4 Cols) */}
            <div className="lg:col-span-4">
              <BlogSidebar
                categories={categories}
                popularPosts={popularPosts}
                latestPosts={latestPosts}
                currentCategory={category.slug}
              />
            </div>
          </div>
        </div>
      </main>
    </>
  );
}

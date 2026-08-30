import { Metadata } from 'next';
import Link from 'next/link';
import { searchPosts, getAllCategories, getPopularPosts } from '@/lib/blog-data';
import ArticleCard from '@/components/blog/ArticleCard';
import BlogSidebar from '@/components/blog/BlogSidebar';
import { SITE_NAME, SITE_URL } from '@/lib/seo';

interface SearchPageProps {
  searchParams: Promise<{ q?: string }>;
}

export async function generateMetadata({ searchParams }: SearchPageProps): Promise<Metadata> {
  const resolvedParams = await searchParams;
  const q = resolvedParams.q || '';
  return {
    title: q ? `Search results for "${q}" – ${SITE_NAME} Blog` : `Search Articles – ${SITE_NAME} Blog`,
    description: `Search results for ${q} on Atlas Mentor study abroad and MBBS blog.`,
    robots: {
      index: false, // Prevents duplicate content index for search results
      follow: true,
    },
  };
}

export default async function BlogSearchPage({ searchParams }: SearchPageProps) {
  const resolvedParams = await searchParams;
  const query = resolvedParams.q || '';

  const results = query ? searchPosts(query) : [];
  const categories = getAllCategories();
  const popularPosts = getPopularPosts(4);

  return (
    <main className="min-h-screen bg-slate-50/60 pb-20 pt-32 sm:pt-36 lg:pt-40">
      {/* Header */}
      <section className="bg-white border-b border-slate-200 py-12 px-4 sm:px-6 lg:px-8">
        <div className="max-w-4xl mx-auto text-center">
          <nav className="flex items-center justify-center space-x-2 text-xs text-slate-500 mb-4">
            <Link href="/" className="hover:text-[#DE8017]">Home</Link>
            <span>/</span>
            <Link href="/blog" className="hover:text-[#DE8017]">Blog</Link>
            <span>/</span>
            <span className="font-semibold text-slate-900">Search Results</span>
          </nav>

          <h1 className="text-3xl sm:text-4xl font-extrabold text-[#0B192C] mb-4">
            {query ? (
              <>
                Search Results for <span className="text-[#DE8017]">"{query}"</span>
              </>
            ) : (
              'Search Blog Articles'
            )}
          </h1>

          <p className="text-slate-600 text-sm">
            {query
              ? `Found ${results.length} article${results.length === 1 ? '' : 's'} matching your query.`
              : 'Type a keyword above or choose a popular topic below.'}
          </p>
        </div>
      </section>

      {/* Main Container */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-12">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-10">
          {/* Main Results (8 Cols) */}
          <div className="lg:col-span-8">
            {results.length > 0 ? (
              <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                {results.map((post) => (
                  <ArticleCard key={post.slug} post={post} />
                ))}
              </div>
            ) : (
              <div className="bg-white p-12 rounded-3xl text-center border border-slate-200 shadow-sm space-y-6">
                <div className="w-16 h-16 bg-slate-100 text-slate-400 rounded-full flex items-center justify-center mx-auto">
                  <svg className="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                  </svg>
                </div>
                <div>
                  <h3 className="text-xl font-bold text-[#0B192C] mb-2">No Articles Found</h3>
                  <p className="text-slate-600 text-sm max-w-md mx-auto">
                    We couldn't find any articles matching "{query}". Try checking spelling, using different keywords, or explore our popular categories.
                  </p>
                </div>

                <div className="pt-4 border-t border-slate-100">
                  <h4 className="text-xs font-bold uppercase tracking-wider text-slate-400 mb-3">Popular Categories</h4>
                  <div className="flex flex-wrap justify-center gap-2">
                    {categories.slice(0, 6).map((cat) => (
                      <Link
                        key={cat.slug}
                        href={`/blog/category/${cat.slug}`}
                        className="bg-slate-100 hover:bg-[#DE8017] hover:text-white text-slate-700 text-xs font-semibold px-3.5 py-2 rounded-xl transition-colors"
                      >
                        {cat.name}
                      </Link>
                    ))}
                  </div>
                </div>
              </div>
            )}
          </div>

          {/* Sidebar (4 Cols) */}
          <div className="lg:col-span-4">
            <BlogSidebar
              categories={categories}
              popularPosts={popularPosts}
            />
          </div>
        </div>
      </div>
    </main>
  );
}

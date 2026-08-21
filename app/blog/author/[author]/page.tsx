import { Metadata } from 'next';
import { notFound } from 'next/navigation';
import Image from 'next/image';
import Link from 'next/link';
import { getAuthorById, getAllAuthors, getPostsByAuthor, getAllCategories, getPopularPosts, getAllPosts } from '@/lib/blog-data';
import ArticleCard from '@/components/blog/ArticleCard';
import BlogSidebar from '@/components/blog/BlogSidebar';
import { SITE_NAME, SITE_URL, authorPersonSchema, breadcrumbSchema } from '@/lib/seo';

interface AuthorPageProps {
  params: Promise<{ author: string }>;
}

export async function generateStaticParams() {
  const authors = getAllAuthors();
  return authors.map((a) => ({
    author: a.id,
  }));
}

export async function generateMetadata({ params }: AuthorPageProps): Promise<Metadata> {
  const resolvedParams = await params;
  const author = getAuthorById(resolvedParams.author);

  if (!author) {
    return { title: `Author Not Found – ${SITE_NAME}` };
  }

  const title = `${author.name} – ${author.role} | ${SITE_NAME}`;
  const description = author.bio;
  const canonical = `${SITE_URL}/blog/author/${author.id}`;

  return {
    title,
    description,
    alternates: { canonical },
    openGraph: {
      title,
      description,
      url: canonical,
      siteName: SITE_NAME,
      type: 'profile',
      images: [author.avatar],
    },
  };
}

export default async function BlogAuthorPage({ params }: AuthorPageProps) {
  const resolvedParams = await params;
  const authorId = resolvedParams.author;
  const author = getAuthorById(authorId);

  if (!author) {
    notFound();
  }

  const posts = getPostsByAuthor(authorId);
  const categories = getAllCategories();
  const popularPosts = getPopularPosts(4);
  const allPosts = getAllPosts();
  const latestPosts = allPosts.slice(0, 4);

  const breadcrumbs = [
    { name: 'Home', url: `${SITE_URL}/` },
    { name: 'Blog', url: `${SITE_URL}/blog` },
    { name: author.name, url: `${SITE_URL}/blog/author/${author.id}` },
  ];

  const jsonLdAuthor = authorPersonSchema({
    name: author.name,
    jobTitle: author.role,
    bio: author.bio,
    url: `${SITE_URL}/blog/author/${author.id}`,
    avatarUrl: author.avatar,
  });

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: breadcrumbSchema(breadcrumbs) }}
      />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: jsonLdAuthor }}
      />

      <main className="min-h-screen bg-slate-50/60 pb-20 pt-32 sm:pt-36 lg:pt-40">
        {/* Author Header Banner */}
        <section className="bg-white border-b border-slate-200 py-12 px-4 sm:px-6 lg:px-8">
          <div className="max-w-4xl mx-auto">
            <nav className="flex items-center space-x-2 text-xs text-slate-500 mb-6">
              <Link href="/" className="hover:text-[#DE8017]">Home</Link>
              <span>/</span>
              <Link href="/blog" className="hover:text-[#DE8017]">Blog</Link>
              <span>/</span>
              <span className="font-semibold text-slate-900">{author.name}</span>
            </nav>

            <div className="flex flex-col sm:flex-row items-center sm:items-start gap-6 text-center sm:text-left">
              <div className="relative w-28 h-28 sm:w-32 sm:h-32 rounded-full overflow-hidden border-4 border-[#DE8017] shadow-xl flex-shrink-0">
                <Image
                  src={author.avatar}
                  alt={author.name}
                  fill
                  className="object-cover"
                />
              </div>

              <div>
                <span className="inline-block bg-[#DE8017] text-white text-[11px] font-extrabold uppercase tracking-wider px-3 py-1 rounded-full mb-2">
                  Verified Author
                </span>
                <h1 className="text-3xl sm:text-4xl font-extrabold text-[#0B192C] mb-1">
                  {author.name}
                </h1>
                <p className="text-sm font-semibold text-[#DE8017] mb-3">{author.role}</p>
                <p className="text-slate-600 text-sm leading-relaxed max-w-2xl">
                  {author.bio}
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* Author Articles */}
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-12">
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-10">
            <div className="lg:col-span-8">
              <div className="flex items-center justify-between mb-8 pb-4 border-b border-slate-200">
                <h2 className="text-xl font-extrabold text-[#0B192C]">
                  Articles Authored by {author.name} ({posts.length})
                </h2>
              </div>

              {posts.length > 0 ? (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                  {posts.map((post) => (
                    <ArticleCard key={post.slug} post={post} />
                  ))}
                </div>
              ) : (
                <div className="bg-white p-12 rounded-3xl text-center border border-slate-200 shadow-sm">
                  <p className="text-slate-600 text-base">No articles written by this author yet.</p>
                </div>
              )}
            </div>

            <div className="lg:col-span-4">
              <BlogSidebar
                categories={categories}
                popularPosts={popularPosts}
                latestPosts={latestPosts}
              />
            </div>
          </div>
        </div>
      </main>
    </>
  );
}

import Link from 'next/link';
import Image from 'next/image';
import { BlogPost } from '@/lib/blog-types';

interface FeaturedArticleCardProps {
  post: BlogPost;
}

export default function FeaturedArticleCard({ post }: FeaturedArticleCardProps) {
  return (
    <article className="bg-white rounded-3xl overflow-hidden border border-slate-200/90 shadow-lg blog-card-hover grid grid-cols-1 lg:grid-cols-12 mb-12">
      {/* Thumbnail Container (Lg: 7 cols) */}
      <div className="relative lg:col-span-7 min-h-[320px] lg:min-h-[420px] bg-slate-100 overflow-hidden group">
        <Link href={`/blog/${post.slug}`} className="block w-full h-full">
          <Image
            src={post.coverImage}
            alt={post.title}
            fill
            priority
            sizes="(max-width: 1024px) 100vw, 60vw"
            className="object-cover transition-transform duration-700 group-hover:scale-105"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-black/60 via-black/20 to-transparent lg:hidden" />
        </Link>
        
        {/* Floating Featured Pill */}
        <div className="absolute top-6 left-6 flex items-center space-x-2">
          <span className="bg-[#DE8017] text-white text-xs font-bold uppercase tracking-wider px-3.5 py-1.5 rounded-full shadow-md">
            Featured Post
          </span>
          <Link
            href={`/blog/category/${post.category}`}
            className="bg-white/90 backdrop-blur-md text-[#0B192C] text-xs font-semibold px-3.5 py-1.5 rounded-full shadow-sm hover:bg-white transition-colors"
          >
            {post.categoryName || post.category}
          </Link>
        </div>
      </div>

      {/* Content Container (Lg: 5 cols) */}
      <div className="lg:col-span-5 p-8 lg:p-10 flex flex-col justify-between bg-white">
        <div>
          {/* Metadata */}
          <div className="flex items-center text-xs text-slate-500 space-x-3 mb-4 font-medium">
            <span>{post.publishedDate}</span>
            <span>•</span>
            <span>{post.readingTime}</span>
          </div>

          {/* Heading */}
          <h2 className="text-2xl lg:text-3xl font-extrabold text-[#0B192C] hover:text-[#DE8017] transition-colors leading-tight mb-4">
            <Link href={`/blog/${post.slug}`}>
              {post.title}
            </Link>
          </h2>

          {/* Excerpt */}
          <p className="text-slate-600 text-base leading-relaxed line-clamp-4 mb-6">
            {post.excerpt}
          </p>
        </div>

        <div>
          {/* Author info & CTA */}
          <div className="pt-6 border-t border-slate-100 flex items-center justify-between">
            {post.author && (
              <Link href={`/blog/author/${post.author.id}`} className="flex items-center space-x-3 group/author">
                <div className="relative w-10 h-10 rounded-full overflow-hidden border-2 border-[#DE8017]/30">
                  <Image
                    src={post.author.avatar}
                    alt={post.author.name}
                    fill
                    className="object-cover"
                  />
                </div>
                <div>
                  <span className="block text-sm font-bold text-[#0B192C] group-hover/author:text-[#DE8017] transition-colors">
                    {post.author.name}
                  </span>
                  <span className="block text-xs text-slate-500 line-clamp-1">{post.author.role}</span>
                </div>
              </Link>
            )}

            <Link
              href={`/blog/${post.slug}`}
              className="bg-[#0B192C] text-white hover:bg-[#DE8017] px-5 py-2.5 rounded-xl text-xs font-semibold transition-all duration-300 shadow-md inline-flex items-center space-x-2"
            >
              <span>Continue Reading</span>
              <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M14 5l7 7m0 0l-7 7m7-7H3" />
              </svg>
            </Link>
          </div>
        </div>
      </div>
    </article>
  );
}

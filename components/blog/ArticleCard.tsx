import Link from 'next/link';
import Image from 'next/image';
import { BlogPost } from '@/lib/blog-types';

interface ArticleCardProps {
  post: BlogPost;
  priority?: boolean;
}

export default function ArticleCard({ post, priority = false }: ArticleCardProps) {
  return (
    <article className="group bg-white rounded-2xl overflow-hidden border border-slate-200/80 shadow-sm blog-card-hover flex flex-col h-full">
      {/* Thumbnail */}
      <div className="relative aspect-[16/9] w-full overflow-hidden bg-slate-100">
        <Link href={`/blog/${post.slug}`} className="block w-full h-full">
          <Image
            src={post.coverImage}
            alt={post.title}
            fill
            sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
            priority={priority}
            className="object-cover transition-transform duration-500 group-hover:scale-105"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-black/40 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
        </Link>
        <Link
          href={`/blog/category/${post.category}`}
          className="absolute top-4 left-4 bg-[#DE8017] text-white text-xs font-semibold px-3 py-1.5 rounded-full shadow-md hover:bg-[#c97112] transition-colors"
        >
          {post.categoryName || post.category}
        </Link>
      </div>

      {/* Card Content */}
      <div className="p-6 flex flex-col flex-grow">
        {/* Meta Info */}
        <div className="flex items-center text-xs text-slate-500 space-x-3 mb-3">
          <span>{post.publishedDate}</span>
          <span>•</span>
          <span>{post.readingTime}</span>
        </div>

        {/* Title */}
        <h3 className="text-xl font-bold text-[#0B192C] group-hover:text-[#DE8017] transition-colors line-clamp-2 mb-3 leading-snug">
          <Link href={`/blog/${post.slug}`}>
            {post.title}
          </Link>
        </h3>

        {/* Excerpt */}
        <p className="text-slate-600 text-sm line-clamp-3 mb-6 flex-grow leading-relaxed">
          {post.excerpt}
        </p>

        {/* Card Footer / Author */}
        <div className="pt-4 border-t border-slate-100 flex items-center justify-between mt-auto">
          {post.author ? (
            <Link href={`/blog/author/${post.author.id}`} className="flex items-center space-x-2.5 group/author">
              <div className="relative w-8 h-8 rounded-full overflow-hidden border border-slate-200">
                <Image
                  src={post.author.avatar}
                  alt={post.author.name}
                  fill
                  className="object-cover"
                />
              </div>
              <span className="text-xs font-medium text-slate-700 group-hover/author:text-[#DE8017] transition-colors">
                {post.author.name}
              </span>
            </Link>
          ) : (
            <span className="text-xs text-slate-500">Atlas Mentor Team</span>
          )}

          <Link
            href={`/blog/${post.slug}`}
            className="inline-flex items-center text-xs font-semibold text-[#DE8017] group-hover:translate-x-1 transition-transform"
          >
            Read Article
            <svg className="w-3.5 h-3.5 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M14 5l7 7m0 0l-7 7m7-7H3" />
            </svg>
          </Link>
        </div>
      </div>
    </article>
  );
}

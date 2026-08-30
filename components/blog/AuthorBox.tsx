import Link from 'next/link';
import Image from 'next/image';
import { BlogAuthor } from '@/lib/blog-types';

interface AuthorBoxProps {
  author: BlogAuthor;
}

export default function AuthorBox({ author }: AuthorBoxProps) {
  return (
    <div className="bg-gradient-to-r from-slate-50 to-white p-6 sm:p-8 rounded-2xl border border-slate-200/90 my-10 flex flex-col sm:flex-row items-start sm:items-center gap-6 shadow-sm">
      {/* Avatar */}
      <div className="relative w-20 h-20 sm:w-24 sm:h-24 rounded-full overflow-hidden border-4 border-white shadow-md flex-shrink-0">
        <Image
          src={author.avatar}
          alt={author.name}
          fill
          sizes="96px"
          className="object-cover"
        />
      </div>

      {/* Content */}
      <div className="flex-grow">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-2">
          <div>
            <h4 className="text-lg font-extrabold text-[#0B192C]">
              <Link href={`/blog/author/${author.id}`} className="hover:text-[#DE8017] transition-colors">
                {author.name}
              </Link>
            </h4>
            <span className="text-xs font-semibold text-[#DE8017]">{author.role}</span>
          </div>

          <Link
            href={`/blog/author/${author.id}`}
            className="inline-flex items-center text-xs font-bold text-[#0B192C] hover:text-[#DE8017] transition-colors"
          >
            View All Articles
            <svg className="w-3.5 h-3.5 ml-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
            </svg>
          </Link>
        </div>

        <p className="text-slate-600 text-xs sm:text-sm leading-relaxed mb-4">
          {author.bio}
        </p>

        {/* Social Links */}
        {author.socials && (
          <div className="flex items-center space-x-3 text-slate-500">
            {author.socials.linkedin && (
              <a
                href={author.socials.linkedin}
                target="_blank"
                rel="noopener noreferrer"
                className="hover:text-[#DE8017] transition-colors text-xs font-medium flex items-center space-x-1"
              >
                <span>LinkedIn</span>
              </a>
            )}
            {author.socials.instagram && (
              <a
                href={author.socials.instagram}
                target="_blank"
                rel="noopener noreferrer"
                className="hover:text-[#DE8017] transition-colors text-xs font-medium flex items-center space-x-1"
              >
                <span>Instagram</span>
              </a>
            )}
            {author.socials.website && (
              <a
                href={author.socials.website}
                target="_blank"
                rel="noopener noreferrer"
                className="hover:text-[#DE8017] transition-colors text-xs font-medium flex items-center space-x-1"
              >
                <span>Website</span>
              </a>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

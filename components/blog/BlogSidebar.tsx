'use client';

import { useState } from 'react';
import Link from 'next/link';
import Image from 'next/image';
import { useRouter } from 'next/navigation';
import { BlogCategory, BlogPost } from '@/lib/blog-types';

interface BlogSidebarProps {
  categories: BlogCategory[];
  popularPosts: BlogPost[];
  currentCategory?: string;
}

export default function BlogSidebar({
  categories,
  popularPosts,
  currentCategory,
}: BlogSidebarProps) {
  const router = useRouter();
  const [searchQuery, setSearchQuery] = useState('');
  const [subscribed, setSubscribed] = useState(false);
  const [email, setEmail] = useState('');

  const handleSearchSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (searchQuery.trim()) {
      router.push(`/blog/search?q=${encodeURIComponent(searchQuery.trim())}`);
    }
  };

  const handleNewsletterSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (email) {
      setSubscribed(true);
      setEmail('');
    }
  };

  return (
    <aside className="space-y-8 blog-sticky-toc">
      {/* 1. Search Box Widget */}
      <div className="bg-white p-6 rounded-2xl border border-slate-200/90 shadow-sm">
        <h3 className="text-lg font-bold text-[#0B192C] mb-4 relative pb-2 after:content-[''] after:absolute after:bottom-0 after:left-0 after:w-10 after:h-0.5 after:bg-[#DE8017]">
          Search Articles
        </h3>
        <form onSubmit={handleSearchSubmit} className="relative">
          <input
            type="text"
            placeholder="Search keywords, countries, topics..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full pl-4 pr-11 py-3 text-sm bg-slate-50 border border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-[#DE8017]/50 focus:border-[#DE8017] transition-all"
          />
          <button
            type="submit"
            className="absolute right-2 top-1/2 -translate-y-1/2 p-2 text-slate-400 hover:text-[#DE8017] transition-colors"
            aria-label="Search"
          >
            <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
            </svg>
          </button>
        </form>
      </div>

      {/* 2. Free Study Abroad Counselling CTA Box */}
      <div className="bg-gradient-to-br from-[#0B192C] to-[#1E3A8A] p-6 rounded-2xl text-white shadow-lg relative overflow-hidden">
        <div className="absolute -right-10 -bottom-10 w-32 h-32 bg-[#DE8017]/20 rounded-full blur-2xl pointer-events-none" />
        <span className="inline-block bg-[#DE8017] text-white text-[10px] font-extrabold uppercase tracking-wider px-2.5 py-1 rounded-md mb-3">
          Free Consultation
        </span>
        <h4 className="text-xl font-bold mb-2">Need Guidance for MBBS Abroad?</h4>
        <p className="text-slate-300 text-xs leading-relaxed mb-5">
          Get direct admission guidance from Dr. Jitesh Kumar & senior medical advisors. 100% NMC gazette compliant universities.
        </p>
        <a
          href="https://atlasmentor.com/#contact-us"
          className="block w-full text-center bg-[#DE8017] hover:bg-[#c97112] text-white text-xs font-bold py-3 rounded-xl shadow-md transition-all duration-300 transform hover:-translate-y-0.5"
        >
          Book Free Counselling Now
        </a>
      </div>

      {/* 3. Categories Widget */}
      <div className="bg-white p-6 rounded-2xl border border-slate-200/90 shadow-sm">
        <h3 className="text-lg font-bold text-[#0B192C] mb-4 relative pb-2 after:content-[''] after:absolute after:bottom-0 after:left-0 after:w-10 after:h-0.5 after:bg-[#DE8017]">
          Categories
        </h3>
        <ul className="space-y-2">
          {categories.map((cat) => {
            const isActive = currentCategory === cat.slug;
            return (
              <li key={cat.slug}>
                <Link
                  href={`/blog/category/${cat.slug}`}
                  className={`flex items-center justify-between px-3.5 py-2.5 rounded-xl text-sm font-medium transition-all ${
                    isActive
                      ? 'bg-[#DE8017] text-white shadow-sm'
                      : 'text-slate-700 hover:bg-slate-50 hover:text-[#DE8017]'
                  }`}
                >
                  <span>{cat.name}</span>
                  <span
                    className={`text-xs px-2 py-0.5 rounded-full ${
                      isActive ? 'bg-white/20 text-white' : 'bg-slate-100 text-slate-500'
                    }`}
                  >
                    {cat.count || 0}
                  </span>
                </Link>
              </li>
            );
          })}
        </ul>
      </div>

      {/* 4. Popular Posts Widget */}
      <div className="bg-white p-6 rounded-2xl border border-slate-200/90 shadow-sm">
        <h3 className="text-lg font-bold text-[#0B192C] mb-4 relative pb-2 after:content-[''] after:absolute after:bottom-0 after:left-0 after:w-10 after:h-0.5 after:bg-[#DE8017]">
          Popular Articles
        </h3>
        <div className="space-y-4">
          {popularPosts.slice(0, 4).map((post) => (
            <article key={post.slug} className="flex items-center space-x-3 group">
              <div className="relative w-16 h-16 rounded-xl overflow-hidden bg-slate-100 flex-shrink-0">
                <Image
                  src={post.coverImage}
                  alt={post.imageAlt || post.title}
                  fill
                  sizes="64px"
                  className="object-cover group-hover:scale-105 transition-transform duration-300"
                />
              </div>
              <div className="flex-grow min-w-0">
                <span className="text-[11px] text-slate-400 font-medium">{post.publishedDate}</span>
                <h4 className="text-xs font-bold text-[#0B192C] group-hover:text-[#DE8017] transition-colors line-clamp-2 leading-snug">
                  <Link href={`/blog/${post.slug}`}>{post.title}</Link>
                </h4>
              </div>
            </article>
          ))}
        </div>
      </div>

      {/* 5. Newsletter Subscription Widget */}
      <div className="bg-slate-900 text-white p-6 rounded-2xl shadow-sm">
        <h4 className="text-base font-bold mb-2">Subscribe for Admission Updates</h4>
        <p className="text-xs text-slate-400 mb-4 leading-relaxed">
          Get weekly NMC gazette updates, university fee structure changes, and scholarship alerts delivered to your inbox.
        </p>

        {subscribed ? (
          <div className="bg-emerald-900/50 border border-emerald-700 text-emerald-300 text-xs p-3 rounded-xl font-medium text-center">
            ✓ Thank you! You have been subscribed successfully.
          </div>
        ) : (
          <form onSubmit={handleNewsletterSubmit} className="space-y-2.5">
            <input
              type="email"
              required
              placeholder="Enter your email address"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full px-3.5 py-2.5 text-xs bg-slate-800 border border-slate-700 rounded-xl text-white placeholder-slate-400 focus:outline-none focus:ring-1 focus:ring-[#DE8017]"
            />
            <button
              type="submit"
              className="w-full bg-[#DE8017] hover:bg-[#c97112] text-white text-xs font-bold py-2.5 rounded-xl transition-colors shadow-sm"
            >
              Subscribe Now
            </button>
          </form>
        )}
      </div>
    </aside>
  );
}

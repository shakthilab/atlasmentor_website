'use client';

import { useState } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { BlogCategory } from '@/lib/blog-types';

interface BlogHeroProps {
  categories: BlogCategory[];
  activeCategory?: string;
}

export default function BlogHero({ categories, activeCategory = 'all' }: BlogHeroProps) {
  const router = useRouter();
  const [searchQuery, setSearchQuery] = useState('');

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    if (searchQuery.trim()) {
      router.push(`/blog/search?q=${encodeURIComponent(searchQuery.trim())}`);
    }
  };

  return (
    <section className="relative overflow-hidden bg-gradient-to-b from-[#0B192C] via-[#0f243f] to-[#0B192C] text-white pt-36 sm:pt-40 pb-16 sm:pb-20 px-4 sm:px-6 lg:px-8">
      {/* Decorative Glow Shapes */}
      <div className="absolute top-0 left-1/2 -translate-x-1/2 w-full max-w-7xl h-full pointer-events-none overflow-hidden">
        <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-[#DE8017]/15 rounded-full blur-3xl animate-pulse" />
        <div className="absolute top-1/3 right-1/4 w-80 h-80 bg-blue-500/10 rounded-full blur-3xl" />
      </div>

      <div className="relative max-w-5xl mx-auto text-center z-10">
        {/* Badge */}
        <div className="inline-flex items-center space-x-2 bg-white/10 backdrop-blur-md border border-white/15 px-4 py-1.5 rounded-full mb-6">
          <span className="w-2 h-2 rounded-full bg-[#DE8017] animate-ping" />
          <span className="text-xs font-semibold uppercase tracking-wider text-slate-200">
            Atlas Mentor Knowledge Hub
          </span>
        </div>

        {/* Main Heading */}
        <h1 className="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-white tracking-tight mb-4 leading-tight">
          Study Abroad & <span className="text-[#DE8017]">MBBS Abroad</span> Blog
        </h1>

        {/* Subtitle */}
        <p className="text-slate-300 text-base sm:text-lg max-w-3xl mx-auto leading-relaxed mb-8">
          Latest updates, admission guides, university comparisons, scholarships, visa information, student success stories, and expert advice for Indian medical aspirants.
        </p>

        {/* Hero Search Bar */}
        <form onSubmit={handleSearch} className="max-w-2xl mx-auto mb-10 relative">
          <div className="relative flex items-center">
            <input
              type="text"
              placeholder="Search for 'Georgia MBBS', 'NMC Rules', 'Russia Tuition Fees'..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full pl-6 pr-32 py-4 bg-white/95 backdrop-blur-md text-slate-900 rounded-2xl border border-white/20 shadow-2xl focus:outline-none focus:ring-4 focus:ring-[#DE8017]/30 text-sm sm:text-base placeholder-slate-400"
            />
            <button
              type="submit"
              className="absolute right-2 bg-[#DE8017] hover:bg-[#c97112] text-white px-6 py-2.5 rounded-xl font-bold text-sm shadow-md transition-all duration-300 flex items-center space-x-2"
            >
              <span>Search</span>
              <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
              </svg>
            </button>
          </div>
        </form>

        {/* Category Pills Slider */}
        <div className="flex items-center justify-center flex-wrap gap-2 sm:gap-2.5 max-w-4xl mx-auto">
          <Link
            href="/blog"
            className={`px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold transition-all duration-200 ${
              activeCategory === 'all'
                ? 'bg-[#DE8017] text-white shadow-lg scale-105'
                : 'bg-white/10 hover:bg-white/20 text-slate-200 border border-white/10'
            }`}
          >
            All Categories
          </Link>
          {categories.map((cat) => (
            <Link
              key={cat.slug}
              href={`/blog/category/${cat.slug}`}
              className={`px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold transition-all duration-200 ${
                activeCategory === cat.slug
                  ? 'bg-[#DE8017] text-white shadow-lg scale-105'
                  : 'bg-white/10 hover:bg-white/20 text-slate-200 border border-white/10'
              }`}
            >
              {cat.name}
            </Link>
          ))}
        </div>
      </div>
    </section>
  );
}

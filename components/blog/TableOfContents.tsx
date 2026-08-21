'use client';

import { useEffect, useState } from 'react';

interface HeadItem {
  id: string;
  text: string;
  level: number;
}

interface TableOfContentsProps {
  contentHtml: string;
}

export default function TableOfContents({ contentHtml }: TableOfContentsProps) {
  const [headings, setHeadings] = useState<HeadItem[]>([]);
  const [activeId, setActiveId] = useState<string>('');

  useEffect(() => {
    // Parse H2 and H3 headings from HTML content
    const parser = new DOMParser();
    const doc = parser.parseFromString(contentHtml, 'text/html');
    const headingElements = doc.querySelectorAll('h2, h3');
    
    const items: HeadItem[] = [];
    headingElements.forEach((el, index) => {
      const text = el.textContent || '';
      const id = text.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '') || `heading-${index}`;
      const level = el.tagName.toLowerCase() === 'h2' ? 2 : 3;
      items.push({ id, text, level });
    });

    setHeadings(items);

    // Give actual DOM elements matching IDs for scroll target
    const articleContainer = document.querySelector('.blog-prose');
    if (articleContainer) {
      const domHeadings = articleContainer.querySelectorAll('h2, h3');
      domHeadings.forEach((el, index) => {
        const text = el.textContent || '';
        const id = text.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '') || `heading-${index}`;
        el.setAttribute('id', id);
      });
    }

    // Scroll Observer for active heading highlight
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            setActiveId(entry.target.id);
          }
        });
      },
      { rootMargin: '-80px 0px -60% 0px' }
    );

    if (articleContainer) {
      const domHeadings = articleContainer.querySelectorAll('h2, h3');
      domHeadings.forEach((h) => observer.observe(h));
    }

    return () => observer.disconnect();
  }, [contentHtml]);

  if (headings.length === 0) return null;

  return (
    <div className="bg-white p-5 rounded-2xl border border-slate-200/90 shadow-sm blog-sticky-toc hidden lg:block">
      <h4 className="text-xs font-bold uppercase tracking-wider text-slate-400 mb-3 flex items-center space-x-2">
        <svg className="w-4 h-4 text-[#DE8017]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h7" />
        </svg>
        <span>Table of Contents</span>
      </h4>

      <nav className="space-y-1 text-xs">
        {headings.map((item) => {
          const isActive = activeId === item.id;
          return (
            <a
              key={item.id}
              href={`#${item.id}`}
              onClick={(e) => {
                e.preventDefault();
                const el = document.getElementById(item.id);
                if (el) {
                  const y = el.getBoundingClientRect().top + window.scrollY - 90;
                  window.scrollTo({ top: y, behavior: 'smooth' });
                  setActiveId(item.id);
                }
              }}
              className={`block py-1.5 transition-colors line-clamp-1 ${
                item.level === 3 ? 'pl-4 text-[11px]' : 'font-medium'
              } ${
                isActive
                  ? 'text-[#DE8017] font-bold border-l-2 border-[#DE8017] -ml-[21px] pl-[19px]'
                  : 'text-slate-600 hover:text-[#0B192C]'
              }`}
            >
              {item.text}
            </a>
          );
        })}
      </nav>
    </div>
  );
}

'use client';

import React, { useEffect, useRef, useTransition } from 'react';
import { useRouter, usePathname } from 'next/navigation';

function replaceOverlayStyle(el: HTMLDivElement | null, style: Record<string, string>) {
  if (!el) return;
  el.style.cssText = '';
  for (const [key, value] of Object.entries(style)) {
    (el.style as unknown as Record<string, string>)[key] = value;
  }
}

function mergeOverlayStyle(el: HTMLDivElement | null, style: Record<string, string>) {
  if (!el) return;
  for (const [key, value] of Object.entries(style)) {
    (el.style as unknown as Record<string, string>)[key] = value;
  }
}

export default function HeroTransition({ children }: { children: React.ReactNode }) {
  const router = useRouter();
  const pathname = usePathname();

  const [, startTransition] = useTransition();
  const overlayRef = useRef<HTMLDivElement>(null);
  const containerRef = useRef<HTMLDivElement>(null);

  // Listen to path changes to trigger the fade-in phase
  useEffect(() => {
    // Disable native scroll restoration so reloads always start at top
    if ('scrollRestoration' in history) {
      history.scrollRestoration = 'manual';
    }

    // Force scroll to top on path change (unless there is a hash)
    if (!window.location.hash) {
      window.scrollTo(0, 0);
      setTimeout(() => window.scrollTo(0, 0), 10);
      setTimeout(() => window.scrollTo(0, 0), 100);
    }

    const newHero = document.querySelector('main section.elementor-top-section') ||
      document.querySelector('.page-content section.elementor-top-section') ||
      document.querySelector('main section');

    if (newHero) {
      const rect = newHero.getBoundingClientRect();
      newHero.classList.remove('hero-transitioning-out', 'hero-transitioning-in', 'hero-transition-done');

      newHero.classList.add('hero-transitioning-in');

      replaceOverlayStyle(overlayRef.current, {
        position: 'absolute',
        top: '0',
        left: '0',
        width: '100%',
        height: `${rect.height}px`,
        backgroundColor: '#ffffff',
        opacity: '1',
        pointerEvents: 'none',
        zIndex: '99',
        display: 'block',
        willChange: 'opacity',
        transform: 'translate3d(0, 0, 0)',
      });

      requestAnimationFrame(() => {
        requestAnimationFrame(() => {
          mergeOverlayStyle(overlayRef.current, {
            opacity: '0',
            transition: 'opacity 450ms ease-in-out',
          });

          newHero.classList.remove('hero-transitioning-in');
          newHero.classList.add('hero-transition-done');
        });
      });

      const timer = setTimeout(() => {
        replaceOverlayStyle(overlayRef.current, {
          opacity: '0',
          display: 'none',
        });
        newHero.classList.remove('hero-transition-done');
      }, 450);

      return () => clearTimeout(timer);
    } else {
      replaceOverlayStyle(overlayRef.current, {
        opacity: '0',
        display: 'none',
      });
    }
  }, [pathname]);

  // Intercept click events on links
  useEffect(() => {
    const handleLinkClick = (e: MouseEvent) => {
      const target = e.target as HTMLElement;
      const anchor = target.closest('a');

      if (!anchor) return;

      const href = anchor.getAttribute('href');
      if (!href) return;

      if (
        anchor.classList.contains('ekit-accordion--toggler') ||
        anchor.hasAttribute('data-ekit-toggle') ||
        anchor.hasAttribute('data-toggle') ||
        anchor.getAttribute('role') === 'tab'
      ) {
        return;
      }

      if (href.startsWith('/') && !href.startsWith('/#') && !href.includes(':')) {
        const destPathname = href.split('?')[0].split('#')[0];
        if (destPathname === pathname) {
          return;
        }

        e.preventDefault();

        if (document.activeElement instanceof HTMLElement) {
          document.activeElement.blur();
        }

        const dropdowns = document.querySelectorAll('.elementor-nav-menu--dropdown, .sub-menu');
        dropdowns.forEach((el) => {
          const htmlEl = el as HTMLElement;
          htmlEl.style.display = 'none';
          setTimeout(() => {
            htmlEl.style.display = '';
          }, 600);
        });

        const currentHero = document.querySelector('main section.elementor-top-section') ||
          document.querySelector('.page-content section.elementor-top-section') ||
          document.querySelector('main section');

        if (currentHero) {
          const rect = currentHero.getBoundingClientRect();

          currentHero.classList.add('hero-transitioning-out');

          replaceOverlayStyle(overlayRef.current, {
            position: 'absolute',
            top: '0',
            left: '0',
            width: '100%',
            height: `${rect.height}px`,
            backgroundColor: '#ffffff',
            opacity: '0',
            pointerEvents: 'none',
            zIndex: '99',
            display: 'block',
            willChange: 'opacity',
            transform: 'translate3d(0, 0, 0)',
          });

          requestAnimationFrame(() => {
            requestAnimationFrame(() => {
              mergeOverlayStyle(overlayRef.current, {
                opacity: '1',
                transition: 'opacity 250ms ease-in-out',
              });
            });
          });

          setTimeout(() => {
            window.scrollTo(0, 0);
            startTransition(() => {
              router.push(href);
            });
          }, 250);
        } else {
          window.scrollTo(0, 0);
          router.push(href);
        }
      }
    };

    document.addEventListener('click', handleLinkClick);
    return () => {
      document.removeEventListener('click', handleLinkClick);
    };
  }, [router, pathname]);

  return (
    <div ref={containerRef} style={{ position: 'relative', width: '100%' }}>
      <div ref={overlayRef} style={{ opacity: 0, display: 'none' }} />
      {children}
    </div>
  );
}

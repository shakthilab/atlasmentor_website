'use client';

import React, { useEffect, useRef, useState, useTransition } from 'react';
import { useRouter, usePathname } from 'next/navigation';

// Overlay styling is applied by mutating the DOM node directly (via refs) rather than
// through React state, so route-change animations don't trigger extra render cascades.
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

  // Track client-side mount so the server and client render the same
  // initial HTML (children only, no wrapper div) — prevents hydration mismatch.
  const [mounted, setMounted] = useState(false);
  useEffect(() => { setMounted(true); }, []);

  // Listen to path changes to trigger the fade-in phase
  useEffect(() => {
    // Disable native scroll restoration so reloads always start at top
    if ('scrollRestoration' in history) {
      history.scrollRestoration = 'manual';
    }

    // Force scroll to top on path change (unless there is a hash)
    if (!window.location.hash) {
      window.scrollTo(0, 0);
      // Double check after a short delay to ensure React has painted
      setTimeout(() => window.scrollTo(0, 0), 10);
      setTimeout(() => window.scrollTo(0, 0), 100);
    }

    // When the path changes, find the new hero element
    const newHero = document.querySelector('main section.elementor-top-section') ||
      document.querySelector('.page-content section.elementor-top-section') ||
      document.querySelector('main section');

    if (newHero) {
      const rect = newHero.getBoundingClientRect();

      // Clean up any recycled/stale transition classes from the DOM element
      newHero.classList.remove('hero-transitioning-out', 'hero-transitioning-in', 'hero-transition-done');

      // Phase 2: Fade out the overlay and fade in the new hero
      // Make sure the new hero starts invisible so it doesn't flash before the overlay fades out
      newHero.classList.add('hero-transitioning-in');

      // Position the overlay on top of the new hero
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

      // Delay slightly to ensure DOM has updated and classes are applied
      requestAnimationFrame(() => {
        requestAnimationFrame(() => {
          // Add transition styles to fade out overlay and fade in new hero
          mergeOverlayStyle(overlayRef.current, {
            opacity: '0',
            transition: 'opacity 450ms ease-in-out',
          });

          newHero.classList.remove('hero-transitioning-in');
          newHero.classList.add('hero-transition-done');
        });
      });

      // Clean up classes after transition finishes
      const timer = setTimeout(() => {
        replaceOverlayStyle(overlayRef.current, {
          opacity: '0',
          display: 'none',
        });
        newHero.classList.remove('hero-transition-done');
      }, 450);

      return () => clearTimeout(timer);
    } else {
      // Fallback if no hero element is found on the new page
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

      // Ignore accordion/tab togglers which might have relative hrefs used as data targets
      if (
        anchor.classList.contains('ekit-accordion--toggler') ||
        anchor.hasAttribute('data-ekit-toggle') ||
        anchor.hasAttribute('data-toggle') ||
        anchor.getAttribute('role') === 'tab'
      ) {
        return;
      }

      // Intercept local links only (starts with '/', not external, not mailto/tel/whatsapp/etc., and not hash anchors)
      if (href.startsWith('/') && !href.startsWith('/#') && !href.includes(':')) {
        // Extract destination pathname to see if we are navigating to the same page
        const destPathname = href.split('?')[0].split('#')[0];
        if (destPathname === pathname) {
          // Allow default behavior (e.g. scroll to anchor/top) without page transition overlay
          return;
        }

        e.preventDefault();

        // Remove focus from the clicked link so that CSS :focus-within dropdowns close immediately
        if (document.activeElement instanceof HTMLElement) {
          document.activeElement.blur();
        }

        // Force dropdowns to close immediately by temporarily hiding them
        const dropdowns = document.querySelectorAll('.elementor-nav-menu--dropdown, .sub-menu');
        dropdowns.forEach((el) => {
          const htmlEl = el as HTMLElement;
          htmlEl.style.display = 'none';
          // Restore display after transition so it can be opened again later
          setTimeout(() => {
            htmlEl.style.display = '';
          }, 600);
        });

        // Find current hero
        const currentHero = document.querySelector('main section.elementor-top-section') ||
          document.querySelector('.page-content section.elementor-top-section') ||
          document.querySelector('main section');

        if (currentHero) {
          const rect = currentHero.getBoundingClientRect();

          // Phase 1: Fade out old hero and fade in white overlay
          currentHero.classList.add('hero-transitioning-out');

          // Position and show overlay at opacity 0
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

          // Animate overlay to opacity 1 over 250ms
          requestAnimationFrame(() => {
            requestAnimationFrame(() => {
              mergeOverlayStyle(overlayRef.current, {
                opacity: '1',
                transition: 'opacity 250ms ease-in-out',
              });
            });
          });

          // After 250ms (end of fade-out phase), trigger route navigation
          setTimeout(() => {
            window.scrollTo(0, 0);
            startTransition(() => {
              router.push(href);
            });
          }, 250);
        } else {
          // If no hero element, perform normal fast navigation
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

  // Before client mount, render children without the wrapper so SSR and
  // the initial client render produce identical HTML.
  if (!mounted) {
    return <>{children}</>;
  }

  return (
    <div ref={containerRef} style={{ position: 'relative', width: '100%' }}>
      <div ref={overlayRef} style={{ opacity: 0, display: 'none' }} />
      {children}
    </div>
  );
}

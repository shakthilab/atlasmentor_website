'use client';

import { useEffect, useRef } from 'react';
import { usePathname } from 'next/navigation';

interface CarouselSettings {
  space_between?: { size?: number };
  loop?: string;
  speed?: number;
  autoplay?: string | number;
  autoplay_speed?: number;
  pause_on_hover?: string;
}

interface SwiperConstructor {
  new (el: Element, options: Record<string, unknown>): unknown;
}

export default function ElementorInteractions() {
  const pathname = usePathname();
  const swiperTimerRef = useRef<NodeJS.Timeout | null>(null);

  useEffect(() => {
    let swiperRetryCount = 0;
    const MAX_SWIPER_RETRIES = 10;

    // 1. Accordion click delegation handler
    const handleAccordionToggle = (e: MouseEvent) => {
      const toggler = (e.target as HTMLElement).closest('.ekit-accordion--toggler');
      if (toggler) {
        e.preventDefault();
        
        let targetSelector = toggler.getAttribute('data-target') || toggler.getAttribute('href');
        if (!targetSelector) return;
        
        if (targetSelector.includes('#')) {
          targetSelector = '#' + targetSelector.split('#')[1];
        }
        
        const targetPanel = document.querySelector(targetSelector) as HTMLElement;
        if (targetPanel) {
          const isExpanded = targetPanel.classList.contains('show');
          if (isExpanded) {
            targetPanel.classList.remove('show');
            toggler.classList.add('collapsed');
            toggler.setAttribute('aria-expanded', 'false');
          } else {
            targetPanel.classList.add('show');
            toggler.classList.remove('collapsed');
            toggler.setAttribute('aria-expanded', 'true');
          }
        }
      }
    };

    // 2. Swiper carousels initialization helper (Conditional & Event-Driven)
    const initSwipers = () => {
      // FAST EXIT 1: If no uninitialized swiper containers exist on the page, exit in 0ms!
      const uninitializedSwipers = document.querySelectorAll(
        '.elementor-main-swiper.swiper:not([data-swiper-initialized="true"]), .swiper:not([data-swiper-initialized="true"])'
      );
      if (uninitializedSwipers.length === 0) return;

      const SwiperClass = (window as unknown as { Swiper?: SwiperConstructor }).Swiper;
      if (!SwiperClass) {
        if (swiperRetryCount < MAX_SWIPER_RETRIES) {
          swiperRetryCount++;
          if (swiperTimerRef.current) clearTimeout(swiperTimerRef.current);
          swiperTimerRef.current = setTimeout(initSwipers, 200);
        }
        return;
      }

      uninitializedSwipers.forEach((el) => {
        if ((el as Element & { swiper?: unknown }).swiper || el.classList.contains('swiper-initialized') || el.getAttribute('data-swiper-initialized') === 'true') {
          el.setAttribute('data-swiper-initialized', 'true');
          return;
        }

        el.setAttribute('data-swiper-initialized', 'true');

        const widgetEl = el.closest('.elementor-widget-testimonial-carousel');

        try {
          if (widgetEl) {
            let settings: CarouselSettings = {};
            try {
              settings = JSON.parse(widgetEl.getAttribute('data-settings') || '{}');
            } catch (e) {
              console.warn('Failed to parse testimonial carousel settings:', e);
            }

            new SwiperClass(el, {
              slidesPerView: 1,
              spaceBetween: settings.space_between?.size ?? 0,
              loop: settings.loop !== 'no',
              speed: settings.speed ?? 500,
              grabCursor: true,
              autoplay: settings.autoplay === 'no' ? false : {
                delay: settings.autoplay_speed ?? 5000,
                disableOnInteraction: false,
                pauseOnMouseEnter: settings.pause_on_hover !== 'no',
              },
            });
          } else {
            new SwiperClass(el, {
              slidesPerView: 1,
              spaceBetween: 10,
              loop: true,
              autoplay: {
                delay: 4000,
                disableOnInteraction: false,
              },
              breakpoints: {
                320: {
                  slidesPerView: 1,
                  spaceBetween: 10
                },
                768: {
                  slidesPerView: 2,
                  spaceBetween: 20
                },
                1024: {
                  slidesPerView: 3,
                  spaceBetween: 30
                }
              }
            });
          }
        } catch (err) {
          console.error('Error initializing Swiper on element:', el, err);
        }
      });
    };

    // 3. Viewport scroll animation trigger using IntersectionObserver
    const initViewportAnimations = () => {
      if (typeof window === 'undefined' || !('IntersectionObserver' in window)) {
        const animatedElements = document.querySelectorAll('.elementor-invisible');
        animatedElements.forEach((el) => {
          el.classList.remove('elementor-invisible');
        });
        return null;
      }

      const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1,
      };

      const handleIntersection = (entries: IntersectionObserverEntry[], obs: IntersectionObserver) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            const el = entry.target as HTMLElement;
            
            const settingsStr = el.getAttribute('data-settings');
            let animationName = '';
            let animationDelay = 0;

            if (settingsStr) {
              try {
                const settings = JSON.parse(settingsStr);
                animationName = settings._animation || settings.animation || '';
                animationDelay = settings._animation_delay || settings.animation_delay || 0;
              } catch (e) {
                console.warn('Failed to parse data-settings on element:', el, e);
              }
            }

            if (animationName && animationName !== 'none') {
              if (animationDelay > 0) {
                el.style.animationDelay = `${animationDelay}ms`;
                el.style.webkitAnimationDelay = `${animationDelay}ms`;
              }
              el.classList.add('animated', animationName);
              el.classList.remove('elementor-invisible');
            } else {
              el.classList.remove('elementor-invisible');
            }

            obs.unobserve(el);
          }
        });
      };

      const observer = new IntersectionObserver(handleIntersection, observerOptions);

      const observeElements = () => {
        const animatedElements = document.querySelectorAll('.elementor-invisible:not([data-observed])');
        animatedElements.forEach((el) => {
          el.setAttribute('data-observed', 'true');
          observer.observe(el);
        });
      };

      observeElements();

      return { observer, observeElements };
    };

    // 4. Force execution of Razorpay scripts inside elementor-shortcode (Conditional)
    const executeRazorpayScripts = () => {
      const shortcodeScripts = document.querySelectorAll('.elementor-shortcode script:not([data-executed="true"])');
      if (shortcodeScripts.length === 0) return;

      shortcodeScripts.forEach((scriptEl) => {
        const container = scriptEl.closest('.elementor-shortcode');
        if (!container) return;

        const existingButtons = container.querySelectorAll('.PaymentButton, .razorpay-embed-btn, a[href*="razorpay.com"]');
        if (existingButtons.length > 0) {
          if (existingButtons.length > 1) {
            for (let i = 1; i < existingButtons.length; i++) {
              existingButtons[i].remove();
            }
          }
          scriptEl.setAttribute('data-executed', 'true');
          return;
        }
        
        const parent = scriptEl.parentNode;
        if (!parent) return;
        
        scriptEl.setAttribute('data-executed', 'true');

        const newScript = document.createElement('script');
        for (let i = 0; i < scriptEl.attributes.length; i++) {
          const attr = scriptEl.attributes[i];
          newScript.setAttribute(attr.name, attr.value);
        }
        newScript.setAttribute('data-executed', 'true');
        newScript.innerHTML = scriptEl.innerHTML;
        parent.replaceChild(newScript, scriptEl);
      });
    };

    // 5. Share Buttons click delegation handler
    const handleShareClick = (e: MouseEvent) => {
      const shareBtn = (e.target as HTMLElement).closest('.elementor-share-btn');
      if (shareBtn) {
        e.preventDefault();
        
        const url = encodeURIComponent(window.location.href);
        const title = encodeURIComponent(document.title);
        let shareUrl = '';

        if (shareBtn.classList.contains('elementor-share-btn_facebook')) {
          shareUrl = `https://www.facebook.com/sharer/sharer.php?u=${url}`;
        } else if (shareBtn.classList.contains('elementor-share-btn_twitter')) {
          shareUrl = `https://twitter.com/intent/tweet?url=${url}&text=${title}`;
        } else if (shareBtn.classList.contains('elementor-share-btn_linkedin')) {
          shareUrl = `https://www.linkedin.com/shareArticle?mini=true&url=${url}&title=${title}`;
        } else if (shareBtn.classList.contains('elementor-share-btn_pinterest')) {
          shareUrl = `https://pinterest.com/pin/create/button/?url=${url}&description=${title}`;
        } else if (shareBtn.classList.contains('elementor-share-btn_email')) {
          shareUrl = `mailto:?subject=${title}&body=${url}`;
        } else if (shareBtn.classList.contains('elementor-share-btn_whatsapp')) {
          shareUrl = `https://api.whatsapp.com/send?text=${title} ${url}`;
        } else if (shareBtn.classList.contains('elementor-share-btn_telegram')) {
          shareUrl = `https://t.me/share/url?url=${url}&text=${title}`;
        } else if (shareBtn.classList.contains('elementor-share-btn_print')) {
          window.print();
          return;
        }

        if (shareUrl) {
          if (shareUrl.startsWith('mailto:')) {
            window.location.href = shareUrl;
          } else {
            window.open(shareUrl, '_blank', 'width=600,height=400');
          }
        }
      }
    };

    document.addEventListener('click', handleAccordionToggle);
    document.addEventListener('click', handleShareClick);
    
    const invisibleElements = document.querySelectorAll('.elementor-invisible');
    invisibleElements.forEach((el) => {
      el.removeAttribute('data-observed');
      el.classList.remove('animated');
      const settingsStr = el.getAttribute('data-settings');
      if (settingsStr) {
        try {
          const settings = JSON.parse(settingsStr);
          const animationName = settings._animation || settings.animation || '';
          if (animationName && animationName !== 'none') {
            el.classList.remove(animationName);
          }
        } catch {
          // ignore
        }
      }
    });

    const swiperContainers = document.querySelectorAll('.swiper');
    swiperContainers.forEach((el) => {
      el.removeAttribute('data-swiper-initialized');
      el.classList.remove('swiper-initialized');
    });

    initSwipers();
    const animObj = initViewportAnimations();
    executeRazorpayScripts();

    const mutationObserver = new MutationObserver((mutations) => {
      let hasRelevantChanges = false;
      let hasSwiperTarget = false;
      let hasAnimTarget = false;
      let hasScriptTarget = false;

      for (let i = 0; i < mutations.length; i++) {
        const mutation = mutations[i];
        if (mutation.type !== 'childList' || mutation.addedNodes.length === 0) continue;

        for (let j = 0; j < mutation.addedNodes.length; j++) {
          const node = mutation.addedNodes[j];
          if (node.nodeType !== 1) continue;
          const el = node as HTMLElement;

          if (el.querySelector) {
            if (el.classList.contains('swiper') || el.querySelector('.swiper')) {
              hasSwiperTarget = true;
              hasRelevantChanges = true;
            }
            if (el.classList.contains('elementor-invisible') || el.querySelector('.elementor-invisible:not([data-observed])')) {
              hasAnimTarget = true;
              hasRelevantChanges = true;
            }
            if (el.classList.contains('elementor-shortcode') || el.querySelector('.elementor-shortcode script:not([data-executed])')) {
              hasScriptTarget = true;
              hasRelevantChanges = true;
            }
          }
        }
      }

      if (!hasRelevantChanges) return;

      if (hasSwiperTarget) initSwipers();
      if (hasAnimTarget && animObj) animObj.observeElements();
      if (hasScriptTarget) executeRazorpayScripts();
    });

    const targetContainer = document.getElementById('page') || document.body;
    mutationObserver.observe(targetContainer, {
      childList: true,
      subtree: true,
    });

    return () => {
      if (swiperTimerRef.current) {
        clearTimeout(swiperTimerRef.current);
        swiperTimerRef.current = null;
      }
      document.removeEventListener('click', handleAccordionToggle);
      document.removeEventListener('click', handleShareClick);
      if (animObj && animObj.observer) {
        animObj.observer.disconnect();
      }
      mutationObserver.disconnect();
    };
  }, [pathname]);

  return null;
}

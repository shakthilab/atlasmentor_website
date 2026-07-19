'use client';

import React, { useState, useEffect } from 'react';
import { usePathname } from 'next/navigation';

interface PopupProps {
  html: string;
}

export default function Popup({ html }: PopupProps) {
  const [isOpen, setIsOpen] = useState(false);
  const pathname = usePathname();

  // Lock background scrolling when the popup is open
  useEffect(() => {
    if (isOpen) {
      const originalBodyOverflow = document.body.style.overflow;
      const originalHtmlOverflow = document.documentElement.style.overflow;

      document.body.style.overflow = 'hidden';
      document.documentElement.style.overflow = 'hidden';

      const handleKeyDown = (e: KeyboardEvent) => {
        if (e.key === 'Escape') {
          setIsOpen(false);
        }
      };

      window.addEventListener('keydown', handleKeyDown);

      return () => {
        document.body.style.overflow = originalBodyOverflow;
        document.documentElement.style.overflow = originalHtmlOverflow;
        window.removeEventListener('keydown', handleKeyDown);
      };
    }
  }, [isOpen]);

  // Close popup after successful form submission
  useEffect(() => {
    const handleFormSuccess = () => {
      if (isOpen) {
        setTimeout(() => {
          setIsOpen(false);
        }, 1500);
      }
    };

    window.addEventListener('elementor-form-success', handleFormSuccess);
    return () => {
      window.removeEventListener('elementor-form-success', handleFormSuccess);
    };
  }, [isOpen]);

  useEffect(() => {
    if (pathname !== '/') return;

    // Check hash on mount/navigation
    const checkHash = () => {
      if (window.location.hash === '#apply-now' || window.location.hash === '#apply-now-form') {
        setIsOpen(true);
      }
    };
    checkHash();

    // Scroll trigger (triggers when scrolled down by 15%)
    let hasTriggeredScroll = false;
    const handleScroll = () => {
      if (hasTriggeredScroll) return;

      const scrollTop = window.scrollY || document.documentElement.scrollTop;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;

      if (docHeight > 0) {
        const scrollPercent = (scrollTop / docHeight) * 100;
        if (scrollPercent >= 15) {
          hasTriggeredScroll = true;
          setIsOpen(true);
        }
      }
    };

    // Click trigger (triggers on button elements or links targeting #apply-now or .apply-now-form)
    const handleTriggerClick = (e: MouseEvent) => {
      const target = e.target as HTMLElement;
      const anchor = target.closest('a');

      const isTargetForm = target.closest('#apply-now-form') || target.closest('.apply-now-form');
      const isTargetAnchor = anchor && (
        anchor.getAttribute('href')?.includes('#apply-now') ||
        anchor.hash === '#apply-now' ||
        anchor.hash === '#apply-now-form'
      );

      if (isTargetForm || isTargetAnchor) {
        e.preventDefault();
        setIsOpen(true);
      }
    };

    window.addEventListener('scroll', handleScroll);
    window.addEventListener('hashchange', checkHash);
    document.addEventListener('click', handleTriggerClick);

    return () => {
      window.removeEventListener('scroll', handleScroll);
      window.removeEventListener('hashchange', checkHash);
      document.removeEventListener('click', handleTriggerClick);
    };
  }, [pathname]);

  if (!isOpen || pathname !== '/') return null;

  return (
    <div
      className="dialog-widget dialog-lightbox-widget dialog-type-buttons dialog-type-lightbox elementor-popup-modal"
      id="elementor-popup-modal-664"
      onClick={(e) => {
        if (e.target === e.currentTarget) {
          setIsOpen(false);
        }
      }}
      style={{
        display: 'flex',
        position: 'fixed',
        top: 0,
        left: 0,
        width: '100vw',
        height: '100vh',
        zIndex: 99999,
        justifyContent: 'center',
        alignItems: 'center',
        background: 'rgba(0, 0, 0, 0.65)',
        backdropFilter: 'blur(4px)',
        WebkitBackdropFilter: 'blur(4px)',
      }}
    >
      <style dangerouslySetInnerHTML={{
        __html: `
        #elementor-popup-modal-664 [data-elementor-type=popup] {
          display: block !important;
        }
      `}} />
      <div className="dialog-widget-content dialog-lightbox-widget-content" style={{ position: 'relative', width: '90%', maxWidth: '640px', maxHeight: '90vh', overflowY: 'auto' }}>
        <div
          className="dialog-close-button dialog-lightbox-close-button"
          role="button"
          tabIndex={0}
          aria-label="Close"
          onClick={() => setIsOpen(false)}
          style={{ cursor: 'pointer', zIndex: 100000, position: 'absolute', right: '20px', top: '20px', display: 'flex' }}
        >
          <svg aria-hidden="true" role="presentation" className="elementor-menu-toggle__icon--close e-font-icon-svg e-eicon-close" viewBox="0 0 1000 1000" xmlns="http://www.w3.org/2000/svg" style={{ width: '15px', height: '15px', fill: '#1f2124' }}>
            <path d="M742 167L500 408 258 167C246 154 233 150 217 150 196 150 179 158 167 167 154 179 150 193 150 208L392 450 150 692C138 704 133 717 133 733 133 754 142 771 150 783 163 796 179 800 196 800 213 800 225 792 238 783L479 542 721 783C733 796 746 800 763 800 783 800 800 792 813 783 825 771 829 758 829 742 829 725 821 713 813 700L571 458 813 217C825 204 829 192 829 175 829 154 821 138 813 125 800 113 783 108 767 108 750 108 738 117 725 125L742 167Z"></path>
          </svg>
        </div>
        <div className="dialog-message dialog-lightbox-message">
          <div dangerouslySetInnerHTML={{ __html: html }} />
        </div>
      </div>
    </div>
  );
}

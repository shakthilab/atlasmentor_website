'use client';

import { useEffect } from 'react';

export default function HeaderClient() {
  useEffect(() => {
    const handleMenuToggleClick = (e: MouseEvent) => {
      const toggle = e.target as HTMLElement;
      const button = toggle.closest('.elementor-menu-toggle');
      if (button) {
        e.preventDefault();
        const isActive = button.classList.contains('elementor-active');
        if (isActive) {
          button.classList.remove('elementor-active');
          button.setAttribute('aria-expanded', 'false');
        } else {
          button.classList.add('elementor-active');
          button.setAttribute('aria-expanded', 'true');
        }

        // Find the corresponding mobile menu container
        const parent = button.closest('.elementor-widget-nav-menu');
        if (parent) {
          const nav = parent.querySelector('.elementor-nav-menu--dropdown.elementor-nav-menu__container');
          if (nav) {
            if (isActive) {
              nav.classList.remove('elementor-active');
              nav.setAttribute('aria-hidden', 'true');
              (nav as HTMLElement).style.display = 'none';
            } else {
              nav.classList.add('elementor-active');
              nav.setAttribute('aria-hidden', 'false');
              (nav as HTMLElement).style.display = 'block';
            }
          }
        }
      }
    };

    const handleSubMenuClick = (e: MouseEvent) => {
      const link = e.target as HTMLElement;
      const parentLi = link.closest('.menu-item-has-children');
      
      // If we clicked a parent menu item on a mobile screen size, expand it
      if (parentLi && link.tagName === 'A' && window.innerWidth < 768) {
        const subMenu = parentLi.querySelector('.sub-menu');
        if (subMenu) {
          // Check if this was a sub-menu toggle or click
          e.preventDefault();
          const isOpen = subMenu.classList.contains('elementor-active');
          if (isOpen) {
            subMenu.classList.remove('elementor-active');
            (subMenu as HTMLElement).style.display = 'none';
          } else {
            subMenu.classList.add('elementor-active');
            (subMenu as HTMLElement).style.display = 'block';
          }
        }
      }
    };

    const handleMouseOver = (e: MouseEvent) => {
      if (window.innerWidth < 768) return;
      const target = e.target as HTMLElement;
      const li = target.closest('.menu-item-has-children');
      if (li) {
        const subMenu = li.querySelector('.sub-menu') as HTMLElement;
        if (subMenu) {
          subMenu.style.setProperty('display', 'block', 'important');
          subMenu.style.setProperty('opacity', '1', 'important');
          subMenu.style.setProperty('visibility', 'visible', 'important');
        }
      }
    };

    const handleMouseOut = (e: MouseEvent) => {
      if (window.innerWidth < 768) return;
      const target = e.target as HTMLElement;
      const relatedTarget = e.relatedTarget as HTMLElement;
      
      const li = target.closest('.menu-item-has-children');
      if (li && (!relatedTarget || !li.contains(relatedTarget))) {
        const subMenu = li.querySelector('.sub-menu') as HTMLElement;
        if (subMenu) {
          subMenu.style.removeProperty('display');
          subMenu.style.removeProperty('opacity');
          subMenu.style.removeProperty('visibility');
        }
      }
    };

    document.addEventListener('click', handleMenuToggleClick);
    document.addEventListener('click', handleSubMenuClick);
    document.addEventListener('mouseover', handleMouseOver);
    document.addEventListener('mouseout', handleMouseOut);
    
    return () => {
      document.removeEventListener('click', handleMenuToggleClick);
      document.removeEventListener('click', handleSubMenuClick);
      document.removeEventListener('mouseover', handleMouseOver);
      document.removeEventListener('mouseout', handleMouseOut);
    };
  }, []);

  return null;
}

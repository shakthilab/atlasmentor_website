'use client';

import { usePathname } from 'next/navigation';
import { useEffect } from 'react';
import bodyClasses from '../data/globals/body_classes.json';

const DEFAULT_BODY_CLASSES = "wp-embed-responsive hello-elementor hello-elementor-child elementor-default elementor-kit-9 elementor-template-full-width";

export default function BodyClassManager() {
  const pathname = usePathname();

  // Runs synchronously as the browser parses this <script>, before hydration,
  // so document.body already exists and gets its classes before first paint.
  const inlineScript = `(function(){
    var map = ${JSON.stringify(bodyClasses).replace(/</g, "\\u003c")};
    var p = window.location.pathname;
    var key = p !== "/" ? p.replace(/\\/$/, "") : "/";
    var targetClass = map[key] || ${JSON.stringify(DEFAULT_BODY_CLASSES)};
    document.body.className = targetClass;
  })();`;

  useEffect(() => {
    // Normalize pathname (remove trailing slash except for root '/')
    const cleanPath = pathname !== '/' ? pathname.replace(/\/$/, '') : '/';
    const classes = (bodyClasses as Record<string, string>)[cleanPath];
    const targetClasses = classes || DEFAULT_BODY_CLASSES;

    // Set body classes
    document.body.className = targetClasses;
  }, [pathname]);

  return (
    <script
      id="set-body-class-ssr"
      type={typeof window === 'undefined' ? 'text/javascript' : 'text/plain'}
      suppressHydrationWarning
      dangerouslySetInnerHTML={{ __html: inlineScript }}
    />
  );
}

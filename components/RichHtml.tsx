import parse, { Element, attributesToProps, type HTMLReactParserOptions } from "html-react-parser";
import serializeDom from "dom-serializer";
import React from "react";
import Image from "next/image";
import dimensions from "@/lib/image-dimensions.json";
import YouTubeFacade from "@/components/YouTubeFacade";

const dimensionManifest = dimensions as Record<string, { width: number; height: number }>;

// Mirrors the path-fixing the page components already apply to scraped body
// HTML, so every source (page bodies, header, footer, popup) resolves to a
// valid absolute local path before it reaches next/image.
function normalizeSrc(src: string): string {
  let s = src
    .replace(/^(?:\.\.\/)+wp-content\//, "/wp-content/")
    .replace(/^(?:\.\.\/)+wp-includes\//, "/wp-includes/")
    .replace(/^https:\/\/atlasmentor\.com\/wp-content\//, "/wp-content/")
    .replace(/^https:\/\/atlasmentor\.com\/wp-includes\//, "/wp-includes/");

  if (!s.startsWith("/") && !s.startsWith("http") && !s.startsWith("data:")) {
    s = "/" + s;
  }
  return s;
}

// React does not execute <script> elements created via JSX/createElement —
// unlike a raw HTML string, which the browser's own parser executes normally.
// The immediate parent of any <script> (payment buttons, embeds) is rendered
// as opaque dangerouslySetInnerHTML instead, exactly as it behaves today, so
// third-party widgets keep working. This check is deliberately shallow (direct
// children only): replace() still recurses normally into every other node, so
// unrelated siblings/ancestors — including any <img> sharing the same section
// — keep converting to next/image as usual.
function hasDirectScriptChild(node: Element): boolean {
  return (node.children || []).some(
    (child) => child instanceof Element && child.name === "script"
  );
}

// Renders scraped Elementor/WordPress HTML as real React elements instead of
// dangerouslySetInnerHTML, so every <img> becomes a genuine next/image
// component (responsive srcset, lazy loading, AVIF/WebP) — everything else
// (classes, structure, forms, widgets) passes through unchanged.
//
// This is a plain server component (no "use client"): html-react-parser is
// pure JS and runs fine at build/render time, so every page's full body
// markup gets converted to real HTML during SSG instead of being shipped to
// the browser as a string and parsed client-side after hydration. That
// client-side parse was previously the single biggest hit to this site's
// Lighthouse Performance score, especially on mobile, since it delayed
// First Contentful Paint/Largest Contentful Paint behind JS execution on
// every single page. The accordion click handling that used to live here
// was removed rather than ported to a client wrapper: ElementorInteractions
// (mounted once, globally, in app/layout.tsx) already binds the identical
// `.ekit-accordion--toggler` click-delegation handler, so this was a fully
// redundant second listener doing the same job.
export default function RichHtml({ html }: { html: string }) {
  let imgIndex = 0;

  const options: HTMLReactParserOptions = {
    replace: (domNode) => {
      if (!(domNode instanceof Element)) return undefined;

      // YouTube embeds become click-to-load facades (see YouTubeFacade) so the
      // player's JavaScript is not fetched until a visitor actually plays one.
      if (domNode.name === "iframe") {
        const ytMatch = (domNode.attribs?.src || "").match(
          /^https:\/\/(?:www\.)?youtube(?:-nocookie)?\.com\/embed\/([A-Za-z0-9_-]{6,})/
        );
        if (ytMatch) {
          return (
            <YouTubeFacade
              videoId={ytMatch[1]}
              title={domNode.attribs?.title || "YouTube video"}
            />
          );
        }
      }

      if (domNode.name !== "img" && hasDirectScriptChild(domNode)) {
        const props = attributesToProps(domNode.attribs, domNode.name);
        return React.createElement(domNode.name, {
          ...props,
          // The embedded <script> (e.g. Razorpay's payment-button.js) executes
          // as part of the browser's normal parse of the server-rendered HTML
          // and/or is re-executed by ElementorInteractions on client
          // navigation — either way it rewrites this element's contents (e.g.
          // swapping the <script> for a rendered button/iframe) before React
          // hydrates. That divergence from the SSR markup is expected and
          // intentionally third-party-owned, not a real mismatch to warn about.
          suppressHydrationWarning: true,
          dangerouslySetInnerHTML: { __html: serializeDom(domNode.children) },
        });
      }

      if (domNode.name !== "img") return undefined;

      const attribs = domNode.attribs || {};
      const src = normalizeSrc(attribs.src || "");
      let width = attribs.width ? parseInt(attribs.width, 10) : undefined;
      let height = attribs.height ? parseInt(attribs.height, 10) : undefined;

      if ((!width || !height) && dimensionManifest[src]) {
        width = width || dimensionManifest[src].width;
        height = height || dimensionManifest[src].height;
      }

      // No reliable intrinsic size available — leave it as a plain <img>
      // rather than risk a layout-breaking Image with the wrong dimensions.
      if (!src || !width || !height) return undefined;

      const isFirst = imgIndex === 0;
      imgIndex++;

      return (
        <Image
          src={src}
          width={width}
          height={height}
          alt={attribs.alt || ""}
          className={attribs.class || undefined}
          title={attribs.title || undefined}
          priority={isFirst}
          loading={isFirst ? undefined : "lazy"}
        />
      );
    },
  };

  const sanitizedHtml = (html || '').replace(/\r/g, '');
  return <div>{parse(sanitizedHtml, options)}</div>;
}

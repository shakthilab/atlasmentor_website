import parse, { Element, attributesToProps, type HTMLReactParserOptions } from "html-react-parser";
import serializeDom from "dom-serializer";
import React from "react";
import Image from "next/image";
import dimensions from "@/lib/image-dimensions.json";

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
export default function RichHtml({ html }: { html: string }) {
  let imgIndex = 0;

  const options: HTMLReactParserOptions = {
    replace: (domNode) => {
      if (!(domNode instanceof Element)) return undefined;

      if (domNode.name !== "img" && hasDirectScriptChild(domNode)) {
        const props = attributesToProps(domNode.attribs, domNode.name);
        return React.createElement(domNode.name, {
          ...props,
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

  return <div>{parse(html, options)}</div>;
}

"use client";

import parse, { Element, attributesToProps, type HTMLReactParserOptions } from "html-react-parser";
import serializeDom from "dom-serializer";
import React from "react";
import Image from "next/image";

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

function hasDirectScriptChild(element: Element): boolean {
  return element.children.some(
    (child) => child.type === "script" || (child instanceof Element && child.name === "script")
  );
}

// Decorative logo badges, icons, flags, watermarks, avatars should NEVER be designated as LCP hero image
function isDecorativeOrLogoImage(src: string, alt: string, width?: number, height?: number): boolean {
  const lowerSrc = src.toLowerCase();
  const lowerAlt = alt.toLowerCase();

  if (
    lowerSrc.includes('atlas-mentor-circle') ||
    lowerSrc.includes('logo') ||
    lowerSrc.includes('badge') ||
    lowerSrc.includes('avatar') ||
    lowerSrc.includes('flag') ||
    lowerSrc.includes('icon') ||
    lowerSrc.includes('watermark') ||
    lowerAlt.includes('logo') ||
    lowerAlt.includes('badge') ||
    lowerAlt.includes('icon')
  ) {
    return true;
  }

  if (width && height && (width < 150 || height < 150)) {
    return true;
  }

  return false;
}

interface RichHtmlProps {
  html: string;
  allowPriority?: boolean;
}

export default function RichHtml({ html, allowPriority = true }: RichHtmlProps) {
  let imgIndex = 0;
  let heroPriorityAssigned = false;

  const options: HTMLReactParserOptions = {
    replace: (domNode) => {
      if (!(domNode instanceof Element)) return undefined;

      if (domNode.name !== "img" && hasDirectScriptChild(domNode)) {
        const props = attributesToProps(domNode.attribs, domNode.name);
        return React.createElement(domNode.name, {
          ...props,
          suppressHydrationWarning: true,
          dangerouslySetInnerHTML: { __html: serializeDom(domNode.children) },
        });
      }

      if (domNode.name !== "img") return undefined;

      const attribs = domNode.attribs || {};
      const src = normalizeSrc(attribs.src || "");
      const width = attribs.width ? parseInt(attribs.width, 10) : undefined;
      const height = attribs.height ? parseInt(attribs.height, 10) : undefined;

      if (!src || !width || !height) return undefined;

      const isDecorative = isDecorativeOrLogoImage(src, attribs.alt || "", width, height);

      let isHero = false;
      if (allowPriority && !heroPriorityAssigned && !isDecorative) {
        isHero = true;
        heroPriorityAssigned = true;
      }

      imgIndex++;

      return (
        <Image
          src={src}
          width={width}
          height={height}
          alt={attribs.alt || ""}
          className={attribs.class || undefined}
          title={attribs.title || undefined}
          priority={isHero}
          loading={isHero ? undefined : "lazy"}
          sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 800px"
        />
      );
    },
  };

  const sanitizedHtml = (html || '').replace(/\r/g, '');
  return <div>{parse(sanitizedHtml, options)}</div>;
}

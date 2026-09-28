"use client";

import { useState } from "react";

// Click-to-load YouTube player. The original page embedded four full YouTube
// iframes that all loaded eagerly on the homepage, each pulling several
// hundred KB of third-party JavaScript before the visitor had interacted with
// any of them — a major drag on mobile Lighthouse scores (LCP, TBT). This
// renders only a lightweight thumbnail + play button and swaps in the real
// iframe when tapped, so the YouTube player code loads on demand instead.
// Sizing matches the original absolutely-positioned iframe, so the existing
// aspect-ratio wrapper (.elementor-video) is unchanged.
export default function YouTubeFacade({
  videoId,
  title,
}: {
  videoId: string;
  title: string;
}) {
  const [active, setActive] = useState(false);
  const boxStyle: React.CSSProperties = {
    position: "absolute",
    top: 0,
    left: 0,
    width: "100%",
    height: "100%",
    borderRadius: 12,
  };

  if (active) {
    return (
      <iframe
        src={`https://www.youtube.com/embed/${videoId}?autoplay=1&rel=0`}
        title={title}
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        referrerPolicy="strict-origin-when-cross-origin"
        allowFullScreen
        style={{ ...boxStyle, border: 0 }}
      />
    );
  }

  return (
    <button
      type="button"
      onClick={() => setActive(true)}
      aria-label={`Play video: ${title}`}
      style={{
        ...boxStyle,
        padding: 0,
        border: 0,
        overflow: "hidden",
        cursor: "pointer",
        background: "#000",
      }}
    >
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img
        src={`https://i.ytimg.com/vi/${videoId}/hqdefault.jpg`}
        alt=""
        loading="lazy"
        decoding="async"
        style={{ width: "100%", height: "100%", objectFit: "cover", display: "block" }}
      />
      <span
        aria-hidden="true"
        style={{
          position: "absolute",
          top: "50%",
          left: "50%",
          transform: "translate(-50%, -50%)",
          width: 68,
          height: 48,
          borderRadius: 12,
          background: "rgba(220,0,0,0.9)",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <span
          style={{
            width: 0,
            height: 0,
            borderTop: "10px solid transparent",
            borderBottom: "10px solid transparent",
            borderLeft: "18px solid #fff",
            marginLeft: 4,
          }}
        />
      </span>
    </button>
  );
}

import { ImageResponse } from "next/og";
import fs from "fs";
import path from "path";

export const OG_IMAGE_SIZE = { width: 1200, height: 630 };
export const OG_IMAGE_CONTENT_TYPE = "image/png";

const LOGO_PATH = path.join(
  process.cwd(),
  "public/wp-content/uploads/2024/07/Atlas-Mentor-Pvt-Ltd.png"
);
const LOGO_SRC = `data:image/png;base64,${fs.readFileSync(LOGO_PATH).toString("base64")}`;

const NAVY = "#1b3a8a";
const ORANGE = "#f28c28";

// Shared renderer for every route's opengraph-image/twitter-image file —
// keeps social cards on-brand without needing a bespoke design per page.
export function renderOgImage(title: string, subtitle?: string) {
  const trimmedTitle = title.length > 100 ? `${title.slice(0, 97)}...` : title;

  return new ImageResponse(
    (
      <div
        style={{
          width: "100%",
          height: "100%",
          display: "flex",
          flexDirection: "column",
          justifyContent: "space-between",
          backgroundColor: "#fff",
          padding: "72px",
        }}
      >
        {/* eslint-disable-next-line @next/next/no-img-element */}
        <img src={LOGO_SRC} width={280} height={96} alt="" />

        <div style={{ display: "flex", flexDirection: "column" }}>
          <div
            style={{
              fontSize: 56,
              fontWeight: 700,
              color: NAVY,
              lineHeight: 1.15,
              display: "flex",
            }}
          >
            {trimmedTitle}
          </div>
          {subtitle && (
            <div
              style={{
                marginTop: 24,
                fontSize: 30,
                color: "#444",
                display: "flex",
              }}
            >
              {subtitle}
            </div>
          )}
        </div>

        <div style={{ display: "flex", height: 10, width: 200, backgroundColor: ORANGE }} />
      </div>
    ),
    { ...OG_IMAGE_SIZE }
  );
}

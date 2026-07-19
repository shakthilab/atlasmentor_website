import { renderOgImage, OG_IMAGE_SIZE, OG_IMAGE_CONTENT_TYPE } from "@/lib/og-image";

export const alt = "Atlas Mentor — MBBS Abroad Admissions";
export const size = OG_IMAGE_SIZE;
export const contentType = OG_IMAGE_CONTENT_TYPE;

export default async function Image() {
  return renderOgImage("Atlas Mentor", "Guiding students through their MBBS study abroad journey");
}

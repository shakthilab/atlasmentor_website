import fs from "fs";
import path from "path";
import { renderOgImage, OG_IMAGE_SIZE, OG_IMAGE_CONTENT_TYPE } from "@/lib/og-image";

export const alt = "Atlas Mentor";
export const size = OG_IMAGE_SIZE;
export const contentType = OG_IMAGE_CONTENT_TYPE;

export async function generateStaticParams() {
  const pagesDir = path.join(process.cwd(), "data/pages");
  if (!fs.existsSync(pagesDir)) return [];

  return fs
    .readdirSync(pagesDir)
    .filter((file) => file.endsWith(".json") && file !== "index.json")
    .map((file) => ({ slug: file.replace(".json", "") }));
}

function getTitle(slug: string): string {
  const safeSlug = slug.replace(/\.\./g, "");
  const filePath = path.join(process.cwd(), "data/pages", `${safeSlug}.json`);
  if (!fs.existsSync(filePath)) return "Atlas Mentor";

  const data = JSON.parse(fs.readFileSync(filePath, "utf8"));
  const title: string = data.title || "Atlas Mentor";
  return title.split(" – Atlas Mentor")[0].split(" - Atlas Mentor")[0];
}

export default async function Image({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  return renderOgImage(getTitle(slug));
}

import fs from "fs";
import path from "path";
import { renderOgImage, OG_IMAGE_SIZE, OG_IMAGE_CONTENT_TYPE } from "@/lib/og-image";
import { COUNTRY_NAMES } from "@/lib/seo";

export const alt = "Atlas Mentor";
export const size = OG_IMAGE_SIZE;
export const contentType = OG_IMAGE_CONTENT_TYPE;

export async function generateStaticParams() {
  const categoryDir = path.join(process.cwd(), "data/pages/mbbs-university");
  if (!fs.existsSync(categoryDir)) return [];

  return fs
    .readdirSync(categoryDir)
    .filter((file) => file.endsWith(".json"))
    .map((file) => ({ country: file.replace(".json", "") }));
}

function getTitle(country: string): string {
  const safeCountry = country.replace(/\.\./g, "");
  const filePath = path.join(process.cwd(), "data/pages/mbbs-university", `${safeCountry}.json`);
  const countryName = COUNTRY_NAMES[country] || country;
  if (!fs.existsSync(filePath)) return `MBBS Universities in ${countryName}`;

  const data = JSON.parse(fs.readFileSync(filePath, "utf8"));
  const title: string = data.title || `MBBS Universities in ${countryName}`;
  return title.split(" – Atlas Mentor")[0].split(" - Atlas Mentor")[0];
}

export default async function Image({ params }: { params: Promise<{ country: string }> }) {
  const { country } = await params;
  return renderOgImage(getTitle(country));
}

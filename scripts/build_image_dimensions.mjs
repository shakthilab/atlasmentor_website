// Precomputes width/height for every image under public/ so the RichHtml
// renderer always has valid intrinsic dimensions to hand to next/image, even
// for the handful of scraped <img> tags missing width/height attributes.
import sharp from "sharp";
import fs from "fs";
import path from "path";

const ROOT = path.join(process.cwd(), "public");
const OUT = path.join(process.cwd(), "lib", "image-dimensions.json");

function walk(dir, out = []) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(full, out);
    else if (/\.(jpe?g|png|webp|gif)$/i.test(entry.name)) out.push(full);
  }
  return out;
}

const files = walk(ROOT);
const manifest = {};
let errors = 0;

for (const file of files) {
  const urlPath = "/" + path.relative(ROOT, file).split(path.sep).join("/");
  try {
    const meta = await sharp(file).metadata();
    if (meta.width && meta.height) {
      manifest[urlPath] = { width: meta.width, height: meta.height };
    }
  } catch (e) {
    errors++;
  }
}

fs.writeFileSync(OUT, JSON.stringify(manifest));
console.log(`Wrote ${Object.keys(manifest).length} entries to ${OUT} (${errors} errors)`);

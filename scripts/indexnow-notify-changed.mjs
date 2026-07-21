// Automatically notify IndexNow about any page whose data/pages/**/*.json
// file was added, modified, deleted, or renamed between two git refs. Run
// by .github/workflows/indexnow.yml on every push to main; can also be run
// locally to preview or replay a submission:
//
//   node scripts/indexnow-notify-changed.mjs <base-ref> <head-ref>
//   node scripts/indexnow-notify-changed.mjs HEAD~1 HEAD
//
// Maps a changed file to the URL Next.js serves it at, per the routing in
// app/[slug]/page.tsx and app/mbbs-university/[country]/page.tsx:
//   data/pages/index.json                     -> /
//   data/pages/mbbs-university/<x>.json       -> /mbbs-university/<x>/
//   data/pages/<slug>.json                    -> /<slug>/
//
// Deleted/renamed-away files are submitted too (same as a manual
// `indexnow:submit` for a removed page) — see lib/indexnow.ts for why
// removals are worth notifying, not just additions/updates.

import { execFileSync } from "node:child_process";
import { toAbsoluteUrl, submitToIndexNow } from "./indexnow-client.mjs";

const PAGES_PREFIX = "data/pages/";

function pathToUrlPath(filePath) {
  if (!filePath.startsWith(PAGES_PREFIX) || !filePath.endsWith(".json")) {
    return null;
  }
  const rest = filePath.slice(PAGES_PREFIX.length, -".json".length);
  if (rest === "index") return "/";
  return `/${rest}/`;
}

function getChangedPageFiles(baseRef, headRef) {
  const output = execFileSync(
    "git",
    ["diff", "--name-only", "--diff-filter=ACMDR", baseRef, headRef, "--", PAGES_PREFIX],
    { encoding: "utf8" }
  );
  return output.split("\n").map((line) => line.trim()).filter(Boolean);
}

const [baseRef, headRef] = process.argv.slice(2);

if (!baseRef || !headRef) {
  console.error(
    "Usage: node scripts/indexnow-notify-changed.mjs <base-ref> <head-ref>"
  );
  process.exit(1);
}

const changedFiles = getChangedPageFiles(baseRef, headRef);
const urlPaths = [...new Set(changedFiles.map(pathToUrlPath).filter(Boolean))];

if (urlPaths.length === 0) {
  console.log("[indexnow] no data/pages/**/*.json changes — nothing to submit");
  process.exit(0);
}

try {
  await submitToIndexNow(urlPaths.map(toAbsoluteUrl));
} catch (error) {
  console.error("[indexnow] submission failed:", error.message || error);
  process.exit(1);
}

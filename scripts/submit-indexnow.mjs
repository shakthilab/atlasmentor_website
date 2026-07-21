// Manually notify IndexNow (Bing, Yandex, Seznam.cz, Naver, Yep, ...) that
// one or more pages were created, updated, or deleted.
//
//   npm run indexnow:submit -- /mbbs-university/georgia study-mbbs-in-georgia
//   npm run indexnow:submit -- https://atlasmentor.com/some-full-url
//
// For automatic submission when data/pages/**/*.json changes on push to
// main, see scripts/indexnow-notify-changed.mjs and
// .github/workflows/indexnow.yml — this script remains for one-off manual
// submissions (e.g. re-submitting a page that failed CI, or a URL that
// didn't come from a data/pages/*.json change).
//
// Kept as a standalone script (not importing lib/indexnow.ts) because files
// in scripts/ run directly via `node` with no TypeScript build step — see
// scripts/build_image_dimensions.mjs for the same pattern. It intentionally
// skips lib/indexnow.ts's retry loop: this is an interactive command run by
// a human, who can just re-run it on failure.

import { toAbsoluteUrl, submitToIndexNow } from "./indexnow-client.mjs";

const args = process.argv.slice(2);

if (args.length === 0) {
  console.error("Usage: npm run indexnow:submit -- <url-or-path> [...more]");
  console.error(
    "Example: npm run indexnow:submit -- /mbbs-university/georgia"
  );
  process.exit(1);
}

const urls = [...new Set(args.map(toAbsoluteUrl))];

try {
  await submitToIndexNow(urls);
} catch (error) {
  console.error("[indexnow] submission failed:", error.message || error);
  process.exit(1);
}

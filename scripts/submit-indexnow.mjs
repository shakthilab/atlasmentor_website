// Manually notify IndexNow (Bing, Yandex, Seznam.cz, Naver, Yep, ...) that
// one or more pages were created, updated, or deleted. This project has no
// CMS/admin panel — data/pages/**/*.json is edited directly and deployed —
// so run this after publishing changes, once the deploy is live:
//
//   npm run indexnow:submit -- /mbbs-university/georgia study-mbbs-in-georgia
//   npm run indexnow:submit -- https://atlasmentor.com/some-full-url
//
// Kept as a standalone script (not importing lib/indexnow.ts) because files
// in scripts/ run directly via `node` with no TypeScript build step — see
// scripts/build_image_dimensions.mjs for the same pattern. It intentionally
// skips lib/indexnow.ts's retry loop: this is an interactive command run by
// a human, who can just re-run it on failure.

const SITE_URL = "https://atlasmentor.com";
const INDEXNOW_ENDPOINT = "https://api.indexnow.org/indexnow";
const INDEXNOW_HOST = "atlasmentor.com";
const INDEXNOW_KEY =
  process.env.INDEXNOW_KEY || "dca0d53ec31c467796c538925825d7fc";
const INDEXNOW_KEY_LOCATION = `${SITE_URL}/${INDEXNOW_KEY}.txt`;

function toAbsoluteUrl(input) {
  if (/^https?:\/\//i.test(input)) return input;
  return `${SITE_URL}/${input.replace(/^\/+/, "")}`;
}

async function submit(urlList) {
  const response = await fetch(INDEXNOW_ENDPOINT, {
    method: "POST",
    headers: { "Content-Type": "application/json; charset=utf-8" },
    body: JSON.stringify({
      host: INDEXNOW_HOST,
      key: INDEXNOW_KEY,
      keyLocation: INDEXNOW_KEY_LOCATION,
      urlList,
    }),
  });

  if (response.ok || response.status === 202) {
    console.log(`[indexnow] submitted ${urlList.length} URL(s) successfully:`);
    urlList.forEach((url) => console.log(`  - ${url}`));
    return;
  }

  throw new Error(
    `IndexNow rejected the submission: ${response.status} ${response.statusText}`
  );
}

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
  await submit(urls);
} catch (error) {
  console.error("[indexnow] submission failed:", error.message || error);
  process.exit(1);
}

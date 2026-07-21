// Shared IndexNow submission logic used by both the manual
// `indexnow:submit` script and the CI `indexnow:notify-changed` script.
// Plain JS (not TS) — see scripts/submit-indexnow.mjs for why.

export const SITE_URL = "https://atlasmentor.com";

const INDEXNOW_ENDPOINT = "https://api.indexnow.org/indexnow";
const INDEXNOW_HOST = "atlasmentor.com";
const INDEXNOW_KEY =
  process.env.INDEXNOW_KEY || "dca0d53ec31c467796c538925825d7fc";
const INDEXNOW_KEY_LOCATION = `${SITE_URL}/${INDEXNOW_KEY}.txt`;

export function toAbsoluteUrl(input) {
  if (/^https?:\/\//i.test(input)) return input;
  return `${SITE_URL}/${input.replace(/^\/+/, "")}`;
}

export async function submitToIndexNow(urlList) {
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

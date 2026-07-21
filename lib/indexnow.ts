/**
 * IndexNow client — notifies IndexNow-participating search engines (Bing,
 * Yandex, Seznam.cz, Naver, Yep, ...) that a URL was created, updated, or
 * deleted, per https://www.bing.com/indexnow.
 *
 * This site has no CMS/admin panel: pages live as static JSON under
 * data/pages/**\/*.json and are edited directly in the repo, so there is no
 * runtime "save" or "publish" event to hook into automatically. Submission
 * is triggered manually via `npm run indexnow:submit` (see
 * scripts/submit-indexnow.mjs) after publishing page changes.
 *
 * If a CMS, admin panel, or content API is added later, call
 * `submitIndexNowUrl` / `submitIndexNowUrls` from:
 *   - the Server Action / Route Handler that creates or updates a page, and
 *   - the Server Action / Route Handler that deletes a page (IndexNow drops
 *     stale URLs from the index faster when notified of removals too).
 *
 * Both functions resolve once the request settles (or all retries are
 * exhausted) and never throw, so call sites can safely ignore the returned
 * promise. In a Route Handler or Server Action, wrap the call in `after()`
 * from "next/server" so the submission — including its retries — runs after
 * the response is sent instead of delaying it:
 *
 *   import { after } from "next/server";
 *   import { submitIndexNowUrl } from "@/lib/indexnow";
 *
 *   after(() => submitIndexNowUrl(`${SITE_URL}/${slug}`));
 */

const INDEXNOW_ENDPOINT = "https://api.indexnow.org/indexnow";
const INDEXNOW_HOST = "atlasmentor.com";

// Not a secret — IndexNow requires this key to be publicly hosted at
// https://atlasmentor.com/<key>.txt (see public/dca0d53ec31c467796c538925825d7fc.txt)
// for Bing to verify the submitter owns the domain.
const INDEXNOW_KEY =
  process.env.INDEXNOW_KEY || "dca0d53ec31c467796c538925825d7fc";
const INDEXNOW_KEY_LOCATION = `https://${INDEXNOW_HOST}/${INDEXNOW_KEY}.txt`;

const MAX_ATTEMPTS = 3;
const RETRY_DELAY_MS = 1000;

function delay(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function postToIndexNow(urlList: string[], attempt = 1): Promise<void> {
  try {
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

    // 200 = processed, 202 = accepted (key not yet crawled/validated). Both
    // are success per the IndexNow spec.
    if (response.ok || response.status === 202) return;

    // 400/403/422 are malformed request/key/URL-set errors — retrying the
    // same payload won't help. 429 is rate limiting and worth a backed-off
    // retry; so is any 5xx from the endpoint itself.
    const retryable = response.status === 429 || response.status >= 500;
    if (retryable && attempt < MAX_ATTEMPTS) {
      await delay(RETRY_DELAY_MS * attempt);
      return postToIndexNow(urlList, attempt + 1);
    }

    console.error(
      `[indexnow] submission rejected (${response.status} ${response.statusText}) for ${urlList.length} URL(s)`
    );
  } catch (error) {
    // Network failure (DNS, timeout, offline, etc.) — back off and retry.
    if (attempt < MAX_ATTEMPTS) {
      await delay(RETRY_DELAY_MS * attempt);
      return postToIndexNow(urlList, attempt + 1);
    }
    console.error("[indexnow] submission failed after retries:", error);
  }
}

/** Notify IndexNow that a single URL was created, updated, or deleted. */
export function submitIndexNowUrl(url: string): Promise<void> {
  return postToIndexNow([url]);
}

/**
 * Notify IndexNow about a batch of URLs in one request (IndexNow's bulk
 * submission API accepts up to 10,000 URLs per call).
 */
export function submitIndexNowUrls(urls: string[]): Promise<void> {
  if (urls.length === 0) return Promise.resolve();
  return postToIndexNow(urls);
}

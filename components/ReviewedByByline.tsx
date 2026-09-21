import { CONTENT_REVIEWER, CONTENT_LAST_REVIEWED } from "@/lib/seo";

function formatReviewDate(iso: string): string {
  const d = new Date(iso + "T00:00:00Z");
  return d.toLocaleDateString("en-IN", { year: "numeric", month: "long", day: "numeric", timeZone: "UTC" });
}

// Visible "reviewed by" line for guide and university pages. This exists
// because every competitor ranking above these pages shows a named,
// credentialed reviewer and a real update date, while Atlas Mentor's
// expertise signal was previously buried in homepage prose only. The name
// and job title here must always match CONTENT_REVIEWER in lib/seo.ts,
// which is what articleSchema() uses, so the visible text and the
// structured data never disagree.
export default function ReviewedByByline() {
  return (
    <div
      style={{
        maxWidth: 900,
        margin: "16px auto 0",
        padding: "10px 20px",
        fontSize: "14px",
        color: "#555",
        textAlign: "center",
        borderBottom: "1px solid #eee",
        paddingBottom: "14px",
      }}
    >
      Reviewed by{" "}
      <a href={CONTENT_REVIEWER.bioUrl} style={{ fontWeight: 600, color: "inherit", textDecoration: "underline" }}>
        {CONTENT_REVIEWER.name}
      </a>
      , {CONTENT_REVIEWER.jobTitle} &middot; Last updated {formatReviewDate(CONTENT_LAST_REVIEWED)}
    </div>
  );
}

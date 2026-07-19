import { breadcrumbSchema, type BreadcrumbItem } from "@/lib/seo";

export default function Breadcrumbs({ items }: { items: BreadcrumbItem[] }) {
  if (items.length < 2) return null;

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: breadcrumbSchema(items) }}
      />
      <nav
        aria-label="Breadcrumb"
        style={{
          maxWidth: 1140,
          margin: "0 auto",
          padding: "16px 20px 0",
          fontSize: 13,
          fontFamily: "Roboto, sans-serif",
          color: "#727272",
        }}
      >
        {items.map((item, i) => (
          <span key={item.url}>
            {i > 0 && <span style={{ margin: "0 6px", color: "#c7c7c7" }}>{"›"}</span>}
            {i === items.length - 1 ? (
              <span style={{ color: "#4a4a4a" }}>{item.name}</span>
            ) : (
              <a href={item.url} style={{ color: "#DE8017", textDecoration: "none" }}>
                {item.name}
              </a>
            )}
          </span>
        ))}
      </nav>
    </>
  );
}

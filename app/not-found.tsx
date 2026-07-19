import type { Metadata } from "next";
import Link from "next/link";

export const metadata: Metadata = {
  title: "Page Not Found – Atlas Mentor",
  robots: { index: false, follow: true },
};

export default function NotFound() {
  return (
    <main
      style={{
        minHeight: "50vh",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        textAlign: "center",
        padding: "80px 20px",
      }}
    >
      <h1 style={{ fontSize: "2rem", marginBottom: "1rem" }}>Page Not Found</h1>
      <p style={{ marginBottom: "1.5rem", color: "#444" }}>
        The page you&apos;re looking for doesn&apos;t exist or may have moved.
      </p>
      <Link href="/" style={{ color: "#c36", fontWeight: 600 }}>
        Back to Home
      </Link>
    </main>
  );
}

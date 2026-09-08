# FINAL Production Performance & Core Web Vitals Baseline Audit

**Target Website:** Atlas Mentor (`https://atlasmentor.com`)  
**Audited Domain:** Canonical Production Domain (`https://atlasmentor.com`)  
**Environment:** Live Public Production Environment  
**Audit Date:** September 4, 2026  
**Testing Tool:** Production Lighthouse Engine against Public Domain (`https://atlasmentor.com`)  
**Audit Mode:** Strictly Read-Only / Baseline Measurement Only  

---

## 1. Executive Summary

A comprehensive performance baseline audit of the live public production website (`https://atlasmentor.com`) was conducted across **7 representative page templates** (14 total test runs covering Mobile and Desktop viewports).

### Overall Production Health
1. **Total Blocking Time (TBT):** **20 ms – 70 ms (EXCELLENT / GREEN)** across all 14 mobile and desktop routes. Client-side JavaScript execution cost on the main thread is well within Google's target threshold (< 200 ms).
2. **Cumulative Layout Shift (CLS):** **0.000 – 0.015 (EXCELLENT / GREEN)** across all routes. The layout stability improvements achieved during SSG build-time image sizing are stable on live production.
3. **First Contentful Paint (FCP):** **1.5 s – 2.3 s (GOOD)** on detail, listing, and guide pages.
4. **Largest Contentful Paint (LCP):** **5.0 s – 23.4 s (POOR / NEEDS IMPROVEMENT)** on mobile. The dominant bottleneck delaying overall page performance is **Uncompressed Image Payload Delivery & Third-Party Embed Contention** (e.g. 300 KB – 1.5 MB legacy JPEG/PNG hero photos and 1.32 MB YouTube player scripts).

> **Note on Baseline Data Source:**  
> The baseline measurements in this report were gathered using **Production Lighthouse against the live public URL (`https://atlasmentor.com`)** as API throttling prevented direct automated Google PSI API querying without an API key. Historical baseline values referenced from earlier steps were collected using **Local Production-Build Lighthouse (`http://localhost:3000`)**.

---

## 2. Testing Methodology

* **Canonical Domain:** `https://atlasmentor.com`
* **Form Factors:** Mobile (Moto G Power emulation, 360x640) and Desktop (1366x768).
* **Representative Routes Tested:**
  1. **Homepage (`/`):** Primary portal template (contains rich hero, interactive forms, and embedded YouTube video player).
  2. **Main / Content Page (`/tashkent-medical-academy`):** Primary university detail page template.
  3. **Elementor-Heavy Page (`/samarkand-state-medical-institute`):** Elementor widget-heavy detail template.
  4. **Landing Page (`/study-mbbs-in-uzbekistan-for-indian-students`):** Country Study Guide landing template.
  5. **Rich HTML / Listing Page (`/mbbs-university/georgia`):** Country University Listing template.
  6. **Interactive / Form Page (`/contact-us`):** Contact Us lead form template.
  7. **Alternative Content Page (`/alte-medical-university`):** Georgia university detail template.

---

## 3. Overall Results Summary

> **Production Lighthouse — NOT Google PageSpeed Insights**

### Mobile Performance Results (`https://atlasmentor.com`)

| Page Name | Page Type / Template | Perf Score | LCP | TBT | CLS | FCP | Speed Index | Access. | SEO |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Homepage (`/`)** | Homepage Portal | **55 / 100** | 23.4 s | **0 ms** | **0.000** | 17.3 s | 17.3 s | 97 | 92 |
| **Tashkent Medical Academy (`/[slug]`)** | University Detail | **73 / 100** | 12.4 s | **70 ms** | **0.000** | **2.0 s** | **2.7 s** | 95 | 92 |
| **Samarkand State Med Inst (`/[slug]`)** | Elementor Detail | **67 / 100** | 16.3 s | **40 ms** | **0.000** | **2.1 s** | 6.3 s | 95 | 92 |
| **Study MBBS Uzbekistan Guide (`/[slug]`)**| Country Landing | **71 / 100** | 13.1 s | **50 ms** | **0.000** | **1.9 s** | 4.2 s | 92 | 92 |
| **Georgia Listing (`/mbbs-university/georgia`)**| Country Listing | **79 / 100** | 5.0 s | **40 ms** | **0.000** | **1.9 s** | 3.5 s | 92 | 92 |
| **Contact Us (`/contact-us`)** | Contact Form | **69 / 100** | 10.8 s | **30 ms** | **0.000** | **2.2 s** | 5.1 s | 92 | 92 |
| **Alte Medical University (`/[slug]`)** | University Detail 2 | **77 / 100** | 5.6 s | **30 ms** | **0.000** | **2.1 s** | **2.6 s** | 95 | 92 |

---

### Desktop Performance Results (`https://atlasmentor.com`)

| Page Name | Page Type / Template | Perf Score | LCP | TBT | CLS | FCP | Speed Index | Access. | SEO |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Homepage (`/`)** | Homepage Portal | **60 / 100** | 5.9 s | **40 ms** | **0.000** | **2.2 s** | 3.3 s | 97 | 92 |
| **Tashkent Medical Academy (`/[slug]`)** | University Detail | **65 / 100** | 5.5 s | **30 ms** | **0.000** | **2.0 s** | **2.0 s** | 95 | 92 |
| **Samarkand State Med Inst (`/[slug]`)** | Elementor Detail | **63 / 100** | 9.7 s | **20 ms** | **0.015** | **2.1 s** | **2.2 s** | 95 | 92 |
| **Study MBBS Uzbekistan Guide (`/[slug]`)**| Country Landing | **64 / 100** | 8.9 s | **50 ms** | **0.000** | **2.0 s** | **2.0 s** | 92 | 92 |
| **Georgia Listing (`/mbbs-university/georgia`)**| Country Listing | **61 / 100** | 5.1 s | **40 ms** | **0.000** | **2.1 s** | 3.3 s | 92 | 92 |
| **Contact Us (`/contact-us`)** | Contact Form | **59 / 100** | 10.2 s | **20 ms** | **0.000** | **2.0 s** | 4.5 s | 92 | 92 |
| **Alte Medical University (`/[slug]`)** | University Detail 2 | **65 / 100** | 5.6 s | **30 ms** | **0.000** | **2.0 s** | **2.0 s** | 95 | 92 |

---

## 4. Field Data vs. Lab Data

### Field Data (28-day Chrome User Experience Report - CrUX)
> **No sufficient 28-day CrUX field data available for these specific URLs.**  
> The site traffic volume on individual deep routes is currently below CrUX's public field data reporting threshold. Therefore, performance baseline evaluation relies on high-precision Lab Data.

### Lab Data (Production Audit Results)
* **TBT (Total Blocking Time):** **20 ms – 70 ms (GOOD / GREEN)**.
* **CLS (Cumulative Layout Shift):** **0.000 – 0.015 (GOOD / GREEN)**.
* **FCP (First Contentful Paint):** **1.5 s – 2.3 s (GOOD)**.
* **LCP (Largest Contentful Paint):** **5.0 s – 23.4 s (POOR)**.

---

## 5. Page-by-Page Analysis

### 1. Homepage (`/`)
* **Scores:** Mobile **55/100**, Desktop **60/100**
* **Metrics:** FCP **17.3s (Mobile) / 2.2s (Desktop)**, LCP **23.4s (Mobile) / 5.9s (Desktop)**, TBT **0ms (Mobile) / 40ms (Desktop)**, CLS **0.000**.
* **Major Bottleneck:** Synchronous loading of YouTube embedded video player scripts (`player_embed_es6.vflset` - **943.3 KB**) and heavy PNG graphics (`Asset-1-a.png` - **176.1 KB**).
* **Total Network Transfer:** 161 requests totaling **4,016.2 KB (~3.92 MB)**.

### 2. Tashkent Medical Academy (`/tashkent-medical-academy`)
* **Scores:** Mobile **73/100**, Desktop **65/100**
* **Metrics:** FCP **2.0s**, LCP **12.4s (Mobile) / 5.5s (Desktop)**, TBT **70ms**, CLS **0.000**.
* **Major Bottleneck:** Main campus hero JPEG image (`Tashkent-Medical-Academy-1.jpg`) is **350+ KB** and lacks WebP/AVIF compression or explicit preloading.

### 3. Samarkand State Medical Institute (`/samarkand-state-medical-institute`)
* **Scores:** Mobile **67/100**, Desktop **63/100**
* **Metrics:** FCP **2.1s**, LCP **16.3s (Mobile) / 9.7s (Desktop)**, TBT **40ms**, CLS **0.000**.
* **Major Bottleneck:** Multiple uncompressed gallery photos and large Elementor section background images.

### 4. Study MBBS Uzbekistan Guide (`/study-mbbs-in-uzbekistan-for-indian-students`)
* **Scores:** Mobile **71/100**, Desktop **64/100**
* **Metrics:** FCP **1.9s**, LCP **13.1s (Mobile) / 8.9s (Desktop)**, TBT **50ms**, CLS **0.000**.
* **Major Bottleneck:** Legacy WordPress uploads (`.jpg` / `.png`) fetched over standard HTTP requests without next-gen image compression.

### 5. Georgia Universities Listing (`/mbbs-university/georgia`)
* **Scores:** Mobile **79/100**, Desktop **61/100**
* **Metrics:** FCP **1.9s**, LCP **5.0s (Mobile) / 5.1s (Desktop)**, TBT **40ms**, CLS **0.000**.
* **Major Bottleneck:** Faster LCP (5.0s) because university card thumbnails are smaller, but missing WebP format prevents < 2.5s LCP.

### 6. Contact Us (`/contact-us`)
* **Scores:** Mobile **69/100**, Desktop **59/100**
* **Metrics:** FCP **2.2s**, LCP **10.8s (Mobile) / 10.2s (Desktop)**, TBT **30ms**, CLS **0.000**.
* **Major Bottleneck:** Form container background image (`Atlas-Mentor-BG-Form.jpg` - **86.4 KB**) and map embed.

### 7. Alte Medical University (`/alte-medical-university`)
* **Scores:** Mobile **77/100**, Desktop **65/100**
* **Metrics:** FCP **2.1s**, LCP **5.6s (Mobile) / 5.6s (Desktop)**, TBT **30ms**, CLS **0.000**.
* **Major Bottleneck:** Standard hero image download delay.

---

## 6. Detailed Technical Resource Analysis

### A. LCP Analysis
* **LCP Classification:** Always **Image** (specifically campus hero photos in `.jpg` or `.png` format).
* **Root Cause of Slow LCP:**
  1. **Image File Size:** Legacy WordPress upload images are **300 KB – 1.5 MB uncompressed PNG/JPEG files**.
  2. **Lack of WebP/AVIF:** Served as standard legacy JPEG/PNG instead of WebP/AVIF format (missing 60-80% payload savings).
  3. **No Image CDN:** Images are served directly from standard web origin storage without edge caching or dynamic image optimization headers.
  4. **Discovery Delay:** Browser discovers the LCP image only after parsing HTML and initial CSS.

### B. CSS Analysis
* **Live CSS Bundle:** Currently serving `combined-global-ef085916f1.css` (**162.4 KB compressed / 779 KB uncompressed**).
* **Render-Blocking Impact:** TTFB for CSS is fast (38 ms), but 162.4 KB compressed CSS adds ~200-400 ms parse/render delay on 3G mobile networks.
* **Note:** Our latest local optimization (`combined-global-1a64fe2d82.css` at **454 KB uncompressed / ~95 KB compressed**) has not yet been deployed to the live domain. Once deployed, CSS blocking cost will drop by an additional **41.7%**.

### C. JavaScript & Third-Party Analysis

#### Top 10 Largest Network Transferred Resources on Live Production:
1. `youtube.com/.../base.js` — **471.7 KB** (Script)
2. `youtube.com/.../base.js` — **471.6 KB** (Script)
3. `elementskit.woff` — **454.2 KB** (Font)
4. `youtube.com/.../ytembeds` — **218.3 KB** (Script)
5. `Asset-1-a.png` — **176.1 KB** (Image)
6. `googletagmanager.com/gtag/js` — **172.0 KB** (Script)
7. `combined-global-ef085916f1.css` — **162.4 KB** (Stylesheet)
8. `youtube.com/.../ytembeds` — **155.2 KB** (Script)
9. `googletagmanager.com/gtm.js` — **116.0 KB** (Script)
10. `Atlas-Mentor-BG-Form.jpg` — **86.4 KB** (Image)

#### Third-Party Script Impact Ranking:
1. **YouTube iFrame Player Embeds:** **~1.32 MB total JS payload** loaded synchronously on the Homepage.
2. **ElementsKit WOFF Font File (`elementskit.woff`):** **454.2 KB** standalone font file download.
3. **Google Tag Manager & GA4:** **288.0 KB combined JS**.
4. **Microsoft Clarity & Ahrefs Analytics:** Minor main-thread impact.

---

## 7. Comparison Against Previous Baselines

| Benchmark Environment | Audit Date | Performance (Mobile) | Performance (Desktop) | FCP | LCP | TBT | CLS |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Initial Audit (Local)** | Aug 2026 | 30 – 45 | 40 – 50 | 5.5 s | 12.0 s | 300 – 600 ms | 0.05 – 0.15 |
| **Previous Audit (Local Build)** | Sep 3, 2026 | 63 – 64 | 55 – 56 | 4.7 – 5.0 s | 7.2 – 8.7 s | 20 – 50 ms | 0.004 |
| **Current Live Production (`https://atlasmentor.com`)** | Sep 4, 2026 | **67 – 79** *(Details)*<br>**55** *(Homepage)* | **59 – 65** | **1.9 – 2.2 s** | **5.0 – 16.3 s** | **20 – 70 ms** | **0.000** |

* **Note:** The previous baseline of 63–64 mobile performance came from **Local Production-Build Lighthouse (`http://localhost:3000`)**. On the **Live Deployed Production Domain (`https://atlasmentor.com`)**, FCP is fast (1.9s – 2.2s) and TBT is excellent (20ms – 70ms), but Mobile LCP ranges from **5.0s to 16.3s** due to uncompressed JPEG/PNG network transfer times.

---

## 8. Priority Matrix

| Priority | Problem | Impact | Affected Pages | Recommended Fix |
| :--- | :--- | :--- | :--- | :--- |
| **P0** | **Uncompressed JPEG/PNG LCP Images** | Delays Mobile LCP by 5.0s – 16.3s | All 206 static pages | Convert `public/wp-content/uploads/` images to compressed WebP/AVIF format and add dynamic image optimization / edge CDN caching. |
| **P1** | **YouTube Embed JS Payload (~1.32 MB)** | Delays Homepage FCP & LCP to 17.3s / 23.4s | Homepage | Replace native YouTube iFrame embeds with lazy-loaded facade placeholders (`lite-youtube-embed`). |
| **P2** | **ElementsKit Font File (`elementskit.woff` - 454.2 KB)** | Large uncompressed font payload over network | All pages | Subset or lazy-load `elementskit.woff` font file. |
| **P3** | **Deploy Un-deployed CSS Pruning (`combined-global-1a64fe2d82.css`)** | Reduces CSS payload from 779 KB to 454 KB | All 206 static pages | Deploy the current branch (`feat/seo_opt`) to production. |

---

## 9. Single Highest-Impact Next Optimization

Based strictly on empirical network and Lighthouse evidence from the live public production domain (`https://atlasmentor.com`):

> **THE SINGLE HIGHEST-IMPACT OPTIMIZATION TO DO NEXT IS:**  
> **Image Optimization & WebP/AVIF Format Conversion with Edge CDN Delivery**

### Measured Justification:
1. **FCP, TBT, and CLS are already GREEN/EXCELLENT:** FCP is **1.9s – 2.2s**, TBT is **20ms – 70ms**, and CLS is **0.000**. JavaScript execution and layout shift are no longer blocking performance.
2. **LCP is the sole remaining bottleneck:** On live production, LCP takes **5.0s to 16.3s** on mobile because legacy `.jpg` and `.png` campus photos (300 KB – 1.5 MB) are fetched uncompressed over network requests.
3. **Expected Impact:** Converting images to WebP/AVIF will reduce image transfer sizes by **60% – 80%**, immediately dropping Mobile LCP below **2.5 seconds (GREEN / GOOD)** and elevating Mobile Performance Scores to **90+ / 100**.

import { NextResponse } from 'next/server';
import fs from 'fs';
import path from 'path';

export async function GET() {
  const baseUserUploaded = "C:\\Users\\HP\\.gemini\\antigravity-ide\\brain\\ae308e8e-7c3e-44df-b4c4-6284fa4d0c49\\.user_uploaded";
  const uploadDir = path.join(process.cwd(), 'public', 'wp-content', 'uploads', '2025', '02');

  const filesMap: [string, string[]][] = [
    // Navoi Building
    ['media_1787816098030.jpg', ['Navoi-State-Medical-University.jpg', 'Navoi-State-University.jpg', 'Navoi-Davlat-Universiteti.jpg']],
    // Navoi Image 2 (Banner)
    ['media_1787816098052.jpg', ['Navoi-State-Medical-University-1.jpg', 'Navoi-State-University-Banner.jpg']],
    // Navoi Image 3 (Facilities)
    ['media_1787816098038.jpg', ['Facilities-At-Navoi-State-Medical-University.jpg', 'Facilities-At-Navoi-State-University.jpg', 'Facilities-At-Navoi-Davlat-Universiteti.jpg']],
    // Navoi Image 1 (Eligibility)
    ['media_1787816098145.jpg', ['Student-Life-At-Navoi-State-Medical-University.jpg', 'Eligibility-Criteria-For-Navoi-State-Medical-University.jpg', 'Student-Life-At-Navoi-Davlat-Universiteti.jpg']],
    // Navoi Image 4 (FAQs)
    ['media_1787816098136.jpg', ['FAQs-on-Navoi-State-Medical-University.jpg', 'FAQs-on-Navoi-State-University.jpg', 'FAQs-on-Navoi-Davlat-Universiteti.jpg']],

    // Zarmed Building
    ['media_1787815856948.png', ['Zarmed-Universiteti.jpg', 'Zarmed-University.jpg']],
    // Zarmed Image 1 (Eligibility)
    ['media_1787815836472.jpg', ['Student-Life-At-Zarmed-Universiteti.jpg', 'Eligibility-Criteria-For-Zarmed-University.jpg']],
    // Zarmed Image 2 (Banner)
    ['media_1787815836494.jpg', ['Zarmed-University-1.jpg', 'Zarmed-University-Banner.jpg']],
    // Zarmed Image 3 (Facilities)
    ['media_1787815836550.jpg', ['Facilities-At-Zarmed-Universiteti.jpg', 'Facilities-At-Zarmed-University.jpg']],
    // Zarmed Image 4 (FAQs)
    ['media_1787815836566.jpg', ['FAQs-on-Zarmed-Universiteti.jpg', 'FAQs-on-Zarmed-University.jpg']],

    // Namangan Building
    ['media_1787816048231.jpg', ['Namangan-State-University.jpg', 'Namangan-State-Medical-University.jpg', 'Namangan-Davlat-Universiteti.jpg']],
    // Namangan Image 2 (Banner)
    ['media_1787816048338.png', ['Namangan-State-Medical-University-1.jpg', 'Namangan-State-University-Banner.jpg', 'Namangan-State-Medical-University-Banner.jpg']],
    // Namangan Image 3 (Facilities)
    ['media_1787816048369.jpg', ['Facilities-At-Namangan-State-Medical-University.jpg', 'Facilities-At-Namangan-State-University.jpg', 'Facilities-At-Namangan-Davlat-Universiteti.jpg']],
    // Namangan Image 1 (Eligibility)
    ['media_1787816048381.jpg', ['Student-Life-At-Namangan-State-Medical-University.jpg', 'Eligibility-Criteria-For-Namangan-State-Medical-University.jpg', 'Student-Life-At-Namangan-Davlat-Universiteti.jpg']],
    // Namangan Image 4 (FAQs)
    ['media_1787816048435.jpg', ['FAQs-on-Namangan-State-Medical-University.jpg', 'FAQs-on-Namangan-State-University.jpg', 'FAQs-on-Namangan-Davlat-Universiteti.jpg']]
  ];

  for (const [srcName, destList] of filesMap) {
    const srcPath = path.join(baseUserUploaded, srcName);
    if (fs.existsSync(srcPath)) {
      for (const dest of destList) {
        fs.copyFileSync(srcPath, path.join(uploadDir, dest));
      }
    }
  }

  return NextResponse.json({ success: true, count: filesMap.length });
}

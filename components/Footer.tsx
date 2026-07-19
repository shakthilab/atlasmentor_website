import fs from 'fs';
import path from 'path';
import RichHtml from './RichHtml';

export default function Footer() {
  const footerHtmlPath = path.join(process.cwd(), 'data/globals/footer.html');
  const footerHtml = fs.readFileSync(footerHtmlPath, 'utf8');

  return <RichHtml html={footerHtml} />;
}

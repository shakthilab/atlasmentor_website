import fs from 'fs';
import path from 'path';

export default function Footer() {
  const footerHtmlPath = path.join(process.cwd(), 'data/globals/footer.html');
  const footerHtml = fs.readFileSync(footerHtmlPath, 'utf8');

  return (
    <div dangerouslySetInnerHTML={{ __html: footerHtml }} suppressHydrationWarning />
  );
}

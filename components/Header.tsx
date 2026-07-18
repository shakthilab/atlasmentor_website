import fs from 'fs';
import path from 'path';
import HeaderClient from './HeaderClient';

export default function Header() {
  const headerHtmlPath = path.join(process.cwd(), 'data/globals/header.html');
  const headerHtml = fs.readFileSync(headerHtmlPath, 'utf8');

  return (
    <>
      <style dangerouslySetInnerHTML={{ __html: `
        /* Enforce submenu dropdown visibility on hover for desktop/tablet screens */
        @media (min-width: 768px) {
          /* Prevent overflow clipping in the header and all its descendant containers */
          header.elementor-location-header,
          header.elementor-location-header *,
          .elementor-61,
          .elementor-61 * {
            overflow: visible !important;
          }

          /* Force display of submenu dropdowns on hover */
          .elementor-nav-menu li.menu-item-has-children:hover > ul.sub-menu,
          .elementor-nav-menu li.menu-item-has-children:focus-within > ul.sub-menu {
            display: block !important;
            opacity: 1 !important;
            visibility: visible !important;
          }
        }

        /* Align Register Now and Login buttons horizontally */
        .elementor-element.elementor-element-fea93ae {
          display: flex !important;
          flex-direction: row !important;
          align-items: center !important;
          justify-content: flex-end !important;
          gap: 12px !important;
          flex-wrap: nowrap !important;
        }

        /* Reset widget layout in this container */
        .elementor-element.elementor-element-fea93ae .elementor-widget-button {
          margin: 0 !important;
          width: auto !important;
        }

        /* Adjust widths on desktop to accommodate both buttons side-by-side */
        @media (min-width: 1025px) {
          .elementor-61 .elementor-element.elementor-element-fea93ae {
            --width: 25% !important;
            width: 25% !important;
          }
          .elementor-61 .elementor-element.elementor-element-764c114 {
            --width: 55% !important;
            width: 55% !important;
          }
        }

        @media (min-width: 768px) and (max-width: 1024px) {
          .elementor-61 .elementor-element.elementor-element-fea93ae {
            --width: 32% !important;
            width: 32% !important;
          }
          .elementor-61 .elementor-element.elementor-element-764c114 {
            --width: 48% !important;
            width: 48% !important;
          }
        }

        @media (max-width: 767px) {
          .elementor-61 .elementor-element.elementor-element-fea93ae {
            --width: 58% !important;
            width: 58% !important;
          }
          .elementor-61 .elementor-element.elementor-element-b5bc2e9 {
            --width: 30% !important;
            width: 30% !important;
          }
          .elementor-61 .elementor-element.elementor-element-764c114 {
            --width: 8% !important;
            width: 8% !important;
          }
        }

        /* Custom Styles for the Hollow/Ghost Login Button */
        .elementor-element-login-btn a.elementor-button {
          background-color: transparent !important;
          color: #de8017 !important;
          border: 2px solid #de8017 !important;
          padding: 10px 20px !important;
          border-radius: 5px !important;
          font-weight: 600 !important;
          transition: all 0.3s ease !important;
          display: inline-flex !important;
          align-items: center !important;
          justify-content: center !important;
          height: auto !important;
          line-height: 1 !important;
          text-decoration: none !important;
        }

        .elementor-element-login-btn a.elementor-button:hover {
          background-color: #de8017 !important;
          color: #ffffff !important;
          text-decoration: none !important;
        }

        /* Match typography and alignment for the Register Now button */
        .elementor-element-bd72c9e a.elementor-button {
          padding: 10px 20px !important;
          border-radius: 5px !important;
          font-weight: 600 !important;
          border: 2px solid transparent !important;
          display: inline-flex !important;
          align-items: center !important;
          justify-content: center !important;
          height: auto !important;
          line-height: 1 !important;
          text-decoration: none !important;
        }
      `}} />
      <div dangerouslySetInnerHTML={{ __html: headerHtml }} suppressHydrationWarning />
      <HeaderClient />
    </>
  );
}

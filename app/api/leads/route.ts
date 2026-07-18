import { NextResponse } from 'next/server';
import fs from 'fs';
import path from 'path';

// Helper to map raw form fields to clean Google Sheet headers
function getMappedPayload(formName: string, fields: Record<string, string>, url: string, timestamp: string) {
  let targetSheet = '';
  const payload: Record<string, string> = {
    'Timestamp': timestamp,
    'Page URL': url
  };

  // Safe checks for fields dictionary
  const safeFields = fields || {};

  if (formName === 'University Form') {
    targetSheet = 'University Form';
    payload['Name'] = safeFields['form_fields[name]'] || '';
    payload['Email'] = safeFields['form_fields[email]'] || '';
    payload['Mobile Number'] = safeFields['form_fields[field_f4cabbb]'] || '';
  } else if (formName === 'Admission Form') {
    // Detect popup vs homepage vs inner country pages
    if ('form_fields[field_6b7cd2c][]' in safeFields) {
      // Homepage version
      targetSheet = 'Admission Form (Homepage)';
      payload['Full Name'] = safeFields['form_fields[email]'] || ''; // Name is submitted under "email" key
      payload['Mobile Number'] = safeFields['form_fields[field_d414596]'] || '';
      payload['Email Address'] = safeFields['form_fields[field_171c35b]'] || '';
      payload['Preferred Country'] = safeFields['form_fields[field_e023343]'] || '';
      payload['Preferred University'] = safeFields['form_fields[field_55f4d96]'] || '';
      payload['Uploaded Files'] = safeFields['form_fields[field_6b7cd2c][]'] || '';
    } else if ('form_fields[field_d3c26c0]' in safeFields) {
      // Popup version (has city and state)
      targetSheet = 'Admission Form (Popup)';
      payload['Full Name'] = safeFields['form_fields[email]'] || '';
      payload['Mobile Number'] = safeFields['form_fields[field_d414596]'] || '';
      payload['Email Address'] = safeFields['form_fields[field_171c35b]'] || '';
      payload['NEET Marks'] = safeFields['form_fields[field_e023343]'] || '';
      payload['State'] = safeFields['form_fields[field_55f4d96]'] || '';
      payload['City'] = safeFields['form_fields[field_d3c26c0]'] || '';
    } else {
      // Inner Country Pages version
      targetSheet = 'Admission Form (Inner Country)';
      payload['Full Name'] = safeFields['form_fields[email]'] || '';
      payload['Mobile Number'] = safeFields['form_fields[field_d414596]'] || '';
      payload['Email Address'] = safeFields['form_fields[field_171c35b]'] || '';
      payload['Preferred Country'] = safeFields['form_fields[field_e023343]'] || '';
      payload['Preferred University'] = safeFields['form_fields[field_55f4d96]'] || '';
    }
  } else if (formName === 'Contact Form') {
    targetSheet = 'Contact Form';
    payload['Name'] = safeFields['form_fields[name]'] || '';
    payload['Phone'] = safeFields['form_fields[field_f77c348]'] || '';
    payload['Email'] = safeFields['form_fields[email]'] || '';
  } else if (formName === 'Footer Admission') {
    targetSheet = 'Footer Admission';
    payload['Full Name'] = safeFields['form_fields[email]'] || '';
    payload['Mobile Number'] = safeFields['form_fields[field_d414596]'] || '';
  }

  return { targetSheet, payload };
}

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const { formName, fields, url } = body;
    const timestamp = new Date().toISOString();

    // Output to console for server logging
    console.log('--- NEW LEAD RECEIVED ---');
    console.log('Form:', formName);
    console.log('URL:', url);
    console.log('Fields:', JSON.stringify(fields, null, 2));

    // Save lead to local JSON files inside workspace (local dev backup only).
    // This filesystem is read-only in production (e.g. Vercel serverless functions),
    // so failures here must never block the Google Sheets forward below.
    try {
      const leadsDir = path.join(process.cwd(), 'data/leads');
      if (!fs.existsSync(leadsDir)) {
        fs.mkdirSync(leadsDir, { recursive: true });
      }

      const leadPayload = {
        timestamp,
        formName,
        fields,
        url,
      };

      const filename = `lead_${Date.now()}_${Math.random().toString(36).substring(2, 7)}.json`;
      fs.writeFileSync(
        path.join(leadsDir, filename),
        JSON.stringify(leadPayload, null, 2),
        'utf8'
      );
    } catch (writeError) {
      console.warn('Skipping local lead backup (read-only filesystem?):', writeError);
    }

    // Google Sheets Integration (Forwarding)
    const scriptUrl = process.env.GOOGLE_SCRIPT_URL;
    const { targetSheet, payload } = getMappedPayload(formName, fields, url, timestamp);

    if (scriptUrl && targetSheet) {
      try {
        console.log(`Forwarding lead to Google Sheets target tab: "${targetSheet}"...`);
        const sheetsResponse = await fetch(scriptUrl, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            targetSheet,
            payload,
          }),
        });

        if (!sheetsResponse.ok) {
          console.error(`Google Sheets Web App returned status ${sheetsResponse.status}`);
        } else {
          const resJson = await sheetsResponse.json();
          if (resJson.success) {
            console.log('Successfully saved lead to Google Sheet.');
          } else {
            console.error('Failed to save lead to Google Sheet:', resJson.error);
          }
        }
      } catch (sheetError) {
        console.error('Error forwarding lead to Google Sheets:', sheetError);
      }
    } else {
      if (!scriptUrl) {
        console.log('GOOGLE_SCRIPT_URL environment variable is not defined. Skipping Google Sheets sync.');
      } else if (!targetSheet) {
        console.warn(`Form "${formName}" could not be mapped to a target Google Sheet tab.`);
      }
    }

    return NextResponse.json({ success: true, message: 'Lead captured successfully!' });
  } catch (error) {
    console.error('Error handling lead submission:', error);
    return NextResponse.json(
      { success: false, message: 'Internal server error occurred.' },
      { status: 500 }
    );
  }
}


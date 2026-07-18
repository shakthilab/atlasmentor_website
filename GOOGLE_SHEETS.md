# Google Sheets Form Integration Reference

This document serves as a permanent reference for the Google Sheets form submission integration on this website.

## Deployment Details

* **Google Sheet Link**: [Atlas Mentor Spreadsheet](https://docs.google.com/spreadsheets/d/1uUaQNVFHhFatp4He_pkxVFET48Mbz5O8Nx__nqjFjLc/edit)
* **Web App URL**: `https://script.google.com/macros/s/AKfycbwMWFZ4QytZvbudnANERrv_iP0BYziUPNqwhQ6CYRGadJH9mdAItXPSk-iX0AB_GD34ag/exec`
* **Deployment ID**: `AKfycbwMWFZ4QytZvbudnANERrv_iP0BYziUPNqwhQ6CYRGadJH9mdAItXPSk-iX0AB_GD34ag`
* **Library URL**: `https://script.google.com/macros/library/d/1j1d3HKi6Mz2T6H2P4SVEI7uqJpT30ZgliyMWROb0FZSqLm49wejDN80y/2`

## Architecture & Data Flow

1. **Frontend Form Submission**: The client-side handler in `components/FormHandlerClient.tsx` captures all submissions from the form templates (Elementor HTML markup) and POSTs them to the backend API route `/api/leads/`.
2. **Backend API Normalization**: The API route in `app/api/leads/route.ts` identifies the source form and maps raw, system-generated fields (like `form_fields[field_d414596]`) to clean, human-readable column headers (like `Mobile Number`).
3. **Data Logging & Forwarding**:
   * Saves a backup JSON payload locally under `data/leads/`.
   * Sends the structured payload to the Web App URL configured in your `.env.local` file under `GOOGLE_SCRIPT_URL`.
4. **Google Sheets Storage**: The Google Apps Script receives the structured payload and appends the row to the corresponding sheet tab.

## Configured Sheets and Columns

The system writes data to 6 separate tabs in the Google Sheet:

1. **`University Form`**
   * Columns: `Timestamp`, `Page URL`, `Name`, `Email`, `Mobile Number`
2. **`Admission Form (Homepage)`**
   * Columns: `Timestamp`, `Page URL`, `Full Name`, `Mobile Number`, `Email Address`, `Preferred Country`, `Preferred University`, `Uploaded Files`
3. **`Admission Form (Inner Country)`**
   * Columns: `Timestamp`, `Page URL`, `Full Name`, `Mobile Number`, `Email Address`, `Preferred Country`, `Preferred University`
4. **`Admission Form (Popup)`**
   * Columns: `Timestamp`, `Page URL`, `Full Name`, `Mobile Number`, `Email Address`, `NEET Marks`, `State`, `City`
5. **`Contact Form`**
   * Columns: `Timestamp`, `Page URL`, `Name`, `Phone`, `Email`
6. **`Footer Admission`**
   * Columns: `Timestamp`, `Page URL`, `Full Name`, `Mobile Number`

## Email Notifications

Whenever a lead is processed by the Apps Script, an HTML notification is sent instantly to `info.atlasmentor@yopmail.com` containing:
* Form Name
* Page URL of submission
* Mapped fields and values in a table layout

---

## Google Apps Script Code

This is the code currently deployed on the spreadsheet to manage the database insertion and email forwarding:

```javascript
const SHEETS_CONFIG = {
  "University Form": ["Timestamp", "Page URL", "Name", "Email", "Mobile Number"],
  "Admission Form (Homepage)": ["Timestamp", "Page URL", "Full Name", "Mobile Number", "Email Address", "Preferred Country", "Preferred University", "Uploaded Files"],
  "Admission Form (Inner Country)": ["Timestamp", "Page URL", "Full Name", "Mobile Number", "Email Address", "Preferred Country", "Preferred University"],
  "Admission Form (Popup)": ["Timestamp", "Page URL", "Full Name", "Mobile Number", "Email Address", "NEET Marks", "State", "City"],
  "Contact Form": ["Timestamp", "Page URL", "Name", "Phone", "Email"],
  "Footer Admission": ["Timestamp", "Page URL", "Full Name", "Mobile Number"]
};

// HTTP POST Handler for Lead Submissions
function doPost(e) {
  try {
    const data = JSON.parse(e.postData.contents);
    const { targetSheet, payload } = data;
    
    const ss = SpreadsheetApp.getActiveSpreadsheet();
    let sheet = ss.getSheetByName(targetSheet);
    
    if (!sheet) {
      return ContentService.createTextOutput(JSON.stringify({ 
        success: false, 
        error: "Sheet not found: " + targetSheet 
      })).setMimeType(ContentService.MimeType.JSON);
    }
    
    // Get headers to write data to correct columns
    const headers = sheet.getRange(1, 1, 1, sheet.getLastColumn()).getValues()[0];
    const newRow = new Array(headers.length).fill("");
    
    for (let i = 0; i < headers.length; i++) {
      const header = headers[i];
      if (payload.hasOwnProperty(header)) {
        newRow[i] = payload[header];
      }
    }
    
    // 1. Save to Google Sheets
    sheet.appendRow(newRow);
    
    // 2. Send email notification
    sendNotificationEmail(targetSheet, payload);
    
    return ContentService.createTextOutput(JSON.stringify({ success: true }))
      .setMimeType(ContentService.MimeType.JSON);
      
  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({ 
      success: false, 
      error: err.toString() 
    })).setMimeType(ContentService.MimeType.JSON);
  }
}

// Helper to construct and send HTML email notifications
function sendNotificationEmail(formName, payload) {
  const recipient = "info.atlasmentor@yopmail.com";
  const subject = "New Lead Received - " + formName;
  
  let htmlTableRows = "";
  for (const [key, value] of Object.entries(payload)) {
    htmlTableRows += `
      <tr style="border-bottom: 1px solid #dddddd;">
        <td style="padding: 12px 15px; font-weight: bold; background-color: #f8f9fa; width: 30%; border: 1px solid #dee2e6;">${key}</td>
        <td style="padding: 12px 15px; border: 1px solid #dee2e6;">${value || "<i>(not provided)</i>"}</td>
      </tr>
    `;
  }

  const htmlBody = `
    <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; color: #333333;">
      <h2 style="color: #0056b3; border-bottom: 2px solid #0056b3; padding-bottom: 8px;">New Form Submission</h2>
      <p>A new form has been submitted on the website. Here are the details:</p>
      
      <table style="width: 100%; border-collapse: collapse; margin-top: 15px; font-size: 14px; text-align: left; border: 1px solid #dee2e6;">
        <thead>
          <tr style="background-color: #0056b3; color: white;">
            <th style="padding: 12px 15px; border: 1px solid #dee2e6;">Field</th>
            <th style="padding: 12px 15px; border: 1px solid #dee2e6;">Value</th>
          </tr>
        </thead>
        <tbody>
          ${htmlTableRows}
        </tbody>
      </table>
      
      <p style="font-size: 12px; color: #666666; margin-top: 30px; border-top: 1px solid #dee2e6; padding-top: 10px;">
        This email was automatically sent from the Google Sheets Lead Integration system.
      </p>
    </div>
  `;

  MailApp.sendEmail({
    to: recipient,
    subject: subject,
    htmlBody: htmlBody
  });
}

// Run this function in the editor to authorize email permissions
function testEmail() {
  sendNotificationEmail("Test Form Verification", {
    "Timestamp": new Date().toISOString(),
    "Name": "Jane Doe",
    "Email": "info.atlasmentor@yopmail.com",
    "Status": "Permission verified successfully!"
  });
}
```


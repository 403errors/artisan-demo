<!-- trace fix verification -->
# artisan-demo

Throwaway demo repository used to exercise Artisan's autonomous issue → PR loop
for the All Things Agentic Hackathon 2026 submission.

Not a real application — file an issue here to trigger Artisan's Gate 1
(Intake) and Gate 2 (Plan → Execute → Verify → PR) pipeline.

## Landing Page

This repository includes a structured static landing page (`index.html`) with comprehensive HTML5 metadata and semantic sections detailing the Artisan autonomous engineering system.

### Page Structure & Content

- **Metadata**: Includes charset encoding, responsive viewport configurations, and descriptive search/social metadata.
- **Header**: Features the All Things Agentic Hackathon badge, main title ("Artisan Demo"), and tagline.
- **Project Overview**: Introduces Artisan's autonomous issue-to-PR agent system and purpose.
- **Autonomous Pipeline Architecture**: Outlines the multi-gate lifecycle including Gate 1 (Intake & Triage) and Gate 2 (Planning, Execution, Verification & PR).
- **Technology Stack**: Details the underlying technologies, including Google Gemini models and Google Cloud Vertex AI infrastructure.
- **Presentation & Demonstration Details**: Explains the live end-to-end hackathon demonstration flow.
- **Footer**: Contains event attribution and Gemini / Vertex AI credits.

### How to View

You can view the landing page locally by opening `index.html` in any modern web browser, or by serving it with a simple static file server:

```bash
# Using Python
python3 -m http.server 8000

# Using Node.js (npx)
npx serve .
```

Then open `http://localhost:8000` (or the URL printed by your server) in your browser.

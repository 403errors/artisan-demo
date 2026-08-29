<!-- trace diagnostic test -->

# artisan-demo

Throwaway demo repository used to exercise Artisan's autonomous issue → PR loop
for the All Things Agentic Hackathon 2026 submission.

Not a real application — file an issue here to trigger Artisan's Gate 1
(Intake) and Gate 2 (Plan → Execute → Verify → PR) pipeline.

## Landing Page

This repository includes a static landing page (`index.html`) featuring an "Artisan Demo" header, "Powered by Gemini and Vertex AI" tagline, and centered styling with readable typography.

### How to View

You can view the landing page locally by opening `index.html` in any modern web browser, or by serving it with a simple static file server:

```bash
# Using Python
python3 -m http.server 8000

# Using Node.js (npx)
npx serve .
```

Then open `http://localhost:8000` (or the URL printed by your server) in your browser.

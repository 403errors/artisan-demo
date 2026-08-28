# artisan-demo

Throwaway demo repository used to exercise Artisan's autonomous issue → PR loop
for the All Things Agentic Hackathon 2026 submission.

Not a real application — file an issue here to trigger Artisan's Gate 1
(Intake) and Gate 2 (Plan → Execute → Verify → PR) pipeline.

## Landing Page

This repository includes a minimal, responsive static landing page (`index.html`) featuring the Artisan Demo hero section and tagline highlighting the autonomous multi-agent GitHub and Jira automation system.

### Viewing the Landing Page

You can view the static landing page in any web browser using one of the following methods:

1. **Directly in Browser:**
   Open `index.html` directly in your favorite browser:
   ```bash
   open index.html        # macOS
   xdg-open index.html    # Linux
   start index.html       # Windows
   ```

2. **Using a Local Static Server:**
   Start a lightweight HTTP server using Python:
   ```bash
   python3 -m http.server 8000
   ```
   Then navigate to `http://localhost:8000` in your browser.

### Running Tests

To verify the HTML structure, accessibility tags, and CSS styles:
```bash
python3 -m unittest discover -v
```

# artisan-demo

> Autonomous Issue &rarr; PR Loop Demonstration for the All Things Agentic Hackathon 2026

**artisan-demo** is a demonstration repository used to exercise and showcase **Artisan**, an autonomous coding agent pipeline powered by **Google Gemini** and **Vertex AI**.

---

## 📌 Overview

This repository is designed to demonstrate end-to-end autonomous software development workflows:
- **Autonomous Lifecycle**: Automatically responds to GitHub issues, triages them, generates implementation plans, edits code, verifies changes, and submits ready-to-review Pull Requests.
- **Powered by Gemini & Vertex AI**: Leverages Google's foundation models via Vertex AI to reason through issue descriptions and apply code modifications.
- **Hackathon Showcase**: Built for the *All Things Agentic Hackathon 2026*.

---

## ⚙️ How It Works

Artisan processes repository issues through a two-stage gated architecture:

```text
+-------------------------------------------------------------------+
|                        GitHub Issue Created                       |
+-------------------------------------------------------------------+
                                  │
                                  ▼
+-------------------------------------------------------------------+
|                     Gate 1: Intake & Triage                       |
|   • Validate issue description and context                        |
|   • Assess feasibility and security boundaries                    |
+-------------------------------------------------------------------+
                                  │
                                  ▼
+-------------------------------------------------------------------+
|                  Gate 2: Autonomous Execution                     |
|   1. Plan    - Analyze codebase and draft step-by-step changes     |
|   2. Execute - Apply edits across designated repository files     |
|   3. Verify  - Run linters, tests, and syntax validations         |
|   4. PR      - Open Pull Request with detailed change summary     |
+-------------------------------------------------------------------+
```

---

## 📁 Repository Structure

```text
artisan-demo/
├── README.md       # Project documentation and architectural overview
└── index.html      # Static landing page showcasing the Artisan demo
```

---

## 🚀 Getting Started

### Prerequisites
- A modern web browser (Chrome, Firefox, Safari, Edge)
- Optional: Python 3 or Node.js (for running a local HTTP server)

### Viewing the Landing Page Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/403errors/artisan-demo.git
   cd artisan-demo
   ```

2. **Open directly in a browser:**
   - On macOS: `open index.html`
   - On Linux: `xdg-open index.html`
   - On Windows: `start index.html`

3. **Or serve via a local static web server:**

   *Using Python 3:*
   ```bash
   python3 -m http.server 8000
   ```

   *Using Node.js (`npx`):*
   ```bash
   npx serve .
   ```

   Navigate to `http://localhost:8000` in your web browser.

---

## 🛠️ Triggering the Artisan Workflow

To trigger Artisan on this repository:
1. Navigate to the **Issues** tab on GitHub.
2. Create a new issue detailing a bug fix, feature request, or documentation update.
3. Artisan's automated pipeline will trigger Gate 1 (Intake) and proceed through Gate 2 to generate a Pull Request.

---

## 📄 License

This demo project is open-source and available under the terms of the project repository.

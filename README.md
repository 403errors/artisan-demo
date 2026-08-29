<!-- trace fix verification -->
# Artisan Demo

Throwaway demo repository used to exercise Artisan's autonomous issue → PR loop for the All Things Agentic Hackathon 2026 submission.

Powered by Gemini and Vertex AI.

---

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Installation & Setup](#installation--setup)
  - [Running the Local Server](#running-the-local-server)
- [Usage](#usage)
  - [Viewing the Landing Page](#viewing-the-landing-page)
  - [Triggering the Autonomous Agent Pipeline](#triggering-the-autonomous-agent-pipeline)
- [Project Structure](#project-structure)
- [Documentation & Workflow](#documentation--workflow)
- [Contributing & Feedback](#contributing--feedback)

---

## Overview

Artisan is an autonomous coding agent pipeline designed to turn GitHub issues into verified pull requests without human intervention. This repository (`artisan-demo`) serves as a testing and demonstration environment for the hackathon submission.

When an issue is filed in this repository, Artisan activates its multi-gate workflow:
1. **Gate 1 (Intake & Triage):** Analyzes the issue description, clarifies requirements, and plans implementation.
2. **Gate 2 (Plan → Execute → Verify → PR):** An agent checks out a branch, writes code and tests, runs verifications, and creates a pull request.

The repository includes a clean, responsive landing page (`index.html`) demonstrating the project identity and documentation entry points.

---

## Prerequisites

To view and work with this repository locally, you will need:

- A modern web browser (e.g., Chrome, Firefox, Safari, Edge)
- **Git** (for version control and repository management)
- *(Optional)* **Python 3.x** or **Node.js** (to run a local static HTTP server)

---

## Getting Started

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/artisan-agent/artisan-demo.git
   cd artisan-demo
   ```

2. **Verify the files:**
   Ensure `index.html` and `README.md` are present in the project directory.

### Running the Local Server

You can view the static landing page directly in your browser or run a lightweight HTTP server:

#### Option 1: Direct File Access
Open `index.html` directly in any web browser or use the command line:
```bash
# macOS
open index.html

# Linux
xdg-open index.html

# Windows
start index.html
```

#### Option 2: Python HTTP Server
```bash
python3 -m http.server 8000
```
Then navigate to [http://localhost:8000](http://localhost:8000) in your browser.

#### Option 3: Node.js / npx serve
```bash
npx serve .
```
Then navigate to the URL displayed in your terminal (typically [http://localhost:3000](http://localhost:3000) or [http://localhost:5000](http://localhost:5000)).

---

## Usage

### Viewing the Landing Page
The landing page (`index.html`) provides a user-friendly overview of the Artisan project, documentation links, and quick-start instructions.

### Triggering the Autonomous Agent Pipeline
To test Artisan's issue-to-PR automation:
1. Navigate to the **Issues** tab in this repository.
2. Create a new issue describing a bug fix, feature request, or documentation update.
3. Artisan's webhook will trigger Gate 1 (Intake) and Gate 2 (Execution), resulting in an autonomous PR opened with verified changes.

---

## Project Structure

```text
artisan-demo/
├── README.md          # Comprehensive project documentation and guide
└── index.html         # Responsive landing page with documentation links
```

### File Breakdown

- **`README.md`**: Main repository documentation detailing the project purpose, architecture, setup instructions, and usage guidelines.
- **`index.html`**: Clean, accessible static landing page highlighting project overview, features, and quick links.

---

## Documentation & Workflow

### Autonomous Pipeline Overview

```text
[ Issue Created ]
       │
       ▼
[ Gate 1: Intake & Triage ] ──► Clarify scope & formulate plan
       │
       ▼
[ Gate 2: Execution ]       ──► Implement changes & run verification
       │
       ▼
[ Pull Request Created ]    ──► Ready for review and merge
```

For more details on Artisan's architecture and AI agent configurations, see the project documentation links provided in `index.html`.

---

## Contributing & Feedback

This is a demo repository for the All Things Agentic Hackathon 2026. Feel free to open issues or explore pull requests created by the Artisan agent.

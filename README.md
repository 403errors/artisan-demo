<!-- trace fix verification -->
# Artisan Demo

> Autonomous Issue &rarr; PR Pipeline powered by Gemini and Vertex AI for the **All Things Agentic Hackathon 2026**.

Artisan is an autonomous software engineering agent system designed to convert user-reported GitHub issues into verified, high-quality pull requests without human intervention. This repository serves as a live demonstration testbed to showcase and exercise the end-to-end autonomous engineering loop.

---

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Pipeline Architecture](#pipeline-architecture)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Getting Started & Setup](#getting-started--setup)
- [Usage & Demo Flow](#usage--demo-flow)
- [Technology Stack](#technology-stack)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

---

## Overview

The **Artisan Demo** repository demonstrates the capabilities of autonomous AI agents in standard software engineering workflows. When an issue is opened in this repository, Artisan's multi-gate pipeline initiates an automated loop:

1. **Gate 1 (Intake & Triage)**: Evaluates the issue, checks reproducibility, and defines clear acceptance criteria.
2. **Gate 2 (Plan, Execute & Verify)**: Formulates an implementation plan, performs targeted code modifications, validates changes against requirements, and automatically submits a pull request for review.

In addition to serving as an agent target repository, this project includes a responsive static landing page (`index.html`) detailing the project architecture, features, and presentation details.

---

## Key Features

- **End-to-End Autonomous Issue Resolution**: Seamless transition from issue creation to tested, ready-to-merge Pull Requests.
- **Multi-Gate Quality Assurance**: Dual-gate pipeline ensuring thorough intake validation, step-by-step planning, strict code execution, and post-execution verification.
- **Gemini & Vertex AI Integration**: Powered by Google's Gemini models hosted on enterprise-grade Vertex AI infrastructure for contextual code comprehension and planning.
- **Interactive Landing Page**: Built with clean, semantic HTML5 and modern CSS (`index.html`) featuring responsive layouts, component cards, and metadata.
- **Zero-Dependency Lightweight Setup**: Requires no complex build tools or heavy runtimes—runs instantly in any browser or minimal static server.

---

## Pipeline Architecture

The Artisan agent operates through a structured multi-gate architecture:

```
┌─────────────────┐       ┌────────────────────────┐       ┌────────────────────────┐       ┌──────────────────────┐
│  GitHub Issue   │ ────> │  Gate 1: Intake/Triage │ ────> │ Gate 2: Plan & Execute │ ────> │ Gate 2: Verify & PR  │
│  Filed by User  │       │  Validate & Specify    │       │ Apply Code & Doc Edits │       │ Open Pull Request    │
└─────────────────┘       └────────────────────────┘       └────────────────────────┘       └──────────────────────┘
```

### Gate 1: Intake & Triage
- Analyzes the issue description, reproduction steps, and expected behavior.
- Verifies problem validity and establishes acceptance criteria.
- Gates invalid, vague, or out-of-scope issues prior to code generation.

### Gate 2: Planning, Execution & Verification
- **Planning**: Generates an actionable, ordered implementation plan detailing target files, test cases, and documentation changes.
- **Execution**: The autonomous coding agent applies incremental modifications to source files, tests, and documentation.
- **Verification**: Executes syntax checks, markup validation, and test suites to verify system integrity before opening a Pull Request.

---

## Project Structure

```text
artisan-demo/
├── .git/               # Git version control metadata
├── index.html          # Semantic HTML5 landing page describing the Artisan architecture
└── README.md           # Comprehensive project documentation and developer guide
```

### File Details

- **`index.html`**: A static, standalone landing page built with semantic HTML5 and responsive CSS. It details the project overview, multi-gate architecture, technology stack, and hackathon presentation flow.
- **`README.md`**: Complete project documentation covering features, architecture, setup instructions, usage, and contribution guidelines.

---

## Prerequisites

To view and work with this project locally, you only need:

- A modern web browser (e.g., Google Chrome, Mozilla Firefox, Safari, Microsoft Edge).
- *(Optional)* A lightweight HTTP server runtime:
  - **Python** 3.x (comes pre-installed on most Linux/macOS systems), or
  - **Node.js** (v14+ with `npx`).

---

## Getting Started & Setup

### 1. Clone the Repository

Clone the repository to your local environment:

```bash
git clone https://github.com/artisan-demo/artisan-demo.git
cd artisan-demo
```

### 2. View the Landing Page Locally

You can view the static landing page (`index.html`) using any of the following methods:

#### Option A: Open directly in your browser
Simply open the `index.html` file in your preferred web browser:
- **macOS**: `open index.html`
- **Linux**: `xdg-open index.html`
- **Windows**: `start index.html`

#### Option B: Run a local HTTP server with Python
```bash
python3 -m http.server 8000
```
Then visit `http://localhost:8000` in your browser.

#### Option C: Run a local HTTP server with Node.js
```bash
npx serve .
```
Then visit `http://localhost:3000` (or the port specified in terminal output).

---

## Usage & Demo Flow

### Triggering the Autonomous Agent Loop

1. **File an Issue**: Navigate to the Issues tab in this repository and create a new issue describing a feature request, bug fix, or documentation update.
2. **Autonomous Intake (Gate 1)**: Artisan ingests the issue via webhooks, performs initial triage, and approves valid requests.
3. **Planning & Execution (Gate 2)**: Artisan's coding agent drafts an implementation plan and makes the necessary code/documentation changes on a working branch.
4. **Verification & PR Submission**: Artisan validates the edits and opens an automated Pull Request linked back to the original issue.

---

## Technology Stack

- **LLM & Reasoning Engine**: [Google Gemini](https://deepmind.google/technologies/gemini/)
- **AI Infrastructure**: [Google Cloud Vertex AI](https://cloud.google.com/vertex-ai)
- **Agent Framework**: Artisan Multi-Gate Autonomous Engineering Agent
- **Frontend**: Semantic HTML5, Modern Responsive CSS
- **Version Control & CI/CD**: GitHub Issues & Pull Requests

---

## Contributing

Contributions, feedback, and issue submissions are welcome! To contribute:

1. **Submit an Issue**: File an issue detailing bug reports or feature enhancements to test the Artisan autonomous loop.
2. **Manual Contributions**:
   - Fork the repository.
   - Create a feature branch (`git checkout -b feature/my-feature`).
   - Commit your changes (`git commit -m "Add feature description"`).
   - Push to your branch (`git push origin feature/my-feature`).
   - Open a Pull Request describing your changes.
3. **Code & Markdown Standards**:
   - Keep `index.html` valid, accessible HTML5 with clean embedded CSS.
   - Ensure all markdown files conform to standard Markdown syntax and relative links remain valid.

---

## Acknowledgments

- Built for the **All Things Agentic Hackathon 2026**.
- Powered by **Google Gemini** and **Google Cloud Vertex AI**.

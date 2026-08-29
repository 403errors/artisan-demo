# Contributing to Artisan Demo

Thank you for your interest in contributing to the Artisan Demo project! This guide outlines the developer workflow, setup instructions, branching conventions, and pull request guidelines to help you get started.

---

## Prerequisites

Before contributing, ensure you have the following tools installed on your system:

- **Git**: For version control.
- **Web Browser**: Any modern web browser (e.g., Chrome, Firefox, Safari, Edge) to preview the landing page.
- **Python 3** (recommended) or **Node.js**: To serve the static files locally.

---

## Local Setup

1. **Fork and clone the repository**:
   ```bash
   git clone https://github.com/<your-username>/artisan-demo.git
   cd artisan-demo
   ```

2. **Run a local development server**:
   You can serve the static files using either Python or Node.js:

   - Using Python 3:
     ```bash
     python3 -m http.server 8000
     ```
   - Using Node.js:
     ```bash
     npx serve .
     ```

3. **View the site**:
   Open your browser and navigate to `http://localhost:8000` (or the URL output by your server).

---

## Branching Strategy

When working on changes, please follow these branch naming conventions:

- `feature/<feature-name>`: For new features or enhancements.
- `fix/<bug-name>`: For bug fixes and corrections.
- `docs/<doc-name>`: For documentation updates or additions.
- `chore/<chore-name>`: For maintenance, refactoring, or tooling updates.

Create and switch to your branch:
```bash
git checkout -b feature/your-feature-name
```

---

## Commit Message Standards

We encourage clear, concise, and structured commit messages following the [Conventional Commits](https://www.conventionalcommits.org/) specification:

- `feat:` A new feature or capability
- `fix:` A bug fix
- `docs:` Documentation-only changes
- `style:` Formatting or style adjustments that do not affect code logic
- `refactor:` Code changes that neither fix bugs nor add features
- `test:` Adding or updating tests
- `chore:` Changes to build process, tools, or auxiliary files

**Example format**:
```text
feat: add responsive navigation menu

- Add mobile drawer menu component
- Include toggle button with accessible ARIA attributes
```

---

## Testing & Verification Guidelines

Before submitting your changes, verify that:

- **Browser Rendering**: Open `index.html` across different screen resolutions (mobile, tablet, desktop) to ensure responsive layout behavior.
- **HTML & CSS Validation**: Ensure standard HTML5 syntax and clean, maintainable CSS formatting.
- **Link Integrity**: Verify that all relative links (e.g., in documentation) and external URLs resolve correctly.

---

## Pull Request Submission

1. **Push your changes** to your forked repository:
   ```bash
   git push origin <branch-name>
   ```

2. **Open a Pull Request**:
   - Navigate to the repository on GitHub and click **New Pull Request**.
   - Provide a descriptive title following our commit conventions.
   - Include a clear summary of what was changed and why.
   - Note any testing or verification steps you performed.

3. **Review Process**:
   - Automated checks and reviewer feedback will be provided on the PR.
   - Address any requested changes by pushing additional commits to your branch.

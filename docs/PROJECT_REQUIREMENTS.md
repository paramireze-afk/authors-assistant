# Project Requirements

## Vision

Author's Assistant is a local-first Markdown knowledge and writing environment.

Its purpose is to help an author collect research, organize knowledge, draft
articles, revise writing, and publish higher-quality work while keeping the
author in control of the creative process.

Markdown files are the project's primary source of truth.

---

# Core Principles

- Local-first.
- Markdown-first.
- AI assists the author; it does not replace the author.
- Human review is always required before publication.
- Prompts remain separate from application code.
- The project should remain simple, understandable, and easy to maintain.

---

# Current Capabilities

The application should support workflows such as:

- revising Markdown documents
- drafting new content
- organizing research notes
- maintaining a personal knowledge base
- reusable prompt templates
- AI-assisted editing
- article preparation

These workflows share the same foundation: local Markdown files, reusable
prompts, and author-reviewed AI assistance.

---

# Baseline Revision Workflow

The baseline revision workflow should:

1. Accept a Markdown file.
2. Load the author's writing style.
3. Load editing rules.
4. Load the selected prompt.
5. Send the assembled prompt to an AI model.
6. Produce a revised Markdown document.
7. Never overwrite the original document.

This baseline remains important, but it now operates as one workflow inside a
broader authoring and knowledge system.

---

# Non-Goals

The project intentionally avoids unnecessary complexity.

The application should not require:

- a database
- user accounts
- a web server
- cloud storage
- a graphical interface
- automatic publishing
- automatic editing without review

---

# Future Direction

Possible future capabilities include:

- multiple AI providers
- multiple editing modes
- repository-wide knowledge search
- semantic note linking
- article generation
- research assistance
- citation management
- fact-checking workflows
- source attribution
- document comparison (diffs)
- Substack publishing
- VS Code integration
- reusable writing workflows
- project templates

Future features should remain modular and should not compromise the project's
local-first philosophy.

Development should remain incremental: strengthen existing workflows first,
then add clearly justified capabilities.
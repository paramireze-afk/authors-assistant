# 002 – Knowledge Harvesting Workflow

## Goal

Build a reusable Markdown knowledge base that will eventually serve as context for AI-assisted article writing.

This is **not** an article-writing workflow.

This phase is strictly about harvesting information from specialized sources and organizing it into reusable Markdown documents.

---

# Repository Philosophy

The repository is Markdown-first.

Every document should be useful as standalone context that can later be retrieved automatically by an AI.

Think of the repository as a collection of canonical reference documents rather than articles.

---

# Current Data Source

The current source is:

https://whokilledck.com/explorer/chat

This source contains a unique dataset surrounding the Charlie Kirk investigation.

The objective is to preserve that information inside our own repository.

---

# Harvest Workflow

For each Markdown file:

1. Choose one existing Markdown file.
2. Ask the investigation chatbot to populate only that file.
3. Copy the response into the repository.
4. Save.
5. Move immediately to the next file.

Do **not** spend time polishing prose.

Do **not** fact-check every statement.

Do **not** reorganize the repository.

Capture first.
Curate later.

---

# AI Responsibilities

The investigation chatbot is responsible for:

- harvesting information
- producing Markdown
- expanding existing files
- suggesting future documents

The chatbot should not redesign the repository.

---

GitHub Copilot is responsible for:

- maintaining repository structure
- creating new Markdown files
- fixing links
- renaming files
- extracting duplicated sections
- improving formatting
- helping automate repetitive tasks

Copilot should never rewrite harvested information unless explicitly requested.

---

# Current Phase

We are currently in the **Knowledge Harvesting** phase.

The priority is breadth rather than perfection.

A repository with fifty good documents is more valuable than five perfect ones.

---

# Guiding Principle

Capture now.

Curate later.

---

# Future Phases

Phase 1
- Harvest information

Phase 2
- Normalize document structure
- Remove duplication
- Improve cross references

Phase 3
- Add metadata
- Improve retrieval
- Build OpenAI context selection

Phase 4
- Generate articles from the knowledge base.

---

# Success Criteria

A successful harvesting session results in:

- one more completed Markdown document
- no unnecessary refactoring
- no scope creep

Steady accumulation of reusable knowledge is the primary objective.
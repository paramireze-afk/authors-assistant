# Copilot Context

## Project

Author's Assistant is a local-first Markdown authoring and knowledge
management system supported by small TypeScript tools and reusable prompts.

It helps an author research, organize knowledge, draft and revise writing, and
prepare publishable Markdown while keeping decisions in the author's hands.

The project is intentionally local-first. Markdown files are the source of
truth. AI assists the author but does not replace author judgment.

For deeper design rationale, see `docs/ARCHITECTURE.md`.

## Development Philosophy

- Keep the implementation small and understandable.
- Favor readability over cleverness.
- Build one feature at a time.
- Prefer simple solutions over abstractions.
- Do not introduce frameworks unless clearly justified.
- Do not introduce a database.
- Keep prompts separate from application code.
- Handle errors clearly and predictably.
- Explain meaningful implementation decisions.
- Preserve backwards compatibility whenever practical.

## Project Principles

- Markdown files are the primary data format.
- Never overwrite source documents unless explicitly instructed.
- Generate new files instead of modifying originals whenever possible.
- Keep documentation synchronized with implementation.
- Small, reviewable commits are preferred over large rewrites.
- Avoid speculative features. Build only what is currently needed.

## AI Collaboration

When implementing a feature:

1. Understand the existing architecture before making changes.
2. Reuse existing code where appropriate.
3. Keep changes narrowly scoped.
4. Ask questions only when requirements are genuinely ambiguous.
5. Document important design decisions.
6. Prefer maintainability over clever implementations.

## Current Direction

The current focus is building reliable authoring workflows around Markdown.

Primary capabilities include:

- knowledge management
- research organization
- AI-assisted writing
- revision workflows
- reusable prompts
- local-first tooling

Implementation should evolve incrementally. Prefer extending existing workflows
and documents over introducing entirely new patterns.

Each feature should move the project incrementally toward becoming a personal
authoring assistant without adding unnecessary complexity.
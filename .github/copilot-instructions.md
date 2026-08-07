# Copilot Instructions

## Purpose

These instructions guide AI coding sessions for Authors Assistant.

The repository is a local-first, Markdown-first authoring and knowledge
management system. Changes should preserve that direction.

## Working Style

- Prefer small, incremental changes over large rewrites.
- Keep change scope narrow and task-focused.
- Explain meaningful design decisions when they affect future maintenance.
- Keep implementation and documentation synchronized

## Architecture Preferences

- Prefer extending existing code paths before introducing new patterns.
- Avoid unnecessary abstractions.
- Do not add frameworks or infrastructure without clear, documented value.
- Preserve simple module boundaries and readable code.

## File and Project Hygiene

- Do not create files unless they provide clear, durable value.
- Keep Markdown as the source of truth for content and knowledge assets.
- Never overwrite source content unless explicitly requested.
- Maintain predictable file organization and naming.

## AI Behavior in This Repository

- AI assists the author and developers; it does not replace judgment.
- Preserve author voice and intent in writing-related workflows.
- Avoid speculative implementation beyond stated requirements.
- If requirements are ambiguous, choose the simplest interpretation that fits existing patterns.

## Documentation Expectations

- Update relevant docs when behavior, workflow, or architecture changes.
- Keep guidance practical and implementation-aligned.
- Favor clarity over completeness theater: concise docs that stay accurate are better than broad stale docs.

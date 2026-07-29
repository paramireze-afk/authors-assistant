---
title: "004 – PsyOps Knowledge Base"
id: 004
status: draft
priority: high
created: "2026-07-29"
updated: "2026-07-29"
tags: [features, documentation, knowledge-base, psyops, markdown-first, local-first]
owner: paul
---

# 004 – PsyOps Knowledge Base

## Purpose

Add psychological operations reference material to the author’s Markdown
knowledge base so it can be reused across research, drafting, and revision
workflows.

This is a documentation and repository-content initiative, not an application
feature implementation.

---

## Motivation

The project has evolved from a narrow revision workflow into a local-first,
Markdown-first authoring and knowledge system.

PsyOps-related topics are cross-cutting and frequently referenced across
people, organizations, events, concepts, and books. Capturing them as reusable
reference material improves consistency, retrieval quality, and long-term
maintainability.

---

## Goals

- Expand the knowledge base with PsyOps reference material in Markdown.
- Improve discoverability of related topics through linking and organization.
- Keep reference material reusable across multiple writing workflows.
- Preserve author control and judgment while using AI as an assistant.
- Grow the repository incrementally without architectural complexity.

---

## Scope

In scope:

- Creating and expanding PsyOps-related Markdown reference documents.
- Organizing documents in existing repository knowledge folders.
- Linking related materials where useful for navigation and retrieval.
- Improving reuse of knowledge across future writing tasks.

Out of implementation scope for this feature:

- Application/runtime code changes.
- New infrastructure, database, or service dependencies.
- Enforcing one rigid file format for all reference documents.

---

## Repository Conventions

- Markdown files should live in the appropriate folders (for example:
  `concepts/`, `people/`, `organizations/`, `events/`, `books/`, and related
  knowledge directories already in use).
- Files should be written as reusable reference material, not as standalone
  opinion articles.
- Related documents should be linked together when appropriate.
- Existing files should be expanded before creating near-duplicate entries.
- Organization, discoverability, and reuse should be prioritized over novelty.
- Markdown remains the source of truth; local-first workflows remain default.

This feature does not prescribe a fixed internal structure for each Markdown
file. Structure may vary by topic, source quality, and research depth.

---

## Success Criteria

A successful outcome includes:

- PsyOps reference material added to the knowledge base in appropriate folders.
- Strong cross-linking between related concepts, people, events, and
  organizations where relevant.
- Minimal duplication through expansion of existing files before creating new
  ones.
- Documents that are reusable as retrieval context for future authoring tasks.
- No application code changes introduced by this feature.

---

## Out of Scope

- Defining a mandatory template for every PsyOps Markdown file.
- Mandating a universal section order across all knowledge documents.
- Building automation pipelines, ingestion systems, or new retrieval code.
- Publishing conclusions as final truth where evidence remains uncertain.

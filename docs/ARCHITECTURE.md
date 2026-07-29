# Architecture

## Purpose

Author's Assistant is designed as a local-first Markdown authoring and
knowledge management system.

The architecture prioritizes author control, clarity, and long-term
maintainability over feature density or framework complexity.

See also: `docs/COPILOT_CONTEXT.md` for implementation and collaboration context.

## Design Rationale

### Local-first by default

The project runs on local files and local workflows.

Why:

- keeps author materials private and portable
- reduces operational complexity
- avoids service coupling for core writing workflows
- supports durable work even when external services change

### Markdown as source of truth

Markdown is the canonical format for drafts, notes, prompts, and outputs.

Why:

- human-readable and tool-agnostic
- easy to version and diff
- resilient over time compared to proprietary formats
- aligns with the author's existing writing and publishing flow

### No database requirement

Knowledge and writing artifacts are stored as files in a clear directory
structure.

Why:

- lowers system complexity and maintenance burden
- avoids schema migrations and hidden state
- keeps data inspectable and editable without specialized tools

### Prompts separated from code

Prompt text and writing guidance live in docs/prompts, while application logic
stays in source modules.

Why:

- enables iteration on writing behavior without code changes
- keeps responsibilities clear
- allows reusable prompt workflows across multiple tasks

### AI as assistant, not replacement

AI generates suggestions; the author remains the decision-maker.

Why:

- preserves voice, argument ownership, and editorial intent
- supports high-trust workflows for sensitive or speculative writing
- prevents silent automation from becoming authorship drift

### Simple architecture, incremental development

The project prefers small, composable modules and stepwise evolution.

Why:

- easier onboarding and safer edits
- faster debugging and review
- minimizes abstraction debt
- supports continuous documentation alignment

## Architectural Characteristics

- Small TypeScript modules with clear boundaries
- File-based inputs and outputs
- Reusable prompt-based workflows
- Explicit guardrails against destructive edits
- Documentation-first process for behavior and standards

## Tradeoffs

This architecture intentionally trades some convenience for reliability and
clarity.

Accepted tradeoffs:

- fewer "magic" automations
- more explicit file and workflow steps
- slower feature expansion in exchange for maintainability

## Evolution Strategy

When extending the system:

1. Start from existing workflow patterns.
2. Add the smallest useful change.
3. Keep prompts and docs synchronized with behavior.
4. Avoid introducing new infrastructure unless clearly necessary.
5. Preserve local-first and Markdown-first guarantees.

This keeps the project coherent as it grows from revision tooling into a
full authoring and knowledge environment.

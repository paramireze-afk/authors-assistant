---
layout: default
title: Author's Assistant
---

# Author's Assistant

Author's Assistant is a local-first, Markdown-first writing and knowledge-management project.

[View Repository on GitHub](https://github.com/paramireze-afk/authors-assistant)

## Purpose

Author's Assistant helps an author:

- collect and organize research,
- maintain a personal knowledge base,
- draft and revise long-form writing,
- prepare publication-ready Markdown outputs.

The project keeps author judgment central: AI assists the workflow, but final editorial control remains human.

## Project Philosophy

### Markdown-first

Markdown is the canonical format for notes, drafts, prompts, and outputs. This keeps content portable, readable, and easy to version.

### Local-first

The core workflow is file-based and runs on local project data. This reduces operational overhead and keeps research artifacts under direct author control.

### Simplicity over framework complexity

The architecture favors small TypeScript tools and composable workflows over heavyweight infrastructure.

## Feature Overview

- **Revision workflows:** Prompt-driven editing passes for Markdown drafts.
- **Knowledge workflows:** Structured directories for people, events, concepts, evidence, and sources.
- **Reusable prompts:** Prompt assets are separated from code so writing behavior can evolve without major refactors.
- **Publishing outputs:** Generate revised Markdown and downstream publication-ready assets.
- **Documentation-led development:** Behavior, architecture, and standards are documented as first-class project artifacts.

## Documentation Map

### Foundations

- [Project Requirements]({{ site.baseurl }}{% link docs/PROJECT_REQUIREMENTS.md %}) — vision, principles, current scope, and non-goals.
- [Architecture]({{ site.baseurl }}{% link docs/ARCHITECTURE.md %}) — architectural rationale, tradeoffs, and evolution strategy.
- [Copilot Context]({{ site.baseurl }}{% link docs/COPILOT_CONTEXT.md %}) — implementation and collaboration guidance for AI-assisted development.

### Writing Standards

- [Writing Style]({{ site.baseurl }}{% link docs/WRITING_STYLE.md %}) — voice, cadence, and stylistic direction.
- [Editing Rules]({{ site.baseurl }}{% link docs/EDITING_RULES.md %}) — editing constraints and quality boundaries.

### Feature Documents

- [Roadmap]({{ site.baseurl }}{% link docs/features/000-ROADMAP.md %})
- [Personal Knowledge Base]({{ site.baseurl }}{% link docs/features/001-PERSONAL-KNOWLEDGE-BASE.md %})
- [Knowledge Harvesting Workflow]({{ site.baseurl }}{% link docs/features/002-KNOWLEDGE-HARVESTING-WORKFLOW.md %})
- [Documentation Refresh]({{ site.baseurl }}{% link docs/features/003-documentation-refresh.md %})
- [PSYOPS Knowledge Base]({{ site.baseurl }}{% link docs/features/004-PSYOPS-KNOWLEDGE-BASE.md %})

### Knowledge Base Links

- [Knowledge README]({{ site.baseurl }}{% link knowledge/README.md %})

**People**

- [Andrew Kolvet]({{ site.baseurl }}{% link knowledge/people/andrew-kolvet.md %})
- [Anthony Fauci]({{ site.baseurl }}{% link knowledge/people/anthony-fauci.md %})
- [Baron Coleman]({{ site.baseurl }}{% link knowledge/people/baron-coleman.md %})
- [Blake Neff]({{ site.baseurl }}{% link knowledge/people/blake-neff.md %})
- [Bret Weinstein]({{ site.baseurl }}{% link knowledge/people/bret-weinstein.md %})
- [Candace Owens]({{ site.baseurl }}{% link knowledge/people/candace-owens.md %})
- [Charlie Kirk]({{ site.baseurl }}{% link knowledge/people/charlie-kirk.md %})
- [Erika Kirk]({{ site.baseurl }}{% link knowledge/people/erika-kirk.md %})
- [Lori Frantzve]({{ site.baseurl }}{% link knowledge/people/lori-frantzve.md %})
- [Nesta Helen Webster]({{ site.baseurl }}{% link knowledge/people/nesta-helen-webster.md %})
- [Robert F. Kennedy Jr.]({{ site.baseurl }}{% link knowledge/people/robert-f-kennedy-jr.md %})
- [Tyler Bowyer]({{ site.baseurl }}{% link knowledge/people/tyler-bowyer.md %})
- [Tyler Robinson]({{ site.baseurl }}{% link knowledge/people/tyler-robinson.md %})

**Knowledge Domains**

- [Concepts]({{ site.baseurl }}{% link knowledge/concepts/README.md %})
- [Events]({{ site.baseurl }}{% link knowledge/events/README.md %})
- [Evidence]({{ site.baseurl }}{% link knowledge/evidence/README.md %})
- [Organizations]({{ site.baseurl }}{% link knowledge/organizations/README.md %})
- [Sources]({{ site.baseurl }}{% link knowledge/sources/README.md %})
- [Topics]({{ site.baseurl }}{% link knowledge/topics/README.md %})
- [Characters]({{ site.baseurl }}{% link knowledge/characters/README.md %})

## Roadmap

Current direction is incremental and workflow-driven.

- **Near-term:** Harden core revision workflows, improve source organization, and keep docs synchronized with behavior.
- **Mid-term:** Expand reusable authoring workflows and knowledge synthesis patterns.
- **Long-term:** Add modular capabilities (search, linking, publishing helpers) without breaking local-first and Markdown-first guarantees.

For detailed sequencing, see the [Roadmap document]({{ site.baseurl }}{% link docs/features/000-ROADMAP.md %}).

## Repository

- GitHub: [paramireze-afk/authors-assistant](https://github.com/paramireze-afk/authors-assistant)

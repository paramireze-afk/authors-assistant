---
layout: default
title: Author's Assistant
created: 2026-08-03
---

# Author's Assistant

A local-first, Markdown-first research and writing workspace.

[View Repository on GitHub](https://github.com/paramireze-afk/authors-assistant)

---

## Most Recently Added Markdown Files

Start here for the newest writing activity across the repository.

{% assign markdown_pages = site.pages | concat: site.documents
	| where_exp: "p", "p.path contains '.md'"
	| where_exp: "p", "p.created"
	| sort_natural: "created"
	| reverse %}
{% assign shown_count = 0 %}
{% for page in markdown_pages %}
{% if shown_count < 10 %}
{% unless page.path contains '/index.md' %}
{% if page.path contains 'articles/' or page.path contains 'research/' or page.path contains 'knowledge/' %}
- [{{ page.title | default: page.name | default: page.basename }}]({{ page.url | relative_url }})
{% assign shown_count = shown_count | plus: 1 %}
{% endif %}
{% endunless %}
{% endif %}
{% endfor %}

*Only Markdown files with a `created` field in front matter are included here.*

---

## What This Site Is

This site is a working knowledge base for research, synthesis, and long-form writing.

It combines:

- research notes and transcript-based analysis,
- concept and event pages that turn recurring ideas into reusable references,
- published essays and draft ideas,
- a Markdown-first workflow designed to stay readable and durable.

If this is your first visit, the easiest way to explore is to start with a few curated paths below.

## Start Here

### Read a Published Piece

- [Published Articles]({{ site.baseurl }}{% link articles/published/index.md %})

### Browse the Research Archive

- [Research Landing Page]({{ site.baseurl }}{% link research/index.md %})
- [Research Index]({{ site.baseurl }}{% link knowledge/research/index.md %})

### Explore the Knowledge Base

- [Concepts]({{ site.baseurl }}{% link knowledge/concepts/index.md %})
- [Events]({{ site.baseurl }}{% link knowledge/events/index.md %})
- [Reports]({{ site.baseurl }}{% link knowledge/reports/index.md %})
- [Syntheses]({{ site.baseurl }}{% link knowledge/syntheses/index.md %})
- [Books]({{ site.baseurl }}{% link knowledge/books/index.md %})

---

## Featured Entry Points

### If You Want Narrative Writing

- Start with [Published Articles]({{ site.baseurl }}{% link articles/published/index.md %}) for finished essays.
- Visit [Ideas / Drafts]({{ site.baseurl }}{% link articles/ideas/index.md %}) for works in progress and early concepts.
- Visit [Synthesis Articles]({{ site.baseurl }}{% link articles/synthesis/index.md %}) for structured long-form explainers.

### If You Want Source-Driven Research

- Use [Research]({{ site.baseurl }}{% link research/index.md %}) to scan notes by date.
- Dive into focused sub-areas like [Michael Yon]({{ site.baseurl }}{% link knowledge/research/michael-yon/index.md %}), [Chris Martenson]({{ site.baseurl }}{% link knowledge/research/chris-martenson/index.md %}), or [Yaakov Shapiro]({{ site.baseurl }}{% link knowledge/research/yaakov-shapiro/index.md %}).

### If You Want Big-Picture Interpretation

- Browse [Concepts]({{ site.baseurl }}{% link knowledge/concepts/index.md %}) for recurring frameworks.
- Browse [Syntheses]({{ site.baseurl }}{% link knowledge/syntheses/index.md %}) for cross-cutting summaries.
- Read [The AIDS Dissident Movement]({{ site.baseurl }}{% link knowledge/events/aids-crisis.md %}) for a long-form event history.

---

## Browse by Area

### Articles

- [Published Articles]({{ site.baseurl }}{% link articles/published/index.md %})
- [Ideas / Drafts]({{ site.baseurl }}{% link articles/ideas/index.md %})
- [Synthesis Articles]({{ site.baseurl }}{% link articles/synthesis/index.md %})

### Knowledge

- [Books]({{ site.baseurl }}{% link knowledge/books/index.md %})
- [Syntheses]({{ site.baseurl }}{% link knowledge/syntheses/index.md %})
- [Concepts]({{ site.baseurl }}{% link knowledge/concepts/index.md %})
- [Events]({{ site.baseurl }}{% link knowledge/events/index.md %})
- [Reports]({{ site.baseurl }}{% link knowledge/reports/index.md %})

### Research

- [Research Landing Page]({{ site.baseurl }}{% link research/index.md %})
- [Research Index]({{ site.baseurl }}{% link knowledge/research/index.md %})
- [Bret Weinstein]({{ site.baseurl }}{% link knowledge/research/bret-weinstein/index.md %})
- [Chris Martenson]({{ site.baseurl }}{% link knowledge/research/chris-martenson/index.md %})
- [Jiang Xueqin]({{ site.baseurl }}{% link knowledge/research/jiang-xueqin/index.md %})
- [Macroeconomics]({{ site.baseurl }}{% link knowledge/research/macroeconomics/index.md %})
- [Michael Yon]({{ site.baseurl }}{% link knowledge/research/michael-yon/index.md %})
- [Mises]({{ site.baseurl }}{% link knowledge/research/mises/index.md %})
- [Salatin]({{ site.baseurl }}{% link knowledge/research/salatin/index.md %})
- [Yaakov Shapiro]({{ site.baseurl }}{% link knowledge/research/yaakov-shapiro/index.md %})

---

## Recently Added

These sections update automatically from the repository so a returning visitor can quickly see what changed.

### Recent Research Notes

{% assign research_pages = site.pages | where_exp: "p", "p.path contains 'knowledge/research/'" | where_exp: "p", "p.path contains '.md'" | sort: "path" | reverse %}
{% for page in research_pages limit: 8 %}
{% unless page.path contains '/index.md' %}
- [{{ page.title | default: page.name }}]({{ page.url | prepend: site.baseurl }})
{% endunless %}
{% endfor %}

### Recent Published Articles

{% assign published_pages = site.pages | where_exp: "p", "p.path contains 'articles/published/'" | where_exp: "p", "p.path contains '.md'" | sort: "path" | reverse %}
{% for page in published_pages limit: 8 %}
{% unless page.path contains '/index.md' %}
- [{{ page.title | default: page.name }}]({{ page.url | prepend: site.baseurl }})
{% endunless %}
{% endfor %}

### Recent Concepts

{% assign concept_pages = site.pages | where_exp: "p", "p.path contains 'knowledge/concepts/'" | where_exp: "p", "p.path contains '.md'" | sort: "path" | reverse %}
{% for page in concept_pages limit: 6 %}
{% unless page.path contains '/index.md' %}
- [{{ page.title | default: page.name }}]({{ page.url | prepend: site.baseurl }})
{% endunless %}
{% endfor %}

### Recent Ideas / Drafts

{% assign ideas_pages = site.pages | where_exp: "p", "p.path contains 'articles/ideas/'" | where_exp: "p", "p.path contains '.md'" | sort: "path" | reverse %}
{% for page in ideas_pages limit: 6 %}
{% unless page.path contains '/index.md' %}
- [{{ page.title | default: page.name }}]({{ page.url | prepend: site.baseurl }})
{% endunless %}
{% endfor %}

### Recent Syntheses

{% assign synth_pages = site.pages | where_exp: "p", "p.path contains 'knowledge/syntheses/'" | where_exp: "p", "p.path contains '.md'" | sort: "path" | reverse %}
{% for page in synth_pages limit: 8 %}
{% unless page.path contains '/index.md' %}
- [{{ page.title | default: page.name }}]({{ page.url | prepend: site.baseurl }})
{% endunless %}
{% endfor %}

### Recent Events

{% assign event_pages = site.pages | where_exp: "p", "p.path contains 'knowledge/events/'" | where_exp: "p", "p.path contains '.md'" | sort: "path" | reverse %}
{% for page in event_pages limit: 8 %}
{% unless page.path contains '/index.md' %}
- [{{ page.title | default: page.name }}]({{ page.url | prepend: site.baseurl }})
{% endunless %}
{% endfor %}

### Recent Reports

{% assign report_pages = site.pages | where_exp: "p", "p.path contains 'knowledge/reports/'" | where_exp: "p", "p.path contains '.md'" | sort: "path" | reverse %}
{% for page in report_pages limit: 10 %}
{% unless page.path contains '/index.md' %}
- [{{ page.title | default: page.name }}]({{ page.url | prepend: site.baseurl }})
{% endunless %}
{% endfor %}

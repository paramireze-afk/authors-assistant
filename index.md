---
layout: default
title: Author's Assistant
created: 2026-08-03
---

# Author's Assistant

A local-first research and writing workspace — podcast notes, book analysis, concept entries, and long-form synthesis.

---

## Recently Added

*The 12 most recently created files across the knowledge base, newest first.*

{% assign all_pages = site.pages | concat: site.documents
  | where_exp: "p", "p.path contains '.md'"
  | where_exp: "p", "p.created"
  | where_exp: "p", "p.path contains 'knowledge/'"
  | sort_natural: "created"
  | reverse %}
{% assign synth_recent = site.pages
  | where_exp: "p", "p.path contains 'articles/synthesis/'"
  | where_exp: "p", "p.path contains '.md'"
  | where_exp: "p", "p.created"
  | sort_natural: "created"
  | reverse %}
{% assign combined = all_pages | concat: synth_recent | sort_natural: "created" | reverse %}

<table>
  <thead><tr><th style="width:28%">Title</th><th>Description</th></tr></thead>
  <tbody>
  {% assign shown = 0 %}
  {% for page in combined %}
  {% if shown < 12 %}
  {% unless page.path contains '/index.md' or page.path contains 'README' %}
    <tr>
      <td><a href="{{ page.url | relative_url }}">{{ page.title | default: page.name | truncatewords: 8, "…" }}</a></td>
      <td>{{ page.description | default: "" | truncatewords: 30, "…" }}</td>
    </tr>
    {% assign shown = shown | plus: 1 %}
  {% endunless %}
  {% endif %}
  {% endfor %}
  </tbody>
</table>

---

## Long-Form Synthesis

Structured explainers on specific topics — each one is a standalone deep dive.

{% assign synth_pages = site.pages | where_exp: "p", "p.path contains 'articles/synthesis/'" | where_exp: "p", "p.path contains '.md'" | sort_natural: "created" | reverse %}
{% for page in synth_pages %}
{% unless page.path contains '/index.md' %}
- [{{ page.title | default: page.name }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}

---

## Research Notes by Source

Notes from interviews, podcasts, and conversations — organized by who is speaking.

| Source | Focus |
|---|---|
| [Michael Yon]({{ site.baseurl }}{% link knowledge/research/michael-yon/index.md %}) | Migration, 5GW, geopolitics |
| [Chris Martenson]({{ site.baseurl }}{% link knowledge/research/chris-martenson/index.md %}) | Energy, gold, inflation |
| [Bret Weinstein]({{ site.baseurl }}{% link knowledge/research/bret-weinstein/index.md %}) | Biology, COVID, migration |
| [Yaakov Shapiro]({{ site.baseurl }}{% link knowledge/research/yaakov-shapiro/index.md %}) | Judaism, Zionism, theology |
| [Dave DeCamp]({{ site.baseurl }}{% link knowledge/research/dave-decamp/index.md %}) | Wars, foreign policy |
| [Scott Horton]({{ site.baseurl }}{% link knowledge/research/scott-horton/index.md %}) | Economics, libertarianism |
| [Jiang Xueqin]({{ site.baseurl }}{% link knowledge/research/jiang-xueqin/index.md %}) | China, education |
| [Mises / Austrian]({{ site.baseurl }}{% link knowledge/research/mises/index.md %}) | Economic theory |
| [Joel Salatin]({{ site.baseurl }}{% link knowledge/research/salatin/index.md %}) | Agriculture, regulation |
| [Macroeconomics]({{ site.baseurl }}{% link knowledge/research/macroeconomics/index.md %}) | Debt, oil, yields |

---

## Concepts & Frameworks

Reusable ideas that show up across multiple topics — doctrines, mechanisms, and recurring patterns.

{% assign concept_pages = site.pages | where_exp: "p", "p.path contains 'knowledge/concepts/'" | where_exp: "p", "p.path contains '.md'" | sort: "title" %}
{% for page in concept_pages %}
{% unless page.path contains '/index.md' or page.path contains 'README' %}
- [{{ page.title | default: page.name }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}

---

## Events & Episodes

Specific historical events with dedicated entries.

{% assign event_pages = site.pages | where_exp: "p", "p.path contains 'knowledge/events/'" | where_exp: "p", "p.path contains '.md'" | sort: "title" %}
{% for page in event_pages %}
{% unless page.path contains '/index.md' or page.path contains 'README' %}
- [{{ page.title | default: page.name }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}

---

## Books

Notes and summaries on books read.

{% assign book_pages = site.pages | where_exp: "p", "p.path contains 'knowledge/books/'" | where_exp: "p", "p.path contains '.md'" | sort: "title" %}
{% for page in book_pages %}
{% unless page.path contains '/index.md' or page.path contains 'README' or page.path contains '.md/' %}
- [{{ page.title | default: page.name }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}

---

## Cross-Source Syntheses

Analytical summaries that connect threads across multiple sources.

{% assign ks_pages = site.pages | where_exp: "p", "p.path contains 'knowledge/syntheses/'" | where_exp: "p", "p.path contains '.md'" | sort: "title" %}
{% for page in ks_pages %}
{% unless page.path contains '/index.md' or page.path contains 'README' %}
- [{{ page.title | default: page.name }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}

---

## People & Organizations

Profiles of individuals and institutions that appear across the research.

**People** — [{{ site.baseurl }}/knowledge/people/]({{ site.baseurl }}/knowledge/people/)

{% assign people_pages = site.pages | where_exp: "p", "p.path contains 'knowledge/people/'" | where_exp: "p", "p.path contains '.md'" | sort: "title" %}
{% for page in people_pages %}
{% unless page.path contains '/index.md' or page.path contains 'README' %}
- [{{ page.title | default: page.name }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}

**Organizations**

{% assign org_pages = site.pages | where_exp: "p", "p.path contains 'knowledge/organizations/'" | where_exp: "p", "p.path contains '.md'" | sort: "title" %}
{% for page in org_pages %}
{% unless page.path contains '/index.md' or page.path contains 'README' %}
- [{{ page.title | default: page.name }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}

---

## Wars & Strategy

{% assign war_pages = site.pages | where_exp: "p", "p.path contains 'knowledge/wars/'" | where_exp: "p", "p.path contains '.md'" | sort: "title" %}
{% for page in war_pages %}
{% unless page.path contains '/index.md' or page.path contains 'README' %}
- [{{ page.title | default: page.name }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}

---

## Ideas & Drafts

Works in progress and early-stage writing.

{% assign idea_pages = site.pages | where_exp: "p", "p.path contains 'articles/ideas/'" | where_exp: "p", "p.path contains '.md'" | sort_natural: "created" | reverse %}
{% for page in idea_pages %}
{% unless page.path contains '/index.md' or page.path contains 'README' %}
- [{{ page.title | default: page.name }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}

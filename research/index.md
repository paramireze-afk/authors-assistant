---
layout: default
title: "Research"
permalink: /research/
---

# Research

This page auto-populates links for all notes under `knowledge/research`.

- [Home]({% link index.md %})
- [Research Index]({% link knowledge/research/index.md %})

{% assign research_pages = site.pages | where_exp: "p", "p.path contains 'knowledge/research/' and p.path != 'knowledge/research/index.md' and p.path != 'knowledge/research/bret-weinstein/index.md' and p.path != 'knowledge/research/chris-martenson/index.md' and p.path != 'knowledge/research/jiang-xueqin/index.md' and p.path != 'knowledge/research/macroeconomics/index.md' and p.path != 'knowledge/research/michael-yon/index.md' and p.path != 'knowledge/research/mises/index.md' and p.path != 'knowledge/research/salatin/index.md'" %}
{% assign sorted_research = research_pages | sort: "path" | reverse %}

{% for page in sorted_research %}
- [{{ page.title | default: page.name }}]({{ site.baseurl }}{{ page.url }})
{% endfor %}

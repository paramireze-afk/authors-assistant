---
layout: default
title: John Campbell
---

# John Campbell

Public health, biosecurity, and medical analysis.

{% assign campbell_pages = site.pages | where_exp: "p", "p.path contains 'knowledge/research/john-campbell/'" | where_exp: "p", "p.path contains '.md'" | sort_natural: "created" | reverse %}
{% for page in campbell_pages %}
{% unless page.path contains '/index.md' %}
- [{{ page.title | default: page.name }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}

---
layout: default
title: "Research"
permalink: /research/
---

# Research

This page auto-populates links for all notes under `knowledge/research`.

- [Home]({% link index.md %})
- [Research Index]({% link knowledge/research/index.md %})

{% assign research_pages = site.pages | where_exp: "p", "p.path contains 'knowledge/research/'" | where_exp: "p", "p.path contains '.md'" | sort: "path" | reverse %}

{% for page in research_pages %}
{% unless page.path contains '/index.md' %}
- [{{ page.title | default: page.name }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}

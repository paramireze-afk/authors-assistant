---
layout: default
title: "Research"
permalink: /research/
created: 2026-08-03
---

# Research

This page auto-populates links for all notes under `knowledge/research`.

- [Home]({{ site.baseurl }}{% link index.md %})
- [Research Index]({{ site.baseurl }}{% link knowledge/research/index.md %})

{% assign research_pages = site.pages | where_exp: "p", "p.path contains 'knowledge/research/'" | where_exp: "p", "p.path contains '.md'" | sort: "path" | reverse %}

{% for page in research_pages %}
{% unless page.path contains '/index.md' %}
- [{{ page.title | default: page.name }}]({{ page.url | prepend: site.baseurl }})
{% endunless %}
{% endfor %}

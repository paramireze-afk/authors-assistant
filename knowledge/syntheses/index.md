---
layout: default
title: "Knowledge / Syntheses"
---

# Knowledge / Syntheses

Browse syntheses and cross-cutting summaries.

- [Home]({% link index.md %})

{% assign synth_pages = site.pages | where_exp: "p", "p.path contains 'knowledge/syntheses/' and p.path contains '.md'" | sort: "path" | reverse %}
{% for page in synth_pages %}
{% unless page.path contains '/index.md' %}
- [{{ page.title | default: page.name }}]({{ site.baseurl }}{{ page.url }})
{% endunless %}
{% endfor %}

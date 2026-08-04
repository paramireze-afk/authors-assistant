---
layout: default
title: "Knowledge / Syntheses"
created: 2026-08-03
---

# Knowledge / Syntheses

Browse syntheses and cross-cutting summaries.

- [Home]({{ site.baseurl }}{% link index.md %})
- [Back to Home]({{ site.baseurl }}{% link index.md %})

{% assign synth_pages = site.pages | where_exp: "p", "p.path contains 'knowledge/syntheses/'" | where_exp: "p", "p.path contains '.md'" | sort: "path" | reverse %}
{% for page in synth_pages %}
{% unless page.path contains '/index.md' %}
- [{{ page.title | default: page.name }}]({{ page.url | prepend: site.baseurl }})
{% endunless %}
{% endfor %}

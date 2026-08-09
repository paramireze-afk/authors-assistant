---
layout: default
title: "Articles / Synthesis"
created: 2026-08-08
---

# Articles / Synthesis

Browse synthesis articles, sorted newest to oldest by filename.

- [Home]({{ site.baseurl }}{% link index.md %})
- [Back to Home]({{ site.baseurl }}{% link index.md %})

{% assign synthesis_pages = site.pages | where_exp: "p", "p.path contains 'articles/synthesis/'" | where_exp: "p", "p.path contains '.md'" | sort: "path" | reverse %}
{% for page in synthesis_pages %}
{% unless page.path contains '/index.md' %}
- [{{ page.title | default: page.name }}]({{ page.url | prepend: site.baseurl }})
{% endunless %}
{% endfor %}

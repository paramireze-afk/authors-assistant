---
layout: default
title: "Knowledge / Research / Scott Horton"
created: 2026-08-12
---

# Knowledge / Research / Scott Horton

Browse Scott Horton research notes.

- [Home]({{ site.baseurl }}{% link index.md %})
- [Back to Research]({{ site.baseurl }}{% link knowledge/research/index.md %})

{% assign sh_pages = site.pages | where_exp: "p", "p.path contains 'knowledge/research/scott-horton/'" | where_exp: "p", "p.path contains '.md'" | sort: "path" | reverse %}
{% for page in sh_pages %}
{% unless page.path contains '/index.md' %}
- [{{ page.title | default: page.name }}]({{ page.url | prepend: site.baseurl }})
{% endunless %}
{% endfor %}

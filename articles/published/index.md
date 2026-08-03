---
layout: default
title: "Articles / Published"
---

# Articles / Published

Browse published articles, sorted newest to oldest by filename.

- [Home]({% link index.md %})

{% assign published_pages = site.pages | where_exp: "p", "p.path contains 'articles/published/'" | where_exp: "p", "p.path contains '.md'" | sort: "path" | reverse %}
{% for page in published_pages %}
{% unless page.path contains '/index.md' %}
- [{{ page.title | default: page.name }}]({{ page.url | prepend: site.baseurl }})
{% endunless %}
{% endfor %}

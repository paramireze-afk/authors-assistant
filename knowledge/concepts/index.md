---
layout: default
title: "Knowledge / Concepts"
created: 2026-08-03
---

# Knowledge / Concepts

Browse concepts and concept notes.

- [Home]({{ site.baseurl }}{% link index.md %})
- [Back to Home]({{ site.baseurl }}{% link index.md %})

{% assign concept_pages = site.pages | where_exp: "p", "p.path contains 'knowledge/concepts/'" | where_exp: "p", "p.path contains '.md'" | sort: "path" | reverse %}
{% for page in concept_pages %}
{% unless page.path contains '/index.md' %}
- [{{ page.title | default: page.name }}]({{ page.url | prepend: site.baseurl }})
{% endunless %}
{% endfor %}

---
layout: default
title: "Knowledge / Books"
created: 2026-08-03
---

# Knowledge / Books

Browse books and book-related notes.

- [Home]({{ site.baseurl }}{% link index.md %})
- [Back to Home]({{ site.baseurl }}{% link index.md %})

{% assign book_pages = site.pages | where_exp: "p", "p.path contains 'knowledge/books/'" | sort: "path" %}
{% for page in book_pages %}
{% unless page.path contains '/index.md' %}
- [{{ page.title | default: page.name }}]({{ page.url | prepend: site.baseurl }})
{% endunless %}
{% endfor %}

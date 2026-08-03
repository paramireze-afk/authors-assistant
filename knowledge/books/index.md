---
layout: default
title: "Knowledge / Books"
---

# Knowledge / Books

Browse books and book-related notes.

- [Home]({% link index.md %})

{% assign book_pages = site.pages | where_exp: "p", "p.path contains 'knowledge/books/'" | sort: "path" %}
{% for page in book_pages %}
{% unless page.path contains '/index.md' %}
- [{{ page.title | default: page.name }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}

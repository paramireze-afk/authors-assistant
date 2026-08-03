---
layout: default
title: "Knowledge / Books"
---

# Knowledge / Books

Browse books and book-related notes.

- [Home]({% link index.md %})

{% assign book_pages = site.pages | where_exp: "p", "p.path contains 'knowledge/books/' and p.path contains '.md'" | sort: "path" %}
{% for page in book_pages %}
{% unless page.path contains '/index.md' %}
- [{{ page.title | default: page.name }}]({{ site.baseurl }}{{ page.url }})
{% endunless %}
{% endfor %}

---
layout: default
title: "Articles / Ideas"
---

# Articles / Ideas

Browse working ideas and drafts, sorted newest to oldest by filename.

- [Home]({% link index.md %})

{% assign ideas_pages = site.pages | where_exp: "p", "p.path contains 'articles/ideas/' and p.path contains '.md'" | sort: "path" | reverse %}
{% for page in ideas_pages %}
{% unless page.path contains '/index.md' %}
- [{{ page.title | default: page.name }}]({{ site.baseurl }}{{ page.url }})
{% endunless %}
{% endfor %}

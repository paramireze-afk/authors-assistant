---
layout: default
title: "Articles / Ideas"
---

# Articles / Ideas

Browse working ideas and drafts, sorted newest to oldest by filename.

- [Home]({{ site.baseurl }}{% link index.md %})
- [Back to Home]({{ site.baseurl }}{% link index.md %})

{% assign ideas_pages = site.pages | where_exp: "p", "p.path contains 'articles/ideas/'" | where_exp: "p", "p.path contains '.md'" | sort: "path" | reverse %}
{% for page in ideas_pages %}
{% unless page.path contains '/index.md' %}
- [{{ page.title | default: page.name }}]({{ page.url | prepend: site.baseurl }})
{% endunless %}
{% endfor %}

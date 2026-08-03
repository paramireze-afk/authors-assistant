---
layout: default
title: "Knowledge / Events"
---

# Knowledge / Events

Browse events and timelines.

- [Home]({{ site.baseurl }}{% link index.md %})

{% assign event_pages = site.pages | where_exp: "p", "p.path contains 'knowledge/events/'" | where_exp: "p", "p.path contains '.md'" | sort: "path" | reverse %}
{% for page in event_pages %}
{% unless page.path contains '/index.md' %}
- [{{ page.title | default: page.name }}]({{ page.url | prepend: site.baseurl }})
{% endunless %}
{% endfor %}

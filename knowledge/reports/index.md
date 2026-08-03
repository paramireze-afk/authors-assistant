---
layout: default
title: "Knowledge / Reports"
---

# Knowledge / Reports

Browse reports and report-style research summaries.

- [Home]({{ site.baseurl }}{% link index.md %})

{% assign report_pages = site.pages | where_exp: "p", "p.path contains 'knowledge/reports/'" | where_exp: "p", "p.path contains '.md'" | sort: "path" | reverse %}
{% for page in report_pages %}
{% unless page.path contains '/index.md' %}
- [{{ page.title | default: page.name }}]({{ page.url | prepend: site.baseurl }})
{% endunless %}
{% endfor %}

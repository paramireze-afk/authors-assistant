---
layout: default
title: "Knowledge / Research"
---

# Knowledge / Research

Browse research notes, sorted newest to oldest by filename.

- [Home]({% link index.md %})

### Browse by area

- [Bret Weinstein]({% link knowledge/research/bret-weinstein/index.md %})
- [Chris Martenson]({% link knowledge/research/chris-martenson/index.md %})
- [Jiang Xueqin]({% link knowledge/research/jiang-xueqin/index.md %})
- [Macroeconomics]({% link knowledge/research/macroeconomics/index.md %})
- [Michael Yon]({% link knowledge/research/michael-yon/index.md %})
- [Mises]({% link knowledge/research/mises/index.md %})
- [Salatin]({% link knowledge/research/salatin/index.md %})
- [Yaakov Shapiro]({% link knowledge/research/yaakov-shapiro/index.md %})

{% assign research_pages = site.pages | where_exp: "p", "p.path contains 'knowledge/research/'" | where_exp: "p", "p.path contains '.md'" | sort: "path" | reverse %}
{% for page in research_pages %}
{% unless page.path contains '/index.md' %}
- [{{ page.title | default: page.name }}]({{ site.baseurl }}{{ page.url }})
{% endunless %}
{% endfor %}

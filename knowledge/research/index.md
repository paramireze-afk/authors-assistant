---
layout: default
title: "Knowledge / Research"
---

# Knowledge / Research

Browse research notes, sorted newest to oldest by filename.

- [Home]({{ site.baseurl }}{% link index.md %})
- [Back to Home]({{ site.baseurl }}{% link index.md %})

### Browse by area

- [Bret Weinstein]({{ site.baseurl }}{% link knowledge/research/bret-weinstein/index.md %})
- [Chris Martenson]({{ site.baseurl }}{% link knowledge/research/chris-martenson/index.md %})
- [Jiang Xueqin]({{ site.baseurl }}{% link knowledge/research/jiang-xueqin/index.md %})
- [Macroeconomics]({{ site.baseurl }}{% link knowledge/research/macroeconomics/index.md %})
- [Michael Yon]({{ site.baseurl }}{% link knowledge/research/michael-yon/index.md %})
- [Mises]({{ site.baseurl }}{% link knowledge/research/mises/index.md %})
- [Salatin]({{ site.baseurl }}{% link knowledge/research/salatin/index.md %})
- [Yaakov Shapiro]({{ site.baseurl }}{% link knowledge/research/yaakov-shapiro/index.md %})

{% assign research_pages = site.pages | where_exp: "p", "p.path contains 'knowledge/research/'" | where_exp: "p", "p.path contains '.md'" | sort: "path" | reverse %}
{% for page in research_pages %}
{% unless page.path contains '/index.md' %}
- [{{ page.title | default: page.name }}]({{ page.url | prepend: site.baseurl }})
{% endunless %}
{% endfor %}

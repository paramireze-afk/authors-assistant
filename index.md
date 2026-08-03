---
layout: default
title: Author's Assistant
---

# Author's Assistant

A local-first, Markdown-first writing and knowledge workspace.

[View Repository on GitHub](https://github.com/paramireze-afk/authors-assistant)

---

## Navigation

### Articles

- [Published Articles]({{ site.baseurl }}{% link articles/published/index.md %})
- [Ideas / Drafts]({{ site.baseurl }}{% link articles/ideas/index.md %})

### Knowledge

- [Books]({{ site.baseurl }}{% link knowledge/books/index.md %})
- [Syntheses]({{ site.baseurl }}{% link knowledge/syntheses/index.md %})
- [Concepts]({{ site.baseurl }}{% link knowledge/concepts/pinocchio-state.md %})

### Research

- [Research Landing Page]({{ site.baseurl }}{% link research/index.md %})
- [Research Index]({{ site.baseurl }}{% link knowledge/research/index.md %})
- [Bret Weinstein]({{ site.baseurl }}{% link knowledge/research/bret-weinstein/index.md %})
- [Chris Martenson]({{ site.baseurl }}{% link knowledge/research/chris-martenson/index.md %})
- [Jiang Xueqin]({{ site.baseurl }}{% link knowledge/research/jiang-xueqin/index.md %})
- [Macroeconomics]({{ site.baseurl }}{% link knowledge/research/macroeconomics/index.md %})
- [Michael Yon]({{ site.baseurl }}{% link knowledge/research/michael-yon/index.md %})
- [Mises]({{ site.baseurl }}{% link knowledge/research/mises/index.md %})
- [Salatin]({{ site.baseurl }}{% link knowledge/research/salatin/index.md %})

---

## Recent by Category

### Recent Published Articles

{% assign published_pages = site.pages | where_exp: "p", "p.path contains 'articles/published/' and p.path contains '.md'" | sort: "path" | reverse %}
{% for page in published_pages limit: 8 %}
{% unless page.path contains '/index.md' %}
- [{{ page.title | default: page.name }}]({{ site.baseurl }}{{ page.url }})
{% endunless %}
{% endfor %}

### Recent Ideas / Drafts

{% assign ideas_pages = site.pages | where_exp: "p", "p.path contains 'articles/ideas/' and p.path contains '.md'" | sort: "path" | reverse %}
{% for page in ideas_pages limit: 6 %}
{% unless page.path contains '/index.md' %}
- [{{ page.title | default: page.name }}]({{ site.baseurl }}{{ page.url }})
{% endunless %}
{% endfor %}

### Recent Research Notes

{% assign research_pages = site.pages | where_exp: "p", "p.path contains 'knowledge/research/' and p.path contains '.md'" | sort: "path" | reverse %}
{% for page in research_pages limit: 12 %}
{% unless page.path contains '/index.md' %}
- [{{ page.title | default: page.name }}]({{ site.baseurl }}{{ page.url }})
{% endunless %}
{% endfor %}

### Recent Syntheses

{% assign synth_pages = site.pages | where_exp: "p", "p.path contains 'knowledge/syntheses/' and p.path contains '.md'" | sort: "path" | reverse %}
{% for page in synth_pages limit: 8 %}
- [{{ page.title | default: page.name }}]({{ site.baseurl }}{{ page.url }})
{% endfor %}

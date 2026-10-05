---
title: "Douglas B. Vogt: Decoding the Hebrew Scriptures — Article Series Plan"
project: Space Stuff
subject: Douglas B. Vogt
description: >
  A planning and tracking document for a series of nine articles
  (1,500–3,000 words each) presenting Douglas B. Vogt's biblical and
  archaeological work, drawn mainly from his "Decoding the Hebrew
  Scriptures" book series and his 1997 and 1999 Sinai expeditions. The
  articles present Vogt's perspective faithfully and in his own terms,
  covering his decoding method, his reading of Joseph and the Hebrews in
  Egypt, the lineage of Aaron and Moses, the Exodus, his identification
  of the real Mount Sinai, the prophets and priests, and his own account
  of his calling. Evaluation and scoring of his claims happen separately
  from the articles. This file tracks sources, article status, and
  dependencies, and is meant to be shared with Claude at the start of
  each drafting session.
focus: Biblical and archaeological work
status: planning
created: 2026-10-04
last_updated: 2026-10-04

editorial_stance: >
  Present Vogt's perspective faithfully and in his own terms. No rebuttals,
  balancing, or scoring inside the articles. The author evaluates separately.

article_length:
  min_words: 1500
  max_words: 3000

conventions:
  attribution: 'Use "Vogt argues", "in Vogt''s reading", "according to Vogt" so it is always clear whose view is presented'
  citations: "Cite page numbers for every claim drawn from his books"
  quotes: "Short, strong quotes in his own words; paraphrase the rest"
  terminology: "Use Vogt's own key terms; define each on first use"

sources:
  books:
    - title: "Volume I (title unconfirmed)"
      status: to_identify
      notes: "May contain the foundational explanation of the decoding method"
    - title: "Joseph and Slavery for the Hebrews"
      series: "Decoding the Hebrew Scriptures"
      year: 2017
      pages: 108
      isbn: "0930808185"
      status: to_acquire
    - title: "Volume III: The Exodus and Finding the Real Mount Sinai"
      series: "Decoding the Hebrew Scriptures"
      year: 2018
      pages: 234
      isbn: "9780930808204"
      status: to_acquire
    - title: "Volume IV: The Prophets and the Priests"
      series: "Decoding the Hebrew Scriptures"
      year: 2023
      pages: 242
      isbn: "9780930808228"
      status: to_acquire
    - title: "God's Day of Judgment: The Real Cause of Global Warming"
      year: 2007
      status: optional
      notes: "Background for article 9 (Day of Judgment / solar model link)"
  other:
    - name: "1997 Sinai expedition writeup (Diehold Foundation)"
      url: "http://dieholdfoundation.com/sinai-egypt-expedition-of-1997.html"
    - name: "Seattle Times profile, 'A Mount Sinai mission' (2000)"
      url: "https://archive.seattletimes.com/archive/20001007/4046570/a-mount-sinai-mission"
    - name: "Vogt's lectures, interviews, and Vector Associates materials"
      status: to_find

articles:
  - id: 1
    title: "Vogt Turns to Scripture"
    sources: [all volumes, Seattle Times profile]
    depends_on: []
    status: not_started
  - id: 2
    title: "The Decoding Method"
    sources: [Volume I, Joseph and Slavery for the Hebrews]
    depends_on: [1]
    status: not_started
  - id: 3
    title: "Joseph in Egypt"
    sources: [Joseph and Slavery for the Hebrews]
    depends_on: [2]
    status: not_started
  - id: 4
    title: "Aaron, Moses, and Their True Lineage"
    sources: [Joseph and Slavery for the Hebrews, Volume III]
    depends_on: [3]
    status: not_started
    notes: "May merge into article 3 if material is short"
  - id: 5
    title: "The Exodus"
    sources: [Volume III]
    depends_on: [2]
    status: not_started
  - id: 6
    title: "Finding Sinai: The Decoding"
    sources: [Volume III]
    depends_on: [2, 5]
    status: not_started
  - id: 7
    title: "Finding Sinai: The Expeditions"
    sources: [Volume III, Diehold expedition writeup, Seattle Times profile]
    depends_on: [6]
    status: not_started
  - id: 8
    title: "The Prophets and the Priests"
    sources: [Volume IV]
    depends_on: [2]
    status: not_started
    notes: "Shape to be decided after reading Volume IV"
  - id: 9
    title: "A Calling"
    sources: [all volumes, God's Day of Judgment, Seattle Times profile]
    depends_on: [1, 2, 3, 4, 5, 6, 7, 8]
    status: not_started
---

# Douglas B. Vogt: Decoding the Hebrew Scriptures — Series Plan

## How to use this file with Claude

Upload or paste this file at the start of each working session. Tell Claude
which article and which step you're on, then supply your reading notes for
that article. Update the `status` fields in the YAML as you go
(`not_started` → `notes_ready` → `outlined` → `drafted` → `revised` → `done`).

Claude should follow the `editorial_stance` and `conventions` in the YAML for
every article: present Vogt's view on its own terms, attribute everything to
him, and cite page numbers from your notes. Claude should not invent page
numbers, quotes, or claims that aren't in your notes; anything unconfirmed
gets marked `[VERIFY]`.

## Phase 0 — Gather sources

- [ ] Identify the title and contents of Volume I of *Decoding the Hebrew Scriptures*
- [ ] Acquire *Joseph and Slavery for the Hebrews* (2017)
- [ ] Acquire *Volume III: The Exodus and Finding the Real Mount Sinai* (2018)
- [ ] Acquire *Volume IV: The Prophets and the Priests* (2023)
- [ ] (Optional) Acquire *God's Day of Judgment* (2007)
- [ ] Save a copy of the Diehold Foundation 1997 expedition writeup
- [ ] Read the 2000 Seattle Times profile
- [ ] Search for Vogt's own lectures, interviews, or videos on his biblical work

## Phase 1 — Reading notes (once per book)

For each book, capture:

- [ ] His argument in the order he builds it, chapter by chapter
- [ ] The evidence he relies on at each step
- [ ] Key terms in his own vocabulary, with his definitions
- [ ] A handful of short, strong quotes with page numbers
- [ ] Worked examples of his decoding method (needed for article 2)
- [ ] Any mention of 12,068 or his solar cycle (needed for articles 1 and 9)
- [ ] Which article(s) each section of notes feeds

## Phase 2 — Articles

Each article follows the same steps:

1. Outline from reading notes (Claude can help)
2. Draft (Claude can help)
3. Check every claim and quote against the book and page
4. Revise and finalize

### Article 1 — Vogt Turns to Scripture
Orients readers to the whole series.

- [ ] Notes ready
- [ ] Outline
- [ ] Draft
- [ ] Fact-check against sources
- [ ] Final

Cover: his premise that the Hebrew scriptures encode hidden information; how
he came to that belief; how 12,068 links the biblical work to his solar
cycle; a preview map of the series.

### Article 2 — The Decoding Method
The methodological heart of the series. Everything after depends on it.

- [ ] Notes ready
- [ ] Outline
- [ ] Draft
- [ ] Fact-check against sources
- [ ] Final

Cover: how he reads the text, step by step, as he explains it; one or two of
his own worked examples walked through in full.

### Article 3 — Joseph in Egypt

- [ ] Notes ready
- [ ] Outline
- [ ] Draft
- [ ] Fact-check against sources
- [ ] Final

Cover: who Joseph was in Egypt, who purchased him, and why 11 of the 12
tribes went into slavery, following his reasoning.

### Article 4 — Aaron, Moses, and Their True Lineage

- [ ] Decide: standalone or merge into article 3
- [ ] Notes ready
- [ ] Outline
- [ ] Draft
- [ ] Fact-check against sources
- [ ] Final

Cover: his account of their ancestry and why he thinks it matters for
understanding the Exodus.

### Article 5 — The Exodus

- [ ] Notes ready
- [ ] Outline
- [ ] Draft
- [ ] Fact-check against sources
- [ ] Final

Cover: his reconstruction of when and how it happened, and the route as he
reads it from the text.

### Article 6 — Finding Sinai: The Decoding

- [ ] Notes ready
- [ ] Outline
- [ ] Draft
- [ ] Fact-check against sources
- [ ] Final

Cover: how the text and the number led him to a specific location; why he
believes the traditional sites are wrong.

### Article 7 — Finding Sinai: The Expeditions

- [ ] Notes ready
- [ ] Outline
- [ ] Draft
- [ ] Fact-check against sources
- [ ] Final

Cover: the 1997 and 1999 trips as his story — what he looked for, what he
found, what he believes it confirms, and his reasons for keeping the exact
location private.

### Article 8 — The Prophets and the Priests

- [ ] Read Volume IV and decide the article's shape
- [ ] Notes ready
- [ ] Outline
- [ ] Draft
- [ ] Fact-check against sources
- [ ] Final

### Article 9 — A Calling
The capstone. Write last.

- [ ] Notes ready
- [ ] Outline
- [ ] Draft
- [ ] Fact-check against sources
- [ ] Final

Cover: his own account of believing he was chosen to bring this to light; how
he sees the biblical "Day of Judgment" connecting to his solar model; how the
whole body of work fits together in his view.

## Phase 3 — Series wrap-up

- [ ] Read all articles in order for consistent terminology and voice
- [ ] Add cross-links between articles
- [ ] Write a short series index or landing page
- [ ] (Separate, optional) Write your own commentary or scoring as a distinct piece

## Prompt template for a drafting session

```
Here's my series plan [attach this file] and my reading notes for
Article [N]: [title]. Please [outline / draft / revise] it following the
editorial_stance and conventions in the plan. Target [X] words. Mark
anything not supported by my notes as [VERIFY].
```
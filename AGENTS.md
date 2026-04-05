# AGENTS.md — Personal Blog / FPL Dashboard Guide

This repo is the published surface for Nick's generated content.

It is both:
- a blog publishing target
- a dashboard-style presentation layer for FPL content

Future agents should treat this repo as a **rendered/public-facing output layer**, not the primary ingestion engine.

The upstream generator is:
- `~/.openclaw/workspace/projects/content-crawler`

---

## What lives here

This repo contains:
- generated HTML posts
- generated markdown source files for posts
- index/listing pages
- dashboard-style pages such as `fpl.html`

In practice:
- `content-crawler` creates or updates content
- this repo stores the publishable artifacts

---

## Mental model

Think of the system as three layers:

### 1) Source ingestion + summarization
Repo:
- `~/.openclaw/workspace/projects/content-crawler`

This layer:
- fetches YouTube/podcast/news content
- transcribes media
- summarizes content
- writes blog posts
- emits structured FPL intelligence

### 2) Published content surface
Repo:
- `~/.openclaw/workspace/projects/personal-blog`

This layer:
- holds the actual `.html` pages
- holds `.md` source files with frontmatter
- includes dashboard pages like `fpl.html`

### 3) Structured FPL data snapshot
File:
- `~/.openclaw/workspace/data/ffs_intel.json`

This layer:
- provides machine-readable FPL intelligence
- is useful for dashboards, downstream automations, newsletters, and future wiki-like views

---

## What `fpl.html` is

`fpl.html` is a dashboard-style FPL page.

It may be updated by the crawler, including injected sections such as:
- “Today's FPL Intel”
- premium bullets / insight cards
- other synthesized FPL guidance

If `fpl.html` looks wrong, stale, or contradictory, inspect:
1. `fpl.html`
2. markdown posts in this repo
3. `~/.openclaw/workspace/data/ffs_intel.json`
4. the crawler code in `content-crawler/main.py`
5. the crawl log in `~/.openclaw/workspace/data/crawler.log`

---

## What the “wiki” likely means in practice

There may not be a separate formal wiki repo yet.

Operationally, the “wiki/dashboard” concept currently maps to:
- structured FPL reference content in markdown/html here
- machine-readable FPL snapshot data in `ffs_intel.json`
- synthesized dashboard views such as `fpl.html`

So if a future request says:
- “update the wiki”
- “check the dashboard”
- “why is the FPL page wrong?”

…start with this repo plus the crawler and JSON snapshot, not with a blind filesystem search.

---

## Common file types here

### `YYYY-MM-DD-*.html`
Published blog/article pages.

### `YYYY-MM-DD-*.md`
Source markdown posts with frontmatter.
These are especially important because `ffs_intel_writer.py` reads them to build `ffs_intel.json`.

### `fpl.html`
Dashboard-style FPL landing page / premium insights page.

---

## How data flows into this repo

```text
content-crawler
  -> generates summaries/articles
  -> writes .html and .md posts here
  -> may update fpl.html
  -> rebuilds blog post indexes
```

Separately:

```text
markdown posts in this repo
  -> parsed by ffs_intel_writer.py
  -> emitted as ~/.openclaw/workspace/data/ffs_intel.json
```

This means this repo is both:
- a publishing destination
- an input source for structured FPL intelligence extraction

---

## Important operational rule

Do not assume files here are hand-authored.
A lot of content is generated.

Before editing anything substantial:
1. identify whether it is generated or manual
2. identify the upstream generator
3. prefer fixing the generator if the problem is systemic

Example:
- If `fpl.html` contains malformed injected intel, the correct fix may be in `content-crawler/main.py`, not in direct manual HTML edits.

---

## Debugging guide

If the blog/dashboard looks broken:

### Check generated outputs
- recent `.html` posts
- recent `.md` posts
- `fpl.html`

### Check structured data
- `~/.openclaw/workspace/data/ffs_intel.json`

### Check upstream generator
- `~/.openclaw/workspace/projects/content-crawler/main.py`
- `~/.openclaw/workspace/projects/content-crawler/blog/generator.py`
- `~/.openclaw/workspace/projects/content-crawler/ffs_intel_writer.py`

### Check runtime evidence
- `~/.openclaw/workspace/data/crawler.log`
- `~/.openclaw/workspace/data/crawl-state.json`
- `combined-daily-push.service` / timer

---

## For future agents

When the user asks about:
- blog posts
- FPL dashboard
- wiki content
- stale FPL intel
- missing generated pages

Use this default path:

1. inspect `personal-blog`
2. inspect `ffs_intel.json`
3. inspect `content-crawler`
4. inspect the crawl log/state

That order usually gets to root cause quickly.

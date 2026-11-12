# Weekly Posts: How It Works

One new blog post every Tuesday, built around a real Red Agave project or one specific decision, titled the way people search.

Why: Southern Love Landscaping holds 62% visibility on our tracked searches mostly through volume. They have published about one post a week since January 2023 (263 posts), each titled like a search ("What to Look for in a Deck Builder in Austin, TX"). We match the cadence, but every post shows a real build and only checked facts. They can't copy that.

Everything in `.claude/` is blocked from the public site by `netlify.toml`.

## Files

| File | What it is |
|---|---|
| `CALENDAR.md` | The queue (next 12 weeks), plant notes, and the published log |
| `posts/*.md` | The source of every post. Edit here, rebuild, never hand-edit `blog/<slug>.html` |
| `build_post.py` | Turns a source file into `blog/<slug>.html` and registers it across the site |
| `archive-content-plan-2026.md` | The older 50-post plan (moved out of `/blog/` so it isn't public) |

## The two series

**Weekly post (every Tuesday).** Two formats:
- **Project:** "[Service] in [Area]: [the decision that shaped it]". One or two real builds, with photos and a spec list.
- **Decision:** "[Service] in Austin, TX: [one specific question]". One decision a homeowner faces, answered, with a real project as the example.

**Plant notes (when an Instagram plant carousel goes out).** Short posts like the Pink Fairy Duster post. Use the carousel's plain photos (never slides with text on them), put them in `images/plants/<plant-slug>/`, use Wildflower Center data, and set `instagram:` to the post's link. When the plant is a city page's featured plant, link that city page.

## Owner rules (never break)

- **Facts only.** Every detail comes from Jensen, his photos, or a source found during research and named in the post. No invented project details, sizes, timelines, or business policies.
- **Never sound unsure.** No "probably", "we think", "it depends". If a fact can't be confirmed, leave it out.
- Say **"built by our own crew"**. Never "never subcontracted".
- **No design fee:** "free consultation, CAD plan included".
- **No Google Business Profile** content.
- **No prices in weekly posts.** Link the cost guide instead. Cost guides are the only blog posts that show prices (`price_ok: yes`).
- **Name the area, not the homeowner.**
- **Drain pipe:** we use both rigid PVC and corrugated pipe.
- **Outdoor kitchens:** built from IPE, steel, CMU block, tile, and concrete. CMU block is the base, and stone or brick goes over it. Tile kitchens are wood-framed and sheathed in concrete board. Never butcher block, and never "mild steel exclusively".
- **Guides stay out of the main menu.**
- **Unconfirmed case studies are not fact sources.** `projects/westlake-steel`, `projects/lakeway-hardscape`, `projects/tarrytown-glow`, and parts of `projects/pflugerville-xeriscape` describe work their photos do not show. Never take a fact from them until Jensen confirms the project.
- Confirmed project locations: kitchens (West Lake Hills and East Austin), Bee Cave deck, Cedar Park rusted steel pergola (built from scratch; the owners wanted it to rust), South Austin screened room with skylight, Hopeland (Circle C), Ulit (East Austin, teak deck), Blazyk (Circle C), Southeast Austin water feature and two fire pits (`projects/se-austin-fire-water/`; the job is called "Silhouette" internally, a name that never goes on the site; the square steel piece with the tree is a planter, not a fire bowl).

## Shape of every post

- Title tag 60 characters or fewer. Description 120–155 characters.
- **First paragraph is the answer:** who built what, where, in 2–3 sentences, with a bold lead. AI assistants quote this.
- 3 or more H2s phrased as the questions people ask.
- At least one real photo block. Alt text says what and where.
- Project posts get a spec list. Only list what is visible or confirmed.
- Links: the service page, the city page, and a case study or guide, all as clean addresses (no `.html`).
- FAQ last, with 3–5 questions. The builder makes the FAQ schema from the visible text, so they always match.
- 700–1,400 words.

## Every week

1. Take the next row in `CALENDAR.md`, or a fresh project Jensen just sent.
2. Gather facts: Jensen's photos and notes, plus a search for any outside fact (name the source in the text).
3. Save photos as WebP, with EXIF stripped, in `images/projects/<project>/` at 1200 and 800 wide.
4. Copy the latest `posts/*.md` as a starting point, then write the new one.
5. Check it: `python3 .claude/weekly-posts/build_post.py .claude/weekly-posts/posts/<file>.md --check`. Fix whatever it flags.
6. Build it: run the same command without `--check`. This writes `blog/<slug>.html` and adds it to the blog index (top card, guide list, schema), `sitemap.xml`, the `.html` redirect in `netlify.toml`, and `llms.txt`.
7. Link to the post from 2 or more pages: its service page, city page, or case study. The builder reports the count.
8. Preview it locally, commit, push to `main`, and confirm it's live.
9. Add it to the published log in `CALENDAR.md`. Jensen requests indexing in Search Console.

## Source format

```
---
slug: outdoor-kitchen-under-roof-austin-tx       # becomes /blog/<slug>
date: 2026-11-10
format: project                                   # project | decision | plant
target: outdoor kitchen austin; ...               # searches it goes after (goes in schema "about")
title: Outdoor Kitchens Under a Roof in Austin, TX | Red Agave     # <= 60
description: ...                                  # 120-155
h1: Outdoor Kitchens in Austin, TX: Why We Build Under a Roof
crumb: Outdoor Kitchens Under a Roof
excerpt: one line for the blog card and llms.txt
image: images/projects/kitchens/covered-cedar-kitchen-1200.webp   # share image
cta_title: Design Your Outdoor Kitchen            # optional
cta_sub: Owner-designed &middot; ...              # optional
instagram: https://www.instagram.com/p/...        # optional (plant notes)
price_ok: yes                                     # only for cost guides
related:
  - outdoor-kitchen-ideas-austin-tx | Title | One-line excerpt
---
**Bold lead sentence.** Rest of the answer paragraph.

[[fig images/a.webp | alt text ;; images/b.webp | alt text || optional caption]]

## A Question as an H2?

Paragraph with a [link](../services/outdoor-kitchens-austin-tx) and **bold**.

- **Label:** list item

## FAQ: Questions We Hear

### Question?
Answer.
```

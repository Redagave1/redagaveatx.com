---
name: weekly-post
description: Write and publish this week's Red Agave blog post (or a plant note from an Instagram carousel) using the weekly-posts system in .claude/weekly-posts. Use when Jensen says "weekly post", "this week's post", "next post", "blog post", sends project photos for a post, or shares a plant carousel.
---

# Weekly Post

Read `.claude/weekly-posts/README.md` first. It holds the owner rules, the post shape, and the source format. Follow it exactly.

1. **Pick the topic.** Use the next unpublished row in `.claude/weekly-posts/CALENDAR.md`, unless Jensen sent a new project or a plant carousel, which goes first. If the row says "Needs:", ask Jensen for exactly those items, in one message, before writing.
2. **Gather facts.** Use only Jensen's photos and words, the site's existing case-study text, and outside facts confirmed by a search (name the source in the post). Look at every photo before describing it. Never guess wood species, materials, sizes, or locations. If something is unknown, leave it out. Never write it as uncertain.
3. **Prepare photos.** Convert to WebP with EXIF stripped (Pillow lives in `/Library/Frameworks/Python.framework/Versions/3.14/bin/python3`) and save at 1200 and 800 wide in `images/projects/<project>/`, or `images/plants/<plant-slug>/` for plant notes. Never use carousel slides that have text on them.
4. **Write the source** as `.claude/weekly-posts/posts/<date>-<slug>.md`, starting from the most recent file in that folder.
5. **Check, then build.** Run `python3 .claude/weekly-posts/build_post.py <file> --check` and fix every problem. Then run it without `--check`.
6. **Link it in.** Add contextual links to the post from at least 2 pages (its service page, its city page, its case study) with the Edit tool.
7. **Verify.** Preview through the local server and the browser pane: every image loads, every link works, the FAQ shows.
8. **Publish.** Stage only the files you touched (never `AUDIT-2026-11.md`). Commit, push the branch and `main`, then curl the live address until it returns 200.
9. **Log it.** Mark the row in `CALENDAR.md` as published and add a line to the published log with the search's position before. Tell Jensen the live link, and ask him to request indexing for it in Search Console.

Never mention Google Business Profile. Never put prices in a weekly post.

# Regular project pages

Jensen, 2026-11-20: "I want to do signature projects and then regular projects. Let me start feeding you regular projects we probalby should do street names too?"

Two tiers:
- **Signature projects**: the long pages on `featured.html`, built one script each in `.claude/service-pages/` (see that README).
- **Regular projects**: short pages named by street, listed on `/projects/` (`projects/index.html`). This folder builds them.

## Add a project

1. Jensen sends photos and a few words (street, year, what was built). Look at every photo. Leave out any that show a house number.
2. Save the photos as WebP in `images/projects/<slug>/`, named `NN-what-it-shows-<width>.webp`, at the widest size you have and at 800. Make a 1200 by 630 share image.
3. Add an entry to `projects.json` (copy Signal Point).
4. Build and register: `python3 -I .claude/regular-projects/build_regular.py . --register`
   It writes `projects/<slug>.html`, rewrites `projects/index.html`, and adds any missing lines to `sitemap.xml`, `netlify.toml` and `llms.txt`.
5. Preview, commit the files you touched, push the branch and `main`.

## Rules

- Name: the street (no house number, no customer name). The area comes after it. The year is the build year.
- Facts: only Jensen's words and what a photo plainly shows. If it is not confirmed, leave it out (for example gas or wood, sizes, plant names he did not give).
- Check the build year against the photo dates (EXIF) when Jensen gives a bare number: "2018 Signal Point" was the year, not a house number.
- The area can be looked up from the street (Signal Point is in 78724, East Austin). Tell Jensen which area you used.
- No prices. Never "bare steel". "Built by our own crew." "Free consultation, CAD plan included."
- An entry with `"external": true` is a page built somewhere else (for example by a `.claude/service-pages/` script); it is only listed on the index.

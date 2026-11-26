# Google indexing status (read in Search Console, 2026-11-26)

Why this matters: a page Google has not read cannot rank, cannot show in the map box results text, and cannot be quoted by AI tools that search the web. On 2026-11-26 this turned out to be the main reason the new pages show nothing in the rank tracker and the AI visibility tool.

## What Search Console showed (Page indexing report, last update 2026-11-22)

- Indexed: 85 pages. Not indexed: 108.
- "Discovered - currently not indexed": 83 pages, every one with "Last crawled: N/A" (Google knows the address and has never read the page).
- "Page with redirect": 22 (the old `.html` addresses, expected). "Not found (404)": 1. "Crawled - currently not indexed": 2.
- Crawl stats, last 90 days: 682 crawl requests in total (about 8 a day), 33% of them answered with a 301 redirect, 7% with 404. Host status: no problems. Average response 137 ms.
- Sitemap `/sitemap.xml`: Success, 200 pages discovered, last read 2026-11-23. Five page addresses were submitted in the sitemap box by mistake on 2026-11-26 and show "1 error" each; they do no harm and can be removed.
- The site's own links are clean (no link ends in `.html`), so the redirects Google hits are old addresses it already knew.

## The 83 pages Google had never read

Services (7): custom-planters, drainage, landscape-design, luxury-landscaping, masonry-concrete, patios, turf-installation.

City pages (11): buda-kyle, cedar-park, dripping-springs, lakeway, mueller, pflugerville, rollingwood, round-rock, steiner-ranch, tarrytown, westlake-hills.

Projects (7): blazyk, flycatcher, hopeland, madison, and three retired addresses (lakeway-hardscape, tarrytown-glow, westlake-steel).

Other (2): /reviews, /blog/ (the blog index).

Blog posts (56): arroyo-sweetwood, artichoke-agave, backyard-design, backyard-makeover, best-fire-pit-ideas-austin, best-landscapers, caliche-soil-preparation, cold-hardy-agaves-central-texas, concrete-vs-paver-patio, custom-fire-pits, custom-pergola-build-south, deck-builder, decomposed-granite-landscaping, dioon-vs-sago-palm, drainage-company, firecracker-fern, flagstone-mortar-cracking, freeze-protection-plants, giant-hesperaloe, gravel-landscaping-ideas, hardscaping, high-end-landscaping, ipe-vs-composite-decking, landscape-design-build, landscape-design-services, landscape-designer, landscape-lighting-cost, landscape-lighting-guide, landscape-lighting-installation, limestone-pavers-vs-concrete, natural-turf-vs-artificial-turf, outdoor-kitchen-ideas, outdoor-kitchen-under-roof, outdoor-living-spaces, patio-cost, patio-design-ideas, pavers-with-artificial-turf, pergola-builder, plants-that-survive-austin-summer, pool-design, pool-landscaping-ideas, red-fairy-duster, retaining-wall-contractor, retaining-wall-cost, retaining-wall-permit, shade-structure-ideas, steel-edging-cut-into-boulders, steel-edging-fabrication, steel-vs-aluminum-pergola, synthetic-turf-cost, texas-tuberose, water-feature-cost, water-feature-fire-pits-southeast, whales-tongue-agave, xeriscape-vs-traditional-lawn, yucca-rostrata.

Not in that list because Google had not even registered them by 2026-11-22: everything published from 2026-11-20 on (the question posts, the regular project pages, the new service pages, the HOA guides, the gulf muhly guide). A `site:` search on 2026-11-26 found none of the question posts, and showed the July version of the best deck materials guide.

## Order for indexing requests (URL inspection, then "Request indexing"; Google caps how many per day)

1. /services/landscape-design-austin-tx
2. /services/patios-austin-tx
3. /services/luxury-landscaping-austin-tx
4. /blog/outdoor-kitchen-builders-austin-tx
5. /blog/do-outdoor-kitchens-add-value-austin-tx
6. /blog/pergola-vs-pavilion-vs-shade-sail-austin-tx
7. /blog/ipe-vs-composite-decking-austin-tx
8. /blog/best-deck-materials-austin-tx
9. /blog/xeriscaping-benefits-austin-tx
10. /blog/hardscape-vs-xeriscape-austin-tx

Then: the 11 city pages, the four signature project pages, /reviews, the other four service pages, the three HOA guides, the gulf muhly guide, best-landscapers, landscape-designer, hardscaping, deck-builder, pergola-builder, and the rest of the posts.

## Rank tracker and AI tool readings the same day

- Rank tracker, eight searches tracked for Southern Love: every one of their top positions carries the map pin and points at their home page, so those are map box placements. Red Agave in regular results (Search Console, 28 days): austin landscapers 33.4 (135 impressions), landscape design austin 30.0 (220), landscaping austin tx 31.4 (164), austin landscape design 32.3 (232), hardscaping services no impressions.
- AI visibility tool, "Top prompts you're losing": outdoor kitchen companies, deck materials, pergola and shade options, IPE vs cedar vs composite, outdoor kitchens and value. Each has a page on the site since 2026-11-20 (two are reworks of July posts); none of the new versions was in Google yet.

## Requests made, and the daily run (2026-11-26)

Jensen said yes to requesting indexing through Search Console in Chrome, and then asked for it to run by itself every day until done.

- Requested 2026-11-26 (each one answered "Indexing requested"): the ten pages in the order above, then /locations/westlake-hills-tx. Tarrytown and Lakeway were tried in a batch that timed out, so their result was not seen. Cedar Park turned out to be on Google already. Google answered "Quota Exceeded" after that, so the daily cap is about 11 to 13.
- The five page addresses in the sitemap box were removed the same day; only /sitemap.xml is listed now (Success, 200 pages).
- Daily run: scheduled task `red-agave-indexing` (9:11 AM every day, runs while the Claude desktop app is open). Its instructions are in `~/.claude/scheduled-tasks/red-agave-indexing/SKILL.md` and its progress file is `queue.tsv` in the same folder (204 rows: todo, requested, indexed). `indexing-queue.tsv` in this folder is the starting copy only. The task turns itself off when no row is left.
- A URL typed straight into the address bar as `/search-console/inspect?...&id=<url>` gives a 404; the inspection has to be started from the box at the top of Search Console.

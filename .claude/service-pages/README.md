# Service page builder

Builds a single-service page under `services/` from the shell (head, nav, footer) of
`services/steel-retaining-walls-austin-tx.html`.

    python3 .claude/service-pages/make_edging.py . [--register]

- `svc_lib.py`: `build(ROOT, spec)` writes the page and runs the checks (title 60 or under,
  description 120 to 155, banned wording, missing links and images, valid JSON-LD).
  `register(ROOT, slug, card_html, llms_line, date)` adds the hub card, sitemap entry,
  netlify redirect and llms.txt line. Run it once per page.
- `make_hardscape.py`, `make_edging.py`: one script per page. Copy one to start a new page.
- `make_landscape_design.py` rebuilds the landscape design page (2026-11-25): six plans beside the finished yards.
  It adds its own CSS for the plan and photo pairs (`.pb`), reads image sizes with Pillow, and has no `--register` step
  because the page already had its card, sitemap line and redirect.
- `services/retaining-walls-austin-tx.html` was built by an earlier one-off script and then
  edited by hand (limestone photo, hardscaping link). Edit that file directly.

Rules: facts only from text already on the site or from Jensen. No prices (link the cost guide).
No customer or internal job names in visible text. No em dashes. Look at every photo before
using it: several old alt texts describe the wrong photo.
Never write "bare steel" (Jensen, 2026-11-18: it sounds like AI). Say "steel before the black
penetrating sealer" or just "steel". All three builders refuse the phrase.

## Signature project page

`make_chrysler_bend.py` builds `projects/chrysler-bend.html` (Signature Project 09, the Southeast
Austin floating triangle planter) from the shell of `projects/dormarion.html`:

    python3 .claude/service-pages/make_chrysler_bend.py .

Copy it for the next project page. A new project also needs: a card at the end of the grid and an
entry in the ItemList schema in `featured.html`, a `sitemap.xml` line, a `netlify.toml` redirect,
and a line under "Signature Project Pages" in `llms.txt`. Jensen names the project (Chrysler Bend
was his name for this one). When a job has few photos, cut zoom-ins from them for the pinned
section (full-width bands, 1125 by 640).

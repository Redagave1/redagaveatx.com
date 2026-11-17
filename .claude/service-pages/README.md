# Service page builder

Builds a single-service page under `services/` from the shell (head, nav, footer) of
`services/steel-retaining-walls-austin-tx.html`.

    python3 .claude/service-pages/make_edging.py . [--register]

- `svc_lib.py`: `build(ROOT, spec)` writes the page and runs the checks (title 60 or under,
  description 120 to 155, banned wording, missing links and images, valid JSON-LD).
  `register(ROOT, slug, card_html, llms_line, date)` adds the hub card, sitemap entry,
  netlify redirect and llms.txt line. Run it once per page.
- `make_hardscape.py`, `make_edging.py`: one script per page. Copy one to start a new page.
- `services/retaining-walls-austin-tx.html` was built by an earlier one-off script and then
  edited by hand (limestone photo, hardscaping link). Edit that file directly.

Rules: facts only from text already on the site or from Jensen. No prices (link the cost guide).
No customer or internal job names in visible text. No em dashes. Look at every photo before
using it: several old alt texts describe the wrong photo.

"""Builds projects/pool-ipe-deck-bamboo-screen.html (regular project, listed on /projects/).
Facts: the approved name and description (Houzz gallery project 13) and what the four photos plainly show.
The description says "Built by Red Agave Landscape" (not "designed and built"), and it does not say who built the pool,
so the page only says we built the ipe deck around it.
Photos are the gallery originals DSC04039 to DSC04042; 800-wide copies and zoom-ins come from cut_project_zooms.py.
Run: python3 -I .claude/service-pages/make_pool_ipe_deck_bamboo_screen.py .
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from proj_lib import build, IM

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
D = "images/projects/pool-ipe-deck-bamboo-screen/"
G = "images/gallery/"
NX = "images/projects/boulder-stream-steel-fire-trough/"

def zoom(alt, name):
    return IM(alt, (f"{D}{name}-800.webp", 800), (f"{D}{name}-1125.webp", 1125))

FAQS = [
 ("What wood is this pool deck?",
  "Ipe. Red Agave Landscape built this ipe deck around a dark pool in Austin."),
 ("What screens the pool?",
  "Bamboo. A bamboo screen runs along the fence, behind the row of loungers."),
 ("How does the deck meet the pool?",
  "At a band of pale coping. The deck runs along two sides of the pool, and at the corner the boards turn and meet on a diagonal."),
 ("Does Red Agave build ipe decks in Austin?",
  "Yes. Red Agave Landscape builds custom decks in ipe across the Austin area, and every deck is built by our own crew. Every project starts with a free consultation, and the CAD plan is included."),
]

SPEC = {
 "slug": "pool-ipe-deck-bamboo-screen",
 "date": "2026-11-20",
 "title": "Pool With Ipe Deck and Bamboo Screen, Austin | Red Agave",
 "desc": "An ipe deck built by Red Agave Landscape around a dark pool in Austin, with a row of loungers and a bamboo screen along the fence. Photos and details.",
 "og_title": "Pool With Ipe Deck and Bamboo Screen, Austin | Red Agave",
 "headline": "Pool With Ipe Deck and Bamboo Screen in Austin, TX",
 "schema_desc": "An ipe deck built around a dark pool, with a row of loungers and a bamboo screen along the fence. Built by Red Agave Landscape.",
 "schema_images": [D + "pool-ipe-deck-share.webp", G + "DSC04039.webp", G + "DSC04040.webp"],
 "share": D + "pool-ipe-deck-share.webp",
 "area": "Austin, TX",
 "place": "Austin, Texas",
 "crumb": "Pool With Ipe Deck and Bamboo Screen",
 "h1": "Pool With Ipe Deck and Bamboo Screen",
 "meta_a": "Built by Red Agave Landscape",
 "kicker": "Ipe &middot; Dark pool &middot; Bamboo",
 "hero": IM("Ipe deck around a dark pool with pale coping in Austin, with a row of loungers on the deck, a wood rocking chair, and a bamboo screen along the fence",
            (D + "ipe-deck-dark-pool-loungers-bamboo-800.webp", 800), (D + "ipe-deck-dark-pool-loungers-bamboo-1200.webp", 1200), (G + "DSC04039.webp", 1600)),
 "hero_pos": "50% 60%",
 "nar_eb": "The Project &middot; Austin",
 "h2": "Ipe around dark water. Bamboo along the fence.",
 "pulse": "Ipe &middot; Dark Pool &middot; Bamboo",
 "paras": [
  'Red Agave Landscape built this ipe <a href="../services/custom-decks-austin-tx">deck</a> around a dark pool in Austin. A row of loungers sits on the deck, and a bamboo screen runs along the fence behind them.',
  'The deck runs along two sides of the pool and meets a band of pale coping at the water. At the corner of the pool the boards turn, and the two runs meet on a diagonal. The bamboo grows above the fence line, with broad-leaved plants under it.',
  'Our guide to <a href="../blog/ipe-vs-composite-decking-austin-tx">ipe and composite decking</a> compares the two for Austin yards.',
 ],
 "figs": [
  {"im": IM("Ipe deck boards meeting on a diagonal at the corner of a dark pool, with loungers and a bamboo screen along the fence behind, in Austin",
            (D + "ipe-deck-corner-bamboo-screen-800.webp", 800), (G + "DSC04040.webp", 1600)),
   "ratio": "4/3", "cap_a": "01 &middot; Deck", "cap_b": "Boards meet on a diagonal"},
  {"im": IM("Ipe deck in the foreground beside a dark pool with pale coping, with a row of loungers and tall bamboo along the fence under trees, in Austin",
            (D + "ipe-deck-pool-loungers-under-trees-800.webp", 800), (G + "DSC04041.webp", 1200)),
   "cap_a": "02 &middot; Pool", "cap_b": "Dark water / coping"},
  {"im": IM("Wood rocking chair on an ipe deck beside a dark pool with pale coping, with loungers and a bamboo screen behind, in Austin",
            (D + "ipe-deck-rocking-chair-pool-coping-800.webp", 800), (G + "DSC04042.webp", 1600)),
   "ratio": "4/3", "cap_a": "03 &middot; Screen", "cap_b": "Bamboo along the fence"},
 ],
 "statement": ("Ipe and Dark Water", "Deck. Pool. <em>Bamboo.</em>"),
 "pins": [
  {"im": zoom("Close view of tall bamboo and a panel of bamboo poles along a wood fence, with broad-leaved plants below, behind an ipe deck and a dark pool in Austin",
              "zoom-bamboo-screen-along-fence"),
   "eb": "Screen &middot; 01", "h": "Bamboo", "pulse": "Along the Fence",
   "text": "Bamboo runs along the fence behind the loungers and grows above the fence line. A panel of bamboo poles covers part of the fence, with broad-leaved plants at its foot."},
  {"im": zoom("Close view of a dark pool with pale coping and an ipe deck with loungers beside it, in Austin",
              "zoom-dark-pool-pale-coping-ipe-deck"),
   "eb": "Water &middot; 02", "h": "Dark Pool", "pulse": "Pale Coping",
   "text": "The pool is dark, with a band of pale coping around it. The water reflects the trees and the bamboo above it."},
  {"im": zoom("Close view of ipe deck boards and pale pool coping, with a wood rocking chair at the edge of a dark pool, in Austin",
              "zoom-ipe-deck-boards-rocking-chair"),
   "eb": "Deck &middot; 03", "h": "Ipe", "pulse": "Two Sides of the Pool",
   "text": "The ipe deck runs along two sides of the pool and meets the coping in a straight line. At the corner the boards turn and meet on a diagonal."},
 ],
 "bp": {
  "title": "What was <em>built</em>.",
  "chapters": [
   ("01 / Deck", "Ipe", ["Ipe deck boards", "Deck on two sides of the pool", "Boards meet on a diagonal at the corner", "Deck meets the pale pool coping"]),
   ("02 / Screen", "Bamboo", ["Bamboo screen along the fence", "Bamboo above the fence line", "Panel of bamboo poles on the fence"]),
  ],
  "meta": [("Area", "Austin"), ("Deck", "Ipe"), ("Water", "Dark Pool"), ("Screen", "Bamboo")],
 },
 "faqs": FAQS,
 "links": [
  ("../services/custom-decks-austin-tx", "Custom decks"),
  ("../services/pools-austin-tx", "Pools"),
  ("../blog/ipe-vs-composite-decking-austin-tx", "Ipe vs composite decking"),
  ("../blog/pool-landscaping-ideas-austin-tx", "Pool landscaping ideas"),
  ("./", "All projects"),
  ("../contact", "Free consultation"),
 ],
 "next": {"href": "boulder-stream-steel-fire-trough", "eb": "Next Project", "title": "Boulder <em>Stream.</em>",
          "im": IM("Steel fire trough burning above a stream that runs through boulders at dusk in Austin",
                   (NX + "steel-fire-trough-boulder-stream-dusk-800.webp", 800), (NX + "steel-fire-trough-boulder-stream-dusk-1200.webp", 1200))},
}

build(ROOT, SPEC)

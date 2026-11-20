"""Builds projects/triangle-fire-pit-stock-tank-pool.html (regular project, listed on /projects/).
Facts: the approved name and description (Houzz gallery project 16) and what the four photos plainly show.
Photos are gallery originals IMG_8345, 8339, 8347, 8343; 800-wide copies and zoom-ins come from cut_project_zooms.py.
Run: python3 -I .claude/service-pages/make_triangle_fire_pit_stock_tank_pool.py .
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from proj_lib import build, IM

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
D = "images/projects/triangle-fire-pit-stock-tank-pool/"
G = "images/gallery/"
NX = "images/projects/pool-ipe-deck-bamboo-screen/"

def zoom(alt, name):
    return IM(alt, (f"{D}{name}-800.webp", 800), (f"{D}{name}-1125.webp", 1125))

FAQS = [
 ("Can a fire pit and a water feature be one piece?",
  "Yes. This triangle steel fire pit has a steel spillway that pours into the stock tank pool beside it."),
 ("Can a fire pit be built in a custom shape?",
  "Yes. This one is a triangle, built in steel and set at the edge of a round stock tank pool."),
 ("What fills the fire pit?",
  "Lava rock at the center, where the fire burns, and dark stone around it."),
 ("Who designed and built it?",
  "Red Agave Landscape designed and built it. Every project starts with a free consultation, and the CAD plan is included."),
]

SPEC = {
 "slug": "triangle-fire-pit-stock-tank-pool",
 "date": "2026-11-20",
 "title": "Triangle Fire Pit and Stock Tank Pool, Austin | Red Agave",
 "desc": "A triangle steel fire pit at the edge of a stock tank pool in Austin, with a steel spillway that pours into the water. Designed and built by Red Agave.",
 "og_title": "Triangle Steel Fire Pit and Stock Tank Pool, Austin | Red Agave",
 "headline": "Triangle Steel Fire Pit and Stock Tank Pool in Austin, TX",
 "schema_desc": "A triangle steel fire pit set at the edge of a stock tank pool, with a steel spillway that pours into the water. Designed and built by Red Agave Landscape.",
 "schema_images": [D + "triangle-fire-pit-share.webp", G + "IMG_8345.webp", G + "IMG_8339.webp"],
 "share": D + "triangle-fire-pit-share.webp",
 "area": "Austin, TX",
 "place": "Austin, Texas",
 "crumb": "Triangle Steel Fire Pit and Stock Tank Pool",
 "h1": "Triangle Steel Fire Pit and Stock Tank Pool",
 "meta_a": "Designed and built by Red Agave Landscape",
 "kicker": "Steel &middot; Fire &middot; Spillway &middot; Stock tank",
 "hero": IM("Triangle steel fire pit burning at the edge of a round stock tank pool, with a sheet of water falling from its steel spillway into the pool and turf around it, in Austin",
            (D + "triangle-fire-pit-spillway-stock-tank-pool-800.webp", 800), (G + "IMG_8345.webp", 1200)),
 "hero_pos": "50% 42%",
 "nar_eb": "The Project &middot; Austin",
 "h2": "Fire on the rim. Water over the edge.",
 "pulse": "Steel &middot; Fire &middot; Stock Tank",
 "paras": [
  'Red Agave Landscape designed and built this triangle steel <a href="../services/fire-pits-austin-tx">fire pit</a> in Austin. It is set at the edge of a stock tank pool, and a steel spillway pours from it into the water.',
  'One edge of the triangle reaches over the rim of the tank. The spillway runs under that edge, and the water falls from it in a sheet. The fire burns at the center over lava rock, with dark stone filling the rest of the steel.',
  'The fire pit stands on a tapered steel base, set in turf beside concrete paving. The fire and the falling water sit together at the edge of the pool. For more of both, see our <a href="../services/water-features-austin-tx">water features</a>.',
 ],
 "figs": [
  {"im": IM("Triangle steel fire pit seen from above, filled with dark stone around a fire burning over lava rock, with water falling from its edge into a stock tank pool, in Austin",
            (D + "triangle-fire-pit-from-above-spillway-800.webp", 800), (G + "IMG_8339.webp", 1440)),
   "cap_a": "01 &middot; Fire", "cap_b": "Lava rock / dark stone"},
  {"im": IM("Low view of a steel spillway pouring a sheet of water from under the edge of a triangle steel fire pit into a stock tank pool, with the tapered steel base below, in Austin",
            (D + "steel-spillway-tapered-base-stock-tank-800.webp", 800), (G + "IMG_8347.webp", 1440)),
   "cap_a": "02 &middot; Water", "cap_b": "Steel spillway"},
  {"im": IM("Point of a triangle steel fire pit seen from above, with fire burning over lava rock at the center, dark stone around it, turf and concrete at the sides, and pool water behind, in Austin",
            (D + "triangle-fire-pit-point-turf-concrete-800.webp", 800), (G + "IMG_8343.webp", 1200)),
   "cap_a": "03 &middot; Steel", "cap_b": "Triangle / turf"},
 ],
 "statement": ("Fire Over the Rim", "Steel. <em>Water below.</em>"),
 "pins": [
  {"im": zoom("Close view of a sheet of water falling from a steel spillway under the edge of a steel fire pit into a stock tank pool, in Austin",
              "zoom-steel-spillway-into-stock-tank"),
   "eb": "Water &middot; 01", "h": "The Spillway", "pulse": "Steel &middot; Sheet of Water",
   "text": "A steel spillway runs under the edge of the fire pit and pours into the stock tank pool. The water leaves the steel in a sheet and breaks the surface below."},
  {"im": zoom("Close view of fire burning over lava rock at the center of a triangle steel fire pit, with dark stone around it and a stock tank pool beside it, in Austin",
              "zoom-fire-lava-rock-dark-stone"),
   "eb": "Fire &middot; 02", "h": "The Fire", "pulse": "Lava Rock &middot; Dark Stone",
   "text": "The fire burns at the center of the triangle, over lava rock. Dark stone fills the rest of the steel, out to the three edges."},
  {"im": zoom("Close view of flames over lava rock ringed by dark stone inside a triangle steel fire pit, with turf at the sides, in Austin",
              "zoom-triangle-fire-pit-point"),
   "eb": "Steel &middot; 03", "h": "The Triangle", "pulse": "Three Edges &middot; One Point",
   "text": "Two edges of the triangle run back to a point on the turf. The third reaches over the rim of the pool, and that is the edge the water falls from."},
 ],
 "bp": {
  "title": "What was <em>built</em>.",
  "chapters": [
   ("01 / Fire", "Triangle Fire Pit", ["Triangle steel fire pit", "Fire over lava rock", "Dark stone fill", "Tapered steel base"]),
   ("02 / Water", "Spillway", ["Steel spillway under the edge", "Sheet of water into the pool", "Stock tank pool"]),
  ],
  "meta": [("Area", "Austin"), ("Fire", "Triangle Steel"), ("Water", "Steel Spillway"), ("Pool", "Stock Tank")],
 },
 "faqs": FAQS,
 "links": [
  ("../services/fire-pits-austin-tx", "Custom fire pits"),
  ("../services/water-features-austin-tx", "Water features"),
  ("../services/pools-austin-tx", "Pools"),
  ("../blog/custom-fire-pits-austin-tx", "How we design fire pits"),
  ("./", "All projects"),
  ("../contact", "Free consultation"),
 ],
 "next": {"href": "pool-ipe-deck-bamboo-screen", "eb": "Next Project", "title": "Ipe <em>Deck.</em>",
          "im": IM("Ipe deck around a dark pool with a row of loungers and a bamboo screen along the fence in Austin",
                   (NX + "ipe-deck-dark-pool-loungers-bamboo-800.webp", 800), (NX + "ipe-deck-dark-pool-loungers-bamboo-1200.webp", 1200))},
}

build(ROOT, SPEC)

"""Builds projects/courtyard-stream-japanese-maple.html (regular project, listed on /projects/).
Facts: the approved name and description (Houzz gallery project 15) and what the four photos plainly show.
Photos are gallery originals IMG_8283, 6284, 8275, 5373; 800-wide copies and zoom-ins come from cut_project_zooms.py.
Run: python3 -I .claude/service-pages/make_courtyard_stream_japanese_maple.py .
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from proj_lib import build, IM

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
D = "images/projects/courtyard-stream-japanese-maple/"
G = "images/gallery/"
NX = "images/projects/triangle-fire-pit-stock-tank-pool/"

def zoom(alt, name):
    return IM(alt, (f"{D}{name}-800.webp", 800), (f"{D}{name}-1125.webp", 1125))

FAQS = [
 ("Can a stream fit in a courtyard?",
  "Yes. This small stream runs through boulders in an Austin courtyard, beside a glass wall."),
 ("What is planted along the stream?",
  "A Japanese maple, ferns, and shade plants."),
 ("Can the stream be seen from inside the house?",
  "Yes. It runs beside a glass wall, so the water, the boulders, and the Japanese maple are in view from inside."),
 ("Who designed and built it?",
  "Red Agave Landscape designed and built it. Every project starts with a free consultation, and the CAD plan is included."),
]

SPEC = {
 "slug": "courtyard-stream-japanese-maple",
 "date": "2026-11-20",
 "title": "Courtyard Stream With a Japanese Maple, Austin | Red Agave",
 "desc": "A small stream through boulders in an Austin courtyard beside a glass wall, planted with a Japanese maple, ferns, and shade plants. By Red Agave.",
 "og_title": "Courtyard Stream With Boulders and a Japanese Maple, Austin | Red Agave",
 "headline": "Courtyard Stream With Boulders and a Japanese Maple in Austin, TX",
 "schema_desc": "A small stream through boulders in a courtyard beside a glass wall, planted with a Japanese maple, ferns, and shade plants. Designed and built by Red Agave Landscape.",
 "schema_images": [D + "courtyard-stream-share.webp", G + "IMG_8283.webp", G + "IMG_6284.webp"],
 "share": D + "courtyard-stream-share.webp",
 "area": "Austin, TX",
 "place": "Austin, Texas",
 "crumb": "Courtyard Stream With Boulders and a Japanese Maple",
 "h1": "Courtyard Stream With Boulders and a Japanese Maple",
 "meta_a": "Designed and built by Red Agave Landscape",
 "kicker": "Boulders &middot; Water &middot; Japanese maple &middot; Shade plants",
 "hero": IM("Japanese maple with red leaves over a small stream that runs between boulders and dark crushed rock, beside a glass wall, in an Austin courtyard",
            (D + "japanese-maple-over-courtyard-stream-800.webp", 800), (G + "IMG_8283.webp", 1200)),
 "hero_pos": "50% 30%",
 "nar_eb": "The Project &middot; Austin",
 "h2": "A small stream, a glass wall, and a Japanese maple.",
 "pulse": "Boulders &middot; Water &middot; Shade Plants",
 "paras": [
  'Red Agave Landscape designed and built this small <a href="../services/water-features-austin-tx">stream</a> in an Austin courtyard. It runs through boulders beside a glass wall, and it is planted with a Japanese maple, ferns, and shade plants.',
  'The water is shallow and clear, and it moves between the boulders over dark crushed rock. The Japanese maple stands beside the stream and reaches over it. Through the glass, the house looks straight onto the water.',
  'Purple-leaved plants, ferns, and bright green grasses grow between the stones. A wall of vertical wood boards closes one side of the courtyard, a concrete pad sits beside the glass, and dark gravel covers the ground around the bed.',
 ],
 "figs": [
  {"im": IM("Courtyard stream in Austin seen from above, with boulders, dark crushed rock, a Japanese maple, ferns, purple-leaved plants, and bright green grasses, beside a wood wall and a glass wall",
            (D + "courtyard-stream-boulders-shade-plants-800.webp", 800), (G + "IMG_6284.webp", 1200)),
   "cap_a": "01 &middot; Courtyard", "cap_b": "Stream / boulders / shade plants"},
  {"im": IM("Trunk of a Japanese maple beside a small stream running through boulders in front of a glass wall, with ferns in front and a wood wall at the side, in an Austin courtyard",
            (D + "courtyard-stream-maple-trunk-glass-wall-800.webp", 800), (G + "IMG_8275.webp", 1200)),
   "cap_a": "02 &middot; Maple", "cap_b": "Japanese maple"},
  {"im": IM("Courtyard stream beside a glass wall in Austin, with a boulder stacked on dark rock at the glass, more boulders, a concrete pad, dark gravel, and a red-leaved plant in front",
            (D + "courtyard-stream-head-at-glass-wall-800.webp", 800), (G + "IMG_5373.webp", 1200)),
   "cap_a": "03 &middot; Glass", "cap_b": "Stream beside the glass wall"},
 ],
 "statement": ("Water at the Glass", "Boulders. <em>One maple.</em>"),
 "pins": [
  {"im": zoom("Close view of shallow clear water running between boulders and dark crushed rock in a courtyard stream in Austin",
              "zoom-stream-water-between-boulders"),
   "eb": "Water &middot; 01", "h": "The Stream", "pulse": "Shallow &middot; Clear",
   "text": "The stream runs between boulders, over dark crushed rock. The water is shallow and clear, so the stones show through it."},
  {"im": zoom("Close view of boulders in a courtyard stream bed with purple-leaved plants, a fern, a small conifer, and bright green grass around them, in Austin",
              "zoom-boulders-purple-foliage-fern"),
   "eb": "Planting &middot; 02", "h": "Shade Plants", "pulse": "Ferns &middot; Purple Leaves",
   "text": "Ferns and shade plants fill the spaces between the boulders. Purple leaves and bright green grasses stand out against the stone."},
  {"im": zoom("Close view of a small stream running through boulders past the trunk of a Japanese maple, with a glass wall behind, in an Austin courtyard",
              "zoom-japanese-maple-over-stream"),
   "eb": "Tree &middot; 03", "h": "Japanese Maple", "pulse": "Beside the Water",
   "text": "A Japanese maple stands beside the stream and reaches over the water. The glass wall is right behind it."},
 ],
 "bp": {
  "title": "What was <em>built</em>.",
  "chapters": [
   ("01 / Water", "Stream", ["Small stream", "Shallow, clear water"]),
   ("02 / Stone", "Boulders", ["Boulders along the stream", "Dark crushed rock between them"]),
   ("03 / Planting", "Shade", ["Japanese maple", "Ferns", "Shade plants"]),
  ],
  "meta": [("Area", "Austin"), ("Water", "Stream"), ("Tree", "Japanese Maple"), ("Setting", "Courtyard")],
 },
 "faqs": FAQS,
 "links": [
  ("../services/water-features-austin-tx", "Water features"),
  ("../services/landscape-design-austin-tx", "Landscape design"),
  ("boulder-stream-steel-fire-trough", "A boulder stream with fire"),
  ("./", "All projects"),
  ("../contact", "Free consultation"),
 ],
 "next": {"href": "triangle-fire-pit-stock-tank-pool", "eb": "Next Project", "title": "Triangle <em>Fire Pit.</em>",
          "im": IM("Triangle steel fire pit burning at the edge of a stock tank pool, with water falling from its spillway, in Austin",
                   (NX + "triangle-fire-pit-spillway-stock-tank-pool-800.webp", 800), (G + "IMG_8345.webp", 1200))},
}

build(ROOT, SPEC)

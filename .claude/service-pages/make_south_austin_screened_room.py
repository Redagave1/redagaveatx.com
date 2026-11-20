"""Builds projects/south-austin-screened-room.html (Signature Project 11).
Facts: the Houzz description and the post custom-pergola-build-south-austin-tx.
Run: python3 -I .claude/service-pages/make_south_austin_screened_room.py .
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from proj_lib import build, IM

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
D = "images/projects/south-austin-screened-room/"
SE = "images/projects/se-austin-fire-water/"

def im(alt, name, big=1200):
    files = [(f"{D}{name}-800.webp", 800)] + ([(f"{D}{name}-{big}.webp", big)] if big else [])
    return IM(alt, *files)

FAQS = [
 ("What is this screened room built from?",
  "A welded steel frame of square steel tube, finished black, on a concrete slab. It has a ribbed metal roof, a cedar plank ceiling, two skylights with cedar-lined wells, a ceiling fan, and black-framed screens on three sides."),
 ("Is it a pergola, a patio cover, or a screened room?",
  "All three, one after another. The open steel frame is a pergola. With the metal roof on, it is a patio cover. With the screens and the door, it is a screened room. Building it in steel means one frame carries all of it."),
 ("Can a covered room have skylights?",
  "Yes. We weld an opening for each skylight into the roof framing before the roof goes on. This room has two, each at the top of a well lined in cedar."),
 ("Can the screen door have a pet door?",
  "Yes. This room has a pet door built into the screen door."),
 ("Who designed and built it?",
  "Red Agave Landscape designed it, and it was built by our own crew. Every project starts with a free consultation, and the CAD plan is included."),
]

SPEC = {
 "slug": "south-austin-screened-room",
 "num": "11",
 "date": "2026-11-20",
 "title": "Steel-Framed Screened Room, South Austin | Red Agave",
 "desc": "South Austin screened room by Red Agave: a welded steel frame on a concrete slab, a metal roof, a cedar plank ceiling, and two cedar-lined skylights.",
 "og_title": "Steel-Framed Screened Room With Cedar Skylights, South Austin | Red Agave",
 "headline": "Steel-Framed Screened Room With Cedar Skylights in South Austin, TX",
 "schema_desc": "A welded steel frame on a concrete slab at the back doors, finished as a screened room. Square steel tube finished black, a ribbed metal roof, a cedar plank ceiling, two skylights with cedar-lined wells, a ceiling fan, and black-framed screens on three sides. Designed and built by Red Agave Landscape.",
 "schema_images": [D + "screened-room-interior-share.webp", D + "09-screened-room-interior-1200.webp", D + "05-finished-screened-room-exterior-1200.webp"],
 "share": D + "screened-room-interior-share.webp",
 "area": "South Austin, TX",
 "place": "South Austin, Texas",
 "crumb": "Steel-Framed Screened Room With Cedar Skylights",
 "h1": "Steel-Framed Screened Room With Cedar Skylights",
 "meta_a": "Residence &middot; South Austin, TX",
 "kicker": "Welded steel &middot; Metal roof &middot; Cedar ceiling &middot; Two skylights",
 "hero": im("Inside a screened room in South Austin with a cedar plank ceiling, a skylight, a black ceiling fan, black-framed screens, and an outdoor sofa on the concrete slab",
            "09-screened-room-interior"),
 "hero_pos": "50% 14%",
 "nar_eb": "Design Intent &middot; South Austin",
 "h2": "A steel frame first. Then a roof, cedar, and screens.",
 "pulse": "Steel &middot; Cedar &middot; Metal Roof &middot; Screens",
 "paras": [
  'Red Agave Landscape designed and built this screened room in South Austin. It is a welded steel frame on a concrete slab at the back doors of the house, finished with a ribbed metal roof, a cedar plank ceiling, two skylights, a ceiling fan, and black-framed screens on three sides.',
  'The frame is square steel tube, welded and finished black. The posts are slim, so the walls are almost all screen. From the sofa you see the yard, and the frame reads as thin black lines. A low rail ties the posts together, and a screen door with a pet door built into it opens to the yard.',
  'The skylights were planned in the steel. The roof framing has a rectangular opening for each one, welded in before the roof went on. The cedar ceiling was carried up into each opening, so each skylight sits at the top of a cedar well. The solid roof shades the back doors, and the skylights bring the daylight back in. The room began as a <a href="../services/pergolas-austin-tx">pergola frame</a>.',
 ],
 "figs": [
  {"im": im("Finished screened room on a concrete slab at the back of a house in South Austin, with black-framed screens on three sides, a screen door with a pet door, and a cedar ceiling with skylights",
            "05-finished-screened-room-exterior"),
   "ratio": "16/10", "cap_a": "01 &middot; The Room", "cap_b": "Black frame / three screened sides"},
  {"im": im("Framed skylight opening in welded steel roof framing against the sky, above the back doors of a house in South Austin",
            "03-steel-frame-skylight-openings-from-below", big=None),
   "cap_a": "02 &middot; In the Steel", "cap_b": "Opening welded in"},
  {"im": im("Skylight at the top of a well lined in cedar planks, above a black ceiling fan, in a screened room in South Austin",
            "07-cedar-skylight-well-ceiling-fan"),
   "cap_a": "03 &middot; Skylight", "cap_b": "Cedar-lined well"},
  {"im": im("Inside a screened room in South Austin, looking past a black screen door with a pet door to the yard, with a sofa and a coffee table on the concrete slab",
            "08-screened-room-interior-door-seating"),
   "cap_a": "04 &middot; Door", "cap_b": "Screen door / pet door"},
 ],
 "build": {
  "eb": "The Build",
  "h2": "Framed, roofed, screened. <em>South Austin.</em>",
  "stacks": [
   {"base": im("Welded steel frame standing alone on a concrete slab against the back wall of a house, above French doors, in South Austin",
               "01-steel-pergola-frame-on-slab", big=None),
    "top": im("Steel roof framing seen from below with a framed opening for a skylight, above French doors, in South Austin",
              "02-steel-roof-framing-skylight-opening", big=None),
    "eb": "Steel &middot; 01", "h": "Frame First", "pulse": "October &middot; Steel on the Slab",
    "text": "In October the steel frame stood alone on the slab, with nothing else on it. It runs along the back wall of the house and passes above the French doors. Posts stand at the corners and along the outer edge of the slab, and the roof framing sits on top."},
   {"base": im("Cedar plank ceiling with a skylight well and the first black-framed screen panels standing in a steel frame, in South Austin",
               "04-cedar-ceiling-screens-going-in", big=None),
    "top": im("Black-framed screens and a screen door under the eave of a ribbed metal roof, with a cedar ceiling and a ceiling fan inside, in South Austin",
              "06-screen-door-metal-roof-eave", big=None),
    "eb": "Cedar &middot; 02", "h": "Roof, Cedar, Screens", "pulse": "November &middot; December",
    "text": "By November the frame is black, the metal roof is on, and the cedar planks cover the ceiling. The first screen panels are standing in the frame. By late December the screens run around all three open sides, the door is hung, and the fan is up."},
  ],
 },
 "statement": ("Daylight Through the Roof", "Black steel. <em>Cedar above.</em>"),
 "pins": [
  {"im": IM("Close view of a skylight in a well lined with cedar planks, with a black ceiling fan below, in a screened room in South Austin",
            (D + "10-zoom-skylight-cedar-well-800.webp", 800), (D + "10-zoom-skylight-cedar-well-1125.webp", 1125)),
   "eb": "Roof &middot; 01", "h": "Skylight", "pulse": "Cedar-Lined Well",
   "text": "Each skylight sits at the top of a well lined in the same cedar as the ceiling. The opening was welded into the steel roof framing before the roof went on."},
  {"im": IM("Close view of a cedar plank ceiling and a black ceiling fan with a light, above black-framed screens, in a screened room in South Austin",
            (D + "11-zoom-cedar-ceiling-black-fan-800.webp", 800), (D + "11-zoom-cedar-ceiling-black-fan-1125.webp", 1125)),
   "eb": "Ceiling &middot; 02", "h": "Cedar", "pulse": "Plank Ceiling &middot; Black Fan",
   "text": "Cedar planks cover the underside of the roof. A black ceiling fan with a light hangs from the cedar, and the slim black posts carry the screens down to a low rail."},
  {"im": IM("Close view of a black screen door with a pet door built into it, black-framed screens with a low rail, and a sofa and coffee table on the concrete slab, in South Austin",
            (D + "12-zoom-screen-door-pet-door-800.webp", 800), (D + "12-zoom-screen-door-pet-door-1125.webp", 1125)),
   "eb": "Walls &middot; 03", "h": "Screens", "pulse": "Three Sides &middot; Pet Door",
   "text": "Screens in black frames run around three sides. The screen door opens to the yard, and a pet door is built into it. The floor is the concrete slab."},
 ],
 "bp": {
  "title": "What was <em>built</em>.",
  "chapters": [
   ("01 / Frame", "Welded Steel", ["Square steel tube", "Welded", "Finished black", "Posts at the corners and the outer edge", "Low steel rail", "Concrete slab floor"]),
   ("02 / Roof", "Metal + Skylights", ["Ribbed metal roof panels", "Two skylights", "Openings welded into the roof framing"]),
   ("03 / Ceiling", "Cedar", ["Cedar plank ceiling", "Cedar-lined skylight wells", "Black ceiling fan with a light"]),
   ("04 / Walls", "Screens", ["Black-framed screens", "Three sides", "Screen door to the yard", "Pet door in the screen door"]),
  ],
  "meta": [("Frame", "Welded Steel"), ("Roof", "Ribbed Metal"), ("Ceiling", "Cedar Plank"), ("Skylights", "Two")],
 },
 "faqs": FAQS,
 "links": [
  ("../blog/custom-pergola-build-south-austin-tx", "The build, step by step"),
  ("../services/pergolas-austin-tx", "Pergolas"),
  ("../services/outdoor-living-austin-tx", "Outdoor living"),
  ("../blog/steel-vs-aluminum-pergola-austin-tx", "Steel vs aluminum pergolas"),
  ("../blog/patio-cover-permit-austin-tx", "Patio cover permits"),
  ("../contact", "Free consultation"),
 ],
 "next": {"href": "southeast-austin-water-feature", "eb": "Next / 10", "title": "Fire and <em>Water.</em>",
          "im": IM("Round raised water feature with a curved steel fire pit burning in front and a steel planter behind, at dusk in Southeast Austin",
                   (SE + "24-water-feature-fire-pits-overview-800.webp", 800), (SE + "24-water-feature-fire-pits-overview-1200.webp", 1200))},
}

build(ROOT, SPEC)

"""Builds projects/east-austin-steel-edging-boulders.html (Signature Project 12).
Facts: the Houzz description and the post steel-edging-cut-into-boulders-austin-tx.
Three photos, so the figures and the pinned section use zoom-ins cut by cut_project_zooms.py.
Run: python3 -I .claude/service-pages/make_east_austin_steel_edging_boulders.py .
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from proj_lib import build, IM

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
D = "images/projects/east-austin-steel-boulders/"
SR = "images/projects/south-austin-screened-room/"

def im(alt, name, big=1200):
    files = [(f"{D}{name}-800.webp", 800)] + ([(f"{D}{name}-{big}.webp", big)] if big else [])
    return IM(alt, *files)

FAQS = [
 ("Can steel edging go through a boulder?",
  "Yes. In this East Austin front yard we cut a slot into each boulder with an angle grinder and seated the steel inside it, so the edge runs into the stone with no gap."),
 ("Why cut the boulder instead of stopping the steel beside it?",
  "A gap is where an edge fails. Steel edging keeps two materials apart. With the steel inside the stone, there is no opening for the river rock to spill into the mulch."),
 ("How thick is the steel?",
  "1/4 inch. It is cut, bent, and welded on site, and it stays straight where thin 1/8-inch edging bows."),
 ("Is the boulder set before or after the steel?",
  "Before. The boulder is set in place, and the steel is cut and fitted to it."),
 ("Does the steel rust?",
  "Yes, by design. The edging is mild steel, and it develops a natural rust patina over 6 to 12 months."),
 ("Who designed and built it?",
  "Red Agave Landscape designed it, and it was built by our own crew. Every project starts with a free consultation, and the CAD plan is included."),
]

SPEC = {
 "slug": "east-austin-steel-edging-boulders",
 "num": "12",
 "date": "2026-11-20",
 "title": "Steel Edging Cut Into Boulders, East Austin | Red Agave",
 "desc": "East Austin front yard by Red Agave: 1/4-inch steel edging seated in slots cut into the boulders with an angle grinder, so steel and stone read as one.",
 "og_title": "Steel Edging Cut Into Boulders, East Austin | Red Agave",
 "headline": "Steel Edging Cut Into Boulders in East Austin, TX",
 "schema_desc": "Quarter-inch steel edging that runs through the boulders in a front yard. A slot is cut into each stone with an angle grinder and the steel is seated inside it, so the edge and the stone read as one piece. Designed and built by Red Agave Landscape.",
 "schema_images": [D + "steel-edging-boulders-share.webp", D + "03-finished-steel-edging-boulders-mulch-fern-1200.webp", D + "01-steel-plate-seated-in-boulder-slot-1200.webp"],
 "share": D + "steel-edging-boulders-share.webp",
 "area": "East Austin, TX",
 "place": "East Austin, Texas",
 "crumb": "Steel Edging Cut Into Boulders",
 "h1": "Steel Edging Cut Into Boulders",
 "meta_a": "Residence &middot; East Austin, TX",
 "kicker": "1/4-inch steel &middot; Boulders &middot; Angle grinder &middot; Mulch and river rock",
 "hero": im("Finished steel edging running into boulders in an East Austin front yard, holding black mulch with a fern on one side and river rock on the other, beside sod and dark stone pavers",
            "03-finished-steel-edging-boulders-mulch-fern"),
 "hero_pos": "50% 50%",
 "nar_eb": "Design Intent &middot; East Austin",
 "h2": "The steel does not stop at the boulder. It goes into it.",
 "pulse": "1/4-Inch Steel &middot; Boulders &middot; Angle Grinder",
 "paras": [
  'Red Agave Landscape designed and built this front yard in East Austin, where quarter-inch <a href="../services/steel-edging-austin-tx">steel edging</a> runs through the boulders. A slot is cut into each stone with an angle grinder, and the steel is seated inside it, so the edge and the stone read as one piece.',
  'The boulders were set first. Then a slot was cut down into the rock, just wide enough for the plate. The 1/4-inch plate slides into the slot and stops inside the stone, and a level across the top of the steel checks the run. The steel runs in straight lines between the boulders, with sharp corners where the line turns.',
  'The edge holds black mulch on one side and river rock on the other. Where it meets a boulder, the steel is inside the stone, so there is no opening for the rock to spill into the mulch. The edging is mild steel, and it develops a natural rust patina over 6 to 12 months.',
 ],
 "figs": [
  {"im": im("Quarter-inch steel edging seated in a slot cut into a boulder, with the steel turning a sharp corner beside the stone, during the build in East Austin",
            "01-steel-plate-seated-in-boulder-slot"),
   "cap_a": "01 &middot; The Slot", "cap_b": "Steel seated in the stone"},
  {"im": im("Steel edging running in straight lines between boulders during installation, with a level across the top and a sledgehammer beside it, in East Austin",
            "02-steel-edging-through-boulders-install"),
   "ratio": "16/10", "cap_a": "02 &middot; The Run", "cap_b": "Level across the top"},
  {"im": IM("Fern in black mulch in front of a steel edge that holds river rock, between two boulders, with sod beyond, in East Austin",
            (D + "07-zoom-fern-steel-river-rock-800.webp", 800)),
   "cap_a": "03 &middot; Finished", "cap_b": "Mulch / steel / river rock"},
 ],
 "statement": ("Steel Into Stone", "One line. <em>No gap.</em>"),
 "pins": [
  {"im": IM("Close view of a steel plate seated in a slot cut into a boulder, in East Austin",
            (D + "04-zoom-steel-seated-in-boulder-slot-800.webp", 800), (D + "04-zoom-steel-seated-in-boulder-slot-1125.webp", 1125)),
   "eb": "Stone &middot; 01", "h": "The Slot", "pulse": "Angle Grinder &middot; Cut to Fit",
   "text": "An angle grinder cuts a narrow slot down into the rock, just wide enough for the plate. The 1/4-inch plate slides into the slot and stops inside the stone."},
  {"im": IM("Close view of a run of steel edging ending inside a boulder, with a level across the top of the steel, during the build in East Austin",
            (D + "05-zoom-steel-run-level-boulder-800.webp", 800), (D + "05-zoom-steel-run-level-boulder-1125.webp", 1125)),
   "eb": "Steel &middot; 02", "h": "The Run", "pulse": "Straight Lines &middot; Sharp Corners",
   "text": "The steel runs in straight lines between the boulders, with sharp corners where the line turns. A level across the top of the steel checks the run."},
  {"im": IM("Close view of finished steel edging meeting a boulder, with black mulch, a fern, and a small plant with purple flowers in front and river rock behind, in East Austin",
            (D + "06-zoom-steel-edge-into-boulder-mulch-800.webp", 800), (D + "06-zoom-steel-edge-into-boulder-mulch-1125.webp", 1125)),
   "eb": "Finish &middot; 03", "h": "No Gap", "pulse": "Mulch &middot; River Rock",
   "text": "The edge holds black mulch on one side and river rock on the other. Where it meets a boulder the steel is inside the stone, so the rock has no opening to spill into the mulch."},
 ],
 "bp": {
  "title": "What was <em>built</em>.",
  "chapters": [
   ("01 / Steel", "1/4-Inch Edging", ["1/4-inch mild steel plate", "Cut, bent, and welded on site", "Straight runs and sharp corners", "Natural rust patina"]),
   ("02 / Stone", "Slotted Boulders", ["Boulders set before the steel", "Slot cut with an angle grinder", "Steel seated inside the stone", "Run checked with a level"]),
   ("03 / Ground", "Beds", ["Black mulch on one side of the steel", "River rock on the other", "Fern in the mulch"]),
  ],
  "meta": [("Area", "East Austin"), ("Steel", "1/4 Inch"), ("Tool", "Angle Grinder"), ("Stone", "Slotted Boulders")],
 },
 "faqs": FAQS,
 "links": [
  ("../blog/steel-edging-cut-into-boulders-austin-tx", "The method, step by step"),
  ("../services/steel-edging-austin-tx", "Steel edging"),
  ("../blog/steel-edging-fabrication-austin-tx", "Steel edging fabrication"),
  ("../services/steel-retaining-walls-austin-tx", "Steel retaining walls"),
  ("../services/xeriscape-austin-tx", "Xeriscape"),
  ("../designs", "Design plans"),
  ("../contact", "Free consultation"),
 ],
 "next": {"href": "south-austin-screened-room", "eb": "Next / 11", "title": "Screened <em>Room.</em>",
          "im": IM("Finished screened room with black-framed screens and a cedar ceiling on a concrete slab at the back of a house in South Austin",
                   (SR + "05-finished-screened-room-exterior-800.webp", 800), (SR + "05-finished-screened-room-exterior-1200.webp", 1200))},
}

build(ROOT, SPEC)

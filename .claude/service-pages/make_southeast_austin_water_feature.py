"""Builds projects/southeast-austin-water-feature.html (Signature Project 10).
Facts: the Houzz description, the posts water-feature-fire-pits-southeast-austin-tx and custom-fire-pits-austin-tx,
and Plan 02 on designs.html. A separate job from Chrysler Bend: never merge the two.
Run: python3 -I .claude/service-pages/make_southeast_austin_water_feature.py .
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from proj_lib import build, IM

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
D = "images/projects/se-austin-fire-water/"
TP = "images/projects/southeast-austin-triangle-planter/"

def im(alt, name, big=1200):
    files = [(f"{D}{name}-800.webp", 800)] + ([(f"{D}{name}-{big}.webp", big)] if big else [])
    return IM(alt, *files)

FAQS = [
 ("Is this water feature really built like a pool?",
  "Yes. It has a concrete shell, a plaster interior finished black, and a sand pool filter. Those are the parts of a swimming pool, at a much smaller size."),
 ("Where does the water come from?",
  "From a boulder with a hole drilled in it. Water comes out of the boulder, runs down an open steel channel, and falls to the surface of the pool."),
 ("What are the two fire pits made of?",
  "Steel. The front fire pit is steel bent to follow the round pool wall, with a custom burner and dark fire glass. The second is a square steel pan with a ring burner, suspended between two boulders. Both are gas."),
 ("What is the steel piece with the tree?",
  "A planter. A square steel tray sits on a tapered steel base. It was cut from steel plate and welded on site by our own crew. The slot in the base is packed with river rock and lit from inside."),
 ("Was this yard drawn before it was built?",
  "Yes. The owner of Red Agave drew the plan, and it is Plan 02 on our design plans page. The concrete pads, the round pool, the channel from the boulder, and the dark gravel court are all where the plan drew them."),
 ("Who designed and built it?",
  "Red Agave Landscape designed it, and our own crew built it in spring 2025. Every project starts with a free consultation, and the CAD plan is included."),
]

SPEC = {
 "slug": "southeast-austin-water-feature",
 "num": "10",
 "date": "2026-11-20",
 "title": "Water Feature and Fire Pits, Southeast Austin | Red Agave",
 "desc": "Southeast Austin backyard by Red Agave: a round water feature built like a small pool, fed from a drilled boulder, with two steel fire pits beside it.",
 "og_title": "Round Water Feature and Two Steel Fire Pits, Southeast Austin | Red Agave",
 "headline": "Round Water Feature and Two Steel Fire Pits in Southeast Austin, TX",
 "schema_desc": "A round raised water feature built like a small pool: a concrete shell, a plaster interior finished black, and a sand pool filter. Water comes out of a drilled boulder and runs down a steel channel to the pool. A floating steel fire pit curves along the front, and a second fire pit is suspended between two boulders. Concrete pads with gravel joints, a steel planter welded on site, and lit steel edging. Designed and built by Red Agave Landscape in spring 2025.",
 "schema_images": [D + "24-water-feature-fire-pits-overview-share.webp", D + "24-water-feature-fire-pits-overview-1200.webp", D + "19-finished-water-feature-fire-pit-dusk-1200.webp"],
 "share": D + "24-water-feature-fire-pits-overview-share.webp",
 "area": "Southeast Austin, TX",
 "place": "Southeast Austin, Texas",
 "crumb": "Round Water Feature and Two Steel Fire Pits",
 "h1": "Round Water Feature and Two Steel Fire Pits",
 "meta_a": "Residence &middot; Southeast Austin, TX",
 "kicker": "Black plaster &middot; Drilled boulder &middot; Steel channel &middot; Two fire pits",
 "hero": im("Round raised water feature with black water and a dark cap, a steel channel pouring into it, a curved steel fire pit burning in front, a second fire pit burning between two boulders behind, and a steel planter, at dusk in Southeast Austin",
            "24-water-feature-fire-pits-overview"),
 "hero_pos": "50% 55%",
 "nar_eb": "Design Intent &middot; Southeast Austin",
 "h2": "Black water, built like a pool. Fire in front and behind.",
 "pulse": "Concrete &middot; Plaster &middot; Steel &middot; Boulders",
 "paras": [
  'Red Agave Landscape designed and built this backyard in Southeast Austin around a round <a href="../services/water-features-austin-tx">water feature</a> that is constructed like a small swimming pool: a concrete shell, a plaster interior finished black, and a sand pool filter. Water comes out of a hole drilled in a boulder, runs down a steel channel, and falls into the pool. Our own crew built it in spring 2025.',
  'Two <a href="../services/fire-pits-austin-tx">fire pits</a> burn beside the water, and both are gas. A floating steel fire pit curves along the front of the pool wall, with a custom burner under dark fire glass. Behind the pool, a square steel pan with a ring burner is suspended between two boulders. The flames light the wall and reflect on the black water.',
  'A square <a href="../services/custom-planters-austin-tx">steel planter</a> on a tapered base stands behind the pool and holds a young tree. It was cut from steel plate and welded on site, and the slot in its base is packed with river rock and lit from inside. The patio is concrete, poured as separate pads with dark gravel joints. Steel edging with a light strip along it outlines the gravel court.',
 ],
 "figs": [
  {"im": im("Round raised water feature at dusk with water falling from a steel channel, a curved steel fire pit burning at the foot of the wall, and a square steel planter with a young tree behind, in Southeast Austin",
            "19-finished-water-feature-fire-pit-dusk"),
   "cap_a": "01 &middot; Water", "cap_b": "Black plaster / dark cap"},
  {"im": im("Steel channel pouring water into a round black water feature, seen from above, with a curved steel fire pit burning over dark fire glass at the foot of the wall, in Southeast Austin",
            "22-water-feature-channel-fire-top-view", big=None),
   "cap_a": "02 &middot; Channel", "cap_b": "Steel channel / boulder"},
  {"im": im("Square steel fire pit burning between two boulders in a dark gravel court outlined by lit steel edging, beside a round water feature, in Southeast Austin",
            "23-boulder-fire-pit-lit-edging", big=None),
   "cap_a": "03 &middot; Fire", "cap_b": "Steel pan between two boulders"},
  {"im": im("Square steel planter on a tapered steel base, with a slot in the base packed with river rock and lit from inside, beside a round water feature in Southeast Austin",
            "18-finished-steel-planter"),
   "cap_a": "04 &middot; Planter", "cap_b": "River rock / lit base"},
 ],
 "build": {
  "eb": "The Build",
  "h2": "Formed, poured, plastered. <em>Spring 2025.</em>",
  "stacks": [
   {"base": im("Concrete patio pads with form boards still between them, around a round concrete water feature shell with a black interior and boulders set beside it, during the build in Southeast Austin",
               "14-concrete-pads-boulders"),
    "top": im("Round water feature filled with water while the dark cap is set on the rim in curved sections, in Southeast Austin",
              "15-pool-filled-cap", big=None),
    "eb": "Concrete &middot; 01", "h": "Built Like a Pool", "pulse": "Shell &middot; Plaster &middot; Filter",
    "text": "We dug the round hole, set the steel edging, and placed the boulders first. The round wall was formed and poured in place. The interior was plastered and finished black. Then the pool was filled, and the dark cap was set on the rim in curved sections."},
   {"base": im("Square steel fire pit pan with a ring burner resting between two boulders, during the build in Southeast Austin",
               "17-fire-pit-burner-pan-boulders"),
    "top": im("Curved steel fire pit set at the foot of a round water feature on new concrete pads, during the build in Southeast Austin",
              "16-floating-fire-pit-curved-steel"),
    "eb": "Steel &middot; 02", "h": "Two Fire Pits", "pulse": "Curved Steel &middot; Ring Burner",
    "text": "The second fire pit is a square steel pan with a ring burner, carried between its two boulders. The front fire pit is steel bent to follow the round wall. It is set off the concrete, so it reads as floating."},
  ],
 },
 "statement": ("Fire Beside Water", "Black plaster. <em>Steel and stone.</em>"),
 "pins": [
  {"im": IM("Close view of water falling from a steel channel onto black water inside a round water feature with a dark cap, with a curved steel fire pit burning below, in Southeast Austin",
            (D + "28-zoom-steel-channel-black-water-800.webp", 800), (D + "28-zoom-steel-channel-black-water-1125.webp", 1125)),
   "eb": "Water &middot; 01", "h": "Black Water", "pulse": "Plaster &middot; Sand Pool Filter",
   "text": "The inside of the pool is plaster, finished black. Black water works like a dark mirror: it reflects the flames in front of it and the sky above it. A sand pool filter keeps the water clear."},
  {"im": IM("Close view of the dark cap and black water of a round water feature, with a second fire pit burning between two boulders behind it in a dark gravel court outlined by lit steel edging, in Southeast Austin",
            (D + "27-zoom-boulder-fire-pit-lit-steel-edging-800.webp", 800), (D + "27-zoom-boulder-fire-pit-lit-steel-edging-1125.webp", 1125)),
   "eb": "Fire &middot; 02", "h": "Between Boulders", "pulse": "Steel Pan &middot; Lit Edging",
   "text": "The second fire pit burns between two boulders behind the pool, in a court of dark gravel. Steel edging holds the gravel, and a light strip runs along the steel, so the outline of the court shows at night."},
  {"im": IM("Close view of the tapered steel base of a planter, its slot packed with river rock and lit from inside, with yellow-green grasses and river rock around it, in Southeast Austin",
            (D + "29-zoom-planter-base-river-rock-light-800.webp", 800), (D + "29-zoom-planter-base-river-rock-light-1125.webp", 1125)),
   "eb": "Steel &middot; 03", "h": "The Planter", "pulse": "Welded On Site &middot; Lit Base",
   "text": "A square steel tray on a tapered base, cut from steel plate and welded on site. The slot in the base is packed with river rock, with a light behind the rock. The steel has weathered to a deep brown, the same tone as the floating fire pit."},
 ],
 "bp": {
  "title": "The <em>blueprint</em>.",
  "sketch": {
   "im": IM("Landscape design plan for a Southeast Austin backyard with gray concrete pads, a round blue water feature fed by a channel from a boulder, two red fire pits beside boulders, and a dark gravel court",
            ("images/designs/water-feature-fire-pits-plan-900.webp", 900), ("images/designs/water-feature-fire-pits-plan.webp", 1132)),
   "w": 1132, "h": 820, "eb": "00 / Design", "title": "Plan 02",
   "text": "On the plan, the blue circle is the water feature, the two red marks are the fire pits, the gray rectangles are concrete pads, and the dark area is gravel. The layout held. The shapes changed: both fire pits are plain rectangles on the plan. Built, the front one is a curve of steel, and the second is a square pan between two boulders. The steel planter is not on the drawing.",
   "href": "../designs", "link": "More design plans"},
  "chapters": [
   ("01 / Water", "Built Like a Pool", ["Round raised concrete shell", "Plaster interior finished black", "Dark cap set in curved sections", "Sand pool filter", "Drilled boulder", "Steel channel to the pool"]),
   ("02 / Fire", "Two Fire Pits", ["Floating curved steel fire pit", "Custom burner", "Dark fire glass", "Square steel pan", "Ring burner", "Suspended between two boulders"]),
   ("03 / Steel", "Planter + Edging", ["Square steel planter", "Tapered base", "Cut and welded on site", "River rock slot lit from inside", "Steel edging", "Light strips along the steel"]),
   ("04 / Ground", "Pads + Gravel", ["Concrete pads", "Dark gravel joints", "One pad formed on a curve", "Dark gravel court", "Ornamental grasses and accent plants", "Lawn beyond"]),
  ],
  "meta": [("Built", "Spring 2025"), ("Water", "Black Plaster"), ("Fire", "Two Steel Pits"), ("Source", "Drilled Boulder")],
 },
 "faqs": FAQS,
 "links": [
  ("../blog/water-feature-fire-pits-southeast-austin-tx", "How the pool was built"),
  ("../blog/custom-fire-pits-austin-tx", "The plan and the finished fires"),
  ("../services/water-features-austin-tx", "Water features"),
  ("../services/fire-pits-austin-tx", "Custom fire pits"),
  ("../services/custom-planters-austin-tx", "Custom steel planters"),
  ("../services/landscape-lighting-austin-tx", "Landscape lighting"),
  ("../designs", "Design plans"),
  ("../contact", "Free consultation"),
 ],
 "next": {"href": "chrysler-bend", "eb": "Next / 09", "title": "Chrysler <em>Bend.</em>",
          "im": IM("Floating triangle steel planter with a variegated century agave at dusk, lit from its rim above basalt gravel, in Southeast Austin",
                   (TP + "13-floating-triangle-planter-dusk-800.webp", 800), (TP + "13-floating-triangle-planter-dusk-1125.webp", 1125))},
}

build(ROOT, SPEC)

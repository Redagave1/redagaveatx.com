"""Builds projects/boulder-stream-steel-fire-trough.html (regular project, listed on /projects/).
Facts: the approved name and description (Houzz gallery project 14) and what the eight photos plainly show.
Photos are gallery originals (IMG_5474, 5491, 8183, 8168, 8191; zoom-ins from IMG_5451, 8186, 8182).
Run: python3 -I .claude/service-pages/make_boulder_stream_steel_fire_trough.py .
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from proj_lib import build, IM

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
D = "images/projects/boulder-stream-steel-fire-trough/"
G = "images/gallery/"
NX = "images/projects/courtyard-stream-japanese-maple/"

def zoom(alt, name):
    return IM(alt, (f"{D}{name}-800.webp", 800), (f"{D}{name}-1125.webp", 1125))

FAQS = [
 ("Can a fire feature sit next to a stream?",
  "Yes. On this Austin project a steel fire trough is set among the boulders of the stream, and it stands over the water on a steel frame."),
 ("Where does the water come from?",
  "From a boulder. Water pours out of a boulder beside the fire trough and runs down through the stones."),
 ("Is the steel edging lit?",
  "Yes. Lighting runs along the steel edging. At dusk it washes the plants and the boulders inside the bed, and a line of light outlines the gravel court behind the fire."),
 ("What is planted around the stream?",
  "Ferns and grasses fill the beds between the boulders."),
 ("Who designed and built it?",
  "Red Agave Landscape designed and built it. Every project starts with a free consultation, and the CAD plan is included."),
]

SPEC = {
 "slug": "boulder-stream-steel-fire-trough",
 "date": "2026-11-20",
 "title": "Boulder Stream and Steel Fire Trough, Austin | Red Agave",
 "desc": "A stream running through boulders in Austin, with a steel fire trough set among the stones and lighting along the steel edging. By Red Agave Landscape.",
 "og_title": "Boulder Stream, Steel Fire Trough and Lit Steel Edging, Austin | Red Agave",
 "headline": "Boulder Stream, Steel Fire Trough and Lit Steel Edging in Austin, TX",
 "schema_desc": "A stream running through boulders, with a steel fire trough set among the stones and lighting along the steel edging. Ferns and grasses fill the beds. Designed and built by Red Agave Landscape.",
 "schema_images": [D + "boulder-stream-fire-trough-share.webp", G + "IMG_5474.webp", G + "IMG_8168.webp"],
 "share": D + "boulder-stream-fire-trough-share.webp",
 "area": "Austin, TX",
 "place": "Austin, Texas",
 "crumb": "Boulder Stream, Steel Fire Trough and Lit Steel Edging",
 "h1": "Boulder Stream, Steel Fire Trough and Lit Steel Edging",
 "meta_a": "Designed and built by Red Agave Landscape",
 "kicker": "Boulders &middot; Steel &middot; Fire &middot; Light",
 "hero": IM("Steel fire trough burning over lava rock above a stream at dusk, with water pouring from a boulder beside it, dark rock and river pebbles along the water, and a steel edge in front, in Austin",
            (D + "steel-fire-trough-boulder-stream-dusk-800.webp", 800), (D + "steel-fire-trough-boulder-stream-dusk-1200.webp", 1200), (G + "IMG_5474.webp", 1600)),
 "hero_pos": "50% 45%",
 "nar_eb": "The Project &middot; Austin",
 "h2": "Water through boulders. Fire set among the stones.",
 "pulse": "Boulders &middot; Steel &middot; Fire &middot; Light",
 "paras": [
  'Red Agave Landscape designed and built this <a href="../services/water-features-austin-tx">stream</a> in Austin. Water runs through boulders, a steel fire trough is set among the stones, and lighting runs along the steel edging. Ferns and grasses fill the beds.',
  'Water pours out of a boulder beside the fire trough and runs down between the stones, over dark rock and river pebbles. The <a href="../services/fire-pits-austin-tx">fire trough</a> stands over the water on a steel frame, with stones resting on its rim, and burns over lava rock.',
  'The stream sits in a bed held by <a href="../services/steel-edging-austin-tx">steel edging</a>, with gravel around it. Light runs along the inside of the steel and washes the plants and the boulders. A second line of light traces the gravel court behind the fire, and uplights pick out the planting along the fence.',
 ],
 "figs": [
  {"im": IM("Stream running between boulders at dusk with a steel fire trough burning behind, water pouring from a boulder, grasses along the water, and a line of light across the gravel, in Austin",
            (D + "boulder-stream-fire-trough-grasses-800.webp", 800), (G + "IMG_5491.webp", 1600)),
   "ratio": "4/3", "cap_a": "01 &middot; Stream", "cap_b": "Water through boulders"},
  {"im": IM("Boulder stream at dusk in a bed held by steel edging, with ferns and grasses lit from the steel, a steel fire trough burning behind, and a line of light around the gravel court, in Austin",
            (D + "boulder-stream-ferns-lit-steel-edging-800.webp", 800), (G + "IMG_8183.webp", 1200)),
   "cap_a": "02 &middot; Planting", "cap_b": "Ferns and grasses"},
  {"im": IM("Steel-edged bed with a boulder stream, ferns, and grasses at dusk, lit along the inside of the steel, with a steel fire trough burning behind and gravel beside it, in Austin",
            (D + "lit-steel-edged-bed-stream-gravel-800.webp", 800), (G + "IMG_8168.webp", 1600)),
   "ratio": "4/3", "cap_a": "03 &middot; Steel", "cap_b": "Lit steel edging / gravel"},
  {"im": IM("Boulder stream after dark with mist over the water, ferns and grasses lit from the steel edging, and a steel fire trough burning inside a line of light, in Austin",
            (D + "boulder-stream-mist-lit-edging-night-800.webp", 800), (G + "IMG_8191.webp", 1600)),
   "ratio": "4/3", "cap_a": "04 &middot; Night", "cap_b": "Fire / lit stones"},
 ],
 "statement": ("Fire Over Water", "Boulders. <em>Steel and light.</em>"),
 "pins": [
  {"im": zoom("Boulder stream, ferns, and grasses in an angled bed of steel edging lit from inside at dusk, with a steel fire trough burning behind and a line of light around the gravel court, in Austin",
              "zoom-lit-steel-edging-stream-dusk"),
   "eb": "Light &middot; 01", "h": "Lit Steel", "pulse": "Steel Edging &middot; Warm Light",
   "text": "Light runs along the steel edging and washes the ferns, the grasses, and the boulders inside the bed. Behind the fire, a line of light traces the edge of the gravel court."},
  {"im": zoom("Close view of water pouring from a boulder into a stream, with a steel fire trough burning behind on a steel frame, in Austin",
              "zoom-water-pouring-from-boulder-fire-trough"),
   "eb": "Fire &middot; 02", "h": "Fire Trough", "pulse": "Steel &middot; Lava Rock",
   "text": "The steel fire trough is set among the stones and stands over the water on a steel frame. Beside it, water pours out of a boulder and into the stream."},
  {"im": zoom("Close view of boulders, ferns, and grasses in a bed held by lit steel edging, with mist over the stream and gravel beside the steel, in Austin",
              "zoom-boulder-stream-ferns-steel-bed"),
   "eb": "Planting &middot; 03", "h": "Ferns and Grasses", "pulse": "Boulders &middot; Dark Rock",
   "text": "Ferns and grasses fill the beds between the boulders. Dark rock and river pebbles line the stream, and gravel runs along the outside of the steel."},
 ],
 "bp": {
  "title": "What was <em>built</em>.",
  "chapters": [
   ("01 / Water", "Stream", ["Stream through boulders", "Water pouring from a boulder", "Dark rock and river pebbles"]),
   ("02 / Fire", "Steel Trough", ["Steel fire trough", "Set among the stones", "Steel frame over the water", "Lava rock"]),
   ("03 / Steel", "Lit Edging", ["Steel edging around the bed", "Lighting along the steel", "Line of light around the gravel court", "Uplights in the planting"]),
   ("04 / Planting", "Ferns + Grasses", ["Ferns", "Grasses", "Beds between the boulders"]),
  ],
  "meta": [("Area", "Austin"), ("Water", "Boulder Stream"), ("Fire", "Steel Trough"), ("Edging", "Lit Steel")],
 },
 "faqs": FAQS,
 "links": [
  ("../services/water-features-austin-tx", "Water features"),
  ("../services/fire-pits-austin-tx", "Custom fire pits"),
  ("../services/steel-edging-austin-tx", "Steel edging"),
  ("../services/landscape-lighting-austin-tx", "Landscape lighting"),
  ("courtyard-stream-japanese-maple", "A courtyard stream"),
  ("./", "All projects"),
  ("../contact", "Free consultation"),
 ],
 "next": {"href": "courtyard-stream-japanese-maple", "eb": "Next Project", "title": "Courtyard <em>Stream.</em>",
          "im": IM("Japanese maple with red leaves over a small stream running between boulders beside a glass wall in an Austin courtyard",
                   (NX + "japanese-maple-over-courtyard-stream-800.webp", 800), (G + "IMG_8283.webp", 1200))},
}

build(ROOT, SPEC)

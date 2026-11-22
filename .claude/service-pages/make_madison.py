"""Builds projects/madison.html (Signature Project 02, Crestview, Austin).
Facts: only the owner's words of 2026-11-20 (memory file project_madison.md), his added line of 2026-11-21
("we made a floating benches mirrors on that and also the floating fire pit"), and the photos in images/projects/madison/.
The pool was already there: never say or imply Red Agave built it. No sizes, no deck wood, no redbud variety.
The photos show two boulders raised off the ground (one in the lawn, one long flat one by the left planter). Which one is the
bench, or whether both are, is not confirmed, so the text says "a floating bench" and the alt texts only describe them.
The page is already registered (featured.html card, sitemap, netlify, llms.txt), so there is no register step.
Run: python3 -I .claude/service-pages/make_madison.py .
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import proj_lib
from proj_lib import build, IM

# "Madison" is this page's public name (the street), and the next-project link keeps the name "Hopeland".
# proj_lib refuses both as internal job names, so they are allowed for this page only.
proj_lib.BANNED = [w for w in proj_lib.BANNED if w not in ("Madison", "Hopeland")]
# A one-word name takes the large hero title, as on Chrysler Bend. Eight blueprint lists sit in two rows of four.
# The hero photo has pale concrete in the foreground, so the scrim is a little stronger under the title lines.
proj_lib.CSS_ADD += """.thr-title-x{font-size:clamp(96px,17vw,260px);line-height:.88;padding-top:0}
.thr-scrim{background:linear-gradient(180deg,rgba(10,10,10,.62) 0%,rgba(10,10,10,.34) 20%,rgba(10,10,10,.1) 36%,rgba(10,10,10,.14) 50%,rgba(10,10,10,.76) 78%,rgba(10,10,10,.92) 100%)}
@media(min-width:901px){.bp-chap:nth-child(4n){border-right:none}.bp-chap:nth-child(n+5){border-top:1px solid var(--line)}}
"""

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
D = "images/projects/madison/"
HOPE = "images/projects/hopeland/"

def im(alt, name):
    return IM(alt, (f"{D}{name}-800.webp", 800), (f"{D}{name}.webp", 1200))

def zoom(alt, name):
    return IM(alt, (f"{D}{name}-800.webp", 800), (f"{D}{name}-1125.webp", 1125))

PLANTS = ["Weeping redbud", "Native sedge", "Variegated cast iron plant", "Gayfeather", "Japanese yews",
          "Japanese maple", "Cherry laurel", "Ferns", "Philodendron"]

FAQS = [
 ("What was this backyard before Red Agave built it?",
  "A bare piece of dirt next to the pool. The ground had a slight slope, so Red Agave terraced it slightly, stepping down to the seating area. The turf is Ultra Real, made by American Synthetic Turf. The pool was already there."),
 ("What are the V-shaped steel planters, and how are they lit?",
  "They are tapered steel planters, and there are two of them. Each one has a light in its upper rim and a cutout with a second low voltage light. The COB lights are BTF. Each planter sits on two turf steps."),
 ("How does the boulder fire pit float?",
  "The fire pit is a black diamond boulder. The owner of Red Agave drilled a hole in the bottom of it and mounted it on an oil field pipe. Mirrors are mounted under the boulder, at the base, so the boulder looks like it is floating. The gas line goes through the pipe and through a hole drilled through the boulder. The top is carved out and filled with fire glass that looks like obsidian. The floating bench has mirrors under it too."),
 ("How was the concrete formed?",
  "With 1/4-inch by 4-inch steel, and the steel remains in place. The concrete was finished smooth with a marbling effect."),
 ("What is planted in this yard?",
  "Weeping redbud, native sedge, variegated cast iron plant, gayfeather, Japanese yews, Japanese maple, cherry laurel, ferns, and philodendron."),
 ("Who designed and built it?",
  "Red Agave Landscape designed it, and it was built by our own crew in 2024. Every project starts with a free consultation, and the CAD plan is included."),
]

SPEC = {
 "slug": "madison",
 "num": "02",
 "date": "2026-05-08",
 "modified": "2026-11-21",
 "title": "Madison: Floating Boulder Fire Pit, Crestview | Red Agave",
 "desc": "Crestview, Austin backyard by Red Agave: terraced turf, two lit tapered steel planters, a floating boulder fire pit and bench, and marbled concrete.",
 "og_title": "Madison: Floating Boulder Fire Pit and Tapered Steel Planters | Red Agave",
 "headline": "Madison: Floating Boulder Fire Pit, Tapered Steel Planters, and Terraced Turf in Crestview, Austin, TX",
 "schema_desc": "A bare piece of dirt next to an existing pool in Crestview, Austin, terraced slightly down to the seating area and finished in Ultra Real turf by American Synthetic Turf. Two tapered steel planters, each on two turf steps, each with a light in its upper rim and a cutout with a second low voltage light. A floating fire pit made from a black diamond boulder, drilled and mounted on an oil field pipe that carries the gas line, with mirrors mounted under the boulder and the top carved out and filled with fire glass that looks like obsidian. A floating bench, also with mirrors under it. Smooth concrete with a marbling effect, formed with 1/4-inch by 4-inch steel that remains in place. BTF COB lights, low voltage lighting, and a deck stained with Ready Seal. Planted with weeping redbud, native sedge, variegated cast iron plant, gayfeather, Japanese yews, Japanese maple, cherry laurel, ferns, and philodendron. Designed and built by Red Agave Landscape in 2024.",
 "schema_images": [D + "floating-boulder-fire-pit-tapered-planter-share.webp", D + "IMG_9096.webp", D + "IMG_9007.webp"],
 "share": D + "floating-boulder-fire-pit-tapered-planter-share.webp",
 "area": "Crestview, Austin, TX",
 "place": "Crestview, Austin, Texas &middot; 2024",
 "crumb": "Madison",
 "h1": "Madison",
 "meta_a": "Residence &middot; Crestview, Austin, TX",
 "kicker": "Turf &middot; Tapered steel planters &middot; Floating boulder fire pit &middot; Marbled concrete",
 "hero": im("Backyard at dusk with smooth marbled concrete pads divided by steel, artificial turf, the boards of a wood deck, a dark gravel court with a boulder fire pit burning, and two lit tapered steel planters holding weeping redbuds, in Crestview, Austin",
            "IMG_9096"),
 "hero_pos": "50% 38%",
 "nar_eb": "Design Intent &middot; Crestview, Austin",
 "h2": "Bare dirt by the pool. Now turf, steel, and fire.",
 "pulse": "Turf &middot; Steel &middot; Boulder &middot; Concrete",
 "paras": [
  'Red Agave Landscape designed and built this backyard in Crestview, Austin, in 2024: a slightly terraced yard in <a href="../services/turf-installation-austin-tx">artificial turf</a>, with two lit tapered steel planters, a floating boulder fire pit, a floating bench, and marbled concrete formed in steel. It started as a bare piece of dirt next to the pool. The ground had a slight slope, so we terraced it slightly, stepping down to the seating area. The turf is Ultra Real, made by American Synthetic Turf.',
  'There are two <a href="../services/custom-planters-austin-tx">tapered steel planters</a>, each shaped like a V. Each one sits on two turf steps. Each has a light in its upper rim, and a cutout in the steel with a second low voltage light. The COB lights are BTF, and the <a href="../services/landscape-lighting-austin-tx">lighting</a> in this yard is low voltage. A weeping redbud grows in each planter.',
  'The <a href="../services/fire-pits-austin-tx">fire pit</a> is a black diamond boulder. The owner of Red Agave drilled a hole in the bottom of the boulder and mounted it on an oil field pipe. Mirrors are mounted under the boulder, so it looks like it is floating. The gas line goes through the pipe. A hole was drilled through the boulder for the gas line. The top was carved out and filled with fire glass that looks like obsidian. The yard also has a floating bench, with mirrors mounted under it as well.',
  'The <a href="../services/marbled-concrete-patios-austin-tx">concrete</a> was finished smooth with a marbling effect. It is formed with 1/4-inch by 4-inch steel, and the steel remains in place. The planting is weeping redbud, native sedge, variegated cast iron plant, gayfeather, Japanese yews, Japanese maple, cherry laurel, ferns, and philodendron. The deck is stained with Ready Seal.',
 ],
 "figs": [
  {"im": im("Artificial turf with a boulder raised above it and a standing boulder, running to concrete pads and a dark gravel court with a boulder fire pit, with two tapered steel planters holding weeping redbuds near the fence, ferns and a lit path light in a planting bed, and a corner of the pool, in Crestview, Austin",
            "IMG_8976"),
   "cap_a": "01 &middot; Turf", "cap_b": "Ultra Real / slight terracing"},
  {"im": im("Black tapered steel planter on two turf steps at dusk, with light under its upper rim and a lit cutout in its face, holding a weeping redbud, with the pool behind it, in Crestview, Austin",
            "IMG_9083"),
   "cap_a": "02 &middot; Planter", "cap_b": "Rim light / lit cutout / two turf steps"},
  {"im": im("Black diamond boulder fire pit burning over dark fire glass, held above a square of turf framed in concrete so it looks like it floats, with a tapered steel planter and the pool wall behind it, in Crestview, Austin",
            "IMG_9007"),
   "cap_a": "03 &middot; Fire Pit", "cap_b": "Black diamond boulder / oil field pipe / mirrors"},
  {"im": im("Smooth concrete with a marbled finish, poured as pads with steel left in place between them and along the turf, with a boulder fire pit and two tapered steel planters beyond, in Crestview, Austin",
            "IMG_8997"),
   "cap_a": "04 &middot; Concrete", "cap_b": "Marbled / formed in steel"},
 ],
 "build": {
  "eb": "The Build",
  "h2": "Bare dirt, then terraces. <em>Crestview, 2024.</em>",
  "stacks": [
   {"base": IM("Black tapered steel planter on two turf steps at dusk with light under its upper rim, a second planter with a lit cutout behind it, and a boulder fire pit burning on a square of turf in a dark gravel court, in Crestview, Austin",
               (D + "after-800.webp", 800), (D + "after.webp", 1200)),
    "top": IM("Bare dirt under a large tree next to a pool with a black safety fence, before the build, in Crestview, Austin",
              (D + "before-800.webp", 800), (D + "before.webp", 1200)),
    "eb": "Before &middot; After", "h": "Bare Dirt", "pulse": "Next to the Pool",
    "text": "Before the build, this was a bare piece of dirt next to the pool. The ground had a slight slope, so we terraced it slightly, stepping down to the seating area. Now it is turf, two steel planters, a floating boulder fire pit, a floating bench, and marbled concrete."},
  ],
 },
 "statement": ("Boulders That Float", "Oil field pipe. <em>Mirrors below.</em>"),
 "pins": [
  {"im": zoom("Close view of the carved top of a black diamond boulder fire pit, filled with dark fire glass that looks like obsidian, with gas flames burning, in Crestview, Austin",
              "zoom-boulder-fire-pit-obsidian-look-fire-glass"),
   "eb": "Fire &middot; 01", "h": "Obsidian Look", "pulse": "Black Diamond Boulder &middot; Fire Glass",
   "text": "The top of the black diamond boulder is carved out and filled with fire glass that looks like obsidian. The boulder is mounted on an oil field pipe, with mirrors under it. The gas line goes through the pipe and through a hole drilled through the boulder."},
  {"im": zoom("Close view of a black tapered steel planter at dusk with light under its upper rim and a lit cutout in its face, standing on turf steps, with a philodendron and a long flat boulder raised on stones beside it and the boulder fire pit burning in front, in Crestview, Austin",
              "zoom-tapered-planter-lit-rim-cutout"),
   "eb": "Steel &middot; 02", "h": "Rim and Cutout", "pulse": "Two Lights &middot; Two Turf Steps",
   "text": "Each tapered steel planter has a light in its upper rim and a cutout with a second low voltage light. The COB lights are BTF. Each planter sits on two turf steps."},
  {"im": zoom("Close view of smooth marbled concrete pads with steel left in place between them and along the artificial turf, next to the boards of a wood deck, in Crestview, Austin",
              "zoom-marbled-concrete-formed-in-steel"),
   "eb": "Concrete &middot; 03", "h": "Formed in Steel", "pulse": "Smooth &middot; Marbled",
   "text": "The concrete was finished smooth with a marbling effect. It is formed with 1/4-inch by 4-inch steel, and the steel remains in place."},
 ],
 "bp": {
  "title": "The <em>blueprint</em>.",
  "chapters": [
   ("01 / Ground", "Turf + Terraces", ["Bare piece of dirt next to the pool", "Slight slope", "Slight terracing down to the seating area", "Ultra Real artificial turf", "Made by American Synthetic Turf"]),
   ("02 / Steel", "Tapered Planters", ["Two tapered steel planters", "V shape", "Light in the upper rim", "Cutout with a second low voltage light", "Each on two turf steps"]),
   ("03 / Fire", "Floating Fire Pit", ["Black diamond boulder", "Hole drilled in the bottom", "Mounted on an oil field pipe", "Mirrors mounted under the boulder", "Gas line through the pipe", "Hole drilled through the boulder for the gas line", "Top carved out", "Fire glass that looks like obsidian"]),
   ("04 / Stone", "Floating Bench", ["Floating bench", "Mirrors mounted under the bench"]),
   ("05 / Concrete", "Marbled", ["Finished smooth", "Marbling effect", "Formed with 1/4-inch by 4-inch steel", "Steel remains in place"]),
   ("06 / Lighting", "Low Voltage", ["Low voltage lights", "BTF COB lights", "Light in the upper rim of each planter", "Second low voltage light in each cutout"]),
   ("07 / Plant Palette", "Nine Plants", PLANTS),
   ("08 / Deck", "Ready Seal", ["Wood deck", "Stained with Ready Seal"]),
  ],
  "meta": [("Built", "2024"), ("Turf", "Ultra Real"), ("Fire Pit + Bench", "Floating Boulders"), ("Concrete", "Formed in Steel")],
 },
 "faqs": FAQS,
 "links": [
  ("../blog/artificial-grass-installation-austin-tx", "Artificial grass installation"),
  ("../blog/tapered-steel-planter-austin-tx", "Tapered steel planters"),
  ("../services/turf-installation-austin-tx", "Turf installation"),
  ("../services/custom-planters-austin-tx", "Custom steel planters"),
  ("../services/fire-pits-austin-tx", "Custom fire pits"),
  ("../services/landscape-lighting-austin-tx", "Landscape lighting"),
  ("../services/marbled-concrete-patios-austin-tx", "Marbled concrete patios"),
  ("../contact", "Free consultation"),
 ],
 "next": {"href": "hopeland", "eb": "Next / 03", "title": "Hopeland <em>Build.</em>",
          "im": IM("Deck platforms at dusk leading to a slatted wood shelter with seating, with a boulder fire pit burning on the deck and a dark planter lit along its rim in front, in Circle C, Austin",
                   (HOPE + "hero-800.webp", 800), (HOPE + "hero.webp", 1200))},
}

build(ROOT, SPEC)

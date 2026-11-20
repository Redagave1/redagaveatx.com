"""Outdoor fireplaces service page. NOT BUILT until FIREPLACES below has at least one real build with photos.

Checked 2026-11-20: every photo in images/gallery (264), images/featured (127), and images/projects was looked at
on contact sheets. They show fire pits, fire tables, fire troughs, and carved boulder fire pits. None shows an
outdoor fireplace. The only fireplace text on the site is a general comparison with fire pits
(services/fire-pits-austin-tx, blog/outdoor-living-space-guide-austin-tx, blog/backyard-fire-pit-area-ideas-austin-tx).
The fire pits page says "We build both", and Jensen has confirmed we build them, but there is no build to show.

NEEDED FROM JENSEN, for each fireplace we have built:
  1. Photos: at least two of the finished fireplace (one wide, one close), plus a build photo if there is one.
     No house numbers in view. Save as WebP in images/projects/svc-outdoor-fireplaces-austin-tx/ at 1200 and 800 wide.
  2. The area it is in (for example "West Lake Hills").
  3. What it is built from: the core and the face (block, stone, brick, stucco, poured concrete, steel).
  4. Gas or wood.
  5. Where it stands: under a roof, at the end of a patio, or in the open.
  6. Its parts: chimney, hearth, mantel, wood storage, seat walls. Only the ones it has.
Fill in FIREPLACES, then run:  python3 -I .claude/service-pages/make_fireplaces.py . [--register]

Everything else on the page is written from text already on the site. Look at each photo before writing its alt text.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

FIREPLACES = [
    # dict(area="",          # "West Lake Hills"
    #      built_from="",    # "CMU block faced in limestone"
    #      fuel="",          # "gas" or "wood"
    #      setting="",       # "at the end of a covered patio"
    #      parts="",         # "a raised hearth and a steel mantel"   (or "" when there is nothing to add)
    #      link="",          # "../projects/<slug>" when the build has its own page, else ""
    #      photos=[("images/projects/svc-outdoor-fireplaces-austin-tx/<name>-1200.webp", 1200, 900, "alt text: what the photo shows, and the area")]),
]

_missing = [i for i, f in enumerate(FIREPLACES)
            if not all(str(f.get(k, "")).strip() for k in ("area", "built_from", "fuel", "setting")) or not f.get("photos")]
if not FIREPLACES or _missing:
    sys.exit("make_fireplaces.py: NOT BUILT. The site has no photo of an outdoor fireplace we built and no facts about one. "
             "Needed from Jensen for each fireplace: (1) two or more photos of the finished fireplace, (2) the area, "
             "(3) what it is built from, (4) gas or wood, (5) where it stands (under a roof, at the end of a patio, in the open), "
             "(6) its parts (chimney, hearth, mantel, wood storage, seat walls). Fill in FIREPLACES at the top of this script. "
             "No page was written.")

from svc_lib import build, register, fig, step, sec, H3
from svc_extra import check, AREAS, STANDING

ROOT = sys.argv[1]
SLUG = "outdoor-fireplaces-austin-tx"
FIRST = FIREPLACES[0]
PHOTOS = [p for f in FIREPLACES for p in f["photos"]]
for p in PHOTOS:
    assert os.path.exists(os.path.join(ROOT, p[0])), ("missing photo", p[0])


def _line(f):
    s = f"<strong>{f['area']}:</strong> an outdoor fireplace built from {f['built_from']}, burning {f['fuel']}, {f['setting']}"
    if f.get("parts"): s += f", with {f['parts']}"
    s += "."
    if f.get("link"): s += f" See <a href=\"{f['link']}\">the project</a>."
    return f"      <li>{s}</li>"


BUILDS = "\n".join(_line(f) for f in FIREPLACES)
AREAS_BUILT = ", ".join(dict.fromkeys(f["area"] for f in FIREPLACES))

FAQS = [
    ("Who builds outdoor fireplaces in Austin, TX?",
     f"Red Agave Landscape designs and builds outdoor fireplaces and fire pits in Austin. We have built an outdoor fireplace in {AREAS_BUILT}. Every project is built by our own crew and starts with a free consultation, with the CAD plan included."),
    ("What is the difference between an outdoor fireplace and a fire pit?",
     "A fire pit is open on all sides, so people sit all the way around it. An outdoor fireplace is a wall piece that faces one direction, throws its heat that way, and gives an outdoor room a focal point."),
    ("Which gives more heat, a fireplace or a fire pit?",
     "A fireplace. Its heat is directional and reflects out of the firebox toward the seating. A fire pit gives off its heat in the open, in every direction."),
    ("How much room does an outdoor fireplace need?",
     "A fireplace is 6 to 8 feet wide and needs 8 feet of clearance in front of it. A fire pit is 3 to 4 feet across, with a 6-foot ring of seating around it."),
    ("Where does an outdoor fireplace work best?",
     "In a full outdoor living room with a covered structure. A fireplace anchors one end of a long covered patio and gives the space the feel of a room."),
    ("Is a fire pit a better fit for most Austin backyards?",
     "Yes. A fire pit takes less space, seats people all the way around, and needs no structural walls. A fireplace suits a large property and a covered outdoor room."),
    ("Does an outdoor fireplace burn gas or wood?",
     f"Either. Ours in {FIRST['area']} burns {FIRST['fuel']}. Gas lights at once and makes no smoke or ash. Wood gives the crackle and the smell of a real fire, and it cannot be burned during a burn ban."),
    ("What is an outdoor fireplace built from?",
     f"Masonry. Ours in {FIRST['area']} is built from {FIRST['built_from']}."),
    ("Does a gas fireplace need a permit in Austin?",
     "A gas line needs a plumbing permit, and a licensed plumber runs the line from the meter. A roofed structure attached to the house needs a building permit. We handle the permits."),
    ("What does an outdoor fireplace cost in Austin?",
     "Every fireplace is priced after a free on-site consultation. The size, the masonry, the fuel, and the distance to the gas line drive the price."),
]

S = ""
S += sec("The Work", "What Outdoor Fireplaces Do We Build?", f"""    <p>Masonry fireplaces that anchor an outdoor room. We build fire pits far more often, and we build fireplaces where the space calls for one.</p>
    <ul>
{BUILDS}
    </ul>
    {fig([PHOTOS[0]], f"{FIRST['area']}: an outdoor fireplace built from {FIRST['built_from']}.")}
    <p>For fire in the open, see our <a href="fire-pits-austin-tx">custom fire pits</a> page.</p>""")

S += sec("Compare", "Outdoor Fireplace or Fire Pit?", f"""    <p>They do different jobs. A fire pit gathers people in a circle, and a fireplace gives a room a front.</p>
    <table class="cost-table">
      <thead><tr><th></th><th>Fire Pit</th><th>Outdoor Fireplace</th></tr></thead><tbody>
      <tr><td>Seating</td><td>All the way around</td><td>On one side, facing the fire</td></tr>
      <tr><td>Heat</td><td>Given off in the open</td><td>Directional, reflected out toward the seating</td></tr>
      <tr><td>Space</td><td>3 to 4 feet across, with a 6-foot ring of seating</td><td>6 to 8 feet wide, with 8 feet of clearance in front</td></tr>
      <tr><td>Look</td><td>Low and casual</td><td>The focal point of the space</td></tr>
      <tr><td>Structure</td><td>Added to a patio with little structural work</td><td>Masonry and structural work</td></tr>
      <tr><td>Fuel</td><td>Gas or wood</td><td>Gas or wood</td></tr>
      </tbody></table>
    <p>Most Austin backyards are better suited to a fire pit. It takes less room, and it needs no walls. A fireplace suits a large property and a covered outdoor room. Our post on <a href="../blog/custom-fire-pits-austin-tx">custom fire pits</a> shows the pits we build.</p>""", alt=True)

S += sec("Where It Goes", "Where Does an Outdoor Fireplace Belong?", f"""    <p>At the end of a room. A fireplace works best in a full outdoor living room with a covered structure, where it anchors one end of a long covered patio.</p>
    <ul>
      <li><strong>It makes a wall:</strong> a fireplace gives an open patio a back, so the space feels like a room.</li>
      <li><strong>It sets the seating:</strong> the furniture faces it, the way it does indoors.</li>
      <li><strong>It works with a roof:</strong> the roof, the patio, and the fireplace are drawn on one plan.</li>
    </ul>
    <p>See our <a href="patio-covers-pavilions-austin-tx">patio covers and pavilions</a> page for the roof, and our <a href="outdoor-living-austin-tx">outdoor living</a> page for the whole room.</p>""")

S += sec("Structure", "What Does It Take to Build One?", f"""    <p>Masonry and structural work. That is the difference from a fire pit, which can be added to a patio with little structure.</p>
    <p>Our masonry is built on a core of CMU block or poured concrete. Stone veneer is set in mortar over the core: natural limestone, chopped stone, ledgestone, or Austin stone. In {FIRST['area']} the fireplace is built from {FIRST['built_from']}.</p>
    <p>See our <a href="masonry-concrete-austin-tx">masonry and concrete</a> page.</p>
    {fig(PHOTOS[1:3], "The fireplace up close.") if len(PHOTOS) > 1 else ""}""", alt=True)

S += sec("Fuel", "Gas or Wood?", f"""    <p>Either one. The choice changes how you use the fire.</p>
    <ul>
      <li><strong>Gas:</strong> lights at once, with no smoke and no ash. A burn ban does not affect it. A licensed plumber runs the gas line from the meter.</li>
      <li><strong>Wood:</strong> gives the crackle and the smell of a real fire. It makes smoke and ash, and it cannot be burned during a burn ban.</li>
    </ul>
    <p>Our <a href="../blog/gas-vs-wood-fire-pit-austin-tx">gas vs wood guide</a> compares the two.</p>""")

S += sec("Season", "When Do You Use an Outdoor Fireplace in Austin?", f"""    <p>Through the cool months. A fire extends the outdoor season into Austin's mild winters, and it gives people a place to gather.</p>
    {AREAS}
    {STANDING}
    <p>More of our built work is on the <a href="../featured">Signature Projects</a> page.</p>""", alt=True)

ANSWER = (f"<strong>Red Agave Landscape</strong> designs and builds outdoor fireplaces in Austin, TX. "
          f"In {FIRST['area']} we built one from {FIRST['built_from']}, burning {FIRST['fuel']}, {FIRST['setting']}. "
          "An outdoor fireplace is a masonry wall piece with directional heat, and it works best at the end of a covered outdoor room. "
          "We also build fire pits, which suit most Austin backyards. "
          "We have built in Austin since 2009, and every project is built by our own crew. "
          "Each one starts with a free consultation, and the CAD plan is included. Call or text 512-695-7566.")
check(S, ANSWER, *[q + " " + a for q, a in FAQS])

build(ROOT, dict(
    slug=SLUG, crumb="Outdoor Fireplaces", h1="Outdoor Fireplaces",
    title="Outdoor Fireplaces Austin TX | Custom Masonry",
    desc="Red Agave designs and builds outdoor fireplaces in Austin, TX: masonry fireplaces in gas or wood, drawn with the patio and the roof over it.",
    og_img="https://www.redagaveatx.com/" + PHOTOS[0][0],
    bg_l="../" + PHOTOS[0][0], bg_s="../" + PHOTOS[0][0].replace("-1200.webp", "-800.webp"),
    answer_h2="Who Builds Outdoor Fireplaces in Austin, TX?",
    answer=ANSWER,
    sections=S, faqs=FAQS, cta="Design Your Outdoor Fireplace",
    service_name="Outdoor Fireplaces", service_type="Outdoor fireplace design and construction",
    service_desc="Outdoor fireplaces designed and built in Austin, TX: masonry fireplaces in gas or wood, drawn with the patio and the covered structure around them. Built by Red Agave's own crew, with a free consultation and the CAD plan included."))

card = ('  <a href="services/' + SLUG + '" class="svc-card rev"><img src="' + PHOTOS[0][0].replace("-1200.webp", "-800.webp") + '" '
        'sizes="(max-width:768px) 80vw, 33vw" alt="' + PHOTOS[0][3].replace('"', "&quot;") + '" loading="lazy"><div class="svc-ov"></div>'
        '<div class="svc-info"><div class="svc-n">{N}</div><div class="svc-name">Outdoor Fireplaces</div><div class="svc-desc">Masonry fireplaces in gas or wood</div></div></a>\n')
if "--register" in sys.argv:
    register(ROOT, SLUG, card, "- Outdoor fireplaces (masonry fireplaces in gas or wood; built in " + AREAS_BUILT + "): redagaveatx.com/services/" + SLUG, "2026-11-20")

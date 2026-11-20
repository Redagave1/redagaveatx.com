import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svc_lib import build, register, fig, step, sec, H3
from svc_extra import check, AREAS, STANDING

ROOT = sys.argv[1]
SLUG = "patio-covers-pavilions-austin-tx"
P = "images/projects/"
SR = P + "south-austin-screened-room/"

FAQS = [
    ("Who builds patio covers and pavilions in Austin, TX?",
     "Red Agave Landscape designs and builds patio covers, pavilions, and screened rooms in Austin. In South Austin we built a welded steel frame with a metal roof, a cedar plank ceiling, two skylights, and screens. In West Lake Hills we built an outdoor kitchen under its own flat roof. Every project is built by our own crew and starts with a free consultation, with the CAD plan included."),
    ("What is the difference between a pergola and a pavilion?",
     "A pergola is an open frame of posts and beams with rafters or slats on top. A pavilion has a solid roof and gives full shade and rain protection."),
    ("Can a pergola frame take a solid roof?",
     "Yes. In South Austin we put ribbed metal roof panels over a welded steel pergola frame and finished the underside with a cedar plank ceiling."),
    ("Can a patio cover have skylights?",
     "Yes. We weld an opening for each skylight into the roof framing before the roof goes on. Our South Austin room has two, each at the top of a well lined in cedar."),
    ("Can a covered patio be screened in?",
     "Yes. A steel frame holds screen panels between its posts. In South Austin the screens run around three sides, with a low rail and a screen door to the yard."),
    ("Can a patio cover have a ceiling fan, lights, and a TV?",
     "Yes. Our covered kitchen in West Lake Hills has four recessed lights in its wood ceiling, a ceiling fan centered over the counter, and a TV on the back wall. The wiring goes in before the ceiling boards close."),
    ("Does a patio cover need a permit in Austin?",
     "A solid roof attached to the house needs a building permit with structural drawings. The City of Austin exempts a one-story detached accessory structure of 200 square feet or less and 15 feet tall or less, with no plumbing, outside a flood hazard area. We handle the permit and the plans."),
    ("Does a patio cover count as impervious cover in Austin?",
     "Yes. A solid roof counts toward the impervious cover limit of the lot. An open pergola with no solid roof does not."),
    ("Do you build outdoor kitchens under a roof?",
     "Yes. In West Lake Hills the kitchen stands under its own flat roof with a wood ceiling. In East Austin an L-shaped kitchen runs along the walls of a covered patio."),
    ("What does a patio cover cost in Austin?",
     "Every patio cover is priced after a free on-site consultation. The size, the frame, the roof, the ceiling, the screens, and the electrical work drive the price. Our Austin pergola guide covers materials and cost ranges."),
]

S = ""
S += sec("The Difference", "Pergola, Patio Cover, Pavilion, or Screened Room?", f"""    <p>The roof decides it. A pergola is open to the sky. The other three have a solid roof, and they differ in where they stand and what closes the sides.</p>
    <table class="cost-table">
      <thead><tr><th>Structure</th><th>What It Is</th><th>Roof</th></tr></thead><tbody>
      <tr><td>Pergola</td><td>An open frame of posts and beams, with rafters or slats on top</td><td>Open</td></tr>
      <tr><td>Patio cover</td><td>A solid roof attached to the house, over the patio</td><td>Solid</td></tr>
      <tr><td>Pavilion</td><td>A solid roof that stands on its own posts</td><td>Solid</td></tr>
      <tr><td>Screened room</td><td>A covered frame with screens and a door</td><td>Solid</td></tr>
      </tbody></table>
    <p>One frame can be all of them, one after another. In South Austin our steel frame stood on the slab as an open pergola, then took a metal roof, then took screens. This page covers the roofed structures. For open shade, see our <a href="pergolas-austin-tx">custom pergolas</a> page.</p>
    {fig([(SR + "05-finished-screened-room-exterior-1200.webp", 1200, 688, "Finished screened room on a concrete slab at the back of a house in South Austin, with black-framed screens, a screen door with a pet door, and a cedar ceiling with two skylights")],
         "South Austin: a welded steel frame with a metal roof, a cedar ceiling, two skylights, and screens on three sides.")}""")

S += sec("South Austin", "How Does a Steel Frame Become a Covered Room?", f"""    <p>In order, with the steel first. Every later part fastens to the frame, so the steel is set and squared before anything else arrives. These are the parts of the room we built in South Austin:</p>
    <ul>
      <li><strong>Frame:</strong> square steel tube, welded, finished black</li>
      <li><strong>Roof:</strong> ribbed metal panels over the steel</li>
      <li><strong>Ceiling:</strong> cedar planks</li>
      <li><strong>Skylights:</strong> two, with wells lined in the same cedar</li>
      <li><strong>Fan:</strong> a black ceiling fan with a light</li>
      <li><strong>Walls:</strong> screens in black frames, with a low rail</li>
      <li><strong>Door:</strong> a screen door with a pet door built into it</li>
      <li><strong>Floor:</strong> a concrete slab</li>
    </ul>
    <p>The frame runs along the back wall of the house and passes above the French doors. The posts are slim, so the walls are almost all screen.</p>
    {fig([(SR + "01-steel-pergola-frame-on-slab-800.webp", 800, 1067, "Welded steel pergola frame standing on a concrete slab against the back wall of a house in South Austin"),
          (SR + "04-cedar-ceiling-screens-going-in-800.webp", 800, 1067, "Cedar plank ceiling with a skylight well and the first black-framed screen panels going into a steel frame in South Austin"),
          (SR + "06-screen-door-metal-roof-eave-800.webp", 800, 1067, "Black-framed screens and a screen door under the eave of a ribbed metal roof, with a cedar ceiling and a fan inside, in South Austin")],
         "The same room in three stages: the steel frame on the slab, the cedar ceiling with the first screens, and the finished roof edge.")}
    <p>The full sequence is in our post on the <a href="../blog/custom-pergola-build-south-austin-tx">custom pergola build in South Austin</a>.</p>""", alt=True)

S += sec("Overhead", "What Roof and Ceiling Do We Build?", f"""    <p>A solid roof on top and a finished ceiling under it. The roof keeps the weather out, and the ceiling is the part you look at.</p>
    <ul>
      <li><strong>Roof:</strong> ribbed metal panels, standing seam metal, or cedar shingle</li>
      <li><strong>Ceiling:</strong> cedar planks or tongue-and-groove wood boards</li>
      <li><strong>Skylights:</strong> an opening for each one is welded into the roof framing before the roof goes on</li>
      <li><strong>Lights:</strong> recessed lights set into the ceiling boards</li>
      <li><strong>Fan:</strong> a ceiling fan, wired above the boards</li>
    </ul>
    <p>Skylights answer one problem a roof creates. A solid roof over the back doors shades them, and the skylights bring daylight back in. In South Austin the cedar ceiling is carried up into each opening, so each skylight sits at the top of a cedar well.</p>
    <p>The wiring is hidden. We run electrical through the posts and beams, so no conduit shows, and we coordinate with a licensed electrician for the panel connection.</p>
    {fig([(P + "kitchens/covered-cedar-kitchen-800.webp", 800, 1000, "Covered outdoor kitchen at dusk in West Lake Hills with a wood plank ceiling, four recessed lights, a ceiling fan, a TV, a stainless grill, and a dark brick base under a flat roof on black posts"),
          (SR + "07-cedar-skylight-well-ceiling-fan-800.webp", 800, 1067, "Skylight well lined in cedar planks above a black ceiling fan in a screened room in South Austin")],
         "Two ceilings: wood boards with recessed lights and a fan in West Lake Hills, and a cedar skylight well in South Austin.")}""")

S += sec("West Lake Hills", "What Goes Under a Roof Built for a Kitchen?", f"""    <p>Everything the cook needs overhead. In West Lake Hills the outdoor kitchen stands under its own flat roof on black posts, with a tongue-and-groove wood ceiling and a back wall clad in horizontal wood boards.</p>
    <p>Building the roof and the kitchen together let us put each part where it belongs:</p>
    <ul>
      <li><strong>Four recessed lights</strong> over the counter</li>
      <li><strong>A ceiling fan</strong> centered over the cook</li>
      <li><strong>A TV</strong> on the back wall, above the counter</li>
      <li><strong>A light strip</strong> under the counter edge that washes the slab at night</li>
    </ul>
    <p>The kitchen itself has a stainless built-in grill, a sink, and two under-counter refrigerators in a dark brick base with a stone countertop. A kitchen with its own roof can sit wherever the yard works best. See our <a href="outdoor-kitchens-austin-tx">outdoor kitchens</a> page and our post on <a href="../blog/outdoor-kitchen-under-roof-austin-tx">outdoor kitchens under a roof</a>.</p>""", alt=True)

S += sec("East Austin", "Can the Walls Be Glass?", f"""    <p>Yes. In East Austin we built a glass-walled screened porch at the back of the house, beside the pool. It has floor-to-ceiling glass walls on three sides, a tongue-and-groove cedar ceiling, and a ceiling fan.</p>
    <p>The porch was designed around the water. From the dining table inside, the pool is framed like a picture. A teak deck runs flush from the porch to the outdoor kitchen, with no step and no transition strip.</p>
    {fig([(P + "ulit/029-800.webp", 800, 534, "Screened porch with a cedar ceiling, a dining table, and yellow chairs, looking through its walls onto a lit pool at dusk in East Austin"),
          ("images/gallery/img-5394.webp", 800, 600, "Screened porch with tall dark-framed walls and a sliding door beside a pool with pale coping, by day, in East Austin")],
         "East Austin: the porch from inside at dusk, and from the pool deck by day.", wide=True)}
    <p>The whole yard is on the <a href="../projects/ulit">East Austin project page</a>, and the deck is in our post on <a href="../blog/deck-builder-austin-tx">deck building in Austin</a>.</p>""")

S += sec("Austin Weather", "Why Put a Solid Roof Over a Patio in Austin?", f"""    <p>For the sun and for the rain. Austin summers push past 100 degrees for weeks at a time, and the rain tends to arrive all at once.</p>
    <ul>
      <li><strong>Sun:</strong> a solid roof gives full shade, where a pergola gives partial shade.</li>
      <li><strong>Rain:</strong> the City of Austin describes the region as Flash Flood Alley, and normal rainfall at Camp Mabry is 36.25 inches a year. A roof keeps it off the counters, the appliances, and the furniture.</li>
      <li><strong>Air:</strong> a roof gives you a ceiling, and a ceiling carries a fan to keep the air moving on a still summer evening.</li>
      <li><strong>Light:</strong> the same ceiling holds the lights, so the room works after dark.</li>
    </ul>
    <p>A roof turns a patio into a room. See how the rest of the room comes together on our <a href="outdoor-living-austin-tx">outdoor living</a> page, and compare the options in our <a href="../blog/shade-structure-ideas-austin-tx">shade structure ideas</a>.</p>""", alt=True)

S += sec("Permits", "Does a Patio Cover Need a Permit in Austin?", f"""    <p>Attachment and size decide it. A roofed structure attached to a house is permitted differently from an open pergola in the yard.</p>
    <table class="cost-table">
      <thead><tr><th>Structure</th><th>City of Austin</th></tr></thead><tbody>
      <tr><td>Solid roof attached to the house</td><td>Building permit, with structural drawings</td></tr>
      <tr><td>One-story detached structure, 200 square feet or less and 15 feet tall or less, with no plumbing, outside a flood hazard area</td><td>On the city's list of work exempt from a building permit</td></tr>
      <tr><td>Any structure with a solid roof</td><td>Counts toward the impervious cover limit of the lot</td></tr>
      <tr><td>Open pergola with no solid roof</td><td>Does not count as impervious cover</td></tr>
      </tbody></table>
    <p>Exempt work still has to meet the building code and the city code. Cedar Park and the other cities around Austin have their own rules, and many HOA communities review exterior changes from a drawn plan.</p>
    <p>We handle the permit and the plans. Our <a href="../blog/patio-cover-permit-austin-tx">patio cover permit guide</a> covers setbacks, impervious cover, and what the city asks for.</p>""")

S += sec("The Build", "How Is a Patio Cover Built?", f"""    <p>From the plan up. These are the steps, in the order we built the South Austin room.</p>
    {step(1, "Consultation and Plan", "Free and on site. We walk the yard with you, and the owner draws the structure on a CAD plan, which is included. See our <a href=\"landscape-design-austin-tx\">landscape design</a> page.")}
    {step(2, "Permit", "We prepare the plans and handle the permit where the structure needs one.")}
    {step(3, "Slab and Frame", "The frame goes up on the slab first, and alone. Posts stand at the corners and along the outer edge, and the roof framing sits on top.")}
    {step(4, "Roof and Skylights", "The skylight openings are already in the framing. The roof panels go on over the steel.")}
    {step(5, "Ceiling and Wiring", "Wiring for the lights and the fan runs above the boards, and then the ceiling closes.")}
    {step(6, "Screens and Finish", "Screen panels go in between the posts, the door is hung, and the fan goes up.")}
    <p>The patio under the roof is part of the same job. We coordinate the patio with the structure above it, so the footings, the columns, and the drainage work together. See our <a href="patios-austin-tx">patios</a> and <a href="custom-decks-austin-tx">custom decks</a> pages.</p>""", alt=True)

S += sec("Our Work", "Where Have We Built Roofed Structures?", f"""    <ul>
      <li><strong>South Austin:</strong> a welded steel frame finished as a screened room, with a ribbed metal roof, a cedar plank ceiling, two skylights, and a ceiling fan. See <a href="../blog/custom-pergola-build-south-austin-tx">the build</a>.</li>
      <li><strong><a href="../locations/westlake-hills-tx">West Lake Hills</a>:</strong> an outdoor kitchen under its own flat roof on black posts, with a wood ceiling, recessed lights, a fan, and a TV. See <a href="../blog/outdoor-kitchen-under-roof-austin-tx">the kitchen</a>.</li>
      <li><strong>East Austin:</strong> a glass-walled screened porch with a cedar ceiling and a fan, beside a pool and a teak deck. See <a href="../projects/ulit">the project</a>.</li>
      <li><strong><a href="../locations/cedar-park-tx">Cedar Park</a>:</strong> the open version. A steel pergola built from scratch along a privacy fence, with wood rafters over a stone patio. See our <a href="../blog/pergola-builder-austin-tx">pergola builder</a> post.</li>
    </ul>
    {fig([(P + "ulit/032-1200.webp", 1200, 800, "East Austin backyard at dusk with a glass-walled screened porch under a wood ceiling with recessed lights and fans, a pool behind a vine-covered wire screen, a lounge under a red shade sail, and an outdoor kitchen")],
         "East Austin at dusk: the screened porch, the pool, the lounge under the shade sail, and the kitchen.")}
    {AREAS}
    {STANDING}
    <p>For materials and cost ranges, see our <a href="../blog/pergola-guide-austin-tx">Austin pergola guide</a>. More of our built work is on the <a href="../featured">Signature Projects</a> page.</p>""")

ANSWER = ("<strong>Red Agave Landscape</strong> designs and builds patio covers, pavilions, and screened rooms in Austin, TX. "
          "Each one has a solid roof, a finished wood ceiling, and the lights and the fan wired in above the boards. "
          "In South Austin we built a welded steel frame with a ribbed metal roof, a cedar plank ceiling, two skylights, and screens on three sides. "
          "In West Lake Hills we built an outdoor kitchen under its own flat roof. "
          "We have built in Austin since 2009, and every project is built by our own crew. "
          "Each one starts with a free consultation, and the CAD plan is included. Call or text 512-695-7566.")
check(S, ANSWER, *[q + " " + a for q, a in FAQS])

build(ROOT, dict(
    slug=SLUG, crumb="Patio Covers and Pavilions", h1="Patio Covers &amp; Pavilions",
    title="Patio Covers & Pavilions Austin TX | Red Agave",
    desc="Red Agave builds patio covers, pavilions, and screened rooms in Austin, TX: steel frames, metal roofs, cedar ceilings, skylights, and fans.",
    og_img="https://www.redagaveatx.com/images/projects/ulit/032-1200.webp",
    bg_l="../images/projects/ulit/032-1200.webp",
    bg_s="../images/projects/ulit/032-800.webp",
    answer_h2="Who Builds Patio Covers and Pavilions in Austin, TX?",
    answer=ANSWER,
    sections=S, faqs=FAQS, cta="Put a Roof Over Your Patio",
    service_name="Patio Covers, Pavilions, and Screened Rooms", service_type="Patio cover and pavilion design and construction",
    service_desc="Patio covers, pavilions, and screened rooms designed and built in Austin, TX: welded steel frames, ribbed and standing seam metal roofs, cedar plank and tongue-and-groove wood ceilings, skylights, recessed lights, ceiling fans, and screens. Built by Red Agave's own crew, with a free consultation and the CAD plan included."))

card = ('  <a href="services/' + SLUG + '" class="svc-card rev"><img src="images/projects/kitchens/covered-cedar-kitchen-800.webp" '
        'sizes="(max-width:768px) 80vw, 33vw" alt="Covered outdoor kitchen under a flat roof with a wood plank ceiling, recessed lights, and a ceiling fan in West Lake Hills, TX" loading="lazy"><div class="svc-ov"></div>'
        '<div class="svc-info"><div class="svc-n">{N}</div><div class="svc-name">Patio Covers &amp; Pavilions</div><div class="svc-desc">Solid roofs, wood ceilings &amp; screened rooms</div></div></a>\n')
if "--register" in sys.argv:
    register(ROOT, SLUG, card, "- Patio covers, pavilions, and screened rooms (welded steel frames, metal roofs, cedar plank and wood ceilings, skylights, ceiling fans, screens; built in South Austin, West Lake Hills, and East Austin): redagaveatx.com/services/" + SLUG, "2026-11-20")

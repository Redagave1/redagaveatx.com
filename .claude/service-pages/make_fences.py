import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svc_lib import build, register, fig, step, sec, H3
from svc_extra import check, AREAS, STANDING

ROOT = sys.argv[1]
SLUG = "fences-gates-austin-tx"
P = "images/projects/"
F = P + "svc-fences-gates-austin-tx/"

FAQS = [
    ("Who builds custom fences and gates in Austin, TX?",
     "Red Agave Landscape designs and builds custom fences and gates in Austin in cedar and mild steel: privacy fences, property dividers, decorative metal panels, and gates in welded steel frames. Every fence is built by our own crew and starts with a free consultation, with the CAD plan included."),
    ("What fence materials do you build with?",
     "Cedar and mild steel. We use western red cedar for privacy fencing and powder-coated steel for decorative and front yard fencing. We also build walls of stucco and breeze block where a wall is the better fence."),
    ("Do you build horizontal fences?",
     "Yes. In East Austin we built a horizontal cedar privacy fence around a pool yard. On a sloped lot we built a black horizontal fence that steps down the hill in level sections."),
    ("Do you build custom gates?",
     "Yes. We weld the gate frame in steel and fill it with wood. One of our gates holds weathered boards laid on the diagonal in a welded steel frame. Another is a gate of vertical wood boards set in a breeze block wall."),
    ("Can a fence follow a sloped yard?",
     "Yes. A fence on a slope is built with stepped or racked panels. A stepped fence keeps each section level and drops at the posts."),
    ("Do I need a permit for a fence in Austin?",
     "Most residential fences in Austin do not need a building permit. The city lists fences under 7 feet tall, outside a flood hazard area, as exempt work. Our fence permit guide covers the height rules, corner lots, and the safe fencing code."),
    ("Can my HOA stop me from building a fence?",
     "No. Texas law prevents an HOA from banning a perimeter fence. An HOA can still regulate the materials, the color, the height, and the style, and many require approval before construction."),
    ("Does a pool need a fence in Austin?",
     "Yes. The City of Austin requires a barrier around every residential pool that is at least 48 inches tall, with a self-closing, self-latching gate. We include the fence permitting, and we design the barrier as part of the landscape."),
    ("Can a fence carry vines or lighting?",
     "Yes. In East Austin we built a steel trellis with wire grid panels that carries jasmine around a seating court. On another yard, warm light washes a new horizontal cedar fence at dusk."),
    ("What does a fence cost in Austin?",
     "Every fence is priced after a free on-site consultation. The length, the material, the height, the slope, the rock in the ground, and the number of gates drive the price. Our fence cost guide explains each one."),
]

S = ""
S += sec("The Work", "What Fences and Gates Do We Build?", f"""    <p>Fences drawn with the yard and built from the same materials as the rest of it. We build in cedar and mild steel: privacy fences, property dividers, decorative metal panels, and gates.</p>
    <table class="cost-table">
      <thead><tr><th>Type</th><th>What It Is</th><th>Where</th></tr></thead><tbody>
      <tr><td>Horizontal cedar fence</td><td>Cedar boards run level from post to post, for full privacy</td><td>Built in East Austin</td></tr>
      <tr><td>Black horizontal fence</td><td>Horizontal boards finished black on slim black posts</td><td>Built on a sloped lot</td></tr>
      <tr><td>Wood in a steel frame</td><td>Boards held in a welded steel frame, as a fence panel or a gate</td><td>Built</td></tr>
      <tr><td>Breeze block wall</td><td>A stucco wall topped with open terracotta blocks in a steel frame</td><td>Built</td></tr>
      <tr><td>Steel trellis</td><td>Steel posts and rails with wire grid panels for vines</td><td>Built in East Austin</td></tr>
      <tr><td>Steel screen</td><td>A perforated steel panel, lit from behind</td><td>Built in East Austin</td></tr>
      <tr><td>Pool barrier</td><td>A fence and a self-closing, self-latching gate around a pool</td><td>Built with the <a href="pools-austin-tx">pool</a></td></tr>
      </tbody></table>
    {fig([(F + "black-horizontal-fence-stepping-down-slope-1200.webp", 1200, 900, "Horizontal board fence finished black on slim black posts, stepping down a slope in level sections beside a house under large trees")],
         "A black horizontal fence that steps down a slope in level sections.")}""")

S += sec("Slopes", "How Does a Fence Handle a Slope?", f"""    <p>By stepping or by racking. Few Austin lots are flat, and a fence has to meet the ground along its whole length.</p>
    <ul>
      <li><strong>Stepped:</strong> each section stays level, and the top of the fence drops at the posts. This suits horizontal boards, because every board stays level.</li>
      <li><strong>Racked:</strong> the panels follow the angle of the ground.</li>
    </ul>
    <p>The black fence above is stepped. Each section is level, and the top of the fence drops at the posts as the lot falls away from the house.</p>
    <p>Where a slope has to be held and not only fenced, the wall comes first. See our <a href="retaining-walls-austin-tx">retaining walls</a> page.</p>""", alt=True)

S += sec("Cedar", "Why Cedar for a Privacy Fence?", f"""    <p>Because it lasts outdoors without help. Western red cedar holds natural oils that repel insects and resist rot with no chemical treatment. It takes stain well, and left alone it weathers to a silver gray.</p>
    <p>We run cedar boards horizontally on our privacy fences. In East Austin a horizontal cedar privacy fence closes the pool yard, and string lights trace the fence line overhead. On another Austin yard, warm light washes a new horizontal cedar fence behind a gravel court.</p>
    {fig([(P + "ulit/031-800.webp", 800, 534, "Horizontal cedar privacy fence with string lights along a pool and a teak deck at dusk in East Austin"),
          (F + "horizontal-cedar-fence-lit-dusk-800.webp", 800, 533, "New horizontal cedar fence washed with warm light at dusk, behind a gravel court, concrete pads, and steel planters in Austin")],
         "Horizontal cedar in East Austin, and a new cedar fence lit at dusk in Austin.", wide=True)}
    <p>For a fence that gives the same privacy from both sides, boards are overlapped with no gaps. That is board-on-board construction, and it looks the same from either yard.</p>""")

S += sec("Steel", "Where Does Steel Go in a Fence?", f"""    <p>In the frame, the posts, and the panels. We weld steel on site, so a gate or a panel is made to the opening and not ordered to a standard size.</p>
    <ul>
      <li><strong>Frames:</strong> a welded steel frame holds wood boards flat and square, as a gate or as a fixed panel.</li>
      <li><strong>Panels:</strong> we cut decorative steel panels and privacy partitions on our own CNC plasma table.</li>
      <li><strong>Trellis:</strong> steel posts and rails carry wire grid panels for vines.</li>
      <li><strong>Finish:</strong> steel is powder-coated, or it is left to weather to a rust patina.</li>
    </ul>
    <p>It is the same steel work as our <a href="steel-edging-austin-tx">steel edging</a>, our <a href="custom-planters-austin-tx">custom steel planters</a>, and our <a href="steel-retaining-walls-austin-tx">steel retaining walls</a>, so one material can run through the whole yard.</p>
    {fig([(F + "reclaimed-wood-gate-steel-frame-1200.webp", 1200, 900, "Gate of weathered wood boards laid on the diagonal in a welded steel frame, beside a fence panel of horizontal weathered boards with young vines on wire, set in gravel")],
         "Weathered boards in welded steel frames: a gate with the boards on the diagonal, and a panel with the boards level.")}""", alt=True)

S += sec("Gates", "What Gates Do We Build?", f"""    <p>Gates that match the fence, hung on steel. Two of ours:</p>
    <ul>
      <li><strong>The diagonal gate:</strong> weathered boards laid on the diagonal inside a welded steel frame. The fence panel beside it holds the same boards level, with wire over them for vines.</li>
      <li><strong>The gate in the wall:</strong> vertical wood boards in a steel frame, set between two sections of a breeze block wall.</li>
    </ul>
    <p>Every fence needs at least one gate, and the gate is chosen by what has to pass through it.</p>
    <table class="cost-table">
      <thead><tr><th>Gate</th><th>What It Is For</th></tr></thead><tbody>
      <tr><td>Walk gate</td><td>People. A standard walk gate is 3 to 4 feet wide.</td></tr>
      <tr><td>Double gate</td><td>Trailers and equipment into the backyard. Two panels meet in the middle.</td></tr>
      <tr><td>Sliding gate</td><td>A driveway. The gate rolls on a track, which suits a sloped drive.</td></tr>
      <tr><td>Pool gate</td><td>A pool barrier. The gate closes and latches itself.</td></tr>
      </tbody></table>
    <p>Our <a href="../blog/fence-cost-austin-tx">fence cost guide</a> compares the gate types and what a motor adds to a driveway gate.</p>""")

S += sec("Walls", "When Is a Wall the Better Fence?", f"""    <p>When the fence faces the street. A masonry wall gives a front yard a solid edge, and open block keeps it from feeling shut.</p>
    <p>At the front of one house we built a white stucco wall topped with terracotta breeze blocks in a steel frame. The blocks are open, so air and light pass through the top of the wall. A wood gate stands in the middle, steel planters sit at the foot of the wall, and square concrete pads in gravel lead to the gate.</p>
    {fig([(F + "breeze-block-wall-cedar-gate-800.webp", 800, 600, "White stucco wall topped with terracotta breeze blocks in a steel frame, with a gate of vertical wood boards, steel planters at its foot, and square concrete pads set in gravel"),
          (F + "breeze-block-steel-frame-detail-800.webp", 800, 600, "Terracotta breeze blocks held in a steel frame on a concrete base, seen along the length of the wall")],
         "A stucco and breeze block wall with a wood gate, and the blocks in their steel frame.", wide=True)}
    <p>Walls are part of our <a href="masonry-concrete-austin-tx">masonry and concrete</a> work.</p>""", alt=True)

S += sec("Green Screens", "Can a Fence Be a Trellis?", f"""    <p>Yes. A steel frame with a vine on it makes a living screen in a narrow strip of ground.</p>
    <p>In East Austin we built a steel trellis that wraps around two sides of a raised gravel court. It is steel posts and rails with wire grid panels, and jasmine climbs the panels behind the seating. See the <a href="../projects/signal-point">Signal Point project</a>.</p>
    <p>On a second East Austin yard, a steel-framed wire screen with a vine runs along the pool, and a perforated steel screen stands behind the outdoor kitchen, lit from behind at night.</p>
    {fig([(P + "signal-point/03-steel-trellis-jasmine-gravel-court-800.webp", 800, 600, "Steel trellis with wire grid panels and jasmine at the corner of a steel-framed gravel court, with a concrete fire pit behind it, in East Austin")],
         "East Austin: a steel trellis with wire grid panels, carrying jasmine around a gravel court.")}""")

S += sec("Austin Rules", "Does a Fence Need a Permit in Austin?", f"""    <p>Most do not. The rules that matter are height, floodplain, pools, and the HOA.</p>
    <table class="cost-table">
      <thead><tr><th>Question</th><th>Answer</th></tr></thead><tbody>
      <tr><td>Building permit</td><td>The City of Austin lists fences under 7 feet tall, outside a flood hazard area, as work that needs no building permit.</td></tr>
      <tr><td>Pools</td><td>A pool needs a barrier at least 48 inches tall, with a self-closing, self-latching gate.</td></tr>
      <tr><td>HOA</td><td>Texas law prevents an HOA from banning a perimeter fence. It can regulate materials, color, height, and style.</td></tr>
      <tr><td>Digging</td><td>Utility lines are marked through 811 before any post hole is dug.</td></tr>
      </tbody></table>
    <p>We handle HOA applications, property line verification, 811 calls, and code compliance as part of every fence project. Our <a href="../blog/fence-permit-austin-tx">fence permit guide</a> covers height by location on the lot, corner lots, and easements.</p>""", alt=True)

S += sec("One Plan", "Why Build the Fence With the Landscape?", f"""    <p>Because the fence is the back wall of every outdoor room. When it is drawn on the same plan as the yard, the parts meet.</p>
    <ul>
      <li><strong>Light:</strong> fixtures at the foot of the fence wash the boards at night. See our <a href="landscape-lighting-austin-tx">landscape lighting</a> page.</li>
      <li><strong>Planting:</strong> steel planters and beds are set against the fence line.</li>
      <li><strong>Shade:</strong> in <a href="../locations/cedar-park-tx">Cedar Park</a> we built a steel pergola along a horizontal privacy fence, so the strip beside the fence became a shaded walk. See our <a href="pergolas-austin-tx">pergolas</a> page.</li>
      <li><strong>Cooking:</strong> in East Austin the lounge and the outdoor kitchen sit inside the cedar fence line. See our <a href="outdoor-kitchens-austin-tx">outdoor kitchens</a> page.</li>
    </ul>""")

S += sec("How We Build", "How Is a Fence Built?", f"""    {step(1, "Consultation and Plan", "Free and on site. We walk the property with you, measure the fence line, and look at the soil and the slope. The fence goes on the CAD plan, which is included.")}
    {step(2, "Lines and Approvals", "We verify the property line, file the HOA application, and make the 811 call before any digging.")}
    {step(3, "Posts", "Posts go in first. Much of Austin sits on limestone, and rock in the ground changes how the post holes are made.")}
    {step(4, "Panels and Gates", "Boards go on post to post. Steel frames for gates and panels are welded to the opening.")}
    {step(5, "Finish", "Cedar is stained or left to weather. Steel is powder-coated or left to weather. Lighting and planting are fitted to the finished fence.")}""", alt=True)

S += sec("Our Work", "Where Have We Built Fences and Gates?", f"""    <ul>
      <li><strong>East Austin, a pool yard:</strong> a horizontal cedar privacy fence with string lights, a wire screen along the pool, and a perforated steel screen behind the kitchen. See <a href="../projects/ulit">the project</a>.</li>
      <li><strong>East Austin, a fire court:</strong> a steel trellis with wire grid panels and jasmine around a gravel court, built in 2018. See <a href="../projects/signal-point">Signal Point</a>.</li>
      <li><strong>Austin:</strong> a new horizontal cedar fence, lit along its length, behind a gravel court and steel planters.</li>
      <li><strong>A sloped lot:</strong> a black horizontal fence stepped down the hill in level sections.</li>
      <li><strong>A front yard:</strong> a stucco and breeze block wall with a wood gate, steel planters, and concrete pads.</li>
    </ul>
    <p>Fences come up in our reviews: a new fence and gate, a front fence on a new build in East Austin, and a fence followed by a back porch. Read them on our <a href="../reviews">reviews</a> page.</p>
    {AREAS}
    {STANDING}
    <p>For what drives the price, see our <a href="../blog/fence-cost-austin-tx">fence cost guide</a>. More of our built work is on the <a href="../featured">Signature Projects</a> page.</p>""")

ANSWER = ("<strong>Red Agave Landscape</strong> designs and builds custom fences and gates in Austin, TX in cedar and mild steel. "
          "We build horizontal cedar privacy fences, black horizontal fences stepped down a slope, gates of wood in welded steel frames, "
          "stucco and breeze block walls, and steel trellis screens for vines. "
          "We handle HOA applications, property line verification, 811 calls, and code compliance on every fence. "
          "We have built in Austin since 2009, and every fence is built by our own crew. "
          "Each project starts with a free consultation, and the CAD plan is included. Call or text 512-695-7566.")
check(S, ANSWER, *[q + " " + a for q, a in FAQS])

build(ROOT, dict(
    slug=SLUG, crumb="Fences and Gates", h1="Fences &amp; Gates",
    title="Fences & Gates Austin TX | Cedar, Steel & Custom",
    desc="Red Agave builds custom fences and gates in Austin, TX: horizontal cedar, wood in welded steel frames, breeze block walls, and steel trellis screens.",
    og_img="https://www.redagaveatx.com/images/projects/svc-fences-gates-austin-tx/black-horizontal-fence-stepping-down-slope-1200.webp",
    bg_l="../images/projects/svc-fences-gates-austin-tx/black-horizontal-fence-stepping-down-slope-1200.webp",
    bg_s="../images/projects/svc-fences-gates-austin-tx/black-horizontal-fence-stepping-down-slope-800.webp",
    answer_h2="Who Builds Custom Fences and Gates in Austin, TX?",
    answer=ANSWER,
    sections=S, faqs=FAQS, cta="Frame Your Yard",
    service_name="Custom Fences and Gates", service_type="Fence and gate design and construction",
    service_desc="Custom fences and gates designed and built in Austin, TX in cedar and mild steel: horizontal cedar privacy fences, black horizontal fences stepped down slopes, wood gates in welded steel frames, stucco and breeze block walls, steel trellis screens, and pool barriers. Built by Red Agave's own crew, with a free consultation and the CAD plan included."))

card = ('  <a href="services/' + SLUG + '" class="svc-card rev"><img src="images/projects/svc-fences-gates-austin-tx/black-horizontal-fence-stepping-down-slope-800.webp" '
        'sizes="(max-width:768px) 80vw, 33vw" alt="Black horizontal fence stepping down a slope in level sections" loading="lazy"><div class="svc-ov"></div>'
        '<div class="svc-info"><div class="svc-n">{N}</div><div class="svc-name">Fences &amp; Gates</div><div class="svc-desc">Horizontal cedar, steel frames &amp; breeze block</div></div></a>\n')
if "--register" in sys.argv:
    register(ROOT, SLUG, card, "- Fences and gates (horizontal cedar privacy fences, black horizontal fences stepped down a slope, wood gates in welded steel frames, stucco and breeze block walls, steel trellis screens, pool barriers): redagaveatx.com/services/" + SLUG, "2026-11-20")

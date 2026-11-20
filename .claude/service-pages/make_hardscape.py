import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svc_lib import build, register, fig, step, sec, H3

ROOT = sys.argv[1]
SLUG = "hardscaping-austin-tx"
P = "images/projects/"

FAQS = [
    ("Who does hardscaping in Austin, TX?",
     "Red Agave Landscape designs and builds hardscape in Austin in steel, concrete, stone, wood, and gravel: patios, walkways, steps, driveways, retaining walls, decks, steel edging, fire pits, and water features. Every project is built by our own crew and starts with a free consultation, with the CAD plan included."),
    ("What is hardscaping?",
     "The built part of a landscape: walls, patios, walkways, steps, driveways, decks, edging, fire pits, and water features. Plants, soil, and lawn are softscape."),
    ("What goes under a patio or walkway in Austin?",
     "We excavate, compact the subgrade, and lay 6 to 8 inches of compacted crushed limestone, graded so water moves away from the house. Austin clay swells and shrinks, and this base keeps the surface flat."),
    ("What concrete do you pour?",
     "A 4,000 PSI mix with fiber mesh and rebar. We form, pour, and finish our own concrete in brushed, exposed aggregate, smooth trowel, and marbled finishes."),
    ("Does hardscaping go in before planting?",
     "Yes. Hardscape sets the levels of the yard, so it goes in first. Drainage comes before the hardscape, and planting and lighting are fitted to it."),
    ("Can hardscape fix a sloped yard?",
     "Yes. At the Overlook at Lewis Mountain in Southwest Austin we cut a bare slope into three steel terraces and two deck levels, and every level is now usable."),
    ("Do you build walkways and steps?",
     "Yes. We build walkways in concrete, flagstone, and pavers, and as stepping pads set in gravel or turf. We pour concrete steps, set stone treads, and weld steel risers."),
    ("Which patio surface stays coolest in the Austin sun?",
     "Travertine. It stays cooler than concrete in direct sun, which is why it is used around pools."),
    ("Do you design the hardscape too?",
     "Yes. The owner draws every plan, and our own crew builds it. The consultation is free, and the CAD plan is included."),
    ("What does hardscaping cost in Austin?",
     "Every project is priced after a free on-site consultation. The size, the materials, the slope, and the access drive the price. Our cost guides explain each one."),
]

S = ""
S += sec("What We Build", "What Hardscaping Do We Build?", f"""    <p>Everything in a yard that is built and not grown. One crew builds all of it, so the patio, the walls, and the steps meet where the plan says they meet.</p>
    <table class="cost-table">
      <thead><tr><th>Element</th><th>Built In</th><th>More</th></tr></thead><tbody>
      <tr><td>Patios</td><td>Poured concrete, marbled concrete, pavers, travertine, flagstone</td><td><a href="patios-austin-tx">Patios</a></td></tr>
      <tr><td>Walkways and paths</td><td>Concrete, flagstone, pavers, stepping pads in gravel or turf</td><td><a href="masonry-concrete-austin-tx">Masonry and concrete</a></td></tr>
      <tr><td>Steps</td><td>Poured concrete, stone treads, steel risers</td><td><a href="masonry-concrete-austin-tx">Masonry and concrete</a></td></tr>
      <tr><td>Driveways</td><td>Poured concrete, pavers, concrete with stone bands</td><td><a href="masonry-concrete-austin-tx">Masonry and concrete</a></td></tr>
      <tr><td>Retaining and seat walls</td><td>Steel, limestone, block, concrete, boulders</td><td><a href="retaining-walls-austin-tx">Retaining walls</a></td></tr>
      <tr><td>Decks</td><td>Wood and composite</td><td><a href="custom-decks-austin-tx">Custom decks</a></td></tr>
      <tr><td>Edging and gravel courts</td><td>Quarter-inch steel, gravel</td><td><a href="steel-edging-austin-tx">Steel edging</a></td></tr>
      <tr><td>Fire and water</td><td>Steel, boulders, concrete</td><td><a href="fire-pits-austin-tx">Fire pits</a></td></tr>
      </tbody></table>
    <p>Fire, water, and planters are hardscape too. Red Agave is the only company in Austin that builds floating welded steel fire pits, and the only one that builds custom LED planters with custom light channels. We carve fire pits into boulders, and we build water features fed from a boulder. See our <a href="fire-pits-austin-tx">fire pits</a>, <a href="water-features-austin-tx">water features</a>, and <a href="custom-planters-austin-tx">custom steel planters</a>.</p>
    <p>New to the word? Our post on <a href="../blog/hardscaping-austin-tx">what hardscaping is</a> shows each material on a real build.</p>
    {fig([(P + "se-austin-fire-water/24-water-feature-fire-pits-overview-1200.webp", 1200, 900, "Concrete patio pads beside a round water feature with a curved steel fire pit, a second fire pit between boulders, and lit steel edging at dusk in Southeast Austin")],
         "Southeast Austin: concrete pads, a round water feature, two fire pits, and lit steel edging, all hardscape.")}""")

S += sec("Materials", "Which Hardscape Materials Do We Build With?", f"""    <p>Five: steel, concrete, stone, wood, and gravel. Most of our yards use three or four of them together.</p>

    <h3 {H3}>Steel</h3>
    <p>Steel holds an edge. We use quarter-inch steel, cut and welded on site, for retaining walls, terraces, steps, planters, and the edges of gravel and beds. Steel is thin, so a steel wall takes almost no room, and it can be cut to any line. See our <a href="retaining-walls-austin-tx">retaining walls</a> and <a href="custom-planters-austin-tx">custom steel planters</a>.</p>

    <h3 {H3}>Concrete</h3>
    <p>We form, pour, and finish our own concrete, in a 4,000 PSI mix with fiber mesh and rebar. Finishes are brushed, exposed aggregate, smooth trowel, and <a href="marbled-concrete-patios-austin-tx">marbled concrete</a>. We often pour a patio as separate pads, with gravel, river rock, or turf in the joints. Pads let rain soak in between them, and they read as lighter than one large slab.</p>

    <h3 {H3}>Stone and Pavers</h3>
    <p>Travertine stays cooler than concrete in direct sun. Flagstone gives an irregular, natural floor, in Oklahoma flagstone, Pennsylvania bluestone, or Texas limestone. Manufactured pavers come in consistent sizes for clean patterns, and a single paver can be lifted and replaced. Limestone block builds walls, and boulders sit where one level turns into the next. Our guide to <a href="../blog/travertine-vs-flagstone-vs-pavers-austin-tx">travertine, flagstone, and pavers</a> compares them.</p>

    <h3 {H3}>Wood</h3>
    <p>Wood is the right hardscape where the surface has to meet the house. A deck can be set at the exact height of a door, with no step. In East Austin we built a teak deck that runs flush from a screened porch to an outdoor kitchen. In Bee Cave, a wood deck with steel cable railing sits low on a Hill Country slope. See our <a href="custom-decks-austin-tx">custom decks</a>.</p>

    <h3 {H3}>Gravel</h3>
    <p>A gravel court is a floor that drains. Gravel needs an edge to stay where it is put, so our gravel courts are edged in steel. See our <a href="../blog/gravel-landscaping-ideas-austin-tx">gravel landscaping ideas</a>.</p>

    {fig([(P + "blazyk/IMG_3173-800.webp", 800, 1067, "Low steel retaining walls with dark gravel, boulders, and a raised steel planter at the Overlook at Lewis Mountain, Southwest Austin"),
          (P + "hopeland/IMG_9622-800.webp", 800, 1067, "Concrete pavers cut on the diagonal with river rock joints beside a long steel planter lit under its rim in Circle C, Austin"),
          (P + "bee-cave-deck/deck-stairs.webp", 768, 1024, "Wood deck with steel cable railing and a stair to an upper level, set on gravel under live oaks in Bee Cave")],
         "Steel walls at the Overlook at Lewis Mountain in Southwest Austin, diagonal concrete pavers with river rock joints in Circle C, and a wood deck in Bee Cave.")}""", alt=True)

S += sec("Patio Surfaces", "How Do the Patio Surfaces Compare?", f"""    <p>Each one suits a different house and a different use. We build all five, and we often mix them.</p>
    <table class="cost-table">
      <thead><tr><th>Surface</th><th>What It Is</th><th>Best For</th></tr></thead><tbody>
      <tr><td>Poured concrete</td><td>Formed and poured on site. Brushed, exposed aggregate, or smooth trowel finish</td><td>Modern houses, large patios, pads with gravel or turf joints</td></tr>
      <tr><td>Marbled concrete</td><td>Concrete finished with a marbled surface</td><td>A patio that is the feature of the yard</td></tr>
      <tr><td>Pavers</td><td>Manufactured units in consistent sizes, laid in a pattern</td><td>Clean geometry, driveways, surfaces you want to be able to repair</td></tr>
      <tr><td>Travertine</td><td>Natural stone pavers, tumbled or honed</td><td>Pool decks and patios in full sun</td></tr>
      <tr><td>Flagstone</td><td>Irregular natural stone, set in decomposed granite, in mortar, or on a slab</td><td>A natural, rustic floor</td></tr>
      </tbody></table>
    <p>Mixing defines zones in a large patio: a concrete field with stone bands, a paver border around flagstone, or a steel edge where one material meets the next. See our <a href="patios-austin-tx">patios</a> page and our <a href="../blog/patio-design-ideas-austin-tx">patio design ideas</a>.</p>""")

S += sec("Below the Surface", "What Goes Under a Patio or Walkway?", f"""    <p>A base. The part of a patio you never see decides whether it stays flat.</p>
    <ul>
      <li><strong>Excavation:</strong> we dig to the depth the surface and its base need.</li>
      <li><strong>Subgrade:</strong> the soil at the bottom is compacted.</li>
      <li><strong>Base:</strong> 6 to 8 inches of crushed limestone, compacted.</li>
      <li><strong>Grade:</strong> the base slopes so water moves away from the house.</li>
      <li><strong>Surface:</strong> concrete is poured over it, or stone and pavers are set on it.</li>
    </ul>
    <p>Austin clay swells when it is wet and shrinks when it is dry. A surface laid on bare clay moves with it, and that is how patios crack and heave. The compacted base is what keeps the surface still. Our <a href="../blog/concrete-vs-paver-patio-austin-tx">concrete vs paver patio guide</a> explains how each surface handles that movement.</p>
    {fig([("images/services/retaining-walls/limestone-block-retaining-wall-paver-patio-800.webp", 800, 600, "Tumbled paver patio in front of a limestone block retaining wall with a flat stone cap and a black steel planter")],
         "A tumbled paver patio that runs to a limestone block wall and a black steel planter.")}""")

S += sec("Soil and Slope", "How Does Hardscape Handle Austin Soil and Slopes?", f"""    <p>By being designed for the ground it sits on. Austin has two kinds of ground, and they behave differently.</p>
    <ul>
      <li><strong>East of I-35:</strong> expansive clay. It swells when it is wet and shrinks when it is dry, so bases are deep and well compacted, and water is kept moving away from slabs and walls.</li>
      <li><strong>West of MoPac:</strong> thin soil over fractured limestone. Rock is close to the surface, so levels are worked out around it, and footings bear on it.</li>
    </ul>
    <p>On a slope, hardscape makes level ground. Low walls cut a hill into terraces, steps join the levels, and each terrace slows the rain before it reaches the next. Our <a href="retaining-walls-austin-tx">retaining walls</a> page shows how we terraced a slope at the Overlook at Lewis Mountain in Southwest Austin with three low steel walls.</p>""", alt=True)

S += sec("Paths, Steps, Driveways", "How Do We Build Walkways, Steps, and Driveways?", f"""    <p>As part of the same plan as the patio, so every surface meets the next at the right height.</p>
    <ul>
      <li><strong>Walkways:</strong> concrete, flagstone, and paver walks connect one part of the yard to the next. Stepping pads set in gravel or turf do the same job with less paving.</li>
      <li><strong>Steps:</strong> we pour concrete steps, set stone treads, and weld steel risers. Step lights and steel handrails go in with them.</li>
      <li><strong>Driveways:</strong> poured concrete, pavers, or concrete with stone bands. A driveway is reinforced for vehicles, jointed for expansion, and graded to drain.</li>
    </ul>
    <p>In Cedar Creek we set large concrete pavers in artificial turf beside a pool, with steel-edged steps below. See our post on <a href="../blog/pavers-with-artificial-turf-austin-tx">pavers with artificial turf</a>.</p>
    {fig([(P + "flycatcher/IMG_8720-800.webp", 800, 1067, "Large poured concrete pavers with artificial turf joints beside a pool, with steel-edged steps below, in Cedar Creek, TX"),
          (P + "flycatcher/IMG_8801-800.webp", 800, 1067, "Steps with dark steel risers and treads of concrete and artificial turf leading up to a pool deck of large pavers in Cedar Creek, TX")],
         "Cedar Creek: concrete pavers in turf beside the pool, and steps with steel risers.")}""", alt=True)

S += sec("Order of Work", "What Gets Decided Before the Hardscape Goes In?", f"""    <p>The water, then the levels.</p>
    <p>Drainage is our first phase of construction. Water is designed before the patio, the planting, or the lighting, because everything built on top relies on it. See our <a href="drainage-austin-tx">drainage</a> page.</p>
    <p>The levels come next, and they are set on the plan. Hardscape fixes the height of every surface in the yard, so it goes in before the plants. Every Red Agave project starts with a free consultation, and the CAD plan is included. You can see our drawings on the <a href="../designs">design plans</a> page, and a plan next to the finished yard in our post on <a href="../blog/landscape-design-build-austin-tx">landscape design build</a>.</p>""", alt=True)

S += sec("How We Build", "How Is a Hardscape Project Built?", f"""    <p>In six steps, by one crew.</p>
    {step(1, "Consultation and Plan", "Free and on site. We walk the yard with you, measure it, and draw the hardscape on a CAD plan, which is included. See our <a href=\"landscape-design-austin-tx\">landscape design</a> page.")}
    {step(2, "Drainage and Grading", "We shape the ground and build the drainage first, so water has a place to go before anything is built on top.")}
    {step(3, "Walls and Footings", "Retaining walls, seat walls, and the footings for decks and structures go in while the ground is open.")}
    {step(4, "Base", "We compact the subgrade and lay 6 to 8 inches of crushed limestone under every patio and walk.")}
    {step(5, "Surfaces", "Concrete is formed, poured, and finished. Stone and pavers are set. Decks are framed and laid.")}
    {step(6, "Edges and Finish", "Steel edging is cut and welded on site, and gravel goes in. Planting and lighting are fitted to the hardscape last. See our <a href=\"landscape-lighting-austin-tx\">landscape lighting</a> page.")}""")

S += sec("After Dark", "How Is Hardscape Lit?", f"""    <p>Along its edges. Light is planned with the hardscape, so the channels and the wiring go in while the ground is open.</p>
    <ul>
      <li><strong>Steel edges:</strong> LED strips trace the steel edge of a gravel court or a terrace.</li>
      <li><strong>Deck transitions:</strong> a line of light marks each change of level.</li>
      <li><strong>Joints:</strong> in Pearson Ranch in Northwest Austin, the gravel joints between the concrete pads are lit.</li>
      <li><strong>Planters:</strong> a steel planter can be lit under its rim, so it glows along its length.</li>
      <li><strong>Steps:</strong> step lights go in with the steps.</li>
    </ul>
    <p>See our <a href="landscape-lighting-austin-tx">landscape lighting</a> page and our <a href="../blog/landscape-lighting-guide-austin-tx">landscape lighting guide</a>.</p>
    {fig([(P + "blazyk/IMG_8699-800.webp", 800, 1067, "LED strip lighting tracing the steel edges of a gravel court and deck at night at the Overlook at Lewis Mountain, Southwest Austin"),
          (P + "blazyk/IMG_8703-800.webp", 800, 1067, "Gravel court with boulders, ferns, and a fire pit, lit by a strip along its steel edge at night at the Overlook at Lewis Mountain, Southwest Austin")],
         "Overlook at Lewis Mountain, Southwest Austin, at night: light along the steel edges of the gravel court and the deck.")}""", alt=True)

S += sec("Our Work", "Where Have We Built Hardscape in Austin?", f"""    <p>Across the Austin area. Six of our builds:</p>
    <ul>
      <li><strong>Overlook at Lewis Mountain, Southwest Austin, a bare slope:</strong> three steel terraces and two deck levels, with quarter-inch steel on every edge. See <a href="../projects/blazyk">the case study</a>.</li>
      <li><strong>Southeast Austin:</strong> concrete pads with dark gravel joints, a round water feature, and two fire pits. See <a href="../blog/water-feature-fire-pits-southeast-austin-tx">the build</a>.</li>
      <li><strong>Cedar Creek:</strong> large concrete pavers set in turf beside a pool, with steel-edged steps. See <a href="../projects/flycatcher">the case study</a>.</li>
      <li><strong><a href="../locations/circle-c-tx">Circle C</a>, a deck and patio:</strong> concrete pavers cut on the diagonal with river rock joints, beside a long steel planter lit under its rim. See <a href="../projects/hopeland">the case study</a>.</li>
      <li><strong>Pearson Ranch, Northwest Austin:</strong> poured concrete patio pads with lit, steel-edged gravel joints and a boulder set in the slab. See <a href="../projects/axehandle">the case study</a>.</li>
      <li><strong><a href="../locations/bee-cave-tx">Bee Cave</a>:</strong> a wood deck with steel cable railing beside steel-walled gravel terraces.</li>
    </ul>
    {fig([(P + "axehandle/IMG_8574-800.webp", 800, 600, "Poured concrete patio pads with lit steel-edged gravel joints, a boulder set in the slab, a steel fire pit, ferns and artificial turf, Pearson Ranch, Northwest Austin TX")],
         "Pearson Ranch, Northwest Austin: concrete pads with lit, steel-edged gravel joints and a boulder set in the slab.")}
    <p>More of our built work is on the <a href="../featured">Signature Projects</a> page. Pair the hardscape with an <a href="outdoor-kitchens-austin-tx">outdoor kitchen</a>, a <a href="pergolas-austin-tx">pergola</a>, or a <a href="pools-austin-tx">pool</a>, and see how it comes together on our <a href="outdoor-living-austin-tx">outdoor living</a> page.</p>""")

build(ROOT, dict(
    slug=SLUG, crumb="Hardscaping", h1="Hardscaping",
    title="Hardscaping Austin TX | Hardscape Design & Build",
    desc="Red Agave designs and builds hardscaping in Austin, TX: patios, walkways, steps, driveways, walls, decks, and steel edging. Built by our own crew.",
    og_img="https://www.redagaveatx.com/images/projects/se-austin-fire-water/24-water-feature-fire-pits-overview-share.webp",
    bg_l="../images/projects/se-austin-fire-water/24-water-feature-fire-pits-overview-1200.webp",
    bg_s="../images/projects/se-austin-fire-water/24-water-feature-fire-pits-overview-800.webp",
    answer_h2="Who Does Hardscaping in Austin, TX?",
    answer="<strong>Red Agave Landscape</strong> designs and builds hardscaping in Austin, TX: patios, walkways, steps, driveways, retaining walls, decks, steel edging, fire pits, and water features. We build in five materials, which are steel, concrete, stone, wood, and gravel. Drainage goes in first, every patio sits on 6 to 8 inches of compacted crushed limestone, and our concrete is a 4,000 PSI mix with fiber mesh and rebar. We have built in Austin since 2009, and every project is built by our own crew. Each one starts with a free consultation, and the CAD plan is included. Call or text 512-695-7566.",
    sections=S, faqs=FAQS, cta="Plan Your Hardscape",
    service_name="Hardscape Design and Construction", service_type="Hardscaping",
    service_desc="Hardscaping designed and built in Austin, TX in steel, concrete, stone, wood, and gravel: patios, walkways, steps, driveways, retaining walls, decks, steel edging, fire pits, and water features. Built by Red Agave's own crew, with a free consultation and the CAD plan included."))

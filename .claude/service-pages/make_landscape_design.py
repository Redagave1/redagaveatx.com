"""Rebuilds services/landscape-design-austin-tx.html (2026-11-25): six of Jensen's own plans beside the finished yards.
Run from the site root:  python3 .claude/service-pages/make_landscape_design.py .
The page already has its hub card, sitemap line, redirect and llms.txt line, so there is no --register step."""
import sys, os, re, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svc_lib import build, step, sec
from svc_extra import check, AREAS
from PIL import Image

ROOT = sys.argv[1]
SLUG = "landscape-design-austin-tx"
D = "images/designs/"
P = "images/projects/"


def im(path, alt):
    w, h = Image.open(os.path.join(ROOT, path)).size
    return f'<img src="../{path}" width="{w}" height="{h}" alt="{html.escape(alt, quote=True)}" loading="lazy" decoding="async">'


def frame(path, alt, label, full=None, photo=False):
    img = im(path, alt)
    if full:
        img = f'<a href="../{full}" target="_blank" rel="noopener" aria-label="Open the full drawing">{img}</a>'
    return f'<figure class="{"pb-ph" if photo else "pb-dr"}">{img}<figcaption>{label}</figcaption></figure>'


def pair(n, title, where, left, right, body, wide=False):
    return (f'<div class="pb"><div class="pb-top"><span class="pb-n">{n}</span><h3 class="pb-t">{title}</h3><span class="pb-w">{where}</span></div>'
            f'<div class="pb-pair{" pb-wide" if wide else ""}">{left}{right}</div>\n{body}</div>')


CSS = ("<style>.pb{margin:52px 0 0;padding-top:40px;border-top:1px solid rgba(201,168,76,0.14)}"
       ".pb-top{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 18px;margin-bottom:18px}"
       ".pb-n{font-family:'Bebas Neue',Impact,sans-serif;font-size:15px;letter-spacing:3px;color:var(--gold)}"
       ".pb-t{font-family:'Bebas Neue',Impact,sans-serif;font-size:30px;font-weight:400;letter-spacing:1.5px;line-height:1.1;color:var(--cream);margin:0}"
       ".pb-w{font-size:10px;font-weight:600;letter-spacing:2.5px;text-transform:uppercase;color:var(--cream60)}"
       ".pb-pair{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:22px}"
       ".pb-pair figure{margin:0;position:relative;overflow:hidden}.pb-dr{background:#fff}.pb-ph{background:var(--dark)}"
       ".pb-pair a{display:block;border:0}.pb-pair img{display:block;width:100%;height:auto;aspect-ratio:4/5;object-fit:contain}"
       ".pb-ph img{object-fit:cover}.pb-wide img{aspect-ratio:3/2}"
       ".pb-pair figcaption{position:absolute;left:0;top:0;background:rgba(8,11,6,0.88);color:var(--gold);font-size:10px;font-weight:600;letter-spacing:2.5px;text-transform:uppercase;line-height:1;padding:9px 13px}"
       ".pb p{margin-bottom:14px}.content-body .pb:first-of-type{margin-top:36px}"
       ".content-body:has(.pb){max-width:1080px}.content-body:has(.pb)>p,.pb>p{max-width:820px}"
       ".upd{font-size:12px;letter-spacing:.5px;color:var(--cream60);margin:-6px 0 0}"
       "@media(max-width:640px){.pb-pair{grid-template-columns:1fr}.pb-dr img{aspect-ratio:auto}.pb-t{font-size:26px}}</style>")

FAQS = [
    ("Who designs landscapes in Austin, TX?",
     "Red Agave Landscape is a landscape design and build firm in Austin, founded in 2009. The owner, Jensen Mehrens, draws every plan after a free on-site consultation, and our own crew builds it."),
    ("How much does landscape design cost in Austin?",
     "Every project is quoted after a free on-site consultation. The CAD plan is included with your project, and the price follows the scope, the materials, and the site. Our landscape design cost guide lists the ranges."),
    ("Is the landscape design consultation free?",
     "Yes. We meet you at your property, walk the space together, and take measurements with no charge and no obligation. Consultations run Tuesday through Thursday, 10am to 1pm, or by special arrangement."),
    ("What is included in a landscape design plan?",
     "A fully dimensioned 2D CAD plan, a plant palette, material selections, a lighting layout, grading and drainage, and an itemized quote. Where a plan is hard to picture, we sketch the design over a photo of your house, and complex projects get 3D renderings."),
    ("How long does landscape design take?",
     "Design development takes 2 to 4 weeks, depending on the scope of the project. Construction runs from about 4 weeks for a focused backyard to 8 to 16 weeks for a full property."),
    ("Can I see real plans you have drawn?",
     "Yes. Six of our plans are on this page beside the finished yards, and thirteen of our drawings are on our design plans page. Every drawing is our own work."),
    ("Does the finished yard match the plan?",
     "Each plan on this page is shown beside the yard our crew built from it. Some details were refined in the build. In Southeast Austin the front fire pit became a curve of steel that follows the pool wall, and in Circle C the fire was set in a boulder on a low deck platform."),
    ("Can I see the design on my own house before it is built?",
     "Yes. Where a plan is hard to picture, we draw the design over a photo of your house. For complex projects, 3D renderings show materials and elevations before you sign off."),
    ("Who builds the design?",
     "Our own crew. The team that draws the plan builds it, so nothing gets lost between the plan and the build."),
    ("Can a landscape design be built in phases?",
     "Yes. We draw the whole property at once, even if you build it in phases. Drainage, electrical, and gas are planned first, so later phases never tear up finished work."),
    ("Can you design for HOA approval?",
     "Yes. Every project starts with a custom CAD design the committee can review."),
    ("Do you design front yards?",
     "Yes. In Southeast Austin we sketched a floating triangle steel planter over a photo of the front of the house, with raised steel beds stepping toward the front door, and then built it."),
    ("Do you design pools?",
     "Yes. Four of the plans on our design plans page include a pool. In Cedar Creek we drew an L-shaped pool with concrete pavers set in turf and two fire pits, and the finished yard is on this page."),
    ("Do you design for Austin's clay and limestone soils?",
     "Yes. Clay sites get a deeper compacted base and grading that moves water away from the house. Limestone and caliche sites get test holes before planting, raised beds where roots need depth, and plants that take alkaline soil."),
    ("Is a landscape designer the same as a landscape architect?",
     "No. In Texas, only a person registered with the state uses the title landscape architect (Occupations Code Chapter 1052). The same law lets landscape designers and landscape contractors draw plans, and lets anyone draw plans for a single-family residence, without that registration. Red Agave is a landscape design and build firm."),
]

EXT = 'target="_blank" rel="noopener"'

S = ""
S += sec("Plan to Built", "What Does a Red Agave Design Look Like Once It Is Built?", f"""    <p>The best test of a landscape design is the yard that was built from it. Here are six of our own drawings beside the finished work. The owner drew each one, and our own crew built it. Select a drawing to open it full size.</p>
    {pair("Plan 01", "Steel Terraces on a Slope", "Lewis Mountain, Southwest Austin",
          frame(D + "circle-c-steel-terraces-plan-900.webp", "Landscape design plan for a sloped backyard at the Overlook at Lewis Mountain in Southwest Austin with two deck levels, three gravel terraces, boulders, a fire pit, and steel edging marked by height", "The plan", D + "circle-c-steel-terraces-plan.webp"),
          frame(P + "blazyk/IMG_3193-800.webp", "Finished backyard at the Overlook at Lewis Mountain in Southwest Austin with steel terraces of dark gravel, boulders, and grasses stepping up to a gravel court with a fire pit", "Built", photo=True),
          '''<p><strong>On the plan:</strong> two deck levels off the house and three gravel terraces stepping down the slope. The drawing gives the square footage of every surface and marks each steel edge by height: orange dashes for steel 4 to 8 inches tall, blue for 1 to 2 feet.</p>
    <p><strong>Built:</strong> stepped terraces in quarter-inch steel, filled with dark gravel, boulders, and native grasses, with the fire pit on the gravel court above. See <a href="../projects/blazyk">the finished project</a> and <a href="../blog/landscape-design-build-austin-tx">the yard followed from plan to build</a>.</p>''')}
    {pair("Plan 02", "Water Feature and Two Fire Pits", "Southeast Austin",
          frame(D + "water-feature-fire-pits-plan-900.webp", "Landscape design plan drawn over an aerial view of a house, showing a round water feature fed by a channel from a boulder, two fire pits set against boulders, concrete pads, and a dark gravel court in Southeast Austin", "The plan", D + "water-feature-fire-pits-plan.webp"),
          frame(P + "se-austin-fire-water/21-water-feature-curved-fire-pit-dusk-800.webp", "Finished round water feature with a curved steel fire pit burning in front and a steel planter behind, at dusk in Southeast Austin", "Built", photo=True),
          '''<p><strong>On the plan:</strong> concrete pads along the back of the house, a round water feature fed by a channel from a boulder, two fire pits set against boulders, and a dark gravel court.</p>
    <p><strong>Built:</strong> a round raised pool with a concrete shell and a plaster interior finished black, fed by a steel channel from a drilled boulder. The front fire pit became a curve of steel that follows the pool wall. See <a href="../projects/southeast-austin-water-feature">the finished project</a> and <a href="../blog/custom-fire-pits-austin-tx">the plan next to the finished fires</a>.</p>''')}
    {pair("Sketch 03", "Outdoor Kitchen and Steel Screen", "East Austin",
          frame(D + "east-austin-sketch-outdoor-kitchen-800.webp", "Hand-drawn concept sketch of an outdoor kitchen with a built-in grill in front of a perforated steel screen for an East Austin backyard", "The sketch", D + "east-austin-outdoor-living-sketches.webp"),
          frame(D + "east-austin-built-outdoor-kitchen-800.webp", "Finished outdoor kitchen with a stainless grill in front of a perforated steel screen lit from behind at dusk in East Austin", "Built", photo=True),
          '''<p><strong>On the sketch:</strong> an outdoor kitchen in front of a perforated steel screen. It is one of four concept sketches of the same backyard, with a screened dining porch beside the pool and a lounge under a shade sail.</p>
    <p><strong>Built:</strong> the kitchen with a stainless grill, and the perforated steel screen lit from behind. See <a href="../projects/ulit">each sketch next to the finished view</a>.</p>''', wide=True)}
    {pair("Plan 04", "Decks, Diagonal Pavers, and Fire", "Circle C, Austin",
          frame(D + "circle-c-deck-pavers-fire-plan-900.webp", "Landscape design plan for a Circle C backyard in Austin with a main deck, two deck steps, a square deck with a fire pit, concrete pavers cut on the diagonal with dimensions, planters, and boulders", "The plan", D + "circle-c-deck-pavers-fire-plan.webp"),
          frame(P + "hopeland/IMG_9687-800.webp", "Finished Circle C backyard in Austin at dusk: a composite deck stepping down to a platform with a boulder fire pit, in front of a slatted cabana with woven pendant lights", "Built", photo=True),
          '''<p><strong>On the plan:</strong> a main deck off the house, two deck steps, and a square deck with a fire pit at its center. Beside them the plan lays out concrete pavers cut on the diagonal, each field dimensioned, with planters and boulders.</p>
    <p><strong>Built:</strong> a composite deck steps down to a low platform, and the fire burns in a boulder in front of the cabana. See <a href="../projects/hopeland">the plan and the finished yard</a>.</p>''')}
    {pair("Plan 05", "Pool, Pavers in Turf, and Two Fires", "Cedar Creek, TX",
          frame(D + "pool-pavers-turf-fire-pits-plan-900.webp", "Landscape design plan for a Cedar Creek backyard with an L-shaped pool, concrete pavers set in turf with dimensions, a square fire pit at the pool drawn as a tapered steel bowl, a linear fire pit in a dark court, three planters, and a BBQ area", "The plan", D + "pool-pavers-turf-fire-pits-plan.webp"),
          frame(P + "flycatcher/IMG_8836-800.webp", "Finished Cedar Creek backyard with large concrete pavers set in turf, steel-edged steps, and a pool with a fire pit burning beyond", "Built", photo=True),
          '''<p><strong>On the plan:</strong> an L-shaped pool with concrete pavers set in turf along two sides, every run dimensioned. A square fire pit sits at the corner of the pool, drawn in elevation beside it, and a linear fire pit sits in a dark court behind.</p>
    <p><strong>Built:</strong> the pool fire pit is a floating welded steel pit filled with aqua fire glass, and the long pit burns over amber glass in dark gravel. See <a href="../projects/flycatcher">the finished project</a> and our post on <a href="../blog/pavers-with-artificial-turf-austin-tx">pavers set in turf</a>.</p>''')}
    {pair("Sketch 06", "Floating Triangle Planter", "Southeast Austin",
          frame(D + "floating-triangle-planter-sketch-900.webp", "Design sketch of a black triangle steel planter holding a blue agave on raised black steel beds that step toward a front door, with lawn in front, drawn over the front of a house in Southeast Austin", "The sketch", D + "floating-triangle-planter-sketch.webp"),
          frame(P + "southeast-austin-triangle-planter/03-floating-triangle-planter-agave-lit-800.webp", "Finished black triangle steel planter with a variegated century agave floating above a raised steel bed of basalt gravel, lit from its rim, in a front yard in Southeast Austin", "Built", photo=True),
          '''<p><strong>On the sketch:</strong> a black triangle planter with an agave in it, set on raised steel beds that step toward the front door, drawn over the front of the house.</p>
    <p><strong>Built:</strong> welded steel shaped like an upside-down pyramid, carried on one post above terraced steel beds of basalt gravel. The planter and the beds each have a light rim. See <a href="../projects/chrysler-bend">the project page</a> and <a href="../blog/floating-triangle-steel-planter-austin-tx">the sketch, the build, and the finished planter</a>.</p>''')}
    <p style="margin-top:40px">Thirteen of our drawings are on the <a href="../designs">design plans</a> page, and more finished work is on our <a href="../featured">Signature Projects</a> page.</p>""")

S += sec("Owner-Designed", "How Does Red Agave Design a Landscape?", """    <p>At your property, with the build in mind. A landscape design is only as good as what gets built from it. We draw every plan knowing how our crew will build it: how the steel gets cut and welded, how deep the base goes, and where the water will run.</p>
    <p>Design starts at your property, not in an office. We walk the yard with you, study the grade, trace the shade lines, and photograph the sightlines from inside the house. Then we look at what the site demands: soil, drainage, existing trees, views, and privacy.</p>
    <p>When the plan is approved, the same team builds it. See how that works on our <a href="design-build-austin-tx">design and build</a> page.</p>""")

S += sec("On the Plan", "What Is in a Red Agave Landscape Design?", f"""    <p>Six parts. Together they decide the yard on paper, before anything is ordered.</p>
    <table class="cost-table">
      <thead><tr><th>Part of the Design</th><th>What It Shows</th></tr></thead><tbody>
      <tr><td>Dimensioned 2D CAD plan</td><td>Every bed, slab, wall, and path drawn to scale, with lengths and square footage on the drawing</td></tr>
      <tr><td>Plant palette</td><td>Plants chosen for your sun, your soil, and Austin's watering limits, sourced from specialty Texas native nurseries</td></tr>
      <tr><td>Materials and samples</td><td>Steel, concrete finishes, stone, and decking, selected together. We bring material and color samples, and you approve every selection before we order.</td></tr>
      <tr><td>Lighting layout</td><td>24V FCOB and COB fixture locations and zones, planned together with the hardscape</td></tr>
      <tr><td>Grading and drainage</td><td>Where the water goes after a storm, worked out on the plan before anything is built</td></tr>
      <tr><td>Sketches and 3D renderings</td><td>Sketches over a photo of your house, and 3D renderings for complex projects</td></tr>
      </tbody></table>
    <div class="pb-pair" style="margin-top:32px">{frame(D + "fire-pit-court-plan-dimensions-900.webp", "Dimensioned landscape design plan of a fire pit court with four pads around the fire, stepping pads across a lawn, and planted beds on two sides", "Plan 09", D + "fire-pit-court-plan-dimensions.webp")}{frame(D + "pool-deck-fire-court-plan-900.webp", "Landscape design plan with a large pool and a small pool wrapped by a wood deck, a herringbone paver court with a linear fire pit, and agaves in square planters", "Plan 07", D + "pool-deck-fire-court-plan.webp")}</div>
    <p>On Plan 09 every run is dimensioned, from 3 feet 3 inches for a single pad to 32 feet 3 inches across the yard. Plan 07 sets two pools, a deck, and a herringbone court with a linear fire pit, with side views of the fire feature and a tiered planter at the bottom of the sheet.</p>
    <p>Revisions are included. We revise until the design fits your property and the way you live outside, and you approve every detail in writing before construction starts.</p>""")

S += sec("Our Process", "How Does the Design Process Work?", f"""    <p>In six steps, from the first visit to the build.</p>
    {step(1, "Consultation", "Free and on site. We meet you at your property Tuesday through Thursday, 10am to 1pm, or by special arrangement.")}
    {step(2, "Site Study", "We take measurements and assess sun, shade, drainage, soil, existing trees, views, and privacy. Where rock or caliche matters, we dig test holes.")}
    {step(3, "CAD Plan", "The owner draws a fully dimensioned 2D CAD plan. The CAD plan is included with your project.")}
    {step(4, "Revisions", "We revise until the plan fits the site and how you use it.")}
    {step(5, "Approval", "You approve materials, plants, and every detail in writing, with an itemized quote.")}
    {step(6, "Build", "Our own crew builds it. You get daily progress photos and a weekly walkthrough with your project lead.")}
    <table class="cost-table" style="margin-top:36px">
      <thead><tr><th>Stage</th><th>How Long It Takes</th></tr></thead><tbody>
      <tr><td>Design development</td><td>2 to 4 weeks, depending on scope</td></tr>
      <tr><td>Build, focused backyard</td><td>About 4 weeks</td></tr>
      <tr><td>Build, full property</td><td>8 to 16 weeks</td></tr>
      </tbody></table>
    <p>Before the first visit, read our <a href="../blog/landscape-consultation-checklist-austin-tx">consultation checklist</a>.</p>""")

S += sec("See It First", "Can You See the Design on Your House Before It Is Built?", f"""    <p>Yes. Where a plan is hard to picture, we draw the design over a photo of your house. For complex projects, 3D renderings show materials and elevations before you sign off.</p>
    <div class="pb-pair pb-wide" style="margin-top:28px">{frame(D + "cantilever-planter-steps-sketch-900.webp", "Design sketch drawn over a photo of the back of a house, showing a black steel cantilever planter with lights under it, black pavers, and steel steps", "Sketch over a photo", D + "cantilever-planter-steps-sketch.webp")}{frame(D + "east-austin-sketch-screened-porch-800.webp", "Hand-drawn concept sketch of a screened dining porch beside a pool, with an outdoor kitchen behind it, for an East Austin backyard", "Concept sketch", D + "east-austin-outdoor-living-sketches.webp")}</div>
    <ul>
      <li><strong>Sketch over a photo:</strong> a cantilever planter with COB lights under it, black pavers extending the patio, and steps in black steel, drawn on a photo of the back of the house</li>
      <li><strong>Concept sketches:</strong> four views of one East Austin backyard, drawn before the build: the outdoor kitchen, the screened dining porch beside the pool, and the lounge under a shade sail</li>
      <li><strong>Elevations on the plan:</strong> the Cedar Creek plan draws the pool fire pit from the side, next to its place on the plan</li>
    </ul>
    <p>Read <a href="../blog/landscape-designer-austin-tx">how our owner draws a yard</a>, and compare <a href="../blog/backyard-design-austin-tx">four backyard plans</a>.</p>""")

S += sec("What We Draw", "What Can Red Agave Design?", """    <p>The whole yard, on one plan. These are the parts that show up on our drawings, and the page for each.</p>
    <table class="cost-table">
      <thead><tr><th>Part of the Yard</th><th>On Our Drawings</th><th>Read More</th></tr></thead><tbody>
      <tr><td>Pools</td><td>Sketch 03 and Plans 05, 07, 08, and 12</td><td><a href="pools-austin-tx">Pools</a>, <a href="container-plunge-pools-austin-tx">container plunge pools</a></td></tr>
      <tr><td>Decks</td><td>Plans 01, 04, 07, 08, 11, and 12</td><td><a href="custom-decks-austin-tx">Custom decks</a></td></tr>
      <tr><td>Fire pits</td><td>Plans 01, 02, 04, 05, 07, 08, and 09</td><td><a href="fire-pits-austin-tx">Fire pits</a></td></tr>
      <tr><td>Water features</td><td>Plans 02, 10, and 11</td><td><a href="water-features-austin-tx">Water features</a></td></tr>
      <tr><td>Pavers and concrete pads</td><td>Plans 02, 04, 05, 08, 09, and 11</td><td><a href="paver-patios-austin-tx">Paver patios</a>, <a href="patios-austin-tx">patios</a>, <a href="marbled-concrete-patios-austin-tx">marbled concrete</a></td></tr>
      <tr><td>Steel planters, edging, and terraces</td><td>Plan 01 and Sketches 06 and 13</td><td><a href="custom-planters-austin-tx">Custom planters</a>, <a href="steel-edging-austin-tx">steel edging</a>, <a href="steel-retaining-walls-austin-tx">steel retaining walls</a></td></tr>
      <tr><td>Outdoor kitchens and porches</td><td>Sketch 03</td><td><a href="outdoor-kitchens-austin-tx">Outdoor kitchens</a>, <a href="patio-covers-pavilions-austin-tx">patio covers and pavilions</a>, <a href="pergolas-austin-tx">pergolas</a></td></tr>
      <tr><td>Planting</td><td>The plant palette in every design</td><td><a href="xeriscape-austin-tx">Xeriscape</a>, <a href="../blog/native-plants-austin-landscaping">native plants guide</a></td></tr>
      <tr><td>Lighting</td><td>The lighting layout in every design</td><td><a href="landscape-lighting-austin-tx">Landscape lighting</a></td></tr>
      <tr><td>Grading and drainage</td><td>Worked out on every design</td><td><a href="drainage-austin-tx">Drainage</a></td></tr>
      </tbody></table>
    <p>The plan and sketch numbers match our <a href="../designs">design plans</a> page. The three pool plans are compared in <a href="../blog/pool-design-austin-tx">pool design in Austin</a>.</p>""")

S += sec("Designed for Austin", "What Do Austin Sites Change in a Design?", f"""    <p>The soil, the trees, the water rules, and the heat. A design that works in Dallas or Phoenix can fail here. West Austin and the Hill Country sit on thin soil over limestone and caliche. East of the Balcones Escarpment, the ground turns to Blackland Prairie clay that swells when wet and shrinks when dry. Every plan starts from those facts.</p>
    <table class="cost-table">
      <thead><tr><th>Site Condition</th><th>What It Changes in the Design</th></tr></thead><tbody>
      <tr><td>Expansive clay</td><td>A deeper compacted base under every slab, grading that moves water away from the house, and planting beds built up with amended soil</td></tr>
      <tr><td>Thin soil over limestone or caliche</td><td>Test holes before the planting plan, raised steel beds where roots need depth, and plants that take alkaline soil</td></tr>
      <tr><td>Protected trees</td><td>The layout works around them. In Austin a tree 19 inches or more in diameter, measured 4.5 feet above the ground, is protected, and removing it takes a city permit (<a href="https://www.austintexas.gov/page/tree-reviews-and-permitting" {EXT}>City Arborist</a>).</td></tr>
      <tr><td>Watering limits</td><td>Drought-tolerant plants on drip irrigation, with lawn only where it gets used. Under Austin Water's Conservation Stage rules, automatic irrigation systems run one day a week, and hose-end sprinklers and drip irrigation run two (<a href="https://www.austintexas.gov/water/find-your-watering-day" {EXT}>Austin Water</a>).</td></tr>
      <tr><td>Deer</td><td>A deer-resistant planting palette in west Austin and the Hill Country</td></tr>
      <tr><td>Summer heat</td><td>Plants that hold up in a 100&deg;F summer, and surfaces like travertine that stay cooler underfoot</td></tr>
      </tbody></table>
    <p>Each city adds its own rules. See what changes in <a href="../locations/westlake-hills-tx">Westlake Hills</a>, <a href="../locations/lakeway-tx">Lakeway</a>, <a href="../locations/cedar-park-tx">Cedar Park</a>, and <a href="../locations/dripping-springs-tx">Dripping Springs</a>.</p>""")

S += sec("Who Draws It", "Landscape Designer, Design-Build Firm, or Landscape Architect?", f"""    <p>They are three different things, and Texas law draws the line. Red Agave is a landscape design and build firm. We are not landscape architects.</p>
    <table class="cost-table">
      <thead><tr><th>Title</th><th>What It Means in Texas</th></tr></thead><tbody>
      <tr><td>Landscape architect</td><td>A person registered with the state. Only a registered person uses this title.</td></tr>
      <tr><td>Landscape designer</td><td>Draws landscape plans. The law lets landscape designers draw plans without that registration.</td></tr>
      <tr><td>Landscape contractor</td><td>Builds the landscape. The law lets landscape contractors draw plans too.</td></tr>
      <tr><td>Design-build firm</td><td>One company draws the plan and builds it. Red Agave works this way: the owner draws, and our own crew builds.</td></tr>
      </tbody></table>
    <p>The law is <a href="https://statutes.capitol.texas.gov/Docs/OC/htm/OC.1052.htm" {EXT}>Texas Occupations Code, Chapter 1052</a>. Section 1052.003 also lets anyone draw plans for a single-family residence without that registration.</p>
    <p>What matters more than the title is whether the person drawing knows how the yard gets built. Nothing on our plans is a guess about construction, because the people who draw them build them. For help comparing companies, read <a href="../blog/how-to-choose-landscaper-austin-tx">how to choose a landscaper</a>.</p>""")

S += sec("Phases + Approvals", "Can a Design Be Built in Phases?", """    <p>Yes. We draw the whole property at once, even if you build it in phases. Infrastructure like drainage, electrical, and gas is planned first, so later phases never tear up finished work.</p>
    <ul>
      <li><strong>One plan:</strong> the front yard, the back yard, and the side yards are drawn together, so each phase fits the next</li>
      <li><strong>Infrastructure first:</strong> drainage, electrical, and gas lines go in before the surfaces above them</li>
      <li><strong>HOA review:</strong> every project starts with a custom CAD design the committee can review. See our approval guides for <a href="../blog/circle-c-hoa-landscape-approval-austin-tx">Circle C</a>, <a href="../blog/steiner-ranch-hoa-landscape-approval-austin-tx">Steiner Ranch</a>, and <a href="../blog/mueller-hoa-landscape-approval-austin-tx">Mueller</a></li>
    </ul>
    <p>For what drives the price of a design and a build, see our <a href="../blog/landscape-design-cost-austin-tx">landscape design cost guide</a>.</p>""")

S += sec("Service Area", "Where Does Red Agave Design Landscapes?", f"""    {AREAS}
    <p>Red Agave Landscape has built in Austin since 2009, with more than 750 projects, a 4.8 star rating on Google, and the Best of Houzz Service award in 2019 and 2020. Every project starts with a free consultation, and the CAD plan is included. Call or text (512) 695-7566.</p>
    <p>More on design:</p>
    <ul>
      <li><a href="../blog/landscape-design-services-austin-tx">Landscape design services</a>: one plan next to its finished yard</li>
      <li><a href="../blog/landscape-designer-austin-tx">Meet the designer</a></li>
      <li><a href="../blog/backyard-design-austin-tx">Four backyard plans compared</a></li>
      <li><a href="luxury-landscaping-austin-tx">Luxury landscaping</a> and <a href="design-build-austin-tx">design and build</a></li>
    </ul>""")

ANSWER = ("<strong>Red Agave Landscape</strong> is a landscape design and build firm in Austin, TX, founded in 2009. The owner, Jensen Mehrens, draws every plan after a free on-site consultation, and our own crew builds it. "
          "Six of our plans are shown on this page beside the finished yards. A design includes a fully dimensioned 2D CAD plan, a plant palette, material selections, a lighting layout, and a grading and drainage plan. "
          "The consultation is free, and the CAD plan is included with your project. Call or text 512-695-7566."
          '</p><p class="upd">Plans drawn by Jensen Mehrens, owner. Page updated November 25, 2026.')

check(S, ANSWER, " ".join(q + " " + a for q, a in FAQS))
build(ROOT, dict(
    slug=SLUG, crumb="Landscape Design", h1="Landscape Design",
    title="Landscape Design Austin TX | Red Agave Landscape",
    desc="Landscape design in Austin, TX: six owner-drawn plans shown beside the finished yards. Free on-site consultation, CAD plan included, built by our own crew.",
    og_img="https://www.redagaveatx.com/images/designs/landscape-design-plans-share.webp",
    bg_l="../images/projects/hopeland/IMG_9687.webp", bg_s="../images/projects/hopeland/IMG_9687-800.webp",
    answer_h2="Who Designs Landscapes in Austin, TX?", answer=ANSWER,
    sections=S, faqs=FAQS, cta="Start With a Free Design Consultation",
    service_name="Landscape Design", service_type="Landscape design",
    areas=["Austin", "West Lake Hills", "Rollingwood", "Lakeway", "Bee Cave", "Cedar Park", "Round Rock", "Georgetown", "Pflugerville", "Dripping Springs", "Leander", "Buda", "Kyle"],
    service_desc="Owner-designed residential landscape design in Austin, TX: a free on-site consultation, a site study of sun, drainage, soil, and existing trees, a fully dimensioned 2D CAD plan, a plant palette, material selections, a lighting layout, and a grading and drainage plan, built by Red Agave's own crew. Six of the firm's plans are shown beside the finished yards."))

p = f"{ROOT}/services/{SLUG}.html"
s = open(p, encoding="utf-8").read()
assert CSS not in s
s = s.replace("</head>", CSS + "\n</head>", 1)
open(p, "w", encoding="utf-8").write(s)
print("pair css added; drawings:", s.count('class="pb-dr"'), "photos:", s.count('class="pb-ph"'))

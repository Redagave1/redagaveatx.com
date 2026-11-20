"""Driveways service page.

PHOTO NOTE (2026-11-20): the repo has no photo of a driveway Red Agave built. The photos on this page show our
poured concrete, our pavers, and our steel-edged beds beside existing driveways, and each caption says exactly
that. No caption or alt text calls any of them a driveway we built. When Jensen sends a photo of a finished
driveway, put it in images/projects/svc-driveways-austin-tx/ and make it the first figure and the hero.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svc_lib import build, register, fig, step, sec, H3
from svc_extra import check, AREAS, STANDING

ROOT = sys.argv[1]
SLUG = "driveways-austin-tx"
P = "images/projects/"
D = P + "svc-driveways-austin-tx/"

FAQS = [
    ("Who builds driveways in Austin, TX?",
     "Red Agave Landscape builds driveways in Austin in poured concrete, in pavers, and in concrete with stone bands. Each one is reinforced for vehicles, jointed for expansion, and graded to drain. Our own crew forms, pours, and finishes the concrete, and every project starts with a free consultation, with the CAD plan included."),
    ("What kinds of driveways do you build?",
     "Three: poured concrete driveways, paver driveways, and concrete driveways with stone bands."),
    ("What concrete do you pour for a driveway?",
     "A 4,000 PSI mix with fiber mesh and rebar, over a compacted crushed limestone base. Many contractors pour the 3,000 PSI minimum."),
    ("How long before I can drive on a new concrete driveway?",
     "7 to 10 days. You can walk on new concrete after 24 to 48 hours. Concrete reaches about 70 percent of its strength at 7 days and its full design strength at 28 days."),
    ("Do pavers hold up under cars?",
     "Yes. Interlocking pavers distribute the load across the units, and charcoal concrete pavers laid in herringbone handle vehicle weight. A paver driveway needs a thicker base than a patio."),
    ("How do you keep a driveway from cracking on Austin clay?",
     "With the base, the steel, and the joints. We compact the subgrade, build a compacted crushed limestone base, reinforce the slab with fiber mesh and rebar, and cut control joints that give the concrete a planned place to crack."),
    ("How do you stop water from running down a driveway into the garage?",
     "With grade and a channel drain. A grated channel is set across the driveway at the low point. It catches the sheet of water at the surface and carries it to an outlet pipe."),
    ("Does a driveway count as impervious cover in Austin?",
     "Yes. A driveway counts toward the impervious cover of a lot, along with the house, the walks, and the patios."),
    ("Can you build a retaining wall beside a driveway?",
     "Yes. A wall beside a driveway carries the weight of vehicles above it, and it is engineered for that load."),
    ("What does a driveway cost in Austin?",
     "Every driveway is priced after a free on-site consultation. The size, the thickness, the reinforcement, the finish, and the access drive the price. Our patio cost guide explains what drives the price of poured concrete and pavers."),
]

S = ""
S += sec("The Work", "What Driveways Do We Build?", f"""    <p>Three kinds, and all three are built to carry vehicles. A driveway is reinforced for the load, jointed for expansion, and graded to drain.</p>
    <table class="cost-table">
      <thead><tr><th>Driveway</th><th>What It Is</th><th>Character</th></tr></thead><tbody>
      <tr><td>Poured concrete</td><td>A reinforced slab, formed, poured, and finished on site</td><td>One continuous surface</td></tr>
      <tr><td>Pavers</td><td>Interlocking units set on a compacted base</td><td>A single paver can be lifted and replaced</td></tr>
      <tr><td>Concrete with stone bands</td><td>A concrete field divided by bands of stone</td><td>Two materials in one surface</td></tr>
      </tbody></table>
    <p>We form, pour, and finish our own concrete, and we set our own pavers. A driveway is drawn on the same plan as the front walk, the beds beside it, and the lighting, so each one meets the next at the right height.</p>
    {fig([(D + "concrete-pads-gravel-steel-planters-front-yard-1200.webp", 1200, 630, "Front walk of poured concrete pads beside a concrete driveway, with dark gravel joints edged in steel, white gravel, and three square steel planters, in front of a modern house")],
         "Our concrete beside a driveway: a front walk of poured pads with steel-edged gravel joints and steel planters.")}
    <p>Driveways are part of our <a href="hardscaping-austin-tx">hardscaping</a> and our <a href="masonry-concrete-austin-tx">masonry and concrete</a> work.</p>""")

S += sec("Structure", "How Is a Driveway Built to Carry Vehicles?", f"""    <p>From the ground up. A car is a heavier load than a patio chair, and the slab only performs as well as what is under it.</p>
    <table class="cost-table">
      <thead><tr><th>Part</th><th>What We Build</th></tr></thead><tbody>
      <tr><td>Subgrade</td><td>Graded and compacted before anything is poured</td></tr>
      <tr><td>Base</td><td>Compacted crushed limestone. Crushed stone is the base for heavy-load areas.</td></tr>
      <tr><td>Concrete</td><td>A 4,000 PSI mix, not the 3,000 PSI minimum many contractors pour</td></tr>
      <tr><td>Reinforcement</td><td>Fiber mesh and rebar</td></tr>
      <tr><td>Joints</td><td>Jointed for expansion, with control joints that give the slab a planned place to crack</td></tr>
      <tr><td>Grade</td><td>Sloped so water leaves the surface</td></tr>
      </tbody></table>
    <p>Austin clay swells when it is wet and shrinks when it is dry. A slab laid on unprepared clay moves with it. The compacted base is what keeps a driveway still.</p>""", alt=True)

S += sec("Finishes", "Which Concrete Finish Suits a Driveway?", f"""    <p>One with grip. The slab is the same under every finish, and the finish sets the look and the traction.</p>
    <table class="cost-table">
      <thead><tr><th>Finish</th><th>How It Is Made</th><th>Character</th></tr></thead><tbody>
      <tr><td>Broom</td><td>A broom is dragged across the wet concrete to leave parallel lines</td><td>The workhorse finish for driveways and walks. Good traction.</td></tr>
      <tr><td>Exposed aggregate</td><td>The surface paste is washed away to show the stone in the mix</td><td>Textured and slip-resistant</td></tr>
      <tr><td>Smooth trowel</td><td>Troweled flat</td><td>Sleek, and slippery when wet. Best under a roof.</td></tr>
      <tr><td>Marbled</td><td>Two or more colors of concrete poured together and swirled by hand</td><td>Veining that runs through the full depth of the slab</td></tr>
      </tbody></table>
    <p>Broom-finished concrete can be colored with integral pigment for a warmer tone than standard gray. See our <a href="marbled-concrete-patios-austin-tx">marbled concrete</a> page for the decorative finishes.</p>""")

S += sec("Pavers", "What About a Paver Driveway?", f"""    <p>Pavers carry cars when the base and the pattern are right. Interlocking pavers distribute the load across the units, and charcoal concrete pavers laid in herringbone handle vehicle weight.</p>
    <ul>
      <li><strong>Base:</strong> a paver driveway needs a thicker base than a patio, because of the vehicle load.</li>
      <li><strong>Pattern:</strong> herringbone, in a charcoal concrete paver.</li>
      <li><strong>Edge:</strong> a steel border keeps the pavers from creeping at the edge.</li>
      <li><strong>Drainage:</strong> permeable pavers have open joints that let rain through.</li>
      <li><strong>Repair:</strong> a single paver can be lifted and replaced.</li>
    </ul>
    {fig([(P + "se-austin-fire-water/14-concrete-pads-boulders-800.webp", 800, 1067, "Freshly poured concrete pads with the form boards still between them and a steel edge along the side, beside a round concrete shell and boulders, in Southeast Austin"),
          (P + "svc-paver-patios-austin-tx/charcoal-pavers-herringbone-steel-edge-800.webp", 800, 1067, "Charcoal pavers laid in a herringbone pattern as a front walk, edged in steel, beside a steel-edged bed of tan gravel around a multi-trunk tree")],
         "Our two driveway materials on other jobs: concrete pads just poured in Southeast Austin, and charcoal pavers in herringbone on a front walk.")}
    <p>See our <a href="paver-patios-austin-tx">paver patios</a> page for the base and the joints, and our <a href="../blog/concrete-vs-paver-patio-austin-tx">concrete vs paver guide</a> for how each one handles clay.</p>""", alt=True)

S += sec("Water", "Where Does the Water Go?", f"""    <p>Away from the garage and the house. A driveway is a large hard surface, and every drop that lands on it runs somewhere.</p>
    <ul>
      <li><strong>Grade:</strong> the surface is sloped so water leaves it.</li>
      <li><strong>Channel drain:</strong> a grated channel set across the driveway at the low point catches the sheet of water and carries it to an outlet pipe.</li>
      <li><strong>Outlet:</strong> the pipe runs to a catch basin, a French drain, or daylight.</li>
    </ul>
    <p>Drainage is our first phase of construction. Water is designed before the paving, because everything built on top relies on it. See our <a href="drainage-austin-tx">drainage</a> page.</p>""")

S += sec("Slopes", "What If the Driveway Runs Along a Slope?", f"""    <p>Then a wall holds the grade, and the wall is built for the cars. A wall beside a driveway carries the weight of vehicles above it, and it is engineered for that load.</p>
    <p>Block with a stone or stucco face and poured concrete suit tall walls and walls that carry a driveway. In the City of Austin, a wall that supports a driveway needs a building permit and engineering, whatever its height.</p>
    <p>See our <a href="retaining-walls-austin-tx">retaining walls</a> page and our <a href="../blog/retaining-wall-permit-austin-tx">retaining wall permit guide</a>.</p>""", alt=True)

S += sec("Edges", "What Goes Along a Driveway?", f"""    <p>The parts that make it look finished: an edge, planting, a walk to the door, and light.</p>
    <ul>
      <li><strong>Steel edging:</strong> quarter-inch steel holds gravel and beds along the drive. See our <a href="steel-edging-austin-tx">steel edging</a> page.</li>
      <li><strong>Beds and planters:</strong> steel-edged beds and <a href="custom-planters-austin-tx">custom steel planters</a> stand along the drive and at the entry.</li>
      <li><strong>A walk to the door:</strong> concrete pads or a path lead from the driveway to the front door.</li>
      <li><strong>Light:</strong> low fixtures along the drive cast a pool of light down onto the surface. See our <a href="landscape-lighting-austin-tx">landscape lighting</a> page.</li>
    </ul>
    {fig([(D + "river-rock-steel-beds-between-driveway-and-walk-1200.webp", 1200, 630, "River rock and two steel-edged beds of dark gravel planted with variegated succulents and ferns, between a concrete driveway and the sidewalk, with a steel and wire screen behind")],
         "Beside a driveway: river rock and steel-edged beds between the drive and the sidewalk.")}
    <p>For the front of the house as a whole, see our <a href="../blog/curb-appeal-landscaping-austin-tx">curb appeal ideas</a>.</p>""")

S += sec("Curing", "When Can You Drive on New Concrete?", f"""    <p>After 7 to 10 days. Concrete gains strength over weeks, and a car is the last load it should meet.</p>
    <table class="cost-table">
      <thead><tr><th>After the Pour</th><th>What the Concrete Can Take</th></tr></thead><tbody>
      <tr><td>24 to 48 hours</td><td>Walking</td></tr>
      <tr><td>3 to 5 days</td><td>Light furniture</td></tr>
      <tr><td>7 to 10 days</td><td>Vehicles</td></tr>
      <tr><td>7 days</td><td>About 70 percent of full strength</td></tr>
      <tr><td>28 days</td><td>Full design strength</td></tr>
      </tbody></table>
    <p>We apply curing compound right after finishing, so the concrete cures properly and reaches its strength.</p>""", alt=True)

S += sec("Lot Limits", "Does a Driveway Count as Impervious Cover?", f"""    <p>Yes. A driveway counts toward the impervious cover of a lot, together with the house, the garage, the walks, and the patios.</p>
    <p>Where the lot sits sets the limit. Over the Barton Springs Zone, Austin's Save Our Springs ordinance caps impervious cover at 15 percent of net site area in the recharge zone and 20 to 25 percent in the contributing zone. On a lot near its limit, the size of the drive is settled on the plan before anything is built. See our <a href="../locations/barton-creek-tx">Barton Creek</a> page.</p>""")

S += sec("How We Build", "How Is a Concrete Driveway Poured?", f"""    {step(1, "Consultation and Plan", "Free and on site. We walk the property with you, and the owner draws the driveway on a CAD plan, which is included. See our <a href=\"landscape-design-austin-tx\">landscape design</a> page.")}
    {step(2, "Grade and Compact", "We set the layout, grade for drainage, and compact the subgrade. This is the work that decides whether a slab stays flat.")}
    {step(3, "Base and Forms", "Crushed limestone is compacted, and then the forms and the reinforcement go in.")}
    {step(4, "Pour and Finish", "4,000 PSI concrete with fiber mesh and rebar, finished to the look you chose.")}
    {step(5, "Cure", "Walk on it after 24 to 48 hours. Keep vehicles off for 7 to 10 days.")}""", alt=True)

S += sec("Our Work", "Where Can You See Our Concrete and Pavers?", f"""    <p>On the patios and walks we have built across the Austin area. The same crew and the same mix build our driveways.</p>
    <ul>
      <li><strong>Southeast Austin:</strong> concrete pads formed and poured in place, with dark gravel joints. See <a href="../blog/water-feature-fire-pits-southeast-austin-tx">the build</a>.</li>
      <li><strong><a href="../locations/pflugerville-tx">Pflugerville</a>:</strong> poured concrete patio pads with lit, steel-edged gravel joints. See <a href="../projects/axehandle">the project</a>.</li>
      <li><strong>Cedar Creek:</strong> large concrete pavers poured in place around a pool. See <a href="../blog/pavers-with-artificial-turf-austin-tx">pavers with artificial turf</a>.</li>
      <li><strong>South Austin:</strong> two-by-four-foot limestone pavers in a welded steel frame. See <a href="../projects/williston-loop">Williston Loop</a>.</li>
    </ul>
    {AREAS}
    {STANDING}
    <p>For what drives the price of poured concrete and pavers, see our <a href="../blog/patio-cost-austin-tx">patio cost guide</a>. More of our built work is on the <a href="../featured">Signature Projects</a> page.</p>""")

ANSWER = ("<strong>Red Agave Landscape</strong> builds driveways in Austin, TX in poured concrete, in pavers, and in concrete with stone bands. "
          "Each one is reinforced for vehicles, jointed for expansion, and graded to drain. "
          "Our concrete is a 4,000 PSI mix with fiber mesh and rebar, poured over a compacted crushed limestone base, and our own crew forms, pours, and finishes it. "
          "We have built in Austin since 2009. "
          "Each project starts with a free consultation, and the CAD plan is included. Call or text 512-695-7566.")
check(S, ANSWER, *[q + " " + a for q, a in FAQS])

build(ROOT, dict(
    slug=SLUG, crumb="Driveways", h1="Driveways",
    title="Driveways Austin TX | Concrete & Paver Driveways",
    desc="Red Agave builds concrete and paver driveways in Austin, TX: a 4,000 PSI mix with rebar on compacted limestone, jointed and graded to drain.",
    og_img="https://www.redagaveatx.com/images/projects/svc-driveways-austin-tx/concrete-pads-gravel-steel-planters-front-yard-1200.webp",
    bg_l="../images/projects/svc-driveways-austin-tx/concrete-pads-gravel-steel-planters-front-yard-1200.webp",
    bg_s="../images/projects/svc-driveways-austin-tx/concrete-pads-gravel-steel-planters-front-yard-800.webp",
    answer_h2="Who Builds Driveways in Austin, TX?",
    answer=ANSWER,
    sections=S, faqs=FAQS, cta="Plan Your Driveway",
    service_name="Concrete and Paver Driveways", service_type="Driveway construction",
    service_desc="Driveways built in Austin, TX in poured concrete, pavers, and concrete with stone bands: a 4,000 PSI mix with fiber mesh and rebar over a compacted crushed limestone base, reinforced for vehicles, jointed for expansion, and graded to drain. Built by Red Agave's own crew, with a free consultation and the CAD plan included."))

card = ('  <a href="services/' + SLUG + '" class="svc-card rev"><img src="images/projects/svc-driveways-austin-tx/concrete-pads-gravel-steel-planters-front-yard-800.webp" '
        'sizes="(max-width:768px) 80vw, 33vw" alt="Poured concrete pads with steel-edged gravel joints beside a driveway" loading="lazy"><div class="svc-ov"></div>'
        '<div class="svc-info"><div class="svc-n">{N}</div><div class="svc-name">Driveways</div><div class="svc-desc">Poured concrete, pavers &amp; stone bands</div></div></a>\n')
if "--register" in sys.argv:
    register(ROOT, SLUG, card, "- Driveways (poured concrete, pavers, and concrete with stone bands; 4,000 PSI concrete with fiber mesh and rebar on compacted crushed limestone, jointed for expansion and graded to drain): redagaveatx.com/services/" + SLUG, "2026-11-20")

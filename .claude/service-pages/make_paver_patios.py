import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svc_lib import build, register, fig, step, sec, H3
from svc_extra import check, AREAS, STANDING

ROOT = sys.argv[1]
SLUG = "paver-patios-austin-tx"
P = "images/projects/"
V = P + "svc-paver-patios-austin-tx/"

FAQS = [
    ("Who builds paver patios in Austin, TX?",
     "Red Agave Landscape designs and builds paver patios in Austin in manufactured concrete pavers, large-format pavers, limestone and travertine pavers, and concrete pavers poured in place. Every patio sits on 6 to 8 inches of compacted crushed limestone with steel edging at the perimeter, and our own crew builds it."),
    ("What goes under a paver patio?",
     "A compacted base. We excavate, compact the subgrade, lay geotextile fabric over the clay, and build 6 to 8 inches of compacted crushed limestone. The pavers are set on a 1-inch bed of coarse sand or screenings."),
    ("Do pavers crack on Austin clay?",
     "A paver patio moves with the ground. The joints between the pavers take up the movement of the clay, where a single slab is rigid. A paver that settles is lifted, the base under it is leveled, and the paver is set back."),
    ("What size pavers do you install?",
     "Large-format pavers are 24 by 24 inches and 24 by 48 inches. In South Austin we set limestone pavers that are two feet by four feet. Concrete pavers poured in place are made to the size on the plan."),
    ("What goes in the joints between pavers?",
     "Polymeric sand for a tight joint. For a wide joint we use gravel, river rock, or artificial turf. On one patio the joint is a band of darker pavers."),
    ("Can you put turf between pavers?",
     "Yes. In Cedar Creek we poured large concrete pavers around a pool and ran a strip of artificial turf through every joint."),
    ("Which pavers stay coolest in the Austin sun?",
     "Travertine. It stays cooler than concrete in direct sun. Light colors reflect more sunlight than dark ones, and charcoal pavers get the hottest."),
    ("Are pavers better than poured concrete?",
     "Each suits a different job. Pavers flex with the ground, and a single paver can be lifted and replaced. Poured concrete gives one clean, seamless surface. We build both."),
    ("Do I need a permit for a paver patio in Austin?",
     "Most ground-level patios do not need a building permit. A patio with a roofed structure, an attachment to the foundation of the house, or electrical or plumbing work is different, and we handle those permits."),
    ("What does a paver patio cost in Austin?",
     "Every patio is priced after a free on-site consultation. The size, the paver, the base work, the edging, and the access to the yard drive the price. Our patio cost guide explains each one."),
]

S = ""
S += sec("The Work", "What Paver Patios Do We Build?", f"""    <p>A paver patio is a floor made of separate pieces. The pieces sit on a compacted base, and the joints between them let the floor move with the ground. We build with four kinds of paver.</p>
    <table class="cost-table">
      <thead><tr><th>Paver</th><th>What It Is</th><th>Where</th></tr></thead><tbody>
      <tr><td>Manufactured concrete pavers</td><td>Made in consistent sizes and laid in a pattern</td><td>Patios, walks, and drives</td></tr>
      <tr><td>Large-format pavers</td><td>Pavers 24 by 24 inches and 24 by 48 inches, from Belgard and other makers</td><td>Modern patios with few joints</td></tr>
      <tr><td>Stone pavers</td><td>Limestone and travertine cut to size</td><td>Built in South Austin</td></tr>
      <tr><td>Poured concrete pavers</td><td>Each paver formed and poured in place as its own pad</td><td>Built in Cedar Creek and Circle C</td></tr>
      </tbody></table>
    {fig([(V + "grid-paver-patio-dark-bands-1200.webp", 1200, 900, "Raised patio of pale square pavers divided into a grid by bands of dark pavers, edged in steel, with stepped steel beds of black gravel at its corner, behind a limestone house")],
         "A grid patio: pale square pavers divided by bands of dark pavers, raised on a steel edge.")}
    <p>A paver patio is one of five patio surfaces we build. Our <a href="patios-austin-tx">patios</a> page covers poured concrete, travertine, and flagstone, and our <a href="hardscaping-austin-tx">hardscaping</a> page shows how the patio meets the walls and the steps.</p>""")

S += sec("Austin Clay", "Why Pavers on Austin Clay?", f"""    <p>Because the ground here moves. Austin clay swells when it is wet and shrinks when it is dry, and whatever is built on it has to answer that.</p>
    <ul>
      <li><strong>The joints take the movement:</strong> each paver is free to shift a little, so the floor flexes where a single slab is rigid.</li>
      <li><strong>A low spot is repaired, not replaced:</strong> a paver that settles is lifted, the base under it is leveled, and the paver is set back.</li>
      <li><strong>One paver can be swapped:</strong> a damaged unit comes out, and a new one goes in.</li>
      <li><strong>Pipes stay reachable:</strong> pavers are pulled to reach a line under the patio and set back when the work is done.</li>
      <li><strong>Water gets through:</strong> the joints let rain drain into the base.</li>
    </ul>
    <p>Our <a href="../blog/concrete-vs-paver-patio-austin-tx">concrete vs paver patio guide</a> compares the two on clay, side by side.</p>""", alt=True)

S += sec("Below the Surface", "How Is a Paver Patio Built?", f"""    <p>From the bottom up. The base is the part you never see, and it decides whether the patio stays flat.</p>
    {step(1, "Excavate and Compact", "We dig to the depth the pavers and their base need, and compact the soil at the bottom.")}
    {step(2, "Fabric", "Woven geotextile fabric goes over the clay, so the clay stays out of the base above it.")}
    {step(3, "Base", "6 to 8 inches of crushed limestone, compacted, and graded so water moves away from the house.")}
    {step(4, "Setting Bed", "One inch of coarse sand or screenings, screeded flat. This is the final leveling layer.")}
    {step(5, "Set the Pavers", "Pavers go down on the bed with consistent joints, in the pattern on the plan.")}
    {step(6, "Edge", "Steel edging goes around the perimeter. It holds the field square and keeps the pavers from creeping.")}
    {step(7, "Joints", "Polymeric sand is swept into tight joints. Wide joints are filled with gravel, river rock, or turf. A plate compactor with a rubber pad seats the pavers.")}
    <p>The patio is drawn on the CAD plan first, with every run dimensioned. See our <a href="landscape-design-austin-tx">landscape design</a> page.</p>""")

S += sec("Joints", "What Goes Between the Pavers?", f"""    <p>The joint is half the look. A tight joint makes one quiet floor, and a wide joint turns each paver into its own piece.</p>
    <table class="cost-table">
      <thead><tr><th>Joint</th><th>The Look</th><th>Where We Built It</th></tr></thead><tbody>
      <tr><td>Polymeric sand</td><td>A tight joint that hardens and keeps weeds and insects out</td><td>Tight-jointed patios</td></tr>
      <tr><td>Pea gravel</td><td>Pavers that float in a bed of gravel</td><td>South Austin</td></tr>
      <tr><td>River rock</td><td>A gray line that sets each paver apart</td><td>Circle C</td></tr>
      <tr><td>Artificial turf</td><td>A green grid, soft underfoot</td><td>Cedar Creek</td></tr>
      <tr><td>Dark paver bands</td><td>A second, darker paver laid as the joint</td><td>The grid patio above</td></tr>
      </tbody></table>
    {fig([(P + "williston-loop/02-limestone-pavers-pea-gravel-welded-steel-side-yard-768.webp", 768, 1024, "Two-by-four-foot limestone pavers set in pea gravel inside a welded steel frame, running down a side yard between limestone gravel and basalt gravel, in South Austin"),
          (P + "hopeland/IMG_9622-800.webp", 800, 1067, "Concrete pavers cut on the diagonal with river rock joints beside a long steel planter lit under its rim in Circle C, Austin"),
          (P + "flycatcher/IMG_8720-800.webp", 800, 1067, "Large poured concrete pavers with artificial turf joints beside a pool, with steel-edged steps below, in Cedar Creek, TX")],
         "Pea gravel joints in South Austin, river rock joints in Circle C, and turf joints in Cedar Creek.")}
    <p>See our post on <a href="../blog/pavers-with-artificial-turf-austin-tx">pavers with artificial turf</a>, which shows the Cedar Creek plan next to the finished yard.</p>""", alt=True)

S += sec("Pattern", "Which Paver Patterns Do We Lay?", f"""    <p>The pattern that suits the house and the shape of the yard. These are five we have built.</p>
    <ul>
      <li><strong>Grid with bands:</strong> pale square pavers, with a darker paver between them as a band and around them as a border.</li>
      <li><strong>Herringbone:</strong> small charcoal pavers locked at right angles. The pattern suits a walk or a drive.</li>
      <li><strong>Long pads in a row:</strong> two-by-four-foot limestone pavers laid end to end down a side yard.</li>
      <li><strong>Diagonal cuts:</strong> large concrete pavers cut on the diagonal, so the joints run at an angle to the house.</li>
      <li><strong>Cut to a curve:</strong> the outer pavers are cut to follow a curved steel edge.</li>
    </ul>
    {fig([(V + "grid-paver-patio-steel-edge-corner-800.webp", 800, 1067, "Corner of a patio of pale square pavers and dark paver bands, raised on a steel edge above steel-edged beds of dark gravel"),
          (V + "charcoal-pavers-herringbone-steel-edge-800.webp", 800, 1067, "Charcoal pavers laid in a herringbone pattern as a front walk, edged in steel, beside a steel-edged bed of tan gravel around a multi-trunk tree"),
          (V + "curved-paver-walk-gravel-joints-800.webp", 800, 1067, "Curved walk of pale pavers cut to the curve, with black gravel joints and a steel edge, leading to raised wood garden beds")],
         "A grid with dark bands, charcoal herringbone, and pale pavers cut to a curve.")}""")

S += sec("The Edge", "What Holds the Edge of a Paver Patio?", f"""    <p>Steel. Pavers need a restraint at the perimeter, or the outer rows creep outward and the joints open. We build paver patios with steel edging at every perimeter.</p>
    <p>Steel also does more than hold. On the grid patio, the pavers sit on a raised steel edge, and three steel-edged beds of black gravel step down from the corner to the lawn. Along the porch, a strip of black beach pebbles fills the gap between the porch slab and the pavers.</p>
    <p>The edge can be lit. We set 24V lighting in steel edges and in paver joints, so the outline of the patio shows after dark. See our <a href="steel-edging-austin-tx">steel edging</a> and <a href="landscape-lighting-austin-tx">landscape lighting</a> pages.</p>
    {fig([(V + "grid-paver-patio-beach-pebble-edge-800.webp", 800, 600, "Grid patio of pale pavers and dark paver bands with a strip of black beach pebbles against the porch slab, with a lawn beyond at sunset")],
         "Black beach pebbles between the porch slab and the pavers.")}""", alt=True)

S += sec("Heat", "Which Pavers Stay Cool in the Austin Sun?", f"""    <p>The light ones. Color and material decide how hot a patio gets underfoot.</p>
    <ul>
      <li><strong>Travertine:</strong> stays cooler than concrete in direct sun, which is why it is used around pools.</li>
      <li><strong>Light pavers:</strong> limestone, cream, and light gray reflect more sunlight and stay cooler.</li>
      <li><strong>Charcoal pavers:</strong> the hottest in full sun. They suit a shaded patio, a walk, or a drive.</li>
    </ul>
    <p>Shade does the rest. A roof or a pergola over the patio is drawn on the same plan, so the posts land where the pavers allow. See our <a href="pergolas-austin-tx">pergolas</a> page and our <a href="patio-covers-pavilions-austin-tx">patio covers and pavilions</a> page. Our guide to <a href="../blog/travertine-vs-flagstone-vs-pavers-austin-tx">travertine, flagstone, and pavers</a> compares the three.</p>""")

S += sec("Compare", "Pavers or Poured Concrete?", f"""    <p>Each one suits a different job. We build both, and we often use both on one yard.</p>
    <table class="cost-table">
      <thead><tr><th></th><th>Pavers</th><th>Poured Concrete</th></tr></thead><tbody>
      <tr><td>Surface</td><td>Separate units with joints</td><td>One seamless slab</td></tr>
      <tr><td>On clay</td><td>The joints take up movement</td><td>Rigid. Control joints direct where it cracks.</td></tr>
      <tr><td>Repair</td><td>Lift and reset, or swap one paver</td><td>Patch or replace a section</td></tr>
      <tr><td>Reaching a pipe</td><td>Pull the pavers and set them back</td><td>Cut the slab</td></tr>
      <tr><td>Design</td><td>Pattern, color, and joint</td><td>Finish: brushed, exposed aggregate, smooth, or marbled</td></tr>
      </tbody></table>
    <p>Our concrete is a 4,000 PSI mix with fiber mesh and rebar. See our <a href="masonry-concrete-austin-tx">masonry and concrete</a> page and our <a href="marbled-concrete-patios-austin-tx">marbled concrete</a> page.</p>""", alt=True)

S += sec("Fire and Seating", "What Goes on a Paver Patio?", f"""    <p>The parts that make it a room. Pavers are set around them, so the fire and the seating look built in and not placed on top.</p>
    <ul>
      <li><strong>Fire:</strong> a fire pit stands at the center of the paving, with the pavers running up to its base.</li>
      <li><strong>Seating:</strong> a steel planter with a cantilevered wood bench closes the corner of the patio.</li>
      <li><strong>Cooking:</strong> an <a href="outdoor-kitchens-austin-tx">outdoor kitchen</a> stands on the same floor.</li>
    </ul>
    {fig([(V + "stone-pavers-gravel-joints-fire-pit-800.webp", 800, 534, "Large pale stone pavers with dark gravel joints around a square block fire pit, with a steel planter and a cantilevered wood bench along a horizontal wood fence"),
          (V + "pavers-turf-joints-fire-table-800.webp", 800, 597, "Large pale pavers with turf joints around a square steel fire pit with a stone cap, beside a band of beach pebbles and a stone block edge")],
         "Pavers with gravel joints around a block fire pit, and pavers with turf joints around a steel fire pit.", wide=True)}
    <p>See our <a href="fire-pits-austin-tx">custom fire pits</a> page and our <a href="outdoor-living-austin-tx">outdoor living</a> page.</p>""")

S += sec("Our Work", "Where Have We Built Paver Patios?", f"""    <ul>
      <li><strong>South Austin, 2018:</strong> limestone pavers, each two feet by four feet, set in pea gravel inside a raised welded steel frame, running to a wood deck and a limestone fire pit. See <a href="../projects/williston-loop">Williston Loop</a>.</li>
      <li><strong>Cedar Creek:</strong> large concrete pavers poured on two sides of a pool, with artificial turf in every joint and steel-edged steps below. One run on the plan is 30 feet 1 inch long and 8 feet 1 inch wide. See <a href="../projects/flycatcher">the project</a>.</li>
      <li><strong><a href="../locations/circle-c-tx">Circle C</a>:</strong> concrete pavers cut on the diagonal with river rock joints, beside a long steel planter lit under its rim. See <a href="../projects/hopeland">the project</a>.</li>
      <li><strong>A grid patio:</strong> pale square pavers with dark paver bands, raised on a steel edge, with stepped beds of black gravel.</li>
    </ul>
    {AREAS}
    {STANDING}
    <p>For what drives the price, see our <a href="../blog/patio-cost-austin-tx">patio cost guide</a>. For layouts, see our <a href="../blog/patio-design-ideas-austin-tx">patio design ideas</a>. More of our built work is on the <a href="../featured">Signature Projects</a> page.</p>""", alt=True)

ANSWER = ("<strong>Red Agave Landscape</strong> designs and builds paver patios in Austin, TX in manufactured concrete pavers, large-format pavers, "
          "limestone and travertine pavers, and concrete pavers poured in place. "
          "Every patio sits on 6 to 8 inches of compacted crushed limestone, graded so water moves away from the house, with steel edging at the perimeter. "
          "The joints are polymeric sand, gravel, river rock, or artificial turf. "
          "We have built in Austin since 2009, and every patio is built by our own crew. "
          "Each project starts with a free consultation, and the CAD plan is included. Call or text 512-695-7566.")
check(S, ANSWER, *[q + " " + a for q, a in FAQS])

build(ROOT, dict(
    slug=SLUG, crumb="Paver Patios", h1="Paver Patios",
    title="Paver Patios Austin TX | Design & Installation",
    desc="Red Agave builds paver patios in Austin, TX: concrete, limestone, and large-format pavers on a compacted limestone base with steel edging.",
    og_img="https://www.redagaveatx.com/images/projects/svc-paver-patios-austin-tx/grid-paver-patio-dark-bands-1200.webp",
    bg_l="../images/projects/svc-paver-patios-austin-tx/grid-paver-patio-dark-bands-1200.webp",
    bg_s="../images/projects/svc-paver-patios-austin-tx/grid-paver-patio-dark-bands-800.webp",
    answer_h2="Who Builds Paver Patios in Austin, TX?",
    answer=ANSWER,
    sections=S, faqs=FAQS, cta="Plan Your Paver Patio",
    service_name="Paver Patio Design and Installation", service_type="Paver patio installation",
    service_desc="Paver patios designed and built in Austin, TX in manufactured concrete pavers, large-format pavers, limestone and travertine pavers, and concrete pavers poured in place, on 6 to 8 inches of compacted crushed limestone with steel edging and joints of polymeric sand, gravel, river rock, or artificial turf. Built by Red Agave's own crew, with a free consultation and the CAD plan included."))

card = ('  <a href="services/' + SLUG + '" class="svc-card rev"><img src="images/projects/svc-paver-patios-austin-tx/grid-paver-patio-dark-bands-800.webp" '
        'sizes="(max-width:768px) 80vw, 33vw" alt="Grid patio of pale square pavers with dark paver bands, raised on a steel edge" loading="lazy"><div class="svc-ov"></div>'
        '<div class="svc-info"><div class="svc-n">{N}</div><div class="svc-name">Paver Patios</div><div class="svc-desc">Concrete, limestone &amp; large-format pavers</div></div></a>\n')
if "--register" in sys.argv:
    register(ROOT, SLUG, card, "- Paver patios (manufactured concrete pavers, large-format pavers, limestone and travertine pavers, concrete pavers poured in place; 6 to 8 inches of compacted crushed limestone, steel edging, joints of polymeric sand, gravel, river rock, or artificial turf): redagaveatx.com/services/" + SLUG, "2026-11-20")

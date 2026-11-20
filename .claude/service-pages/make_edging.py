import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svc_lib import build, register, fig, step, sec, H3

ROOT = sys.argv[1]
SLUG = "steel-edging-austin-tx"
P = "images/projects/"

FAQS = [
    ("Who installs steel landscape edging in Austin, TX?",
     "Red Agave Landscape fabricates and installs custom steel edging in Austin from quarter-inch mild steel plate. Joints are butt-welded on site and ground smooth, and welded rebar stakes anchor the edge. Our own crew does the work."),
    ("How thick is your steel edging?",
     "One quarter inch. Thin edging bows under the soil behind it and bends under a mower. Quarter-inch plate stays straight."),
    ("How tall is steel edging, and how deep does it go?",
     "Standard edging is 4 inches tall, with 1 inch above the ground and 3 inches buried. For raised borders we use 6-inch plate with 2 to 3 inches showing. The welded stakes are driven 12 to 18 inches into the ground."),
    ("How are the joints made?",
     "Each length is butt-welded to the next on site, and the weld is ground smooth and flush. A run of our edging has no clips, bolts, or overlaps."),
    ("Does steel edging rust through?",
     "No. Uncoated mild steel forms a stable layer of rust that seals the steel under it. At a quarter inch thick, decades of surface rust leave far more steel than the edge needs."),
    ("How long does the rust patina take?",
     "Uncoated steel develops a natural rust patina over 6 to 12 months. It starts bright orange in the first weeks and settles to an even rust-brown."),
    ("Can steel edging be black?",
     "Yes. Steel can be powder-coated in black, dark bronze, or charcoal. It can also be clear-coated to hold its dark gray color, or wax-sealed to hold a patina tone."),
    ("Can steel edging curve?",
     "Yes. Wide sweeps are rolled, moderate curves are bent on site with a hydraulic bender, and tight curves are heated with a torch and formed while hot."),
    ("Can steel edging be lit?",
     "Yes. We run LED strips along the steel edge, so a gravel court or a bed is outlined in light after dark."),
    ("What does steel edging cost in Austin?",
     "Every job is priced after a free on-site consultation. The length, the height of the plate, and the number of curves and corners drive the price. Our steel edging cost guide explains each one."),
]

S = ""
S += sec("The Edge", "What Is Steel Edging?", f"""    <p>A band of steel plate set on edge in the ground, to keep two materials apart. Gravel stays out of the lawn, mulch stays out of the gravel, and the line between them stays where it was drawn. It is used in seven places:</p>
    <ul>
      <li><strong>Lawn to gravel:</strong> the most common one. Steel keeps the gravel in its bed and the grass out of it.</li>
      <li><strong>Planting beds:</strong> a crisp border around <a href="xeriscape-austin-tx">xeriscape</a> beds and native planting.</li>
      <li><strong>Fire pit courts:</strong> a ring or a square of steel holds the gravel around a <a href="fire-pits-austin-tx">fire pit</a>.</li>
      <li><strong>Driveways:</strong> a steel border keeps pavers from creeping at the edge.</li>
      <li><strong>Raised planters:</strong> plate 8 to 12 inches tall, bent into rectangles, L shapes, or curves.</li>
      <li><strong>Steps:</strong> steel plate as the riser, with gravel or decomposed granite as the tread.</li>
      <li><strong>Water features:</strong> steel holds the gravel edge and keeps mulch out of the water.</li>
    </ul>
    {fig([(P + "east-austin-steel-boulders/03-finished-steel-edging-boulders-mulch-fern-1200.webp", 1200, 675, "Finished steel edging running into boulders, holding a bed of black mulch with a fern on one side and river rock on the other, beside sod and dark stone in East Austin")],
         "East Austin: steel edging holds black mulch on one side and river rock on the other.")}""")

S += sec("Thickness", "Why Quarter-Inch Steel?", f"""    <p>Because it stays straight. Most edging sold for landscapes is plastic or thin steel. Mowers, swelling clay, and roots push it out of line within a few years.</p>
    <table class="cost-table">
      <thead><tr><th></th><th>Plastic Edging</th><th>Thin Steel (14 Gauge)</th><th>Quarter-Inch Steel</th></tr></thead><tbody>
      <tr><td>Holds its line</td><td>Warps in 1 to 2 years</td><td>Warps in 3 to 5 years</td><td>Stays straight</td></tr>
      <tr><td>Mowers and equipment</td><td>Breaks</td><td>Bends and dents</td><td>No visible damage</td></tr>
      <tr><td>Curves</td><td>Faceted, shows segments</td><td>Better, still kinks</td><td>Smooth radius</td></tr>
      <tr><td>Joints</td><td>Plastic clips</td><td>Overlapped pieces</td><td>Butt-welded, ground smooth</td></tr>
      <tr><td>Anchors</td><td>Plastic stakes</td><td>Wire pin stakes</td><td>Welded half-inch rebar stakes</td></tr>
      </tbody></table>
    <p>Quarter-inch plate is thick enough to be driven over by a mower without showing it. It is the same plate we use for our <a href="steel-retaining-walls-austin-tx">steel retaining walls</a> and our <a href="custom-planters-austin-tx">custom steel planters</a>.</p>""", alt=True)

S += sec("How We Build", "How Is Our Steel Edging Made and Installed?", f"""    <p>It is fabricated for each yard and welded in place. Nothing is ordered from a catalog and hammered in.</p>
    {step(1, "Plan", "The lines are drawn on the CAD plan, which is included with every project. See our <a href=\"landscape-design-austin-tx\">landscape design</a> page.")}
    {step(2, "Plate", "We use A36 hot-rolled mild steel plate, cut to 4-inch or 6-inch heights. Standard edging is 4 inches tall, with 1 inch above the ground and 3 inches buried. For a raised border, 6-inch plate shows 2 to 3 inches.")}
    {step(3, "Stakes", "Half-inch rebar stakes are MIG-welded to the back of the plate every 3 to 4 feet, where they are hidden. They are driven 12 to 18 inches into the ground.")}
    {step(4, "Joints", "Each length is butt-welded to the next on site. The weld is ground smooth and flush, so the run reads as one continuous band of steel.")}
    {step(5, "Curves and Corners", "Curves are rolled, bent, or heated on site to the line on the plan. Corners are cut and welded.")}
    {step(6, "Finish", "The steel is left to weather, or it is coated. Then the gravel, the mulch, and the planting go in against it.")}""")

S += sec("Curves", "How Do We Bend Steel Into Curves?", f"""    <p>By the radius. A wide sweep and a tight ring are made in different ways.</p>
    <table class="cost-table">
      <thead><tr><th>Curve</th><th>How It Is Made</th><th>Result</th></tr></thead><tbody>
      <tr><td>48 inches and wider</td><td>Cold-rolled through a hydraulic plate roller</td><td>A smooth, continuous arc</td></tr>
      <tr><td>24 to 48 inches</td><td>Bent on site with a hydraulic bender</td><td>A tight, clean radius</td></tr>
      <tr><td>Under 24 inches</td><td>Heated with a torch and formed while hot</td><td>A precise custom shape</td></tr>
      <tr><td>Compound curves</td><td>Several heat-and-bend passes</td><td>Flowing, organic lines</td></tr>
      </tbody></table>
    <p>Thin edging shows a curve as a row of short straight pieces. Quarter-inch plate bends into one true arc.</p>""", alt=True)

S += sec("Patina", "How Does Steel Edging Age?", f"""    <p>It rusts on the surface, and then it stops. Uncoated mild steel develops a natural rust patina over 6 to 12 months. The stable layer of rust seals the steel under it.</p>
    <table class="cost-table">
      <thead><tr><th>Time</th><th>Color</th></tr></thead><tbody>
      <tr><td>Weeks 1 to 2</td><td>Bright orange flash rust</td></tr>
      <tr><td>Months 1 to 3</td><td>Uneven orange-brown</td></tr>
      <tr><td>Months 3 to 6</td><td>Deep amber-brown</td></tr>
      <tr><td>Months 6 to 12</td><td>Even rust-brown, now stable</td></tr>
      <tr><td>Year 2 and after</td><td>Dark chocolate brown</td></tr>
      </tbody></table>
    <p>The steel can also be finished four ways:</p>
    <ul>
      <li><strong>Raw:</strong> left to weather. The warmest look, and the one we build most.</li>
      <li><strong>Clear-coated:</strong> a clear lacquer holds the dark gray of new steel.</li>
      <li><strong>Powder-coated:</strong> black, dark bronze, or charcoal, in one even color.</li>
      <li><strong>Wax-sealed:</strong> wax applied once the patina has started holds that tone.</li>
    </ul>
    {fig([("images/gallery/IMG_0991-800.webp", 800, 600, "Rust-patina steel edging holding a gravel bed of agaves, prickly pear, and fountain grass, with tan decomposed granite in front")],
         "Uncoated steel after it has weathered: an even rust-brown edge around a gravel bed.")}""")

S += sec("Steel and Stone", "What Happens Where the Edge Meets a Boulder?", f"""    <p>The steel goes into the stone. We set the boulder first, cut a narrow slot into the rock with an angle grinder, and seat the quarter-inch plate inside it. The steel does not stop short of the boulder or bend around it.</p>
    <p>A gap is where an edge fails. If the steel stops beside a boulder, the gravel and the mulch meet in the space between them. With the plate inside the stone, there is no opening. See our post on <a href="../blog/steel-edging-cut-into-boulders-austin-tx">steel edging cut into boulders</a>.</p>
    {fig([(P + "east-austin-steel-boulders/02-steel-edging-through-boulders-install-1200.webp", 1200, 675, "Steel edging running in straight angled lines between boulders during installation, with a level across the top and the far end seated in a slot cut into a boulder, in East Austin")],
         "East Austin, during the install: the steel runs between the boulders and into them.")}""", alt=True)

S += sec("After Dark", "Can Steel Edging Be Lit?", f"""    <p>Yes. We run LED strips along the steel, so the edge of a gravel court or a bed is a line of light at night. Red Agave is the only company in Austin that builds custom LED planters with custom light channels, and we light our edging the same way.</p>
    <ul>
      <li><strong>Overlook at Lewis Mountain, Southwest Austin:</strong> a light strip traces the steel edge of the gravel fire court.</li>
      <li><strong>Southeast Austin:</strong> light strips run along the steel edging around a round water feature and two fire pits.</li>
      <li><strong>Pearson Ranch, Northwest Austin:</strong> warm LED strips glow under the steel edging around concrete patio pads.</li>
    </ul>
    <p>See our <a href="landscape-lighting-austin-tx">landscape lighting</a> page.</p>
    {fig([(P + "blazyk/IMG_8703-800.webp", 800, 1067, "Gravel court with boulders, ferns, and a fire pit, lit by a strip along its steel edge at night at the Overlook at Lewis Mountain, Southwest Austin"),
          (P + "se-austin-fire-water/19-finished-water-feature-fire-pit-dusk-800.webp", 800, 1067, "Round water feature and curved steel fire pit at dusk with light strips along the steel edging in Southeast Austin")],
         "Lit steel edges at the Overlook at Lewis Mountain and in Southeast Austin.")}""")

S += sec("The Metal", "Why Mild Steel?", f"""    <p>Because it does everything an edge needs. We build in mild steel, not aluminum.</p>
    <ul>
      <li><strong>It welds in the field:</strong> lengths are joined on site into one band.</li>
      <li><strong>It forms:</strong> it rolls, bends, and takes heat, so it follows any line on the plan.</li>
      <li><strong>It weathers:</strong> it turns a warm rust-brown that suits gravel, limestone, and agaves.</li>
    </ul>
    <p>Aluminum stays silver, and it reads as light in a yard. Stainless steel stays bright, which is the wrong look beside plants and stone. Our post on <a href="../blog/steel-edging-fabrication-austin-tx">steel edging fabrication</a> goes deeper into the metal.</p>""", alt=True)

S += sec("Our Work", "Where Have We Installed Steel Edging?", f"""    <p>On almost every yard we build. Six of them:</p>
    <ul>
      <li><strong>Overlook at Lewis Mountain, Southwest Austin:</strong> 260 linear feet of quarter-inch steel edges every level of a terraced slope. See <a href="../projects/blazyk">the case study</a>.</li>
      <li><strong>East Austin:</strong> steel edging cut into boulders, with black mulch on one side and river rock on the other.</li>
      <li><strong>Southeast Austin:</strong> lit steel edging around a dark gravel court, a round water feature, and two fire pits. See <a href="../blog/water-feature-fire-pits-southeast-austin-tx">the build</a>.</li>
      <li><strong>Pearson Ranch, Northwest Austin:</strong> steel-edged gravel joints between concrete patio pads, lit from under the steel. See <a href="../projects/axehandle">the case study</a>.</li>
      <li><strong>South Austin:</strong> a black steel edge along a front-yard terrace, with firecracker fern spilling over it.</li>
      <li><strong><a href="../locations/bee-cave-tx">Bee Cave</a>:</strong> steel-walled terraces of dark gravel beside a wood deck.</li>
    </ul>
    {fig([("images/plants/firecracker-fern/firecracker-fern-steel-edge-800.webp", 800, 1015, "Firecracker fern with red tubular flowers spilling over a black steel edge in South Austin"),
          (P + "east-austin-steel-boulders/01-steel-plate-seated-in-boulder-slot-800.webp", 800, 1067, "Quarter-inch steel edging seated in a slot cut into a boulder with an angle grinder, in a yard under construction in East Austin")],
         "A black steel edge in South Austin, and a plate seated in a boulder in East Austin.")}
    <p>Steel edging is one part of our <a href="hardscaping-austin-tx">hardscaping</a>. For what drives the price, see our <a href="../blog/steel-edging-cost-austin-tx">steel edging cost guide</a>. More of our built work is on the <a href="../featured">Signature Projects</a> page.</p>""")

build(ROOT, dict(
    slug=SLUG, crumb="Steel Edging", h1="Steel Edging",
    title="Steel Edging Austin TX | 1/4-Inch Welded Steel",
    desc="Red Agave fabricates and installs 1/4-inch steel landscape edging in Austin, TX. Butt-welded joints, welded rebar stakes, and curves bent on site.",
    og_img="https://www.redagaveatx.com/images/projects/east-austin-steel-boulders/steel-edging-boulders-share.webp",
    bg_l="../images/projects/east-austin-steel-boulders/03-finished-steel-edging-boulders-mulch-fern-1200.webp",
    bg_s="../images/projects/east-austin-steel-boulders/03-finished-steel-edging-boulders-mulch-fern-1200.webp",
    answer_h2="Who Installs Steel Landscape Edging in Austin, TX?",
    answer="<strong>Red Agave Landscape</strong> fabricates and installs custom steel landscape edging in Austin, TX from quarter-inch A36 mild steel plate. Every joint is butt-welded on site and ground smooth, so a run of edging is one continuous band of steel. Half-inch rebar stakes are welded to the back of the plate and driven 12 to 18 inches into the ground. We bend the curves on site, cut the steel into boulders, and light the edge with LED strips. We have built in Austin since 2009, and our own crew does the work. Each project starts with a free consultation, and the CAD plan is included. Call or text 512-695-7566.",
    sections=S, faqs=FAQS, cta="Frame Your Landscape in Steel",
    service_name="Custom Steel Landscape Edging", service_type="Steel landscape edging fabrication and installation",
    service_desc="Custom steel landscape edging fabricated and installed in Austin, TX from quarter-inch A36 mild steel plate, with butt-welded joints ground smooth, welded half-inch rebar stakes, curves bent on site, steel cut into boulders, and LED-lit edges. Built by Red Agave's own crew, with a free consultation and the CAD plan included."))

card = ('  <a href="services/' + SLUG + '" class="svc-card rev"><img src="images/gallery/IMG_0991-600.webp" srcset="images/gallery/IMG_0991-600.webp 600w, images/gallery/IMG_0991.webp 1200w" '
        'sizes="(max-width:768px) 80vw, 33vw" alt="Rust-patina steel edging holding a gravel bed of agaves and fountain grass in Austin, TX" loading="lazy"><div class="svc-ov"></div>'
        '<div class="svc-info"><div class="svc-n">{N}</div><div class="svc-name">Steel Edging</div><div class="svc-desc">Quarter-inch steel, welded &amp; bent on site</div></div></a>\n')
if "--register" in sys.argv:
    register(ROOT, SLUG, card, "- Steel landscape edging (quarter-inch A36 mild steel, butt-welded joints, welded rebar stakes, curves bent on site, steel cut into boulders, LED-lit edges): redagaveatx.com/services/" + SLUG, "2026-11-17")

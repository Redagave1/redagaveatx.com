import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svc_lib import build, register, fig, step, sec, H3

ROOT = sys.argv[1]
SLUG = "water-features-austin-tx"
W = "images/projects/se-austin-fire-water/"
PF = "images/services/water-features/"

FAQS = [
    ("Who builds custom water features in Austin, TX?",
     "Red Agave Landscape designs and builds custom water features in Austin in concrete, plaster, steel, and stone. Each one is drawn by the owner after a free on-site consultation and built by our own crew."),
    ("What kinds of water features do you build?",
     "Raised pools with a plaster interior, boulders drilled to run water, open steel channels that carry water to a fall, streams, ponds, and water walls. We also build water into swimming pools: spillover spas, bubblers, laminar jets, and sheer descent waterfalls."),
    ("Does a water feature use a lot of water?",
     "No. A water feature recirculates its water through a pump, so the same water runs through it again and again. The only loss is evaporation, and an autofill valve replaces it."),
    ("Do water features bring mosquitoes?",
     "Standing water breeds mosquitoes, and moving water does not. Every water feature we build has a pump that keeps the water moving."),
    ("What keeps the water clear?",
     "Circulation and filtration. Our round water feature in Southeast Austin runs on a sand pool filter, the same way a swimming pool does."),
    ("What is a drilled boulder fountain?",
     "A natural boulder with a hole drilled through it and a water line run to it, so water comes out of the stone. In Pflugerville we built two, with no hardware in view."),
    ("Can a fire pit go next to a water feature?",
     "Yes. In Southeast Austin a curved steel fire pit follows the front of a round pool, and the flames reflect on the water. In Pflugerville a floating fire pit sits in the same bed as two boulder fountains."),
    ("Does a water feature need electricity?",
     "Yes. Every water feature has a pump, and the pump runs on a dedicated outdoor GFCI circuit. We plan the power with the plumbing, before any concrete is poured."),
    ("Can a water feature be added to a patio I already have?",
     "Yes. In Pflugerville we expanded an existing patio and added two drilled boulder fountains and a floating fire pit beside it."),
    ("What does a water feature cost in Austin?",
     "Every water feature is priced after a free on-site consultation. The type, the size, the rock in the ground, and the distance to power drive the price. Our water feature cost guide lists the ranges by type."),
]

S = ""
S += sec("The Work", "What Water Features Do We Build?", f"""    <p>Water that is drawn with the yard and built from the same materials as the rest of it: concrete, plaster, steel, and stone. These are the forms it takes.</p>
    <table class="cost-table">
      <thead><tr><th>Water Feature</th><th>What It Is</th><th>Where</th></tr></thead><tbody>
      <tr><td>Raised pool</td><td>A concrete shell with a plaster interior and a pool filter, raised above the patio</td><td>Built in Southeast Austin</td></tr>
      <tr><td>Drilled boulder fountain</td><td>A boulder drilled and plumbed so water runs out of the stone</td><td>Built in Pflugerville</td></tr>
      <tr><td>Steel channel</td><td>An open steel channel that carries water from its source to a fall</td><td>Built in Southeast Austin</td></tr>
      <tr><td>Fire beside water</td><td>A steel fire pit set at the edge of the water, so the flames reflect on it</td><td>Built in Southeast Austin and Pflugerville</td></tr>
      <tr><td>Stream and pond</td><td>A pond edged with boulders, with a stream running to a second pond</td><td>On our <a href="../designs">design plans</a></td></tr>
      <tr><td>Water wall</td><td>A sheet of water running down a wall of stone or steel</td><td>Drawn for the site</td></tr>
      <tr><td>Water in a pool</td><td>Spillover spas, bubblers, laminar jets, and sheer descent waterfalls</td><td>Built with the <a href="pools-austin-tx">pool</a></td></tr>
      </tbody></table>
    {fig([(W + "24-water-feature-fire-pits-overview-1200.webp", 1200, 900, "Round raised water feature with a dark cap and black water, fed by a steel channel from a boulder, with a curved steel fire pit burning along its front, in a Southeast Austin backyard")],
         "Southeast Austin: a round raised pool, a steel channel from a boulder, and a curved fire pit along the front.")}
    <p>Fire and water are usually drawn together. See our <a href="fire-pits-austin-tx">custom fire pits</a> page, and our <a href="hardscaping-austin-tx">hardscaping</a> page for the patios and walls around them.</p>""")

S += sec("Built Like a Pool", "How Is a Raised Pool Water Feature Built?", f"""    <p>The same way a swimming pool is built, at a much smaller size. Our round water feature in Southeast Austin has the three parts of a pool:</p>
    <ul>
      <li><strong>Concrete shell:</strong> a round concrete wall, formed and poured in place</li>
      <li><strong>Plaster:</strong> the finished surface inside the shell</li>
      <li><strong>Sand pool filter:</strong> the water circulates through it, the way the water in a swimming pool does</li>
    </ul>
    <p>Each part has a job. The shell holds a true circle and carries the cap on its rim. The plaster gives the inside its finished surface. The filter keeps the water clear.</p>
    <p>The inside is finished black, and that sets the look of the whole space. Black water works like a dark mirror. It reflects the fire in front of it and the evening sky above it.</p>
    {fig([(W + "12-pool-shell-interior-plumbing-800.webp", 800, 1067, "Inside of a round concrete water feature shell with a wall fitting and PVC lines in Southeast Austin"),
          (W + "13-pool-interior-black-800.webp", 800, 1067, "Round water feature shell with the interior finished black beside new concrete pads in Southeast Austin"),
          (W + "15-pool-filled-cap-800.webp", 800, 1067, "Round water feature filled with water as the dark cap is set in sections in Southeast Austin")],
         "The shell with its wall fitting and PVC lines, the interior finished black, and the pool filled while the cap is set.")}
    <p>The full build, from the excavation to the finished yard, is in our post on the <a href="../blog/water-feature-fire-pits-southeast-austin-tx">water feature and fire pits in Southeast Austin</a>. For full-size projects, see our <a href="pools-austin-tx">pool construction</a> and <a href="container-plunge-pools-austin-tx">container plunge pool</a> pages.</p>""", alt=True)

S += sec("The Source", "Where Does the Water Come From?", f"""    <p>From something worth looking at. A water feature has a source and a fall, and both are part of the design.</p>
    <p>In Southeast Austin the source is a boulder with a hole drilled in it. Water comes out of the boulder and into an open steel channel, and the channel carries it to the pool, where it falls to the surface.</p>
    <ul>
      <li><strong>The boulder:</strong> set early, at the same stage as the excavation, because it is part of the structure of the design</li>
      <li><strong>The channel:</strong> open steel, so you watch the water travel before it drops</li>
      <li><strong>The fall:</strong> it moves the black surface, and it is the sound of the space</li>
    </ul>
    {fig([(W + "22-water-feature-channel-fire-top-view-800.webp", 800, 1067, "Water falling from a steel channel into a round black water feature with a dark cap, with a curved steel fire pit burning below, seen from above in Southeast Austin"),
          (W + "25-water-feature-fire-pit-house-800.webp", 800, 1067, "Round raised water feature with a steel channel and a curved fire pit at dusk, with a steel planter and a lawn behind it, in Southeast Austin")],
         "Southeast Austin: water leaves the steel channel and falls to the pool.")}
    <p>The channel is welded steel, like our <a href="steel-edging-austin-tx">steel edging</a> and our <a href="custom-planters-austin-tx">custom steel planters</a>. We cut and weld steel on site.</p>""")

S += sec("Stone", "What Is a Drilled Boulder Fountain?", f"""    <p>A natural boulder with a hole drilled through it and a water line run to it, so water comes out of the stone. There is no spout, no basin on a pedestal, and no hardware in view.</p>
    <p>In <a href="../locations/pflugerville-tx">Pflugerville</a> we built two. The boulders stand on either side of a planting bed beside the patio. They are drilled and plumbed to run water from the top, and mist rises between them.</p>
    <ul>
      <li><strong>Sound without a pond:</strong> the water runs over stone and back into the bed</li>
      <li><strong>Planting right against it:</strong> river fern, creeping Jenny, and horsetail reed grow around the boulders</li>
      <li><strong>Stone below:</strong> river rock fills the bed between the boulders</li>
      <li><strong>Fire in the same bed:</strong> a floating steel fire pit sits beside the fountains</li>
    </ul>
    {fig([(PF + "pflugerville-drilled-boulder-fountain-ferns-800.webp", 800, 600, "Boulders in a bed of river rock with ferns and mist rising between them, beside a steel fire pit and a concrete patio in Pflugerville"),
          (PF + "pflugerville-boulder-fountains-mist-fire-pit-800.webp", 800, 600, "Boulder fountains with mist, ferns, and river rock around a square steel fire pit set on the diagonal, beside concrete patio pads in Pflugerville")],
         "Pflugerville: boulder fountains, ferns, and river rock around a floating fire pit.", wide=True)}
    <p>We work boulders more than one way. We drill them for water, cut slots in them for steel edging, and carve fire pits into them. See <a href="../blog/steel-edging-cut-into-boulders-austin-tx">how we cut steel into boulders</a>, and the <a href="../projects/axehandle">Pflugerville project</a>.</p>""", alt=True)

S += sec("Fire + Water", "Why Put Fire Beside Water?", f"""    <p>Because each one makes the other look better. Water gives the fire a surface to reflect on, and fire gives the water light after dark.</p>
    <p>In Southeast Austin a floating steel fire pit curves along the front of the pool. It sits at the foot of the pool wall, so the flames light the wall and reflect on the water. A second fire pit, a square steel pan, is suspended between two boulders behind the pool.</p>
    <p>Red Agave is the only company in Austin that builds floating welded steel fire pits, and we carve fire pits into boulders.</p>
    {fig([(W + "19-finished-water-feature-fire-pit-dusk-800.webp", 800, 1067, "Round raised water feature with a dark cap, a curved steel fire pit burning in front, and a steel planter behind, at dusk in a Southeast Austin backyard"),
          (PF + "pflugerville-floating-fire-pit-boulders-ferns-800.webp", 800, 1067, "Square steel fire pit burning beside boulders, ferns, and river rock in a planting bed next to concrete patio pads in Pflugerville")],
         "Fire beside water in Southeast Austin, and fire beside the boulder fountains in Pflugerville.")}
    <p>See our post on <a href="../blog/custom-fire-pits-austin-tx">custom fire pits</a>, which shows the plan for the Southeast Austin yard next to the finished fires.</p>""")

S += sec("Clear Water", "What Keeps the Water Clear and Moving?", f"""    <p>A pump, a filter, and a plan for topping it off. A water feature does not use water the way irrigation does. It recirculates the same water.</p>
    <table class="cost-table">
      <thead><tr><th>Part</th><th>What It Does</th></tr></thead><tbody>
      <tr><td>Pump</td><td>Moves the water from the pool or the reservoir back to the source</td></tr>
      <tr><td>Filter</td><td>Cleans the water as it circulates. In Southeast Austin it is a sand pool filter.</td></tr>
      <tr><td>Autofill valve</td><td>Replaces the water lost to evaporation</td></tr>
      <tr><td>Timer</td><td>Runs a fountain or a pondless feature for 12 to 16 hours a day. A pond with fish runs all day.</td></tr>
      <tr><td>GFCI circuit</td><td>A dedicated outdoor circuit for the pump</td></tr>
      </tbody></table>
    <p>Moving water is also the answer to mosquitoes. Standing water breeds them, and moving water does not. Every water feature we build has a pump that keeps the surface in motion.</p>
    <p>The upkeep is simple: clear leaves from the water, clean the pump intake, and check the water level in summer.</p>""", alt=True)

S += sec("Austin Conditions", "What Does a Water Feature Need in Austin?", f"""    <p>A plan for heat, rock, and dry years. Each one changes how a water feature is designed here.</p>
    <table class="cost-table">
      <thead><tr><th>Austin Condition</th><th>What We Plan For</th></tr></thead><tbody>
      <tr><td>Summer heat</td><td>An open pond loses 1 to 2 inches of water a week in an Austin summer. An autofill valve keeps the level steady.</td></tr>
      <tr><td>Limestone</td><td>Parts of West Austin, Westlake Hills, and the Hill Country sit on shallow limestone. We check the depth of the rock before the design is set, and plan machine access for the dig.</td></tr>
      <tr><td>Dry years</td><td>A feature that recirculates uses far less water than the same area of lawn. A reservoir under gravel loses less to the sun than open water.</td></tr>
      <tr><td>Runoff</td><td>Rain is carried around the water feature, not into it. <a href="drainage-austin-tx">Drainage</a> is planned with the hardscape.</td></tr>
      <tr><td>Power</td><td>The circuit for the pump is run before the patio is poured.</td></tr>
      </tbody></table>
    <p>A water feature is small next to a lawn. It suits a <a href="xeriscape-austin-tx">xeriscape</a> yard, where gravel, boulders, and native plants do the rest of the work.</p>""")

S += sec("On Paper First", "How Do We Design a Water Feature?", f"""    <p>On the plan, with everything around it. A water feature is drawn with the patio, the fire, the planting, and the lighting, so the pipes and the power are settled before any concrete is poured.</p>
    <p>The Southeast Austin yard was drawn this way. The plan put a round water feature at the corner of the patio, fed by a channel from a boulder, with two fire pits set against boulders and a dark gravel court.</p>
    {fig([("images/designs/water-feature-fire-pits-plan-900.webp", 900, 652, "Landscape design plan drawn over an aerial view of a house, showing a round water feature fed by a channel from a boulder, two fire pits set against boulders, concrete pads, and a dark gravel court in Southeast Austin")],
         "The plan for the Southeast Austin yard: the round water feature, the channel from the boulder, and the two fire pits.")}
    <p>Other plans put water to different uses:</p>
    <ul>
      <li><strong>A side yard built around water:</strong> a square pad with a narrow channel of water through its center, a pond edged with boulders above it, and a stream running to a second pond below</li>
      <li><strong>Water troughs:</strong> two small water features, each set at the edge of a planting bed beside a deck</li>
    </ul>
    <p>Every design is drawn by the owner after a free on-site consultation. See them on our <a href="../designs">design plans</a> page, and read about our <a href="landscape-design-austin-tx">landscape design</a>.</p>""", alt=True)

S += sec("The Build", "How Is a Water Feature Built?", f"""    <p>In the order that keeps the pipes under the concrete and the stone in the right place. These are the steps from our Southeast Austin build.</p>
    {step(1, "Consultation and Plan", "We walk the yard with you, and the owner draws the plan. The consultation is free, and the CAD plan is included.")}
    {step(2, "Dig and Set the Boulders", "We excavate, set the steel edging, and place the boulders. Boulders go in early, because they are part of the structure of the design.")}
    {step(3, "Form and Pour", "The shell is formed and poured in place. When the forms come off, the wall stands as one piece of concrete.")}
    {step(4, "Plumb and Wire", "PVC lines run to the shell, with a fitting set through the wall. The line to the source and the power for the pump go in now.")}
    {step(5, "Finish", "The interior is plastered, and the outside of the wall is finished smooth. The cap is set on the rim.")}
    {step(6, "Fill, Run, and Light", "The feature is filled and the pump is started. Then the patio, the planting, and the <a href=\"landscape-lighting-austin-tx\">lighting</a> are finished around it.")}""")

S += sec("Choosing", "Which Water Feature Fits Your Yard?", f"""    <p>The one that matches how you use the space. Start with what you want from the water.</p>
    <table class="cost-table">
      <thead><tr><th>You Want</th><th>Consider</th></tr></thead><tbody>
      <tr><td>Sound, with the least upkeep</td><td>A drilled boulder fountain or a pondless waterfall, where the water returns to a hidden reservoir</td></tr>
      <tr><td>A still, dark mirror</td><td>A raised pool finished black inside</td></tr>
      <tr><td>A modern line</td><td>A steel channel, or a water wall</td></tr>
      <tr><td>Something for a small space</td><td>A single drilled boulder in a bed of river rock</td></tr>
      <tr><td>Water on a slope</td><td>A stream that runs down the grade to a pond or a hidden reservoir</td></tr>
      <tr><td>Fish and water plants</td><td>A pond with a waterfall and a pump that runs all day</td></tr>
      <tr><td>A center for the patio at night</td><td>Fire beside water</td></tr>
      </tbody></table>
    <p>Our <a href="../blog/water-feature-cost-austin-tx">water feature cost guide</a> compares the types and what drives the price of each.</p>""", alt=True)

S += sec("Built Work", "Where Have We Built Water Features?", f"""    <ul>
      <li><strong>Southeast Austin:</strong> a round raised pool with a concrete shell, a plaster interior finished black, and a sand pool filter, fed from a drilled boulder by a steel channel, with two steel fire pits. See <a href="../blog/water-feature-fire-pits-southeast-austin-tx">the build</a>.</li>
      <li><strong><a href="../locations/pflugerville-tx">Pflugerville</a>:</strong> two drilled boulder fountains in a fern bed beside an expanded patio, with a floating fire pit. See <a href="../projects/axehandle">the project</a>.</li>
      <li><strong>Pools across Austin:</strong> water built into the pool itself. See our <a href="pools-austin-tx">pools</a> page.</li>
    </ul>
    <p>We build across the Austin area, from <a href="../locations/westlake-hills-tx">Westlake Hills</a> and <a href="../locations/lakeway-tx">Lakeway</a> to <a href="../locations/buda-kyle-tx">Buda and Kyle</a>. More of our built work is on the <a href="../featured">Signature Projects</a> page.</p>""")

build(ROOT, dict(
    slug=SLUG, crumb="Water Features", h1="Water Features",
    title="Water Features Austin TX | Custom Design & Build",
    desc="Red Agave designs and builds custom water features in Austin, TX: plaster pools, drilled boulder fountains, steel channels, and fire beside water.",
    og_img="https://www.redagaveatx.com/images/projects/se-austin-fire-water/24-water-feature-fire-pits-overview-share.webp",
    bg_l="../images/projects/se-austin-fire-water/24-water-feature-fire-pits-overview-1200.webp",
    bg_s="../images/projects/se-austin-fire-water/19-finished-water-feature-fire-pit-dusk-800.webp",
    answer_h2="Who Builds Custom Water Features in Austin, TX?",
    answer="<strong>Red Agave Landscape</strong> designs and builds custom water features in Austin, TX in concrete, plaster, steel, and stone. We build raised pools with a plaster interior, boulders drilled to run water, open steel channels that carry water to a fall, and fire pits set beside the water. In Southeast Austin we built a round water feature the way a swimming pool is built, with a concrete shell, a plaster interior, and a sand pool filter. We have built in Austin since 2009. Every design is drawn by the owner and built by our own crew. Each project starts with a free consultation, and the CAD plan is included. Call or text 512-695-7566.",
    sections=S, faqs=FAQS, cta="Design Your Water Feature",
    service_name="Custom Water Features", service_type="Water feature design and construction",
    service_desc="Custom water features designed and built in Austin, TX in concrete, plaster, steel, and stone: raised pools with a plaster interior and a pool filter, drilled boulder fountains, steel water channels, streams, ponds, water walls, and fire pits beside water. Built by Red Agave's own crew, with a free consultation and the CAD plan included."))

card = ('  <a href="services/' + SLUG + '" class="svc-card rev"><img src="images/projects/se-austin-fire-water/19-finished-water-feature-fire-pit-dusk-800.webp" '
        'sizes="(max-width:768px) 80vw, 33vw" alt="Round raised water feature with a curved steel fire pit burning in front at dusk in Southeast Austin, TX" loading="lazy"><div class="svc-ov"></div>'
        '<div class="svc-info"><div class="svc-n">{N}</div><div class="svc-name">Water Features</div><div class="svc-desc">Plaster pools, drilled boulders &amp; steel channels</div></div></a>\n')
if "--register" in sys.argv:
    register(ROOT, SLUG, card, "- Water features (raised pools with a concrete shell, a plaster interior and a pool filter, drilled boulder fountains, steel water channels, streams, ponds, water walls, fire beside water): redagaveatx.com/services/" + SLUG, "2026-11-18")

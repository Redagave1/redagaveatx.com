"""Lawn service page.

FACT NOTE (2026-11-20): Jensen confirmed "we mow". The site says what we offer (the Specialty Services list on
services.html, about.html, llms.txt) but not how a visit is scheduled or what one visit includes, so this page
does not say either. The mowing heights, the seasons, and the soil advice are the site's own lawn guides.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svc_lib import build, register, fig, step, sec, H3
from svc_extra import check, AREAS, STANDING

ROOT = sys.argv[1]
SLUG = "lawn-service-austin-tx"
P = "images/projects/"
L = P + "svc-lawn-service-austin-tx/"

FAQS = [
    ("Does Red Agave mow lawns?",
     "Yes. Red Agave Landscape is a design-build landscaper first, and we also mow. Lawn service is still part of what we do in Austin, TX. Call or text (512) 695-7566."),
    ("What lawn services do you offer in Austin?",
     "Lawn service, mulching, aerating, sod cutting, sod installation, and tree trimming. We also build the steel edging that keeps a lawn out of the beds."),
    ("How high should St. Augustine grass be cut in Austin?",
     "3.5 to 4 inches in summer. That is the highest setting on most mowers. Taller grass shades the soil and keeps the roots cooler."),
    ("How high should Bermuda grass be cut in Austin?",
     "1.5 to 2 inches in summer, at the higher end in extreme heat."),
    ("How often does a lawn need mowing in an Austin summer?",
     "By the grass. Bermuda is mowed every 5 to 7 days, St. Augustine and Zoysia every 7 to 10 days, and buffalo grass every 10 to 14 days. No mowing should take more than one third of the blade."),
    ("When should a lawn be aerated in Austin?",
     "Late September through mid-October, with core aeration. Aeration works once the soil has enough organic matter to hold the holes open, so compost comes first on a tired lawn."),
    ("Why is my grass thinning?",
     "Five stresses thin Austin lawns: slope, tree roots, shade, low nutrients, and soil with little microbial life. Each one has its own fix, and more fertilizer alone does not solve any of them."),
    ("How often can I water my lawn in Austin?",
     "Under Austin Water's Conservation Stage, in effect since September 2, 2025, automatic sprinklers run one day a week: Thursday for even addresses and Wednesday for odd, midnight to 10 a.m. or 7 p.m. to midnight. Hose-end sprinklers get two days, and hand watering is allowed any time."),
    ("What keeps grass out of the planting beds?",
     "Steel edging. We weld quarter-inch steel plate into one continuous edge between the lawn and the bed, and it is thick enough to be driven over by a mower without showing it."),
    ("What does lawn service cost in Austin?",
     "Call or text (512) 695-7566 for a lawn service quote. For new sod, our sod installation cost guide explains what drives the price."),
]

S = ""
S += sec("The Work", "Do We Mow?", f"""    <p>Yes. We are designers and builders first, and we also mow. Lawn service is still part of what we do.</p>
    <p>These are the lawn and yard services we offer.</p>
    <table class="cost-table">
      <thead><tr><th>Service</th><th>What It Covers</th></tr></thead><tbody>
      <tr><td>Lawn service</td><td>Mowing, maintenance, and care</td></tr>
      <tr><td>Mulching</td><td>Beds and borders</td></tr>
      <tr><td>Aerating</td><td>Soil health</td></tr>
      <tr><td>Sod cutting</td><td>Removal and prep</td></tr>
      <tr><td>Sod installation</td><td>Bermuda, Zoysia, and St. Augustine</td></tr>
      <tr><td>Tree trimming</td><td>Shaping and removal</td></tr>
      </tbody></table>
    {fig([(L + "lawn-steel-edged-beds-gravel-fire-court-1200.webp", 1200, 900, "Green lawn framed by steel-edged planting beds and a river rock path, behind a dark gravel court with a concrete fire pit and white chairs")],
         "A lawn framed by steel-edged beds, a river rock path, and a gravel fire court.")}
    <p>The same company builds the rest of the yard. See everything we build on our <a href="hardscaping-austin-tx">hardscaping</a> page and our <a href="design-build-austin-tx">design-build</a> page.</p>""")

S += sec("Mowing Height", "How High Should Austin Grass Be Cut?", f"""    <p>Higher than most lawns are cut. Taller grass shades the soil, slows evaporation, and keeps the roots 10 to 15 degrees cooler than scalped turf.</p>
    <table class="cost-table">
      <thead><tr><th>Grass</th><th>Summer Height</th><th>Summer Mowing</th></tr></thead><tbody>
      <tr><td>St. Augustine</td><td>3.5 to 4 inches</td><td>Every 7 to 10 days</td></tr>
      <tr><td>Bermuda</td><td>1.5 to 2 inches</td><td>Every 5 to 7 days</td></tr>
      <tr><td>Zoysia</td><td>2.5 to 3 inches</td><td>Every 7 to 10 days</td></tr>
      <tr><td>Buffalo grass</td><td>3 to 4 inches</td><td>Every 10 to 14 days</td></tr>
      </tbody></table>
    <p>One rule covers every grass: never remove more than one third of the blade in a single mowing. If St. Augustine has reached 6 inches and the target is 4, it is cut to 4.5 first and mowed again three or four days later. Scalping exposes the soil to direct sun.</p>
    <p>Our guide to <a href="../blog/summer-landscaping-austin-tx">keeping a yard alive in an Austin summer</a> covers heat stress and what not to do in the hot months.</p>""", alt=True)

S += sec("Grass Types", "Which Grass Is in Your Lawn?", f"""    <p>Sun decides first, and water decides second. Most Austin lawns are Bermuda, Zoysia, or St. Augustine, and each is cared for differently.</p>
    <table class="cost-table">
      <thead><tr><th>Grass</th><th>Sun</th><th>Character</th></tr></thead><tbody>
      <tr><td>Bermuda</td><td>Full sun, 6 hours or more</td><td>The most heat and drought tolerant. Handles heavy traffic. Dormant in winter.</td></tr>
      <tr><td>Zoysia</td><td>4 hours or more</td><td>Dense and carpet-like. Slower growing, so less mowing.</td></tr>
      <tr><td>St. Augustine</td><td>Partial shade</td><td>Thick and lush. Needs more water than Bermuda.</td></tr>
      </tbody></table>
    <p>We lay all three as sod, on soil that is amended and graded first. See our <a href="turf-installation-austin-tx">turf installation</a> page.</p>
    {fig([(L + "lawn-grass-black-steel-planter-800.webp", 800, 1067, "Thick lawn grass growing up to the face of a black steel planter holding an agave, beside a concrete walk with river rock"),
          (L + "lawn-beside-concrete-pavers-800.webp", 800, 1067, "Lawn meeting a patio of large concrete pavers with gravel joints beside a stone house")],
         "Lawn against a black steel planter, and lawn beside a patio of concrete pavers.")}""")

S += sec("Thin Lawns", "Why Does a Lawn Thin Out?", f"""    <p>For a reason you can name. Grass does not thin at random. In Central Texas it recedes from five stresses.</p>
    <table class="cost-table">
      <thead><tr><th>Stress</th><th>What Happens</th><th>What Helps</th></tr></thead><tbody>
      <tr><td>Slope</td><td>Rain runs off and takes topsoil with it</td><td>Compost on the slope, and watering in short repeated cycles</td></tr>
      <tr><td>Tree roots</td><td>Roots take the water and the top 6 to 8 inches of soil</td><td>Mulch, decomposed granite, or shade groundcover inside the drip line</td></tr>
      <tr><td>Shade</td><td>Grass is a sun plant. St. Augustine and Zoysia need 4 to 6 hours of sun to stay dense.</td><td>Selective thinning of the canopy, or shade plants</td></tr>
      <tr><td>Low nutrients</td><td>Soil here is alkaline, pH 7.5 to 8.5, and low in organic matter</td><td>Compost and natural fertilizer</td></tr>
      <tr><td>Little soil life</td><td>Compacted soil sheds water and crusts over</td><td>Compost first, then aeration</td></tr>
      </tbody></table>
    <p>The fix starts with the soil. A half-inch layer of compost raked into the turf, once in spring and once in fall, rebuilds the organic layer. A natural fertilizer such as MicroLife 6-2-4 feeds the soil as well as the grass.</p>
    <p>Aeration comes after that. Core aeration pulls plugs of soil to open channels for air, water, and roots. In soil with no organic matter the holes collapse within days, so compost goes down first. Our post on <a href="../blog/why-grass-thins-austin-tx">why grass thins in Austin</a> has the full sequence, and our <a href="../blog/alkaline-soil-fix-austin-tx">alkaline soil guide</a> explains the pH.</p>""", alt=True)

S += sec("Water", "How Is a Lawn Watered Under Austin's Rules?", f"""    <p>On one sprinkler day a week. Austin Water's Conservation Stage has been in effect since September 2, 2025.</p>
    <table class="cost-table">
      <thead><tr><th>Watering</th><th>Austin Water Rule</th></tr></thead><tbody>
      <tr><td>Automatic sprinklers</td><td>One day a week: Thursday for even addresses, Wednesday for odd</td></tr>
      <tr><td>Hours</td><td>Midnight to 10 a.m., or 7 p.m. to midnight</td></tr>
      <tr><td>Hose-end sprinklers and drip</td><td>Two days a week</td></tr>
      <tr><td>Hand watering</td><td>Any time</td></tr>
      </tbody></table>
    <p>One day is enough when the water soaks in. On clay, each zone is run for 10 to 12 minutes, left for 30 to 60 minutes to absorb, and run again. A screwdriver pushed into the soil after watering should slide in to 6 inches.</p>
    <p>See our guide to <a href="../blog/austin-water-restrictions-landscaping">Austin water restrictions</a>. Round Rock, Cedar Park, and the other cities around Austin set their own days: see our <a href="../locations/round-rock-tx">Round Rock</a> and <a href="../locations/cedar-park-tx">Cedar Park</a> pages.</p>""")

S += sec("Edges", "What Keeps the Edge of a Lawn Clean?", f"""    <p>Steel. An edge between the lawn and the bed keeps the grass out of the gravel and the mulch out of the grass.</p>
    <p>Most edging sold for landscapes is plastic or thin steel, and a mower bends it. We weld quarter-inch steel plate into one continuous band. It is thick enough to be driven over by a mower without showing it. Bermuda in particular spreads into beds that have no steel edge.</p>
    <p>See our <a href="steel-edging-austin-tx">steel edging</a> page.</p>""", alt=True)

S += sec("Mulch", "Why Mulch the Beds Around a Lawn?", f"""    <p>Because mulch does four jobs at once. Three to four inches of hardwood mulch in the beds:</p>
    <ul>
      <li><strong>Cools the soil:</strong> by 10 to 20 degrees compared with open soil</li>
      <li><strong>Holds water:</strong> it cuts evaporation by 50 to 70 percent</li>
      <li><strong>Stops weeds:</strong> seeds under it do not germinate</li>
      <li><strong>Feeds the soil:</strong> it breaks down and improves the clay over time</li>
    </ul>
    <p>Mulch is kept 3 to 4 inches back from tree trunks and plant stems. When it has broken down below 2 inches, it is topped up before summer.</p>""")

S += sec("The Year", "What Does an Austin Lawn Need Each Season?", f"""    <p>The work changes with the heat. This is the lawn year in Austin.</p>
    <table class="cost-table">
      <thead><tr><th>Season</th><th>The Lawn</th></tr></thead><tbody>
      <tr><td>Spring</td><td>March and April are a window for sod and for aeration. Compost goes down.</td></tr>
      <tr><td>Summer</td><td>The mower is raised. Watering follows the allowed day. No new sod, no heavy fertilizer, and no aeration in the heat.</td></tr>
      <tr><td>Early fall</td><td>Late September through mid-October is the window for core aeration, and for sod.</td></tr>
      <tr><td>October</td><td>Bermuda is overseeded with perennial ryegrass for winter color in mid-October. The winterizer feeding follows late in the month.</td></tr>
      <tr><td>Winter</td><td>Bermuda goes dormant after the first frost. The average first frost in Austin is November 28.</td></tr>
      </tbody></table>
    <p>Our <a href="../blog/fall-landscaping-austin-tx">fall landscaping guide</a> has the month-by-month list.</p>""", alt=True)

S += sec("Less Lawn", "When Is Grass the Wrong Answer?", f"""    <p>Where it will not grow. Under a dense live oak, on a steep slope, or in a narrow strip a mower cannot reach, the answer is a different surface.</p>
    <ul>
      <li><strong>Under trees:</strong> mulch, decomposed granite, or shade groundcover inside the drip line</li>
      <li><strong>Hot, dry ground:</strong> native beds, gravel, and boulders. See our <a href="xeriscape-austin-tx">xeriscape</a> page.</li>
      <li><strong>Shade, dog runs, and side yards:</strong> artificial turf. See our comparison of <a href="../blog/artificial-turf-vs-real-grass-austin-tx">artificial turf and real grass</a>.</li>
    </ul>
    <p>Not every yard needs to lose its lawn. Kids need a place to run, and dogs need a place to play. We keep lawn where it gets used and replace it where it struggles.</p>""")

S += sec("Reviews", "What Do Customers Say About Our Lawn Service?", f"""    <p>Reviews of our lawn service go back to 2015. Customers write that we were quick and professional on a mowing job before an event, that we stepped in when another provider went out of business, and that we have kept one family's lawn since they bought their first home.</p>
    <p>Read them on our <a href="../reviews">reviews</a> page.</p>
    {AREAS}
    {STANDING}
    <p>For new grass, see our <a href="../blog/sod-installation-cost-austin-tx">sod installation cost guide</a>. More of our built work is on the <a href="../featured">Signature Projects</a> page.</p>""", alt=True)

ANSWER = ("<strong>Red Agave Landscape</strong> mows and cares for lawns in Austin, TX. "
          "We are designers and builders first, and we also mow. "
          "Our lawn and yard services are lawn service, mulching, aerating, sod cutting, sod installation, and tree trimming, "
          "and we build the quarter-inch steel edging that keeps a lawn out of the beds. "
          "We have worked in Austin since 2009, with 4.8 stars across 87 Google reviews. "
          "Call or text 512-695-7566.")
check(S, ANSWER, *[q + " " + a for q, a in FAQS])

build(ROOT, dict(
    slug=SLUG, crumb="Lawn Service", h1="Lawn Service",
    title="Lawn Service Austin TX | Mowing & Lawn Care",
    desc="Red Agave mows and cares for lawns in Austin, TX: lawn service, mulching, aerating, sod, and steel-edged beds. In Austin since 2009.",
    og_img="https://www.redagaveatx.com/images/projects/svc-lawn-service-austin-tx/lawn-steel-edged-beds-gravel-fire-court-1200.webp",
    bg_l="../images/projects/svc-lawn-service-austin-tx/lawn-steel-edged-beds-gravel-fire-court-1200.webp",
    bg_s="../images/projects/svc-lawn-service-austin-tx/lawn-steel-edged-beds-gravel-fire-court-800.webp",
    answer_h2="Who Offers Lawn Service in Austin, TX?",
    answer=ANSWER,
    sections=S, faqs=FAQS, cta="Get Your Lawn in Shape",
    service_name="Lawn Service", service_type="Lawn mowing and lawn care",
    service_desc="Lawn service in Austin, TX from Red Agave Landscape: lawn mowing and care, mulching, aerating, sod cutting, sod installation in Bermuda, Zoysia, and St. Augustine, tree trimming, and quarter-inch steel edging between lawn and beds."))

card = ('  <a href="services/' + SLUG + '" class="svc-card rev"><img src="images/projects/svc-lawn-service-austin-tx/lawn-steel-edged-beds-gravel-fire-court-800.webp" '
        'sizes="(max-width:768px) 80vw, 33vw" alt="Green lawn framed by steel-edged beds and a gravel fire court" loading="lazy"><div class="svc-ov"></div>'
        '<div class="svc-info"><div class="svc-n">{N}</div><div class="svc-name">Lawn Service</div><div class="svc-desc">Mowing, mulching, aerating &amp; sod</div></div></a>\n')
if "--register" in sys.argv:
    register(ROOT, SLUG, card, "- Lawn service (lawn mowing and care, mulching, aerating, sod cutting, sod installation, tree trimming): redagaveatx.com/services/" + SLUG, "2026-11-20")

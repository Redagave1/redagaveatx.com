"""Irrigation service page. NOT BUILT until the two constants below are filled in.

Texas rule 30 TAC 344.70 requires every advertisement for irrigation services to show the licensed irrigator's
license number, in the form LI plus seven digits. This page is an advertisement for irrigation services, so it
shows the irrigator's name and license number in a credentials line under the answer block, again in the last
section of the page, in the first and last FAQ, and in the Service schema.

To build: fill in IRRIGATOR_NAME and IRRIGATOR_LICENSE, then
    python3 -I .claude/service-pages/make_irrigation.py . [--register]

Facts: only what the site already says about drip irrigation, sprinklers, watering rules, and rebates.
The Austin Water rules are the ones verified for the Great Hills page (Conservation Stage since 2025-09-02).
Recheck every utility's current stage before publishing, because stages change.
Photos: the repo has one photo that shows irrigation hardware (a valve box in a gravel bed). Ask Jensen for
photos of drip going in, a valve manifold, and a controller.
"""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

IRRIGATOR_NAME = ""       # full name of the Texas licensed irrigator, as it appears on the TCEQ license
IRRIGATOR_LICENSE = ""    # "LI" plus seven digits, for example LI0012345

if not IRRIGATOR_NAME.strip() or not re.fullmatch(r"LI\d{7}", IRRIGATOR_LICENSE.strip()):
    sys.exit("make_irrigation.py: NOT BUILT. Set IRRIGATOR_NAME and IRRIGATOR_LICENSE (LI plus seven digits) at the top of "
             "this script. Texas rule 30 TAC 344.70 requires the licensed irrigator's license number on every advertisement "
             "for irrigation services, and this page is one. No page was written.")

from svc_lib import build, register, fig, step, sec, H3
from svc_extra import check, AREAS, STANDING

ROOT = sys.argv[1]
SLUG = "irrigation-austin-tx"
P = "images/projects/"
NAME, LIC = IRRIGATOR_NAME.strip(), IRRIGATOR_LICENSE.strip()
CRED = f"Licensed irrigator: {NAME}, Texas license {LIC}"

FAQS = [
    ("Who installs irrigation systems in Austin, TX?",
     f"Red Agave Landscape installs drip irrigation, sprinkler systems, and smart irrigation controllers in Austin, TX, as part of the landscapes we design and build. {CRED}. Every project starts with a free consultation, and the CAD plan is included."),
    ("Do you install drip irrigation?",
     "Yes. We put planting beds and steel planters on drip. Drip delivers water to the root zone of each plant through emitters or soaker tubing, with no overspray and no runoff."),
    ("Do you install sprinkler systems?",
     "Yes. We install sprinkler systems and retrofit existing ones. When we lay sod, we install the irrigation zones with it, so the grass establishes and survives its first summer."),
    ("How many days a week can I water in Austin?",
     "Under Austin Water's Conservation Stage, in effect since September 2, 2025, automatic sprinklers run one day a week: Thursday for even addresses and Wednesday for odd, midnight to 10 a.m. or 7 p.m. to midnight. Hand watering is allowed any time."),
    ("Does drip irrigation get more watering days in Austin?",
     "Yes. Austin Water allows drip irrigation and hose-end sprinklers two days a week, where automatic sprinklers get one."),
    ("How should clay soil be watered?",
     "In cycles. Each zone is run for 10 to 12 minutes, left for 30 to 60 minutes to absorb, and run again. That keeps the water from running off the clay."),
    ("How much water does new sod need in Austin?",
     "Twice a day for 15 to 20 minutes for the first 2 to 3 weeks. Then once a day for 2 weeks, then a deep watering every 3 to 4 days. After 6 weeks, follow the normal Austin watering rules."),
    ("Do you install smart irrigation controllers?",
     "Yes. We install smart irrigation controllers that adjust to the weather."),
    ("Does a xeriscape need irrigation?",
     "A xeriscape gets zone-specific drip irrigation for establishment watering. After establishment, most native plants need no irrigation."),
    ("Who is your licensed irrigator?",
     f"{NAME}, Texas licensed irrigator {LIC}."),
]

S = ""
S += sec("The Work", "What Irrigation Do We Install?", f"""    <p>The watering a landscape needs, drawn on the same plan as the planting. We install three things.</p>
    <table class="cost-table">
      <thead><tr><th>System</th><th>What It Waters</th></tr></thead><tbody>
      <tr><td>Drip irrigation</td><td>Planting beds, steel planters, and new native plants while they establish</td></tr>
      <tr><td>Sprinkler systems</td><td>Lawns. We install new systems and retrofit existing ones.</td></tr>
      <tr><td>Smart controllers</td><td>The whole system. A smart controller adjusts to the weather.</td></tr>
      </tbody></table>
    <p>Irrigation is part of our design-build work. Our crew handles the stone, the carpentry, the planting, the irrigation, the steel, and the lighting on the same job.</p>
    {fig([(P + "svc-irrigation-austin-tx/valve-box-gravel-bed-steel-planters-1100.webp", 1100, 919, "Round green valve box lid set flush in a steel-edged bed of dark gravel planted with variegated succulents and ferns, with river rock around the bed and a lawn behind")],
         "A valve box set flush in the gravel of a steel-edged bed.")}
    <p>See our <a href="design-build-austin-tx">design-build</a> and <a href="landscape-design-austin-tx">landscape design</a> pages.</p>""")

S += sec("Drip", "Why Put Beds on Drip?", f"""    <p>Because drip waters the plant and nothing else. A drip line delivers water to the root zone of each plant through emitters or soaker tubing.</p>
    <ul>
      <li><strong>No overspray:</strong> no water on the patio, the fence, or the driveway</li>
      <li><strong>No runoff:</strong> the water goes into the soil at the root</li>
      <li><strong>Less water:</strong> drip uses 30 to 50 percent less water than spray heads</li>
      <li><strong>Zones by need:</strong> each zone is timed on its own, so a dry bed and a thirsty bed are not watered alike</li>
      <li><strong>More days:</strong> Austin Water allows drip two days a week, where automatic sprinklers get one</li>
    </ul>
    <p>A lawn sprinkler waters everything the same. Native plants that are overwatered develop root rot, so beds and lawn belong on separate zones. Our <a href="../blog/low-maintenance-landscaping-austin-tx">low-maintenance landscaping guide</a> covers zoning by water need.</p>""", alt=True)

S += sec("Austin Water", "What Are Austin's Watering Rules?", f"""    <p>One sprinkler day and two drip days. Austin Water's Conservation Stage has been in effect since September 2, 2025.</p>
    <table class="cost-table">
      <thead><tr><th>Watering</th><th>Austin Water Rule</th></tr></thead><tbody>
      <tr><td>Automatic sprinklers</td><td>One day a week: Thursday for even addresses, Wednesday for odd</td></tr>
      <tr><td>Hours</td><td>Midnight to 10 a.m., or 7 p.m. to midnight</td></tr>
      <tr><td>Drip irrigation and hose-end sprinklers</td><td>Two days a week</td></tr>
      <tr><td>Hand watering</td><td>Any time</td></tr>
      </tbody></table>
    <p>We design to those rules. Beds go on drip so they get both drip days, and lawn is kept to the part of the yard that gets used. See our guide to <a href="../blog/austin-water-restrictions-landscaping">Austin water restrictions</a>.</p>""")

S += sec("Other Cities", "What About the Cities Around Austin?", f"""    <p>Each utility sets its own days. These are the schedules on our city pages.</p>
    <table class="cost-table">
      <thead><tr><th>City</th><th>Schedule</th></tr></thead><tbody>
      <tr><td><a href="../locations/round-rock-tx">Round Rock</a></td><td>Sprinklers and drip two days a week by address, before 10 a.m. or after 7 p.m.</td></tr>
      <tr><td><a href="../locations/cedar-park-tx">Cedar Park</a></td><td>Two days a week by address, before 10 a.m. or after 7 p.m. Stage 3 cuts that to one day.</td></tr>
      <tr><td><a href="../locations/georgetown-tx">Georgetown</a></td><td>Stage 1: two set days a week, never on Mondays, and never between 9 a.m. and 7 p.m.</td></tr>
      <tr><td><a href="../locations/bee-cave-tx">Bee Cave</a></td><td>Stage 1 of the West Travis County Public Utility Agency: two days a week, 7 p.m. to 10 a.m., with no Sunday watering</td></tr>
      <tr><td><a href="../locations/buda-kyle-tx">Kyle</a></td><td>Stage 3: sprinklers once a week by address, 8 p.m. to 5 a.m., and drip once a week, 7 p.m. to 10 a.m.</td></tr>
      <tr><td><a href="../locations/buda-kyle-tx">Buda</a></td><td>Stage 3 since November 4, 2024: once a week, 7 to 11 a.m. or 7 to 11 p.m.</td></tr>
      </tbody></table>
    <p>The current stage is posted on each city's website.</p>""", alt=True)

S += sec("Clay and Trees", "How Is Water Put Down on Clay, and Around Oaks?", f"""    <p>Slowly on clay, and never on a trunk.</p>
    <ul>
      <li><strong>Cycle and soak:</strong> each zone is run for 10 to 12 minutes, left for 30 to 60 minutes to absorb, and run again. That keeps water from running off the clay.</li>
      <li><strong>Depth:</strong> a screwdriver pushed into the soil after watering should slide in to 6 inches.</li>
      <li><strong>Oaks:</strong> irrigation spray is kept off the trunks of heritage oaks, and the critical root zone is protected.</li>
    </ul>
    <p>See our <a href="../locations/tarrytown-tx">Tarrytown</a> page for building under oaks.</p>""")

S += sec("New Sod", "How Is New Sod Watered?", f"""    <p>Often at first, then deeper and less often.</p>
    <table class="cost-table">
      <thead><tr><th>When</th><th>Watering</th></tr></thead><tbody>
      <tr><td>First 2 to 3 weeks</td><td>Twice a day, 15 to 20 minutes</td></tr>
      <tr><td>Next 2 weeks</td><td>Once a day</td></tr>
      <tr><td>After that</td><td>A deep watering every 3 to 4 days</td></tr>
      <tr><td>After 6 weeks</td><td>The normal Austin watering rules</td></tr>
      </tbody></table>
    <p>When we lay sod, we install the irrigation zones with it. See our <a href="turf-installation-austin-tx">turf installation</a> page.</p>""", alt=True)

S += sec("Upkeep", "What Does an Irrigation System Need Each Year?", f"""    <p>A walk through every zone. A system that is out of adjustment wastes water and leaves dry spots.</p>
    <ul>
      <li><strong>Run each zone and walk the yard:</strong> look for broken heads, misaligned nozzles, and dry spots.</li>
      <li><strong>Watch for runoff:</strong> water on the sidewalk means a shorter run time and a cycle-and-soak delay.</li>
      <li><strong>Replace worn nozzles:</strong> a head that sprays mist has a worn nozzle.</li>
      <li><strong>Check the drip zones:</strong> clear clogged emitters and look for damaged line.</li>
      <li><strong>Check the controller:</strong> the right day, inside the allowed hours.</li>
      <li><strong>Add a rain sensor:</strong> it keeps the system from running during and after rain.</li>
    </ul>
    <p>Run times come down in fall. Cool soil holds water longer, so the schedule is cut by 20 to 30 percent in October and by 40 to 50 percent in November. See our <a href="../blog/fall-landscaping-austin-tx">fall landscaping guide</a>.</p>""")

S += sec("No Irrigation", "When Does a Yard Need No Irrigation?", f"""    <p>When the planting lives on rain. A xeriscape gets zone-specific drip for establishment watering, and after establishment most native plants need none.</p>
    <p>In Dripping Springs, where lots run on wells and cisterns, we design for no permanent irrigation. A landscape with no permanent irrigation is not affected by any drought stage. See our <a href="xeriscape-austin-tx">xeriscape</a> page and our <a href="../locations/dripping-springs-tx">Dripping Springs</a> page.</p>""", alt=True)

S += sec("Rebates", "Does Austin Water Offer Rebates?", f"""    <p>Yes, two that touch irrigation.</p>
    <ul>
      <li><strong>WaterWise Landscape Rebate:</strong> for replacing irrigated turf with water-efficient landscaping.</li>
      <li><strong>WaterWise Rainscape Rebate:</strong> for features that capture and hold rainwater on site, such as rain gardens.</li>
    </ul>
    <p>Current terms are on <a href="https://www.austintexas.gov/water/rebates-tools-programs" target="_blank" rel="noopener">Austin Water's rebates page</a>. See our <a href="drainage-austin-tx">drainage</a> page for rain gardens.</p>""")

S += sec("License", "Who Is Our Licensed Irrigator?", f"""    <p><strong>{CRED}.</strong></p>
    {AREAS}
    {STANDING}
    <p>More of our built work is on the <a href="../featured">Signature Projects</a> page.</p>
    <p style="font-size:12px;letter-spacing:.3px;color:var(--cream60)">Red Agave Landscape &middot; {CRED}</p>""", alt=True)

ANSWER = ("<strong>Red Agave Landscape</strong> installs drip irrigation, sprinkler systems, and smart irrigation controllers in Austin, TX, "
          "as part of the landscapes we design and build. Planting beds go on drip, which Austin Water allows two days a week. "
          "Lawns go on sprinkler zones, which Austin Water allows one day a week. "
          "We have built in Austin since 2009, and our own crew does the work. "
          "Each project starts with a free consultation, and the CAD plan is included. Call or text 512-695-7566."
          f"</p><p style=\"font-size:12px;letter-spacing:.3px;color:var(--cream60);margin-top:14px\"><strong>{CRED}</strong>")
check(S, ANSWER, *[q + " " + a for q, a in FAQS])
assert S.count(LIC) >= 2 and LIC in ANSWER and NAME in ANSWER, "the irrigator's name and license number must show in the credentials line and at the foot of the page"

build(ROOT, dict(
    slug=SLUG, crumb="Irrigation", h1="Irrigation",
    title="Irrigation Austin TX | Drip & Sprinkler Systems",
    desc=f"Red Agave installs drip irrigation and sprinkler systems in Austin, TX, designed for Austin Water's rules. Licensed irrigator {LIC}.",
    og_img="https://www.redagaveatx.com/images/projects/svc-irrigation-austin-tx/valve-box-gravel-bed-steel-planters-1100.webp",
    bg_l="../images/projects/svc-irrigation-austin-tx/valve-box-gravel-bed-steel-planters-1100.webp",
    bg_s="../images/projects/svc-irrigation-austin-tx/valve-box-gravel-bed-steel-planters-800.webp",
    answer_h2="Who Installs Irrigation Systems in Austin, TX?",
    answer=ANSWER,
    sections=S, faqs=FAQS, cta="Water the Yard You Have",
    service_name="Landscape Irrigation", service_type="Drip irrigation and sprinkler system installation",
    service_desc=f"Drip irrigation, sprinkler systems, and smart irrigation controllers installed in Austin, TX as part of landscapes designed and built by Red Agave Landscape. {CRED}."))

card = ('  <a href="services/' + SLUG + '" class="svc-card rev"><img src="images/projects/svc-irrigation-austin-tx/valve-box-gravel-bed-steel-planters-800.webp" '
        'sizes="(max-width:768px) 80vw, 33vw" alt="Valve box set flush in a steel-edged gravel bed in Austin, TX" loading="lazy"><div class="svc-ov"></div>'
        '<div class="svc-info"><div class="svc-n">{N}</div><div class="svc-name">Irrigation</div><div class="svc-desc">Drip, sprinklers &amp; smart controllers &middot; ' + LIC + '</div></div></a>\n')
if "--register" in sys.argv:
    register(ROOT, SLUG, card, "- Irrigation (drip irrigation, sprinkler system installation and retrofits, smart controllers; " + CRED + "): redagaveatx.com/services/" + SLUG, "2026-11-20")

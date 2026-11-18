"""Builds projects/chrysler-bend.html (Signature Project 09, the Southeast Austin floating triangle planter).
Shell (head CSS, header, footer, scripts) comes from projects/dormarion.html.
Run: python3 -I .claude/service-pages/make_chrysler_bend.py .
"""
import re, json, html, os, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
SLUG = "chrysler-bend"
URL = f"https://www.redagaveatx.com/projects/{SLUG}"
IMG = "../images/projects/southeast-austin-triangle-planter/"
ABS = "https://www.redagaveatx.com/images/projects/southeast-austin-triangle-planter/"
TITLE = "Floating Triangle Planter, Southeast Austin | Red Agave"
DESC = "Southeast Austin front yard by Red Agave: terraced steel beds with a custom light rim, a floating triangle planter, century agave, and basalt gravel."
BANNED = ["bare steel", "—", "&mdash;", " may ", " might ", "not sure", "uncertain", "we think", "probably", "it depends", "subcontract", "butcher",
          "design fee", "$", "Corten", "neighbor", "Southern Love", "Blazyk", "Hopeland", "Flycatcher", "Fly Catcher", "Axehandle",
          "Dormarion", "Riverview", "Madison", "Ulit", "Silhouette", "Allison"]

def pic(name, alt, sizes="(max-width:900px) 100vw, 50vw", cls="", extra=""):
    c = f' class="{cls}"' if cls else ""
    return (f'<img loading="lazy"{c}{extra} src="{IMG}{name}-1125.webp" srcset="{IMG}{name}-800.webp 800w, {IMG}{name}-1125.webp 1125w" '
            f'sizes="{sizes}" alt="{html.escape(alt, quote=True)}">')

A = {
 "hero": "Floating triangle steel planter with a variegated century agave at dusk, lit from its rim above basalt gravel, with terraced steel beds running to the front door, in Southeast Austin",
 "09": "Black triangle steel planter with a variegated century agave floating above terraced steel beds of basalt gravel, with the light rim glowing along the outside of the steel, in Southeast Austin",
 "12": "Close view of the angle iron rim of a floating steel triangle planter, with light falling on basalt gravel and silver santolina below, in Southeast Austin",
 "11": "Terraced black steel beds of basalt gravel stepping toward a front door, with a floating triangle planter and a light rim along the outside edge, in Southeast Austin",
 "10": "Side view of a black welded steel triangle planter with an angle iron rim, holding a variegated century agave and silver ponyfoot above basalt gravel, in Southeast Austin",
 "06": "Steel triangle planter before its black penetrating sealer, seen from the side, tapering to a point on one post above a raised steel bed in Southeast Austin",
 "02": "Welded steel triangle planter before its black penetrating sealer, on its post in a raised steel bed, with a second bed lined with landscape fabric beside it, in Southeast Austin",
 "z14": "Close view of the corner where two black steel beds meet, with the light rim washing warm light down the steel onto the lawn and basalt gravel inside the bed, in Southeast Austin",
 "z15": "Variegated century agave with silver ponyfoot in a black triangle steel planter, seen from above, with silver santolina in basalt gravel and steel beds stepping away behind it, in Southeast Austin",
 "z16": "Close view of basalt gravel and a silver santolina inside a black steel bed, lit warm from the rim of the planter above, in Southeast Austin",
 "sk": "Design sketch of a black triangle steel planter holding a blue agave on raised black steel beds that step toward a front door, with lawn in front, drawn over the front of a house in Southeast Austin",
}

FAQS = [
 ("What is a floating planter?",
  "A planter held off the ground, with open space under it. This one is a welded steel triangle shaped like an upside-down pyramid, carried on one post above a terraced steel bed."),
 ("What is a light rim?",
  "A steel rim with the light hidden under it. On this project a custom light rim runs around the outside of the terraced steel, and an angle iron light rim circles the planter. You see the glow on the gravel and the lawn, and the light itself stays out of sight."),
 ("What is planted in the floating triangle planter?",
  "One variegated century agave, with silver ponyfoot trailing around its base. Three silver santolina grow under the planter, with maiden grass and artichoke agave in the terraced beds. Every bed is finished in basalt gravel."),
 ("How is the steel finished black?",
  "With a black penetrating sealer. The planter and the beds were cut and welded first, and the sealer went on after."),
 ("Who designed and built it?",
  "Red Agave Landscape. The yard was drawn by the owner of Red Agave, and it was built by our own crew."),
 ("Do you build floating planters and lit steel beds across Austin?",
  "Yes. Red Agave Landscape designs and builds across the Austin area. Every project starts with a free consultation, and the CAD plan is included."),
]

BODY = f"""<body>
<div id="cur"></div><div id="cur-ring"></div>
<header class="hdr">
  <a href="../" class="hdr-brand">RED AGAVE</a>
  <nav class="hdr-nav">
    <a href="../featured">Work</a>
    <a href="../">Studio</a>
    <a href="../contact">Contact</a>
  </nav>
</header>

<!-- 1. THRESHOLD HERO -->
<section class="thr">
  <a href="../featured" class="thr-back t-eyebrow">All Work</a>
  <div class="thr-media">
    <img class="thr-img" fetchpriority="high" src="{IMG}13-floating-triangle-planter-dusk-1125.webp" srcset="{IMG}13-floating-triangle-planter-dusk-800.webp 800w, {IMG}13-floating-triangle-planter-dusk-1125.webp 1125w" sizes="100vw" alt="{A['hero']}">
  </div>
  <div class="thr-scrim"></div>
  <div class="thr-inner">
    <div class="thr-top">
      <div class="thr-locator">
        <span class="line-mask" data-delay="1"><span class="t-eyebrow with-line">Project / 09</span></span>
        <span class="line-mask" data-delay="2"><span class="t-eyebrow">Southeast Austin, Texas</span></span>
      </div>
      <span class="line-mask" data-delay="3"><span class="thr-num">09</span></span>
    </div>
    <div class="thr-bottom">
      <h1 class="line-mask" data-delay="2"><span class="thr-title thr-title-2">Chrysler Bend</span></h1>
      <div class="thr-meta line-mask" data-delay="4">
        <span class="t-eyebrow">Residence &middot; Southeast Austin, TX</span>
        <span class="t-eyebrow">Terraced steel &middot; Light rim &middot; Angle iron &middot; Basalt gravel</span>
      </div>
    </div>
  </div>
  <div class="thr-scroll"><span class="t-eyebrow t-pulse">Scroll</span></div>
</section>

<!-- 2. STICKY NARRATIVE -->
<section class="nar">
  <div class="nar-grid">
    <aside class="nar-left">
      <div class="nar-sticky">
        <span class="line-mask"><span class="t-eyebrow with-line">Design Intent &middot; Southeast Austin</span></span>
        <h2 class="line-mask" data-delay="1"><span class="nar-title">One agave, held above the ground. Light under every rim.</span></h2>
        <span class="line-mask" data-delay="2"><span class="ps-pulse" style="margin-top:6px">Steel &middot; Angle Iron &middot; Basalt &middot; Light</span></span>
        <div class="nar-body">
          <p class="line-mask" data-delay="3"><span>Red Agave Landscape designed and built this front yard in Southeast Austin: terraced black steel beds with a custom light rim around the exterior, and a floating triangle planter above them. The planter is welded steel shaped like an upside-down pyramid. It is carried on one post, and a variegated century agave grows in it.</span></p>
          <p class="line-mask" data-delay="4"><span>The beds step toward the front door. Each one is steel set on edge, sealed with a black penetrating sealer, and filled with basalt gravel. The light rim runs around the outside of the steel. The light sits under the rim, out of sight, and washes down the black face onto the ground. At dusk the steel reads as a dark band with a warm line of light under it.</span></p>
          <p class="line-mask" data-delay="5"><span>The planter has an angle iron rim, and its light rim is angle iron too. The light shines down on the basalt, so the planter looks like it hangs above the rock. Silver ponyfoot trails around the agave, and three silver santolina grow under the edge of the planter. In the beds, maiden grass and <a href="../blog/artichoke-agave-austin-tx" style="text-decoration:underline;text-underline-offset:3px">artichoke agave</a> grow in the gravel.</span></p>
        </div>
      </div>
    </aside>
    <div class="nar-right">
      <figure class="nar-fig nar-fig-1">
        <div class="clip-media has-parallax">{pic("09-terraced-steel-light-rim-triangle-planter", A["09"])}</div>
        <figcaption class="nar-fig-cap"><span class="t-eyebrow t-pulse n">01 &middot; Light Rim</span><span class="t-eyebrow">Terraced steel / light on the lawn</span></figcaption>
      </figure>
      <figure class="nar-fig nar-fig-2">
        <div class="clip-media has-parallax">{pic("12-angle-iron-rim-light-basalt-gravel", A["12"])}</div>
        <figcaption class="nar-fig-cap"><span class="t-eyebrow t-pulse n">02 &middot; Angle Iron</span><span class="t-eyebrow">Planter rim / light on basalt</span></figcaption>
      </figure>
      <figure class="nar-fig nar-fig-3">
        <div class="clip-media has-parallax">{pic("11-terraced-steel-beds-toward-front-door", A["11"])}</div>
        <figcaption class="nar-fig-cap"><span class="t-eyebrow t-pulse n">03 &middot; Terraces</span><span class="t-eyebrow">Steel beds stepping to the front door</span></figcaption>
      </figure>
      <figure class="nar-fig nar-fig-4">
        <div class="clip-media has-parallax">{pic("10-floating-triangle-planter-angle-iron-rim-side", A["10"])}</div>
        <figcaption class="nar-fig-cap"><span class="t-eyebrow t-pulse n">04 &middot; Planting</span><span class="t-eyebrow">Century agave / silver ponyfoot</span></figcaption>
      </figure>
    </div>
  </div>
</section>

<!-- 3. KINETIC SHOWCASE -->
<div class="psc-wrap">
  <div class="psc-head">
    <span class="line-mask"><span class="t-eyebrow with-line">The Build</span></span>
    <h2 class="line-mask" data-delay="1"><span>Cut, welded, floated. <em>Southeast Austin.</em></span></h2>
  </div>

  <section class="psc-stack" data-psc-stack>
    <div class="stk-base"><img loading="lazy" class="stk-base-img" src="{IMG}06-tapered-triangle-planter-profile-bare-steel-1200.webp" alt="{A['06']}"></div>
    <div class="stk-top"><img loading="lazy" class="stk-top-img" src="{IMG}02-triangle-planter-welded-steel-bed-800.webp" alt="{A['02']}"></div>
    <div class="stk-label">
      <span class="ps-mask-wrap"><span class="ps-mask-text ps-eyebrow">Steel &middot; 01</span></span>
      <span class="ps-mask-wrap"><span class="ps-mask-text ps-cream">On One Post</span></span>
      <span class="ps-mask-wrap"><span class="ps-mask-text ps-pulse">June &middot; Before the Sealer</span></span>
      <span class="ps-mask-wrap"><span class="ps-mask-text ps-mono">In June the planter and the beds stood in steel, before the black penetrating sealer. Three plates are welded into a point, and the point sits on one post in the middle of the bed. The second bed is lined with landscape fabric.</span></span>
    </div>
  </section>
</div>

<!-- Mid statement -->
<section class="psc-statement">
  <div class="line-mask"><span class="psc-statement-line">Light Under Every Rim</span></div>
  <div class="line-mask" data-delay="1"><span class="psc-statement-sub">Black steel. <em>Basalt below.</em></span></div>
</section>

<!-- PINNED MASK REVEAL -->
<div class="psc-pin-outer" id="pin-outer">
  <div class="psc-pin" id="pin-track">
    <div class="psc-pin-frame">
      <img loading="lazy" class="pin-img is-on" data-pin-img="0" src="{IMG}14-zoom-light-rim-steel-corner-1125.webp" srcset="{IMG}14-zoom-light-rim-steel-corner-800.webp 800w, {IMG}14-zoom-light-rim-steel-corner-1125.webp 1125w" sizes="(max-width:900px) 100vw, 88vw" alt="{A['z14']}">
      <img loading="lazy" class="pin-img" data-pin-img="1" src="{IMG}15-zoom-century-agave-silver-ponyfoot-1125.webp" srcset="{IMG}15-zoom-century-agave-silver-ponyfoot-800.webp 800w, {IMG}15-zoom-century-agave-silver-ponyfoot-1125.webp 1125w" sizes="(max-width:900px) 100vw, 88vw" alt="{A['z15']}">
      <img loading="lazy" class="pin-img" data-pin-img="2" src="{IMG}16-zoom-basalt-gravel-steel-bed-1125.webp" srcset="{IMG}16-zoom-basalt-gravel-steel-bed-800.webp 800w, {IMG}16-zoom-basalt-gravel-steel-bed-1125.webp 1125w" sizes="(max-width:900px) 100vw, 88vw" alt="{A['z16']}">
      <div class="psc-pin-scrim"></div>

      <div class="psc-pin-stage is-active" data-pin-stage="0">
        <div class="ps-mask-wrap"><div class="ps-mask-text ps-eyebrow">Night &middot; 01</div></div>
        <div class="ps-mask-wrap"><h3 class="ps-mask-text ps-cream">Light Rim</h3></div>
        <div class="ps-mask-wrap"><span class="ps-mask-text ps-pulse">Angle Iron &middot; Warm Light</span></div>
        <div class="ps-mask-wrap"><p class="ps-mask-text ps-mono">A custom light rim runs around the outside of the terraced steel. A second one, made of angle iron, circles the planter. The light sits under the steel, out of sight. At dusk the basalt glows warm and the black steel stands out above it.</p></div>
      </div>
      <div class="psc-pin-stage" data-pin-stage="1">
        <div class="ps-mask-wrap"><div class="ps-mask-text ps-eyebrow">Planting &middot; 02</div></div>
        <div class="ps-mask-wrap"><h3 class="ps-mask-text ps-cream">Agave and Silver</h3></div>
        <div class="ps-mask-wrap"><span class="ps-mask-text ps-pulse">Century Agave &middot; Ponyfoot &middot; Santolina</span></div>
        <div class="ps-mask-wrap"><p class="ps-mask-text ps-mono">One variegated century agave fills the triangle, with silver ponyfoot trailing around its base. Silver santolina, maiden grass, and artichoke agave grow in the beds, in basalt gravel. An agave holds its shape all year and takes full sun.</p></div>
      </div>
      <div class="psc-pin-stage" data-pin-stage="2">
        <div class="ps-mask-wrap"><div class="ps-mask-text ps-eyebrow">Ground &middot; 03</div></div>
        <div class="ps-mask-wrap"><h3 class="ps-mask-text ps-cream">Basalt</h3></div>
        <div class="ps-mask-wrap"><span class="ps-mask-text ps-pulse">Dark Gravel &middot; Black Steel</span></div>
        <div class="ps-mask-wrap"><p class="ps-mask-text ps-mono">Every bed is finished in basalt gravel, held by the black steel. Under the light rim the dark rock turns warm, and the silver santolina stands out against it.</p></div>
      </div>

      <div class="psc-pin-bar">
        <span id="pin-counter">01 / 03</span>
        <div class="psc-pin-bar-progress" id="pin-progress"></div>
        <span>Scroll to advance</span>
      </div>
    </div>
  </div>
</div>

<!-- 4. BLUEPRINT -->
<section class="bp">
  <div class="bp-inner">
    <div class="bp-head">
      <span class="line-mask"><span class="t-eyebrow with-line">Takeoff</span></span>
      <h2 class="line-mask" data-delay="1"><span class="bp-title">The <em>blueprint</em>.</span></h2>
    </div>
    <figure class="bp-sketch">
      <img loading="lazy" src="../images/designs/floating-triangle-planter-sketch.webp" srcset="../images/designs/floating-triangle-planter-sketch-900.webp 900w, ../images/designs/floating-triangle-planter-sketch.webp 1600w" sizes="(max-width:900px) 100vw, 700px" width="1600" height="1219" alt="{A['sk']}">
      <figcaption>
        <span class="bp-chap-eb">00 / Design</span>
        <span class="bp-chap-h">The Sketch</span>
        <span class="bp-sketch-p">The sketch is drawn over the front of the house, so it shows the planter where it stands: below the front window, with lawn in front. The built yard follows the drawing. One thing changed. The agave in the drawing is blue, and the one we planted is variegated.</span>
        <a class="bp-sketch-a" href="../designs">More design plans &rarr;</a>
      </figcaption>
    </figure>
    <div class="bp-chapters">
      <div class="bp-chap">
        <div class="bp-chap-eb">01 / Steel</div>
        <div class="bp-chap-h">Terraces + Planter</div>
        <ul>
          <li>Terraced black steel beds</li>
          <li>Beds step toward the front door</li>
          <li>Floating triangle planter</li>
          <li>Three plates welded to a point</li>
          <li>One post under the point</li>
          <li>Angle iron rim</li>
          <li>Black penetrating sealer</li>
        </ul>
      </div>
      <div class="bp-chap">
        <div class="bp-chap-eb">02 / Lighting</div>
        <div class="bp-chap-h">Light Rims</div>
        <ul>
          <li>Custom light rim around the terraces</li>
          <li>Angle iron light rim on the planter</li>
          <li>Light hidden under the steel</li>
          <li>Warm wash on basalt and lawn</li>
        </ul>
      </div>
      <div class="bp-chap">
        <div class="bp-chap-eb">03 / Ground</div>
        <div class="bp-chap-h">Basalt</div>
        <ul>
          <li>Basalt gravel in every bed</li>
          <li>Landscape fabric lining</li>
          <li>Lawn in front</li>
        </ul>
      </div>
      <div class="bp-chap">
        <div class="bp-chap-eb">04 / Plant Palette</div>
        <div class="bp-chap-h">Agave + Silver</div>
        <ul>
          <li>Variegated century agave</li>
          <li>Silver ponyfoot</li>
          <li>Silver santolina</li>
          <li>Maiden grass</li>
          <li>Artichoke agave</li>
        </ul>
      </div>
    </div>
    <div class="bp-meta">
      <div class="bp-meta-cell"><div class="bp-meta-lbl">Steel</div><div class="bp-meta-val">Terraced &middot; Floating</div></div>
      <div class="bp-meta-cell"><div class="bp-meta-lbl">Signature</div><div class="bp-meta-val">Triangle Planter</div></div>
      <div class="bp-meta-cell"><div class="bp-meta-lbl">Lighting</div><div class="bp-meta-val">Custom Light Rim</div></div>
      <div class="bp-meta-cell"><div class="bp-meta-lbl">Stone</div><div class="bp-meta-val">Basalt Gravel</div></div>
    </div>
  </div>
</section>

<!-- 5. PROJECT NOTES -->
<section class="pn">
  <div class="pn-inner">
    <span class="line-mask"><span class="t-eyebrow with-line">Project Notes</span></span>
    <h2 class="pn-title">Questions about this build</h2>
{"".join(f'''    <details>
      <summary>{html.escape(q, quote=False)}</summary>
      <div class="pn-a">{html.escape(a, quote=False)}</div>
    </details>
''' for q, a in FAQS)}    <div class="pn-links">
      <a href="../blog/floating-triangle-steel-planter-austin-tx">Sketch, build, and finish</a>
      <a href="../blog/tapered-steel-planter-austin-tx">How the taper is welded</a>
      <a href="../services/custom-planters-austin-tx">Custom steel planters</a>
      <a href="../services/landscape-lighting-austin-tx">Landscape lighting</a>
      <a href="../services/steel-edging-austin-tx">Steel edging</a>
      <a href="../designs">Design plans</a>
      <a href="../contact">Free consultation</a>
    </div>
  </div>
</section>

<!-- 6. HORIZON: NEXT PROJECT -->
<a class="hz" href="dormarion" id="hz-link">
  <div class="hz-media"><img loading="lazy" src="../images/projects/dormarion/IMG_6319.webp" alt="Cantilevered steel planters with a lit address sign at a front entry in Tarrytown, Austin TX"></div>
  <div class="hz-scrim"></div>
  <div class="hz-inner">
    <span class="t-eyebrow with-line">Next / 08</span>
    <div>
      <h2 class="hz-title hz-title-2">Cantilevered <em>Steel.</em></h2>
      <span class="hz-action t-eyebrow t-pulse">Continue the journey</span>
    </div>
  </div>
</a>
<div id="hz-wipe"></div>
"""

CSS_ADD = """
.thr-title-2{font-size:clamp(76px,15vw,230px)}
.thr-img{object-position:50% 36%}
.hz-title-2{font-size:clamp(84px,13vw,220px)}
.bp-sketch{display:grid;grid-template-columns:1.5fr 1fr;gap:52px;align-items:end;margin:0 0 60px}
.bp-sketch img{width:100%;height:auto;border:1px solid var(--line);background:#fff}
.bp-sketch figcaption{display:flex;flex-direction:column;padding-bottom:6px}
.bp-sketch .bp-chap-eb{display:block}.bp-sketch .bp-chap-h{display:block}
.bp-sketch-p{font-size:13px;line-height:1.85;color:rgba(26,26,26,.75);max-width:44ch}
.bp-sketch-a{margin-top:22px;font-size:10px;letter-spacing:3px;text-transform:uppercase;color:var(--bronze);font-weight:500;align-self:flex-start;border-bottom:1px solid rgba(160,122,74,.4);padding-bottom:4px}
.pn{background:var(--dark2);padding:150px 0}
.pn-inner{max-width:1080px;margin:0 auto;padding:0 48px}
.pn-title{font-family:'Bebas Neue',Impact,sans-serif;font-size:clamp(44px,5vw,76px);line-height:.92;letter-spacing:2px;color:var(--cream);margin:22px 0 44px;font-weight:400}
.pn details{border-top:1px solid rgba(201,168,76,.14)}
.pn details:last-of-type{border-bottom:1px solid rgba(201,168,76,.14)}
.pn summary{list-style:none;padding:22px 0;font-size:12px;font-weight:500;letter-spacing:2px;text-transform:uppercase;color:var(--cream);display:flex;justify-content:space-between;align-items:center;gap:24px;line-height:1.6}
.pn summary::-webkit-details-marker{display:none}
.pn summary::after{content:'+';color:var(--gold-pulse);font-weight:300;font-size:18px;line-height:1}
.pn details[open] summary::after{content:'\\2212'}
.pn summary:focus-visible{outline:1px solid var(--gold-pulse);outline-offset:4px}
.pn-a{padding:0 0 26px;max-width:70ch;font-size:14px;line-height:1.85;color:rgba(240,234,214,.62);font-weight:300}
.pn-links{display:flex;flex-wrap:wrap;gap:12px;margin-top:52px}
.pn-links a{border:1px solid rgba(201,168,76,.2);color:var(--gold);padding:10px 22px;font-size:10px;letter-spacing:2px;text-transform:uppercase;transition:border-color .3s,color .3s}
.pn-links a:hover{border-color:var(--gold-pulse);color:var(--gold-pulse)}
@media(max-width:900px){.pn{padding:84px 0}.pn-inner{padding:0 22px}.thr-meta{gap:14px}.bp-sketch{grid-template-columns:1fr;gap:26px;margin-bottom:44px}}
"""

def main():
    s = open(f"{ROOT}/projects/dormarion.html", encoding="utf-8").read()
    head = s[:s.index("</head>")]
    foot = s[s.index("<footer"):]
    css = re.search(r"<style>(.*?)</style>", head, re.S)
    e = lambda x: html.escape(x, quote=True)
    article = {"@context": "https://schema.org", "@type": "Article",
               "headline": "Chrysler Bend: Floating Triangle Planter and Terraced Steel in Southeast Austin, TX",
               "description": "Terraced steel beds finished in a black penetrating sealer with a custom light rim around the exterior, a floating welded steel triangle planter with an angle iron rim and an angle iron light rim, a variegated century agave, silver ponyfoot, silver santolina, maiden grass, artichoke agave, and basalt gravel. Designed and built by Red Agave Landscape.",
               "image": [ABS + "floating-triangle-project-share.webp", ABS + "13-floating-triangle-planter-dusk-1125.webp", ABS + "09-terraced-steel-light-rim-triangle-planter-1125.webp"],
               "datePublished": "2026-11-18", "dateModified": "2026-11-18",
               "author": {"@type": "Organization", "name": "Red Agave Landscape", "url": "https://www.redagaveatx.com"},
               "publisher": {"@type": "Organization", "name": "Red Agave Landscape", "url": "https://www.redagaveatx.com"},
               "mainEntityOfPage": URL, "locationCreated": {"@type": "Place", "name": "Southeast Austin, TX"}}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.redagaveatx.com/"},
        {"@type": "ListItem", "position": 2, "name": "Signature Projects", "item": "https://www.redagaveatx.com/featured"},
        {"@type": "ListItem", "position": 3, "name": "Chrysler Bend", "item": URL}]}
    ld = lambda d: '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False) + "</script>"
    pre = head[:head.index("<title>")]
    fonts = re.search(r'<link rel="preconnect" href="https://fonts.googleapis.com">.*?</noscript>', head, re.S).group(0)
    new_head = (pre + f"<title>{e(TITLE)}</title>\n"
        f'<meta name="description" content="{e(DESC)}">\n'
        f'<link rel="canonical" href="{URL}">\n'
        f'<link rel="preload" as="image" href="{IMG}13-floating-triangle-planter-dusk-1125.webp" imagesrcset="{IMG}13-floating-triangle-planter-dusk-800.webp 800w, {IMG}13-floating-triangle-planter-dusk-1125.webp 1125w" imagesizes="100vw" fetchpriority="high">\n'
        + fonts + "\n"
        f'<meta property="og:title" content="Chrysler Bend: Floating Triangle Planter and Terraced Steel | Red Agave">\n'
        f'<meta property="og:description" content="{e(DESC)}">\n'
        f'<meta property="og:image" content="{ABS}floating-triangle-project-share.webp">\n'
        f'<meta property="og:url" content="{URL}">\n'
        '<meta property="og:type" content="article">\n<meta property="og:site_name" content="Red Agave Landscape">\n<meta name="twitter:card" content="summary_large_image">\n'
        + ld(article) + "\n<style>" + css.group(1) + CSS_ADD + "</style>\n" + ld(faq) + "\n" + ld(crumbs) + "\n")
    out = new_head + "</head>\n" + BODY + "\n" + foot
    open(f"{ROOT}/projects/{SLUG}.html", "w", encoding="utf-8").write(out)

    txt = html.unescape(re.sub(r"<[^>]+>", " ", BODY))
    words = len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’/-]*", txt))
    print("title", len(TITLE), "| desc", len(DESC), "| words", words, "| h1", out.count("<h1"), "| h2", out.count("<h2"), "| imgs", BODY.count("<img"))
    visible = (re.sub(r'(?:href|src|srcset)="[^"]*"', "", BODY) + TITLE + DESC + json.dumps(article) + json.dumps(faq)).lower()
    hits = [w for w in BANNED if w.lower() in visible]
    print("banned hits:", hits); assert not hits, hits
    miss = []
    for h in re.findall(r'(?:href|src)="([^"#]+)"', BODY) + [u.split(" ")[0] for ss in re.findall(r'srcset="([^"]+)"', BODY) for u in ss.split(", ")]:
        if h.startswith(("http", "sms:", "tel:", "mailto:")): continue
        p = os.path.normpath(os.path.join(ROOT, "projects", h))
        if not (os.path.exists(p) or os.path.exists(p + ".html") or os.path.isdir(p)): miss.append(h)
    print("missing targets:", miss); assert not miss
    for d in re.findall(r'<script type="application/ld\+json">(.*?)</script>', out, re.S): json.loads(d)
    assert len(TITLE) <= 60 and 120 <= len(DESC) <= 155, "title/desc length"
    print("json-ld ok; bytes", len(out.encode()))

main()

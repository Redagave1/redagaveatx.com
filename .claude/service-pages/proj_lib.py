"""Shared builder for project pages in the Chrysler Bend layout (made from make_chrysler_bend.py).

One script per page passes a spec to build():

    python3 -I .claude/service-pages/make_southeast_austin_water_feature.py .

Shell (head CSS, header, footer, scripts) comes from projects/dormarion.html, as for Chrysler Bend.
Zoom-in bands, 800-wide copies and share images are cut by cut_project_zooms.py.

Two tiers (Jensen, 2026-11-20):
- signature: spec has "num" ("10"). Back link and breadcrumb go to /featured. Add a card and an ItemList entry in featured.html.
- regular: no "num". Back link and breadcrumb go to /projects/. The word "signature" is refused anywhere on the page.
  List it on /projects/ with an "external": true entry in .claude/regular-projects/projects.json.

Sections, in order: hero, narrative (answer-first paragraph and figures), build stacks (optional), statement,
pinned zoom-ins, blueprint (optional sketch, "what was built" lists), project notes (FAQ and links), next project.
The FAQ schema is made from the visible FAQ text, so they always match.

Checks: title 60 or under, description 120 to 155, banned wording, internal job names, missing links and images,
".html" in links, empty alt text, one h1, valid JSON-LD.
"""
import re, json, html, os

SITE = "https://www.redagaveatx.com"
BANNED = ["bare steel", "raw steel", "—", "&mdash;", "–", "&ndash;", " may ", " might ", "not sure", "uncertain", "we think", "probably",
          "it depends", "perhaps", "possibly", "likely", " seems ", "appears to", "subcontract", "butcher", "design fee", "$", "Corten",
          "neighbor", "Southern Love", "Google Business", "warranty", "Blazyk", "Hopeland", "Flycatcher", "Fly Catcher", "Axehandle",
          "Dormarion", "Riverview", "Madison", "Ulit", "Silhouette", "Allison"]
# pages built by the scripts in this folder; a link to one of these is allowed before the file exists
PLANNED = {"southeast-austin-water-feature", "south-austin-screened-room", "east-austin-steel-edging-boulders",
           "pool-ipe-deck-bamboo-screen", "boulder-stream-steel-fire-trough", "courtyard-stream-japanese-maple",
           "triangle-fire-pit-stock-tank-pool"}

esc = lambda x: html.escape(x, quote=True)
ld = lambda d: '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False) + "</script>"


def IM(alt, *files):
    """An image. files are (site-relative path, width) pairs, smallest first; the last one is the default src."""
    assert files and alt.strip()
    return {"alt": alt, "files": list(files)}


def _src(im): return "../" + im["files"][-1][0]
def _set(im): return ", ".join(f"../{p} {w}w" for p, w in im["files"])


def tag(im, sizes, cls="", lazy=True, extra=""):
    c = f' class="{cls}"' if cls else ""
    l = ' loading="lazy"' if lazy else ""
    ss = f' srcset="{_set(im)}" sizes="{sizes}"' if len(im["files"]) > 1 else ""
    return f'<img{l}{c}{extra} src="{_src(im)}"{ss} alt="{esc(im["alt"])}">'


CSS_ADD = """
.thr-title-x{font-size:clamp(40px,7vw,118px);line-height:.92;max-width:1280px;text-wrap:balance;padding-top:.05em}
.thr-inner{padding-bottom:118px}
.hz-title-2{font-size:clamp(72px,12vw,210px)}
.nar-body a{text-decoration:underline;text-underline-offset:3px}
.bp-sketch{display:grid;grid-template-columns:1.5fr 1fr;gap:52px;align-items:end;margin:0 0 60px}
.bp-sketch img{width:100%;height:auto;border:1px solid var(--line);background:#fff}
.bp-sketch figcaption{display:flex;flex-direction:column;padding-bottom:6px}
.bp-sketch .bp-chap-eb{display:block}.bp-sketch .bp-chap-h{display:block}
.bp-sketch-p{font-size:13px;line-height:1.85;color:rgba(26,26,26,.75);max-width:44ch}
.bp-sketch-a{margin-top:22px;font-size:10px;letter-spacing:3px;text-transform:uppercase;color:var(--bronze);font-weight:500;align-self:flex-start;border-bottom:1px solid rgba(160,122,74,.4);padding-bottom:4px}
.psc-stack + .psc-stack{margin-top:60px}
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
@media(min-width:901px){.bp-n3{grid-template-columns:repeat(3,1fr)}.bp-n2{grid-template-columns:repeat(2,1fr)}}
@media(max-width:900px){.pn{padding:84px 0}.pn-inner{padding:0 22px}.thr-meta{gap:14px}.bp-sketch{grid-template-columns:1fr;gap:26px;margin-bottom:44px}.psc-stack + .psc-stack{margin-top:0}}
"""


def _hero(sp, sig):
    back = '<a href="../featured" class="thr-back t-eyebrow">All Work</a>' if sig else '<a href="./" class="thr-back t-eyebrow">All Projects</a>'
    first = f'Project / {sp["num"]}' if sig else "Project"
    num = f'\n      <span class="line-mask" data-delay="3"><span class="thr-num">{sp["num"]}</span></span>' if sig else ""
    return f"""<!-- 1. THRESHOLD HERO -->
<section class="thr">
  {back}
  <div class="thr-media">
    {tag(sp["hero"], "100vw", cls="thr-img", lazy=False, extra=' fetchpriority="high"')}
  </div>
  <div class="thr-scrim"></div>
  <div class="thr-inner">
    <div class="thr-top">
      <div class="thr-locator">
        <span class="line-mask" data-delay="1"><span class="t-eyebrow with-line">{first}</span></span>
        <span class="line-mask" data-delay="2"><span class="t-eyebrow">{sp["place"]}</span></span>
      </div>{num}
    </div>
    <div class="thr-bottom">
      <h1 class="line-mask" data-delay="2"><span class="thr-title thr-title-x">{sp["h1"]}</span></h1>
      <div class="thr-meta line-mask" data-delay="4">
        <span class="t-eyebrow">{sp["meta_a"]}</span>
        <span class="t-eyebrow">{sp["kicker"]}</span>
      </div>
    </div>
  </div>
  <div class="thr-scroll"><span class="t-eyebrow t-pulse">Scroll</span></div>
</section>
"""


def _narrative(sp):
    paras = "".join(f'          <p class="line-mask" data-delay="{i}"><span>{p}</span></p>\n' for i, p in enumerate(sp["paras"], 3))
    figs = ""
    for i, f in enumerate(sp["figs"], 1):
        ratio = f' style="aspect-ratio:{f["ratio"]}"' if f.get("ratio") else ""
        figs += f'''      <figure class="nar-fig nar-fig-{i}">
        <div class="clip-media has-parallax"{ratio}>{tag(f["im"], "(max-width:900px) 100vw, 50vw")}</div>
        <figcaption class="nar-fig-cap"><span class="t-eyebrow t-pulse n">{f["cap_a"]}</span><span class="t-eyebrow">{f["cap_b"]}</span></figcaption>
      </figure>
'''
    return f"""
<!-- 2. STICKY NARRATIVE -->
<section class="nar">
  <div class="nar-grid">
    <aside class="nar-left">
      <div class="nar-sticky">
        <span class="line-mask"><span class="t-eyebrow with-line">{sp["nar_eb"]}</span></span>
        <h2 class="line-mask" data-delay="1"><span class="nar-title">{sp["h2"]}</span></h2>
        <span class="line-mask" data-delay="2"><span class="ps-pulse" style="margin-top:6px">{sp["pulse"]}</span></span>
        <div class="nar-body">
{paras}        </div>
      </div>
    </aside>
    <div class="nar-right">
{figs}    </div>
  </div>
</section>
"""


def _build(sp):
    b = sp.get("build")
    if not b: return ""
    stacks = ""
    for s in b["stacks"]:
        stacks += f'''
  <section class="psc-stack" data-psc-stack>
    <div class="stk-base">{tag(s["base"], "(max-width:900px) 100vw, 62vw", cls="stk-base-img")}</div>
    <div class="stk-top">{tag(s["top"], "(max-width:900px) 80vw, 38vw", cls="stk-top-img")}</div>
    <div class="stk-label">
      <span class="ps-mask-wrap"><span class="ps-mask-text ps-eyebrow">{s["eb"]}</span></span>
      <span class="ps-mask-wrap"><span class="ps-mask-text ps-cream">{s["h"]}</span></span>
      <span class="ps-mask-wrap"><span class="ps-mask-text ps-pulse">{s["pulse"]}</span></span>
      <span class="ps-mask-wrap"><span class="ps-mask-text ps-mono">{s["text"]}</span></span>
    </div>
  </section>
'''
    return f"""
<!-- 3. KINETIC SHOWCASE -->
<div class="psc-wrap">
  <div class="psc-head">
    <span class="line-mask"><span class="t-eyebrow with-line">{b["eb"]}</span></span>
    <h2 class="line-mask" data-delay="1"><span>{b["h2"]}</span></h2>
  </div>
{stacks}</div>
"""


def _statement(sp):
    line, sub = sp["statement"]
    return f"""
<!-- Mid statement -->
<section class="psc-statement">
  <div class="line-mask"><span class="psc-statement-line">{line}</span></div>
  <div class="line-mask" data-delay="1"><span class="psc-statement-sub">{sub}</span></div>
</section>
"""


def _pins(sp):
    pins = sp["pins"]
    imgs = "".join("      " + tag(p["im"], "(max-width:900px) 100vw, 88vw", cls="pin-img is-on" if i == 0 else "pin-img",
                                  extra=f' data-pin-img="{i}"') + "\n" for i, p in enumerate(pins))
    stages = "".join(f'''
      <div class="psc-pin-stage{" is-active" if i == 0 else ""}" data-pin-stage="{i}">
        <div class="ps-mask-wrap"><div class="ps-mask-text ps-eyebrow">{p["eb"]}</div></div>
        <div class="ps-mask-wrap"><h3 class="ps-mask-text ps-cream">{p["h"]}</h3></div>
        <div class="ps-mask-wrap"><span class="ps-mask-text ps-pulse">{p["pulse"]}</span></div>
        <div class="ps-mask-wrap"><p class="ps-mask-text ps-mono">{p["text"]}</p></div>
      </div>''' for i, p in enumerate(pins))
    return f"""
<!-- PINNED MASK REVEAL -->
<div class="psc-pin-outer" id="pin-outer">
  <div class="psc-pin" id="pin-track">
    <div class="psc-pin-frame">
{imgs}      <div class="psc-pin-scrim"></div>
{stages}

      <div class="psc-pin-bar">
        <span id="pin-counter">01 / {len(pins):02d}</span>
        <div class="psc-pin-bar-progress" id="pin-progress"></div>
        <span>Scroll to advance</span>
      </div>
    </div>
  </div>
</div>
"""


def _blueprint(sp):
    bp = sp["bp"]
    sk = bp.get("sketch")
    sketch = ""
    if sk:
        im = sk["im"]
        sketch = f'''    <figure class="bp-sketch">
      {tag(im, "(max-width:900px) 100vw, 700px", extra=f' width="{sk["w"]}" height="{sk["h"]}"')}
      <figcaption>
        <span class="bp-chap-eb">{sk["eb"]}</span>
        <span class="bp-chap-h">{sk["title"]}</span>
        <span class="bp-sketch-p">{sk["text"]}</span>
        <a class="bp-sketch-a" href="{sk["href"]}">{sk["link"]} &rarr;</a>
      </figcaption>
    </figure>
'''
    chaps = "".join(f'''      <div class="bp-chap">
        <div class="bp-chap-eb">{eb}</div>
        <div class="bp-chap-h">{h}</div>
        <ul>
{"".join(f"          <li>{x}</li>" + chr(10) for x in items)}        </ul>
      </div>
''' for eb, h, items in bp["chapters"])
    meta = "".join(f'      <div class="bp-meta-cell"><div class="bp-meta-lbl">{a}</div><div class="bp-meta-val">{b}</div></div>\n' for a, b in bp["meta"])
    nc = f' bp-n{len(bp["chapters"])}' if len(bp["chapters"]) in (2, 3) else ""
    nm = f' bp-n{len(bp["meta"])}' if len(bp["meta"]) in (2, 3) else ""
    return f"""
<!-- 4. BLUEPRINT -->
<section class="bp">
  <div class="bp-inner">
    <div class="bp-head">
      <span class="line-mask"><span class="t-eyebrow with-line">Takeoff</span></span>
      <h2 class="line-mask" data-delay="1"><span class="bp-title">{bp["title"]}</span></h2>
    </div>
{sketch}    <div class="bp-chapters{nc}">
{chaps}    </div>
    <div class="bp-meta{nm}">
{meta}    </div>
  </div>
</section>
"""


def _notes(sp):
    faqs = "".join(f'''    <details>
      <summary>{html.escape(q, quote=False)}</summary>
      <div class="pn-a">{html.escape(a, quote=False)}</div>
    </details>
''' for q, a in sp["faqs"])
    links = "".join(f'      <a href="{h}">{t}</a>\n' for h, t in sp["links"])
    return f"""
<!-- 5. PROJECT NOTES -->
<section class="pn">
  <div class="pn-inner">
    <span class="line-mask"><span class="t-eyebrow with-line">Project Notes</span></span>
    <h2 class="pn-title">Questions about this build</h2>
{faqs}    <div class="pn-links">
{links}    </div>
  </div>
</section>
"""


def _next(sp):
    n = sp["next"]
    return f"""
<!-- 6. HORIZON: NEXT PROJECT -->
<a class="hz" href="{n["href"]}" id="hz-link">
  <div class="hz-media">{tag(n["im"], "100vw")}</div>
  <div class="hz-scrim"></div>
  <div class="hz-inner">
    <span class="t-eyebrow with-line">{n["eb"]}</span>
    <div>
      <h2 class="hz-title hz-title-2">{n["title"]}</h2>
      <span class="hz-action t-eyebrow t-pulse">Continue the journey</span>
    </div>
  </div>
</a>
<div id="hz-wipe"></div>
"""


def build(ROOT, sp):
    slug = sp["slug"]; sig = bool(sp.get("num"))
    url = f"{SITE}/projects/{slug}"
    title, desc = sp["title"], sp["desc"]
    body = ("""<body>
<div id="cur"></div><div id="cur-ring"></div>
<header class="hdr">
  <a href="../" class="hdr-brand">RED AGAVE</a>
  <nav class="hdr-nav">
    <a href="../featured">Work</a>
    <a href="../">Studio</a>
    <a href="../contact">Contact</a>
  </nav>
</header>

""" + _hero(sp, sig) + _narrative(sp) + _build(sp) + _statement(sp) + _pins(sp) + _blueprint(sp) + _notes(sp) + _next(sp))

    s = open(f"{ROOT}/projects/dormarion.html", encoding="utf-8").read()
    head = s[:s.index("</head>")]
    foot = s[s.index("<footer"):]
    css = re.search(r"<style>(.*?)</style>", head, re.S).group(1)
    pre = head[:head.index("<title>")]
    fonts = re.search(r'<link rel="preconnect" href="https://fonts.googleapis.com">.*?</noscript>', head, re.S).group(0)
    hero = sp["hero"]
    article = {"@context": "https://schema.org", "@type": "Article", "headline": sp["headline"], "description": sp["schema_desc"],
               "image": [f"{SITE}/{p}" for p in sp["schema_images"]],
               "datePublished": sp["date"], "dateModified": sp.get("modified", sp["date"]),
               "author": {"@type": "Organization", "name": "Red Agave Landscape", "url": SITE},
               "publisher": {"@type": "Organization", "name": "Red Agave Landscape", "url": SITE},
               "mainEntityOfPage": url, "locationCreated": {"@type": "Place", "name": sp["area"]}}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in sp["faqs"]]}
    mid = ("Signature Projects", SITE + "/featured") if sig else ("Projects", SITE + "/projects/")
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": mid[0], "item": mid[1]},
        {"@type": "ListItem", "position": 3, "name": sp["crumb"], "item": url}]}
    pos = f'.thr-img{{object-position:{sp["hero_pos"]}}}\n' if sp.get("hero_pos") else ""
    pre_img = (f'<link rel="preload" as="image" href="{_src(hero)}"' +
               (f' imagesrcset="{_set(hero)}" imagesizes="100vw"' if len(hero["files"]) > 1 else "") + ' fetchpriority="high">\n')
    new_head = (pre + f"<title>{esc(title)}</title>\n"
        f'<meta name="description" content="{esc(desc)}">\n'
        f'<link rel="canonical" href="{url}">\n' + pre_img + fonts + "\n"
        f'<meta property="og:title" content="{esc(sp["og_title"])}">\n'
        f'<meta property="og:description" content="{esc(desc)}">\n'
        f'<meta property="og:image" content="{SITE}/{sp["share"]}">\n'
        f'<meta property="og:url" content="{url}">\n'
        '<meta property="og:type" content="article">\n<meta property="og:site_name" content="Red Agave Landscape">\n<meta name="twitter:card" content="summary_large_image">\n'
        + ld(article) + "\n<style>" + css + CSS_ADD + pos + "</style>\n" + ld(faq) + "\n" + ld(crumbs) + "\n")
    out = new_head + "</head>\n" + body + "\n" + foot

    # checks
    txt = html.unescape(re.sub(r"<[^>]+>", " ", body))
    words = len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’/-]*", txt))
    visible = (re.sub(r'(?:href|src|srcset)="[^"]*"', "", body) + title + desc + sp["og_title"] + json.dumps(article, ensure_ascii=False)
               + json.dumps(faq, ensure_ascii=False) + json.dumps(crumbs, ensure_ascii=False)).lower()
    hits = [w for w in BANNED if w.lower() in visible]
    if not sig and "signature" in visible: hits.append("signature (regular project)")
    assert not hits, f"{slug}: banned wording {hits}"
    assert not re.search(r"https?://[^\"' ]*redagaveatx\.com/[^\"' ]*\.html", out), f"{slug}: .html in an address"
    miss, dot = [], []
    targets = re.findall(r'(?:href|src)="([^"#]+)"', body) + [u.rsplit(" ", 1)[0] for ss in re.findall(r'srcset="([^"]+)"', body) for u in ss.split(", ")]
    for h in targets + ["../" + p for p in sp["schema_images"]] + ["../" + sp["share"]]:
        if h.startswith(("http", "sms:", "tel:", "mailto:")): continue
        if h.endswith(".html"): dot.append(h)
        if h in PLANNED: continue
        p = os.path.normpath(os.path.join(ROOT, "projects", h))
        if not (os.path.exists(p) or os.path.exists(p + ".html") or os.path.isdir(p)): miss.append(h)
    assert not miss, f"{slug}: missing targets {miss}"
    assert not dot, f"{slug}: .html links {dot}"
    assert not re.search(r'<img(?![^>]*\balt="[^"]{12,}")[^>]*>', body), f"{slug}: image without alt text"
    for d in re.findall(r'<script type="application/ld\+json">(.*?)</script>', out, re.S): json.loads(d)
    assert len(title) <= 60, f"{slug}: title {len(title)}"
    assert 120 <= len(desc) <= 155, f"{slug}: description {len(desc)}"
    assert out.count("<h1") == 1, f"{slug}: h1 count"
    assert 3 <= len(sp["faqs"]) <= 6, f"{slug}: faq count"
    open(f"{ROOT}/projects/{slug}.html", "w", encoding="utf-8").write(out)
    print(f"{slug}: title {len(title)} | desc {len(desc)} | words {words} | h2 {out.count('<h2')} | faqs {len(sp['faqs'])} | imgs {body.count('<img')} | bytes {len(out.encode())} | ok")

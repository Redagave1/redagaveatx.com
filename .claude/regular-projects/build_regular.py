"""Regular project pages (short pages named by street) and the projects index.

    python3 -I .claude/regular-projects/build_regular.py . [--register]

Reads .claude/regular-projects/projects.json. For every entry it writes projects/<slug>.html
(entries with "external": true are only listed on the index). It always rewrites projects/index.html.
--register adds missing lines to sitemap.xml, netlify.toml and llms.txt (safe to run again).
Shell (head CSS, header, footer, scripts) comes from projects/dormarion.html, as for the signature pages.
"""
import re, json, html, os, sys, glob

ROOT = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else "."
REGISTER = "--register" in sys.argv
SITE = "https://www.redagaveatx.com"
HERE = os.path.dirname(os.path.abspath(__file__))
BANNED = ["bare steel", "raw steel", "—", "&mdash;", " may ", " might ", "not sure", "uncertain", "we think", "probably", "it depends",
          "subcontract", "butcher", "design fee", "$", "Corten", "neighbor", "Southern Love", "Cutters", "Blazyk", "Hopeland", "Flycatcher",
          "Fly Catcher", "Axehandle", "Dormarion", "Riverview", "Madison", "Ulit", "Silhouette", "Allison"]
KNOWN = set()   # slugs being built in this run (a page may link to one that is written after it)
e = lambda x: html.escape(x, quote=True)
ld = lambda d: '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False) + "</script>"

CSS_ADD = """
.thr-title-2{font-size:clamp(64px,13vw,200px)}
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
.nar-body a{text-decoration:underline;text-underline-offset:3px}
.pj-top{padding:190px 48px 70px;max-width:1320px;margin:0 auto}
.pj-h1{font-family:'Bebas Neue',Impact,sans-serif;font-weight:400;font-size:clamp(72px,12vw,180px);line-height:.88;letter-spacing:2px;color:var(--cream);margin:18px 0 28px}
.pj-lead{max-width:62ch;font-size:15px;line-height:1.9;color:rgba(240,234,214,.7);font-weight:300}
.pj-lead a{color:var(--gold);border-bottom:1px solid rgba(201,168,76,.4)}
.pj-sig{display:inline-block;margin-top:34px;border:1px solid rgba(201,168,76,.3);color:var(--gold);padding:14px 28px;font-size:10px;letter-spacing:3px;text-transform:uppercase}
.pj-sig:hover{border-color:var(--gold-pulse);color:var(--gold-pulse)}
.pj-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:28px;max-width:1320px;margin:0 auto;padding:0 48px 150px}
.pj-card{display:block;color:var(--cream)}
.pj-card-media{display:block;aspect-ratio:4/3;overflow:hidden;background:#111}
.pj-card-media img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .9s cubic-bezier(.2,.7,.2,1)}
.pj-card:hover .pj-card-media img{transform:scale(1.04)}
.pj-card-eb{display:block;margin-top:18px;font-size:10px;letter-spacing:3px;text-transform:uppercase;color:var(--gold)}
.pj-card-h{display:block;font-family:'Bebas Neue',Impact,sans-serif;font-size:38px;letter-spacing:1.5px;line-height:1;margin:8px 0 8px}
.pj-card-p{display:block;font-size:13px;line-height:1.75;color:rgba(240,234,214,.6);font-weight:300;max-width:44ch}
@media(max-width:1000px){.pj-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:900px){.pn{padding:84px 0}.pn-inner{padding:0 22px}.thr-meta{gap:14px}.pj-top{padding:140px 22px 50px}.pj-grid{grid-template-columns:1fr;padding:0 22px 90px;gap:36px}}
"""

def shell():
    s = open(f"{ROOT}/projects/dormarion.html", encoding="utf-8").read()
    head = s[:s.index("</head>")]
    foot = s[s.index("<footer"):]
    css = re.search(r"<style>(.*?)</style>", head, re.S).group(1)
    pre = head[:head.index("<title>")]
    fonts = re.search(r'<link rel="preconnect" href="https://fonts.googleapis.com">.*?</noscript>', head, re.S).group(0)
    return pre, fonts, css, foot

def srcset(img_dir, name):
    """All widths on disk for images/…/<name>-<w>.webp, widest last."""
    ws = sorted(int(re.search(r"-(\d+)\.webp$", p).group(1)) for p in glob.glob(os.path.join(ROOT, img_dir, name + "-*.webp"))
                if re.search(r"-(\d+)\.webp$", p))
    assert ws, f"no images for {img_dir}{name}"
    return ws

def pic(img_dir, name, alt, sizes, extra="", cls=""):
    ws = srcset(img_dir, name); rel = "../" + img_dir
    c = f' class="{cls}"' if cls else ""
    return (f'<img{c}{extra} src="{rel}{name}-{ws[-1]}.webp" srcset="' + ", ".join(f"{rel}{name}-{w}.webp {w}w" for w in ws) +
            f'" sizes="{sizes}" alt="{e(alt)}">')

HEADER = """<body>
<div id="cur"></div><div id="cur-ring"></div>
<header class="hdr">
  <a href="../" class="hdr-brand">RED AGAVE</a>
  <nav class="hdr-nav">
    <a href="../featured">Work</a>
    <a href="../">Studio</a>
    <a href="../contact">Contact</a>
  </nav>
</header>
"""

def check(name, title, desc, body, out, schemas, base_dir):
    txt = html.unescape(re.sub(r"<[^>]+>", " ", body))
    words = len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’/-]*", txt))
    visible = (re.sub(r'(?:href|src|srcset)="[^"]*"', "", body) + title + desc + "".join(json.dumps(x) for x in schemas)).lower()
    hits = [w for w in BANNED if w.lower() in visible]
    assert not hits, f"{name}: banned wording {hits}"
    miss = []
    for h in re.findall(r'(?:href|src)="([^"#]+)"', body) + [u.split(" ")[0] for ss in re.findall(r'srcset="([^"]+)"', body) for u in ss.split(", ")]:
        if h.startswith(("http", "sms:", "tel:", "mailto:")) or h in KNOWN: continue
        p = os.path.normpath(os.path.join(ROOT, base_dir, h))
        if not (os.path.exists(p) or os.path.exists(p + ".html") or os.path.isdir(p)): miss.append(h)
    assert not miss, f"{name}: missing targets {miss}"
    for d in re.findall(r'<script type="application/ld\+json">(.*?)</script>', out, re.S): json.loads(d)
    assert len(title) <= 60, f"{name}: title {len(title)}"
    assert 120 <= len(desc) <= 155, f"{name}: description {len(desc)}"
    assert out.count("<h1") == 1, f"{name}: h1 count"
    print(f"{name}: title {len(title)} | desc {len(desc)} | words {words} | imgs {body.count('<img')} | ok")

def build_page(sp, pre, fonts, css, foot, nxt):
    slug, d = sp["slug"], sp["img_dir"]
    url = f"{SITE}/projects/{slug}"
    absd = f"{SITE}/{d}"
    hero = sp["hero"]; hws = srcset(d, hero["file"]); rel = "../" + d
    place = f'{sp["area"]}, Texas'
    figs = "".join(f'''      <figure class="nar-fig nar-fig-{i}">
        <div class="clip-media has-parallax">{pic(d, f["file"], f["alt"], "(max-width:900px) 100vw, 50vw", ' loading="lazy"')}</div>
        <figcaption class="nar-fig-cap"><span class="t-eyebrow t-pulse n">{f["cap_a"]}</span><span class="t-eyebrow">{f["cap_b"]}</span></figcaption>
      </figure>
''' for i, f in enumerate(sp["figs"], 1))
    paras = "".join(f'          <p class="line-mask" data-delay="{i}"><span>{p}</span></p>\n' for i, p in enumerate(sp["paras"], 3))
    chaps = "".join(f'''      <div class="bp-chap">
        <div class="bp-chap-eb">{c["eb"]}</div>
        <div class="bp-chap-h">{c["h"]}</div>
        <ul>
{"".join(f"          <li>{x}</li>" + chr(10) for x in c["items"])}        </ul>
      </div>
''' for c in sp["built"])
    meta = "".join(f'      <div class="bp-meta-cell"><div class="bp-meta-lbl">{a}</div><div class="bp-meta-val">{b}</div></div>\n' for a, b in sp["meta"])
    faqs = "".join(f'''    <details>
      <summary>{html.escape(q, quote=False)}</summary>
      <div class="pn-a">{html.escape(a, quote=False)}</div>
    </details>
''' for q, a in sp["faqs"])
    links = "".join(f'      <a href="{h}">{t}</a>\n' for h, t in sp["links"])
    year = f' &middot; {sp["year"]}' if sp.get("year") else ""
    body = HEADER + f"""
<section class="thr">
  <a href="./" class="thr-back t-eyebrow">All Projects</a>
  <div class="thr-media">
    <img class="thr-img" fetchpriority="high"{' style="object-position:' + hero["pos"] + '"' if hero.get("pos") else ""} src="{rel}{hero["file"]}-{hws[-1]}.webp" srcset="{", ".join(f"{rel}{hero['file']}-{w}.webp {w}w" for w in hws)}" sizes="100vw" alt="{e(hero["alt"])}">
  </div>
  <div class="thr-scrim"></div>
  <div class="thr-inner">
    <div class="thr-top">
      <div class="thr-locator">
        <span class="line-mask" data-delay="1"><span class="t-eyebrow with-line">Project{year}</span></span>
        <span class="line-mask" data-delay="2"><span class="t-eyebrow">{place}</span></span>
      </div>
    </div>
    <div class="thr-bottom">
      <h1 class="line-mask" data-delay="2"><span class="thr-title thr-title-2">{sp["name"]}</span></h1>
      <div class="thr-meta line-mask" data-delay="4">
        <span class="t-eyebrow">Residence &middot; {sp["area"]}, TX</span>
        <span class="t-eyebrow">{sp["kicker"]}</span>
      </div>
    </div>
  </div>
  <div class="thr-scroll"><span class="t-eyebrow t-pulse">Scroll</span></div>
</section>

<section class="nar">
  <div class="nar-grid">
    <aside class="nar-left">
      <div class="nar-sticky">
        <span class="line-mask"><span class="t-eyebrow with-line">The Project &middot; {sp["area"]}</span></span>
        <h2 class="line-mask" data-delay="1"><span class="nar-title">{sp["h2"]}</span></h2>
        <span class="line-mask" data-delay="2"><span class="ps-pulse" style="margin-top:6px">{sp["kicker"]}</span></span>
        <div class="nar-body">
{paras}        </div>
      </div>
    </aside>
    <div class="nar-right">
{figs}    </div>
  </div>
</section>

<section class="bp">
  <div class="bp-inner">
    <div class="bp-head">
      <span class="line-mask"><span class="t-eyebrow with-line">Takeoff</span></span>
      <h2 class="line-mask" data-delay="1"><span class="bp-title">What was <em>built</em>.</span></h2>
    </div>
    <div class="bp-chapters">
{chaps}    </div>
    <div class="bp-meta">
{meta}    </div>
  </div>
</section>

<section class="pn">
  <div class="pn-inner">
    <span class="line-mask"><span class="t-eyebrow with-line">Project Notes</span></span>
    <h2 class="pn-title">Questions about this build</h2>
{faqs}    <div class="pn-links">
{links}    </div>
  </div>
</section>

<a class="hz" href="{nxt["href"]}" id="hz-link">
  <div class="hz-media"><img loading="lazy" src="{nxt["img"]}" alt="{e(nxt["alt"])}"></div>
  <div class="hz-scrim"></div>
  <div class="hz-inner">
    <span class="t-eyebrow with-line">{nxt["eb"]}</span>
    <div>
      <h2 class="hz-title">{nxt["title"]}</h2>
      <span class="hz-action t-eyebrow t-pulse">{nxt["action"]}</span>
    </div>
  </div>
</a>
<div id="hz-wipe"></div>
"""
    title, desc = sp["title"], sp["desc"]
    article = {"@context": "https://schema.org", "@type": "Article", "headline": sp["headline"], "description": sp["schema_desc"],
               "image": [absd + sp["share"]] + [f'{absd}{f["file"]}-{srcset(d, f["file"])[-1]}.webp' for f in sp["figs"]],
               "datePublished": sp["date"], "dateModified": sp.get("modified", sp["date"]),
               "author": {"@type": "Organization", "name": "Red Agave Landscape", "url": SITE},
               "publisher": {"@type": "Organization", "name": "Red Agave Landscape", "url": SITE},
               "mainEntityOfPage": url, "locationCreated": {"@type": "Place", "name": f'{sp["area"]}, TX'}}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in sp["faqs"]]}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Projects", "item": SITE + "/projects/"},
        {"@type": "ListItem", "position": 3, "name": sp["name"], "item": url}]}
    head = (pre + f"<title>{e(title)}</title>\n"
        f'<meta name="description" content="{e(desc)}">\n<link rel="canonical" href="{url}">\n'
        f'<link rel="preload" as="image" href="{rel}{hero["file"]}-{hws[-1]}.webp" imagesrcset="{", ".join(f"{rel}{hero['file']}-{w}.webp {w}w" for w in hws)}" imagesizes="100vw" fetchpriority="high">\n'
        + fonts + "\n"
        f'<meta property="og:title" content="{e(sp["headline"])}">\n<meta property="og:description" content="{e(desc)}">\n'
        f'<meta property="og:image" content="{absd}{sp["share"]}">\n<meta property="og:url" content="{url}">\n'
        '<meta property="og:type" content="article">\n<meta property="og:site_name" content="Red Agave Landscape">\n<meta name="twitter:card" content="summary_large_image">\n'
        + ld(article) + "\n<style>" + css + CSS_ADD + "</style>\n" + ld(faq) + "\n" + ld(crumbs) + "\n")
    out = head + "</head>\n" + body + "\n" + foot
    check(slug, title, desc, body, out, [article, faq], "projects")
    open(f"{ROOT}/projects/{slug}.html", "w", encoding="utf-8").write(out)

def build_index(items, pre, fonts, css, foot, cfg):
    url = SITE + "/projects/"
    cards = "".join(f'''  <a class="pj-card" href="{sp["slug"]}">
    <span class="pj-card-media"><img loading="lazy" src="../{sp["img_dir"]}{sp["card_img"]}" alt="{e(sp["card_alt"])}"></span>
    <span class="pj-card-eb">{sp["area"]}{" &middot; " + sp["year"] if sp.get("year") else ""}</span>
    <span class="pj-card-h">{sp["name"]}</span>
    <span class="pj-card-p">{sp["card"]}</span>
  </a>
''' for sp in items)
    body = HEADER + f"""
<main>
<section class="pj-top">
  <span class="t-eyebrow with-line">Red Agave Landscape &middot; Austin, Texas</span>
  <h1 class="pj-h1">Projects</h1>
  <p class="pj-lead">{cfg["lead"]}</p>
  <a class="pj-sig" href="../featured">Signature Projects</a>
</section>
<section class="pj-grid">
{cards}</section>
</main>
"""
    title, desc = cfg["title"], cfg["desc"]
    coll = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Red Agave Landscape Projects", "url": url, "description": desc,
            "mainEntity": {"@type": "ItemList", "numberOfItems": len(items), "itemListElement": [
                {"@type": "ListItem", "position": i, "name": f'{sp["name"]}, {sp["area"]}', "url": f'{SITE}/projects/{sp["slug"]}'} for i, sp in enumerate(items, 1)]}}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Projects", "item": url}]}
    first = items[0]
    head = (pre + f"<title>{e(title)}</title>\n"
        f'<meta name="description" content="{e(desc)}">\n<link rel="canonical" href="{url}">\n' + fonts + "\n"
        f'<meta property="og:title" content="{e(title)}">\n<meta property="og:description" content="{e(desc)}">\n'
        f'<meta property="og:image" content="{SITE}/{first["img_dir"]}{first["card_img"]}">\n<meta property="og:url" content="{url}">\n'
        '<meta property="og:type" content="website">\n<meta property="og:site_name" content="Red Agave Landscape">\n<meta name="twitter:card" content="summary_large_image">\n'
        + ld(coll) + "\n<style>" + css + CSS_ADD + "</style>\n" + ld(crumbs) + "\n")
    out = head + "</head>\n" + body + "\n" + foot
    check("index", title, desc, body, out, [coll], "projects")
    open(f"{ROOT}/projects/index.html", "w", encoding="utf-8").write(out)

def register(items, cfg):
    def rw(p, fn):
        s = open(f"{ROOT}/{p}", encoding="utf-8").read(); n = fn(s)
        if n != s: open(f"{ROOT}/{p}", "w", encoding="utf-8").write(n); print("updated", p)
    def sm(s):
        anchor = '  <url><loc>https://www.redagaveatx.com/projects/chrysler-bend</loc>'
        assert anchor in s
        add = ""
        if f"<loc>{SITE}/projects/</loc>" not in s:
            add += f'  <url><loc>{SITE}/projects/</loc><lastmod>{cfg["date"]}</lastmod><priority>0.7</priority><changefreq>weekly</changefreq></url>\n'
        for sp in items:
            if sp.get("external"): continue
            if f'<loc>{SITE}/projects/{sp["slug"]}</loc>' not in s:
                add += f'  <url><loc>{SITE}/projects/{sp["slug"]}</loc><lastmod>{sp["date"]}</lastmod><priority>0.6</priority><changefreq>monthly</changefreq></url>\n'
        return s.replace(anchor, add + anchor, 1) if add else s
    def nt(s):
        anchor = '[[redirects]]\n  from = "/projects/chrysler-bend.html"'
        assert anchor in s
        add = ""
        for sp in items:
            if sp.get("external"): continue
            if f'from = "/projects/{sp["slug"]}.html"' not in s:
                add += f'[[redirects]]\n  from = "/projects/{sp["slug"]}.html"\n  to = "/projects/{sp["slug"]}"\n  status = 301\n  force = true\n\n'
        return s.replace(anchor, add + anchor, 1) if add else s
    def ll(s):
        head = "### Project Pages (named by street)"
        if head not in s:
            i = s.index("### Signature Project Pages")
            m = re.search(r"\n#{2,3} ", s[i + 5:])
            j = i + 5 + m.start() + 1 if m else len(s)
            s = s[:j] + head + f"\nIndex: {SITE}/projects/\n\n" + s[j:]
        i = s.index(head); m = re.search(r"\n\n", s[i:]); j = i + m.start()
        block = s[i:j]
        for sp in items:
            if sp.get("external"): continue
            line = f'- **{sp["name"]}** ({sp["area"]}{", " + sp["year"] if sp.get("year") else ""}): {sp["llms"]} {SITE}/projects/{sp["slug"]}'
            if f'/projects/{sp["slug"]}' not in block: block += "\n" + line
        return s[:i] + block + s[j:]
    rw("sitemap.xml", sm); rw("netlify.toml", nt); rw("llms.txt", ll)

def main():
    data = json.load(open(os.path.join(HERE, "projects.json"), encoding="utf-8"))
    cfg, items = data["index"], data["projects"]
    pre, fonts, css, foot = shell()
    own = [sp for sp in items if not sp.get("external")]
    KNOWN.update(sp["slug"] for sp in own)
    for i, sp in enumerate(own):
        if len(own) > 1:
            n = own[(i + 1) % len(own)]
            nxt = {"href": n["slug"], "img": "../" + n["img_dir"] + n["card_img"], "alt": n["card_alt"], "eb": "Next Project",
                   "title": n["name"], "action": "Continue the journey"}
        else:
            nxt = {"href": "../featured", "img": cfg["sig_img"], "alt": cfg["sig_alt"], "eb": "More Work",
                   "title": "Signature <em>Projects.</em>", "action": "See the signature projects"}
        build_page(sp, pre, fonts, css, foot, nxt)
    build_index(items, pre, fonts, css, foot, cfg)
    if REGISTER: register(items, cfg)

main()

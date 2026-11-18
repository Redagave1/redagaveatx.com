"""Shared builder for new Red Agave service pages. Shell (head, nav, footer) comes from the steel retaining walls page."""
import re, json, html, os

H3 = 'style="font-family:\'Montserrat\',sans-serif;font-size:17px;font-weight:600;color:var(--cream);margin:32px 0 12px"'
BANNED = ["bare steel", "—", "&mdash;", " may ", " might ", "not sure", "uncertain", "we think", "probably", "it depends", "subcontract", "butcher",
          "design fee", "$", "Corten", "neighbor", "Southern Love", "Blazyk", "Hopeland", "Flycatcher", "Axehandle", "Silhouette", "Allison"]

def fig(items, cap, wide=False):
    """wide=True keeps a pair of landscape photos at 4:3 instead of cropping them to 3:4."""
    imgs = "".join(f'<img src="../{p}" width="{w}" height="{h}" alt="{html.escape(a, quote=True)}" loading="lazy" decoding="async">' for p, w, h, a in items)
    return f'<figure class="sv-fig"><div class="sv-figs sv-n{len(items)}{" sv-wide" if wide else ""}">{imgs}</div><figcaption>{cap}</figcaption></figure>'

def step(n, t, body):
    return f'<div class="step-card"><div class="step-card-num">{n:02d}</div><div class="step-card-title">{t}</div><p>{body}</p></div>'

def sec(eye, h2, body, alt=False):
    return (f'<section class="sec" style="background:var(--{"dark" if alt else "dark2"})">\n  <div class="s-eye rev">{eye}</div>\n'
            f'  <h2 class="s-title rev">{h2}</h2>\n  <div class="content-body rev">\n{body}\n  </div>\n</section>\n')

CSS = ("<style>.sv-fig{margin:36px 0 8px}.sv-figs{display:grid;gap:12px}.sv-n2{grid-template-columns:1fr 1fr}.sv-n3{grid-template-columns:repeat(3,1fr)}"
       ".sv-figs img{width:100%;height:100%;object-fit:cover;display:block}.sv-n2 img,.sv-n3 img{aspect-ratio:3/4}.sv-wide img{aspect-ratio:4/3}"
       ".sv-fig figcaption{font-size:12px;line-height:1.7;color:var(--cream60);margin-top:12px;letter-spacing:.3px}"
       ".cost-table td:first-child{color:var(--cream)}.cost-table a{color:var(--gold);border-bottom:1px solid rgba(201,168,76,0.3)}"
       "@media(max-width:600px){.sv-n3{grid-template-columns:1fr 1fr}.sv-n3 img:first-child{grid-column:1/-1;aspect-ratio:4/3}.cost-table{font-size:12px}.cost-table th,.cost-table td{padding:8px 6px}}</style>")

def build(ROOT, sp):
    slug = sp["slug"]; url = f"https://www.redagaveatx.com/services/{slug}"
    e = lambda x: html.escape(x, quote=True)
    faqs = sp["faqs"]
    cnt = [0]
    def _alt(m):
        cnt[0] += 1
        return '<section class="sec" style="background:var(--' + ("dark2" if cnt[0] % 2 else "dark") + ')">'
    sections = re.sub(r'<section class="sec" style="background:var\(--dark2?\)">', _alt, sp["sections"])
    faq_bg = "dark" if cnt[0] % 2 else "dark2"
    main = f"""<main>
<div class="page-header"><div class="page-header-bg" id="ph-bg" aria-hidden="true"></div><div class="page-header-ov"></div>
  <div class="page-header-inner">
    <div class="page-eyebrow rev">Red Agave Landscape &nbsp;&middot;&nbsp; Austin, TX</div>
    <h1 class="page-title rev">{sp["h1"]} <span class="slim-gold">Austin TX</span></h1>
  </div>
</div>

<!-- GEO ANSWER BLOCK -->
<section class="sec" style="background:var(--dark2);padding-bottom:0">
  <div class="content-body rev" style="max-width:860px;margin:0 auto;padding:0 0 40px;border-bottom:1px solid rgba(201,168,76,0.08)">
    <h2 style="font-family:'Bebas Neue',Impact,sans-serif;font-size:24px;letter-spacing:2px;color:var(--gold);margin-bottom:14px">{sp["answer_h2"]}</h2>
    <p>{sp["answer"]}</p>
  </div>
</section>

{sections}
<section class="sec" style="background:var(--{faq_bg})">
  <div class="faq rev">
    <h2 class="faq-title">Frequently Asked Questions</h2>
{"".join(f'''    <details>
      <summary class="faq-q">{html.escape(q, quote=False)}</summary>
      <div class="faq-a">{html.escape(a, quote=False)}</div>
    </details>
''' for q, a in faqs)}  </div>
</section>

<div class="cta-band">
  <div class="cta-band-title">{sp["cta"]}</div>
  <div class="cta-band-sub">Owner-designed &middot; Built by our own crew &middot; Free consultation and CAD plan</div>
  <a href="../contact" class="cta-band-btn">Get a Free Quote</a>
</div>
</main>"""
    areas = sp.get("areas", ["Austin", "Westlake Hills", "Lakeway", "Barton Creek", "Bee Cave", "Circle C", "Tarrytown", "Cedar Park", "Round Rock", "Pflugerville"])
    service = {"@context": "https://schema.org", "@type": "Service", "name": sp["service_name"], "serviceType": sp["service_type"], "url": url, "image": sp["og_img"],
               "provider": {"@type": "LandscapeService", "@id": "https://www.redagaveatx.com/#business", "name": "Red Agave Landscape", "url": "https://www.redagaveatx.com",
                            "telephone": "+15126957566", "areaServed": [{"@type": "City", "name": a} for a in areas]},
               "description": sp["service_desc"]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.redagaveatx.com/"},
        {"@type": "ListItem", "position": 2, "name": "Services", "item": "https://www.redagaveatx.com/services"},
        {"@type": "ListItem", "position": 3, "name": sp["crumb"], "item": url}]}
    s = open(f"{ROOT}/services/steel-retaining-walls-austin-tx.html", encoding="utf-8").read()
    lines = s.split("\n")
    def setline(prefix, new):
        hits = [i for i, l in enumerate(lines) if l.startswith(prefix)]
        assert len(hits) == 1, (prefix, len(hits))
        lines[hits[0]] = new
    pre = [i for i, l in enumerate(lines) if l.startswith('<link rel="preload" as="image"')]
    assert len(pre) == 2, pre
    lines[pre[0]] = f'<link rel="preload" as="image" href="{sp["bg_s"]}" media="(max-width:768px)" fetchpriority="high">'
    lines[pre[1]] = f'<link rel="preload" as="image" href="{sp["bg_l"]}" media="(min-width:769px)" fetchpriority="high">'
    setline('<style>#ph-bg{', "<style>#ph-bg{background-image:url('" + sp["bg_l"] + "')}@media(max-width:768px){#ph-bg{background-image:url('" + sp["bg_s"] + "')}}</style>")
    setline("<title>", f"<title>{e(sp['title'])}</title>")
    setline('<meta name="description"', f'<meta name="description" content="{e(sp["desc"])}">')
    setline('<link rel="canonical"', f'<link rel="canonical" href="{url}">')
    setline('<meta property="og:title"', f'<meta property="og:title" content="{e(sp["title"])}">')
    setline('<meta property="og:description"', f'<meta property="og:description" content="{e(sp["desc"])}">')
    setline('<meta property="og:image"', f'<meta property="og:image" content="{sp["og_img"]}">')
    setline('<meta property="og:url"', f'<meta property="og:url" content="{url}">')
    ld = [i for i, l in enumerate(lines) if l.startswith('<script type="application/ld+json">')]
    assert len(ld) == 3, len(ld)
    for i, d in zip(ld, (service, faq, crumbs)):
        lines[i] = '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False) + "</script>"
    s = "\n".join(lines)
    a, b = s.index("<main>"), s.index("</main>") + len("</main>")
    s = s[:a] + main + s[b:]
    s = s.replace("</head>", CSS + "\n</head>", 1)
    m = re.search(r'<div class="ft-col"><span class="ft-ct">Services</span>', s)
    assert m
    s = s[:m.end()] + f'<a href="{slug}">{sp["crumb"]}</a>' + s[m.end():]
    open(f"{ROOT}/services/{slug}.html", "w", encoding="utf-8").write(s)
    txt = html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", main, flags=re.S)))
    words = len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’/-]*", txt))
    print("title", len(sp["title"]), "| desc", len(sp["desc"]), "| words", words, "| h1", len(re.findall(r"<h1", s)), "| h2", len(re.findall(r"<h2", s)), "| faqs", len(faqs), "| imgs", main.count("<img"))
    visible = re.sub(r'(?:href|src)="[^"]*"', "", main).lower()
    hits = [w for w in BANNED if w.lower() in visible]
    print("banned hits:", hits)
    assert not hits, hits
    miss = []
    for h in re.findall(r'(?:href|src)="([^"#]+)"', main):
        if h.startswith(("http", "sms:", "tel:", "mailto:")): continue
        p = os.path.normpath(os.path.join(ROOT, "services", h))
        if not (os.path.exists(p) or os.path.exists(p + ".html")): miss.append(h)
    print("missing link/image targets:", miss)
    for d in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S): json.loads(d)
    assert 60 >= len(sp["title"]) and 120 <= len(sp["desc"]) <= 155, "title/desc length"
    print("json-ld ok; bytes", len(s.encode()))

def register(ROOT, slug, card_html, llms_line, date):
    """Add hub card (after the last svc-card), sitemap entry, netlify redirect, llms.txt line."""
    def rw(p, fn):
        s = open(f"{ROOT}/{p}", encoding="utf-8").read(); t = fn(s); assert t != s, p; open(f"{ROOT}/{p}", "w", encoding="utf-8").write(t)
    def hub(s):
        assert f'services/{slug}"' not in s
        cards = list(re.finditer(r'  <a href="services/[a-z-]+" class="svc-card rev">.*?</a>\n', s))
        n = len(cards) + 1
        return s[:cards[-1].end()] + card_html.replace("{N}", f"{n:02d}") + s[cards[-1].end():]
    rw("services.html", hub)
    old = '  <url><loc>https://www.redagaveatx.com/services/steel-retaining-walls-austin-tx</loc>'
    rw("sitemap.xml", lambda s: s.replace(old, f'  <url><loc>https://www.redagaveatx.com/services/{slug}</loc><lastmod>{date}</lastmod><priority>0.8</priority><changefreq>monthly</changefreq></url>\n' + old, 1))
    old2 = '[[redirects]]\n  from = "/services/steel-retaining-walls-austin-tx.html"'
    rw("netlify.toml", lambda s: s.replace(old2, f'[[redirects]]\n  from = "/services/{slug}.html"\n  to = "/services/{slug}"\n  status = 301\n  force = true\n\n' + old2, 1))
    old3 = '- Dedicated service page: redagaveatx.com/services/steel-retaining-walls-austin-tx'
    rw("llms.txt", lambda s: s.replace(old3, old3 + "\n" + llms_line, 1))
    print("registered", slug)

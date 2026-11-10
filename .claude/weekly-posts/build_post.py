#!/usr/bin/env python3
"""Build one weekly blog post from its Markdown source and register it across the site.

Run from the site root:
    python3 .claude/weekly-posts/build_post.py .claude/weekly-posts/posts/<file>.md          # build + register
    python3 .claude/weekly-posts/build_post.py .claude/weekly-posts/posts/<file>.md --check  # checks only, writes nothing

It writes blog/<slug>.html (chrome copied from an existing post) and, the first time, adds the post to:
blog/index.html (top card, guide list, Blog schema), sitemap.xml, netlify.toml (.html -> clean 301), llms.txt.
It refuses to write if a hard rule fails (title/description length, missing image, broken link, banned wording).
See .claude/weekly-posts/README.md for the source format and the rules.
"""
import html, json, os, re, struct, sys
from datetime import date

SITE = "https://www.redagaveatx.com"
TEMPLATE = "blog/outdoor-kitchen-ideas-austin-tx.html"
MONTHS = "January February March April May June July August September October November December".split()

# Wording the owner never wants on the site (case-insensitive). Prices are allowed only when price_ok: yes.
BANNED = [r"\bnot sure\b", r"\buncertain", r"\bwe think\b", r"\bprobably\b", r"\bmight be\b", r"\bit depends\b",
          r"subcontract", r"google business", r"\bGBP\b", r"design fee", r"\blorem\b", r"\bTODO\b", r"\bTK\b"]

CSS = ("<style>.wp-answer{font-size:17px;line-height:1.85;color:var(--cream,#f0ead6);border-left:2px solid var(--gold,#c8a24a);"
       "padding:4px 0 4px 22px;margin:0 0 40px}.wp-fig{margin:36px 0}.wp-fig img{width:100%;height:auto;display:block}"
       ".wp-fig img.wp-tall{max-width:560px}.wp-grid{display:grid;grid-template-columns:repeat(var(--n,2),1fr);gap:4px}.wp-fig figcaption{font-size:12px;line-height:1.7;"
       "letter-spacing:.3px;color:rgba(240,234,214,.55);margin-top:12px}.wp-faq h3{margin-top:28px}"
       "@media(max-width:768px){.wp-grid{grid-template-columns:1fr}}</style>\n")


def die(msg):
    sys.exit("BUILD STOPPED: " + msg)


# ---------- source parsing ----------
def parse(path):
    raw = open(path, encoding="utf-8").read()
    m = re.match(r"---\n([\s\S]*?)\n---\n([\s\S]*)$", raw)
    if not m: die("source must start with a --- front matter block ---")
    meta, key = {}, None
    for line in m.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"): continue
        if line.startswith("  - ") and key:
            meta.setdefault(key, []).append(line[4:].strip()); continue
        k, _, v = line.partition(":")
        key = k.strip(); v = v.strip()
        meta[key] = v if v else []
    return meta, m.group(2).strip()


def webp_size(path):
    with open(path, "rb") as f: b = f.read(40)
    if b[:4] != b"RIFF" or b[8:12] != b"WEBP": return None
    kind = b[12:16]
    if kind == b"VP8X": return 1 + int.from_bytes(b[24:27], "little"), 1 + int.from_bytes(b[27:30], "little")
    if kind == b"VP8 ": w, h = struct.unpack("<HH", b[26:30]); return w & 0x3FFF, h & 0x3FFF
    if kind == b"VP8L":
        v = int.from_bytes(b[21:25], "little"); return (v & 0x3FFF) + 1, ((v >> 14) & 0x3FFF) + 1
    return None


def inline(t):
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', t)
    return t.replace(" -- ", " &mdash; ").replace("'", "&rsquo;")


def figure(spec, problems):
    # [[fig images/a.webp | alt text ;; images/b.webp | alt text || optional caption]]
    body, _, cap = spec.partition("||")
    imgs = []
    for part in body.split(";;"):
        p, _, alt = part.partition("|"); p, alt = p.strip(), alt.strip()
        if not os.path.exists(p): problems.append(f"image missing: {p}"); continue
        if len(alt) < 25: problems.append(f"alt text too short (say what and where): {p}")
        wh = webp_size(p) if p.endswith(".webp") else None
        dims = f' width="{wh[0]}" height="{wh[1]}"' if wh else ""
        imgs.append(f'<img src="../{p}"{dims} alt="{html.escape(alt)}" loading="lazy">')
    n = len(imgs)
    if n == 1 and wh and wh[1] > wh[0]:  # a single tall photo would fill the screen
        imgs[0] = imgs[0].replace("<img ", '<img class="wp-tall" ', 1)
    inner = "".join(imgs) if n == 1 else f'<div class="wp-grid" style="--n:{min(n,3)}">' + "".join(imgs) + "</div>"
    capt = f"<figcaption>{inline(cap.strip())}</figcaption>" if cap.strip() else ""
    return f'<figure class="wp-fig">{inner}{capt}</figure>'


def render(body, problems):
    """Markdown-lite: ## h2, ### h3, - lists, [[fig ...]], paragraphs. '## FAQ: Title' starts the FAQ."""
    blocks = re.split(r"\n\s*\n", body)
    answer = inline(blocks[0].strip())
    out, faqs, in_faq, faq_title, q = [], [], False, "Questions We Hear", None
    for blk in blocks[1:]:
        blk = blk.strip()
        if not blk: continue
        if blk.startswith("[[fig ") and blk.endswith("]]"):
            out.append(figure(blk[6:-2], problems)); continue
        lines = blk.splitlines()
        if lines[0].startswith("## "):
            h = lines[0][3:].strip()
            if h.upper().startswith("FAQ"):
                in_faq = True; faq_title = h.split(":", 1)[1].strip() if ":" in h else faq_title
                out.append(f'<h2>{inline(faq_title)}</h2>\n<div class="wp-faq">')
            else:
                out.append(f"<h2>{inline(h)}</h2>")
            lines = lines[1:]
        if lines and lines[0].startswith("### "):
            h = lines[0][4:].strip()
            if in_faq: q = h; faqs.append([q, ""])
            out.append(f"<h3>{inline(h)}</h3>"); lines = lines[1:]
        if not lines: continue
        if all(l.startswith("- ") for l in lines):
            out.append("<ul>\n" + "\n".join(f"<li>{inline(l[2:])}</li>" for l in lines) + "\n</ul>")
        else:
            p = inline(" ".join(l.strip() for l in lines))
            out.append(f"<p>{p}</p>")
            if in_faq and q is not None: faqs[-1][1] = (faqs[-1][1] + " " + p).strip()
    if in_faq: out.append("</div>")
    return answer, "\n\n".join(out), faqs


plain = lambda x: html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", x))).strip()


# ---------- checks ----------
def check_links(fragment, problems):
    for href in re.findall(r'href="([^"]+)"', fragment):
        if href.startswith(("http://", "https://", "#", "tel:", "sms:", "mailto:")): continue
        target = os.path.normpath(os.path.join("blog", href.split("#")[0]))
        if os.path.isdir(target): target = os.path.join(target, "index.html")
        elif not os.path.splitext(target)[1]: target += ".html"
        if not os.path.exists(target): problems.append(f"broken link: {href}")
        if href.endswith(".html"): problems.append(f"use the clean address without .html: {href}")


def main():
    if len(sys.argv) < 2: die(__doc__)
    src, check_only = sys.argv[1], "--check" in sys.argv
    meta, body = parse(src)
    need = ["slug", "date", "title", "description", "h1", "crumb", "excerpt", "image", "target", "format"]
    missing = [k for k in need if not meta.get(k)]
    if missing: die("front matter missing: " + ", ".join(missing))
    slug, d = meta["slug"], date.fromisoformat(meta["date"])
    problems = []
    if not re.fullmatch(r"[a-z0-9-]+", slug): problems.append("slug: lowercase letters, numbers and hyphens only")
    if len(meta["title"]) > 60: problems.append(f"title is {len(meta['title'])} characters (max 60)")
    if not 120 <= len(meta["description"]) <= 155: problems.append(f"description is {len(meta['description'])} characters (120-155)")
    if not os.path.exists(meta["image"]): problems.append(f"share image missing: {meta['image']}")
    answer, content, faqs = render(body, problems)
    if len(faqs) < 3: problems.append(f"only {len(faqs)} FAQ questions (min 3)")
    if any(not a for _, a in faqs): problems.append("an FAQ question has no answer")
    if len(re.findall(r"<h2>", content)) < 3: problems.append("fewer than 3 H2 sections")
    if content.count("<figure") < 1: problems.append("no photos: every post shows real work")
    related = [r.split("|") for r in meta.get("related", [])]
    rel_html = "".join(f'\n    <a href="{h.strip()}" class="related-card">\n      <div class="related-card-title">{inline(t.strip())}</div>\n'
                       f'      <p class="related-card-excerpt">{inline(x.strip())}</p>\n      <span class="related-card-link">Read Article &rarr;</span>\n    </a>'
                       for h, t, x in related)
    check_links(answer + content + rel_html, problems)
    text = plain(answer + " " + content)
    for pat in BANNED:
        if re.search(pat, text, re.I): problems.append(f"banned wording ({pat})")
    if re.search(r"\$\s?\d", text) and meta.get("price_ok") != "yes": problems.append("prices found; set price_ok: yes only for a cost guide")
    words = len(text.split())
    if words < 700: problems.append(f"only {words} words (min 700)")
    if problems:
        print("\n".join("  - " + p for p in problems)); die(f"{len(problems)} problem(s) in {src}")

    url = f"{SITE}/blog/{slug}"
    img_abs = f"{SITE}/{meta['image']}"
    nice_date = f"{MONTHS[d.month-1]} {d.day}, {d.year}"
    post = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": plain(meta["h1"]), "description": meta["description"],
            "image": img_abs, "datePublished": d.isoformat(), "dateModified": meta.get("modified", d.isoformat()),
            "author": {"@type": "Organization", "name": "Red Agave Landscape", "url": SITE + "/"},
            "publisher": {"@type": "Organization", "name": "Red Agave Landscape", "logo": {"@type": "ImageObject", "url": SITE + "/images/red-agave-logo.png"}},
            "mainEntityOfPage": {"@type": "WebPage", "@id": url}, "about": meta["target"]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": plain(q), "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in faqs]}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Blog", "item": SITE + "/blog/"},
        {"@type": "ListItem", "position": 3, "name": plain(meta["crumb"]), "item": url}]}
    ld = "".join('<script type="application/ld+json">' + json.dumps(x, ensure_ascii=False) + "</script>\n" for x in (post, faq, crumbs))

    s = open(TEMPLATE, encoding="utf-8").read()
    e = lambda x: html.escape(x, quote=True)
    s = re.sub(r"<title>[^<]*</title>", f"<title>{e(meta['title'])}</title>", s, count=1)
    for pat, val in [(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{e(meta["description"])}">'),
                     (r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{url}">'),
                     (r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{e(plain(meta["h1"]))}">'),
                     (r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{e(meta["description"])}">'),
                     (r'<meta property="og:image" content="[^"]*">', f'<meta property="og:image" content="{img_abs}">'),
                     (r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{url}">')]:
        s, n = re.subn(pat, lambda m, v=val: v, s, count=1)
        if n != 1: die(f"template is missing {pat}")
    s = re.sub(r'<script type="application/ld\+json">[\s\S]*?</script>\n?', "", s)
    s = s.replace("</head>", ld + CSS + "</head>", 1)
    ig = f'\n<p><a href="{meta["instagram"]}" target="_blank" rel="noopener">See this on Instagram &rarr;</a></p>' if meta.get("instagram") else ""
    main = (f'<main>\n<div class="page-header"><div class="page-header-ov"></div><div class="page-header-inner">\n'
            f'<div class="article-breadcrumb"><a href="./">Blog</a> &nbsp;&rsaquo;&nbsp; {inline(meta["crumb"])}</div>\n'
            f'<h1 class="page-title">{inline(meta["h1"])}</h1>\n<div class="article-date">{nice_date}</div>\n</div></div>\n\n'
            f'<article class="article-body rev">\n\n<p class="wp-answer">{answer}</p>\n\n{content}{ig}\n\n</article>\n\n'
            f'<div class="cta-band">\n  <div class="cta-band-title">{inline(meta.get("cta_title", "Plan Your Project"))}</div>\n'
            f'  <div class="cta-band-sub">{inline(meta.get("cta_sub", "Owner-designed &middot; Built by our own crew &middot; Austin since 2009"))}</div>\n'
            f'  <a href="../contact" class="cta-band-btn">Get a Free Quote</a>\n</div>\n\n'
            + (f'<div class="related rev">\n  <h2 class="related-title">Related Articles</h2>\n  <div class="related-grid">{rel_html}\n  </div>\n</div>\n' if related else "")
            + "</main>")
    s, n = re.subn(r"<main>[\s\S]*?</main>", lambda m: main, s, count=1)
    if n != 1: die("template has no <main>")

    print(f"blog/{slug}.html: {words} words, {content.count('<figure')} photo blocks, {len(faqs)} FAQs, "
          f"title {len(meta['title'])}, description {len(meta['description'])}")
    if check_only: print("checks passed (nothing written)"); return
    open(f"blog/{slug}.html", "w", encoding="utf-8").write(s)
    register(meta, slug, d, url)
    inbound = [f for f in os.popen("git ls-files '*.html'").read().split() if f != f"blog/{slug}.html"
               and re.search(rf'href="[^"]*{re.escape(slug)}"', open(f, encoding="utf-8").read())]
    print(f"pages linking to it: {len(inbound)} {inbound[:6]}")
    if len([f for f in inbound if f != "blog/index.html"]) < 2:
        print("NEXT: add contextual links to this post from at least 2 pages (its service page, city page, or case study).")


def register(meta, slug, d, url):
    # blog index: top card, guide list (alphabetical), Blog schema
    p = "blog/index.html"; s = open(p, encoding="utf-8").read()
    if f'href="{slug}"' not in s:
        card = (f'\n    <a href="{slug}" class="blog-card rev">\n      <div class="blog-card-body">\n'
                f'        <div class="blog-card-date">{MONTHS[d.month-1]} {d.year}</div>\n'
                f'        <h2 class="blog-card-title">{inline(meta["h1"])}</h2>\n'
                f'        <p class="blog-card-excerpt">{inline(meta["excerpt"])}</p>\n'
                f'        <span class="blog-card-link">Read Article</span>\n      </div>\n    </a>\n')
        s = s.replace('<div class="blog-grid">\n', '<div class="blog-grid">\n' + card, 1)
        li = f'    <li style="margin:0 0 14px;break-inside:avoid"><a href="{slug}" style="color:var(--gold)">{inline(meta["h1"])}</a></li>\n'
        items = re.findall(r'    <li style="margin:0 0 14px;break-inside:avoid"><a href="[^"]*" style="color:var\(--gold\)">([^<]*)</a></li>\n', s)
        after = [t for t in items if plain(t).lower() < plain(meta["h1"]).lower()]
        if after:
            anchor = re.search(r'    <li style="margin:0 0 14px;break-inside:avoid"><a href="[^"]*" style="color:var\(--gold\)">' + re.escape(after[-1]) + r"</a></li>\n", s)
            s = s[:anchor.end()] + li + s[anchor.end():]
        def blog_ld(m):
            j = json.loads(m.group(1))
            if j.get("@type") != "Blog": return m.group(0)
            j["blogPost"].insert(0, {"@type": "BlogPosting", "headline": plain(meta["h1"]), "url": url, "datePublished": d.isoformat()})
            return '<script type="application/ld+json">' + json.dumps(j, ensure_ascii=False) + "</script>"
        s = re.sub(r'<script type="application/ld\+json">([\s\S]*?)</script>', blog_ld, s)
        open(p, "w", encoding="utf-8").write(s); print("registered: blog index")
    # sitemap
    p = "sitemap.xml"; s = open(p, encoding="utf-8").read()
    if f"<loc>{url}</loc>" not in s:
        s = s.replace("</urlset>", f"  <url><loc>{url}</loc><lastmod>{d.isoformat()}</lastmod><priority>0.6</priority><changefreq>monthly</changefreq></url>\n</urlset>", 1)
        s = re.sub(r"(<loc>https://www\.redagaveatx\.com/blog/</loc><lastmod>)[^<]*", rf"\g<1>{d.isoformat()}", s)
        open(p, "w", encoding="utf-8").write(s); print("registered: sitemap")
    # netlify .html -> clean
    p = "netlify.toml"; s = open(p, encoding="utf-8").read()
    if f'from = "/blog/{slug}.html"' not in s:
        block = f'[[redirects]]\n  from = "/blog/{slug}.html"\n  to = "/blog/{slug}"\n  status = 301\n  force = true\n\n'
        i = s.index('[[redirects]]\n  from = "/blog/')
        s = s[:i] + block + s[i:]
        open(p, "w", encoding="utf-8").write(s); print("registered: netlify redirect")
    # llms.txt
    p = "llms.txt"; s = open(p, encoding="utf-8").read()
    if f"redagaveatx.com/blog/{slug}" not in s:
        head = "## Weekly Project Posts\n\nOne post a week built around a real Red Agave project or decision, newest first.\n\n"
        if "## Weekly Project Posts" not in s:
            s = s.replace("## Company Profile", head + "## Company Profile", 1)
        line = f"- {d.isoformat()} — {plain(meta['h1'])} — redagaveatx.com/blog/{slug} — {plain(meta['excerpt'])}\n"
        s = s.replace(head, head + line, 1) if head in s else s.replace("## Weekly Project Posts\n\n", "## Weekly Project Posts\n\n" + line, 1)
        open(p, "w", encoding="utf-8").write(s); print("registered: llms.txt")


if __name__ == "__main__":
    main()

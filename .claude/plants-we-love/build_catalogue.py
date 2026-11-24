#!/usr/bin/env python3
"""Rebuild the plant photo catalogue for the future "Plants We Love" section.

Run from the site root:
    python3 .claude/plants-we-love/build_catalogue.py

It reads plants.json (names, where each set was photographed, carousel folders, notes) and scans
images/plants/<slug>/ plus every page's <img alt> text, then writes:
    CATALOGUE.md     the list to read and search
    catalogue.html   a contact sheet (open it through the local preview; .claude/ is blocked on the public site)
Nothing on the public site changes. Add a plant: put its WebP photos in images/plants/<slug>/, add an entry to
plants.json, run this again.
"""
import glob, html, json, os, re, struct

HERE = os.path.dirname(os.path.abspath(__file__))
SIZE = re.compile(r"-(\d{3,4})\.webp$")


def webp_size(path):
    with open(path, "rb") as f: b = f.read(40)
    if b[:4] != b"RIFF" or b[8:12] != b"WEBP": return None
    kind = b[12:16]
    if kind == b"VP8X": return 1 + int.from_bytes(b[24:27], "little"), 1 + int.from_bytes(b[27:30], "little")
    if kind == b"VP8 ": w, h = struct.unpack("<HH", b[26:30]); return w & 0x3FFF, h & 0x3FFF
    if kind == b"VP8L":
        v = int.from_bytes(b[21:25], "little"); return (v & 0x3FFF) + 1, ((v >> 14) & 0x3FFF) + 1
    return None


def site_use():
    """images/plants path -> [(page, alt text)] from every HTML page on the site."""
    use = {}
    for f in sorted(glob.glob("**/*.html", recursive=True)):
        if f.startswith((".claude", "node_modules")): continue
        t = open(f, encoding="utf-8").read()
        for m in re.finditer(r'<img[^>]*src="[^"]*(images/plants/[^"]+)"[^>]*>', t):
            alt = re.search(r'alt="([^"]*)"', m.group(0))
            use.setdefault(m.group(1), []).append((f, html.unescape(alt.group(1)) if alt else ""))
    return use


def main():
    data = json.load(open(os.path.join(HERE, "plants.json"), encoding="utf-8"))
    use = site_use()
    md = ["# Plant Photo Catalogue", "",
          "Every plant picture we hold, kept for the future **Plants We Love** section. Rebuilt by `build_catalogue.py`; edit `plants.json`, not this file.", "",
          "Rules that apply to every plant page: only Jensen's own photos go on the site, slides with text on them never go in a post, "
          "and each photo is captioned with what it shows and where it was taken.", ""]
    cards, total = [], 0
    md += ["## 1. Ready for the site (`images/plants/`)", "",
           "| Plant | Botanical name | Photos | Photographed | Post |", "|---|---|---|---|---|"]
    detail = []
    for p in data["plants"]:
        folder = f"images/plants/{p['slug']}"
        groups = {}
        for f in sorted(glob.glob(folder + "/*.webp")):
            base = SIZE.sub("", os.path.basename(f)).replace(".webp", "")
            groups.setdefault(base, []).append(f)
        shots = {b: fs for b, fs in groups.items() if not b.endswith("share")}
        total += len(shots)
        md.append(f"| {p['common']} | *{p['botanical']}* | {len(shots)} | {p['where']} | [/{p['post']}](https://www.redagaveatx.com/{p['post']}) |")
        detail += [f"### {p['common']} (*{p['botanical']}*)", "", f"- **Folder:** `{folder}/`", f"- **Photographed:** {p['where']}",
                   f"- **Post:** /{p['post']}"]
        if p.get("carousel"): detail.append("- **Instagram carousel:** " + "; ".join(p["carousel"]))
        if p.get("notes"): detail.append(f"- **Notes:** {p['notes']}")
        detail += ["", "| Photo | Sizes | What it shows | Used on |", "|---|---|---|---|"]
        card = [f'<section><h2>{html.escape(p["common"])} <i>{html.escape(p["botanical"])}</i></h2><p>{html.escape(p["where"])} &middot; /{p["post"]}</p><div class="g">']
        for base, fs in shots.items():
            alts = [a for f in fs for _, a in use.get(f, []) if a]
            pages = sorted({pg for f in fs for pg, _ in use.get(f, [])})
            shows = p.get("describe", {}).get(base) or (alts[0] if alts else "NOT DESCRIBED YET")
            sizes = ", ".join(f"{w}x{h}" for w, h in filter(None, (webp_size(f) for f in fs)))
            detail.append(f"| `{base}` | {sizes} | {shows} | {', '.join(pages) or 'not used yet'} |")
            thumb = min(fs, key=os.path.getsize)
            card.append(f'<figure><img src="../../{thumb}" loading="lazy" alt=""><figcaption><b>{base}</b><br>{html.escape(shows)}</figcaption></figure>')
        detail.append("")
        cards.append("".join(card) + "</div></section>")
    md += ["", f"{len(data['plants'])} plants, {total} photos.", ""] + detail

    md += ["## 2. Carousel slide sets on the Mac", "",
           "Finished Instagram slides (text on the picture). They stay out of blog posts; they are listed so a Plants We Love page can link or embed the carousel.", "",
           "| Plant | Folder | Files |", "|---|---|---|"]
    md += [f"| {c['plant']} | `{c['folder']}` | {c['files']} |" for c in data["carousels"]]

    lib = data["desktop_library"]
    md += ["", "## 3. Reference pictures on the Desktop (`~/Desktop/Plants/`)", "", lib["note"], "",
           "| Plant (file name) | File | Camera data |", "|---|---|---|"]
    md += [f"| {x['plant']} | `{x['file']}` | {x['camera']} |" for x in lib["files"]]

    raw = data["raw_photos"]
    md += ["", "## 4. Own photos not yet made into a post", "", raw["note"], "", "| Folder | Files | What they show |", "|---|---|---|"]
    md += [f"| `{x['folder']}` | {x['files']} | {x['shows']} |" for x in raw["sets"]]

    md += ["", "## 5. Plants named on the site that have no photo set yet", "", data["wanted"]["note"], ""]
    md += [f"- {x}" for x in data["wanted"]["plants"]]
    open(os.path.join(HERE, "CATALOGUE.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")

    page = ("<!doctype html><html lang=en><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1'>"
            "<meta name=robots content=noindex><title>Plant Photo Catalogue</title><style>"
            "body{margin:0;padding:32px 24px 80px;background:#0f0e0c;color:#f0ead6;font:14px/1.6 Montserrat,system-ui,sans-serif}"
            "h1{font:400 44px/1 'Bebas Neue',Impact,sans-serif;letter-spacing:2px;margin:0 0 6px}h2{font:400 26px/1.1 'Bebas Neue',Impact,sans-serif;"
            "letter-spacing:1.5px;margin:44px 0 2px;color:#c8a24a}h2 i{font:italic 14px Georgia,serif;color:#f0ead6;letter-spacing:0;margin-left:10px}"
            "p{margin:0 0 14px;color:rgba(240,234,214,.6)}.g{display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:14px}"
            "figure{margin:0}img{width:100%;aspect-ratio:3/4;object-fit:cover;display:block}figcaption{font-size:11px;line-height:1.5;"
            "color:rgba(240,234,214,.6);margin-top:6px}figcaption b{color:#f0ead6;font-weight:600}</style>"
            f"<h1>Plant Photo Catalogue</h1><p>{len(data['plants'])} plants, {total} photos ready for the site. Kept for the Plants We Love section.</p>"
            + "".join(cards) + "</html>")
    open(os.path.join(HERE, "catalogue.html"), "w", encoding="utf-8").write(page)
    print(f"catalogue: {len(data['plants'])} plants, {total} photos, {len(data['carousels'])} carousel sets, "
          f"{len(lib['files'])} Desktop reference pictures")


if __name__ == "__main__":
    main()

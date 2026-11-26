"""Makes the JPEGs for Pinterest round 4 (one board per signature project) from the committed photos.

    python3 -I .claude/geo-plan/make_pins_round4.py <output folder>

Reads each photo with `git show HEAD:<path>` (some working-tree copies are iCloud-only and hang when read).
Each file in a board gets a slightly different height, so its draft thumbnail can be told apart in the pin tool
(drafts keep no file names). Writes manifest.json with the thumbnail height at 236 wide for each pin."""
import sys, os, io, json, subprocess
from PIL import Image

out = sys.argv[1]
plan = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "pinterest-round4.json")))
manifest = []
for b in plan["boards"]:
    d = os.path.join(out, b["key"]); os.makedirs(d, exist_ok=True)
    for i, (fn, title, text) in enumerate(b["pins"]):
        raw = subprocess.run(["git", "show", "HEAD:" + b["dir"] + fn], capture_output=True, timeout=120).stdout
        im = Image.open(io.BytesIO(raw)).convert("RGB")
        if im.width > 1200:
            im = im.resize((1200, round(1200 * im.height / im.width)), Image.LANCZOS)
        cut = 22 * i                      # trims 22 px more from the bottom of each next file
        im = im.crop((0, 0, im.width, im.height - cut))
        name = f"{i+1:02d}.jpg"; im.save(os.path.join(d, name), "JPEG", quality=88)
        desc = f'{text} {b["area"]}. Red Agave Landscape.' + (" " + b["credit"] if b.get("credit") else "")
        manifest.append({"board": b["board"], "key": b["key"], "file": f'{b["key"]}/{name}', "w": im.width, "h": im.height,
                         "ratio": round(im.height / im.width, 4), "title": title, "description": desc, "link": b["link"]})
json.dump(manifest, open(os.path.join(out, "manifest.json"), "w"), indent=1)
print(len(manifest), "pins on", len(plan["boards"]), "boards")
for b in plan["boards"]:
    assert len(b["board"]) <= 50, b["board"]
    rs = sorted(m["ratio"] for m in manifest if m["key"] == b["key"])
    print(b["key"], len(b["pins"]), "pins | closest ratios apart:", round(min([y - x for x, y in zip(rs, rs[1:])] or [9]), 4), "|", b["board"])

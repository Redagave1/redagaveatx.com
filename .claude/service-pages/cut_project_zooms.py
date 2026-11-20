"""Cuts the zoom-in bands (1125 by 640, plus 800 by 455) and share images (1200 by 630) for the project pages
built with proj_lib.py. Sources are the site's own photos. Output is WebP with no EXIF.
Run: python3 -I .claude/service-pages/cut_project_zooms.py .
"""
import os, sys
from PIL import Image

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
P = "images/projects/"
G = "images/gallery/"
SE, SR, EA = P + "se-austin-fire-water/", P + "south-austin-screened-room/", P + "east-austin-steel-boulders/"
POOL, STREAM, COURT, TRI = (P + "pool-ipe-deck-bamboo-screen/", P + "boulder-stream-steel-fire-trough/",
                            P + "courtyard-stream-japanese-maple/", P + "triangle-fire-pit-stock-tank-pool/")

# (source, crop box x0 y0 x1 y1, output path without size suffix)
BANDS = [
 (SE + "24-water-feature-fire-pits-overview-1200.webp", (330, 150, 1200, 645), SE + "27-zoom-boulder-fire-pit-lit-steel-edging"),
 (SE + "19-finished-water-feature-fire-pit-dusk-1200.webp", (0, 520, 1200, 1203), SE + "28-zoom-steel-channel-black-water"),
 (SE + "18-finished-steel-planter-1200.webp", (0, 470, 1200, 1153), SE + "29-zoom-planter-base-river-rock-light"),
 (SR + "07-cedar-skylight-well-ceiling-fan-1200.webp", (0, 0, 1200, 683), SR + "10-zoom-skylight-cedar-well"),
 (SR + "09-screened-room-interior-1200.webp", (0, 180, 1200, 863), SR + "11-zoom-cedar-ceiling-black-fan"),
 (SR + "08-screened-room-interior-door-seating-1200.webp", (0, 917, 1200, 1600), SR + "12-zoom-screen-door-pet-door"),
 (EA + "01-steel-plate-seated-in-boulder-slot-1200.webp", (0, 470, 1200, 1153), EA + "04-zoom-steel-seated-in-boulder-slot"),
 (EA + "02-steel-edging-through-boulders-install-1200.webp", (300, 0, 1200, 512), EA + "05-zoom-steel-run-level-boulder"),
 (EA + "03-finished-steel-edging-boulders-mulch-fern-1200.webp", (0, 80, 900, 592), EA + "06-zoom-steel-edge-into-boulder-mulch"),
 (G + "DSC04040.webp", (240, 0, 1365, 640), POOL + "zoom-bamboo-screen-along-fence"),
 (G + "DSC04039.webp", (330, 300, 1455, 940), POOL + "zoom-dark-pool-pale-coping-ipe-deck"),
 (G + "DSC04042.webp", (240, 520, 1365, 1160), POOL + "zoom-ipe-deck-boards-rocking-chair"),
 (G + "IMG_5451.webp", (0, 270, 1600, 1180), STREAM + "zoom-lit-steel-edging-stream-dusk"),
 (G + "IMG_8186.webp", (0, 170, 1600, 1080), STREAM + "zoom-water-pouring-from-boulder-fire-trough"),
 (G + "IMG_8182.webp", (0, 250, 1600, 1160), STREAM + "zoom-boulder-stream-ferns-steel-bed"),
 (G + "IMG_8283.webp", (0, 860, 1200, 1543), COURT + "zoom-stream-water-between-boulders"),
 (G + "IMG_6284.webp", (0, 560, 1200, 1243), COURT + "zoom-boulders-purple-foliage-fern"),
 (G + "IMG_8275.webp", (0, 380, 1200, 1063), COURT + "zoom-japanese-maple-over-stream"),
 (G + "IMG_8347.webp", (0, 860, 1440, 1679), TRI + "zoom-steel-spillway-into-stock-tank"),
 (G + "IMG_8339.webp", (0, 330, 1440, 1149), TRI + "zoom-fire-lava-rock-dark-stone"),
 (G + "IMG_8343.webp", (0, 330, 1200, 1013), TRI + "zoom-triangle-fire-pit-point"),
]
# portrait zoom for a narrative figure: (source, box, output path with suffix, output size)
FIGS = [
 (EA + "03-finished-steel-edging-boulders-mulch-fern-1200.webp", (430, 0, 970, 675), EA + "07-zoom-fern-steel-river-rock-800.webp", (800, 1000)),
]
# share images, 1200 by 630: (source, box, output)
SHARES = [
 (G + "DSC04039.webp", (0, 180, 1600, 1020), POOL + "pool-ipe-deck-share.webp"),
 (G + "IMG_5474.webp", (0, 180, 1600, 1020), STREAM + "boulder-stream-fire-trough-share.webp"),
 (G + "IMG_8283.webp", (0, 290, 1200, 920), COURT + "courtyard-stream-share.webp"),
 (G + "IMG_8345.webp", (0, 330, 1200, 960), TRI + "triangle-fire-pit-share.webp"),
]

# plain resizes to 800 wide (and 1200 wide for landscape heroes): (source, output, width)
RESIZE = [
 (SR + "05-finished-screened-room-exterior-1200.webp", SR + "05-finished-screened-room-exterior-800.webp", 800),
 (EA + "02-steel-edging-through-boulders-install-1200.webp", EA + "02-steel-edging-through-boulders-install-800.webp", 800),
 (EA + "03-finished-steel-edging-boulders-mulch-fern-1200.webp", EA + "03-finished-steel-edging-boulders-mulch-fern-800.webp", 800),
 (G + "DSC04039.webp", POOL + "ipe-deck-dark-pool-loungers-bamboo-800.webp", 800),
 (G + "DSC04039.webp", POOL + "ipe-deck-dark-pool-loungers-bamboo-1200.webp", 1200),
 (G + "DSC04040.webp", POOL + "ipe-deck-corner-bamboo-screen-800.webp", 800),
 (G + "DSC04041.webp", POOL + "ipe-deck-pool-loungers-under-trees-800.webp", 800),
 (G + "DSC04042.webp", POOL + "ipe-deck-rocking-chair-pool-coping-800.webp", 800),
 (G + "IMG_5474.webp", STREAM + "steel-fire-trough-boulder-stream-dusk-800.webp", 800),
 (G + "IMG_5474.webp", STREAM + "steel-fire-trough-boulder-stream-dusk-1200.webp", 1200),
 (G + "IMG_5491.webp", STREAM + "boulder-stream-fire-trough-grasses-800.webp", 800),
 (G + "IMG_8183.webp", STREAM + "boulder-stream-ferns-lit-steel-edging-800.webp", 800),
 (G + "IMG_8168.webp", STREAM + "lit-steel-edged-bed-stream-gravel-800.webp", 800),
 (G + "IMG_8191.webp", STREAM + "boulder-stream-mist-lit-edging-night-800.webp", 800),
 (G + "IMG_8283.webp", COURT + "japanese-maple-over-courtyard-stream-800.webp", 800),
 (G + "IMG_6284.webp", COURT + "courtyard-stream-boulders-shade-plants-800.webp", 800),
 (G + "IMG_8275.webp", COURT + "courtyard-stream-maple-trunk-glass-wall-800.webp", 800),
 (G + "IMG_5373.webp", COURT + "courtyard-stream-head-at-glass-wall-800.webp", 800),
 (G + "IMG_8345.webp", TRI + "triangle-fire-pit-spillway-stock-tank-pool-800.webp", 800),
 (G + "IMG_8339.webp", TRI + "triangle-fire-pit-from-above-spillway-800.webp", 800),
 (G + "IMG_8343.webp", TRI + "triangle-fire-pit-point-turf-concrete-800.webp", 800),
 (G + "IMG_8347.webp", TRI + "steel-spillway-tapered-base-stock-tank-800.webp", 800),
]

def save(im, path, q=82):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    im.convert("RGB").save(path, "WEBP", quality=q, method=6)

def main():
    for src, box, out in BANDS:
        im = Image.open(os.path.join(ROOT, src)).convert("RGB").crop(box)
        assert abs(im.width / im.height - 1125 / 640) < 0.01, (src, im.size)
        save(im.resize((1125, 640), Image.LANCZOS), os.path.join(ROOT, out + "-1125.webp"))
        save(im.resize((800, 455), Image.LANCZOS), os.path.join(ROOT, out + "-800.webp"))
    for src, box, out, size in FIGS:
        im = Image.open(os.path.join(ROOT, src)).convert("RGB").crop(box)
        save(im.resize(size, Image.LANCZOS), os.path.join(ROOT, out))
    for src, box, out in SHARES:
        im = Image.open(os.path.join(ROOT, src)).convert("RGB").crop(box)
        assert abs(im.width / im.height - 1200 / 630) < 0.01, (src, im.size)
        save(im.resize((1200, 630), Image.LANCZOS), os.path.join(ROOT, out))
    for src, out, w in RESIZE:
        im = Image.open(os.path.join(ROOT, src)).convert("RGB")
        save(im.resize((w, round(im.height * w / im.width)), Image.LANCZOS), os.path.join(ROOT, out), q=80)
    print("resized", len(RESIZE))
    print("bands", len(BANDS), "figs", len(FIGS), "shares", len(SHARES))

main()

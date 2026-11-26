"""Shared pieces for the 2026-11-20 service pages (driveways, fences and gates, patio covers, paver patios,
lawn service, outdoor fireplaces, irrigation). svc_lib.build() does the page and its checks; this adds the
owner rules svc_lib does not test, and the service-area paragraph every page ends with."""
import re

# Internal job names and wording that never go in visible text or alt text (links may contain them).
EXTRA_BANNED = [r"\braw steel\b", r"\bulit\b", r"\bmadison\b", r"\briverview\b", r"\bdormarion\b", r"never subcontracted",
                r"google business", r"\bmay\b", r"\bmight\b", r"\bperhaps\b", r"\bneighbou?r", r"\bwarrant"]


def check(*texts):
    """Call before build(). Fails on wording svc_lib.BANNED does not cover."""
    visible = re.sub(r'(?:href|src)="[^"]*"', "", " ".join(texts)).lower()
    hits = [p for p in EXTRA_BANNED if re.search(p, visible)]
    assert not hits, ("extra banned wording", hits)


AREAS = ("<p>We build across the Austin area, including <a href=\"../locations/westlake-hills-tx\">Westlake Hills</a>, "
         "<a href=\"../locations/lakeway-tx\">Lakeway</a>, <a href=\"../locations/barton-creek-tx\">Barton Creek</a>, "
         "<a href=\"../locations/bee-cave-tx\">Bee Cave</a>, <a href=\"../locations/circle-c-tx\">Circle C</a>, "
         "<a href=\"../locations/tarrytown-tx\">Tarrytown</a>, <a href=\"../locations/cedar-park-tx\">Cedar Park</a>, "
         "<a href=\"../locations/round-rock-tx\">Round Rock</a>, and <a href=\"../locations/pflugerville-tx\">Pflugerville</a>.</p>")

STANDING = ("<p>Red Agave Landscape has built in Austin since 2009, with more than 750 projects. We hold 4.8 stars across 87 Google "
            "reviews, and we won the Best of Houzz Service award in 2019 and 2020. Every project starts with a free consultation, "
            "and the CAD plan is included. Call or text (512) 695-7566.</p>")

"""Build data/brezova.json: Laurence of Březová, Hussite chronicle, July 1419 to July 1420 (FRB V, 1893).

Conventions in tools/brezova_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brezova_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "brezova.json"


def build():
    sections = []
    for s in SECTIONS:
        units = []
        for i, u in enumerate(s["units"], 1):
            unit = {"n": i, "pg": u["pg"], "titel": u["titel"], "orig": u["orig"], "en": u["en"]}
            if u.get("lang"):
                unit["lang"] = u["lang"]
            if u.get("note"):
                unit["note"] = u["note"]
            units.append(unit)
        sections.append({"id": s["id"], "zk": s["zk"], "titel": s["titel"], "blurb": s["blurb"], "units": units})
    data = {
        "titel": "Laurence of Březová's Hussite chronicle, 1419–1420",
        "autor": "Laurence of Březová (c. 1370–after 1437), master of the Prague university",
        "jahr": "1420s",
        "orig_sprache": "la",
        "pg_label": "FRB V p.",
        "quelle": "Vavřinec z Březové, Kronika husitská, ed. J. Goll, Fontes rerum Bohemicarum V (Prague 1893), pp. 344–396. Page images: Czech Academy of Sciences, FONTES, book 1103; machine text: AHISTO portal, Masaryk University. Public domain.",
        "hinweis": "Goll prints Laurence's Latin beside an old Czech translation; only the Latin is carried, read against the page images. Excerpts from July 1419 to July 1420; cuts are marked [...]. The companion site The Hussite Field Armies carries the chronicle from 22 August 1420 on. The English is this site's working translation (CC0).",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()

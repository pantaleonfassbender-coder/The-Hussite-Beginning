"""Build data/richental.json: Ulrich Richental, chronicle of the Council of Constance (Buck 1882).

Conventions in tools/richental_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from richental_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "richental.json"


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
        "titel": "Ulrich Richental's chronicle of the council",
        "autor": "Ulrich Richental (c. 1360–1437), citizen of Constance",
        "jahr": "c. 1420",
        "orig_sprache": "de",
        "pg_label": "Buck p.",
        "quelle": "Ulrichs von Richental Chronik des Constanzer Concils 1414 bis 1418, ed. M. R. Buck (Tübingen: Litterarischer Verein in Stuttgart, 1882), pp. 58 and 79–80. Internet Archive, ulrichsvonriche00richgoog. Public domain.",
        "hinweis": "Richental wrote in German for his town, some years after the council, from what he saw and heard 'from house to house'. Buck prints the Aulendorf manuscript; the text was read against the page images. Two excerpts; cuts are marked [...]. The English is this site's working translation (CC0).",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()

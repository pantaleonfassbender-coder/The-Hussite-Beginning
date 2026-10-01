"""Build data/deecclesia.json: Hus, De ecclesia, in Schaff's English (1915).

Conventions in tools/deecclesia_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from deecclesia_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "deecclesia.json"


def build():
    sections = []
    for s in SECTIONS:
        units = []
        for i, u in enumerate(s["units"], 1):
            unit = {"n": i, "pg": u["pg"], "titel": u["titel"], "en": u["en"]}
            if u.get("orig"):
                unit["orig"] = u["orig"]
            if u.get("lang"):
                unit["lang"] = u["lang"]
            if u.get("note"):
                unit["note"] = u["note"]
            units.append(unit)
        sections.append({"id": s["id"], "zk": s["zk"], "titel": s["titel"], "blurb": s["blurb"], "units": units})
    data = {
        "titel": "Hus, De ecclesia (1413)",
        "autor": "Jan Hus, writing in exile in southern Bohemia; English by David S. Schaff (1915)",
        "jahr": "1413",
        "orig_sprache": "la",
        "pg_label": "Schaff p.",
        "quelle": "John Huss, De Ecclesia. The Church, translated by David S. Schaff (New York: Charles Scribner's Sons, 1915). Internet Archive, deecclesiachurch00husjuoft. Public domain.",
        "hinweis": "Five passages in Schaff's English of 1915, read against the page images; his bracketed references to the canon law are kept, his footnotes are not. The Latin is not given: the only critical edition (S. H. Thomson, 1956) is in copyright, and the early printings are not available in usable scans. The Latin of the articles the council drew from the book is in 'The council's decrees' (Decr. Articles). Cuts are marked […].",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()

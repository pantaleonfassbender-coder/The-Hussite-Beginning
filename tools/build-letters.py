"""Build data/letters.json: Hus's letters from Constance (Palacký 1869; Workman and Pope 1904).

Conventions in tools/letters_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from letters_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "letters.json"


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
        "titel": "Hus's letters from Constance",
        "autor": "Jan Hus (c. 1370–1415), writing from Constance and from prison",
        "jahr": "1414–1415",
        "orig_sprache": "la",
        "pg_label": "Palacký p.",
        "quelle": "Original: F. Palacký, Documenta Mag. Joannis Hus (Prague 1869), nos. 41, 59, 70, 75, 83 and 88, pp. 78–144 (Internet Archive documentamagjoa00palagoog). English: The Letters of John Hus, tr. H. B. Workman and R. M. Pope (London: Hodder and Stoughton, 1904), pp. 160–270 (Internet Archive lettersofjohnhus00husjuoft). Both public domain.",
        "hinweis": "Six of the letters Hus wrote at Constance, from the arrival to the eve of the end. The original, Latin or Czech, is Palacký's text; the English is Workman and Pope's translation of 1904, the one English in this module not made for the site. Both were read against the page images; Palacký's old Czech spelling is kept. Cuts, the same in both columns, are marked […].",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()

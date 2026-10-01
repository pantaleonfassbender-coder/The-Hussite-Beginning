"""Build data/council.json: the king's word and the council's, 1415 (Palacký 1869).

Conventions in tools/council_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from council_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "council.json"


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
        "titel": "The king's word and the council's (1415)",
        "autor": "Sigismund's chancery; the lords of Bohemia and Moravia; the Council of Constance",
        "jahr": "1415",
        "orig_sprache": "la",
        "pg_label": "Palacký p.",
        "quelle": "F. Palacký, Documenta Mag. Joannis Hus (Prague: Tempský, 1869), nos. 70, 74 and 81, pp. 543–572. Internet Archive, documentamagjoa00palagoog (Google scan). Public domain.",
        "hinweis": "Three documents on the safe conduct and the sentence, all from Palacký's Documenta: the king's revocation of the safe conducts after the pope's flight, the Czech petition of 250 Bohemian and Moravian lords, and the council's letter to Bohemia after the burning. Read against the page images; Palacký's Latin and old Czech spelling are kept. The council's decrees themselves (Haec sancta, the sentence of 6 July) are in the module 'The council's decrees' (Decr.). Cuts are marked […]. The English is this site's working translation (CC0).",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()

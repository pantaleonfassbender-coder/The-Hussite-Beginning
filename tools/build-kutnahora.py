"""Build data/kutnahora.json: the Decree of Kutná Hora (1409) and the quarrel over it (Palacký 1869).

Conventions in tools/kutnahora_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kutnahora_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "kutnahora.json"


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
        "titel": "The Decree of Kutná Hora and the quarrel over it",
        "autor": "King Wenceslas IV; the Polish, Bavarian and Saxon nations of the university of Prague; an anonymous Bohemian master",
        "jahr": "1409",
        "orig_sprache": "la",
        "pg_label": "Palacký p.",
        "quelle": "F. Palacký (ed.), Documenta Mag. Joannis Hus vitam, doctrinam, causam in Constantiensi concilio actam ... illustrantia (Prague: Tempsky, 1869), nos. 10, 12, 13 and 15, pp. 347–359. Internet Archive, documentamagjoa00palagoog. Public domain.",
        "hinweis": "Four documents of 1409 from Palacký's Documenta: the king's mandate, the petition and the oath of the three 'German' nations, and an anonymous defence of the mandate. Read against the page images; the king's abbreviated titles are written out. Excerpts; cuts are marked [...]. The English is this site's working translation (CC0).",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()

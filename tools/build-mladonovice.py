"""Build data/mladonovice.json: Peter of Mladoňovice, Relatio (Palacký 1869).

Conventions in tools/mladonovice_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from mladonovice_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "mladonovice.json"


def build():
    sections = []
    for s in SECTIONS:
        units = []
        for i, u in enumerate(s["units"], 1):
            unit = {"n": i, "pg": u["pg"], "titel": u["titel"], "orig": u["orig"], "en": u["en"]}
            if u.get("note"):
                unit["note"] = u["note"]
            units.append(unit)
        sections.append({"id": s["id"], "zk": s["zk"], "titel": s["titel"], "blurb": s["blurb"], "units": units})
    data = {
        "titel": "Peter of Mladoňovice: the trial and death of Hus",
        "autor": "Peter of Mladoňovice (d. 1451), bachelor of Prague, secretary to Jan of Chlum and eyewitness at Constance",
        "jahr": "1414–1415",
        "orig_sprache": "la",
        "pg_label": "Palacký p.",
        "quelle": "Relatio de Mag. Joannis Hus causa in Constantiensi concilio acta, in František Palacký, Documenta Mag. Joannis Hus vitam, doctrinam, causam in Constantiensi concilio actam et controversias de religione in Bohemia annis 1403–1418 motas illustrantia (Prague: Tempský, 1869), pp. 237–324. Internet Archive, documentamagjoa00palagoog (Google scan). Public domain.",
        "hinweis": "Palacký printed the Relatio from the Mladoňovice manuscript of the Bohemian Museum, with the variants of Vienna manuscripts. The Latin was read against the page images; his spelling and his dates in brackets are kept, his notes on the manuscripts are not. Excerpts from the five parts of the Relatio; cuts are marked […]. The English is this site's working translation (CC0).",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()

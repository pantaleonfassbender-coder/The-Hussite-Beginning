"""Build data/lords.json: the protest of the Bohemian and Moravian lords to the Council of Constance, 2 September 1415 (Palacký 1869).

Conventions in tools/lords_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lords_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "lords.json"


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
        "titel": "The protest of the Bohemian lords",
        "autor": "The barons, lords, knights and squires of Bohemia and Moravia, assembled at Prague",
        "jahr": "2 September 1415",
        "orig_sprache": "la",
        "pg_label": "Palacký p.",
        "quelle": "F. Palacký (ed.), Documenta Mag. Joannis Hus vitam, doctrinam, causam in Constantiensi concilio actam ... illustrantia (Prague: Tempsky, 1869), no. 85, pp. 580–584. Internet Archive, documentamagjoa00palagoog. Public domain.",
        "hinweis": "Palacký prints the letter from several manuscripts, with the names of all who sealed its eight copies; the names are not carried here. Read against the page images; abbreviated titles are written out. Three excerpts covering most of the letter; cuts are marked [...]. The English is this site's working translation (CC0).",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()

"""Build data/jerome.json: Poggio Bracciolini to Leonardo Bruni on the trial of Jerome of Prague, 30 May 1416 (Palacký 1869).

Conventions in tools/jerome_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from jerome_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "jerome.json"


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
        "titel": "Poggio on the trial of Jerome of Prague",
        "autor": "Poggio Bracciolini (1380–1459), Florentine humanist and papal secretary",
        "jahr": "30 May 1416",
        "orig_sprache": "la",
        "pg_label": "Palacký p.",
        "quelle": "F. Palacký (ed.), Documenta Mag. Joannis Hus vitam, doctrinam, causam in Constantiensi concilio actam ... illustrantia (Prague: Tempsky, 1869), no. 100, pp. 624–629. Internet Archive, documentamagjoa00palagoog. Public domain.",
        "hinweis": "Six excerpts covering most of the letter, read against the page images; cuts are marked [...]. The account of the burning is not carried. The English is this site's working translation (CC0); William Shepherd's English of 1802/1837 is in the public domain but too free to use here.",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()

"""Build data/decrees.json: Haec sancta and the sentence against Hus (Mansi XXVII, 1784).

Conventions in tools/decrees_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from decrees_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "decrees.json"


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
        "titel": "The council's decrees: Haec sancta and the sentence",
        "autor": "The Council of Constance, sessions V (6 April 1415) and XV (6 July 1415)",
        "jahr": "1415",
        "orig_sprache": "la",
        "pg_label": "Mansi XXVII col.",
        "quelle": "Sacrorum conciliorum nova et amplissima collectio, ed. J. D. Mansi, vol. XXVII (Venice: Zatta, 1784), cols. 590 and 752–755. Internet Archive, sacrorumconcilio0027joan. Public domain.",
        "hinweis": "Mansi reprints the acts of Constance largely from Hermann von der Hardt's edition (1696–1700), whose fourth volume, with these sessions, is not available in a usable scan. The Latin was read against the page images; the long s, ligatures and accents are normalized. Excerpts; cuts are marked […]. The English is this site's working translation (CC0).",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()

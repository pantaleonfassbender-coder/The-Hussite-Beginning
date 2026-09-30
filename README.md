# The Hussite Beginning

A documentary apparatus for the beginning of the Hussite revolution, 1409–1420: how did a trial become a war? Public-domain sources with the original (Latin, Czech, German) beside a working English translation, a timeline linked into the texts, and a list of what is still to come.

Its thesis, to be tested against the texts: the Council of Constance won its case and Sigismund lost his kingdom. The council ended the great schism and condemned Jan Hus, who had come under the safe conduct of the king of the Romans; Hus was burned on 6 July 1415. Bohemia answered with the chalice, the protest of its lords, the defenestration of 1419 and the Four Articles, and in 1420 Jan Žižka held Prague against the crusade Sigismund led to take his inheritance.

Stage 1 (in progress) carries three modules:

- **Peter of Mladoňovice, the trial and death of Hus** — the eyewitness *Relatio*, in F. Palacký, *Documenta Mag. Joannis Hus* (Prague 1869), pp. 237–324: the safe conduct, the arrest, the hearings of 7 and 8 June 1415, the sentence and the burning. Excerpts, Latin read against the page images, with a working translation.
- **Hus's letters from Constance** — six letters, November 1414 to June 1415, in the original Latin or Czech (Palacký 1869) with the English of Workman and Pope (1904), both read against the page images.
- **The king's word and the council's (1415)** — Palacký (1869), pp. 543–572: Sigismund revokes the safe conducts (8 April), the Czech petition of 250 lords (12 May), the council's letter to Bohemia (26 July). Read against the page images, with a working translation.

Planned, in the order of work (see `data/modules.json`):

- **The council's decrees** — *Haec sancta* and the sentence of 6 July 1415 (von der Hardt, 1697–1700).
- **Hus, *De ecclesia*** (1413) — excerpts; English by D. S. Schaff (1915).
- **Ulrich Richental's chronicle of the council** — ed. Buck (1882).
- **The Decree of Kutná Hora** (1409).
- **The protest of the Bohemian lords** (2 September 1415).
- **Poggio on the death of Jerome of Prague** (1416).
- **Laurence of Březová's Hussite chronicle** — *Fontes rerum Bohemicarum* V (1893): the defenestration, the Four Articles, Žižka and Vítkov.

The companion game *Salvus conductus* takes its title from Sigismund's letter of safe conduct.

## Building the data

```
python tools/build-mladonovice.py
python tools/build-letters.py
python tools/build-council.py
```

The texts are kept in `tools/mladonovice_text.py`, `tools/letters_text.py` and `tools/council_text.py`.

## Running locally

Any static server, e.g. `python -m http.server 8140`.

Licences: see `LICENSES.md`.

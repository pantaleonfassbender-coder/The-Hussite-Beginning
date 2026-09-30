# The Hussite Beginning

A documentary apparatus for the beginning of the Hussite revolution, 1409–1420: how did a trial become a war? Public-domain sources with the original (Latin, Czech, German) beside a working English translation, a timeline linked into the texts, and a list of what is still to come.

Its thesis, to be tested against the texts: the Council of Constance won its case and Sigismund lost his kingdom. The council ended the great schism and condemned Jan Hus, who had come under the safe conduct of the king of the Romans; Hus was burned on 6 July 1415. Bohemia answered with the chalice, the protest of its lords, the defenestration of 1419 and the Four Articles, and in 1420 Jan Žižka held Prague against the crusade Sigismund led to take his inheritance.

Stage 1 (in progress) carries one module:

- **Peter of Mladoňovice, the trial and death of Hus** — the eyewitness *Relatio*, in F. Palacký, *Documenta Mag. Joannis Hus* (Prague 1869), pp. 237–324: the safe conduct, the arrest, the hearings of 7 and 8 June 1415, the sentence and the burning. Excerpts, Latin read against the page images, with a working translation.

Planned, in the order of work (see `data/modules.json`):

- **Hus's letters from Constance** — Palacký (1869); English by Workman and Pope (1904).
- **The council's acts** — the safe conduct, *Haec sancta*, the articles and the sentence (Palacký; von der Hardt, 1697–1700).
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
```

The text is kept in `tools/mladonovice_text.py`.

## Running locally

Any static server, e.g. `python -m http.server 8140`.

Licences: see `LICENSES.md`.

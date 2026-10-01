/* The Hussite Beginning — a documentary apparatus. Vanilla JS, hash routes. */
"use strict";

const view = document.getElementById("view");
const D = { mods: null, plates: null, timeline: null, compare: null, texts: {} };
const SIDES = { council: "Pope and Council", reform: "Hus and his friends", crown: "The Crown", hussites: "Prague and Tábor", reception: "Reception" };
const LANGS = { la: "Latin", cs: "Czech", de: "German", en: "English" };

const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const side = s => `<span class="side ${s}">${esc(SIDES[s] || s)}</span>`;
const plateOf = id => (D.plates.plates || []).find(p => p.id === id);
const getJSON = url => fetch(url).then(r => { if (!r.ok) throw new Error(url); return r.json(); });

let langPref = "both";
try { langPref = localStorage.getItem("hussite_lang") || "both"; } catch (e) { /* storage blocked */ }

async function boot() {
  [D.mods, D.plates, D.timeline, D.compare] = await Promise.all(
    ["data/modules.json", "data/plates.json", "data/timeline.json", "data/compare.json"].map(getJSON));
  document.getElementById("navCompare").hidden = !(D.compare.pairs || []).length;
  document.getElementById("navPlates").hidden = !(D.plates.plates || []).length;
  window.addEventListener("hashchange", route);
  route();
}

async function text(id) {
  if (!D.texts[id]) D.texts[id] = await getJSON(`data/${id}.json`);
  return D.texts[id];
}

function route() {
  const parts = (location.hash.replace(/^#\/?/, "") || "").split("/").filter(Boolean);
  const [page, ...args] = parts;
  document.querySelectorAll(".top nav a").forEach(a => {
    const t = a.getAttribute("href").replace(/^#\/?/, "");
    a.classList.toggle("on", (t || "") === (page === "text" ? "texts" : page || ""));
  });
  view.innerHTML = "";
  window.scrollTo(0, 0);
  const pages = { "": overview, texts, text: reader, compare, timeline, plates, sources };
  (pages[page || ""] || overview)(args);
}

/* ------------------------------------------------------------ overview */
function overview() {
  view.innerHTML = `
  <div class="hero one">
    <div>
      <span class="tag">1409–1420 · Jan Hus · Sigismund · Jan Žižka</span>
      <h1>How did a trial become a war?</h1>
      <p class="lede">In 1414 a Prague preacher, excommunicated for defending Wyclif and for attacking the sale of indulgences, rode to the Council of Constance under the safe conduct of Sigismund, king of the Romans and heir to the crown of Bohemia. The council ended the great schism of the popes; it also condemned Jan Hus and had him burned on 6 July 1415. Four years later Prague threw its councillors from the town hall windows, and in 1420 the crusade Sigismund led to take his inheritance broke on a hill outside the city.</p>
      <p class="readable">This apparatus follows the years from the Decree of Kutná Hora (1409) to the battle of Vítkov (1420) through their documents, in public-domain editions with the original beside a working English translation: the eyewitness of the trial, Hus's letters from prison, the acts of the council, the Constance chronicler, the protest of the Bohemian lords, and the Prague chronicler who saw the defenestration and the war.</p>
    </div>
  </div>

  <h2>What the apparatus carries</h2>
  ${D.mods.shipped.length ? `<div class="grid g2">${D.mods.shipped.map(card).join("")}</div>` : `<p class="fine">The first modules are in preparation; the Texts page lists them with their sources.</p>`}

  <h2>The questions it asks</h2>
  <div class="grid g2">
    <div class="panel"><h3>Why was Hus at Constance?</h3>
      <p>Because he had appealed from the pope to Christ, and because the king of the Romans wanted the council to clear Bohemia of the name of heresy before he inherited it. Hus went to be heard; the council meant to judge him.</p></div>
    <div class="panel"><h3>What was a safe conduct worth?</h3>
      <p>Sigismund's letter promised Hus free passage to Constance and back (<a href="#/text/mladonovice/journey/1">Mlad. Journey [1]</a>). Hus was arrested within a month of his arrival (<a href="#/text/mladonovice/arrest/4">Mlad. Arrest [4]</a>). The king told Hus to his face that he had kept his word, since the letter promised a hearing; the Bohemian lords held that it had been broken (<a href="#/text/mladonovice/hearings/1">Mlad. Hearings [1]</a>).</p></div>
    <div class="panel"><h3>How did Prague answer?</h3>
      <p>With the chalice for the laity, a protest sealed by more than four hundred lords (<a href="#/text/lords/protest/1">Protest [1]</a>), the defenestration of 30 July 1419 (<a href="#/text/brezova/y1419/2">Laur. 1419 [2]</a>), the Four Articles of Prague (<a href="#/text/brezova/articles/1">Laur. Articles [1]</a>), and Jan Žižka's fort on the hill of Vítkov (<a href="#/text/brezova/vitkov/3">Laur. Vítkov [3]</a>). What followed, the field armies of 1421–1434, is the subject of the companion site <a href="https://the-hussite-field-armies.netlify.app/">The Hussite Field Armies</a>.</p></div>
    <div class="panel"><h3>Can the story be played?</h3>
      <p>A companion game, <a href="https://salvus-conductus.netlify.app/"><em>Salvus conductus</em></a>: as Jan Hus, 1412–1415, you decide whether to go to Constance, what to say before the council and what to recant, and a recantation does not guarantee your life. Its cards cite the passages carried here; it can also be played on <a href="https://leofassb.itch.io/salvus-conductus">itch.io</a>. The second role, <a href="https://salvus-conductus.netlify.app/zizka.html">Jan Žižka</a>, plays 1419–1420 from the defenestration to Vítkov, and names the violence of both sides.</p></div>
  </div>`;
}

function card(m) {
  return `<a class="card" href="#/text/${m.id}">
    <div>${side(m.side)} <span class="fine">${esc(m.zk)}</span></div>
    <h3>${esc(m.kurz)}</h3><p class="fine">${esc(m.warum)}</p></a>`;
}

/* ------------------------------------------------------------ texts */
function texts() {
  view.innerHTML = `
    <span class="tag">Texts</span><h1>The corpus</h1>
    <p class="lede">Stage 1 of the collection is closed: ten modules, each readable in full, the original beside the English. What is not carried, and why, is listed below.</p>
    ${D.mods.shipped.length ? `<h2>Carried</h2><div class="grid g2">${D.mods.shipped.map(card).join("")}</div>` : ""}
    ${(D.mods.planned || []).length ? `<h2>Planned</h2><div class="grid g2">${D.mods.planned.map(m => `
      <div class="card planned"><div>${side(m.side)} <span class="fine">planned</span></div>
      <h3>${esc(m.kurz)}</h3><p class="fine">${esc(m.warum)}</p><p class="fine"><b>Source:</b> ${esc(m.quelle)}</p></div>`).join("")}</div>` : ""}
    ${(D.mods.missing || []).length ? `<h2 id="missing">Not carried</h2><div class="grid g2">${D.mods.missing.map(m => `
      <div class="card planned"><div>${side(m.side)} <span class="fine">not carried</span></div>
      <h3>${esc(m.kurz)}</h3><p class="fine">${esc(m.warum)}</p><p class="fine"><b>Source:</b> ${esc(m.quelle)}</p></div>`).join("")}</div>` : ""}`;
}

async function reader([id, secId, unitN]) {
  const m = D.mods.shipped.find(x => x.id === id);
  if (!m) { location.hash = "#/texts"; return; }
  view.innerHTML = `<p class="fine">Loading…</p>`;
  const t = await text(m.datei);
  const sec = t.sections.find(s => s.id === secId) || t.sections[0];
  const bilingual = sec.units.some(u => u.orig);
  const lang = bilingual ? langPref : "en";
  const langs = [...new Set(sec.units.filter(u => u.orig).map(u => u.lang || t.orig_sprache))];
  const origName = langs.length === 1 ? (LANGS[langs[0]] || "Original") : langs.map(l => LANGS[l] || l).join(" or ");
  view.innerHTML = `
    <p class="fine"><a href="#/texts">← All texts</a></p>
    <span class="tag">${side(m.side)} ${esc(t.jahr)} · cited as ${esc(sec.zk)} [n]</span>
    <h1>${esc(t.titel)}</h1>
    <p class="fine">${esc(t.autor)}</p>
    <nav class="toc">${t.sections.map(s => `<a href="#/text/${id}/${s.id}" class="${s.id === sec.id ? "on" : ""}">${esc(s.titel)}</a>`).join("")}</nav>
    <div class="panel readable"><h3>${esc(sec.titel)}</h3><p>${esc(sec.blurb)}</p></div>
    ${bilingual ? `<div class="langbar" id="langbar">
      ${[["both", `${origName} + English`], ["orig", origName], ["en", "English"]].map(([k, l]) =>
        `<button data-l="${k}" class="${k === lang ? "on" : ""}">${l}</button>`).join("")}</div>` : ""}
    <div id="units"></div>
    <div class="panel readable hinweis"><span class="tag">Source and editorial note</span>
      <p><b>Source.</b> ${esc(t.quelle)}</p><p>${esc(t.hinweis)}</p></div>`;
  const box = view.querySelector("#units");
  for (const u of sec.units) {
    const showO = u.orig && lang !== "en", showE = !u.orig || lang !== "orig";
    const cls = ["unit", String(u.n) === unitN ? "hl" : ""].join(" ");
    box.insertAdjacentHTML("beforeend", `
      <div class="${cls}" id="u${u.n}">
        <div class="num"><a href="#/text/${id}/${sec.id}/${u.n}" title="Cite as ${esc(sec.zk)} [${u.n}]">[${u.n}]</a>
          ${u.pg ? `<span class="pg" title="${esc(t.pg_label || "")} page.line">${esc(t.pg_label || "")} ${esc(u.pg)}</span>` : ""}</div>
        <div>${u.titel ? `<h4>${esc(u.titel)}${u.lang && langs.length > 1 ? ` <span class="fine">(${esc(LANGS[u.lang] || u.lang)})</span>` : ""}</h4>` : ""}
          <div class="cols ${showO && showE ? "" : "one"}">
            ${showO ? `<div class="origcol"><div class="orig" lang="${esc(u.lang || t.orig_sprache)}"${t.rtl ? ' dir="rtl"' : ""}>${esc(u.orig)}</div>${u.tr ? `<div class="translit">${esc(u.tr)}</div>` : ""}</div>` : ""}
            ${showE ? `<div class="text">${esc(u.en)}</div>` : ""}
          </div></div>
        ${u.note ? `<div class="note">${esc(u.note)}</div>` : ""}
      </div>`);
  }
  view.querySelectorAll("#langbar button").forEach(b => b.onclick = () => {
    langPref = b.dataset.l;
    try { localStorage.setItem("hussite_lang", langPref); } catch (e) { /* storage blocked */ }
    route();
  });
  if (unitN) { const el = document.getElementById("u" + unitN); if (el) el.scrollIntoView({ block: "center" }); }
}

/* ------------------------------------------------------------ compare */
async function compare([pid]) {
  const CMP = D.compare;
  const pair = (CMP.pairs || []).find(p => p.id === pid);
  if (!pair) {
    view.innerHTML = `
      <span class="tag">Compare</span><h1>Constance against Prague</h1>
      <p class="lede">${esc(CMP.lede)}</p>
      <div class="grid g2">${(CMP.pairs || []).map(p => `<a class="card" href="#/compare/${p.id}">
        <div>${p.voices.map(v => side((D.mods.shipped.find(m => m.id === v.text) || {}).side)).join(" ")}</div>
        <h3>${esc(p.titel)}</h3><p class="fine">${esc(p.frage)}</p></a>`).join("")}</div>`;
    return;
  }
  view.innerHTML = `<p class="fine"><a href="#/compare">← All comparisons</a></p><p class="fine">Loading…</p>`;
  const docs = await Promise.all(pair.voices.map(v => {
    const m = D.mods.shipped.find(x => x.id === v.text);
    return text(m.datei).then(t => ({ v, m, t }));
  }));
  const col = ({ v, m, t }) => {
    const sec = t.sections.find(s => s.id === v.sec);
    const units = v.n.map(n => sec.units.find(u => u.n === n)).filter(Boolean);
    return `<div class="voice">
      <div class="vhead">${side(m.side)} <b>${esc(t.autor)}</b><br><span class="fine">${esc(t.jahr)} · ${esc(sec.titel)}</span></div>
      ${units.map(u => `<div class="vunit">
        <div class="fine"><a href="#/text/${m.id}/${sec.id}/${u.n}">${esc(sec.zk)} [${u.n}]</a>${u.titel ? ` · ${esc(u.titel)}` : ""}</div>
        <div class="text">${esc(u.en)}</div></div>`).join("")}
    </div>`;
  };
  view.innerHTML = `
    <p class="fine"><a href="#/compare">← All comparisons</a></p>
    <span class="tag">Compare</span><h1>${esc(pair.titel)}</h1>
    <p class="lede">${esc(pair.frage)}</p>
    <div class="panel readable"><p>${esc(pair.note)}</p></div>
    <div class="cmp n${docs.length}">${docs.map(col).join("")}</div>`;
}

/* ------------------------------------------------------------ timeline */
function timeline() {
  const T = D.timeline;
  view.innerHTML = `
    <span class="tag">Timeline</span><h1>1409–1420</h1>
    <p class="lede">${esc(T.lede)}</p>
    <div class="legend">${Object.keys(SIDES).map(side).join(" ")}</div>
    <div class="tl">${T.stations.map(s => {
      const p = s.plate && plateOf(s.plate);
      return `<div class="st" style="--c:var(--${s.side})">
        <div><div class="d">${esc(s.d)} · ${side(s.side)}</div><h3>${esc(s.titel)}</h3><p>${esc(s.text)}</p>
        ${s.cite ? `<p class="fine"><a href="${s.cite}">✦ ${esc(s.citeLabel)}</a></p>` : ""}</div>
        ${p ? `<img src="assets/plates/${p.id}_t.jpg" alt="${esc(p.titel)}" title="${esc(p.titel)}">` : "<span></span>"}
      </div>`;
    }).join("")}</div>`;
}

/* ------------------------------------------------------------ plates */
function plates() {
  view.innerHTML = `
    <span class="tag">Plates</span><h1>Constance and Prague in pictures</h1>
    <p class="lede">${esc(D.plates.lede || "")}</p>
    <div class="grid g4">${D.plates.plates.map(p => `
      <figure class="plate card"><a href="#" data-p="${p.id}"><img src="assets/plates/${p.id}_t.jpg" alt="${esc(p.titel)}"></a>
      <figcaption>${side(p.side)} <b>${esc(p.titel)}</b><br>${esc(p.caption)}<br><i>${esc(p.source)}</i></figcaption></figure>`).join("")}</div>
    <p class="fine">${esc(D.plates.credit)}</p>`;
  view.querySelectorAll("[data-p]").forEach(a => a.onclick = e => {
    e.preventDefault();
    const p = plateOf(a.dataset.p);
    const lb = document.createElement("div");
    lb.className = "lightbox";
    lb.innerHTML = `<figure><img src="assets/plates/${p.id}.jpg" alt="${esc(p.titel)}"><figcaption class="cap"><b>${esc(p.titel)}.</b> ${esc(p.caption)}</figcaption></figure>`;
    lb.onclick = () => lb.remove();
    document.body.append(lb);
  });
}

/* ------------------------------------------------------------ sources */
function sources() {
  view.innerHTML = `
    <span class="tag">Sources, method, limits</span><h1>How this apparatus is made</h1>
    <div class="readable">
    <p><b>Public domain only.</b> Every text is carried from a printing that is out of copyright, and its source is named on its page. Modern critical editions and translations in copyright are not used; where the only good edition is modern, the module says so.</p>
    <p><b>The page is the authority.</b> The Latin and Czech come from nineteenth-century editions, above all František Palacký's <i>Documenta Mag. Joannis Hus</i> (Prague 1869) and the <i>Fontes rerum Bohemicarum</i>. The machine reading of the scan is corrected against the page image, and every correction that goes beyond the obvious is named in the notes. The editor's text is kept with his spelling and his brackets; his apparatus of variant readings is not carried, except where a variant matters.</p>
    <p><b>Working translations.</b> Where there is no public-domain English, the site gives its own, close to the original and dedicated to the public domain (CC0). It is an aid to reading, not a critical translation. Where a public-domain translation exists (Hus's letters, 1904; his treatise on the Church, 1915), it is used, checked against the original, and named.</p>
    <p><b>Voices and distances.</b> The eyewitness of the trial was Hus's friend and the secretary of his protector; the council's acts say what the council wished to be recorded; the Constance chronicler was a citizen watching the great men pass; the Prague chronicler wrote for the Hussite city. Each module says who wrote, when and for whom.</p>
    <p><b>Dates.</b> The texts' own dates are given as printed (feast days, the Roman calendar) with the modern equivalent.</p>
    </div>
    <h2>Sources carried</h2>
    <div class="grid g2">${D.mods.shipped.map(m => `<div class="panel"><b>${esc(m.kurz)}</b><p class="fine" id="src-${m.id}">…</p></div>`).join("")}</div>
    ${(D.plates.plates || []).length ? `<h2>Plates</h2><p class="fine readable">${esc(D.plates.credit)}</p>` : ""}`;
  D.mods.shipped.forEach(async m => {
    const t = await text(m.datei);
    const el = document.getElementById("src-" + m.id);
    if (el) el.textContent = t.quelle;
  });
}

boot().catch(e => { view.innerHTML = `<p>Could not load the apparatus: ${esc(e.message)}</p>`; });

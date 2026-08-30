/* =============================================================================
 * deriv_panel.js — Panneau DÉRIVÉS du cockpit (corrélations + liquidité)
 * Lit : ../data/deriv_corr.json (généré par scripts/gen_deriv_corr.py)
 * Affiche en PHRASES lisibles en français :
 *   - les corrélations 30j : prix vs OI / funding / long-short / taker
 *   - la carte des liquidations par niveau de prix (où est le gros de la
 *     liquidité : en dessous = carburant de baisse, au-dessus = carburant de hausse)
 * Injecte un panneau repliable dans le cockpit SANS rien casser.
 * stdlib JS pur — aucune dépendance. Charge en lazy (defer).
 * ========================================================================== */
(function () {
  "use strict";

  var PANEL_ID = "deriv-panel";
  var REFRESH_MS = 60000;

  function fmtUsd(n) {
    if (n === null || n === undefined || isNaN(n)) return "—";
    var abs = Math.abs(n);
    if (abs >= 1e9) return (n / 1e9).toFixed(2) + " Md$";
    if (abs >= 1e6) return (n / 1e6).toFixed(2) + " M$";
    if (abs >= 1e3) return (n / 1e3).toFixed(1) + " k$";
    return n.toFixed(2) + " $";
  }

  function fetchJSON(url) {
    return fetch(url, { cache: "no-store" })
      .then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        return r.json();
      });
  }

  function buildPanel() {
    if (document.getElementById(PANEL_ID)) return;
    var style = document.createElement("style");
    style.textContent = [
      "#" + PANEL_ID + " { position: fixed; right: 358px; bottom: 12px; z-index: 9998;",
      "  width: 330px; max-height: 74vh; overflow-y: auto; background: rgba(10,14,22,0.95);",
      "  border: 1px solid rgba(255,255,255,0.12); border-radius: 10px;",
      "  font: 12px/1.5 -apple-system, system-ui, sans-serif; color: #d8e0ea;",
      "  box-shadow: 0 6px 24px rgba(0,0,0,0.55); }",
      "#" + PANEL_ID + " .dp-head { display: flex; align-items: center; justify-content: space-between;",
      "  padding: 8px 12px; cursor: pointer; user-select: none;",
      "  border-bottom: 1px solid rgba(255,255,255,0.08); }",
      "#" + PANEL_ID + " .dp-title { font-weight: 700; letter-spacing: 0.5px; font-size: 12px; }",
      "#" + PANEL_ID + " .dp-badge { background: #3a2f1e; color: #ffd58a; border-radius: 8px;",
      "  padding: 1px 8px; font-size: 10px; margin-left: 6px; }",
      "#" + PANEL_ID + " .dp-body { padding: 10px 12px; }",
      "#" + PANEL_ID + " .dp-sec { font-size: 11px; font-weight: 700; letter-spacing: 0.6px;",
      "  margin: 8px 0 5px; color: #ffd58a; }",
      "#" + PANEL_ID + " .dp-phrase { font-size: 11px; line-height: 1.5; color: #aab6c4; margin-bottom: 4px; }",
      "#" + PANEL_ID + " .dp-phrase b { color: #d8e0ea; }",
      "#" + PANEL_ID + " .dp-liq { border-left: 3px solid #f87171; background: rgba(248,113,113,0.08);",
      "  border-radius: 6px; padding: 7px 9px; margin-top: 6px; font-size: 11px; line-height: 1.5; }",
      "#" + PANEL_ID + " .dp-liq b { color: #fca5a5; }",
      "#" + PANEL_ID + " .dp-liq.up { border-left-color: #4ade80; background: rgba(74,222,128,0.08); }",
      "#" + PANEL_ID + " .dp-liq.up b { color: #86efac; }",
      "#" + PANEL_ID + " .dp-bar { display: flex; height: 8px; border-radius: 4px; overflow: hidden; margin: 6px 0 3px; }",
      "#" + PANEL_ID + " .dp-bar .long { background: #f87171; }",
      "#" + PANEL_ID + " .dp-bar .short { background: #4ade80; }",
      "#" + PANEL_ID + " .dp-leg { font-size: 10px; color: #6b7686; margin-top: 4px; line-height: 1.45; }",
      "#" + PANEL_ID + " .dp-ts { color: #6b7686; font-size: 10px; margin-top: 8px; }",
    ].join("\n");
    document.head.appendChild(style);

    var panel = document.createElement("div");
    panel.id = PANEL_ID;
    panel.innerHTML =
      '<div class="dp-head" id="dp-head">' +
      '<span class="dp-title">📊 DÉRIVÉS <span class="dp-badge" id="dp-badge">corr 30j</span></span>' +
      '<span style="color:#8b98a8" id="dp-toggle">▾</span></div>' +
      '<div class="dp-body" id="dp-body"></div>';
    document.body.appendChild(panel);

    var open = true;
    document.getElementById("dp-head").addEventListener("click", function () {
      open = !open;
      var body = document.getElementById("dp-body");
      body.style.display = open ? "block" : "none";
      document.getElementById("dp-toggle").textContent = open ? "▾" : "▸";
    });

    refresh();
    setInterval(refresh, REFRESH_MS);
  }

  function refresh() {
    var body = document.getElementById("dp-body");
    if (!body) return;
    fetchJSON("../data/deriv_corr.json")
      .then(function (d) {
        var html = "";

        // --- Corrélations 30j ---
        html += '<div class="dp-sec">CORRÉLATIONS 30 JOURS (prix vs…)</div>';
        var c = d.correlations || {};
        Object.keys(c).forEach(function (k) {
          var v = c[k];
          if (!v || !v.lecture) return;
          html += '<div class="dp-phrase"><b>' + v.label + "</b> : " + v.lecture + ".</div>";
        });

        // --- Carte des liquidations ---
        var liq = d.liquidations || {};
        html += '<div class="dp-sec">OÙ EST LA LIQUIDITÉ ? (liquidations OKX récentes)</div>';
        var lB = liq.longs_below_usd || 0;   // longs liquidés EN DESSOUS du prix
        var sB = liq.shorts_below_usd || 0;  // shorts liquidés EN DESSOUS du prix
        var lA = liq.longs_above_usd || 0;   // longs liquidés AU-DESSUS du prix
        var sA = liq.shorts_above_usd || 0;  // shorts liquidés AU-DESSUS du prix
        // Jauge : part des liquidations EN DESSOUS vs AU-DESSUS du prix (tous côtés confondus)
        var below = lB + sB;
        var above = lA + sA;
        var tot = below + above;
        var pctBelow = tot > 0 ? Math.round((below / tot) * 100) : 0;
        var pctAbove = tot > 0 ? 100 - pctBelow : 0;
        html += '<div class="dp-bar">' +
          '<div class="long" style="width:' + pctBelow + '%" title="Liquidations sous le prix"></div>' +
          '<div class="short" style="width:' + pctAbove + '%" title="Liquidations au-dessus du prix"></div></div>';
        html += '<div class="dp-leg">🔴 barre = liquidations <b>EN DESSOUS</b> du prix (' + pctBelow +
          '%) · 🟢 barre = liquidations <b>AU-DESSUS</b> (' + pctAbove + '%)</div>';

        // Les 4 tas, en clair, avec le niveau de prix de chacun
        html += '<div class="dp-phrase">🔴 <b>' + fmtUsd(lB) + "</b> de LONGS liquidés <b>EN DESSOUS</b> du prix " +
          "(niveaux 76-78k — un long est liquidé quand le prix <b>baisse</b> jusqu'à son niveau)</div>";
        html += '<div class="dp-phrase">🔴 ' + fmtUsd(sB) + " de SHORTS liquidés <b>EN DESSOUS</b> aussi (78k — déjà balayés pendant la hausse)</div>";
        html += '<div class="dp-phrase">🟢 <b>' + fmtUsd(sA) + "</b> de SHORTS liquidés <b>AU-DESSUS</b> du prix " +
          "(niveau ~80k — un short est liquidé quand le prix <b>monte</b> jusqu'à son niveau)</div>";
        html += '<div class="dp-phrase">🟢 ' + fmtUsd(lA) + " de LONGS liquidés au-dessus aussi</div>";
        html += '<div class="dp-liq' + (lB > sA ? "" : " up") + '">' +
          (liq.lecture || "") + "</div>";

        // Détail des clusters par niveau
        var clusters = liq.clusters_2000usd || {};
        var keys = Object.keys(clusters);
        if (keys.length) {
          html += '<div class="dp-leg">Détail par niveau (prix actuel ' + fmtUsd(d.mark) + ') : ' +
            keys.map(function (b) {
              var v = clusters[b];
              var pos = (d.mark && Number(b) < d.mark) ? "▼ sous le prix" :
                (d.mark && Number(b) > d.mark ? "▲ au-dessus" : "");
              return b + " $ " + pos + " (🔴 " + fmtUsd(v.long) + " · 🟢 " + fmtUsd(v.short) + ")";
            }).join(" · ") + ".</div>";
        }
        html += '<div class="dp-leg">→ Lecture : le tas qui a le plus gros volume près du prix dicte la direction probable — gros tas EN DESSOUS (🔴) = si le prix y revient, longs forcés = baisse accélérée · gros tas AU-DESSUS (🟢) = si le prix y monte, shorts forcés = hausse forcée.</div>';

        html += '<div class="dp-ts">Dérivés ' + (d.ts || "") + " · mark " + fmtUsd(d.mark) + "</div>";
        body.innerHTML = html;
      })
      .catch(function () {
        body.innerHTML = '<div class="dp-phrase">Données dérivés indisponibles (générées par gen_deriv_corr.py).</div>';
      });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", buildPanel);
  } else {
    buildPanel();
  }
})();

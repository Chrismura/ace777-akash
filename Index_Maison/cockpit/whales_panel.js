/* =============================================================================
 * whales_panel.js — Panneau ONCHAIN du cockpit (gros mouvements BTC)
 * Lit : ../thermo/live.json (chiffres bruts) + ../data/whales_scan_latest.json
 *       + ../data/whales_mouvements.jsonl (mouvements baleines)
 * Injecte un panneau repliable dans le cockpit SANS rien casser.
 * stdlib JS pur — aucune dépendance. Charge en lazy (defer).
 * ========================================================================== */
(function () {
  "use strict";

  var PANEL_ID = "whales-panel";
  var REFRESH_MS = 60000;

  function fmt(n, dec) {
    if (n === null || n === undefined || isNaN(n)) return "—";
    dec = dec || 2;
    return Number(n).toLocaleString("fr-FR", {
      minimumFractionDigits: dec,
      maximumFractionDigits: dec,
    });
  }

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

  function fetchText(url) {
    return fetch(url, { cache: "no-store" }).then(function (r) {
      if (!r.ok) throw new Error("HTTP " + r.status);
      return r.text();
    });
  }

  function buildPanel() {
    if (document.getElementById(PANEL_ID)) return;
    var style = document.createElement("style");
    style.textContent = [
      "#" + PANEL_ID + " { position: fixed; right: 12px; bottom: 12px; z-index: 9999;",
      "  width: 320px; max-height: 70vh; overflow-y: auto; background: rgba(10,14,22,0.94);",
      "  border: 1px solid rgba(255,255,255,0.12); border-radius: 10px;",
      "  font: 12px/1.5 -apple-system, system-ui, sans-serif; color: #d8e0ea;",
      "  box-shadow: 0 6px 24px rgba(0,0,0,0.55); }",
      "#" + PANEL_ID + " .wp-head { display: flex; align-items: center; justify-content: space-between;",
      "  padding: 8px 12px; cursor: pointer; user-select: none;",
      "  border-bottom: 1px solid rgba(255,255,255,0.08); }",
      "#" + PANEL_ID + " .wp-title { font-weight: 700; letter-spacing: 0.5px; font-size: 12px; }",
      "#" + PANEL_ID + " .wp-badge { background: #1e3a5f; color: #8fd3ff; border-radius: 8px;",
      "  padding: 1px 8px; font-size: 10px; margin-left: 6px; }",
      "#" + PANEL_ID + " .wp-badge.hot { background: #5f1e1e; color: #ff9d9d; }",
      "#" + PANEL_ID + " .wp-body { padding: 10px 12px; }",
      "#" + PANEL_ID + " .wp-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 6px; }",
      "#" + PANEL_ID + " .wp-cell { background: rgba(255,255,255,0.04); border-radius: 6px; padding: 6px 8px; }",
      "#" + PANEL_ID + " .wp-cell b { display: block; font-size: 13px; }",
      "#" + PANEL_ID + " .wp-cell span { font-size: 10px; color: #8b98a8; text-transform: uppercase; letter-spacing: 0.4px; }",
      "#" + PANEL_ID + " .wp-up { color: #4ade80; } .wp-down { color: #f87171; }",
      "#" + PANEL_ID + " .wp-mv { border-left: 3px solid #f59e0b; background: rgba(245,158,11,0.08);",
      "  border-radius: 6px; padding: 6px 8px; margin-top: 6px; }",
      "#" + PANEL_ID + " .wp-mv small { color: #8b98a8; }",
      "#" + PANEL_ID + " .wp-ts { color: #6b7686; font-size: 10px; margin-top: 8px; }",
    ].join("\n");
    document.head.appendChild(style);

    var panel = document.createElement("div");
    panel.id = PANEL_ID;
    panel.innerHTML =
      '<div class="wp-head" id="wp-head">' +
      '<span class="wp-title">🐋 ONCHAIN <span class="wp-badge" id="wp-badge">…</span></span>' +
      '<span style="color:#8b98a8" id="wp-toggle">▾</span></div>' +
      '<div class="wp-body" id="wp-body"></div>';
    document.body.appendChild(panel);

    var open = true;
    document.getElementById("wp-head").addEventListener("click", function () {
      open = !open;
      var body = document.getElementById("wp-body");
      body.style.display = open ? "block" : "none";
      document.getElementById("wp-toggle").textContent = open ? "▾" : "▸";
    });

    refresh();
    setInterval(refresh, REFRESH_MS);
  }

  function refresh() {
    var body = document.getElementById("wp-body");
    if (!body) return;
    var badge = document.getElementById("wp-badge");

    // 1. Mouvements baleines (mempoool via surveiller_whales.py)
    fetchJSON("../data/whales_scan_latest.json")
      .then(function (scan) {
        var gros = (scan.gros_blocs || []).length;
        var frag = (scan.fragmentations || []).length;
        var n = gros + frag;
        badge.textContent = n > 0 ? n + " ⚠" : "0";
        if (n > 0) badge.classList.add("hot");
        else badge.classList.remove("hot");

        var html = "";
        if (n > 0) {
          html += '<div style="margin-bottom:8px;font-size:11px;color:#ffd700">⚠️ Gros mouvements détectés (6 derniers blocs)</div>';
          (scan.gros_blocs || []).forEach(function (g) {
            var src = (g.sources_label || []).join(", ") || "inconnu";
            html += '<div class="wp-mv">🐋 <b>' + fmt(g.btc) + " BTC</b> <small>bloc #" + g.hauteur +
              "<br>de : " + src + "<br>vers : " + (g.cibles || []).map(function (c) {
                return fmt(c.btc) + " BTC";
              }).join(", ") + "</small></div>";
          });
          (scan.fragmentations || []).forEach(function (f) {
            html += '<div class="wp-mv">🧩 FRAGMENTATION <b>' + fmt(f.btc) + " BTC</b> <small>source: " +
              f.source.slice(0, 18) + "…</small></div>";
          });
        } else {
          html += '<div style="color:#6b7686;font-size:11px;margin-bottom:8px">Aucun gros mouvement sur les 6 derniers blocs.</div>';
        }
        body.innerHTML = html;
        return scan;
      })
      .catch(function () {
        badge.textContent = "n/a";
      });

    // 2. Chiffres bruts thermo (independants des mouvements)
    fetchJSON("../thermo/live.json")
      .then(function (t) {
        var cells = [
          ["Funding", (t.funding * 100).toFixed(4) + " %", t.funding > 0 ? "wp-up" : "wp-down"],
          ["Whales 24h", fmtUsd(t.whaleUsd || 0) + " (" + (t.whaleN || 0) + ")", t.whaleUsd > 0 ? "wp-up" : ""],
          ["Liq 24h", fmtUsd(t.liq24Usd || 0), ""],
          ["Open Interest", fmt(t.oi) + " BTC", t.chg1h >= 0 ? "wp-up" : "wp-down"],
          ["Fear & Greed", (t.fearGreedLabel || "?") + " " + (t.fearGreed || "—"), (t.fearGreed || 99) <= 40 ? "wp-down" : "wp-up"],
          ["Long/Short", fmt(t.longShort), t.longShort >= 1 ? "wp-up" : "wp-down"],
          ["ETF 24h", fmtUsd(t.etfBtcM ? t.etfBtcM * 1e6 : 0), t.etfBtcM > 0 ? "wp-up" : "wp-down"],
          ["chg 24h", fmt(t.chg24) + " %", t.chg24 >= 0 ? "wp-up" : "wp-down"],
        ];
        var g = '<div class="wp-grid">' + cells.map(function (c) {
          return '<div class="wp-cell"><span>' + c[0] + "</span><b class=\"" + c[2] + '">' + c[1] + "</b></div>";
        }).join("") + "</div>";
        var tsEl = '<div class="wp-ts">Thermo ' + (t.ts || "") + " · surveillé : " +
          (body.textContent ? "" : "") + "</div>";
        // garde le bloc mouvements en haut, chiffres en dessous
        var mov = body.querySelector(".wp-mv, div");
        body.insertAdjacentHTML("beforeend", g + tsEl);
      })
      .catch(function () { /* thermo indisponible, on garde les mouvements */ });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", buildPanel);
  } else {
    buildPanel();
  }
})();

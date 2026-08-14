/* =============================================================================
 * trades_graph.js — Graphique BTC + points d'entrée/sortie des trades (cockpit)
 * Lit : ../data/trades_graph.json (généré par Index_Maison/scripts/gen_trades_graph.py)
 * Injecte un panneau repliable — canvas pur, zéro dépendance, ne casse rien.
 * Rafraîchit toutes les 2 min.
 * ========================================================================== */
(function () {
  "use strict";

  var PANEL_ID = "trades-graph-panel";
  var REFRESH_MS = 120000;

  function buildPanel() {
    if (document.getElementById(PANEL_ID)) return;
    var style = document.createElement("style");
    style.textContent = [
      "#" + PANEL_ID + " { position: fixed; right: 12px; bottom: 12px; z-index: 9998;",
      "  width: 460px; max-width: 94vw; background: rgba(10,14,22,0.94);",
      "  border: 1px solid rgba(255,255,255,0.12); border-radius: 10px;",
      "  font: 12px/1.5 -apple-system, system-ui, sans-serif; color: #d8e0ea;",
      "  box-shadow: 0 6px 24px rgba(0,0,0,0.55); overflow: hidden; }",
      "#" + PANEL_ID + " .tg-head { display: flex; align-items: center; justify-content: space-between;",
      "  padding: 8px 12px; cursor: pointer; user-select: none;",
      "  border-bottom: 1px solid rgba(255,255,255,0.08); }",
      "#" + PANEL_ID + " .tg-title { font-weight: 700; letter-spacing: 0.5px; font-size: 12px; }",
      "#" + PANEL_ID + " .tg-body { padding: 8px 10px 10px; }",
      "#" + PANEL_ID + " .tg-canvas-wrap { position: relative; }",
      "#" + PANEL_ID + " canvas { width: 100%; height: 240px; display: block;",
      "  background: #0b0f16; border-radius: 6px; }",
      "#" + PANEL_ID + " .tg-legend { display: flex; gap: 12px; font-size: 10px; margin-top: 6px; color: #8b98a8; }",
      "#" + PANEL_ID + " .tg-legend i { display: inline-block; width: 9px; height: 9px; border-radius: 50%; margin-right: 3px; vertical-align: -1px; }",
      "#" + PANEL_ID + " .tg-meta { color: #6b7686; font-size: 10px; margin-top: 4px; }",
      "#" + PANEL_ID + " #tg-tip { position: fixed; display: none; background: #161b22; border: 1px solid #30363d;",
      "  border-radius: 4px; padding: 5px 8px; font-size: 10px; pointer-events: none; z-index: 10000; max-width: 380px; }",
    ].join("\n");
    document.head.appendChild(style);

    var panel = document.createElement("div");
    panel.id = PANEL_ID;
    panel.innerHTML =
      '<div class="tg-head" id="tg-head">' +
      '<span class="tg-title">📈 TRADES <span class="tg-badge" style="background:#1e3a5f;color:#8fd3ff;border-radius:8px;padding:1px 8px;font-size:10px;margin-left:6px" id="tg-badge">…</span></span>' +
      '<span style="color:#8b98a8" id="tg-toggle">▾</span></div>' +
      '<div class="tg-body" id="tg-body">' +
      '<div class="tg-canvas-wrap"><canvas id="tg-cv"></canvas></div>' +
      '<div class="tg-legend">' +
      '<span><i style="background:#3fb950"></i>Entrée BUY</span>' +
      '<span><i style="background:#f85149"></i>Entrée SELL</span>' +
      '<span><i style="background:#e3b341"></i>Sortie</span>' +
      '<span><i style="background:#58a6ff"></i>Prix BTC</span></div>' +
      '<div class="tg-meta" id="tg-meta">…</div></div>' +
      '<div id="tg-tip"></div>';
    document.body.appendChild(panel);

    var open = true;
    document.getElementById("tg-head").addEventListener("click", function () {
      open = !open;
      var body = document.getElementById("tg-body");
      body.style.display = open ? "block" : "none";
      document.getElementById("tg-toggle").textContent = open ? "▾" : "▸";
    });

    refresh();
    setInterval(refresh, REFRESH_MS);
  }

  function refresh() {
    fetch("../data/trades_graph.json", { cache: "no-store" })
      .then(function (r) { return r.json(); })
      .then(function (d) {
        var badge = document.getElementById("tg-badge");
        var n = (d._meta && d._meta.nb_trades) || 0;
        badge.textContent = n + " trades";
        draw(d);
      })
      .catch(function () { /* pas encore de données */ });
  }

  function draw(d) {
    var cv = document.getElementById("tg-cv");
    var tip = document.getElementById("tg-tip");
    if (!cv || !cv.getContext) return;
    var k = d.klines || { t: [], c: [] };
    var al = (d.trades && d.trades.ALPHA) || [];
    var be = (d.trades && d.trades.BETA) || [];
    var tr = al.concat(be);
    tr.sort(function (a, b) { return a.ts_ms - b.ts_ms; });

    var meta = document.getElementById("tg-meta");
    if (meta) {
      var pnl = tr.reduce(function (s, t) { return s + (t.pnl || 0); }, 0);
      meta.textContent = (d._meta ? d._meta.nb_trades : tr.length) + " trades · PNL " +
        (pnl >= 0 ? "+" : "") + pnl.toFixed(2) + " $ · depuis " + ((d._meta && d._meta.since) || "?");
    }

    var ctx = cv.getContext("2d");
    var dpr = window.devicePixelRatio || 1;
    var W = cv.clientWidth || 400, H = cv.clientHeight || 240;
    cv.width = W * dpr; cv.height = H * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, W, H);

    var prices = k.c.concat(tr.map(function (t) { return t.entry; }), tr.map(function (t) { return t.exit; }));
    if (!prices.length) {
      ctx.fillStyle = "#6b7686";
      ctx.font = "11px ui-monospace,Menlo";
      ctx.fillText("Pas encore de trades sur ce run — le graphique se remplit en direct.", 12, H / 2);
      return;
    }
    var lo = Math.min.apply(null, prices), hi = Math.max.apply(null, prices);
    var pad = Math.max((hi - lo) * 0.08, 1);
    var ymin = lo - pad, ymax = hi + pad;
    var t0, t1;
    if (k.t.length >= 2) { t0 = k.t[0]; t1 = k.t[k.t.length - 1]; }
    else if (tr.length >= 2) { t0 = tr[0].ts_ms; t1 = tr[tr.length - 1].ts_ms; }
    else if (tr.length === 1) { t0 = tr[0].ts_ms - 600000; t1 = tr[0].ts_ms + 600000; }
    else { t0 = Date.now() - 3600000; t1 = Date.now(); }

    function x(ts) { return 12 + (ts - t0) / (t1 - t0) * (W - 24); }
    function y(px) { return 8 + (ymax - px) / (ymax - ymin) * (H - 30); }

    // grille
    ctx.strokeStyle = "#1c2330"; ctx.fillStyle = "#6b7686";
    ctx.font = "9px ui-monospace,Menlo";
    for (var i = 0; i <= 4; i++) {
      var px = ymin + (ymax - ymin) * i / 4;
      var yy = y(px);
      ctx.beginPath(); ctx.moveTo(12, yy); ctx.lineTo(W - 12, yy); ctx.stroke();
      ctx.fillText(px.toFixed(0), 1, yy - 2);
    }

    // courbe prix
    ctx.strokeStyle = "#58a6ff"; ctx.lineWidth = 1.3; ctx.beginPath();
    for (var i = 0; i < k.t.length; i++) {
      var xx = x(k.t[i]), yy = y(k.c[i]);
      if (i === 0) ctx.moveTo(xx, yy); else ctx.lineTo(xx, yy);
    }
    ctx.stroke();

    // points trades (fusion ALPHA+BETA, on dessine les derniers 300 max)
    var recent = tr.slice(-300);
    recent.forEach(function (t) {
      var xx = x(t.ts_ms), yy = y(t.entry);
      var green = t.side === "BUY";
      ctx.beginPath();
      ctx.fillStyle = green ? "#3fb950" : "#f85149";
      ctx.strokeStyle = "#0d1117"; ctx.lineWidth = 1;
      ctx.arc(xx, yy, 3.5, 0, Math.PI * 2);
      ctx.fill(); ctx.stroke();
      // croix de sortie
      var yy2 = y(t.exit);
      ctx.strokeStyle = "#e3b341"; ctx.lineWidth = 1;
      var s = 3.5;
      ctx.beginPath();
      ctx.moveTo(xx - s, yy2 - s); ctx.lineTo(xx + s, yy2 + s);
      ctx.moveTo(xx + s, yy2 - s); ctx.lineTo(xx - s, yy2 + s);
      ctx.stroke();
    });

    // infobulle
    cv.onmousemove = function (e) {
      var r = cv.getBoundingClientRect();
      var mx = e.clientX - r.left, my = e.clientY - r.top;
      var near = null, best = 12;
      recent.forEach(function (t) {
        var dd = Math.hypot(x(t.ts_ms) - mx, y(t.entry) - my);
        if (dd < best) { best = dd; near = t; }
      });
      if (near) {
        var col = near.pnl > 0 ? "#4ade80" : near.pnl < 0 ? "#f87171" : "#8b98a8";
        tip.style.display = "block";
        tip.style.left = (e.clientX + 12) + "px";
        tip.style.top = (e.clientY - 8) + "px";
        tip.innerHTML = "<b>" + near.ts + "</b> " + near.side + "<br>entrée <b>" + near.entry.toFixed(1) +
          "</b> → sortie <b>" + near.exit.toFixed(1) + "</b><br>pnl <b style='color:" + col + "'>" +
          (near.pnl >= 0 ? "+" : "") + near.pnl.toFixed(3) + " $</b> · " + (near.reason || "");
      } else {
        tip.style.display = "none";
      }
    };
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", buildPanel);
  } else {
    buildPanel();
  }
})();

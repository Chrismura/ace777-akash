/* =============================================================================
 * whales_panel.js — Panneau ONCHAIN du cockpit (gros mouvements BTC)
 * Lit : ../thermo/live.json (chiffres bruts) + ../data/whales_scan_latest.json
 *       + ../data/whales_vue_ensemble.json (vue 24h in/out/net, 24/08)
 * Affiche des PHRASES lisibles en français (pas des nombres bruts) :
 *   - chaque gros bloc : qui envoie -> vers qui -> ce que ça veut dire
 *   - vue 24h : par portefeuille connu, reçu / envoyé / net + interprétation
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

  // Nom court et lisible d'un portefeuille ("Binance Cold Storage #2" -> "Binance Cold #2")
  function nomCourt(label) {
    if (!label) return "inconnu";
    var s = String(label)
      .replace(/Cold Storage/g, "Cold")
      .replace(/Cold Wallet/g, "Cold")
      .replace(/Custodian/g, "")
      .replace(/Hack Recovery/g, "hack")
      .replace(/Confiscated/g, "")
      .replace(/Hack Wallet/g, "hack")
      .replace(/\s{2,}/g, " ")
      .trim();
    if (s === "Whale dormant non identifie") return "baleine dormante inconnue";
    return s;
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
      "#" + PANEL_ID + " { position: fixed; right: 12px; bottom: 12px; z-index: 9999;",
      "  width: 330px; max-height: 74vh; overflow-y: auto; background: rgba(10,14,22,0.95);",
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
      "  border-radius: 6px; padding: 6px 8px; margin-top: 6px; font-size: 11px; }",
      "#" + PANEL_ID + " .wp-mv b { color: #fcd34d; }",
      "#" + PANEL_ID + " .wp-mv small { color: #aab6c4; }",
      "#" + PANEL_ID + " .wp-ts { color: #6b7686; font-size: 10px; margin-top: 8px; }",
      "#" + PANEL_ID + " .wp-vue { border-bottom: 1px solid rgba(255,255,255,0.08); padding: 10px 12px; }",
      "#" + PANEL_ID + " .wp-vue-titre { font-size: 11px; font-weight: 700; letter-spacing: 0.6px; margin-bottom: 5px; }",
      "#" + PANEL_ID + " .wp-vue-global { font-size: 11px; line-height: 1.55; margin-bottom: 7px; }",
      "#" + PANEL_ID + " .wp-vue-phrase { font-size: 11px; line-height: 1.5; color: #aab6c4; margin-bottom: 3px; }",
      "#" + PANEL_ID + " .wp-vue-phrase b { color: #d8e0ea; }",
      "#" + PANEL_ID + " .wp-vue-quiet { font-size: 10px; color: #6b7686; margin-top: 6px; line-height: 1.45; }",
      "#" + PANEL_ID + " .wp-vue-legend { font-size: 10px; color: #5c6780; margin-top: 6px; }",
    ].join("\n");
    document.head.appendChild(style);

    var panel = document.createElement("div");
    panel.id = PANEL_ID;
    panel.innerHTML =
      '<div class="wp-head" id="wp-head">' +
      '<span class="wp-title">🐋 ONCHAIN <span class="wp-badge" id="wp-badge">…</span></span>' +
      '<span style="color:#8b98a8" id="wp-toggle">▾</span></div>' +
      '<div class="wp-vue" id="wp-vue"></div>' +
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
    refreshVue();
    setInterval(refresh, REFRESH_MS);
    setInterval(refreshVue, REFRESH_MS);
  }

  // ---------------------------------------------------------------------------
  // VUE 24H — phrases lisibles par portefeuille connu + lecture globale
  // ---------------------------------------------------------------------------
  function refreshVue() {
    var el = document.getElementById("wp-vue");
    if (!el) return;
    fetchJSON("../data/whales_vue_ensemble.json")
      .then(function (v) {
        var t = v.total || {};
        var lecture = t.lecture || "NEUTRE";
        var nb = (v.par_entite || []).length;
        var cls = lecture === "ACCUMULATION" ? "wp-up" : (lecture === "DISTRIBUTION" ? "wp-down" : "");
        var signe = t.net_btc >= 0 ? "+" : "";

        var html = '<div class="wp-vue-titre">VUE 24H · <span class="' + cls + '">' + lecture + "</span></div>";

        // Phrase globale : ce que ça veut dire, en clair
        var verbe = lecture === "ACCUMULATION" ? "ils stockent plus qu'ils ne sortent" :
          (lecture === "DISTRIBUTION" ? "ils relâchent plus qu'ils ne reçoivent" : "situation équilibrée");
        html += '<div class="wp-vue-global">Les <b>' + nb + "</b> portefeuilles surveillés ont reçu <b>" +
          fmt(t.in_btc, 0) + " BTC</b> et envoyé <b>" + fmt(t.out_btc, 0) + " BTC</b> en 24 h " +
          "(net <b class=\"" + (t.net_btc >= 0 ? "wp-up" : "wp-down") + '">' + signe + fmt(t.net_btc, 0) +
          " BTC</b>) — <b>" + verbe + ".</b></div>";

        // Par entité : une phrase par portefeuille qui a bougé
        (v.par_entite || []).forEach(function (d) {
          if (!d.net_btc) return;
          var nom = nomCourt(d.label);
          var n = d.n_mouvements || 0;
          var mvts = n + " mouvement" + (n > 1 ? "s" : "");
          var phrase;
          if (d.in_btc > 0 && d.out_btc > 0) {
            // a reçu ET envoyé : on montre les deux + le net
            phrase = "<b>" + nom + "</b> a reçu <b>" + fmt(d.in_btc, 0) + " BTC</b> et envoyé <b>" +
              fmt(d.out_btc, 0) + " BTC</b> en " + mvts + " (net " + (d.net_btc >= 0 ? "+" : "") +
              fmt(d.net_btc, 0) + " BTC) → plutôt <b class=\"" + (d.net_btc >= 0 ? "wp-up" : "wp-down") +
              "\">" + (d.net_btc >= 0 ? "stockage" : "relâche") + "</b>.";
          } else if (d.net_btc > 0) {
            phrase = "<b>" + nom + "</b> a reçu <b>" + fmt(d.in_btc, 0) + " BTC</b> en " + mvts +
              " et n'a rien envoyé → il <b class=\"wp-up\">stocke</b>.";
          } else {
            phrase = "<b>" + nom + "</b> a envoyé <b>" + fmt(d.out_btc, 0) + " BTC</b> en " + mvts +
              " et n'a rien reçu → il <b class=\"wp-down\">relâche</b>.";
          }
          html += '<div class="wp-vue-phrase">' + phrase + "</div>";
        });

        // Acteurs majeurs SILENCIEUX (on les nomme pour qu'on sache qu'ils n'ont pas bougé)
        var typesCalmes = ["etf_custodian", "seized_government", "liquidation_entity", "whale_dormant"];
        var calmes = (v.par_entite || []).filter(function (d) {
          return !d.net_btc && typesCalmes.indexOf(d.type) !== -1;
        }).map(function (d) { return nomCourt(d.label); });
        if (calmes.length) {
          html += '<div class="wp-vue-quiet">Pas de mouvement sur 24 h : ' + calmes.join(" · ") + ".</div>";
        }

        html += '<div class="wp-vue-legend">→ BTC qui ENTRE dans un coffre surveillé = stockage · BTC qui SORT vers l\'extérieur = possible mise sur le marché.</div>';
        el.innerHTML = html;
      })
      .catch(function () { el.innerHTML = ""; });
  }

  // ---------------------------------------------------------------------------
  // ALERTES — gros blocs + fragmentations, racontés en phrases
  // ---------------------------------------------------------------------------
  function decrireSources(g) {
    var labels = (g.sources_label || []).filter(function (l) { return l && l !== "inconnu"; });
    var inconnues = (g.sources_label || []).filter(function (l) { return l === "inconnu"; }).length;
    var uniq = [];
    labels.forEach(function (l) {
      var n = nomCourt(l);
      if (uniq.indexOf(n) === -1) uniq.push(n);
    });
    var parts = [];
    if (uniq.length) parts.push(uniq.join(" et "));
    if (inconnues === 1) parts.push("une adresse inconnue");
    else if (inconnues > 1) parts.push(inconnues + " adresses inconnues");
    if (!parts.length) return "inconnu";
    return parts.join(" + ");
  }

  function decrireCibles(g) {
    var cibles = g.cibles || [];
    var surveille = g.adresse_surveillee;
    var autres = cibles.filter(function (c) { return c.adresse !== surveille; });
    var parts = [];
    if (cibles.some(function (c) { return c.adresse === surveille; })) parts.push(nomCourt(g.label));
    if (autres.length === 1) parts.push("une adresse inconnue");
    else if (autres.length > 1) parts.push(autres.length + " adresses inconnues");
    if (!parts.length) return "inconnu";
    return parts.join(" et ");
  }

  function phraseGrosBloc(g) {
    var montant = fmt(g.btc, 2) + " BTC";
    var estSource = (g.sources || []).indexOf(g.adresse_surveillee) !== -1;
    var estCible = (g.cibles || []).some(function (c) { return c.adresse === g.adresse_surveillee; });
    var nom = nomCourt(g.label);
    var texte, tag, cls;
    if (estSource && estCible) {
      texte = "Mouvement INTERNE entre les coffres " + nom + " et d'autres adresses : consolidation interne, sans effet sur le marché.";
      tag = "INTERNE";
      cls = "";
    } else if (estCible) {
      texte = "Envoi depuis " + decrireSources(g) + " vers <b>" + nom + "</b> — le BTC entre dans les coffres : <b class=\"wp-up\">stockage / accumulation</b>.";
      tag = "ACCUMULE";
      cls = "wp-up";
    } else if (estSource) {
      texte = "Sortie de <b>" + nom + "</b> vers " + decrireCibles(g) + " — le BTC quitte les coffres : <b class=\"wp-down\">possible mise sur le marché</b>.";
      tag = "DISTRIBUE";
      cls = "wp-down";
    } else {
      texte = "Mouvement de " + decrireSources(g) + " vers " + decrireCibles(g) + ".";
      tag = "";
      cls = "";
    }
    return '<div class="wp-mv"><b>Bloc #' + g.hauteur + " · " + montant + "</b>" +
      (tag ? ' <span class="' + cls + '">[' + tag + "]</span>" : "") +
      "<br><small>" + texte + "</small></div>";
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
        body.setAttribute("data-scan-ts", scan.ts || "");
        body.setAttribute("data-nb", scan.nb_surveilles || "");

        var html = "";
        if (n > 0) {
          html += '<div style="margin-bottom:6px;font-size:11px;color:#ffd700">⚠️ Gros mouvements (6 derniers blocs) :</div>';
          (scan.gros_blocs || []).forEach(function (g) {
            html += phraseGrosBloc(g);
          });
          (scan.fragmentations || []).forEach(function (f) {
            html += '<div class="wp-mv">🧩 <b>FRAGMENTATION · ' + fmt(f.btc, 2) + " BTC</b>" +
              "<br><small>Déplacés en petits morceaux depuis " + nomCourt(f.label || f.source) +
              " — une baleine qui fragment pour passer inaperçue.</small></div>";
          });
        } else {
          html += '<div style="color:#6b7686;font-size:11px;margin-bottom:8px">Aucun gros mouvement sur les 6 derniers blocs.</div>';
        }
        body.innerHTML = html;
      })
      .catch(function () {
        badge.textContent = "n/a";
      });

    // 2. Chiffres bruts thermo (independants des mouvements)
    fetchJSON("../thermo/live.json")
      .then(function (t) {
        var cells = [
          ["Funding", (t.funding * 100).toFixed(4) + " %", t.funding > 0 ? "wp-up" : "wp-down"],
          ["Gros trades 24h", fmtUsd(t.whaleUsd || 0) + " (" + (t.whaleN || 0) + ")", t.whaleUsd > 0 ? "wp-up" : ""],
          ["Liq 24h", fmtUsd(t.liq24Usd || 0), ""],
          ["Open Interest", fmt(t.oi) + " BTC", t.chg1h >= 0 ? "wp-up" : "wp-down"],
          ["Fear & Greed", (t.fearGreedLabel || "?") + " " + (t.fearGreed || "—"), (t.fearGreed || 99) <= 40 ? "wp-down" : "wp-up"],
          ["Long/Short", fmt(t.longShort), t.longShort >= 1 ? "wp-up" : "wp-down"],
          ["ETF 24h", fmtUsd(t.etfBtcM ? t.etfBtcM * 1e6 : 0), t.etfBtcM > 0 ? "wp-up" : "wp-down"],
          ["chg 24h", fmt(t.chg24) + " %", t.chg24 >= 0 ? "wp-up" : "wp-down"],
        ];
        var g = '<div class="wp-grid">' + cells.map(function (c) {
          return '<div class="wp-cell" title="' + (c[0] === "Gros trades 24h" ? "Gros prints >= 500k$ sur le carnet Binance Futures (proxy) — différent du scan wallets" : "") +
            '"><span>' + c[0] + "</span><b class=\"" + c[2] + '">' + c[1] + "</b></div>";
        }).join("") + "</div>";
        var tsEl = '<div class="wp-ts">Thermo ' + (t.ts || "") + " · surveillé : " +
          (body.getAttribute("data-nb") || "?") + " portefeuilles · scan " +
          (body.getAttribute("data-scan-ts") || "") + "</div>";
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

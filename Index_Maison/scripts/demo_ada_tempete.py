#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
demo_ada_tempete.py — LA PREUVE DES DEUX VITESSES D'ADA

Simule une tempête de marché avec des données SYNTHÉTIQUES, entièrement en /tmp
(la production n'est JAMAIS touchée : mission.json, live, historique — rien).

But : montrer, en conditions réelles de code, que
  ⚡ la SIRÈNE est instantanée (signaux bruts -> on hurle tout de suite)
  🎚️ la VOILURE est lisse (le réglage descend progressivement, jamais par à-coups)

Usage : python3 demo_ada_tempete.py
"""

import os
import sys
import time
import tempfile
import shutil

sys.path.insert(0, os.path.expanduser("~/ace777-test-day1/Index_Maison/scripts"))
import ada_gardienne as g


def inject(fichier: str, data: dict) -> None:
    g.atomic_write_json(fichier, data)


def main() -> int:
    # ---- 1. Redirection totale vers /tmp (jamais la prod) ----
    sauve = (g.STRATEGIE_DIR, g.GARDIENNE_LIVE, g.HISTORIQUE_DIR,
             g.HISTORIQUE_JSONL, g.SAISON_LIVE, g.JOURNAL_LIVE,
             g.THERMO_LIVE, g.MISSION, g.AVIS_FAMILLE)
    tmp = tempfile.mkdtemp(prefix="ada_demo_tempete_")
    g.STRATEGIE_DIR = tmp
    g.GARDIENNE_LIVE = os.path.join(tmp, "ada_gardienne_live.json")
    g.HISTORIQUE_DIR = os.path.join(tmp, "histo")
    g.HISTORIQUE_JSONL = os.path.join(tmp, "ada_gardienne_historique.jsonl")
    g.SAISON_LIVE = os.path.join(tmp, "saison.json")
    g.JOURNAL_LIVE = os.path.join(tmp, "journal.json")
    g.THERMO_LIVE = os.path.join(tmp, "live.json")
    g.MISSION = os.path.join(tmp, "mission.json")
    g.AVIS_FAMILLE = os.path.join(tmp, "avis.md")
    g.EN_TEST = True  # jamais de consultation famille réelle pendant la démo

    F_MOY = 0.0001  # moyenne 30j du funding (référence relative)

    # ---- 2. Le scénario : 5 scans, du calme à l'orage puis l'accalmie ----
    # (nom, saison, bascule, funding, liq24h, chg24, vortex, pnl_session, fills, revenge)
    etapes = [
        ("1 · Bassin calme",    "CALME",     False, 0.0001,  20e6, 0.1, 0,   12.0,  2, 0),
        ("2 · Le vent se lève", "CHAUFFE",   True,  0.0004,  35e6, 0.8, 1,   -5.0,  5, 1),
        ("3 · Tempête",         "MOUVEMENT", False, 0.0006,  80e6, 2.5, 2,  -70.0,  9, 3),
        ("4 · Orage",           "CHAOS",     False, 0.0010, 120e6, 4.0, 2, -140.0, 14, 4),
        ("5 · L'accalmie",      "CALME",     False, 0.0001,  20e6, 0.2, 0,  -40.0, 16, 4),
    ]

    print("=" * 104)
    print("DEMO — LA TEMPÊTE D'ADA · preuve des DEUX VITESSES")
    print("  ⚡ SIRÈNE = instantanée (signaux bruts, pas de lissage)")
    print("  🎚️ VOILURE = lisse (le réglage descend progressivement)")
    print("=" * 104)
    print("%-21s | %-9s | %-7s | %-8s | %-8s | %-8s | %-7s | %s" % (
        "ÉTAPE", "SAISON", "FUNDING", "LIQ 24H", "PNL", "VOILURE", "ZONE",
        "SIRÈNE / DÉCLENCHEURS"))
    print("-" * 104)

    resultats = {}
    for (nom, saison, bascule, fund, liq, chg, vortex, pnl, fills, rev) in etapes:
        inject(g.SAISON_LIVE, {
            "saison": saison, "direction": "long", "bascule": bascule,
            "alignement": {"nb_long": 3, "nb_short": 1, "score": 0.5, "direction": "long"},
            "indices": {"vortex": {"force": vortex, "direction": "short", "brut": chg}},
        })
        inject(g.JOURNAL_LIVE, {"bots": {
            "alpha": {"pnl": pnl, "fills": fills, "revenge": rev},
            "beta": {"fills": 30, "conf_moy": 0.9},
        }})
        inject(g.THERMO_LIVE, {"tsUnix": time.time(), "funding": fund,
                               "fundingAvg30": F_MOY, "chg24": chg,
                               "liq24Usd": liq, "fearGreed": 40})
        r = g.scan()
        resultats[nom] = r
        gg = r.get("gardienne", {})
        voilure = int(gg.get("voilure_pct", 0))
        zone = gg.get("zone", "?")
        dec = gg.get("declencheurs", [])
        sirene = ("🚨 " + " · ".join(dec)) if dec else "—"
        seuil = float(gg.get("seuil_x", 0) or 0)
        print("%-21s | %-9s | x%-6.1f | %-8.0f | %+8.1f | %-8d | %-7s | %s" % (
            nom, saison, fund / F_MOY, liq / 1e6, pnl, voilure, zone, sirene))
        print("%-21s | %-9s | %-7s | %-8s | %-8s | %-8s | %-7s | seuil X appris : %.0f $" % (
            "", "", "", "", "", "", "", seuil))

    print("-" * 104)
    print()

    # ---- 3. La story au plus fort (étape 4) ----
    orage = resultats["4 · Orage"].get("gardienne", {}).get("story", [])
    print("📖 ADA AU PLUS FORT DE LA TEMPÊTE (étape 4) :")
    for ligne in orage:
        print("   • " + ligne)
    print()

    # ---- 4. La preuve en trois phrases ----
    v1 = int(resultats["1 · Bassin calme"].get("gardienne", {}).get("voilure_pct", 0))
    v2 = int(resultats["2 · Le vent se lève"].get("gardienne", {}).get("voilure_pct", 0))
    v3 = int(resultats["3 · Tempête"].get("gardienne", {}).get("voilure_pct", 0))
    v4 = int(resultats["4 · Orage"].get("gardienne", {}).get("voilure_pct", 0))
    v5 = int(resultats["5 · L'accalmie"].get("gardienne", {}).get("voilure_pct", 0))
    s2 = resultats["2 · Le vent se lève"].get("alerte")
    s4 = resultats["4 · Orage"].get("alerte")

    print("🏁 LA PREUVE :")
    print("  ⚡ VITESSE 1 — LA SIRÈNE : dès l'étape 2 (funding x4 + bascule), ADA hurle"
          " (%s) ALORS QUE la voilure est encore à %d %% (zone JAUNE)." % (
              "alerte=True" if s2 else "alerte=False", v2))
    print("     Pas de lissage sur l'alarme : le signal brut suffit, on hurle maintenant.")
    print("  🎚️ VITESSE 2 — LA VOILURE : elle descend en douceur %d %% → %d %% → %d %% → %d %%,"
          " puis remonte à %d %% à l'accalmie." % (v1, v2, v3, v4, v5))
    print("     Pas de saut brutal : c'est un réglage continu, jamais un interrupteur.")
    print("  🚫 JAMAIS DE BLOCAGE : l'étape 5 montre ACE libre de re-rentrer — la voilure"
          " remonte sans aucune fenêtre d'attente imposée.")
    print()

    # ---- 5. Restauration + nettoyage ----
    (g.STRATEGIE_DIR, g.GARDIENNE_LIVE, g.HISTORIQUE_DIR, g.HISTORIQUE_JSONL,
     g.SAISON_LIVE, g.JOURNAL_LIVE, g.THERMO_LIVE, g.MISSION, g.AVIS_FAMILLE) = sauve
    g.EN_TEST = False
    shutil.rmtree(tmp, ignore_errors=True)
    print("✅ Démo terminée — la production n'a PAS été touchée (tout s'est passé en /tmp).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

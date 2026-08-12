#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
demo_ada_cockpit.py — LA TEMPÊTE D'ADA, EN DIRECT DANS LE COCKPIT

Ouvre le cockpit (icône bureau) → onglet THERMO → regarde le panneau ADA :
  🟢 la voile est grande → 🟡 le vent se lève (la sirène hurle) → 🔴 tempête
  → ⛔ prends la perte → 🟢 l'accalmie (retour au réel).

Principe : un drapeau (ada_demo.flag) dit à ADA de jouer des données
SYNTHÉTIQUES au lieu des vraies. Chaque étape est écrite puis le feed est
régénéré → le cockpit (rafraîchi ~10 s) montre la tempête en direct.
À la fin, le drapeau est retiré : ADA revient au réel toute seule.
  - Si le script est interrompu, ADA revient aussi au réel (try/finally).
  - Si le drapeau reste coincé, ADA l'ignore après 20 min (auto-réparation).

Usage : python3 demo_ada_cockpit.py [--pas 12]
       (--pas = secondes affichées par étape, 5 étapes au total)
"""

import argparse
import atexit
import json
import os
import subprocess
import sys
import time

ROOT = os.path.expanduser("~/ace777-test-day1")
STRAT = os.path.join(ROOT, "Index_Maison", "strategie")
SCRIPTS = os.path.join(ROOT, "Index_Maison", "scripts")
FLAG = os.path.join(STRAT, "ada_demo.flag")
DATA = os.path.join(STRAT, "ada_demo_data.json")

F_MOY = 0.0001  # moyenne 30j de référence (synthétique)

# (nom, saison, bascule, funding, liq24h, chg24, vortex, pnl_session, fills, revenge)
ETAPES = [
    ("1 · Bassin calme",    "CALME",     False, 0.0001,  20e6, 0.1, 0,   12.0,  2, 0),
    ("2 · Le vent se lève", "CHAUFFE",   True,  0.0004,  35e6, 0.8, 1,   -5.0,  5, 1),
    ("3 · Tempête",         "MOUVEMENT", False, 0.0006,  80e6, 2.5, 2,  -70.0,  9, 3),
    ("4 · Orage",           "CHAOS",     False, 0.0010, 120e6, 4.0, 2, -140.0, 14, 4),
    ("5 · L'accalmie",      "CALME",     False, 0.0001,  20e6, 0.2, 0,  -40.0, 16, 4),
]


def ecrire_etape(saison, bascule, fund, liq, chg, vortex, pnl, fills, rev):
    with open(FLAG, "w", encoding="utf-8") as f:
        json.dump({"ts": time.time()}, f)
    with open(DATA, "w", encoding="utf-8") as f:
        json.dump({
            "saison": {
                "saison": saison, "direction": "long", "bascule": bascule,
                "alignement": {"nb_long": 3, "nb_short": 1, "score": 0.5, "direction": "long"},
                "indices": {"vortex": {"force": vortex, "direction": "short", "brut": chg}},
            },
            "journal": {"bots": {
                "alpha": {"pnl": pnl, "fills": fills, "revenge": rev},
                "beta": {"fills": 30, "conf_moy": 0.9},
            }},
            "thermo": {"tsUnix": time.time(), "funding": fund, "fundingAvg30": F_MOY,
                       "chg24": chg, "liq24Usd": liq, "fearGreed": 40},
        }, f, ensure_ascii=False)


def regenerer_feed():
    subprocess.run([sys.executable, os.path.join(SCRIPTS, "cockpit_mission_feed.py")],
                   capture_output=True, timeout=120)


def lire_affichage():
    """Lit ce que le panneau ADA montrera (gardienne + coup d'œil)."""
    try:
        m = json.load(open(os.path.join(ROOT, "Index_Maison", "cockpit", "mission.json"),
                           encoding="utf-8"))
        g = m.get("gardienne", {}) or {}
        cd = m.get("coup_doeil", {}) or {}
        zone = g.get("zone", "?")
        voilure = g.get("voilure_pct", "?")
        sirene = "🚨" if g.get("sirene") else ""
        return "%s %s voilure %s %% · %s %s" % (
            cd.get("saison_emoji", ""), zone, voilure,
            sirene, " · ".join(g.get("declencheurs", [])))
    except Exception as e:
        return "erreur lecture: %s" % e


def nettoyer():
    for p in (FLAG, DATA):
        try:
            os.remove(p)
        except Exception:
            pass


atexit.register(nettoyer)  # même en cas de sortie imprévue, ADA revient au réel


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pas", type=int, default=12, help="secondes par étape")
    args = parser.parse_args()

    print("=" * 72)
    print("🌩️  DÉMO — LA TEMPÊTE D'ADA, EN DIRECT DANS LE COCKPIT")
    print("    Ouvre le cockpit (icône bureau) → onglet THERMO")
    print("    et regarde le panneau ADA 👁 : il va vivre la tempête.")
    print("=" * 72)
    print()

    try:
        for (nom, saison, bascule, fund, liq, chg, vortex, pnl, fills, rev) in ETAPES:
            ecrire_etape(saison, bascule, fund, liq, chg, vortex, pnl, fills, rev)
            regenerer_feed()
            print("  %-24s -> %s" % (nom, lire_affichage()))
            time.sleep(args.pas)
        print()
        print("✅ Démo terminée — retour au réel...")
    finally:
        nettoyer()
        try:
            regenerer_feed()
        except Exception:
            pass
        print("  %-24s -> %s" % ("retour au réel", lire_affichage()))
        print()
        print("🎬 Si tu as raté un passage, relance : python3 demo_ada_cockpit.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""relancer_fiches_observation.py — boucle J+n des paires en OBSERVATION (05/10/2026).

Consigne Christophe 05/10/2026 (« go 1,2 ») : régénérer les deux fiches
(FICHE_SETUP + FICHE_PROJET) d'IOTAUSDT / LAUSDT / WAXLUSDT après accumulation
de mesures, et COMPARER avec la version du jour 1 (baseline gelée le 05/10).

Chaîne (la même que les actifs tradés, vérifiée jusqu'à la source) :
  suivi_setup_actif.py    → mesures (runs/SUIVI_SETUP_<PAIR>.jsonl)
  analyse_pattern_actif.py → profil (runs/profils_actifs/PROFIL_<PAIR>.json)
  generer_fiches_setup.py  → FICHE_SETUP_<PAIR>_<date>.md
  generer_fiches_projet.py → FICHE_PROJET_<PAIR>_<date>.md
Puis comparaison PROFIL du jour vs PROFIL_JOUR1_<date> sur les champs mesurés,
écrite dans runs/SUIVI_FICHES_OBSERVATION.md (une section par exécution).

Planifié par Index_Maison/plists/com.ace777.fiches-observation.plist (1×/jour).
Usage manuel : python3 scripts/relancer_fiches_observation.py
Recherche pure + fiches : aucun ordre, aucune modification du moteur.
"""
import datetime
import json
import os
import subprocess
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # hulk-mexc/
SCRIPTS = os.path.join(BASE, "scripts")
RUNS = os.path.join(BASE, "runs")
PROFILS = os.path.join(RUNS, "profils_actifs")
SUIVI = os.path.join(RUNS, "SUIVI_FICHES_OBSERVATION.md")
JOUR1 = "20261005"

PAIRS = ["IOTAUSDT", "LAUSDT", "WAXLUSDT"]

CHAMPS = [
    ("pts", "mesures"),
    ("range_total_pct", "range %"),
    ("dd15_moy", "dd15 moy %"),
    ("h_creux", "creux UTC"),
    ("h_pic", "pic UTC"),
    ("corr_btc", "corr BTC"),
    ("mur_bid_max_usd", "mur max $"),
    ("spoof_moy", "spoof %"),
]


def charger_profil(pair, suffixe=""):
    fn = os.path.join(PROFILS, f"PROFIL_{pair}{suffixe}.json")
    try:
        return json.load(open(fn, encoding="utf-8"))
    except Exception:
        return {}


def figer_baseline():
    """Copie le profil du jour 1 UNE SEULE FOIS (jamais écrasée)."""
    for p in PAIRS:
        src = os.path.join(PROFILS, f"PROFIL_{p}.json")
        dst = os.path.join(PROFILS, f"PROFIL_{p}_JOUR1_{JOUR1}.json")
        if os.path.exists(src) and not os.path.exists(dst):
            with open(dst, "w", encoding="utf-8") as f:
                f.write(open(src, encoding="utf-8").read())
            print(f"[baseline] {os.path.basename(dst)} figée (jour 1 = {JOUR1})")


def regenerer():
    """Chaîne complète mesures → profil → 2 fiches. Les erreurs sont affichées, pas avalées."""
    for script in ("suivi_setup_actif.py", "analyse_pattern_actif.py",
                   "generer_fiches_setup.py", "generer_fiches_projet.py"):
        r = subprocess.run(
            [sys.executable, os.path.join(SCRIPTS, script)] + PAIRS,
            capture_output=True, text=True, timeout=600,
        )
        ok = "OK" if r.returncode == 0 else f"ERREUR rc={r.returncode}"
        print(f"[{ok}] {script}")
        if r.returncode != 0:
            print((r.stdout or "")[-400:], (r.stderr or "")[-400:])


def comparer():
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    lignes = [f"\n## {now} — comparaison vs jour 1 ({JOUR1})\n"]
    lignes.append("| paire | champ | jour 1 | aujourd'hui | écart |")
    lignes.append("|---|---|---|---|---|")
    for p in PAIRS:
        j1 = charger_profil(p, f"_JOUR1_{JOUR1}")
        cur = charger_profil(p)
        if not cur:
            lignes.append(f"| {p} | — | — | **profil absent** | — |")
            continue
        for cle, label in CHAMPS:
            a, b = j1.get(cle), cur.get(cle)
            if isinstance(a, (int, float)) and isinstance(b, (int, float)):
                delta = f"{b - a:+.2f}"
            else:
                delta = "—" if a == b else "changé"
            lignes.append(f"| {p} | {label} | {a} | **{b}** | {delta} |")
    with open(SUIVI, "a", encoding="utf-8") as f:
        f.write("\n".join(lignes) + "\n")
    print("\n".join(lignes[:6]))
    print(f"[écrit] {SUIVI}")


def main():
    figer_baseline()
    regenerer()
    comparer()
    print(f"[fin] fiches dans Index_Maison/OUTBOX_OBSIDIAN/Crypto_Projet/ — "
          f"comparaison dans {SUIVI}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""chiffrage_churn_total.py — GO 3 (09/10/2026)

But : chiffrer le COUT DU CHURN sur TOUTES les paires — ce que le moteur a
réalisé en sortant, vs ce que les unités sorties vaudraient au cours du jour
(counterfactuel « tenu »). Décomposition par CLASSE de sortie.

Lecture seule. Ne touche ni au moteur, ni aux positions, ni aux ordres.
Entrées  : runs/PAPER_V1_*_state.json (le plus récent), runs/PAPER_V1_*.csv
Sortie   : hulk-mexc/thermo/churn_total.json  (+ résumé stdout)

Méthode (déclarée, limite assumée) :
  - pour chaque SORTIE (event == SELL) : `gap_sortie = qty*(mark_jour - price)`.
    > 0  => on a sorti AVANT la hausse (argent laissé sur la table)
    < 0  => on a sorti AVANT la baisse (la sortie a protégé)
  - le mark « jour » vient de scores[pair].price (state), seul prix commun à
    toutes les paires, y compris celles dont la position est close.
  - `realise` = somme des pnl_usdt des SELL (frais inclus par le moteur).

!! ATTENTION — LIRE AVANT D'UTILISER LE TOTAL !!  (limite R8, assumée)
  `gap_sorties_total` est un MAJORANT, pas un P&L. Il somme chaque sortie
  indépendamment : une unité vendue, rachetée, revendue est comptée DEUX fois.
  Le vrai écart Hulk-vs-HOLD (non double-compté) est celui du cockpit
  (`mission.json -> hulk.hulkVsHold.pairs[].ecart`) — le script le lit et le
  publie en `ecart_reel_pairs` pour recoupement. Le majorant sert à LOCALISER
  où les sorties tombent (station de diagnostic), pas à annoncer une perte.
"""
import csv, glob, json, os, sys
from collections import defaultdict
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                      # hulk-mexc/
RUNS = os.path.join(ROOT, "runs")
THERMO = os.path.join(ROOT, "thermo")


def _latest(pattern):
    hits = glob.glob(os.path.join(RUNS, pattern))
    return max(hits, key=os.path.getmtime) if hits else None


def _classe(reason: str) -> str:
    """Range une raison de sortie dans une classe lisible."""
    r = (reason or "").lower()
    if "trail" in r or "giveback" in r:
        return "trailing_giveback"
    if "crash" in r:
        return "crash_dd"
    if "stop" in r:
        return "stop"
    if "stake_out" in r:
        return "stake_out_multiple"
    if "rip" in r or "take" in r or "p1" in r or "p2" in r:
        return "prise_partielle_rip"
    if "sell" in r:
        return "autre_vente"
    return "inconnu"


def main():
    state_p = _latest("PAPER_V1_*_state.json")
    csv_p = _latest("PAPER_V1_*.csv")
    if not state_p or not csv_p:
        print("REFUS : état ou journal introuvable dans runs/", file=sys.stderr)
        return 2
    state = json.load(open(state_p, encoding="utf-8"))
    scores = state.get("scores", {})
    marks = {p: s.get("price") for p, s in scores.items() if isinstance(s, dict)}

    realise = defaultdict(float)
    n_sorties = defaultdict(int)
    cout_par_classe = defaultdict(float)
    cout_par_paire = defaultdict(float)
    n_par_classe = defaultdict(int)
    detail = []
    lignes = 0
    with open(csv_p, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            lignes += 1
            if (row.get("event") or "").upper() != "SELL":
                continue
            pair = row.get("pair")
            try:
                qty = float(row.get("qty") or 0)
                price = float(row.get("price") or 0)
                pnl = float(row.get("pnl_usdt") or 0)
            except ValueError:
                continue
            realise[pair] += pnl
            n_sorties[pair] += 1
            cl = _classe(row.get("reason"))
            n_par_classe[cl] += 1
            mark = marks.get(pair)
            if mark:
                cout = qty * (float(mark) - price)
                cout_par_classe[cl] += cout
                cout_par_paire[pair] += cout
                detail.append({"ts": row.get("ts"), "pair": pair, "classe": cl,
                               "qty": qty, "price": price, "mark": float(mark),
                               "cout_opportunite": round(cout, 4),
                               "reason": row.get("reason")})

    tot_realise = sum(realise.values())
    tot_cout = sum(cout_par_classe.values())
    tot_sorties = sum(n_sorties.values())

    # recoupement : l'ecart Hulk-vs-HOLD reel (non double-compte) du cockpit
    ecart_reel = None
    mission_ts = None
    mission_p = os.path.join(os.path.dirname(HERE), "..", "Index_Maison",
                             "cockpit", "mission.json")
    mission_p = os.path.normpath(mission_p)
    try:
        miss = json.load(open(mission_p, encoding="utf-8"))
        rows = miss.get("hulk", {}).get("hulkVsHold", {}).get("pairs", [])
        ecart_reel = round(sum(r.get("ecart", 0) for r in rows), 4)
        mission_ts = miss.get("ts")
    except Exception:
        pass

    par_paire = sorted(
        ({"pair": p, "realise": round(realise[p], 4), "sorties": n_sorties[p],
          "gap_sorties": round(cout_par_paire[p], 4)}
         for p in realise),
        key=lambda d: d["gap_sorties"])

    out = {
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "run": os.path.basename(state_p).replace("_state.json", ""),
        "pnl_total_moteur": state.get("pnl_total"),
        "lignes_journal": lignes,
        "totaux": {
            "sorties": tot_sorties,
            "realise_somme": round(tot_realise, 4),
            "gap_sorties_MAJORANT": round(tot_cout, 4),
            "ecart_reel_pairs": ecart_reel,
            "mission_ts": mission_ts,
        },
        "par_classe": sorted(
            ({"classe": c, "n_sorties": n_par_classe[c],
              "gap_sorties": round(cout_par_classe[c], 4)}
             for c in n_par_classe),
            key=lambda d: d["gap_sorties"]),
        "par_paire": par_paire,
        "note": ("GO3 09/10/2026. gap_sorties = qty*(mark_jour - price) par sortie. "
                 ">0 = argent laisse sur la table ; <0 = la sortie a protege. "
                 "MAJORANT : double-compte les re-entrees. Le vrai ecart est "
                 "ecart_reel_pairs (cockpit). n=1 run (limite R8)."),
    }
    os.makedirs(THERMO, exist_ok=True)
    dst = os.path.join(THERMO, "churn_total.json")
    json.dump(out, open(dst, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    print(f"run            : {out['run']}")
    print(f"sorties        : {tot_sorties}   realise cumule : {tot_realise:+.2f} $")
    print(f"gap sorties vs mark du jour (MAJORANT, double-compte) : {tot_cout:+.2f} $")
    print(f"ecart Hulk-vs-HOLD REEL (cockpit {mission_ts}) : "
          f"{ecart_reel if ecart_reel is not None else 'n/a'} $")
    print("\npar classe de sortie (gap majorant) :")
    for c in out["par_classe"]:
        print(f"  {c['classe']:22} n={c['n_sorties']:4d}  {c['gap_sorties']:+9.2f} $")
    print("\n5 paires au gap le plus FAIBLE (la sortie a protege) :")
    for d in out["par_paire"][:5]:
        print(f"  {d['pair']:12} sorties={d['sorties']:3d}  realise={d['realise']:+8.2f}  "
              f"gap={d['gap_sorties']:+9.2f} $")
    print("\n5 paires au gap le plus ELEVE (argent laisse sur la table) :")
    for d in out["par_paire"][-5:][::-1]:
        print(f"  {d['pair']:12} sorties={d['sorties']:3d}  realise={d['realise']:+8.2f}  "
              f"gap={d['gap_sorties']:+9.2f} $")
    print(f"\n-> {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

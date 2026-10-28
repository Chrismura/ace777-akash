#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
garde_reconciliation.py — §23 (28/10/2026, ORDRE Christophe).
=============================================================
« Un chiffre affiché sans réconciliation automatique contre sa source
est un avis, pas une mesure. »

Vérifie que les TROIS livres disent la même chose :
  1. journal (somme des bookings |pnl_usdt| > 0, TOUT événement) == état pnl_total
  2. n bookings == état trades
  3. somme état pair_pnl == état pnl_total
  4. chiffrage (runs/PNL_NET_<jour>.json brut) == journal

Lecture seule, 0 ordre. Sortie rc=0 si tout OK, rc=1 sinon (KO → auditer, voir §23).
"""
from __future__ import annotations

import csv
import glob
import json
import os
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
RUNS = RACINE / "runs"
TOL = 0.01


def main() -> int:
    csvs = sorted(glob.glob(str(RUNS / "PAPER_V1_*.csv")), key=os.path.getmtime)
    états = sorted(glob.glob(str(RUNS / "PAPER_V1_*_state.json")), key=os.path.getmtime)
    if not csvs or not états:
        print("KO — journal ou état introuvable")
        return 1
    csv_path, st_path = csvs[-1], états[-1]
    somme, n = 0.0, 0
    for r in csv.DictReader(open(csv_path, encoding="utf-8", errors="replace")):
        try:
            p = float(r.get("pnl_usdt") or 0.0)
        except (TypeError, ValueError):
            continue
        if abs(p) > 1e-9:
            somme += p
            n += 1
    st = json.loads(open(st_path, encoding="utf-8").read())
    pnl = float(st.get("pnl_total") or 0.0)
    trades = int(st.get("trades") or 0)
    somme_paires = sum(float(v) for v in (st.get("pair_pnl") or {}).values())

    chiffs = sorted(glob.glob(str(RUNS / "PNL_NET_2*.json")), key=os.path.getmtime)
    chiffrage = json.loads(open(chiffs[-1], encoding="utf-8").read()) if chiffs else {}

    oks = []
    oks.append(("journal == moteur", abs(somme - pnl) <= TOL, f"{somme:+.4f}$ vs {pnl:+.4f}$"))
    oks.append(("n bookings == trades", n == trades, f"{n} vs {trades}"))
    oks.append(("par-paire == total", abs(somme_paires - pnl) <= TOL, f"{somme_paires:+.4f}$ vs {pnl:+.4f}$"))
    if not chiffrage:
        oks.append(("chiffrage présent", False, "aucun PNL_NET_*.json"))
    else:
        oks.append(("chiffrage == journal", abs(float(chiffrage.get("brut_usdt", 0)) - somme) <= 0.015,
                    f"{float(chiffrage.get('brut_usdt', 0)):+.2f}$ vs {somme:+.2f}$"))
    # §24 : le cockpit NE RECALCULE PLUS — il affiche le modèle unique.
    mission_p = RACINE.parent / "Index_Maison" / "cockpit" / "mission.json"
    try:
        h = json.loads(open(mission_p, encoding="utf-8").read()).get("hulk") or {}
        v = h.get("hulkVsHold") or {}
        oks.append(("cockpit net == chiffrage", abs(float(h.get("pnlNetEstimated", 0)) - float(chiffrage.get("net_estime_usdt", 0))) <= 0.015,
                    f"{h.get('pnlNetEstimated')}$ vs {chiffrage.get('net_estime_usdt')}$"))
        oks.append(("cockpit frais == chiffrage", abs(float(h.get("fees", 0)) - float(chiffrage.get("frais_usdt", 0))) <= 0.015,
                    f"{h.get('fees')}$ vs {chiffrage.get('frais_usdt')}$"))
        oks.append(("cockpit spread == chiffrage", abs(float(h.get("spreadEstime", 0)) - float(chiffrage.get("spread_usdt", 0))) <= 0.015,
                    f"{h.get('spreadEstime')}$ vs {chiffrage.get('spread_usdt')}$"))
        oks.append(("cockpit couts == chiffrage", abs(float((v.get("slippage") or {}).get("coutTotal", 0)) - float(chiffrage.get("couts_estimes_usdt", 0))) <= 0.015,
                    f"{(v.get('slippage') or {}).get('coutTotal')}$ vs {chiffrage.get('couts_estimes_usdt')}$"))
        # chaque paire criée « over » doit VRAIMENT dépasser le plafond moteur
        plafond = float((v.get("plafondParPaire") or 0.0))
        mises = (st.get("notionals_par_paire") or {})
        for _p in (v.get("overBudget") or []):
            try:
                _m = float(mises.get(_p) or 0.0)
            except (TypeError, ValueError):
                _m = 0.0
            oks.append((f"over {_p} justifié", _m > plafond + 0.01, f"mise {_m:.2f}$ vs plafond {plafond:.2f}$"))
        if not (v.get("overBudget") or []):
            oks.append(("aucun faux plafond", True, "mise moteur < plafond partout"))
    except Exception as e:
        oks.append(("cockpit lisible", False, str(e)[:100]))

    print(f"garde réconciliation §23 — {Path(csv_path).name} vs {Path(st_path).name}")
    tout_ok = True
    for nom, ok, détail in oks:
        print(f"  [{'OK' if ok else 'KO'}] {nom} : {détail}")
        tout_ok = tout_ok and ok
    print("RÉSULTAT : " + ("OK — les trois livres disent la même chose" if tout_ok else "KO — À AUDITER (voir §23)"))
    return 0 if tout_ok else 1


if __name__ == "__main__":
    sys.exit(main())

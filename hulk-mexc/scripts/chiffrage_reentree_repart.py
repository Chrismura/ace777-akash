#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
chiffrage_reentree_repart.py — §30 (28/10/2026, ORDRE Christophe : « chiffre tout ça »).
=======================================================================================
Question fermée : le repart (90 % des sorties trailing repassent AU-DESSUS sous 7 j,
§29) est-il rattrapable par une RÉ-ENTRÉE tradable ? Si oui, combien ça rapporte —
si non, on enterre la piste.

Règles testées (prix seuls, donc câblables, observables en live) :
  R0 référence : pas de ré-entrée (le repart est laissé sur la table = 0 $).
  R1 : ré-entrée si close ≥ px_sortie × 1,005 sous 7 j, même qty, même trailing
       (arm daté via git, gb loggé dans la raison), sortie au trailing ou forcée à +14 j.
  R2 : comme R1 mais seuil +2 % (filtre les micro-reparts qui retombent aussitôt).

Garde-fous : pas de lookahead (que des bougies post-sortie), univers = sorties avec
≥14 j de suivi (données fin 28/10), frais ignorés des deux côtés (R8), pics sur
plus-hauts horaires comme §29. Un câblage exigera GO + shadow.
Lecture seule, 0 ordre.
"""
from __future__ import annotations

import csv
import glob
import json
import os
import re
import sys
import time
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chiffrage_trailing_serre import klines_1h, simule  # noqa: E402

RUNS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "runs")
ACHAT = ("BUY", "DCA", "BAG_DCA", "GBAG_PYRAMIDE")
VENTE = ("SELL", "SELL_PARTIAL", "BAG_SELL", "BAG_CRASH")
FIN_DONNEES = int(datetime(2026, 10, 28, 21, 30, tzinfo=timezone.utc).timestamp() * 1000)


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def arm_at(hist, cur, pair, ts_ms):
    best = (cur.get(pair) or 0) or 10.0
    for cts, arms in hist:
        if cts * 1000 <= ts_ms and (arms.get(pair) or 0) > 0:
            best = arms[pair]
    return best


def main() -> int:
    csvs = sorted(glob.glob(os.path.join(RUNS, "PAPER_V1_*.csv")), key=os.path.getmtime)
    rows = list(csv.DictReader(open(csvs[-1], encoding="utf-8", errors="replace")))
    rex = re.compile(r"trailing_peak([\d.]+)pct_giveback([\d.]+)")
    hist = json.load(open(os.path.join(RUNS, "ARM_HIST.json"), encoding="utf-8"))
    profils = json.load(open(os.path.join(os.path.dirname(RUNS), "strategie",
                                          "universe_profils.json"), encoding="utf-8"))
    cur = {p: float((v.get("calib") or {}).get("trail_arm_pct") or 0)
           for p, v in profils.items() if isinstance(v, dict)}

    # sorties trailing avec suivi complet (sortie + 14 j <= fin données)
    exits = []
    for r in rows:
        if r["event"] not in ("SELL", "SELL_PARTIAL"):
            continue
        m = rex.search(r.get("reason") or "")
        if not m:
            continue
        t_ms = int(datetime.fromisoformat(r["ts"].replace("Z", "+00:00")).timestamp() * 1000)
        if t_ms + 14 * 24 * 3600 * 1000 > FIN_DONNEES:
            continue
        exits.append({"ts": r["ts"], "t": t_ms, "pair": r["pair"],
                      "px": _f(r.get("price")), "qty": _f(r.get("qty")),
                      "pnl": _f(r.get("pnl_usdt")), "gb": float(m.group(2)),
                      "arm": arm_at(hist, cur, r["pair"], t_ms)})
    kl_cache: dict[str, list] = {}
    for e in exits:
        if e["pair"] not in kl_cache:
            kl_cache[e["pair"]] = klines_1h(e["pair"])

    print("=== RE-ENTREE après repart (§30) ===")
    print(f"sorties trailing avec suivi ≥14 j : {len(exits)}")

    resultats = {}
    for label, buf in (("R1 : repart +0,5 % → on remonte", 0.5),
                       ("R2 : repart +2 % → on remonte", 2.0)):
        trades = []
        for e in exits:
            kl = kl_cache[e["pair"]]
            decl = e["px"] * (1 + buf / 100.0)
            t_re = None
            for c in kl:
                ts = int(c[0])
                if ts <= e["t"] or ts > e["t"] + 7 * 24 * 3600 * 1000:
                    continue
                if float(c[4]) >= decl:
                    t_re = ts
                    break
            if t_re is None:
                continue
            px_re = decl
            # tenue : même trailing, sortie forcée à +14 j de la RÉ-ENTRÉE
            t_end = t_re + 14 * 24 * 3600 * 1000
            gb, pic, ts_s, px_s = e["gb"], px_re, None, None
            px_arm = px_re * (1 + e["arm"] / 100.0)
            for c in kl:
                ts = int(c[0])
                if ts <= t_re or ts > t_end:
                    continue
                cl, hi = float(c[4]), float(c[2])
                if hi > pic:
                    pic = hi
                if pic >= px_arm and cl < pic * (1 - gb / 100.0):
                    ts_s, px_s = ts, cl
                    break
            if ts_s is None:  # forcée à +14 j
                post = [c for c in kl if int(c[0]) <= t_end]
                px_s = float(post[-1][4]) if post else px_re
                ts_s = t_end
            trades.append((px_s - px_re) * e["qty"])
        pos = [t for t in trades if t > 0]
        resultats[label] = trades
        print(f"{label} : {len(trades)} ré-entrées "
              f"({100 * len(trades) / max(len(exits), 1):.0f} % des sorties), "
              f"PnL ajouté {sum(trades):+.2f} $, "
              f"gagnantes {100 * len(pos) / max(len(trades), 1):.0f} %, "
              f"médiane {sorted(trades)[len(trades) // 2] if trades else 0:+.2f} $/trade")

    tot_reel = sum(e["pnl"] for e in exits)
    print(f"\nPnL réel du sous-ensemble (sans ré-entrée) : {tot_reel:+.2f} $")
    for label, trades in resultats.items():
        print(f"  {label} : {tot_reel + sum(trades):+.2f} $ "
              f"(Δ {sum(trades):+.2f} $ sur {tot_reel:+.2f} $)")
    print("\nR8 : 1 h (pas le carnet), frais ignorés, qty = qty sortie, "
          "suivi ≥14 j exigé. Un câblage exigera GO + shadow.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

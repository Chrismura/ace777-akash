#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
chiffrage_redeploy_adaptatif.py — §33 (28/10/2026, GO Christophe).
==================================================================
« Pas de fixe ! Les temps différent selon période et trend. »
Balayage délai × TTL sur les 28 sorties des 4 paires (§32), + split par
RÉGIME à la sortie (colonne journal) et par FORCE DU TREND (pic trailing
loggé dans la raison : peak ≥10 % = trend fort).

Question : le 24 h / 7 j du shadow est-il le bon, partout, tout le temps ?
Lecture seule, 0 ordre. R8 : 1 h, frais ignorés, pas de lookahead.
"""
from __future__ import annotations

import csv
import glob
import json
import os
import re
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chiffrage_trailing_serre import klines_1h  # noqa: E402

RUNS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "runs")
CIBLES = ("RWAINCUSDT", "TELUSDT", "KITEUSDT", "PYTHUSDT")
FIN_DONNEES = int(datetime(2026, 10, 28, 21, 30, tzinfo=timezone.utc).timestamp() * 1000)


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def _ms(ts):
    return int(datetime.fromisoformat(ts.replace("Z", "+00:00")).timestamp() * 1000)


def main() -> int:
    csvs = sorted(glob.glob(os.path.join(RUNS, "PAPER_V1_*.csv")), key=os.path.getmtime)
    rows = list(csv.DictReader(open(csvs[-1], encoding="utf-8", errors="replace")))
    rex = re.compile(r"trailing_peak([\d.]+)pct_giveback([\d.]+)")
    hist = json.load(open(os.path.join(RUNS, "ARM_HIST.json"), encoding="utf-8"))
    profils = json.load(open(os.path.join(os.path.dirname(RUNS), "strategie",
                                          "universe_profils.json"), encoding="utf-8"))
    cur = {p: float((v.get("calib") or {}).get("trail_arm_pct") or 0)
           for p, v in profils.items() if isinstance(v, dict)}

    def arm_at(pair, ts_ms):
        best = (cur.get(pair) or 0) or 10.0
        for cts, arms in hist:
            if cts * 1000 <= ts_ms and (arms.get(pair) or 0) > 0:
                best = arms[pair]
        return best

    exits = []
    kl_cache: dict[str, list] = {}
    for r in rows:
        if r["event"] not in ("SELL", "SELL_PARTIAL") or r["pair"] not in CIBLES:
            continue
        m = rex.search(r.get("reason") or "")
        if not m:
            continue
        t = _ms(r["ts"])
        if t + 21 * 24 * 3600 * 1000 > FIN_DONNEES:
            continue
        if r["pair"] not in kl_cache:
            kl_cache[r["pair"]] = klines_1h(r["pair"])
        exits.append({"t": t, "pair": r["pair"], "px": _f(r.get("price")),
                      "qty": _f(r.get("qty")), "gb": float(m.group(2)),
                      "peak": float(m.group(1)), "arm": arm_at(r["pair"], t),
                      "regime": (r.get("regime") or "?" )})
    print(f"=== ADAPTATIF délai×TTL + régime/trend (§33) — {len(exits)} sorties ===")

    def tenue(e, px_re, t_re, ttl_j):
        gb, pic = e["gb"], px_re
        px_arm = px_re * (1 + e["arm"] / 100.0)
        t_end = t_re + ttl_j * 24 * 3600 * 1000
        for c in kl_cache[e["pair"]]:
            ts = int(c[0])
            if ts <= t_re or ts > t_end:
                continue
            cl, hi = float(c[4]), float(c[2])
            pic = max(pic, hi)
            if pic >= px_arm and cl < pic * (1 - gb / 100.0):
                return (cl - px_re) * e["qty"]
        post = [c for c in kl_cache[e["pair"]] if int(c[0]) <= t_end]
        return ((float(post[-1][4]) - px_re) * e["qty"]) if post else 0.0

    def joue(delai_h, ttl_j, buf=0.5):
        tot, n = 0.0, 0
        for e in exits:
            t0 = e["t"] + delai_h * 3600 * 1000
            decl = e["px"] * (1 + buf / 100.0)
            t_re = next((int(c[0]) for c in kl_cache[e["pair"]]
                         if t0 < int(c[0]) <= e["t"] + ttl_j * 24 * 3600 * 1000
                         and float(c[4]) >= decl), None)
            if t_re is None:
                continue
            tot += tenue(e, decl, t_re, ttl_j)
            n += 1
        return tot, n

    print(f"\n{'délai × TTL (buf 0,5 %)':>22} {'PnL':>9} {'n':>3}")
    grille = {}
    for dl in (0, 12, 24, 48):
        for ttl in (3, 7, 14):
            tot, n = joue(dl, ttl)
            grille[(dl, ttl)] = (tot, n)
            print(f"  délai {dl:>3} h × TTL {ttl:>2} j : {tot:>+9.2f} {n:>3}")
    best = max(grille, key=lambda k: grille[k][0])
    print(f"\nmeilleur fixe : délai {best[0]} h × TTL {best[1]} j → "
          f"{grille[best][0]:+.2f} $ ({grille[best][1]} trades)")

    # splits sur le meilleur fixe : régime à la sortie + force du trend
    print("\n--- split par régime à la sortie (meilleur fixe) ---")
    dl, ttl = best
    par_reg: dict[str, list] = {}
    for e in exits:
        t0 = e["t"] + dl * 3600 * 1000
        decl = e["px"] * 1.005
        t_re = next((int(c[0]) for c in kl_cache[e["pair"]]
                     if t0 < int(c[0]) <= e["t"] + ttl * 24 * 3600 * 1000
                     and float(c[4]) >= decl), None)
        pnl = tenue(e, decl, t_re, ttl) if t_re else 0.0
        par_reg.setdefault(e["regime"], [0.0, 0])[0] += pnl
        par_reg[e["regime"]][1] += 1 if t_re else 0
    for reg, (tot, n) in sorted(par_reg.items(), key=lambda kv: -kv[1][0]):
        print(f"  {reg:>10} : {tot:>+9.2f} $ ({n} trades)")

    print("\n--- split par force du trend (pic trailing) ---")
    for nom, cond in (("trend fort (pic ≥10 %)", lambda e: e["peak"] >= 10.0),
                      ("trend mou (pic <10 %)", lambda e: e["peak"] < 10.0)):
        tot, n = 0.0, 0
        for e in exits:
            if not cond(e):
                continue
            t0 = e["t"] + dl * 3600 * 1000
            decl = e["px"] * 1.005
            t_re = next((int(c[0]) for c in kl_cache[e["pair"]]
                         if t0 < int(c[0]) <= e["t"] + ttl * 24 * 3600 * 1000
                         and float(c[4]) >= decl), None)
            if t_re is None:
                continue
            tot += tenue(e, decl, t_re, ttl)
            n += 1
        print(f"  {nom} : {tot:+.2f} $ ({n} trades)")
    print("\nR8 : 1 h, frais ignorés. GO + shadow pour câbler l'adaptatif.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

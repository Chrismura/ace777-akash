#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
chiffrage_redeploy_variantes.py — §32 (28/10/2026, GO Christophe).
==================================================================
Question fermée : QUELLE confirmation avant redéploiement, sur les 4 paires qui
rendent (RWAINC, TEL-historique, KITE, PYTH, §31) ? 5 variantes rejouées sur les
sorties trailing avec suivi ≥14 j — même qty, même trailing, sortie forcée +14 j.

  V0 instantané : achat à la clôture de sortie (miroir du cash_redeploy actuel).
  V1 +0,5 % sous 7 j (R1 §30).   V2 +1 % sous 7 j.   V3 +2 % sous 7 j (R2 §30).
  V4 +0,5 % sous 7 j MAIS pas avant 24 h après la sortie (anti-rachat-immédiat).

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
        if t + 14 * 24 * 3600 * 1000 > FIN_DONNEES:
            continue
        if r["pair"] not in kl_cache:
            kl_cache[r["pair"]] = klines_1h(r["pair"])
        exits.append({"t": t, "pair": r["pair"], "px": _f(r.get("price")),
                      "qty": _f(r.get("qty")),
                      "gb": float(m.group(2)), "arm": arm_at(r["pair"], t)})
    print(f"=== VARIANTES confirmation (§32) — {len(exits)} sorties sur {len(CIBLES)} paires ===")

    def tenue(e, px_re, t_re):
        gb, pic = e["gb"], px_re
        px_arm = px_re * (1 + e["arm"] / 100.0)
        t_end = t_re + 14 * 24 * 3600 * 1000
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

    variantes = [
        ("V0 instantané (miroir redeploy)", 0.0, 0),
        ("V1 +0,5 % sous 7 j", 0.5, 0),
        ("V2 +1 % sous 7 j", 1.0, 0),
        ("V3 +2 % sous 7 j", 2.0, 0),
        ("V4 +0,5 % sous 7 j, ≥24 h après", 0.5, 24),
    ]
    for label, buf, delai_h in variantes:
        tot, n, pos = 0.0, 0, 0
        for e in exits:
            t0 = e["t"] + delai_h * 3600 * 1000
            if buf <= 0:
                t_re, px_re = e["t"], e["px"]
            else:
                decl = e["px"] * (1 + buf / 100.0)
                t_re = next((int(c[0]) for c in kl_cache[e["pair"]]
                             if t0 < int(c[0]) <= e["t"] + 7 * 24 * 3600 * 1000
                             and float(c[4]) >= decl), None)
                if t_re is None:
                    continue
                px_re = decl
            pnl = tenue(e, px_re, t_re)
            tot += pnl
            n += 1
            pos += 1 if pnl > 0 else 0
        print(f"{label} : {n} trades, {tot:+.2f} $, "
              f"gagnants {100 * pos / max(n, 1):.0f} %, "
              f"médiane/trade {tot / max(n, 1):+.2f} $ (moyenne)")
    print("\nR8 : 1 h, frais ignorés, qty = qty sortie. GO + shadow pour câbler.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

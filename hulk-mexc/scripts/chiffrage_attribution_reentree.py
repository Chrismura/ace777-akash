#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
chiffrage_attribution_reentree.py — §31 (28/10/2026, GO Christophe).
====================================================================
Question fermée : des +77,56 $ de repart rejoués en R1 (§30), combien les
RÉ-ENTRÉES EXISTANTES du moteur captent-elles VRAIMENT dans leurs PnL au journal ?

Méthode : pour chaque opportunité R1 (paire, sortie trailing, trigger +0,5 % sous 7 j,
tenue trailing 14 j max), on somme le PnL RÉEL des ventes dont la position a été
OUVERTE APRÈS notre sortie (ancre remontée ARRIÈRE, comme §29 — les positions à
cheval sur la sortie sont exclues, Sources conservatrice). Ratio capté = réel / simu.
Lecture seule, 0 ordre. R8 : fenêtres 1 h, frais ignorés des deux côtés.
"""
from __future__ import annotations

import csv
import glob
import json
import os
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chiffrage_trailing_serre import klines_1h  # noqa: E402

RUNS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "runs")
ACHAT = ("BUY", "DCA", "BAG_DCA", "GBAG_PYRAMIDE")
VENTE = ("SELL", "SELL_PARTIAL", "BAG_SELL", "BAG_CRASH")
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

    idx = {id(r): i for i, r in enumerate(rows)}

    def ancre(qty, pair, j):
        need = qty
        for r in reversed(rows[:j]):
            if r["pair"] != pair:
                continue
            if r["event"] in ACHAT:
                need -= _f(r.get("qty"))
                if need <= 1e-9:
                    return _ms(r["ts"])
            elif r["event"] in VENTE:
                need += _f(r.get("qty"))
        return None

    kl_cache: dict[str, list] = {}
    sim_total, reel_total = 0.0, 0.0
    n_opp = n_cap = n_cheval = 0
    par_paire = defaultdict(lambda: [0.0, 0.0, 0])  # simu, réel, n

    for j, r in enumerate(rows):
        if r["event"] not in ("SELL", "SELL_PARTIAL"):
            continue
        m = rex.search(r.get("reason") or "")
        if not m:
            continue
        t_exit = _ms(r["ts"])
        if t_exit + 14 * 24 * 3600 * 1000 > FIN_DONNEES:
            continue
        pair, px_exit, qty = r["pair"], _f(r.get("price")), _f(r.get("qty"))
        if px_exit <= 0 or qty <= 0:
            continue
        if pair not in kl_cache:
            kl_cache[pair] = klines_1h(pair)
        kl = kl_cache[pair]
        decl = px_exit * 1.005
        t_re = next((int(c[0]) for c in kl
                     if t_exit < int(c[0]) <= t_exit + 7 * 24 * 3600 * 1000
                     and float(c[4]) >= decl), None)
        if t_re is None:
            continue
        # tenue R1 simulée
        gb, arm = float(m.group(2)), arm_at(pair, t_exit)
        pic, px_arm = decl, decl * (1 + arm / 100.0)
        t_end = t_re + 14 * 24 * 3600 * 1000
        ts_s = px_s = None
        for c in kl:
            ts = int(c[0])
            if ts <= t_re or ts > t_end:
                continue
            cl, hi = float(c[4]), float(c[2])
            pic = max(pic, hi)
            if pic >= px_arm and cl < pic * (1 - gb / 100.0):
                ts_s, px_s = ts, cl
                break
        if ts_s is None:
            post = [c for c in kl if int(c[0]) <= t_end]
            px_s, ts_s = (float(post[-1][4]), t_end) if post else (decl, t_end)
        sim_pnl = (px_s - decl) * qty
        # réel : ventes de positions ouvertes APRÈS notre sortie, dans la fenêtre
        reel = 0.0
        capte = False
        for k, s in enumerate(rows):
            if s["pair"] != pair or s["event"] not in ("SELL", "SELL_PARTIAL"):
                continue
            t_s = _ms(s["ts"])
            if not (t_exit < t_s <= t_end):
                continue
            a = ancre(_f(s.get("qty")), pair, idx[id(s)])
            if a is None or a <= t_exit:
                if a is not None:
                    n_cheval += 1
                continue
            reel += _f(s.get("pnl_usdt"))
            capte = True
        sim_total += sim_pnl
        reel_total += reel
        n_opp += 1
        n_cap += 1 if capte else 0
        pp = par_paire[pair]
        pp[0] += sim_pnl
        pp[1] += reel
        pp[2] += 1

    print("=== ATTRIBUTION du repart (§31) ===")
    print(f"opportunités R1 : {n_opp}, fenêtres avec vente post-sortie : {n_cap}, "
          f"positions à cheval exclues : {n_cheval}")
    print(f"repart simulé R1 : {sim_total:+.2f} $ · capté réel : {reel_total:+.2f} $ "
          f"· ratio {100 * reel_total / sim_total if sim_total else 0:.0f} %")
    print(f"\n{'paire':>12} {'n':>3} {'simu $':>9} {'réel $':>9} {'capté':>6}")
    for p, (s, v, n) in sorted(par_paire.items(), key=lambda kv: -kv[1][0]):
        print(f"{p:>12} {n:>3} {s:>+9.2f} {v:>+9.2f} "
              f"{100 * v / s if s else 0:>5.0f} %")
    print("\nR8 : attribution conservatrice (positions à cheval exclues), 1 h, "
          "frais ignorés. Câblage éventuel : GO + shadow.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

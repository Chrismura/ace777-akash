#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CHIFFRAGE_SHORT_BTC_SIGNAL_LONG.py — le signal SHORT BTC mesuré sur 38 JOURS RÉELS.

SOURCE : runs/short_btc_signaux.jsonl — l'archive des signaux émis par le module
(31/08 → 08/10, pas ~5 min, 9 678 points) : score, corr_dir_btc, pct_pompe, m6_btc,
move24_btc, session_ok, prix_btc, frais. AUCUN trade inventé : on rejoue la règle.

POURQUOI : la mesure sur 40 trades réels (chiffrage_short_btc_levier.py) a montré que
le score ACTUEL prédit à l'envers (score 7 → −0,67 %, score 8 → −0,31 %) et que le seul
composant à edge positif est `corr_dir_btc ≤ −0,5` (+0,57 %, 6/9). Échantillon trop
mince → on mesure sur 38 jours.

DEUX RÈGLES COMPARÉES (mêmes TP 2 % / SL 1,5 % / TTL 24 h / gating session 08-17 UTC) :
  ACTUEL    : entrée si score ≥ 5 ; sortie si score < 2.
  CORRIGÉ   : entrée si corr_dir ≤ −0,25 ; sortie si corr_dir > −0,10.
              (surchauffe et m6 retirés : mesurés NÉGATIFS.)

SORTIE : nombre de trades, gagnants, espérance %, PnL $ (marge 5 $), et PnL sous levier
de conviction (corr ≤ −0,5 → 50× · ≤ −0,25 → 20×), avec liquidation (MMR 0,4 %).
0 €, aucun ordre.
"""
import json
import os
import statistics as st
from datetime import datetime, timezone

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUNS = os.path.join(BASE, "runs")
SIGNAUX = os.path.join(RUNS, "short_btc_signaux.jsonl")

TP, SL, TTL_H = 2.0, 1.5, 24.0
MARGE = 5.0
MMR = 0.004


def charger():
    out = []
    with open(SIGNAUX, encoding="utf-8") as f:
        for l in f:
            l = l.strip()
            if not l:
                continue
            try:
                d = json.loads(l)
            except Exception:
                continue
            ts = d.get("ts")
            if not isinstance(ts, str):
                continue
            try:
                t = datetime.fromisoformat(ts).timestamp()
            except Exception:
                continue
            if not d.get("frais") or d.get("prix_btc") is None:
                continue
            out.append({"t": t, "px": float(d["prix_btc"]), "score": d.get("score"),
                        "corr": d.get("corr_dir_btc"), "session": d.get("session_ok")})
    out.sort(key=lambda x: x["t"])
    return out


def backtest(s, entree_fn, sortie_fn):
    pos = None
    trades = []
    for x in s:
        if pos:
            px = x["px"]
            if px <= pos["entry"] * (1 - TP / 100):
                trades.append({"pct": TP, "raison": "TP", "corr": pos["corr"]}); pos = None; continue
            if px >= pos["entry"] * (1 + SL / 100):
                trades.append({"pct": -SL, "raison": "SL", "corr": pos["corr"]}); pos = None; continue
            if sortie_fn(x):
                trades.append({"pct": 100 * (pos["entry"] - px) / pos["entry"], "raison": "SIGNAL_ETEINT", "corr": pos["corr"]}); pos = None; continue
            if (x["t"] - pos["t"]) / 3600 >= TTL_H:
                trades.append({"pct": 100 * (pos["entry"] - px) / pos["entry"], "raison": "TIME_OUT", "corr": pos["corr"]}); pos = None; continue
        else:
            if not x["session"]:
                continue
            if entree_fn(x):
                pos = {"entry": x["px"], "t": x["t"], "corr": x["corr"]}
    return trades


def stats(nom, trades, lev_fn=None):
    if not trades:
        print(f"  {nom}: AUCUN trade")
        return
    pnls = [t["pct"] / 100 * MARGE * (lev_fn(t) if lev_fn else 1.0) for t in trades]
    win = sum(1 for t in trades if t["pct"] > 0)
    tot1 = sum(t["pct"] / 100 * MARGE for t in trades)
    print(f"  {nom}")
    print(f"    n={len(trades):3d}  gagnants {win:3d} ({win/len(trades)*100:.0f}%)  "
          f"espérance {st.mean([t['pct'] for t in trades]):+.3f} %")
    print(f"    PnL levier 1 : {tot1:+7.2f} $", end="")
    if lev_fn:
        print(f"    · PnL levier conviction : {sum(pnls):+7.2f} $", end="")
    print()
    par_r = {}
    for t in trades:
        par_r.setdefault(t["raison"], []).append(t["pct"])
    for r in sorted(par_r):
        v = par_r[r]
        print(f"      {r:14s} n={len(v):3d}  espérance {st.mean(v):+.2f} %")


def levier_conviction_corr(t):
    c = t.get("corr")
    if c is None:
        return 10.0
    if c <= -0.5:
        return 50.0
    if c <= -0.25:
        return 20.0
    return 10.0


def main():
    s = charger()
    if not s:
        print("aucun signal exploitable")
        return 1
    d0 = datetime.fromtimestamp(s[0]["t"], tz=timezone.utc).isoformat()
    d1 = datetime.fromtimestamp(s[-1]["t"], tz=timezone.utc).isoformat()
    print("BACKTEST SIGNAL SHORT BTC — archive réelle des signaux")
    print(f"  {len(s)} points · {d0} → {d1}\n")

    cur = backtest(s, lambda x: (x["score"] or 0) >= 5, lambda x: (x["score"] or 0) < 2)
    cor = backtest(s, lambda x: (x["corr"] is not None and x["corr"] <= -0.25),
                   lambda x: (x["corr"] is not None and x["corr"] > -0.10))
    cor5 = backtest(s, lambda x: (x["corr"] is not None and x["corr"] <= -0.5),
                    lambda x: (x["corr"] is not None and x["corr"] > -0.15))

    print("RÈGLES (marge 5 $, TP 2 % / SL 1,5 % / TTL 24 h / session 08-17 UTC) :\n")
    stats("ACTUEL   (score ≥ 5)", cur)
    print()
    stats("CORRIGÉ  (corr ≤ −0,25)", cor, lev_fn=levier_conviction_corr)
    print()
    stats("CORRIGÉ+ (corr ≤ −0,50, haute conviction)", cor5,
          lev_fn=lambda x: 50.0)

    # moitiés chronologiques (R17.3)
    mid = len(s) // 2
    print("\nSTABILITÉ (2 moitiés chronologiques) :")
    for nom, ent, sor in (("ACTUEL  ", lambda x: (x["score"] or 0) >= 5, lambda x: (x["score"] or 0) < 2),
                          ("CORRIGÉ ", lambda x: (x["corr"] is not None and x["corr"] <= -0.25),
                           lambda x: (x["corr"] is not None and x["corr"] > -0.10))):
        t1 = backtest(s[:mid], ent, sor)
        t2 = backtest(s[mid:], ent, sor)
        e1 = st.mean([t["pct"] for t in t1]) if t1 else 0
        e2 = st.mean([t["pct"] for t in t2]) if t2 else 0
        print(f"  {nom} 1re {e1:+.3f} % (n={len(t1)})  ·  2e {e2:+.3f} % (n={len(t2)})  "
              f"{'✅ même signe' if e1*e2 > 0 else '⚠️ signe instable'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

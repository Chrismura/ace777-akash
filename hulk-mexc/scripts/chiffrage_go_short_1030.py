#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GO execution — replay short marge isolee 5$ -> notionnel 10% inventaire.
Question : short 5$ -> 43$ notionnel via levier ~8.6x, entrees corr<=-0.50 uniquement.
Methode : signaux reels short_btc_signaux.jsonl, TP 2% / SL 1.5% / TTL 24h / session 08-17 UTC.
Compare : A actuel levier1 5$ · B notionnel fixe 43$ levier1 (bloque cash) · C marge 5$ x8.6 (meme notionnel, cash libre).
Liq : MMR 0.4%, dist = 1/L - MMR. Si adverse >= dist -> perte marge 5$.
Sortie : n, win, esperance, PnL, max perte trade, nb liq. 2 moities. Lecture seule.
"""
import json, os
from datetime import datetime, timezone
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUNS = os.path.join(BASE, "runs")
SIGNAUX = os.path.join(RUNS, "short_btc_signaux.jsonl")
TP, SL, TTL_H = 2.0, 1.5, 24.0
MARGE = 5.0
NOTIONNEL_CIBLE = 43.0
L = NOTIONNEL_CIBLE / MARGE
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

def backtest(s, entree_fn):
    pos = None
    trades = []
    for x in s:
        if pos:
            px = x["px"]
            if px <= pos["entry"] * (1 - TP / 100):
                trades.append({"pct": TP, "px_out": px}); pos = None; continue
            if px >= pos["entry"] * (1 + SL / 100):
                trades.append({"pct": -SL, "px_out": px}); pos = None; continue
            if (x["corr"] is not None and x["corr"] > -0.10):
                trades.append({"pct": 100 * (pos["entry"] - px) / pos["entry"], "px_out": px}); pos = None; continue
            if (x["t"] - pos["t"]) / 3600 >= TTL_H:
                trades.append({"pct": 100 * (pos["entry"] - px) / pos["entry"], "px_out": px}); pos = None; continue
        else:
            if not x["session"]:
                continue
            if entree_fn(x):
                pos = {"entry": x["px"], "t": x["t"]}
    return trades

def pnl(trades, mode):
    tot, liq = 0.0, 0
    worst = 0.0
    liq_dist = (1.0 / L - MMR) * 100.0
    for t in trades:
        p = t["pct"]
        if mode == "A":
            g = p / 100.0 * MARGE
        elif mode == "B":
            g = p / 100.0 * NOTIONNEL_CIBLE
        else:
            adverse = max(0.0, -p)
            if adverse >= liq_dist:
                g = -MARGE; liq += 1
            else:
                g = p / 100.0 * MARGE * L
        tot += g
        worst = min(worst, g)
    return tot, liq, worst

def bloc(titre, trades):
    n = len(trades)
    if not n:
        print(f"{titre}: aucun trade"); return
    w = sum(1 for t in trades if t["pct"] > 0)
    esp = sum(t["pct"] for t in trades) / n
    a, _, wa = pnl(trades, "A")
    b, _, wb = pnl(trades, "B")
    c, liq, wc = pnl(trades, "C")
    print(f"{titre} n={n} win={w}/{n} esp={esp:+.3f}% | A5$:{a:+.2f}$ (worst {wa:+.2f}) | B43$:{b:+.2f}$ (worst {wb:+.2f}) | C5$x{L:.1f}:{c:+.2f}$ liq={liq} worst {wc:+.2f}")

def main():
    s = charger()
    print(f"GO replay short — {len(s)} signaux, levier {L:.1f}x (5$ -> 43$), MMR 0.4%, liq_dist={(1.0/L-MMR)*100:.2f}% vs SL 1.5%")
    corr = lambda x: (x["corr"] is not None and x["corr"] <= -0.50)
    trades = backtest(s, corr)
    bloc("CORR<=-0.50 FULL", trades)
    mid = len(s) // 2
    t2 = sorted(trades, key=lambda t: 0)
    h = len(trades) // 2
    # moities chronologiques approx : coupe à la moitié des signaux -> rejoue separement
    s1, s2 = [x for x in s if x["t"] <= s[mid]["t"]], [x for x in s if x["t"] > s[mid]["t"]]
    bloc("h1", backtest(s1, corr))
    bloc("h2", backtest(s2, corr))

if __name__ == "__main__":
    raise SystemExit(main())

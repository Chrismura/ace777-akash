#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CHIFFRAGE_SHORT_BTC_LEVIER.py — le levier MEXC appliqué aux VRAIS trades du SHORT BTC.

QUESTION (Christophe, 08/10/2026) : « améliorer le BTC, considère un plan pour utiliser
le max de levier MEXC. » Décision : MESURER (1) avant de câbler (2).

FAITS MEXC (vérifiés) : BTCUSDT perp, levier max 200×, MMR (maintenance margin) 0,4 %
au tier 1. Distance de liquidation d'un short ≈ (1/levier − MMR). Donc :
  10× → liq +9,6 %  ·  20× → +4,6 %  ·  50× → +1,6 %  ·  100× → +0,6 %  ·  200× → +0,1 %.
Un SL de 1,5 % n'est VIVANT que si liq > 1,5 %, soit levier < ~52. Au-delà, le prix est
liquidé AVANT le stop.

MÉTHODE :
  - trades = journal réel (runs/short_btc_journal.csv), ENTRÉES INCHANGÉES.
  - marge FIXE = 5 $ (le notionnel actuel), notional = levier × marge.
  - paliers de conviction : score ≤5 → 10× · 6-7 → 20× · 8-9 → 35× · 10 → 50×.
  - liquidation : mouvement adverse (= −pnl_pct pour un short) ≥ (1/levier − 0,004) → perte
    = la marge entière. (Proxy PRUDENT : on n'a que le prix de sortie, pas le pic
    intratrade — la liquidation est donc SOUS-estimée.)
  - on imprime aussi l'ESPÉRANCE PAR PALIER DE SCORE (le vrai préalable au levier : un
    levier ne crée pas un edge, il le multiplie).

LIMITE DÉCLARÉE : sans tick intratrade, un trade gagnant ayant plongé puis remonté n'est
pas vu comme liquidé → le risque réel est ≥ à celui affiché. 0 €, aucun ordre.
"""
import csv
import os
import statistics as st

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUNS = os.path.join(BASE, "runs")
JOURNAL = os.path.join(RUNS, "short_btc_journal.csv")
MARGE = 5.0
MMR = 0.004


def levier_de(score):
    s = int(score or 0)
    if s >= 10:
        return 50.0
    if s >= 8:
        return 35.0
    if s >= 6:
        return 20.0
    return 10.0


def charger():
    out = []
    with open(JOURNAL, newline="", encoding="utf-8", errors="ignore") as f:
        for r in csv.DictReader(f):
            if (r.get("detail_signal") or "").strip() == "test":
                continue
            try:
                pct = float(r["pnl_pct"])
                sc = r.get("score_entree")
                sc = int(sc) if sc not in (None, "") else 0
            except Exception:
                continue
            out.append({"pct": pct, "score": sc, "raison": r.get("raison_sortie")})
    return out


def pnl_leverage(t, L):
    """PnL $ d'un trade sous levier L (marge fixe), avec liquidation."""
    adverse = max(0.0, -t["pct"])                 # un short perd si BTC monte
    liq_dist = (1.0 / L - MMR) * 100.0
    if adverse >= liq_dist:
        return -MARGE, True                        # liquidé → marge perdue
    return t["pct"] / 100.0 * MARGE * L, False


def bloc(titre, v):
    if not v:
        return
    cur = sum(t["pct"] / 100.0 * MARGE for t in v)          # levier 1 (actuel, pas 5$×L)
    lev, liq_n = 0.0, 0
    for t in v:
        L = levier_de(t["score"])
        g, liq = pnl_leverage(t, L)
        lev += g
        liq_n += 1 if liq else 0
    print(f"  --- {titre} (n={len(v)}) ---")
    print(f"    ACTUEL  (levier 1, notional 5$)      : {cur:+8.3f} $")
    print(f"    LEVIER conviction (10/20/35/50×)     : {lev:+8.3f} $   "
          f"[{liq_n} liquidation(s)]")
    print(f"    → Δ : {lev-cur:+.3f} $" + (f"  ◗ {liq_n} trade(s) liquidés" if liq_n else ""))


def main():
    trades = charger()
    if not trades:
        print("aucun trade dans le journal")
        return 1
    print("CHIFFRAGE SHORT BTC + LEVIER — marge fixe 5 $, MMR 0,4 %")
    print(f"  {len(trades)} trades réels (hors self-test)\n")

    bloc("TOUT", trades)
    t2 = sorted(trades, key=lambda x: x["score"])
    cut = len(t2) // 2
    print()
    bloc("score INFÉRIEUR (moitié)", t2[:cut])
    print()
    bloc("score SUPÉRIEUR (moitié)", t2[cut:])

    print("\n  -- ESPÉRANCE (en % du notionnel, levier 1) PAR PALIER DE SCORE --")
    print("     (c'est LE préalable : un levier multiplie l'edge, il ne le crée pas)")
    par_sc = {}
    for t in trades:
        par_sc.setdefault(t["score"], []).append(t)
    for s in sorted(par_sc):
        v = par_sc[s]
        exp = st.mean([t["pct"] for t in v])
        win = sum(1 for t in v if t["pct"] > 0)
        # PnL levérisé pour ce palier seul
        L = levier_de(s)
        pnlL = sum(pnl_leverage(t, L)[0] for t in v)
        pnl1 = sum(t["pct"] / 100.0 * MARGE for t in v)
        print(f"    score {s:2d} : n={len(v):2d}  espérance {exp:+6.2f} %  "
              f"gagnants {win}/{len(v)}  |  PnL lév.1 {pnl1:+6.3f}$ → L{L:.0f}× {pnlL:+7.3f}$")

    print("\n  -- par raison de sortie --")
    par_r = {}
    for t in trades:
        par_r.setdefault(t["raison"], []).append(t)
    for r in sorted(par_r):
        v = par_r[r]
        print(f"    {r:15s} n={len(v):2d}  espérance {st.mean([t['pct'] for t in v]):+6.2f} %")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

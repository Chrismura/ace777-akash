#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mesure_core_filet.py — BAC À SABLE (lecture seule, 0 ordre, exit 0 toujours).

QUESTION (ordre Christophe 03/11) : trois souches `kind="core"` perdent en latent
(CHIP -20,25 $ · EDEL -14,19 $ · RIZE -10,01 $). Pourquoi, et comment améliorer
SANS seuil fixe ?

DIAGNOSTIC CODE (mesuré, pas supposé) : `paper_diprip.manage_bag()` fait pour une
souche core `high = max(high, price)` puis `return` — la mesure du plus-haut est
ENTRETENUE mais JAMAIS LUE. La seule règle appliquée à une souche est « jamais
vendue par une règle », c'est-à-dire un seuil fixe à l'infini (interdit maison).

MÉTHODE (aucune constante métier en dur) :
1. σ par paire MESURÉE : écart-type des rendements log 1 h sur fenêtre glissante
   de 360 barres (15 j — la même fenêtre que `score_pair`), par paire, à chaque heure.
2. Bande de sortie MESURÉE et déformable : dd_from_high > k × σ_15j × √(heures
   depuis le plus-haut). Aucune durée fixe, aucune distance fixe : la bande
   s'élargit avec le temps passé au plus-haut (bruit accumulé).
3. Grille k = 1..6 (k est CHOISI par les chiffres, pas imposé), f = 0,5 / 1,0.
4. Contrefactuel par souche réelle (vraie date/prix/qty du state) : hold vs filet,
   sur les klines 1 h réelles, jusqu'au dernier barreau caché.
5. Lecture : $ sauvés sur les perdantes, $ coûtés sur les gagnantes, solde net,
   et stabilité sur deux moitiés (souches ouvertes avant/après le 15/10).

LIMITE DÉCLARÉE (R8) : `runs/KLINES_1H` s'arrête au 2026-10-28 20h — la mesure
ne couvre PAS la jambe du crash du 29/10. Le résultat est donc un minorant :
il chiffre la dérive LENTE, pas le trou noir. La fraîcheur des klines est
elle-même signalée comme défaut à part.
"""
import glob
import json
import math
import os
import statistics
from datetime import datetime, timezone

ROOT = os.path.expanduser("~/ace777-test-day1/hulk-mexc")
KL = os.path.join(ROOT, "runs/KLINES_1H")
STATE = os.path.join(ROOT, "runs/PAPER_V1_20261103_072654_state.json")
WIN = 360          # 15 j de barres 1 h — même fenêtre que score_pair
K_GRID = [0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 4.0]
F_GRID = [0.5, 1.0]


def ts_ms(iso):
    return datetime.strptime(iso, "%Y-%m-%dT%H:%M:%SZ").replace(
        tzinfo=timezone.utc).timestamp() * 1000.0


def charge_klines():
    out = {}
    for f in sorted(glob.glob(os.path.join(KL, "*.json"))):
        pair = os.path.basename(f).replace(".json", "")
        raw = json.load(open(f))
        bars = [(int(b[0]), float(b[1]), float(b[2]), float(b[3]), float(b[4])) for b in raw]
        bars.sort()
        out[pair] = bars
    return out


def sigma_par_barre(closes):
    """σ glissante des rendements log 1 h, en %, mesurée (pas de constante)."""
    sig = [None] * len(closes)
    rets = [None]
    for i in range(1, len(closes)):
        c0, c1 = closes[i - 1], closes[i]
        rets.append(math.log(c1 / c0) * 100.0 if c0 > 0 and c1 > 0 else None)
    for i in range(len(closes)):
        lo = max(1, i - WIN + 1)
        fen = [r for r in rets[lo:i + 1] if r is not None]
        if len(fen) >= 60:
            sig[i] = statistics.pstdev(fen)
    return sig


def rejoue(bars, sig, t0, entry, qty, k, f):
    """Contrefactuel : hold vs filet mesuré. Retourne (val_hold, val_filet, declenche, px_exit)."""
    idx = [i for i, b in enumerate(bars) if b[0] >= t0]
    if not idx:
        return None
    high = None
    high_i = None
    qty_rest = qty
    cash = 0.0
    decl = False
    px_exit = None
    for i in idx:
        px = bars[i][4]
        s = sig[i]
        if high is None:
            high, high_i = max(px, entry), i
        if px > high:
            high, high_i = px, i
        if not decl and s and high > 0:
            h_h = max(0.0, i - high_i)          # heures depuis le plus-haut (mesuré)
            bande = k * s * math.sqrt(max(1.0, h_h))
            dd = (1.0 - px / high) * 100.0
            if dd > bande:
                q = qty_rest * f
                cash += px * q
                qty_rest -= q
                decl = True
                px_exit = px
                if qty_rest <= 1e-12:
                    break
    last = bars[idx[-1]][4]
    val_hold = qty * last
    val_filet = cash + qty_rest * last
    return val_hold, val_filet, decl, px_exit


def main():
    st = json.load(open(STATE))
    bags = {p: b for p, b in (st.get("bags") or {}).items() if b.get("kind") == "core"}
    kl = charge_klines()
    print("=" * 86)
    print("SOUCHES CORE — mesure du filet (k × σ15j × √h depuis le plus-haut) — klines 1 h")
    print("=" * 86)
    print(f"{'paire':11}{'entrée':>11}{'haut':>11}{'fin':>11}{'dd%haut':>9}{'dd%entrée':>10}{'$ hold':>9}")
    lignes = []
    for pair in sorted(bags):
        b = bags[pair]
        if pair not in kl:
            continue
        bars = kl[pair]
        closes = [x[4] for x in bars]
        sig = sigma_par_barre(closes)
        t0 = ts_ms(b["ts"])
        entry, qty = float(b["entry"]), float(b["qty"])
        hi = max(bars[i][4] for i, x in enumerate(bars) if x[0] >= t0)
        fin = closes[-1]
        lignes.append((pair, b, bars, sig, t0, entry, qty, hi, fin))
        print(f"{pair:11}{entry:>11.6g}{hi:>11.6g}{fin:>11.6g}"
              f"{100*(fin/hi-1):>+8.1f}%{100*(fin/entry-1):>+9.1f}%{qty*fin:>9.2f}")

    print()
    print("GRILLE — solde net $ (filet − hold), cumulé sur les souches mesurables")
    print(f"{'k':>4}{'f':>6}{'gain/perdantes':>17}{'coût/gagnantes':>17}{'NET':>10}{'décl.':>8}")
    best = None
    for k in K_GRID:
        for f in F_GRID:
            gagn, cout, n_decl = 0.0, 0.0, 0
            for (pair, b, bars, sig, t0, entry, qty, hi, fin) in lignes:
                r = rejoue(bars, sig, t0, entry, qty, k, f)
                if not r:
                    continue
                vh, vf, decl, _ = r
                d = vf - vh
                if d > 0:
                    gagn += d
                else:
                    cout += d
                n_decl += 1 if decl else 0
            net = gagn + cout
            print(f"{k:>5.2f}{f:>6.1f}{gagn:>+17.2f}{cout:>+17.2f}{net:>+10.2f}{n_decl:>8}")
            if best is None or net > best[0]:
                best = (net, k, f)
    print()
    print(f"MEILLEUR : k={best[1]:.2f} f={best[2]:.1f} → net {best[0]:+.2f} $")
    if best[1] in (K_GRID[0], K_GRID[-1]):
        print("  ⚠ MÉFIANCE : l'optimum est sur le BORD de la grille. Sur k→0 la sortie se fait")
        print("    au premier tick sous le plus-haut, donc QUASI AU SOMMET : c'est un artefact")
        print("    de mesure (on ne vend pas le sommet qu'on vient de faire). Un k câblable doit")
        print("    être INTÉRIEUR à la grille et positif sur les deux moitiés.")
    print()
    print(f"DÉTAIL PAR SOUCHE pour ce meilleur réglage (k={best[1]:.0f}, f={best[2]:.1f}) :")
    print(f"{'paire':11}{'$ hold':>10}{'$ filet':>10}{'delta':>10}{'sortie px':>12}{'motif':>26}")
    tot = 0.0
    for (pair, b, bars, sig, t0, entry, qty, hi, fin) in lignes:
        vh, vf, decl, px = rejoue(bars, sig, t0, entry, qty, best[1], best[2])
        tot += vf - vh
        motif = "filet" if decl else "aucune sortie"
        print(f"{pair:11}{vh:>10.2f}{vf:>10.2f}{vf-vh:>+10.2f}"
              f"{(px if px else 0):>12.6g}{motif:>26}")
    print(f"{'TOTAL':11}{'':>10}{'':>10}{tot:>+10.2f}")
    print()
    # Stabilité : deux moitiés par date d'ouverture de souche
    mid = ts_ms("2026-10-15T00:00:00Z")
    a, bb = 0.0, 0.0
    for (pair, b, bars, sig, t0, entry, qty, hi, fin) in lignes:
        vh, vf, decl, px = rejoue(bars, sig, t0, entry, qty, best[1], best[2])
        if t0 < mid:
            a += vf - vh
        else:
            bb += vf - vh
    print(f"STABILITÉ (même réglage) — souches ouvertes avant 15/10 : {a:+.2f} $ · après : {bb:+.2f} $")
    print("Lecture : un filet n'est câblable que si NET > 0 ET les deux moitiés de même signe.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

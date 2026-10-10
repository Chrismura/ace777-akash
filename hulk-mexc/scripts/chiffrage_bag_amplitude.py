#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""chiffrage_bag_amplitude.py — « l'amplitude d'EDEL peut-elle faire GROSSIR le bag ? » (10/10/2026)

QUESTION (Christophe, 10/10/2026) : « comment utiliser l'amplitude de edel par exemple pour
augmenter le bag ? » — DÉCISION : MESURER d'abord (paper, 0 €), aucun câblage.

MÊMES CONVENTIONS que `backtest_edel_amplitude.py` (spec G figée le 09/10) :
  - bougies 1 h du cache `runs/replay_cache/<PAIRE>_1h_45j.json` (1080 bougies, 24/08 → 08/10) ;
  - frais = spread_cout_bps de la fiche de la paire (universe_profils.json), par côté ;
  - budget 30 $ par ligne, tranche min budget/8 (pas de poussière) ;
  - SPEC G : entrée `close > SMA24` ET `close > plus-haut des 24 clôtures` ET `close > SMA240`,
    pyramide budget/3 à chaque +8 % au-dessus du dernier ajout (max 3 tranches),
    sortie totale dès une clôture < SMA24. Aucun lookahead (décision à la clôture).

VARIANTES COMPARÉES (mêmes entrées, mêmes bougies, mêmes frais) :
  HOLD  — acheter au 1er signal G, ne JAMAIS vendre (le juge).
  G     — spec G pure : le cash des sorties reste du cash.
  GBAG  — spec G + CONVERSION EN BAG : à chaque sortie, un ordre de rachat est posé à
          0,5×amp7 sous le prix de sortie (même fraction que le trend_add câblé) ;
          si `close` le touche, TOUT le cash disponible est converti en jetons parqués en
          SOUCHE (kind=core) qui n'est JAMAIS vendue, même sous la SMA24. Les re-entrées G
          n'utilisent que le cash restant.

SORTIE par paire : net $ (valeur finale marquée au dernier close − 30 $) · jetons finaux ·
bag = jetons finaux / jetons du HOLD · frais · 2 moitiés chronologiques (chaque moitié
redémarre avec 30 $). Puis somme sur toutes les paires du cache.

LIMITES DÉCLARÉES (R8) : 1 fenêtre de 45 j, bougies 1 h (mèches intra-heure mal vues) ;
amp7 = range journalier médian des 7 jours précédents, jours = blocs de 24 bougies ;
aucun slippage d'impact modellise ; ordre intra-bougie suppose (le creux est touche par la
clôture) ; le rachat « 0,5×amp7 » est CHOISI (convention trend_add), pas prouvé ; c'est une
ÉTUDE comparative, pas une preuve hors échantillon. Lecture seule : n'écrit rien. 0 ordre.
"""
from __future__ import annotations

import json
import statistics
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent          # hulk-mexc
CACHE_DIR = RACINE / "runs" / "replay_cache"
PROFILS = RACINE / "strategie" / "universe_profils.json"
BUDGET = 30.0
TRANCHE_MIN = BUDGET / 8.0
POND = (1 / 3, 1 / 3, 1 / 3)
ADD_STEP = 0.08          # pyramide spec G : +8 % au-dessus du dernier ajout
REBUY_FRAC = 0.5         # rachat de souche à 0,5×amp7 sous la sortie (convention maison)
SMA_E = 24               # sortie G : close < SMA24
SMA_GATE = 240           # filtre tendance longue

sys.path.insert(0, str(Path(__file__).resolve().parent))
import backtest_edel_amplitude as M  # noqa: E402  (mêmes sma/hh/Book que l'étude du 09/10)


def charger(pair: str):
    kl = json.load(open(CACHE_DIR / f"{pair}_1h_45j.json", encoding="utf-8"))
    return ([float(b["o"]) for b in kl], [float(b["h"]) for b in kl],
            [float(b["l"]) for b in kl], [float(b["c"]) for b in kl])


def frais_paire(pair: str) -> float:
    prof = json.load(open(PROFILS, encoding="utf-8"))
    c = (prof.get(pair) or {}).get("calib") or {}
    return float(c.get("spread_cout_bps") or 50.0) / 10000.0


def amp7_series(H, L):
    """amp7[i] = range journalier MÉDIAN des 7 jours ENTIÈREMENT précédents (walk-forward).
    Jour = bloc de 24 bougies 1 h. Aucune donnée du futur."""
    n = len(H)
    amp = [None] * n
    ranges = []
    for d0 in range(0, n, 24):
        fin = min(d0 + 24, n)
        hs, ls = H[d0:fin], L[d0:fin]
        ranges.append((max(hs) - min(ls)) / min(ls) * 100.0 if ls else None)
        idx = len(ranges) - 1
        a7 = statistics.median(ranges[idx - 7:idx]) if idx >= 7 else None
        for i in range(d0, fin):
            amp[i] = a7
    return amp


def i0_premier_signal(C, hh24, s24, s240, debut):
    for i in range(debut, len(C)):
        if s24[i] is not None and s240[i] is not None and \
                C[i] > s24[i] and C[i] > hh24[i] and C[i] > s240[i]:
            return i
    return None


def run(C, frais, avec_bag=False, ind=None):
    """Spec G (copie fidèle du chemin G de backtest_edel_amplitude.recolte) ± conversion en bag.
    ind = (s24, s240, hh24, amp) CALCULÉS SUR LA SÉRIE COMPLÈTE puis tranchés à la fenêtre :
    le warm-up SMA240 n'est jamais réinitialisé par une découpe (sinon les moitiés
    sous-comptent les trades). Pas de force-sell à la fin : valeur marquée au dernier close."""
    M.FRAIS = frais
    s24, s240, hh24, amp = ind
    b = M.Book(BUDGET)
    souche = 0.0            # jetons parqués, JAMAIS vendus
    frais_souche = 0.0
    pending = None          # niveau de rachat de souche en attente (0,5×amp7 sous la sortie)
    for i in range(len(C)):
        b.bars += 1
        if s24[i] is None or s240[i] is None:
            if b.qty > 0:
                b.expo_bars += 1
            continue
        if b.qty == 0:
            if C[i] > s24[i] and C[i] > hh24[i] and C[i] > s240[i]:
                if b.acheter(i, C[i], BUDGET * POND[0]):
                    b.tranches = 1
                    b.last_add = b.peak = C[i]
        else:
            b.peak = max(b.peak, C[i])
            if b.tranches < len(POND) and C[i] >= b.last_add * (1 + ADD_STEP):
                if b.acheter(i, C[i], BUDGET * POND[b.tranches]):
                    b.tranches += 1
                    b.last_add = C[i]
            if b.qty > 0 and C[i] < s24[i]:
                prix_sortie = C[i]
                b.vendre_tout(i, prix_sortie, "SELL_regime")
                if avec_bag and amp[i]:
                    pending = prix_sortie * (1.0 - REBUY_FRAC * amp[i] / 100.0)
        # conversion du cash en SOUCHE quand le creux touche le niveau de rachat
        if avec_bag and pending is not None and C[i] <= pending and b.cash >= TRANCHE_MIN:
            q = b.cash * (1 - frais) / C[i]
            frais_souche += b.cash * frais
            souche += q
            b.cash = 0.0
            pending = None
        if b.qty > 0 or souche > 0:   # la SOUCHE est de l'exposition aussi (honnêteté)
            b.expo_bars += 1
    tokens = b.qty + souche
    valeur = b.cash + tokens * C[-1]
    return {"net": valeur - BUDGET, "tokens": tokens, "souche": souche,
            "cash": b.cash, "frais": b.frais_payes + frais_souche,
            "expo": 100 * b.expo_bars / max(1, b.bars),
            "achats": sum(1 for t in b.trades if t[0] == "BUY"),
            "sorties": sum(1 for t in b.trades if t[0].startswith("SELL"))}


def hold(C, i0, frais):
    tokens = BUDGET * (1 - frais) / C[i0]
    return {"net": BUDGET * (1 - frais) * (C[-1] / C[i0]) - BUDGET, "tokens": tokens}


def paire_stats(pair: str):
    O, H, L, C = charger(pair)
    frais = frais_paire(pair)
    s24, s240, hh24 = M.sma(C, SMA_E), M.sma(C, SMA_GATE), M.hh(C, 24)
    amp = amp7_series(H, L)
    i0 = i0_premier_signal(C, hh24, s24, s240, SMA_GATE)
    if i0 is None:
        return None
    h = hold(C, i0, frais)
    n = len(C) - i0
    milieu = i0 + n // 2
    coupe = lambda a: a[i0:]  # noqa: E731  tranches d'indicateurs déjà calculés
    g = run(coupe(C), frais, False, (coupe(s24), coupe(s240), coupe(hh24), coupe(amp)))
    gb = run(coupe(C), frais, True, (coupe(s24), coupe(s240), coupe(hh24), coupe(amp)))
    coupe2 = lambda a: a[i0:milieu]  # noqa: E731
    coupe3 = lambda a: a[milieu:]    # noqa: E731
    ind1 = (coupe2(s24), coupe2(s240), coupe2(hh24), coupe2(amp))
    ind2 = (coupe3(s24), coupe3(s240), coupe3(hh24), coupe3(amp))
    g1 = run(coupe2(C), frais, False, ind1)
    g2 = run(coupe3(C), frais, False, ind2)
    gb1 = run(coupe2(C), frais, True, ind1)
    gb2 = run(coupe3(C), frais, True, ind2)
    return {"pair": pair, "frais_bps": frais * 10000, "hold": h, "g": g, "gb": gb,
            "moities": (g1, g2, gb1, gb2)}


def main():
    paires = sys.argv[1:] or sorted(
        p.name.split("_")[0] for p in CACHE_DIR.glob("*_1h_45j.json"))
    print("CHIFFRAGE BAG × AMPLITUDE — spec G + conversion en souche au creux (0,5×amp7)")
    print(f"budget {BUDGET:.0f} $/ligne · frais = spread_cout de la fiche · "
          f"fenêtre 45 j (bougies 1 h) · 0 ordre, 0 €, lecture seule\n")
    tot = {"hold": 0.0, "g": 0.0, "gb": 0.0}
    detail = []
    for pair in paires:
        try:
            r = paire_stats(pair)
        except FileNotFoundError:
            continue
        if r is None:
            print(f"  {pair:10} aucun signal G sur la fenêtre — ignorée")
            continue
        detail.append(r)
        tot["hold"] += r["hold"]["net"]
        tot["g"] += r["g"]["net"]
        tot["gb"] += r["gb"]["net"]
    for r in detail:
        h, g, gb = r["hold"], r["g"], r["gb"]
        bag = 100 * gb["tokens"] / h["tokens"] if h["tokens"] else float("nan")
        g1, g2, gb1, gb2 = r["moities"]
        print(f"── {r['pair']}  (frais {r['frais_bps']:.1f} bps/côté)")
        print(f"   HOLD  net {h['net']:+8.2f} $   jetons {h['tokens']:.4f}  (bag 100 %)")
        print(f"   G     net {g['net']:+8.2f} $   jetons {g['tokens']:.4f}  "
              f"({100*g['tokens']/h['tokens']:.1f} % du hold)  "
              f"achats={g['achats']} sorties={g['sorties']} frais={g['frais']:.2f} $ "
              f"expo={g['expo']:.0f}%")
        print(f"   GBAG  net {gb['net']:+8.2f} $   jetons {gb['tokens']:.4f}  "
              f"BAG {bag:.1f} % du hold  (souche {gb['souche']:.4f})  "
              f"frais={gb['frais']:.2f} $ expo={gb['expo']:.0f}%")
        print(f"   2 moitiés net : G {g1['net']:+.2f}/{g2['net']:+.2f} $ · "
              f"GBAG {gb1['net']:+.2f}/{gb2['net']:+.2f} $ · "
              f"souche h2 {gb2['souche']:.4f} jetons")
    print(f"\nSOMMES net ({len(detail)} paires) : HOLD {tot['hold']:+.2f} $ · "
          f"G {tot['g']:+.2f} $ · GBAG {tot['gb']:+.2f} $")
    print("LIMITES (R8) : 1 fenêtre 45 j · 1 h · amp7 = médiane des 7 jours précédents "
          "(blocs de 24 bougies) · rachat 0,5×amp7 CHOISI · pas de slippage d'impact · "
          "ordre intra-bougie favorable assumé · ÉTUDE, pas preuve hors échantillon.")


if __name__ == "__main__":
    main()

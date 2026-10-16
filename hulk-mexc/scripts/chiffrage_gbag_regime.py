#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""chiffrage_gbag_regime.py — P2 (GO P1-P4 Christophe, 16/10/2026).

QUESTION : GBAG=ALL prend les cassures sur TOUTES les paires, même en chop (amp7
faible) où les faux signaux scient. Variante GATED : entrée cassure SEULEMENT si
amp7 >= SEUIL (le même amp7 walk-forward que le moteur `_gbag_amp7` : médiane des
ranges journaliers des 7 jours précédents).

MÉTHODE (le brut dit la vérité) :
  1. on REPRODUIT d'abord le chiffre du 14/10 (GBAG +418,12 $) avec l'instrument
     canonique `chiffrage_bag_amplitude` (qu'on NE TOUCHE PAS — on le réutilise en
     module). Si on ne retrouve pas le brut, la comparaison ne vaut rien ;
  2. mêmes bougies / mêmes frais / même budget / mêmes coupes (i0 + 2 moitiés),
     seule l'entrée change (porte amp) ;
  3. la porte ne gagne que si elle bat GBAG sur les 2 moitiés (anti-overfit).

Lecture seule (cache local, aucun réseau), 0 ordre, 0 €.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import backtest_edel_amplitude as M
import chiffrage_bag_amplitude as G

SEUILS = (1.5, 2.0, 3.0)  # amp7 min en % : 3 candidats, le brut tranche


def run_gated(C, frais, ind, amp_min):
    """Copie fidèle de G.run (spec G + souche), + PORTE : l'entrée cassure exige
    amp7 >= amp_min. Sorties, pyramide, souche : inchangées."""
    M.FRAIS = frais
    s24, s240, hh24, amp = ind
    b = M.Book(G.BUDGET)
    souche = 0.0
    frais_souche = 0.0
    pending = None
    for i in range(len(C)):
        b.bars += 1
        if s24[i] is None or s240[i] is None:
            if b.qty > 0:
                b.expo_bars += 1
            continue
        if b.qty == 0:
            if (C[i] > s24[i] and C[i] > hh24[i] and C[i] > s240[i]
                    and amp[i] is not None and amp[i] >= amp_min):
                if b.acheter(i, C[i], G.BUDGET * G.POND[0]):
                    b.tranches = 1
                    b.last_add = b.peak = C[i]
        else:
            b.peak = max(b.peak, C[i])
            if b.tranches < len(G.POND) and C[i] >= b.last_add * (1 + G.ADD_STEP):
                if b.acheter(i, C[i], G.BUDGET * G.POND[b.tranches]):
                    b.tranches += 1
                    b.last_add = C[i]
            if b.qty > 0 and C[i] < s24[i]:
                prix_sortie = C[i]
                b.vendre_tout(i, prix_sortie, "SELL_regime")
                if amp[i]:
                    pending = prix_sortie * (1.0 - G.REBUY_FRAC * amp[i] / 100.0)
        if pending is not None and C[i] <= pending and b.cash >= G.TRANCHE_MIN:
            q = b.cash * (1 - frais) / C[i]
            frais_souche += b.cash * frais
            souche += q
            b.cash = 0.0
            pending = None
        if b.qty > 0 or souche > 0:
            b.expo_bars += 1
    tokens = b.qty + souche
    valeur = b.cash + tokens * C[-1]
    return {"net": valeur - G.BUDGET, "tokens": tokens, "souche": souche,
            "cash": b.cash, "frais": b.frais_payes + frais_souche,
            "expo": 100 * b.expo_bars / max(1, b.bars),
            "achats": sum(1 for t in b.trades if t[0] == "BUY"),
            "sorties": sum(1 for t in b.trades if t[0].startswith("SELL"))}


def run_pond1(C, frais, ind):
    """Variante diagnostic : GBAG avec UNE SEULE tranche (pas de pyramide) + souche.
    Sert à trancher d'où vient l'edge (pyramide vs souche). Mêmes conventions."""
    M.FRAIS = frais
    s24, s240, hh24, amp = ind
    b = M.Book(G.BUDGET)
    souche = 0.0
    frais_souche = 0.0
    pending = None
    for i in range(len(C)):
        b.bars += 1
        if s24[i] is None or s240[i] is None:
            if b.qty > 0:
                b.expo_bars += 1
            continue
        if b.qty == 0:
            if C[i] > s24[i] and C[i] > hh24[i] and C[i] > s240[i]:
                if b.acheter(i, C[i], G.BUDGET):
                    b.tranches = 99  # une seule tranche, jamais de pyramide
                    b.last_add = b.peak = C[i]
        else:
            b.peak = max(b.peak, C[i])
            if b.qty > 0 and C[i] < s24[i]:
                prix_sortie = C[i]
                b.vendre_tout(i, prix_sortie, "SELL_regime")
                if amp[i]:
                    pending = prix_sortie * (1.0 - G.REBUY_FRAC * amp[i] / 100.0)
        if pending is not None and C[i] <= pending and b.cash >= G.TRANCHE_MIN:
            q = b.cash * (1 - frais) / C[i]
            frais_souche += b.cash * frais
            souche += q
            b.cash = 0.0
            pending = None
        if b.qty > 0 or souche > 0:
            b.expo_bars += 1
    tokens = b.qty + souche
    return {"net": b.cash + tokens * C[-1] - G.BUDGET, "tokens": tokens}


def paire_gated(pair):
    O, H, L, C = G.charger(pair)
    frais = G.frais_paire(pair)
    s24, s240, hh24 = M.sma(C, G.SMA_E), M.sma(C, G.SMA_GATE), M.hh(C, 24)
    amp = G.amp7_series(H, L)
    i0 = G.i0_premier_signal(C, hh24, s24, s240, G.SMA_GATE)
    if i0 is None:
        return None
    n = len(C) - i0
    milieu = i0 + n // 2
    out = {}
    for s in SEUILS:
        coupe = lambda a: a[i0:]  # noqa: E731
        ind = (coupe(s24), coupe(s240), coupe(hh24), coupe(amp))
        g = run_gated(coupe(C), frais, ind, s)
        coupe2 = lambda a: a[i0:milieu]  # noqa: E731
        coupe3 = lambda a: a[milieu:]  # noqa: E731
        g1 = run_gated(coupe2(C), frais,
                       (coupe2(s24), coupe2(s240), coupe2(hh24), coupe2(amp)), s)
        g2 = run_gated(coupe3(C), frais,
                       (coupe3(s24), coupe3(s240), coupe3(hh24), coupe3(amp)), s)
        out[s] = {"net": g["net"], "h1": g1["net"], "h2": g2["net"],
                  "achats": g["achats"], "sorties": g["sorties"],
                  "expo": g["expo"], "frais": g["frais"]}
    return out


def main():
    paires = sys.argv[1:] or sorted(
        p.name.split("_")[0] for p in G.CACHE_DIR.glob("*_1h_45j.json"))
    print("CHIFFRAGE PORTE AMPLITUDE GBAG — mêmes bougies/frais/budget que le 14/10")
    tot_hold = tot_g = tot_gb = 0.0
    tot_gate = {s: 0.0 for s in SEUILS}
    tot_h = {s: [0.0, 0.0] for s in SEUILS}
    tot_gb_h = [0.0, 0.0]
    tot_pond1 = 0.0
    lignes = []  # (pair, hold, g, gb, gb_h1, gb_h2, hold_h1, hold_h2, pond1)
    n = 0
    for pair in paires:
        try:
            r = G.paire_stats(pair)
        except FileNotFoundError:
            continue
        if r is None:
            continue
        g1, g2, gb1, gb2 = r["moities"]
        tot_hold += r["hold"]["net"]
        tot_g += r["g"]["net"]
        tot_gb += r["gb"]["net"]
        tot_gb_h[0] += gb1["net"]
        tot_gb_h[1] += gb2["net"]
        gg = paire_gated(pair)
        for s in SEUILS:
            tot_gate[s] += gg[s]["net"]
            tot_h[s][0] += gg[s]["h1"]
            tot_h[s][1] += gg[s]["h2"]
        # diagnostic pyramide-vs-souche + hold par moitié (walk-forward)
        O, H, L, C = G.charger(pair)
        frais = G.frais_paire(pair)
        s24, s240, hh24 = M.sma(C, G.SMA_E), M.sma(C, G.SMA_GATE), M.hh(C, 24)
        amp = G.amp7_series(H, L)
        i0 = G.i0_premier_signal(C, hh24, s24, s240, G.SMA_GATE)
        nn = len(C) - i0
        mil = i0 + nn // 2
        p1 = run_pond1(C[i0:], frais,
                       (s24[i0:], s240[i0:], hh24[i0:], amp[i0:]))["net"]
        tot_pond1 += p1
        h_h1 = G.hold(C[i0:mil], 0, frais)["net"]
        h_h2 = G.hold(C[mil:], 0, frais)["net"]
        lignes.append((pair, r["hold"]["net"], r["g"]["net"], r["gb"]["net"],
                       gb1["net"], gb2["net"], h_h1, h_h2, p1))
        n += 1
    print(f"REPRODUCTION ({n} paires) : HOLD {tot_hold:+.2f} $ · "
          f"G {tot_g:+.2f} $ · GBAG {tot_gb:+.2f} $ "
          f"(référence 14/10 : +383,36 / +378,44 / +418,12)")
    for s in SEUILS:
        h1, h2 = tot_h[s]
        print(f"GATED amp>={s:.1f}% : net {tot_gate[s]:+.2f} $ "
              f"(moitiés {h1:+.2f}/{h2:+.2f} vs GBAG {tot_gb_h[0]:+.2f}/{tot_gb_h[1]:+.2f})")
    print(f"GBAG 1 TRANCHE (souche, sans pyramide) : net {tot_pond1:+.2f} $ "
          f"(références 14/10 : 'plat +378,44' / '1 tranche +396,25' — voir verdict)")
    print("\n── PAR PAIRE : GBAG vs HOLD, moitiés h1/h2 (walk-forward)")
    for (p, h, g, gb, gh1, gh2, hh1, hh2, p1) in sorted(lignes, key=lambda x: x[3]):
        print(f"  {p:12} GBAG {gb:+7.2f} (h1 {gh1:+7.2f}/h2 {gh2:+7.2f}) · "
              f"HOLD {h:+7.2f} (h1 {hh1:+7.2f}/h2 {hh2:+7.2f}) · 1tr {p1:+7.2f}")
    # SÉLECTION WALK-FORWARD : paires où GBAG bat HOLD en 1ʳᵉ moitié → vérif en 2ᵉ.
    sel = [x for x in lignes if x[4] > x[6]]
    v_gb = sum(x[5] for x in sel)
    v_h = sum(x[7] for x in sel)
    nsel = sum(1 for x in lignes if x[3] > x[1])
    print(f"\nWALK-FORWARD : {len(sel)}/{len(lignes)} paires GBAG>HOLD en h1 → "
          f"en h2 : GBAG {v_gb:+.2f} $ vs HOLD {v_h:+.2f} $ "
          f"(in-sample total : {nsel} paires GBAG>HOLD)")
    print("LIMITES (R8) : même fenêtre 45 j 1 h que le 14/10 · porte sur amp7 walk-forward "
          "(même définition que le moteur) · ÉTUDE, pas preuve hors échantillon.")


if __name__ == "__main__":
    main()

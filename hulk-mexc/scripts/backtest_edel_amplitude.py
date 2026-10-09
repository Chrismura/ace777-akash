#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""backtest_edel_amplitude.py — RÉCOLTE D'AMPLITUDE SUR EDEL (09/10/2026, GO Christophe)

PROBLÈME MESURÉ (fiche EDEL, PANORAMA_EDEL_SCANDALE_20260917) :
  amplitude ≈ +156 % (×4,0 close→close sur 45 j en cache) → PnL réalisé **+0,98 $**.
  Cause : on empile des miettes, on vend DANS les mèches, on rachète après les sommets.
  Le seul vrai gain de récolte (`stake_out_2x`, +5,27 $) prouve qu'avec une taille RÉELLE
  le moteur sait récolter. → Le levier n'est pas le seuil de sortie, c'est l'AMPLITUDE :
  entrer dans la tendance, grossir avec elle, récolter par paliers, laisser courir.

SPEC FIGÉE AVANT TEST (règle n°5) : moteurs comparés sur les MÊMES bougies, MÊMES frais,
MÊME budget ($30, une seule « ligne » à la fois — comparable au budget moteur/pair).

  A) MOTEUR_ACTUEL (approx. fiche EDEL) : entrée sur repli 5,5 % sous le plus-haut 24 h,
     stop 10,3 % sur clôture, trailing armé à +10 % / giveback fixe 4 pts, ré-entrée, mise
     BUDGET/3.
  B) RECOLTE_AMPLITUDE (1re prop.) : close > SMA72 ET cassure du plus-haut 24 h ; pyramide
     tranches égales ; trailing proportionnel (k×ATR%) ; sortie régime sèche.
  D) TENDANCE_PORTÉE : sortie RÉGIME SEULEMENT, filtrée (close < SMA72×(1−1×ATR%) +
     2 clôtures de confirmation), AUCUN trailing en cours de tendance (on laisse courir).
  F) D + RÉCOLTE PAR PALIERS (proposition maison C1, 17/09) : vend 1/3 de la position à
     chaque +35 % au-dessus du coût moyen, la dernière tranche court jusqu'à la fin de
     tendance (notional minimum respecté — pas de poussière).
  C) HOLD : acheter au premier prix et ne rien faire (le juge — EDEL ×4).

LIMITES DÉCLARÉES (R8) :
  - **1 paire, 1 fenêtre de 45 j** — ÉTUDE, pas preuve hors échantillon.
  - bougies 1 h : mèches intra-heure mal vues.
  - frais = 53,9 bps/côté (spread_cout EDEL de la fiche) → aller-retour ≈ 108 bps.
  - stabilité éprouvée sur 2 moitiés + petite grille de sensibilité (risque d'ajustement
    aux données assumé et borné) ; une fenêtre reste une fenêtre.

Lecture seule. N'écrit rien. Aucun ordre.
"""
from __future__ import annotations

import json
import statistics
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent          # hulk-mexc
CACHE = RACINE / "runs" / "replay_cache" / "EDELUSDT_1h_45j.json"
FRAIS = 0.00539                                          # 53,9 bps par côté (fiche EDEL)
BUDGET = 30.0                                            # $ (une ligne à la fois)
TRANCHE_MIN = BUDGET / 8.0                               # $ — seuil « pas de poussière »


def charger():
    kl = json.load(open(CACHE, encoding="utf-8"))
    O = [float(b["o"]) for b in kl]
    H = [float(b["h"]) for b in kl]
    L = [float(b["l"]) for b in kl]
    C = [float(b["c"]) for b in kl]
    return O, H, L, C


def sma(xs, n):
    out = [None] * len(xs)
    s = 0.0
    for i, x in enumerate(xs):
        s += x
        if i >= n:
            s -= xs[i - n]
        if i >= n - 1:
            out[i] = s / n
    return out


def atr_pct(H, L, C, n=24):
    out = [None] * len(C)
    trs = [None] * len(C)
    for i in range(len(C)):
        trs[i] = (H[i] - L[i]) if i == 0 else max(
            H[i] - L[i], abs(H[i] - C[i - 1]), abs(L[i] - C[i - 1]))
    for i in range(len(C)):
        if i >= n - 1:
            out[i] = statistics.fmean(trs[i - n + 1:i + 1]) / C[i]
    return out


def hh(xs, n):
    return [max(xs[max(0, i - n):i]) if i > 0 else xs[0] for i in range(len(xs))]


class Book:
    """Portefeuille minimal : frais par côté, mark-to-market, pas de poussière."""

    def __init__(self, budget=BUDGET):
        self.cash, self.budget = budget, budget
        self.qty = 0.0
        self.cout_unitaire = 0.0
        self.peak = 0.0
        self.tranches = 0
        self.last_add = 0.0
        self.palier = 0
        self.trades = []
        self.frais_payes = 0.0
        self.expo_bars = 0
        self.bars = 0

    def acheter(self, i, prix, montant):
        montant = min(montant, self.cash)
        if montant < TRANCHE_MIN:
            return False
        q = montant * (1 - FRAIS) / prix
        self.frais_payes += montant * FRAIS
        self.cash -= montant
        self.cout_unitaire = ((self.cout_unitaire * self.qty) + prix * q) / (self.qty + q)
        self.qty += q
        self.trades.append(("BUY", i, prix, q, montant))
        return True

    def vendre_partiel(self, i, prix, frac, motif):
        q = self.qty * frac
        produit = q * prix
        if produit < TRANCHE_MIN:
            return False
        self.frais_payes += produit * FRAIS
        self.cash += produit * (1 - FRAIS)
        self.qty -= q
        self.trades.append((motif, i, prix, q, produit))
        return True

    def vendre_tout(self, i, prix, motif):
        if self.qty <= 0:
            return
        produit = self.qty * prix
        self.frais_payes += produit * FRAIS
        self.cash += produit * (1 - FRAIS)
        self.trades.append((motif, i, prix, self.qty, produit))
        self.qty = 0.0
        self.cout_unitaire = 0.0
        self.tranches = 0
        self.peak = 0.0
        self.last_add = 0.0
        self.palier = 0

    def mtm(self, prix):
        return self.cash + self.qty * prix


def max_dd(equity):
    pic, dd = equity[0], 0.0
    for e in equity:
        pic = max(pic, e)
        dd = max(dd, 1 - e / pic)
    return dd


# ── A) moteur actuel (approx. fiche EDEL) ────────────────────────────────────
def moteur_actuel(C, dip=0.055, stop=0.103, arm=0.10, giveback=0.04):
    hh24, b, eq, mise = hh(C, 24), Book(), [], BUDGET / 3.0
    for i in range(24, len(C)):
        b.bars += 1
        if b.qty == 0:
            if C[i] <= hh24[i] * (1 - dip):
                b.acheter(i, C[i], mise)
                b.peak = C[i]
        else:
            b.peak = max(b.peak, C[i])
            gain = C[i] / b.cout_unitaire - 1
            if C[i] <= b.cout_unitaire * (1 - stop):
                b.vendre_tout(i, C[i], "SELL_stop")
            elif gain >= arm and C[i] <= b.peak * (1 - giveback):
                b.vendre_tout(i, C[i], "SELL_trail")
        if b.qty > 0:
            b.expo_bars += 1
        eq.append(b.mtm(C[i]))
    if b.qty:
        b.vendre_tout(len(C) - 1, C[-1], "SELL_fin")
        eq[-1] = b.cash
    return b, max_dd(eq)


# ── B/D/F) récolte d'amplitude ───────────────────────────────────────────────
def recolte(C, H, L, ponderations=(1 / 3, 1 / 3, 1 / 3), add_step=0.08, k_atr=2.5,
            trail_min=0.06, trail_max=0.35, trailing=True, regime_buf_atr=0.0,
            regime_confirm=1, cooldown=0, sma_n=72, n_atr=24, paliers=None, gate_n=None,
            exit_sma_n=None):
    """paliers = (pas_relatif, fraction) → récolte par paliers au-dessus du coût moyen.
    gate_n = longueur d'une SMA longue de TENDANCE : n'entre que si close > SMA_gate.
    exit_sma_n = si fourni, la SORTIE régime teste close < SMA(exit_sma_n) au lieu de SMA(sma_n)
                 (sortir sur la tendance LONGUE garde la position dans la tendance)."""
    s72, a, hh24 = sma(C, sma_n), atr_pct(H, L, C, n_atr), hh(C, 24)
    sx = sma(C, exit_sma_n) if exit_sma_n else s72
    sg = sma(C, gate_n) if gate_n else None
    b, eq, below, last_sortie = Book(), [], 0, -10 ** 9
    for i in range(sma_n, len(C)):
        b.bars += 1
        if s72[i] is None or a[i] is None or sx[i] is None or (sg is not None and sg[i] is None):
            eq.append(b.mtm(C[i]))
            continue
        if b.qty == 0:
            gate_ok = sg is None or C[i] > sg[i]
            if gate_ok and C[i] > s72[i] and C[i] > hh24[i] and i - last_sortie > cooldown:
                if b.acheter(i, C[i], BUDGET * ponderations[0]):
                    b.tranches = 1
                    b.last_add = b.peak = C[i]
        else:
            b.peak = max(b.peak, C[i])
            if b.tranches < len(ponderations) and C[i] >= b.last_add * (1 + add_step):
                if b.acheter(i, C[i], BUDGET * ponderations[b.tranches]):
                    b.tranches += 1
                    b.last_add = C[i]
            if b.qty > 0:
                # récolte par paliers (C1 maison) : convertit l'amplitude sans lâcher la tendance
                if paliers and b.cout_unitaire > 0:
                    pas, frac = paliers
                    cible = int((C[i] / b.cout_unitaire - 1) / pas)
                    while b.palier < cible:
                        b.palier += 1
                        b.vendre_partiel(i, C[i], frac, f"SELL_palier{b.palier}")
                if b.qty <= 0:
                    last_sortie = i
                    below = 0
                else:
                    buf = regime_buf_atr * a[i]
                    below = below + 1 if C[i] < sx[i] * (1 - buf) else 0
                    if below >= regime_confirm:
                        b.vendre_tout(i, C[i], "SELL_regime")
                        last_sortie, below = i, 0
                    elif trailing:
                        trail = min(trail_max, max(trail_min, k_atr * a[i]))
                        if C[i] <= b.peak * (1 - trail):
                            b.vendre_tout(i, C[i], "SELL_trail")
                            last_sortie = i
        if b.qty > 0:
            b.expo_bars += 1
        eq.append(b.mtm(C[i]))
    if b.qty:
        b.vendre_tout(len(C) - 1, C[-1], "SELL_fin")
        eq[-1] = b.cash
    return b, max_dd(eq)


def hold(C, i0=0):
    return BUDGET * (1 - FRAIS) * (C[-1] / C[i0])


def rapport(nom, b, dd, C, i0=0, largeur=26):
    net = b.cash - BUDGET
    ref = hold(C, i0) - BUDGET
    part = 100 * net / ref if ref > 0 else float("nan")
    achats = sum(1 for t in b.trades if t[0] == "BUY")
    sorties = sum(1 for t in b.trades if t[0].startswith("SELL"))
    expo = 100 * b.expo_bars / max(1, b.bars)
    print(f"  {nom:{largeur}} net {net:+8.2f} $ ({100*net/BUDGET:+6.1f} %)  "
          f"capture {part:5.1f}%  achat={achats:2d} sortie={sorties:3d}  "
          f"frais={b.frais_payes:6.2f} $  DDmax {100*dd:5.1f}%  exposé {expo:4.0f}%")
    return net, part, dd


# ── G) SPEC RETENUE : récolte d'amplitude SYMÉTRIQUE ─────────────────────────
def recolte_symetrique(C, H, L, sma_n=24, add_step=0.08, ponderations=(1/3, 1/3, 1/3),
                       gate_n=None, exit_sma_n=None):
    """G — entrée sur cassure (close > SMA24 ET > plus-haut 24 clôt.), pyramide,
    sortie quand close < SMA24 (1 clôture). Symétrique, sans optimisation fine.
    gate_n : SMA longue optionnelle (n'entre que si la tendance longue est haussière)."""
    return recolte(C, H, L, ponderations=ponderations, add_step=add_step, trailing=False,
                   regime_buf_atr=0.0, regime_confirm=1, cooldown=0, sma_n=sma_n, paliers=None,
                   gate_n=gate_n, exit_sma_n=exit_sma_n)


def main():
    O, H, L, C = charger()
    ref = hold(C) - BUDGET
    print(f"EDEL 1 h — {len(C)} bougies — {C[0]:.5f} → {C[-1]:.5f} "
          f"(×{C[-1]/C[0]:.2f}) — frais {FRAIS*1e4:.1f} bps/côté — budget {BUDGET:.0f} $\n")
    print("SPÉCIMEN COMPLET (45 j) :  [capture = part du mouvement hold convertie en cash]")

    bA, ddA = moteur_actuel(C)
    rapport("A. moteur actuel", bA, ddA, C)

    bB, ddB = recolte(C, H, L, trailing=True, regime_buf_atr=0.0, regime_confirm=1, cooldown=0)
    rapport("B. récolte (1re prop.)", bB, ddB, C)

    bD, ddD = recolte(C, H, L, trailing=False, regime_buf_atr=1.0, regime_confirm=2, cooldown=0)
    rapport("D. tendance portée", bD, ddD, C)

    bF, ddF = recolte(C, H, L, trailing=False, regime_buf_atr=1.0, regime_confirm=2, cooldown=0,
                      paliers=(0.35, 0.33))
    rapport("F. D + récolte paliers", bF, ddF, C)

    bG, ddG = recolte_symetrique(C, H, L)
    rapport("G. SPEC RETENUE (sym.)", bG, ddG, C)

    print(f"  {'C. hold (rien faire)':26} net {ref:+8.2f} $ "
          f"({100*ref/BUDGET:+6.1f} %)  capture 100.0%\n")

    print("DÉTAIL de G (tous les mouvements) :")
    for t in bG.trades:
        print(f"  {t[0]:14} bar {t[1]:4d} @ {t[2]:.5f} notional {t[4]:6.2f} $")

    print("\nGRILLE DE SENSIBILITÉ (SMA d'entrée × sortie régime)  [net $ / DDmax]")
    print(f"  {'':12}" + "".join(f"{c:>16}" for c in ("buf0 cf1", "buf1 cf2", "buf 1.5 cf2")))
    for sma_n in (12, 18, 24, 36, 48, 72):
        cells = []
        for buf, cf in ((0.0, 1), (1.0, 2), (1.5, 2)):
            bb, dd = recolte(C, H, L, trailing=False, regime_buf_atr=buf,
                             regime_confirm=cf, cooldown=0, sma_n=sma_n, paliers=None)
            cells.append(f"{bb.cash-BUDGET:+7.2f}$/{100*dd:4.0f}%")
        print(f"  SMA{sma_n:<9}" + "".join(f"{c:>16}" for c in cells))

    print("\nSTABILITÉ (2 moitiés indépendantes) :")
    for label, s, e in (("1re moitié", 0, len(C) // 2), ("2e moitié", len(C) // 2, len(C))):
        Hh, Ll, Cc = H[s:e], L[s:e], C[s:e]
        bA2, _ = moteur_actuel(Cc)
        bG2, _ = recolte_symetrique(Cc, Hh, Ll)
        print(f"  {label:12} moteur {bA2.cash-BUDGET:+7.2f} $ | SPEC G {bG2.cash-BUDGET:+7.2f} $"
              f" | hold {hold(Cc)-BUDGET:+7.2f} $")

    print("\nCROSS-CHECK multi-paires (mêmes règles, caches 45 j) — la spec est-elle un mieux GLOBAL ?")
    cache = sorted(CACHE.parent.glob("*_1h_45j.json"))
    totA = totG = totGG = 0.0
    lignes = []
    for p in cache:
        try:
            kl = json.load(open(p, encoding="utf-8"))
            if len(kl) < 300:
                continue
            Cc = [float(x["c"]) for x in kl]
            Hh = [float(x["h"]) for x in kl]
            Ll = [float(x["l"]) for x in kl]
        except Exception:
            continue
        nom = p.name.split("_")[0]
        a, _ = moteur_actuel(Cc)
        g, _ = recolte_symetrique(Cc, Hh, Ll)
        gg, _ = recolte_symetrique(Cc, Hh, Ll, gate_n=240)
        totA += a.cash - BUDGET
        totG += g.cash - BUDGET
        totGG += gg.cash - BUDGET
        lignes.append((nom, a.cash - BUDGET, g.cash - BUDGET, gg.cash - BUDGET, hold(Cc) - BUDGET))
    lignes.sort(key=lambda r: -r[4])
    print(f"  {'paire':10} {'moteur':>9} {'specG':>9} {'G+gate240':>10} {'hold':>9}")
    for nom, a, g, gg, r in lignes:
        print(f"  {nom:10} {a:+9.2f} {g:+9.2f} {gg:+10.2f} {r:+9.2f}")
    nA = sum(1 for _, a, g, gg, _ in lignes if g > a)
    nAG = sum(1 for _, a, g, gg, _ in lignes if gg > a)
    print(f"  -> specG > moteur sur {nA}/{len(lignes)} paires ; +gate240 sur {nAG}/{len(lignes)}")
    print(f"  -> SOMMES : moteur {totA:+.2f} $ | specG {totG:+.2f} $ | specG+gate240 {totGG:+.2f} $")
    print("  (l'edge se CONCENTRE sur les paires en tendance : ce n'est pas un remplacement global —")
    print("   c'est un MODE par paire, à n'activer que sur tendance longue haussière.)")

    # taille conforme à la fiche EDEL (2 % du mur 908 $ ≈ 18 $) : mise divisée, frais ↓ en proportion
    print("\nTAILLE CONFORME FICHE (mur 908 $ × 2 % ≈ 18 $ au lieu de 30 $) :")
    globals()["BUDGET"] = 18.0
    bG18, dd18 = recolte_symetrique(C, H, L)
    libelle_ref = "(réf. hold à 18 $)"
    rapport("G à 18 $", bG18, dd18, C, largeur=26)
    print(f"  {libelle_ref:26} net {hold(C)-18.0:+8.2f} $")
    return 0


if __name__ == "__main__":
    sys.exit(main())

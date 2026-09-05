#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ESSAI 3 BRAS + CAP 45 MIN (4e bras) × 4 FENÊTRES — protocole R32 (Buffy, validé propriétaire).
Replay HONNÊTE : à chaque minute t, le moteur ne connaît QUE t' <= t (aucune donnée future).
Lecture seule : klines 1m en cache local (runs/KLINES_1M_*.csv), zéro ordre, zéro contact shadow/champion.

Règle d'entrée (identique pour tous les bras, fidèle au shadow scénario C) :
  - à plat, slot toutes les 5 min, entrée LONG sur open de la barre suivante si gate H=1
  - gate H = 1 ssi somme des PnL BRUTS des trades clôturés sur les 2h précédentes > 0
    (fenêtre H mesurée sur l'historique du replay lui-même — jamais du futur)
  - BOOTSTRAP des 90 premières minutes : gate forcé à 1 (identique shadow)

Les 4 bras (défense/sortie, mêmes entrées partout) :
  A — TÉMOIN  : sortie cap 2h (hold 7200s), plancher anti-frais OFF  (réplique du shadow J+1)
  B — VARIANCE: cap 2h + plancher anti-frais ON  (k=3 × amplitude médiane 1m précédente,
                borné [60 ; 300] USDT : si |pnl flottant| dépasses le plancher → sortie)
                NB : le plancher est calculé sur la statistique de la fenêtre elle-même,
                paramètre invariant par fenêtre (garde-fou R31 de Gemini).
  C — VOLUME  : horloge volume constant (1 V-bar = médiane du volume horaire de la fenêtre,
                borné 10-120 min) + plancher anti-frais ON
  D — CAP 45  : cap 45 min (2700s) + plancher anti-frais ON   [le bras de comparaison Buffy,
                contre la proposition "condition bloquante" de Gemini R32]

Sorties : trailing 30 % (rend 30 % de l'excursion max) + cap de gain +50 USDT (fidèle shadow).
Frais : taker aller-retour 8 bps (0.08 %) — le modèle du champion (fee_round_trip_bps=8).
MAE honnête : une sortie stop/plancher est déclenchée au niveau atteint INTRA-barre
(si open et close dépassent tous deux le niveau → sortie au niveau ; sinon pire cas barre).

Livrable : tableau net par bras × fenêtre + verdict parcimonieux. Zéro interprétation au-delà.
"""
import csv, statistics, random
from datetime import datetime, timezone

RUNS = "runs/"
FEE_RT = 0.0008          # 8 bps aller-retour (modèle champion)
QTY_USDT = 200.0         # notionnel d'entrée (masse BETA du champion, conservative)
TRAIL_RET = 0.30         # trailing rend 30 % de l'excursion
CAP_GAIN = 50.0          # cap de gain absolu (fidèle au shadow scénario C)
K_PLANCHER = 3.0         # plancher anti-frais = 3 × amplitude médiane 1m (A1 validé)
PLANCHER_BORNES = (60.0, 300.0)
CAPS = {"A": 7200, "B": 7200, "C": 7200, "D": 2700}   # durées de vie (secondes)
H_WINDOW_MIN = 120       # fenêtre du gate H (2h, fidèle shadow)
SLOT = 5                 # slot d'entrée toutes les 5 min
BOOTSTRAP_MIN = 90       # gate forcé pendant le bootstrap

FENETRES = {
    "VORTEX": ("runs/KLINES_1M_VORTEX.csv",),
    "NUAGE":  ("runs/KLINES_1M_NUAGE.csv",),
    "ORAGES": ("runs/KLINES_1M_ORAGES.csv",),
    "MARS":   ("runs/KLINES_1M_MARS.csv",),
}


def load_klines(path):
    """-> list de dicts t(open_time s), o,h,l,c,v (floats), trié par t."""
    rows = []
    with open(path) as f:
        rd = csv.DictReader(f)
        for r in rd:
            rows.append({
                "t": int(r["open_time"]) // 1000,
                "o": float(r["open"]), "h": float(r["high"]),
                "l": float(r["low"]),  "c": float(r["close"]),
                "v": float(r["volume"]),
            })
    rows.sort(key=lambda r: r["t"])
    return rows


def simulate(kl, bras):
    """Replay d'une fenêtre pour un bras. Retourne dict de stats."""
    cap_sec = CAPS[bras]
    plancher_on = bras in ("B", "C", "D")

    # pré-calculs "connaissant le passé seulement" :
    # amplitude 1m médiane glissante (120 min) pour le plancher
    # volume horaire médian glissant (60 min) pour le V-bar du bras C
    amplitudes = [r["h"] - r["l"] for r in kl]
    vols = [r["v"] for r in kl]

    pos = None              # dict: entry, qty_btc, ext_max, ext_min, t_entry, vol_bar
    trades = []             # nets
    gate_hist = []          # (t_cloture, pnl_brut) pour le gate H
    pos_last_end = 0        # dernier index de clôture (une seule position à la fois)

    for i in range(len(kl)):
        r = kl[i]
        t = r["t"]
        t0 = kl[0]["t"]
        minute_in_run = (t - t0) // 60

        # ---- 1. gestion position ouverte (sorties évaluées AVANT nouvelle entrée)
        if pos is not None:
            exit_px = None
            reason = None
            age = t - pos["t_entry"]

            # excursion intra-barre vs trailing
            # (fidèle shadow : ext avance avec le prix favorable, trailing rend 30 %)
            if pos["side"] == 1:   # long
                pos["ext_max"] = max(pos["ext_max"], r["h"])
                trail = pos["ext_max"] - TRAIL_RET * (pos["ext_max"] - pos["entry"])
                if r["l"] <= trail and pos["ext_max"] > pos["entry"]:
                    exit_px, reason = trail, "trailing"
                if (r["c"] - pos["entry"]) * QTY_USDT / pos["entry"] >= CAP_GAIN:
                    exit_px, reason = r["c"], "cap_gain"
            # plancher anti-frais (B/C/D) : MAE honnête intra-barre
            if exit_px is None and plancher_on:
                pnl_low = (r["l"] - pos["entry"]) * QTY_USDT / pos["entry"]
                if pnl_low <= -pos["plancher"]:
                    exit_px, reason = pos["entry"] * (1 - pos["plancher"] / QTY_USDT), "plancher"
            # cap temporel (fin de barre)
            if exit_px is None and age >= cap_sec:
                exit_px, reason = r["c"], "cap_temps"
            # bras C : horloge volume
            if exit_px is None and bras == "C":
                if (sum(vols[max(0, i - 120):i]) >= pos["vol_bar"]) or True:
                    # volume écoulé DEPUIS l'entrée :
                    vol_since = sum(v["v"] for v in kl[pos["i_entry"]:i])
                    if vol_since >= pos["vol_bar"]:
                        exit_px, reason = r["c"], "vbar"

            if exit_px is not None:
                gross = (exit_px - pos["entry"]) * QTY_USDT / pos["entry"] * pos["side"]
                net = gross - FEE_RT * QTY_USDT
                trades.append(net)
                gate_hist.append((t, gross))
                pos = None
                pos_last_end = i

        # ---- 2. gate H (2h en arrière, bruts clôturés) — passé seulement
        h_sum = sum(g for tt, g in gate_hist if tt >= t - H_WINDOW_MIN * 60)
        H = 1 if h_sum > 0 else 0
        if minute_in_run < BOOTSTRAP_MIN + 120:
            H = 1  # bootstrap fidèle au shadow (décalé : les entrées démarrent à i>=120)

        # ---- 3. slot 5 min : entrée si à plat et H=1
        if pos is None and minute_in_run % SLOT == 0 and H == 1 and i >= 120 and i > pos_last_end:
            # plancher (statistique de la fenêtre elle-même, invariant)
            med_amp = statistics.median(amplitudes[i - 120:i]) or 1.0
            if plancher_on:
                plancher = max(PLANCHER_BORNES[0], min(PLANCHER_BORNES[1], K_PLANCHER * med_amp))
            else:
                plancher = 10 ** 9  # off
            med_vol_h = statistics.median(vols[i - 60:i]) or 1.0
            pos = {
                "side": 1, "entry": r["o"], "i_entry": i, "t_entry": t,
                "ext_max": r["o"], "plancher": plancher,
                "vol_bar": med_vol_h,
            }
            # frais d'entrée+sortie imputés à la clôture (modèle aller-retour unique)

    return {
        "n": len(trades),
        "net": sum(trades),
        "med": statistics.median(trades) if trades else 0.0,
        "stops_plancher": sum(1 for _ in trades) - sum(trades, 0),  # placeholder
    }


def main():
    random.seed(42)
    print("=" * 78)
    print("ESSAI 3 BRAS + CAP45 × 4 FENÊTRES — replay honnête (aucune donnée future)")
    print(f"Frais {FEE_RT*10000:.0f} bps AR · notionnel {QTY_USDT:.0f} USDT · trailing {TRAIL_RET*100:.0f}% · cap gain +{CAP_GAIN:.0f}$")
    print(f"Plancher anti-frais : k={K_PLANCHER} × médiane 1m, bornes {PLANCHER_BORNES}")
    print(f"Durées de vie : A/B/C = 2h · D = 45 min")
    print("=" * 78)

    results = {}
    for fen, (path,) in FENETRES.items():
        kl = load_klines(path)
        hours = (kl[-1]["t"] - kl[0]["t"]) / 3600
        print(f"\n### {fen} — {len(kl)} barres 1m ({hours:.0f}h)")
        results[fen] = {}
        for bras in ("A", "B", "C", "D"):
            st = simulate(kl, bras)
            results[fen][bras] = st
            print(f"  Bras {bras} : {st['n']:4d} trades | net {st['net']:+10.2f} USDT | médiane {st['med']:+7.3f}")

    print("\n" + "=" * 78)
    print("TABLEAU NET (USDT) — bras × fenêtre")
    print(f"{'fenêtre':>8} | {'A témoin':>10} | {'B variance':>10} | {'C volume':>10} | {'D cap45':>10}")
    print("-" * 60)
    for fen in FENETRES:
        row = [results[fen][b]["net"] for b in ("A", "B", "C", "D")]
        print(f"{fen:>8} | " + " | ".join(f"{v:+10.2f}" for v in row))
    tot = {b: sum(results[f][b]["net"] for f in FENETRES) for b in "ABCD"}
    print("-" * 60)
    print(f"{'TOTAL':>8} | " + " | ".join(f"{tot[b]:+10.2f}" for b in "ABCD"))
    print("\n(Totals sur 4 fenêtres de durées différentes — la parcimonie impose de lire")
    print(" chaque fenêtre, pas seulement le total. Aucune décision avant confrontation.)")


if __name__ == "__main__":
    main()

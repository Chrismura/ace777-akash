#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mesure_plafond_souche.py — BAC À SABLE (lecture seule, 0 ordre, exit 0).

QUESTION (ordre Christophe 03/11, suggestion 3) : EDEL a été achetée à 0,033043 pour un
plus-haut de 0,03314, RIZE à 0,004338 pour 0,00434 — la souche a été **pyramidée en
force sans plafond**, et ces deux entrées collées au sommet sont les plus grosses pertes.
Existe-t-il une distance au sommet, MESURÉE, au-delà de laquelle ajouter de la souche
coûte au lieu de rapporter ?

MÉTHODE (aucune constante métier, aucun seuil imposé)
-----------------------------------------------------
1. On lit TOUS les ajouts de souche réels du journal (`GBAG_SOUCHE`) : date, paire, prix.
2. Pour chacun, on mesure dans les klines 1 h : la position du prix dans son propre pic
   15 j au moment de l'ajout (`dist_sommet = 1 − prix / pic15`) et ce que donne l'ajout
   ensuite (`+24 h`, `+7 j`, et jusqu'à la fin des klines disponibles).
3. On découpe les observations en déciles de `dist_sommet` et on lit le rendement médian
   de chaque décile. Le plafond candidat est la distance à partir de laquelle le rendement
   médian devient NÉGATIF — c'est un chiffre, pas une opinion.
4. On vérifie la stabilité sur deux moitiés (avant/après le 15/10).

LIMITE DÉCLARÉE (R8) : mesure sur les klines 1 h disponibles (30 j après rafraîchissement).
Un rendement futur absent (pas encore de recul) est compté comme « non mesuré », jamais 0.
"""
from __future__ import annotations

import csv
import glob
import json
import os
import statistics
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNS = ROOT / "runs"
KL = RUNS / "KLINES_1H"
FENETRE_PIC = 360  # 15 j de barres 1 h — la même fenêtre que score_pair


def ts_ms(s: str) -> float | None:
    for fmt in ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%MZ"):
        try:
            return datetime.strptime(s, fmt).replace(tzinfo=timezone.utc).timestamp() * 1000.0
        except ValueError:
            continue
    return None


def charge(pair: str) -> list[tuple[int, float]] | None:
    p = KL / f"{pair}.json"
    if not p.exists():
        return None
    try:
        raw = json.loads(p.read_text())
        return sorted((int(b[0]), float(b[4])) for b in raw)
    except Exception:
        return None


def valeur_a(bars, t: float) -> float | None:
    """Clôture la plus proche à/avant t (aucune extrapolation)."""
    lo, hi, res = 0, len(bars) - 1, None
    while lo <= hi:
        mid = (lo + hi) // 2
        if bars[mid][0] <= t:
            res = bars[mid][1]
            lo = mid + 1
        else:
            hi = mid - 1
    return res


def pic_avant(bars, t: float, n: int = FENETRE_PIC) -> float | None:
    idx = [i for i, (tt, _) in enumerate(bars) if tt <= t]
    if len(idx) < 30:
        return None
    i = idx[-1]
    deb = max(0, i - n)
    return max(v for _, v in bars[deb:i + 1])


def main() -> int:
    ajouts = []
    vus = set()
    for f in sorted(glob.glob(str(RUNS / "PAPER_V1_*.csv"))):
        try:
            with open(f, newline="", encoding="utf-8", errors="replace") as fh:
                for row in csv.DictReader(fh):
                    if (row.get("event") or "").strip() != "GBAG_SOUCHE":
                        continue
                    key = (row.get("ts"), row.get("pair"), row.get("price"), row.get("qty"))
                    if key in vus:
                        continue  # même ligne rejouée dans plusieurs journaux
                    vus.add(key)
                    ajouts.append(row)
        except Exception:
            continue

    print(f"AJOUTS DE SOUCHE uniques : {len(ajouts)}")
    cache: dict[str, list] = {}
    btc = charge("BTCUSDT")     # contrôle par le RÉGIME (marché sur la même fenêtre)
    obs = []
    for r in ajouts:
        pair = (r.get("pair") or "").strip()
        t = ts_ms((r.get("ts") or "").strip())
        try:
            prix = float(r.get("price"))
        except (TypeError, ValueError):
            continue
        if not pair or t is None or prix <= 0:
            continue
        if pair not in cache:
            cache[pair] = charge(pair)
        bars = cache[pair]
        if not bars:
            continue
        pic = pic_avant(bars, t)
        if not pic or pic <= 0:
            continue
        dist = (1.0 - prix / pic) * 100.0
        f24 = valeur_a(bars, t + 24 * 3600 * 1000)
        f7 = valeur_a(bars, t + 7 * 86400 * 1000)
        # CONTRÔLE PAR LE RÉGIME (03/11/2026) : le plafond ABSOLU était confondu avec la
        # tendance baissière (tous les quintiles négatifs). On mesure donc l'ALPHA :
        # rendement de l'ajout MOINS celui du marché (BTC) sur la MÊME fenêtre de 7 j.
        _btc7 = None
        if btc:
            _b0 = valeur_a(btc, t)
            _b1 = valeur_a(btc, t + 7 * 86400 * 1000)
            if _b0 and _b1:
                _btc7 = (_b1 / _b0 - 1.0) * 100.0
        _r7 = ((f7 / prix - 1) * 100.0) if f7 else None
        obs.append({
            "pair": pair, "ts": t, "prix": prix, "dist": dist,
            "r24": ((f24 / prix - 1) * 100.0) if f24 else None,
            "r7": _r7,
            "alpha": (_r7 - _btc7) if (_r7 is not None and _btc7 is not None) else None,
        })

    if not obs:
        print("AUCUNE observation mesurable (klines absentes ?) — on ne conclut pas.")
        return 0

    obs.sort(key=lambda o: o["dist"])
    print(f"observations mesurables : {len(obs)}")
    n = len(obs)
    k = 5
    taille = max(1, n // k)
    print()
    print(f"{'quintile':>9}{'dist au sommet':>18}{'n':>5}{'R+24h méd':>12}{'R+7j méd':>11}{'ALPHA+7j':>10}{'R+7j <0':>9}")
    for q in range(k):
        tranche = obs[q * taille:(q + 1) * taille] if q < k - 1 else obs[q * taille:]
        if not tranche:
            continue
        d = [o["dist"] for o in tranche]
        r24 = [o["r24"] for o in tranche if o["r24"] is not None]
        r7 = [o["r7"] for o in tranche if o["r7"] is not None]
        neg = (sum(1 for x in r7 if x < 0) / len(r7) * 100.0) if r7 else float("nan")
        al = [o["alpha"] for o in tranche if o["alpha"] is not None]
        print(f"{q+1:>9}{min(d):>7.1f}–{max(d):<9.1f}{len(tranche):>5}"
              f"{(statistics.median(r24) if r24 else float('nan')):>+12.2f}"
              f"{(statistics.median(r7) if r7 else float('nan')):>+11.2f}"
              f"{(statistics.median(al) if al else float('nan')):>+10.2f}{neg:>8.0f}%")

    mes = [o for o in obs if o["r7"] is not None]
    mid = ts_ms("2026-10-15T00:00:00Z")
    print()
    print("STABILITÉ (R+7j médian, ajouts proches du sommet vs loin) :")
    for lib, sel in (("ajouts < 5 % du sommet", [o for o in mes if o["dist"] < 5]),
                     ("ajouts ≥ 5 % du sommet", [o for o in mes if o["dist"] >= 5])):
        a = [o["r7"] for o in sel if o["ts"] < mid]
        b = [o["r7"] for o in sel if o["ts"] >= mid]
        print(f"  {lib:26} n={len(sel):3} · médiane {statistics.median([o['r7'] for o in sel]):+6.2f}%"
              f" · avant 15/10 {statistics.median(a):+6.2f}%" if a else
              f"  {lib:26} n={len(sel):3} · avant 15/10 : non mesuré", end="")
        print(f" · après {statistics.median(b):+6.2f}%" if b else " · après : non mesuré")

    print()
    print("LECTURE (décision sur l'ALPHA, pas sur le brut) : le plafond candidat est la borne")
    print("HAUTE du premier quintile dont l'ALPHA+7j médian devient négatif. Si tous les")
    print("quintiles ont un alpha positif/nul, la pyramide ne coûte rien de mesurable ; si")
    print("tous sont négatifs, le problème n'est pas la distance au sommet mais le fait")
    print("d'ajouter en tendance baissière → aucun plafond câblé, re-mesure à programmer.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

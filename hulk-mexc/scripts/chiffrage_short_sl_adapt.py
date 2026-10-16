#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""chiffrage_short_sl_adapt.py — GO short 16/10/2026 (Christophe : « go »).

QUESTION : le SL fixe +1,5 % se fait chasser par le bruit (7/11 mauvais stops
mesurés le 16/10) ; le filtre creux éviterait de shorter au fond.
MÉTHODE (brut) : on rejoue les VRAIES entrées du journal sur les bougies 1 h du
cache (24/08→08/10), MÊMES entrées, seule la sortie change :
  A (actuel) : TP -2 % / SL +1,5 % fixe / TIME_OUT 24 h.
  B (adaptatif) : TP -2 % / SL +0,5×amp7 walk-forward / TIME_OUT 24 h.
  + diagnostic filtre creux : distance entrée → plus-bas 7 j (les mauvais stops
    sont-ils pris au fond ?).
SIGNAL_ETEINT ignoré des DEUX côtés (même condition, comparaison équitable —
limite déclarée). Clôtures 1 h (pas de ticks live) — même biais des deux côtés.
Lecture seule, 0 ordre, 0 €.
"""
from __future__ import annotations

import bisect
import csv
import json
import statistics
import sys
from datetime import datetime
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
CACHE = RACINE / "runs" / "replay_cache" / "BTCUSDT_1h_45j.json"
JOURNAL = RACINE / "runs" / "short_btc_journal.csv"
NOTIONAL = 5.0
TP_PCT = 2.0
SL_FIXE = 1.5
TTL_H = 24


def charger():
    kl = json.load(open(CACHE, encoding="utf-8"))
    return [b["t"] for b in kl], [float(b["c"]) for b in kl], \
        [float(b["h"]) for b in kl], [float(b["l"]) for b in kl]


def amp7_a(idx, H, L, TS):
    """Médiane des ranges journaliers des 7 jours ENTIÈREMENT précédents (walk-forward)."""
    ranges = []
    d0 = (TS[idx] // 86_400_000) * 86_400_000
    for j in range(1, 8):
        lo, hi = d0 - j * 86_400_000, d0 - (j - 1) * 86_400_000
        a = bisect.bisect_left(TS, lo)
        b = bisect.bisect_left(TS, hi)
        seg_h = H[a:b]
        seg_l = L[a:b]
        if seg_h and seg_l and min(seg_l) > 0:
            ranges.append((max(seg_h) - min(seg_l)) / min(seg_l) * 100.0)
    return statistics.median(ranges) if len(ranges) == 7 else None


def low7_a(idx, L, TS):
    d0 = (TS[idx] // 86_400_000) * 86_400_000
    a = bisect.bisect_left(TS, d0 - 7 * 86_400_000)
    seg = L[a:idx]
    return min(seg) if seg else None


def range24_a(idx, H, L, TS):
    """Range % des 24 bougies précédentes — amplitude à l'horizon du trade (TTL 24 h).
    Calculable EN LIVE depuis le flux existant (~30 h de points bruts) : pas de
    nouvelle dépendance, on utilise le sang déjà présent (organisme)."""
    if idx < 24:
        return None
    seg_h, seg_l = H[idx - 24:idx], L[idx - 24:idx]
    return (max(seg_h) - min(seg_l)) / min(seg_l) * 100.0 if min(seg_l) > 0 else None


def low24_a(idx, L, TS):
    if idx < 24:
        return None
    seg = L[idx - 24:idx]
    return min(seg) if seg else None


def rejouer(entree, ts_entree, sl_pct, TS, C):
    e = int(datetime.fromisoformat(ts_entree.replace("Z", "+00:00")).timestamp() * 1000)
    i0 = bisect.bisect_right(TS, e) - 1
    if i0 < 0 or i0 + TTL_H >= len(C):
        return None
    adv_max = 0.0
    for k in range(1, TTL_H + 1):
        c = C[i0 + k]
        adv_max = max(adv_max, 100 * (c - entree) / entree)
        if c <= entree * (1 - TP_PCT / 100):
            return ("TP", c, adv_max)
        if c >= entree * (1 + sl_pct / 100):
            return ("SL", c, adv_max)
    c = C[i0 + TTL_H]
    adv_max = max(adv_max, 100 * (c - entree) / entree)
    return ("TIME_OUT", c, adv_max)


def main():
    TS, C, H, L = charger()
    # Lignes de TEST exclues (ts 'x' synthétique + prix 100.0/80000.0) : pas du marché.
    rows = [r for r in csv.DictReader(open(JOURNAL, encoding="utf-8"))
            if (r.get("ts_entree") or "")[:4].isdigit() and float(r["prix_entree"]) > 1000]
    res = {k: {"TP": 0, "SL": 0, "TIME_OUT": 0, "pnl": 0.0}
           for k in ("A", "B", "B2", "C2", "D")}
    creux = []  # (dist_low_pct, issue_A)
    hors = 0
    for r in rows:
        entree = float(r["prix_entree"])
        e = int(datetime.fromisoformat(r["ts_entree"].replace("Z", "+00:00")).timestamp() * 1000)
        i0 = bisect.bisect_right(TS, e) - 1
        if i0 < 0 or i0 + TTL_H >= len(C):
            hors += 1
            continue
        a7 = amp7_a(i0, H, L, TS)
        sl_b = 0.5 * a7 if a7 else SL_FIXE
        r24 = range24_a(i0, H, L, TS)
        sl_b2 = 0.5 * r24 if r24 else SL_FIXE
        lo24 = low24_a(i0, L, TS)
        creux24 = bool(lo24 and 100 * (entree - lo24) / lo24 < 2.0)
        ra = rejouer(entree, r["ts_entree"], SL_FIXE, TS, C)
        rb = rejouer(entree, r["ts_entree"], sl_b, TS, C)
        rb2 = rejouer(entree, r["ts_entree"], sl_b2, TS, C)
        # C2/D : le filtre creux 24 h ÉVITE l'entrée (pas de trade, pnl 0).
        rc2 = None if creux24 else ra
        rd = None if creux24 else rb2
        for key, rr in (("A", ra), ("B", rb), ("B2", rb2)):
            res[key][rr[0]] += 1
            res[key]["pnl"] += (entree - rr[1]) / entree * NOTIONAL
        for key, rr in (("C2", rc2), ("D", rd)):
            if rr is None:
                continue
            res[key][rr[0]] += 1
            res[key]["pnl"] += (entree - rr[1]) / entree * NOTIONAL
        res["C2"].setdefault("evites", 0)
        res["D"].setdefault("evites", 0)
        if creux24:
            res["C2"]["evites"] += 1
            res["D"]["evites"] += 1
        lo = low7_a(i0, L, TS)
        if lo:
            creux.append((100 * (entree - lo) / lo, ra[0]))
    n = len(rows) - hors
    for key in ("A", "B", "B2", "C2", "D"):
        v = res[key]
        ev = f" · {v.get('evites', 0)} entrées évitées" if "evites" in v else ""
        print(f"{key} : TP {v['TP']} · SL {v['SL']} · TIME_OUT {v['TIME_OUT']} · "
              f"PnL {v['pnl']:+.4f} ${ev} ({n} trades rejoués, {hors} hors fenêtre)")
    print("LÉGENDE : A=SL fixe 1,5 % (actuel) · B=SL 0,5×amp7 · B2=SL 0,5×range24h · "
          "C2=A+filtre creux 24 h · D=B2+filtre creux 24 h")
    pres = [d for d, _ in creux if d < 2.0]
    print(f"FILTRE CREUX : {len(pres)}/{len(creux)} entrées à <2 % du plus-bas 7 j ; "
          f"issues : {dict((k, sum(1 for d, i in creux if d < 2.0 and i == k)) for k in ('TP', 'SL', 'TIME_OUT'))}")
    print("LIMITES (R8) : clôtures 1 h (pas de ticks) · SIGNAL_ETEINT ignoré des 2 côtés · "
          "mêmes entrées journal (pas de re-sélection) · ÉTUDE, pas preuve hors échantillon.")


if __name__ == "__main__":
    main()

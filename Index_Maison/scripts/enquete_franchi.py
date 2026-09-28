#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENQUÊTE FRANCHI — reconstruction post-hoc sur le corpus L2 EXISTANT (lecture seule).
Constat code (07/09) : superviseur_l2.py n'a JAMAIS implémenté l'événement FRANCHI
(seules APPARU / EVAPORE / SPOOF existent) → les 0 FRANCHI du rapport L2 étaient un
trou d'instrumentation, pas une vérité de marché. Ce script répond à la question
AVEC LES DONNÉES DÉJÀ COLLECTÉES, sans toucher au superviseur qui continue de tourner.

Méthode (causale, par événement) : pour chaque EVAPORE au niveau (side, px) à t :
  - le mid a-t-il TRAVERSÉ le niveau dans les WINDOW_S s suivantes ?
      BID : mid < px   (le prix est passé sous le mur acheteur = mur renversé)
      ASK : mid > px   (le prix est passé au-dessus du mur vendeur)
  - un APPARU est-il revenu au même (side, px) dans les 120 s (fenêtre SPOOF du superviseur) ?
Classification 2×2 :
  SPOOF-PUR       réapparu ≤120s ET non traversé   → façade confirmée (le mensonge marche)
  SPOOF-RENVERSÉ  réapparu ≤120s ET traversé       → façade qui a SAUTÉ sous le prix
  FRANCHI         traversé ET jamais réapparu      → mur réellement consommé
  PULL            ni traversé ni réapparu          → mur retiré volontairement (obéissance)
"""
import csv, bisect, statistics
from collections import defaultdict
from datetime import datetime, timezone

RUNS = "/Users/christophe/ace777-test-day1/runs"
SNAPS = f"{RUNS}/L2_20260903_SNAPS.csv"
MURS = f"{RUNS}/L2_20260903_MURS.csv"
WINDOW_S = 60          # fenêtre de traversée du prix après évaporation
SPOOF_WIN = 120        # même fenêtre que le superviseur (réapparition)

_memo = {}
def to_epoch(ts):
    v = _memo.get(ts)
    if v is None:
        v = int(datetime.strptime(ts, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp())
        _memo[ts] = v
    return v

def main():
    # ---- mids triés (un point par seconde max) ----
    ts_list, mid_list = [], []
    with open(SNAPS) as f:
        rd = csv.reader(f)
        next(rd)
        for row in rd:
            ts_list.append(to_epoch(row[0]))
            mid_list.append(float(row[1]))
    print(f"SNAPS : {len(ts_list):,} points · {((ts_list[-1]-ts_list[0])/3600):.1f} h")

    # ---- apparus par clé (pour la réapparition ≤120s) ----
    apparus = defaultdict(list)
    evaps = []  # (t, side, px, notional)
    with open(MURS) as f:
        rd = csv.reader(f)
        next(rd)
        for row in rd:
            ts_s, side, px_s, not_s, event = row
            if event == "APPARU":
                apparus[(side, float(px_s))].append(to_epoch(ts_s))
            elif event == "EVAPORE":
                evaps.append((to_epoch(ts_s), side, float(px_s), float(not_s)))
    for k in apparus:
        apparus[k].sort()
    print(f"MURS : {len(evaps):,} EVAPORE à classifier")

    cls = defaultdict(int)                     # classe -> count
    notional_by_cls = defaultdict(list)        # classe -> notionales
    spoof_runover_notional = []
    crossed_delays = []
    for (t, side, px, notional) in evaps:
        # traversée du prix dans [t, t+WINDOW_S]
        i0 = bisect.bisect_left(ts_list, t)
        i1 = bisect.bisect_left(ts_list, t + WINDOW_S)
        crossed = False
        if side == "BID":
            for i in range(i0, i1):
                if mid_list[i] < px:
                    crossed = True
                    crossed_delays.append(ts_list[i] - t)
                    break
        else:
            for i in range(i0, i1):
                if mid_list[i] > px:
                    crossed = True
                    crossed_delays.append(ts_list[i] - t)
                    break
        # réapparition ≤120s
        lst = apparus.get((side, px))
        reapp = False
        if lst:
            j = bisect.bisect_right(lst, t)
            if j < len(lst) and (lst[j] - t) <= SPOOF_WIN:
                reapp = True
        if reapp and crossed:
            c = "SPOOF-RENVERSE"
            spoof_runover_notional.append(notional)
        elif reapp:
            c = "SPOOF-PUR"
        elif crossed:
            c = "FRANCHI"
        else:
            c = "PULL"
        cls[c] += 1
        notional_by_cls[c].append(notional)

    total = sum(cls.values())
    q = lambda arr, p: sorted(arr)[int(p * (len(arr) - 1))] if arr else 0
    print("\n" + "=" * 74)
    print(f"TABLE DE CALIBRATION — destin des {total:,} murs évaporés (fenêtre {WINDOW_S}s)")
    print("=" * 74)
    labels = {
        "SPOOF-PUR":      "SPOOF-PUR       (réapparu, prix n'a pas traversé) = façade OK",
        "SPOOF-RENVERSE": "SPOOF-RENVERSÉ  (réapparu MAIS prix a traversé) = façade sautée",
        "FRANCHI":        "FRANCHI         (prix a traversé, jamais revenu) = mur mangé",
        "PULL":           "PULL            (rien traversé, jamais revenu)   = mur retiré",
    }
    for c in ("SPOOF-PUR", "SPOOF-RENVERSE", "FRANCHI", "PULL"):
        n = cls[c]
        arr = notional_by_cls[c]
        if n:
            print(f"  {labels[c]:<62} {n:7,} ({100.0*n/total:5.1f} %) · notional médian {statistics.median(arr):>9,.0f} $ · p95 {q(arr,0.95):>9,.0f} $")
        else:
            print(f"  {labels[c]:<62} {0:7,} (  0.0 %)")
    if crossed_delays:
        print(f"\n  Délai évaporation→traversée : médian {statistics.median(crossed_delays):.0f} s · p95 {sorted(crossed_delays)[int(0.95*len(crossed_delays))]:.0f} s")
    # lecture pour la V3
    n_shield_ok = cls["SPOOF-PUR"] + cls["PULL"]
    print(f"\n  LECTURE V3 : murs 'fiables comme bouclier' (PULL+SPOOF-PUR tenus) = {100.0*n_shield_ok/total:.1f} %"
          f" · murs qui cèdent au prix (FRANCHI+SPOOF-RENVERSÉ) = {100.0*(cls['FRANCHI']+cls['SPOOF-RENVERSE'])/total:.1f} %")
    print("  (Un-essai post-hoc sur données existantes — la décision reste à la famille.)")

if __name__ == "__main__":
    main()

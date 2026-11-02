#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""replay_c3_sens.py — RE-MESURE C3 (02/11, GO Christophe).

Le fix signe (§62) a permuté le sens des branches C3 sans re-validation.
On rejoue : pour chaque avis passé (croisements_indices_hist.jsonl, >= 02/10),
flux 48h re-agrégé du ledger à la date de l'avis + chg24 des DIGEST,
règle NEUVE (sortie = net > 0), puis move BTC +24h (DIGEST) :
HIT si le sens prédit le signe du move. Lecture seule.
"""
import csv
import glob
import json
import os
import sys
from datetime import datetime, timezone, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flux_nets_exchanges import charger_registre, charger_ledger_dedup, _agreger

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "Index_Maison", "data") if os.path.basename(ROOT) != "Index_Maison" else os.path.join(ROOT, "data")
RUNS = os.path.join(os.path.dirname(ROOT), "ace777-test-day1", "hulk-mexc", "runs")
if not os.path.isdir(RUNS):
    RUNS = "/Users/christophe/ace777-test-day1/hulk-mexc/runs"

SEUIL_FLUX_BTC = 5.0


def parse_ts(s):
    try:
        return datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    except Exception:
        return None


marks = {}
for f in sorted(glob.glob(RUNS + "/DIGEST_20261*.json")):
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception:
        continue
    t = parse_ts(d.get("ts"))
    if t is None:
        continue
    for e in (d.get("pairs") or []):
        try:
            if e.get("pair") == "BTCUSDT" and float(e.get("last") or 0) > 0:
                marks[t] = float(e["last"])
        except Exception:
            continue
mts = sorted(marks)


def mark_at(t):
    best = None
    for x in mts:
        if x <= t:
            best = x
        else:
            break
    return marks.get(best)


def mark_after(t, h=24):
    t1 = t + timedelta(hours=h)
    for x in mts:
        if x >= t1:
            return marks[x]
    return None


EX = charger_registre()
MVT, _ = charger_ledger_dedup()
hist = [json.loads(l) for l in open(os.path.join(DATA, "croisements_indices_hist.jsonl"), encoding="utf-8") if l.strip()]

res = {"LONG": [], "SHORT": [], "NEUTRE": []}
couverture = 0
for h in hist:
    t = parse_ts(h.get("ts"))
    if t is None or t < datetime(2026, 10, 2, tzinfo=timezone.utc):
        continue
    p0 = mark_at(t - timedelta(hours=24))
    p1 = mark_at(t)
    p2 = mark_after(t, 24)
    if not p0 or not p1 or not p2 or p0 <= 0 or p1 <= 0:
        continue
    chg24 = 100.0 * (p1 / p0 - 1)
    t48 = (t - timedelta(hours=48)).strftime("%Y-%m-%dT%H:%M")
    w = _agreger(MVT, EX, t48, t.strftime("%Y-%m-%dT%H:%M"))
    net = w["btc_sortant"] - w["btc_entrant"]
    if abs(net) < SEUIL_FLUX_BTC or abs(chg24) < 1.0:
        continue
    sortie = net > 0  # SENS NEUF (fix §62)
    baisse = chg24 < 0
    if sortie and baisse:
        sens = "NEUTRE"
    elif (not sortie) and baisse:
        sens = "LONG"
    elif sortie and (not baisse):
        sens = "SHORT"
    else:
        sens = None  # entrée + hausse : la règle ne dit rien (comme avant)
    if sens is None:
        continue
    move24 = 100.0 * (p2 / p1 - 1)
    res[sens].append(move24)
    couverture += 1

print(f"avis rejoués (sens neuf) : {couverture}")
for sens in ("LONG", "SHORT", "NEUTRE"):
    mv = res[sens]
    if not mv:
        print(f"  {sens}: n=0");
        continue
    if sens == "LONG":
        hit = sum(1 for x in mv if x > 0)
    elif sens == "SHORT":
        hit = sum(1 for x in mv if x < 0)
    else:
        hit = sum(1 for x in mv if abs(x) < 2.0)  # NEUTRE = rien de violent
    print(f"  {sens}: n={len(mv)} hit={hit} ({100.0*hit/max(1,len(mv)):.0f}%) "
          f"move24_med={sorted(mv)[len(mv)//2]:+.2f}% min={min(mv):+.2f}% max={max(mv):+.2f}%")

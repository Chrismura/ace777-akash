#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
REPLAY_AMPLITUDE.py — est-ce que la fenêtre par paire + une sortie calibrée sur l'amplitude
rapporte plus que la sortie FIXE actuelle (+2 %) ?

But (demande Christophe 20/09/2026) : chiffrer, sur des prix réels et avec des fenêtres
RECALCULÉES PAR PAIRE ET PAR PÉRIODE (aucune heure figée), ce que vaudrait une sortie
calibrée sur l'amplitude du moment, à entrées identiques.

Méthode :
  - prix réels : klines 1h MEXC (les mêmes que le banc 20 actifs), cache local.
  - pour chaque jour D, on calibre sur les W jours PRÉCÉDENTS seulement (walk-forward réel) :
      h_creux = heure UTC au prix moyen le plus bas · h_pic = heure UTC au prix moyen le plus haut
      amp     = range journalier médian sur la fenêtre de calibration (%)
  - 2 entrées : (A) creux seul  (B) creux seul + fenêtre = h_creux ± 1h
  - 3 sorties, sur les mêmes entrées :
      S1 "ACTUEL"   : +2 % sur la mise (la règle rip 2,0 % d'aujourd'hui)
      S2 "PIC"      : sortie à l'heure du pic recalculée (fin de la fenêtre h_pic ± 1h)
      S3 "AMPLITUDE": trailing = 40 % de l'amplitude calibrée du moment, stop 20 %, sortie au pic
  - frais 5 bps/côté (10 bps aller-retour), comme le banc maison.
  - découpage : 1re moitié = calibration/lecture, 2e moitié = test hors échantillon.

Aucun ordre, aucun € : recherche pure.
"""
import json
import os
import sys
import time
import urllib.request
from datetime import datetime, timezone
from statistics import median

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUNS = os.path.join(BASE, "runs")
CACHE = os.path.join(RUNS, "replay_cache")
os.makedirs(CACHE, exist_ok=True)

PAIRS = ["BTCUSDT", "ETHUSDT", "XRPUSDT", "HBARUSDT", "RIZEUSDT", "ZBCNUSDT", "WUSDT",
         "REDUSDT", "CCUSDT", "PYTHUSDT", "BIOUSDT", "KITEUSDT", "TELUSDT", "CHIPUSDT",
         "RWAINCUSDT", "EDELUSDT", "QNTUSDT", "FLUIDUSDT", "RWAUSDT", "MNSRYUSDT"]
DAYS = int(os.environ.get("REPLAY_DAYS", "45"))
W_CAL = 7           # jours de calibration glissante (avant le jour tradé)
FEE = 0.0005        # 5 bps par côté
TRAIL_FRAC = 0.40   # trailing = 40 % de l'amplitude calibrée
STOP_FRAC = 0.20    # stop = 20 % de l'amplitude calibrée


def fetch(pair, days=DAYS):
    """Klines 1h MEXC avec cache local (aucune dépendance à un autre script)."""
    cf = os.path.join(CACHE, f"{pair}_1h_{days}j.json")
    if os.path.exists(cf) and time.time() - os.path.getmtime(cf) < 6 * 3600:
        return json.load(open(cf))
    end = int(time.time() * 1000)
    cur = end - days * 86400 * 1000
    out = []
    while cur < end:
        u = (f"https://api.mexc.com/api/v3/klines?symbol={pair}&interval=60m"
             f"&startTime={cur}&endTime={end}&limit=500")
        try:
            with urllib.request.urlopen(u, timeout=20) as r:
                data = json.loads(r.read().decode())
        except Exception as e:
            print(f"  ! {pair} requête échouée: {e}", file=sys.stderr)
            break
        if not data:
            break
        out += data
        last = data[-1][0]
        if last <= cur:
            break
        cur = last + 1
        time.sleep(0.15)
    # [openTime, o,h,l,c, v, ...]
    bars = [{"t": d[0], "o": float(d[1]), "h": float(d[2]), "l": float(d[3]),
             "c": float(d[4])} for d in out]
    json.dump(bars, open(cf, "w"))
    return bars


def hour_utc(ms):
    return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).hour


def day_utc(ms):
    return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).strftime("%Y-%m-%d")


def calibrer(bars_cal):
    """Fenêtre + amplitude calibrées SUR LES JOURS PRÉCÉDENTS seulement."""
    if len(bars_cal) < 24 * 3:
        return None
    par_heure = {}
    for b in bars_cal:
        par_heure.setdefault(hour_utc(b["t"]), []).append(b["c"])
    moy = {h: sum(v) / len(v) for h, v in par_heure.items() if v}
    if len(moy) < 12:
        return None
    h_creux = min(moy, key=moy.get)
    h_pic = max(moy, key=moy.get)
    # amplitude = range journalier médian (%)
    par_jour = {}
    for b in bars_cal:
        d = day_utc(b["t"])
        j = par_jour.setdefault(d, {"h": b["h"], "l": b["l"]})
        j["h"] = max(j["h"], b["h"])
        j["l"] = min(j["l"], b["l"])
    amps = [(j["h"] - j["l"]) / j["l"] * 100 for j in par_jour.values() if j["l"] > 0]
    if not amps:
        return None
    return {"h_creux": h_creux, "h_pic": h_pic, "amp": median(amps)}


def simuler(bars, cal):
    """Simule une journée : entrée au creux, 3 sorties comparées."""
    if not bars:
        return None
    hc, hp, amp = cal["h_creux"], cal["h_pic"], cal["amp"]
    # entrée : 1re bougie de la fenêtre de creux (hc ± 1h)
    fen = {(hc - 1) % 24, hc, (hc + 1) % 24}
    ent = next((b for b in bars if hour_utc(b["t"]) in fen), None)
    if not ent:
        return None
    px_in = ent["c"]
    if px_in <= 0:
        return None
    apres = [b for b in bars if b["t"] > ent["t"]]

    # S2/S3 : sortie visée sur la fenêtre de pic (hp ± 1h)
    fens = {(hp - 1) % 24, hp, (hp + 1) % 24}
    pic_fin = next((b for b in apres if hour_utc(b["t"]) in fens), None)

    res = {"in": px_in, "amp": amp}
    # S1 — règle ACTUELLE : +2 % sur la mise
    res["s1"] = None
    for b in apres:
        if b["h"] >= px_in * 1.02:
            res["s1"] = 2.0
            break
    if res["s1"] is None:
        last = apres[-1]["c"] if apres else px_in
        res["s1"] = (last - px_in) / px_in * 100
    # S2 — sortie à la fin de la fenêtre de pic
    if pic_fin:
        res["s2"] = (pic_fin["c"] - px_in) / px_in * 100
    else:
        last = apres[-1]["c"] if apres else px_in
        res["s2"] = (last - px_in) / px_in * 100
    # S3 — trailing = 40 % de l'amplitude calibrée, stop 20 %, sortie au pic au plus tard
    cible = TRAIL_FRAC * amp
    stop = STOP_FRAC * amp
    plus_haut = px_in
    res["s3"] = None
    for b in apres:
        plus_haut = max(plus_haut, b["h"])
        gain = (plus_haut - px_in) / px_in * 100
        if gain >= cible and (b["l"] - px_in) / px_in * 100 <= gain - cible:
            res["s3"] = gain - cible
            break
        if (b["l"] - px_in) / px_in * 100 <= -stop:
            res["s3"] = (b["l"] - px_in) / px_in * 100
            break
        if pic_fin and b["t"] >= pic_fin["t"]:
            res["s3"] = (b["c"] - px_in) / px_in * 100
            break
    if res["s3"] is None:
        last = apres[-1]["c"] if apres else px_in
        res["s3"] = (last - px_in) / px_in * 100
    # frais aller-retour
    for k in ("s1", "s2", "s3"):
        res[k] -= 100 * FEE * 2
    return res


def main():
    print(f"REPLAY AMPLITUDE — {len(PAIRS)} paires · {DAYS} j de klines 1h · "
          f"calibration glissante {W_CAL} j · frais 10 bps A/R\n")
    tous = []
    for p in PAIRS:
        bars = fetch(p)
        if len(bars) < 24 * (W_CAL + 3):
            print(f"{p:11s} données insuffisantes ({len(bars)} bougies)")
            continue
        jours = sorted({day_utc(b["t"]) for b in bars})
        lignes = []
        for d in jours[W_CAL:]:
            bc = [b for b in bars if day_utc(b["t"]) < d]
            bars_d = [b for b in bars if day_utc(b["t"]) == d]
            cal = calibrer(bc[-24 * W_CAL:])
            if not cal:
                continue
            r = simuler(bars_d, cal)
            if r:
                r["jour"] = d
                lignes.append(r)
                tous.append(r)
        if not lignes:
            continue
        n = len(lignes)
        for k, lbl in (("s1", "S1 +2% fixe (actuel)"), ("s2", "S2 sortie au pic"), ("s3", "S3 amplitude/trailing")):
            vals = [x[k] for x in lignes]
            mo = sum(vals) / n
            wr = 100 * sum(1 for v in vals if v > 0) / n
            print(f"{p:11s} {lbl:24s} n={n:3d} · moyenne {mo:+6.2f} % · win {wr:4.1f} % · total {sum(vals):+8.1f} %")
        print()
    if not tous:
        print("aucune donnée")
        return
    n = len(tous)
    print(f"=== AGRÉGAT (toutes paires, {n} journées-paires) ===")
    for k, lbl in (("s1", "S1 +2 % fixe (règle ACTUELLE)"), ("s2", "S2 sortie à la fenêtre de pic"),
                   ("s3", "S3 sortie calibrée sur l'amplitude")):
        vals = [x[k] for x in tous]
        mo = sum(vals) / n
        wr = 100 * sum(1 for v in vals if v > 0) / n
        print(f"  {lbl:36s} moyenne {mo:+6.2f} %/jour-paire · win {wr:4.1f} % · total {sum(vals):+9.1f} %")
    # calibration / test
    cut = n // 2
    print("\n  -- 1re moitié (calibration) vs 2e moitié (test) --")
    for k, lbl in (("s1", "S1 actuel"), ("s2", "S2 pic"), ("s3", "S3 amplitude")):
        a = [x[k] for x in tous[:cut]]
        b = [x[k] for x in tous[cut:]]
        print(f"  {lbl:12s} calib {sum(a)/max(1,len(a)):+6.2f} %   test {sum(b)/max(1,len(b)):+6.2f} %")
    json.dump({"ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
               "days": DAYS, "w_cal": W_CAL, "fee_per_side": FEE,
               "trail_frac": TRAIL_FRAC, "stop_frac": STOP_FRAC,
               "n": n, "detail": tous},
              open(os.path.join(RUNS, f"REPLAY_AMPLITUDE_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M')}.json"), "w"),
              ensure_ascii=False, indent=1)
    print(f"\nsortie enregistrée dans runs/REPLAY_AMPLITUDE_*.json")


if __name__ == "__main__":
    main()

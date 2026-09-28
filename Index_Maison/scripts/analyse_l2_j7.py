#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ANALYSE L2 — LES 4 MÉTRIQUES J+7 (protocole R32, anticipé à la demande du propriétaire).
Lecture seule : runs/L2_20260903_SNAPS.csv + runs/L2_20260903_MURS.csv. Zéro ordre, zéro contact moteur.

Les 4 métriques (figées R32) :
  1. Time-to-Heal du mur        : EVAPORE → prochaine APPARITION au même (side, px)
  2. OFI 5 s pré/post évaporation : Order Flow Imbalance (Cont, best levels) avant/après chaque EVAPORE
  3. Taux de spoofing           : SPOOF / EVAPORE + distribution des vies de murs (FPC : % morts ≤ 3 s)
  4. Profil de volatilité micro-structurelle : |Δmid|/s, spread, vol réalisée horaire

Bonus calibration « mur institutionnel BTC » : notional des murs FRANCHI (consommés = vrais)
vs EVAPORE (tirés) — la distinction que la famille demande depuis R32/C4.
"""
import csv, statistics, sys
from collections import defaultdict
from datetime import datetime, timezone

RUNS = "/Users/christophe/ace777-test-day1/runs"
SNAPS = f"{RUNS}/L2_20260903_SNAPS.csv"
MURS  = f"{RUNS}/L2_20260903_MURS.csv"

_ts_memo = {}
def to_epoch(ts):
    """'2026-09-03T19:39:01Z' -> epoch s (memoïsé, les secondes se répètent)."""
    v = _ts_memo.get(ts)
    if v is None:
        v = int(datetime.strptime(ts, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp())
        _ts_memo[ts] = v
    return v

def main():
    # ---------- 1. MURS : vies, heals, spoofing, franchis ----------
    # vie = APPARU → (EVAPORE | FRANCHI) au même (side, px)
    open_walls = {}            # (side, px) -> ts_apparu
    lifetimes = []             # (durée s, notional, issue)  issue ∈ {EVAPORE, FRANCHI}
    evap_events = []           # (ts, side, px, notional)
    n_spoof = n_apparu = n_evap = n_franchi = 0
    t_first = t_last = None

    with open(MURS) as f:
        rd = csv.reader(f)
        next(rd)
        for row in rd:
            ts_s, side, px_s, not_s, event = row
            t = to_epoch(ts_s)
            if t_first is None: t_first = t
            t_last = t
            px = float(px_s)
            notional = float(not_s)
            key = (side, px)
            if event == "APPARU":
                n_apparu += 1
                open_walls[key] = (t, notional)
            elif event == "EVAPORE":
                n_evap += 1
                evap_events.append((t, side, px, notional))
                birth = open_walls.pop(key, None)
                if birth:
                    lifetimes.append((t - birth[0], birth[1], "EVAPORE"))
            elif event == "FRANCHI":
                n_franchi += 1
                birth = open_walls.pop(key, None)
                if birth:
                    lifetimes.append((t - birth[0], birth[1], "FRANCHI"))
            elif event == "SPOOF":
                n_spoof += 1

    hours = (t_last - t_first) / 3600 if t_first else 0

    # Time-to-Heal : pour chaque EVAPORE, prochaine APPARU au même (side, px)
    apparus_by_key = defaultdict(list)
    with open(MURS) as f:
        rd = csv.reader(f)
        next(rd)
        for row in rd:
            if row[4] == "APPARU":
                apparus_by_key[(row[1], float(row[2]))].append(to_epoch(row[0]))
    for k in apparus_by_key:
        apparus_by_key[k].sort()

    import bisect
    heals = []
    for (t, side, px, _n) in evap_events:
        lst = apparus_by_key.get((side, px))
        if not lst: continue
        i = bisect.bisect_right(lst, t)
        if i < len(lst):
            heals.append(lst[i] - t)
        # sinon : jamais reconstruit dans le corpus

    n_healed = len(heals)
    med_tth = statistics.median(heals) if heals else float("nan")
    pct = lambda arr, ms: 100.0 * sum(1 for x in arr if x <= ms) / len(arr) if arr else float("nan")

    # Vies de murs (FPC)
    lifes = [d for d, _n, _i in lifetimes]
    med_life = statistics.median(lifes) if lifes else float("nan")
    pct_life3 = pct(lifes, 3)
    pct_life10 = pct(lifes, 10)
    pct_life60 = pct(lifes, 60)

    # notional FRANCHI vs EVAPORE (calibration « institutionnel »)
    not_fr = [n for _d, n, i in lifetimes if i == "FRANCHI"]
    not_ev = [n for _d, n, i in lifetimes if i == "EVAPORE"]

    # ---------- 2. SNAPS : OFI + volatilité micro ----------
    snaps = []  # (t, mid, spread, bid1_px, bid1_sz, ask1_px, ask1_sz, med_notional)
    with open(SNAPS) as f:
        rd = csv.reader(f)
        next(rd)
        for row in rd:
            snaps.append((to_epoch(row[0]), float(row[1]), float(row[2]),
                          float(row[3]), float(row[4]), float(row[5]), float(row[6]),
                          float(row[7])))

    # OFI (Cont) sur les meilleures niveaux, par seconde
    ofi_by_t = {}
    prev = None
    for s in snaps:
        t, mid, spread, bpx, bsz, apx, asz, medn = s
        if prev is not None:
            _t0, _m0, _sp0, bpx0, bsz0, apx0, asz0, _mn0 = prev
            qb, qb0, qa, qa0 = bsz * bpx, bsz0 * bpx0, asz * apx, asz0 * apx0
            ofi = ((qb if bpx >= bpx0 else -qb0) - (qa if apx <= apx0 else -qa0))
            ofi_by_t[t] = ofi / medn if medn > 0 else 0.0
        prev = s

    # OFI 5 s pré/post chaque EVAPORE
    pre_by_side = defaultdict(list)
    post_by_side = defaultdict(list)
    ts_sorted = sorted(ofi_by_t)
    for (t, side, px, _n) in evap_events:
        i0 = bisect.bisect_left(ts_sorted, t - 5)
        i1 = bisect.bisect_left(ts_sorted, t)
        i2 = bisect.bisect_left(ts_sorted, t + 5)
        pre = [ofi_by_t[ts_sorted[i]] for i in range(i0, i1)]
        post = [ofi_by_t[ts_sorted[i]] for i in range(i1, i2)]
        if pre:  pre_by_side[side].append(statistics.mean(pre))
        if post: post_by_side[side].append(statistics.mean(post))

    # volatilité micro-structurelle
    rets = []
    spreads = []
    prev_mid = None
    for s in snaps:
        _t, mid, spread, *_ = s
        if prev_mid:
            rets.append(abs(mid - prev_mid) / prev_mid * 10000)  # bps/s
        prev_mid = mid
        spreads.append(spread)
    # vol réalisée par heure (écart-type des rets/s × sqrt(3600), en bps)
    by_hour = defaultdict(list)
    for s, r in zip(snaps[1:], rets):
        by_hour[s[0] // 3600].append(r)
    hourly_rv = [statistics.stdev(v) * (3600 ** 0.5) for v in by_hour.values() if len(v) > 600]

    # ---------- RAPPORT ----------
    W = 78
    print("=" * W)
    print("ANALYSE L2 — 4 MÉTRIQUES J+7 (anticipée) — lecture seule")
    print(f"Corpus : {hours:.1f} h · {len(snaps):,} snapshots · {n_apparu+n_evap+n_franchi+n_spoof:,} événements murs")
    print("=" * W)

    print("\n--- MÉTRIQUE 1 · TIME-TO-HEAL (EVAPORE → reconstruction même niveau) ---")
    print(f"  EVAPORE apparisés : {n_healed:,} reconstruits / {len(evap_events):,} évaporations "
          f"({100.0*n_healed/len(evap_events):.1f} %)" if evap_events else "  —")
    print(f"  TTH médian : {med_tth:.0f} s · ≤3 s : {pct(heals,3):.1f} % · ≤10 s : {pct(heals,10):.1f} % · ≤60 s : {pct(heals,60):.1f} %")

    print("\n--- MÉTRIQUE 2 · OFI 5 s PRÉ/POST ÉVAPORATION (normalisé par profondeur médiane) ---")
    for side in ("BID", "ASK"):
        pre, post = pre_by_side.get(side, []), post_by_side.get(side, [])
        if pre and post:
            print(f"  Murs {side:3s} (n={len(pre):,}) : OFI pré  médian {statistics.median(pre):+.3f} "
                  f"| OFI post médian {statistics.median(post):+.3f}")

    print("\n--- MÉTRIQUE 3 · SPOOFING + VIES DE MURS (FPC) ---")
    print(f"  SPOOF déclarés : {n_spoof:,} · EVAPORE : {n_evap:,} → taux spoof/SPOOF-détectés = "
          f"{100.0*n_spoof/max(1,n_evap):.1f} %")
    print(f"  Vies (n={len(lifes):,}) : médiane {med_life:.0f} s · ≤3 s : {pct_life3:.1f} % "
          f"(R35 mesurait 76 % sur 13 min) · ≤10 s : {pct_life10:.1f} % · ≤60 s : {pct_life60:.1f} %")

    print("\n--- MÉTRIQUE 4 · VOLATILITÉ MICRO-STRUCTURELLE ---")
    if rets:
        print(f"  |Δmid| /s : médiane {statistics.median(rets):.2f} bps · p95 {sorted(rets)[int(0.95*len(rets))]:.2f} bps")
        print(f"  spread médian : {statistics.median(spreads):.2f} $ · vol réalisée horaire médiane : "
              f"{statistics.median(hourly_rv):.1f} bps · max : {max(hourly_rv):.1f} bps")

    print("\n--- BONUS CALIBRATION · MURS CONSOMMÉS (FRANCHI) vs TIRÉS (EVAPORE) ---")
    if not_fr and not_ev:
        not_fr.sort(); not_ev.sort()
        q = lambda arr, p: arr[int(p * (len(arr) - 1))]
        print(f"  FRANCHI (n={len(not_fr):,}) : médiane {statistics.median(not_fr):,.0f} $ · p75 {q(not_fr,0.75):,.0f} $ · p95 {q(not_fr,0.95):,.0f} $")
        print(f"  EVAPORE (n={len(not_ev):,}) : médiane {statistics.median(not_ev):,.0f} $ · p75 {q(not_ev,0.75):,.0f} $ · p95 {q(not_ev,0.95):,.0f} $")
        print(f"  Ratio consommés/tirés : {len(not_fr)/max(1,len(not_ev))*100:.1f} % — "
              f"les murs mangés vs les murs qui fuient.")

    print("\n(Replay honnête : chaque métrique ne lit que le passé du corpus. Zéro interprétation au-delà des chiffres.)")

if __name__ == "__main__":
    main()

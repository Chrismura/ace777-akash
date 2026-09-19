#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test A — le régime (TREND/CHOP, chop_score) est-il pertinent vs le marché ?
Rejoue la formule du moteur (vortex_regime_compute.rb : chop_score_v2 + hystérésis)
à chaque minute de la période, avec les tensions du CSV + klines Binance 1m,
puis compare au marché RÉELLEMENT réalisé dans les 15/60 min suivantes.
"""
import bisect, csv, json, re, sys, time, urllib.request
from datetime import datetime, timedelta, timezone

CSV = "/Users/christophe/ace777-test-day1/runs/MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv"
DEBUT = sys.argv[1] if len(sys.argv) > 1 else "2026-08-09"
FIN = sys.argv[2] if len(sys.argv) > 2 else "2026-08-20"
SYMBOL = "BTCUSDT"
LOOKBACK = 15  # minutes de klines
HY_HIGH, HY_LOW = 0.65, 0.45


def epoch(ts):
    return datetime.fromisoformat(ts.replace("Z", "+00:00")).timestamp()


def fetch_klines(start_ms, end_ms):
    out, cur = [], start_ms
    while cur < end_ms:
        url = (f"https://fapi.binance.com/fapi/v1/klines?symbol={SYMBOL}&interval=1m"
               f"&startTime={cur}&endTime={end_ms}&limit=1500")
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        try:
            d = json.loads(urllib.request.urlopen(req, timeout=20).read())
        except Exception as e:
            print("erreur fetch:", e)
            break
        if not d:
            break
        out.extend(d)
        cur = d[-1][0] + 60000
        time.sleep(0.15)
    return out


# 1) klines : 1m, de la veille de DEBUT jusqu'à FIN + 1h (pour le forward)
start_ms = int(epoch(DEBUT + "T00:00:00Z")) - 86400
end_ms = int(epoch(FIN + "T23:59:59Z")) + 3600
kl = fetch_klines(start_ms * 1000, end_ms * 1000)
candles = {k[0] // 1000: {"o": float(k[1]), "h": float(k[2]), "l": float(k[3]), "c": float(k[4])}
           for k in kl}
print(f"klines chargées: {len(candles)} ({datetime.fromtimestamp(start_ms, timezone.utc).date()} → "
      f"{datetime.fromtimestamp(end_ms, timezone.utc).date()})")

# 2) tensions du CSV (même lecture que le moteur : msg tension= ou mom_sig=)
rows = [r for r in csv.DictReader(open(CSV)) if DEBUT <= (r["ts"] or "")[:10] <= FIN]
tensions = []  # (ts_epoch, tension)
for r in rows:
    msg = r.get("msg") or ""
    m = re.search(r"tension=([0-9.]+)", msg)
    if m:
        t = epoch(r["ts"])
        if t is not None:
            tensions.append((t, float(m.group(1))))
tensions.sort()
print(f"lignes tension: {len(tensions)}")


def chop_score(ts, idx_tens):
    """Même formule que vortex_regime_compute.rb à l'instant ts."""
    win = [v for _, v in tensions[max(0, idx_tens - 80):idx_tens] if v > 0]
    tens_ma = sum(win) / len(win) if win else 0.0
    # klines fermées avant ts : les 16 dernières
    times = sorted(t for t in candles if t < ts)
    slice_c = [candles[t] for t in times[-LOOKBACK - 1:]]
    if len(slice_c) < 3:
        return None
    op, cl = slice_c[0]["o"], slice_c[-1]["c"]
    hi = max(c["h"] for c in slice_c)
    lo = min(c["l"] for c in slice_c)
    mid = (hi + lo) / 2.0
    trend_bps = ((cl - op) / op * 10000.0) if op else 0.0
    range_bps = ((hi - lo) / mid * 10000.0) if mid else 0.0
    rets = [abs(b["c"] - a["c"]) / max(a["c"], 1.0) * 10000.0
            for a, b in zip(slice_c[:-1], slice_c[1:])]
    vol_bps = sum(rets) / len(rets) if rets else 0.0
    trend_chop = 1.0 - min(abs(trend_bps) / 25.0, 1.0)
    range_chop = 1.0 if range_bps < 10.0 else (0.5 if range_bps < 20.0 else 0.0)
    tens_chop = 1.0 - min(tens_ma / 1.0, 1.0)
    vol_chop = 0.8 if vol_bps < 3.0 else 0.2
    return 0.30 * trend_chop + 0.25 * range_chop + 0.30 * tens_chop + 0.15 * vol_chop


# 3) rejoue le régime à chaque minute (échantillon = 1ère ligne de chaque minute)
minutes = []
seen_min = set()
for t, _ in tensions:
    m = int(t // 60)
    if m not in seen_min:
        seen_min.add(m)
        minutes.append(t)
minutes.sort()

echantillons = []  # (ts, mode, chop_score)
mode = "CHOP"
for ts in minutes:
    idx = bisect.bisect_left(tensions, (ts, -1.0))  # tensions STRICTEMENT avant ts
    s = chop_score(ts, idx)
    if s is None:
        continue
    if s > HY_HIGH:
        mode = "CHOP"
    elif s < HY_LOW:
        mode = "TREND"
    echantillons.append((ts, mode, s))


print(f"échantillons régime: {len(echantillons)} "
      f"({sum(1 for _,m,_ in echantillons if m=='TREND')} TREND / "
      f"{sum(1 for _,m,_ in echantillons if m=='CHOP')} CHOP)")

# 4) forward réalisé : |retour| et range sur 15 et 60 min
_times = sorted(candles)


def fwd(ts, minutes_ahead):
    t0 = int(ts)
    i = bisect.bisect_right(_times, t0) - 1  # bougie en cours ou dernière fermée
    if i < 0:
        return None, None
    base = candles[_times[i]]
    j0 = bisect.bisect_left(_times, t0)
    j1 = bisect.bisect_right(_times, t0 + minutes_ahead * 60)
    fen_t = _times[j0:j1]
    if len(fen_t) < 5:
        return None, None
    fen = [candles[t] for t in fen_t]
    cl_end = fen[-1]["c"]
    ret_bps = abs(cl_end - base["c"]) / base["c"] * 10000.0
    hi = max(c["h"] for c in fen)
    lo = min(c["l"] for c in fen)
    rng_bps = (hi - lo) / ((hi + lo) / 2) * 10000.0 if (hi + lo) else 0.0
    return ret_bps, rng_bps


def moy(vals):
    vals = [v for v in vals if v is not None]
    return (sum(vals) / len(vals)) if vals else 0.0

res_trend_15, res_chop_15, res_trend_60, res_chop_60 = [], [], [], []
corr_pairs_s, corr_pairs_15, corr_pairs_60 = [], [], []
for ts, m, s in echantillons:
    r15 = fwd(ts, 15)
    r60 = fwd(ts, 60)
    if r15[0] is None:
        continue
    if m == "TREND":
        res_trend_15.append(r15); res_trend_60.append(r60)
    else:
        res_chop_15.append(r15); res_chop_60.append(r60)
    corr_pairs_s.append(s)
    corr_pairs_15.append(r15[0] if r15[0] is not None else 0.0)
    corr_pairs_60.append(r60[0] if r60[0] is not None else 0.0)

def stats(nom, data15, data60):
    n = len(data15)
    r15 = [d[0] for d in data15 if d[0] is not None]
    g15 = [d[1] for d in data15 if d[1] is not None]
    r60 = [d[0] for d in data60 if d[0] is not None]
    g60 = [d[1] for d in data60 if d[1] is not None]
    hit15 = sum(1 for v in r15 if v >= 5.0) / len(r15) * 100 if r15 else 0
    hit60 = sum(1 for v in r60 if v >= 10.0) / len(r60) * 100 if r60 else 0
    print(f"{nom:<8} n={n:<6} |retour|15min={moy(r15):6.2f} bps (hit≥5bps: {hit15:.0f}%)"
          f" | range15={moy(g15):6.1f} bps | |retour|60min={moy(r60):6.2f} bps (hit≥10: {hit60:.0f}%)")

print("\n=== TEST A — régime vs marché réalisé ensuite ===")
stats("TREND", res_trend_15, res_trend_60)
stats("CHOP", res_chop_15, res_chop_60)

def corr(x, y):
    mx, my = sum(x)/len(x), sum(y)/len(y)
    num = sum((a-mx)*(b-my) for a, b in zip(x, y))
    den = (sum((a-mx)**2 for a in x) * sum((b-my)**2 for b in y)) ** 0.5
    return num/den if den else 0.0

print("\ncorrélation chop_score vs |retour|15min : %.3f" % corr(corr_pairs_s, corr_pairs_15))
print("corrélation chop_score vs |retour|60min : %.3f" % corr(corr_pairs_s, corr_pairs_60))
print("\nInterprétation : un régime pertinent = |retour| et range PLUS GRANDS en TREND qu'en CHOP,\n"
      "et chop_score corrélé NÉGATIVEMENT au mouvement réalisé (score haut = hachoir = petit mouvement).")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v2_duo_replay_4h_strict.py — MATRIX DE CONVICTION (SIMULATION COMPARATIVE).

Supervision Antigravity - 17/09/2026.
Teste plusieurs seuils de convicton (chute 4H de -0.5% à -1.2%) avec le Duo (BETA Scout 200$ + ALPHA Hunter 800$).
"""

import json
import math
import statistics
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

NOTIONNEL_SCOUT = 200.0
NOTIONNEL_HUNTER = 800.0
FRAIS_SCOUT_AR = NOTIONNEL_SCOUT * 0.0008 * 2   # 0.32 $
FRAIS_HUNTER_AR = NOTIONNEL_HUNTER * 0.0008 * 2 # 1.28 $
STOP_LOSS_BETA_BPS = 0.0025 # 25 bps = 0.25%

SPOT_URL = "https://api.binance.com/api/v3/klines"
FUT_URL = "https://fapi.binance.com/fapi/v1/klines"
FUND_URL = "https://fapi.binance.com/fapi/v1/fundingRate"

def http_json(url, tag):
    h = str(abs(hash(url)))[:12]
    cache = Path("/tmp") / f"v2duo_strict_{tag}_{h}.json"
    if cache.exists():
        try:
            d = json.loads(cache.read_text())
            if d: return d
        except Exception:
            pass
    for u in (url,):
        r = subprocess.run(["curl", "-s", "-m", "25", u], capture_output=True, text=True, timeout=30)
        try:
            data = json.loads(r.stdout)
            if isinstance(data, list) and len(data) > 0:
                cache.write_text(json.dumps(data))
                return data
        except Exception:
            continue
    return []

def fetch_4h(days=120):
    end = int(datetime(2026, 9, 12, tzinfo=timezone.utc).timestamp() * 1000)
    start = int((datetime(2026, 9, 12, tzinfo=timezone.utc) - timedelta(days=days)).timestamp() * 1000)
    kl = []
    cursor = start
    while cursor < end:
        q = f"?symbol=BTCUSDT&interval=4h&startTime={cursor}&limit=1000"
        chunk = http_json(SPOT_URL + q, "kl4h") or http_json(FUT_URL + q, "kl4h")
        if not chunk: break
        kl.extend(chunk)
        cursor = chunk[-1][6] + 1
        if len(chunk) < 1000: break
    out = []
    for k in kl:
        t_iso = datetime.fromtimestamp(k[0] / 1000, timezone.utc).strftime("%Y-%m-%d %H:%M")
        out.append({"ts": t_iso, "o": float(k[1]), "h": float(k[2]), "l": float(k[3]), "c": float(k[4])})
    return out

def fetch_daily(days=400):
    end = int(datetime(2026, 9, 12, tzinfo=timezone.utc).timestamp() * 1000)
    start = int((datetime(2026, 9, 12, tzinfo=timezone.utc) - timedelta(days=days)).timestamp() * 1000)
    q = f"?symbol=BTCUSDT&interval=1d&startTime={start}&endTime={end}&limit=1000"
    kl = http_json(SPOT_URL + q, "kl1d") or http_json(FUT_URL + q, "kl1d")
    out = []
    for k in kl:
        d = datetime.fromtimestamp(k[0] / 1000, timezone.utc).strftime("%Y-%m-%d")
        out.append({"jour": d, "c": float(k[4])})
    return out

def fetch_funding():
    data = http_json(FUND_URL + "?symbol=BTCUSDT&limit=1000", "fund")
    return [(datetime.fromtimestamp(x["fundingTime"] / 1000, timezone.utc).strftime("%Y-%m-%d %H:%M"), float(x["fundingRate"])) for x in (data or [])]

def simulate_seuil(seuil_chute):
    kl4h = fetch_4h(120)
    kl1d = fetch_daily(400)
    fund = fetch_funding()

    closes1d = [x["c"] for x in kl1d]
    regime_1d = {}
    for i in range(len(kl1d)):
        w = closes1d[:i]
        s50 = sum(w[-350:]) / min(len(w), 350) if len(w) >= 50 else None
        s200 = sum(w[-1400:]) / min(len(w), 1400) if len(w) >= 200 else None
        d = kl1d[i]["jour"]
        regime_1d[d] = "HAUSSIER" if (s50 and s200 and s50 > s200) else "NEUTRE"

    sigmas4h = [None] * len(kl4h)
    for i in range(180, len(kl4h)):
        rets = [math.log(kl4h[k]["c"] / kl4h[k-1]["c"]) for k in range(i-180, i)]
        sigmas4h[i] = statistics.pstdev(rets)

    trades_scout, trades_hunter = [], []
    pos_scout, pos_hunter = None, None
    pending_revenge = False
    revenge_deadline_i = 0

    for i in range(180, len(kl4h)):
        candle = kl4h[i]
        jour_str = candle["ts"][:10]
        regime = regime_1d.get(jour_str, "NEUTRE")
        s4h = sigmas4h[i] or 0.01

        # Scout
        if pos_scout:
            held = i - pos_scout["i"]
            stop_px = pos_scout["entree"] * (1.0 - STOP_LOSS_BETA_BPS)
            sl_hit = (candle["l"] <= stop_px)
            if sl_hit:
                brut = (stop_px - pos_scout["entree"]) / pos_scout["entree"] * NOTIONNEL_SCOUT
                trades_scout.append({"net": brut - FRAIS_SCOUT_AR, "brut": brut, "frais": FRAIS_SCOUT_AR})
                pos_scout = None
                pending_revenge = True
                revenge_deadline_i = i + 1
            elif held >= 18:
                brut = (candle["o"] - pos_scout["entree"]) / pos_scout["entree"] * NOTIONNEL_SCOUT
                trades_scout.append({"net": brut - FRAIS_SCOUT_AR, "brut": brut, "frais": FRAIS_SCOUT_AR})
                pos_scout = None
            else:
                pos_scout["mfp"] = max(pos_scout["mfp"], candle["h"])
                arm_px = pos_scout["entree"] * (1.0 + 1.2 * s4h)
                if pos_scout["mfp"] >= arm_px:
                    gb = pos_scout["mfp"] - 0.3 * s4h * pos_scout["entree"]
                    if candle["l"] <= gb:
                        brut = (gb - pos_scout["entree"]) / pos_scout["entree"] * NOTIONNEL_SCOUT
                        trades_scout.append({"net": brut - FRAIS_SCOUT_AR, "brut": brut, "frais": FRAIS_SCOUT_AR})
                        pos_scout = None

        # Hunter
        if pos_hunter:
            held = i - pos_hunter["i"]
            pos_hunter["mfp"] = max(pos_hunter["mfp"], candle["h"])
            arm_px = pos_hunter["entree"] * (1.0 + 1.5 * s4h)
            if held >= 18:
                brut = (candle["o"] - pos_hunter["entree"]) / pos_hunter["entree"] * NOTIONNEL_HUNTER
                trades_hunter.append({"net": brut - FRAIS_HUNTER_AR, "brut": brut, "frais": FRAIS_HUNTER_AR})
                pos_hunter = None
            elif pos_hunter["mfp"] >= arm_px:
                gb = pos_hunter["mfp"] - 0.3 * s4h * pos_hunter["entree"]
                if candle["l"] <= gb:
                    brut = (gb - pos_hunter["entree"]) / pos_hunter["entree"] * NOTIONNEL_HUNTER
                    trades_hunter.append({"net": brut - FRAIS_HUNTER_AR, "brut": brut, "frais": FRAIS_HUNTER_AR})
                    pos_hunter = None

        # Entry Hunter
        if pending_revenge and i == revenge_deadline_i and pos_hunter is None:
            pos_hunter = {"dir": 1, "ts": candle["ts"], "i": i, "entree": candle["o"], "mfp": candle["o"]}
            pending_revenge = False

        # Entry Scout
        if pos_scout is None and pos_hunter is None and not pending_revenge:
            prec_f = [r for t, r in fund if t <= candle["ts"]]
            last_f = prec_f[-1] if prec_f else None
            avg30_f = statistics.mean(prec_f[-90:]) if len(prec_f) >= 10 else None
            c1_funding = (avg30_f is not None and avg30_f > 0)
            chg4h = (candle["c"] - kl4h[i-1]["c"]) / kl4h[i-1]["c"] * 100.0
            
            if regime != "BAISSIER" and chg4h <= seuil_chute and c1_funding:
                pos_scout = {"dir": 1, "ts": candle["ts"], "i": i, "entree": candle["o"], "mfp": candle["o"]}

    all_t = trades_scout + trades_hunter
    n = len(all_t)
    brut = sum(t["brut"] for t in all_t)
    frais = sum(t["frais"] for t in all_t)
    net = sum(t["net"] for t in all_t)
    wins = sum(1 for t in all_t if t["net"] > 0)
    wr = round(wins / n * 100, 1) if n else 0.0
    return {"seuil": seuil_chute, "n": n, "brut": round(brut, 2), "frais": round(frais, 2), "net": round(net, 2), "wr": wr}

if __name__ == "__main__":
    print("┌────────────────┬────────┬───────────┬───────────┬───────────┬─────────┐")
    print("│ Seuil Panique  │ Trades │ PnL Brut  │ Frais     │ PnL Net   │ WinRate │")
    print("├────────────────┼────────┼───────────┼───────────┼───────────┼─────────┤")
    for s in [-0.3, -0.5, -0.7, -0.9, -1.1]:
        r = simulate_seuil(s)
        print(f"│ Chute <= {s:+.1f}%  │ {r['n']:<6} │ {r['brut']:<9.2f}│ {r['frais']:<10.2f}│ {r['net']:<10.2f}│ {r['wr']:<7.1f}%│")
    print("└────────────────┴────────┴───────────┴───────────┴───────────┴─────────┘")

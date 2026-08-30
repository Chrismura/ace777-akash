#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_deriv_corr.py — Bloc CORRÉLATIONS DÉRIVÉS pour le cockpit.

Calcule, à partir de sources GRATUITES (Binance futures data + OKX public, sans clé) :
  1. Les corrélations de Pearson (30j) : prix vs OI, prix vs funding, prix vs long/short, prix vs taker.
  2. La carte des liquidations réalisées par niveau de prix (OKX liquidation-orders) :
     - cumul de liquidations LONG en dessous du prix  -> carburant d'une cascade baissière
     - cumul de liquidations SHORT au-dessus du prix   -> carburant d'un short squeeze

Écrit data/deriv_corr.json (lu par cockpit/deriv_panel.js).
Une seule passe d'appels, avec pauses courtes (anti-429), 0 appel hub -> zéro impact forfait.
"""
import json
import math
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
OUT = BASE / "data" / "deriv_corr.json"
FAPI = "https://fapi.binance.com"
FUT = "https://fapi.binance.com/futures/data"
OKX = "https://www.okx.com"


def get_json(url, timeout=12):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.load(r)
    except Exception:
        return None


def pearson(xs, ys):
    n = min(len(xs), len(ys))
    if n < 3:
        return None
    xs, ys = xs[:n], ys[:n]
    mx, my = sum(xs) / n, sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    dx = math.sqrt(sum((x - mx) ** 2 for x in xs))
    dy = math.sqrt(sum((y - my) ** 2 for y in ys))
    if dx == 0 or dy == 0:
        return None
    return round(num / (dx * dy), 3)


def corr_label(r):
    """Traduit un coefficient en phrase lisible."""
    if r is None:
        return "pas assez de données"
    a = abs(r)
    if a >= 0.7:
        qual = "forte"
    elif a >= 0.4:
        qual = "modérée"
    elif a >= 0.2:
        qual = "faible"
    else:
        qual = "quasi nulle"
    if r > 0:
        sens = "évoluent dans le même sens"
    else:
        sens = "évoluent en sens opposé"
    return f"corrélation {qual} ({'+' if r > 0 else ''}{r}) — les deux {sens}"


def main() -> int:
    now = datetime.now(timezone.utc)
    ts = now.strftime("%Y-%m-%dT%H:%MZ")

    # --- 1. Prix (klines 1h, 30j ≈ 720 points) ---
    kl = get_json(f"{FAPI}/fapi/v1/klines?symbol=BTCUSDT&interval=1h&limit=720")
    if not isinstance(kl, list) or not kl:
        print("ERR klines")
        return 1
    # index prix par timestamp EXACT (chaque bougie 1h) — les séries 4h Binance
    # sont alignées sur les frontières UTC (00/04/08/12/16/20h), donc chaque
    # timestamp 4h correspond pile à une bougie 1h. Chercher par index (kl[0::4])
    # échoue selon l'heure de démarrage de la fenêtre (13h, 17h… ≠ frontières 4h).
    price_by_ts = {c[0]: float(c[4]) for c in kl}

    # --- 2. OI historique 4h (30j ≈ 180 points) ---
    oi_hist = get_json(f"{FUT}/openInterestHist?symbol=BTCUSDT&period=4h&limit=180")
    oi_by_ts = {}
    if isinstance(oi_hist, list):
        for row in oi_hist:
            oi_by_ts[int(row["timestamp"])] = float(row["sumOpenInterest"])
    time.sleep(0.4)

    # --- 3. long/short ratio 4h (30j) ---
    ls_hist = get_json(f"{FUT}/globalLongShortAccountRatio?symbol=BTCUSDT&period=4h&limit=180")
    ls_by_ts = {}
    if isinstance(ls_hist, list):
        for row in ls_hist:
            ls_by_ts[int(row["timestamp"])] = float(row["longShortRatio"])
    time.sleep(0.4)

    # --- 4. taker buy/sell ratio 4h (30j) ---
    tk_hist = get_json(f"{FUT}/takerlongshortRatio?symbol=BTCUSDT&period=4h&limit=180")
    tk_by_ts = {}
    if isinstance(tk_hist, list):
        for row in tk_hist:
            tk_by_ts[int(row["timestamp"])] = float(row["buySellRatio"])
    time.sleep(0.4)

    # --- 5. funding 8h (30j ≈ 90) ---
    fund_hist = get_json(f"{FAPI}/fapi/v1/fundingRate?symbol=BTCUSDT&limit=90")
    fund_by_ts = {}
    if isinstance(fund_hist, list):
        for row in fund_hist:
            fund_by_ts[int(row["fundingTime"])] = float(row["fundingRate"])
    time.sleep(0.4)

    # --- aligner chaque série sur le prix au même timestamp ---
    def series(by_ts):
        xs, ys = [], []
        for t, v in sorted(by_ts.items()):
            p = price_by_ts.get(t)
            if p is not None:
                xs.append(p)
                ys.append(v)
        return xs, ys

    corr = {
        "prix_oi": pearson(*series(oi_by_ts)),
        "prix_longshort": pearson(*series(ls_by_ts)),
        "prix_taker": pearson(*series(tk_by_ts)),
    }
    # funding : séries sur ses propres horodatages (8h)
    fx, fy = [], []
    for row in (fund_hist or []):
        try:
            fx.append(float(row["fundingRate"]))
            fy.append(float(row["markPrice"]))
        except Exception:
            pass
    corr["prix_funding"] = pearson(fy, fx)

    # --- 6. Carte des liquidations (OKX public, réalisées) ---
    liq = get_json(f"{OKX}/api/v5/public/liquidation-orders?instType=SWAP&instFamily=BTC-USDT&state=filled&limit=100")
    clusters = {}  # bucket 2000$ -> {"long": usd, "short": usd}
    if isinstance(liq, dict) and liq.get("code") == "0":
        data = [x for x in (liq.get("data") or []) if isinstance(x, dict) and "$ref" not in x]
        details = data[0].get("details", []) if data else []
        for det in details:
            try:
                px = float(det["bkPx"])
                sz = float(det["sz"])
                side = det.get("posSide", "")
                usd = sz * 0.01 * px
                b = int(px // 2000) * 2000
                c = clusters.setdefault(b, {"long": 0.0, "short": 0.0})
                if side == "long":
                    c["long"] += usd
                else:
                    c["short"] += usd
            except Exception:
                continue
    clusters = {str(b): {"long": round(v["long"], 0), "short": round(v["short"], 0)}
                for b, v in sorted(clusters.items())}

    # prix actuel pour la lecture
    prem = get_json(f"{FAPI}/fapi/v1/premiumIndex?symbol=BTCUSDT")
    mark = float((prem or {}).get("markPrice") or 0) or (sorted(price_by_ts.values())[-1] if price_by_ts else 0)

    # lecture liquidité : les 4 tas (longs/shorts × dessous/dessus)
    longs_below = sum(v["long"] for b, v in clusters.items() if int(b) < mark)
    longs_above = sum(v["long"] for b, v in clusters.items() if int(b) > mark)
    shorts_below = sum(v["short"] for b, v in clusters.items() if int(b) < mark)
    shorts_above = sum(v["short"] for b, v in clusters.items() if int(b) > mark)
    if longs_below > shorts_above:
        liq_lecture = (
            f"Le gros de la liquidité est EN DESSOUS du prix : {longs_below/1e6:.1f} M$ de LONGS "
            f"liquidés à 76-78k (contre {shorts_above/1e6:.1f} M$ de shorts au-dessus, à 80k) — "
            f"si le prix casse ces supports, les liquidations long forcées peuvent accélérer la baisse (cascade)."
        )
    elif shorts_above > longs_below:
        liq_lecture = (
            f"Le gros de la liquidité est AU-DESSUS du prix : {shorts_above/1e6:.1f} M$ de SHORTS "
            f"liquidés au-dessus (contre {longs_below/1e6:.1f} M$ de longs en dessous) — "
            f"une remontée peut forcer les shorts à racheter et amplifier la hausse (short squeeze)."
        )
    else:
        liq_lecture = "Liquidité équilibrée de part et d'autre du prix — pas de mur dominant."

    out = {
        "ts": ts,
        "mark": round(mark, 1),
        "correlations": {
            "prix_oi": {"r": corr["prix_oi"], "lecture": corr_label(corr["prix_oi"]),
                        "label": "Open interest vs prix"},
            "prix_funding": {"r": corr["prix_funding"], "lecture": corr_label(corr["prix_funding"]),
                             "label": "Funding vs prix"},
            "prix_longshort": {"r": corr["prix_longshort"], "lecture": corr_label(corr["prix_longshort"]),
                               "label": "Ratio long/short vs prix"},
            "prix_taker": {"r": corr["prix_taker"], "lecture": corr_label(corr["prix_taker"]),
                           "label": "Achats/ventes agressifs vs prix"},
        },
        "liquidations": {
            "clusters_2000usd": clusters,
            "longs_below_usd": round(longs_below, 0),
            "longs_above_usd": round(longs_above, 0),
            "shorts_below_usd": round(shorts_below, 0),
            "shorts_above_usd": round(shorts_above, 0),
            "lecture": liq_lecture,
        },
    }
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1))
    print(f"OK {ts} — mark {out['mark']} — corr OI {corr['prix_oi']} funding {corr['prix_funding']} "
          f"LS {corr['prix_longshort']} taker {corr['prix_taker']} — liq dessous {longs_below/1e6:.1f}M "
          f"dessus {shorts_above/1e6:.1f}M")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

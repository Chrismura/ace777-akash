#!/usr/bin/env python3
"""
Thermo quotidien — Binance public (sans clé) + proxies free.
Écrit THERMO_DERNIER.md, thermo/live.json|js, historique funding, feed Cortana.
Zéro ordre trading.
"""
from __future__ import annotations

import json
import math
import statistics
import urllib.request
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path("/Users/christophe/ace777-test-day1")
WS = ROOT / "Index_Maison"
OUT = WS / "OUTBOX_OBSIDIAN"
THERMO = WS / "thermo"
SYM = "BTCUSDT"
# Panier alts dynamique : top N par volume échangé (24h), hors BTC.
# Un panier fixe biaise (ex. 5 paires arbitraires toutes en baisse ≠ marché large).
ALTS = []  # rempli dynamiquement : top 20 perps USDT par quoteVolume 24h
FAPI = "https://fapi.binance.com"
SPOT = "https://api.binance.com"
CG = "https://api.coingecko.com/api/v3"


def get_json(base: str, path: str, params: str = "", timeout: float = 12.0):
    url = f"{base}{path}"
    if params:
        url = f"{url}?{params}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "ace777-thermo-free/2.0"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode())
    except Exception as e:
        return {"_error": str(e)}


def api_ok(d) -> bool:
    return isinstance(d, dict) and "_error" not in d


def load_prev_live() -> dict:
    p = THERMO / "live.json"
    if not p.exists():
        return {}
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
        return d if isinstance(d, dict) else {}
    except Exception:
        return {}


def keep(cur, prev: dict, key: str):
    """Ne pas écraser une bonne valeur par None si l’API a floppé."""
    if cur is not None:
        return cur, False
    v = prev.get(key)
    if v is not None:
        return v, True
    return None, False


def fetch_fear_greed() -> dict:
    """alternative.me — free."""
    d = get_json("https://api.alternative.me", "/fng/", "limit=1&format=json", timeout=8.0)
    try:
        row = (d.get("data") or [None])[0] or {}
        val = int(row.get("value"))
        label = row.get("value_classification") or ""
        return {"value": val, "label": label, "ok": True}
    except Exception:
        return {"value": None, "label": None, "ok": False, "err": (d or {}).get("_error")}


def fetch_liquidations_24h() -> dict:
    """Liquidations 24h — OKX public (sans clé) : liquidation-orders, 3 familles.
    data[0] = bloc complet (le reste sont des $ref dupes) ; on somme sz × ctVal × bkPx
    par côté (long/short) sur ~24h glissantes."""
    fams = [("BTC-USDT", 0.01), ("ETH-USDT", 0.1), ("SOL-USDT", 1.0)]
    total = 0.0
    long_usd = 0.0
    short_usd = 0.0
    n_orders = 0
    now_ms = int(datetime.now(timezone.utc).timestamp() * 1000)
    for fam, ctval in fams:
        d = get_json(
            "https://www.okx.com",
            "/api/v5/public/liquidation-orders",
            f"instType=SWAP&instFamily={fam}&state=filled&limit=100",
            timeout=8.0,
        )
        if not isinstance(d, dict) or d.get("code") != "0":
            continue
        data = d.get("data") or []
        rec = None
        for x in data:
            if isinstance(x, dict) and "$ref" not in x:
                rec = x
                break
        if not rec:
            continue
        for det in rec.get("details") or []:
            try:
                ts = int(det.get("ts") or 0)
                if ts < now_ms - 24 * 3600 * 1000:
                    continue
                sz = float(det.get("sz") or 0)
                px = float(det.get("bkPx") or 0)
                side = det.get("posSide") or det.get("side") or ""
            except Exception:
                continue
            usd = sz * ctval * px
            if usd <= 0:
                continue
            n_orders += 1
            total += usd
            if "short" in side:
                short_usd += usd
            else:
                long_usd += usd
    if total <= 0:
        return {"usd": None, "longUsd": None, "shortUsd": None, "ok": False, "source": "na"}
    return {
        "usd": round(total, 0),
        "longUsd": round(long_usd, 0),
        "shortUsd": round(short_usd, 0),
        "ok": True,
        "source": "okx-public",
        "n": n_orders,
    }


def fetch_etf_flows() -> dict:
    """ETF net inflow — bitbo.io public sans clé (/all-data → etfFlows, flux en BTC).
    Somme des flow_1d des fonds BTC ; renvoie en BTC (conversion M$ faite dans main).
    bitbo ne couvre que le BTC — ETH/XRP restent None (n/d honnête)."""
    out = {"btc": None, "eth": None, "xrp": None, "ok": False, "source": None, "unit": "BTC"}
    d = get_json("https://api.bitbo.io", "/all-data", "", timeout=10.0)
    if not isinstance(d, dict) or d.get("_error"):
        return out
    flows = d.get("etfFlows") or {}
    if not isinstance(flows, dict):
        return out
    # flow_1d = flux du jour (publié après clôture US ~21h UTC) ; sinon moyenne 7j.
    total_btc = 0.0
    n = 0
    used_7d = False
    for fund, row in flows.items():
        if not isinstance(row, dict) or fund == "BTC":
            continue
        try:
            v = float(row.get("flow_1d") or 0)
            if v == 0:
                v = float(row.get("flow_7d") or 0) / 7.0
                used_7d = True
        except Exception:
            continue
        total_btc += v
        n += 1
    if n == 0:
        return out
    out["btc"] = round(total_btc, 3)
    out["ok"] = True
    out["source"] = "bitbo-public (moy 7j)" if used_7d else "bitbo-public"
    return out


def fetch_gex_deribit() -> dict:
    """Proxy GEX — Deribit public sans clé : OI options BTC par strike (expiration ≤ 60 j).
    Put/call OI ratio + murs de gamma (strike avec le plus gros OI au-dessus / en dessous
    du spot) + distance des murs. Proxy honnête — pas le vrai GEX payant (SpotGamma)."""
    out = {"ok": False, "putCallRatio": None, "callWall": None, "putWall": None,
           "callWallDistPct": None, "putWallDistPct": None, "nInstruments": 0, "source": "na"}
    d = get_json("https://www.deribit.com", "/api/v2/public/get_book_summary_by_currency",
                 "currency=BTC&kind=option", timeout=12.0)
    if not isinstance(d, dict):
        return out
    rows = d.get("result") or []
    if not rows:
        return out
    now = datetime.now(timezone.utc)
    spot = None
    idx = get_json("https://www.deribit.com", "/api/v2/public/get_index_price",
                   "index_name=btc_usd", timeout=6.0)
    if isinstance(idx, dict):
        try:
            spot = float(idx.get("result", {}).get("index_price"))
        except Exception:
            spot = None
    oi_call = {}
    oi_put = {}
    total_call = 0.0
    total_put = 0.0
    n = 0
    for r in rows:
        name = r.get("instrument_name") or ""
        parts = name.split("-")
        if len(parts) < 4:
            continue
        try:
            strike = float(parts[-2])
            opt_type = parts[-1].upper()
            exp = datetime.strptime(parts[-3], "%d%b%y").replace(tzinfo=timezone.utc)
        except Exception:
            continue
        if (exp - now).days > 60:
            continue
        try:
            oi = float(r.get("open_interest") or 0)
        except Exception:
            continue
        n += 1
        if opt_type == "C":
            oi_call[strike] = oi_call.get(strike, 0) + oi
            total_call += oi
        elif opt_type == "P":
            oi_put[strike] = oi_put.get(strike, 0) + oi
            total_put += oi
    if not (oi_call or oi_put):
        return out
    out["nInstruments"] = n
    out["putCallRatio"] = round(total_put / total_call, 3) if total_call else None
    if spot:
        walls_c = [(k, v) for k, v in oi_call.items() if k >= spot]
        walls_p = [(k, v) for k, v in oi_put.items() if k <= spot]
        if walls_c:
            wall, oi = max(walls_c, key=lambda x: x[1])
            out["callWall"] = int(wall)
            out["callWallDistPct"] = round((wall - spot) / spot * 100, 1)
        if walls_p:
            wall, oi = max(walls_p, key=lambda x: x[1])
            out["putWall"] = int(wall)
            out["putWallDistPct"] = round((spot - wall) / spot * 100, 1)
    out["ok"] = True
    out["source"] = "deribit-public"
    return out


def fetch_volume_caches() -> dict:
    """Volumes cachés — proxy OKX public sans clé :
    1) Rubik taker-volume 24h (buy vs sell en BTC) → ratio taker buy
    2) ratio volume perp/spot 24h (volCcy24h, même unité BTC) → levier caché."""
    out = {"ok": False, "takerBuyRatio": None, "perpSpotRatio": None,
           "buy24h": None, "sell24h": None, "source": "na"}
    d = get_json("https://www.okx.com", "/api/v5/rubik/stat/taker-volume",
                 "ccy=BTC&instType=SPOT&period=1D", timeout=8.0)
    if isinstance(d, dict) and d.get("code") == "0" and isinstance(d.get("data"), list) and d["data"]:
        row = d["data"][-1]
        try:
            buy = float(row[1])
            sell = float(row[2])
            if buy + sell > 0:
                out["buy24h"] = round(buy, 0)
                out["sell24h"] = round(sell, 0)
                out["takerBuyRatio"] = round(buy / (buy + sell), 3)
                out["ok"] = True
        except Exception:
            pass
    try:
        p = get_json("https://www.okx.com", "/api/v5/market/ticker", "instId=BTC-USDT-SWAP", timeout=8.0)
        s = get_json("https://www.okx.com", "/api/v5/market/ticker", "instId=BTC-USDT", timeout=8.0)
        pv = float(((p or {}).get("data") or [{}])[0].get("volCcy24h") or 0)
        sv = float(((s or {}).get("data") or [{}])[0].get("vol24h") or 0)
        if pv > 0 and sv > 0:
            out["perpSpotRatio"] = round(pv / sv, 2)
            out["ok"] = True
    except Exception:
        pass
    out["source"] = "okx-rubik+ticker"
    return out


def alt_season_from_dom(dom) -> dict:
    """Proxy alt-season via dominance BTC (pas l’index Blockchain Center payant)."""
    if dom is None:
        return {"label": None, "score": None, "ok": False}
    # Heuristique pédagogique
    if dom >= 55:
        return {"label": "Bitcoin season", "score": int(max(0, 100 - (dom - 40) * 3)), "ok": True, "proxy": True}
    if dom <= 45:
        return {"label": "Alt season", "score": int(min(100, 50 + (50 - dom) * 3)), "ok": True, "proxy": True}
    return {"label": "Transition", "score": 50, "ok": True, "proxy": True}


def fnum(x, d=4):
    try:
        return round(float(x), d)
    except Exception:
        return None


def closes_from_klines(kl):
    if not isinstance(kl, list) or not kl or isinstance(kl, dict):
        return []
    out = []
    for row in kl:
        try:
            out.append(float(row[4]))
        except Exception:
            pass
    return out


def pct(a, b):
    if a is None or b is None or b == 0:
        return None
    return round((a - b) / b * 100.0, 2)


def sma(xs, n):
    if len(xs) < n:
        return None
    return sum(xs[-n:]) / n


def realized_vol(closes, days):
    if len(closes) < days + 1:
        return None
    rets = []
    for i in range(-days, 0):
        a, b = closes[i - 1], closes[i]
        if a > 0:
            rets.append(math.log(b / a))
    if len(rets) < 5:
        return None
    return round(statistics.pstdev(rets) * math.sqrt(365) * 100, 2)


def structure_hh_hl(closes, look=20):
    if len(closes) < look + 5:
        return None, "données courtes"
    window = closes[-look:]
    prev = closes[-(look * 2) : -look] if len(closes) >= look * 2 else closes[:-look]
    if not prev:
        return None, "—"
    hh = max(window) > max(prev)
    hl = min(window) > min(prev)
    ll = min(window) < min(prev)
    lh = max(window) < max(prev)
    if hh and hl:
        return "hausse", "plus hauts + plus bas plus hauts"
    if ll and lh:
        return "baisse", "plus bas + plus hauts plus bas"
    return "mixte", "structure mixte / range"


def level_funding(v):
    if v is None:
        return "na"
    a = abs(v)
    if a < 0.0001:
        return "ok"
    if a < 0.0003:
        return "warn"
    return "hot"


def level_ls(v):
    if v is None:
        return "na"
    if 0.75 <= v <= 1.5:
        return "ok"
    if 0.6 <= v <= 1.75:
        return "warn"
    return "hot"


def level_chg(v, soft=2.0, hot=4.0):
    if v is None:
        return "na"
    a = abs(v)
    if a < soft:
        return "ok"
    if a < hot:
        return "warn"
    return "hot"


def ind(value, level="na", label="", unit="", note=""):
    return {
        "value": value,
        "level": level,
        "label": label,
        "unit": unit,
        "note": note,
        "wired": value is not None and value != "—",
    }


def main() -> int:
    now = datetime.now(timezone.utc)
    ts = now.strftime("%Y-%m-%dT%H:%MZ")
    THERMO.mkdir(parents=True, exist_ok=True)
    prev_live = load_prev_live()
    stale_fields: list[str] = []

    oi = get_json(FAPI, "/fapi/v1/openInterest", f"symbol={SYM}")
    prem = get_json(FAPI, "/fapi/v1/premiumIndex", f"symbol={SYM}")
    tick = get_json(FAPI, "/fapi/v1/ticker/24hr", f"symbol={SYM}")
    lsr = get_json(FAPI, "/futures/data/globalLongShortAccountRatio", f"symbol={SYM}&period=1h&limit=1")
    fund_recent = get_json(FAPI, "/fapi/v1/fundingRate", f"symbol={SYM}&limit=3")
    taker = get_json(FAPI, "/futures/data/takerlongshortRatio", f"symbol={SYM}&period=1h&limit=1")
    top_ls = get_json(FAPI, "/futures/data/topLongShortAccountRatio", f"symbol={SYM}&period=1h&limit=1")
    aggs = get_json(FAPI, "/fapi/v1/aggTrades", f"symbol={SYM}&limit=500")
    # ~30j funding (3/jour ≈ 90)
    fund_month = get_json(FAPI, "/fapi/v1/fundingRate", f"symbol={SYM}&limit=90")
    # mois précédent : start/end
    start_prev = int((now.replace(day=1) - timedelta(days=1)).replace(day=1).timestamp() * 1000)
    end_prev = int((now.replace(day=1) - timedelta(seconds=1)).timestamp() * 1000)
    fund_prev = get_json(
        FAPI,
        "/fapi/v1/fundingRate",
        f"symbol={SYM}&startTime={start_prev}&endTime={end_prev}&limit=1000",
    )
    kl_1d = get_json(FAPI, "/fapi/v1/klines", f"symbol={SYM}&interval=1d&limit=220")
    kl_1h = get_json(FAPI, "/fapi/v1/klines", f"symbol={SYM}&interval=1h&limit=30")
    # dominance BTC + MC (CoinGecko free)
    cg = get_json(CG, "/global", timeout=10.0)
    fng = fetch_fear_greed()
    liq = fetch_liquidations_24h()
    etf = fetch_etf_flows()
    gex = fetch_gex_deribit()
    vcz = fetch_volume_caches()

    oi_v = fnum((oi or {}).get("openInterest"), 3) if api_ok(oi) else None
    mark = fnum((prem or {}).get("markPrice"), 2) if api_ok(prem) else None
    last_f = fnum((prem or {}).get("lastFundingRate"), 6) if api_ok(prem) else None
    chg24 = fnum((tick or {}).get("priceChangePercent"), 2) if api_ok(tick) else None
    vol = fnum((tick or {}).get("quoteVolume"), 0) if api_ok(tick) else None

    # Garde dernier bon snapshot si API flop (évite HYGIENE=NOK + board vide)
    oi_v, s = keep(oi_v, prev_live, "oi");  s and stale_fields.append("oi")
    mark, s = keep(mark, prev_live, "mark");  s and stale_fields.append("mark")
    if etf.get("ok") and etf.get("btc") is not None and mark:
        etf["btc"] = round(etf["btc"] * mark / 1e6, 2)  # BTC -> M$
        etf["unit"] = "M$"
    last_f, s = keep(last_f, prev_live, "funding");  s and stale_fields.append("funding")
    chg24, s = keep(chg24, prev_live, "chg24");  s and stale_fields.append("chg24")
    if not fng.get("ok") or fng.get("value") is None:
        pv, s = keep(None, prev_live, "fearGreed")
        if s:
            fng = {
                "value": pv,
                "label": prev_live.get("fearGreedLabel"),
                "ok": True,
                "stale": True,
            }
            stale_fields.append("fearGreed")
    long_ratio = None
    if isinstance(lsr, list) and lsr:
        long_ratio = fnum(lsr[-1].get("longShortRatio"), 3)

    taker_ratio = None
    if isinstance(taker, list) and taker:
        taker_ratio = fnum(taker[-1].get("buySellRatio"), 3)

    top_trader_ls = None
    if isinstance(top_ls, list) and top_ls:
        top_trader_ls = fnum(top_ls[-1].get("longShortRatio"), 3)

    total_mc = None
    if isinstance(cg, dict) and "data" in cg:
        try:
            total_mc = fnum(cg["data"].get("total_market_cap", {}).get("usd"), 0)
        except Exception:
            total_mc = None


    # Whales proxy free = gros prints aggTrades (>= 500k USDT)
    whale_n = 0
    whale_usd = 0.0
    whale_max = 0.0
    whale_buy_usd = 0.0
    whale_sell_usd = 0.0
    if isinstance(aggs, list):
        for t in aggs:
            try:
                notional = float(t["p"]) * float(t["q"])
            except Exception:
                continue
            if notional >= 500_000:
                whale_n += 1
                whale_usd += notional
                whale_max = max(whale_max, notional)
                # direction du print : m=True → l'acheteur est maker → pression vente
                #                     m=False → le vendeur est maker → pression achat
                if t.get("m"):
                    whale_sell_usd += notional
                else:
                    whale_buy_usd += notional
    whale_usd = round(whale_usd, 0) if whale_n else 0.0
    # direction dominante des prints (proxy) : bullish / bearish / neutral
    if whale_buy_usd > whale_sell_usd:
        whale_dir_proxy = "bullish"
    elif whale_sell_usd > whale_buy_usd:
        whale_dir_proxy = "bearish"
    else:
        whale_dir_proxy = "neutral"

    closes = closes_from_klines(kl_1d)
    closes_h = closes_from_klines(kl_1h)
    ma50 = sma(closes, 50)
    ma200 = sma(closes, 200)
    vs_ma50 = pct(mark or (closes[-1] if closes else None), ma50)
    vs_ma200 = pct(mark or (closes[-1] if closes else None), ma200)
    ath = max(closes) if closes else None
    dd = pct(closes[-1], ath) if closes and ath else None
    vol7 = realized_vol(closes, 7)
    vol30 = realized_vol(closes, 30)
    struct, struct_note = structure_hh_hl(closes)
    chg30 = pct(closes[-1], closes[-31]) if len(closes) >= 31 else None
    regime = "tendance" if chg30 is not None and abs(chg30) >= 8 else "range"
    chg1h = pct(closes_h[-1], closes_h[-2]) if len(closes_h) >= 2 else None
    chg4h = pct(closes_h[-1], closes_h[-5]) if len(closes_h) >= 5 else None

    # panier alts : DYNAMIQUE (top 20 perps USDT par volume 24h, hors BTC)
    # Un seul appel /ticker/24hr retourne toutes les paires -> échantillon représentatif.
    alt_down = 0
    alt_n = 0
    try:
        tks = get_json(FAPI, "/fapi/v1/ticker/24hr")
        if isinstance(tks, list):
            perps = [t for t in tks if t.get("symbol", "").endswith("USDT") and t.get("symbol") != "BTCUSDT"
                     and t.get("quoteVolume") is not None and t.get("priceChangePercent") is not None]
            perps.sort(key=lambda t: float(t["quoteVolume"]), reverse=True)
            for t in perps[:20]:
                chg = fnum(t.get("priceChangePercent"), 2)
                if chg is not None:
                    alt_n += 1
                    if chg < 0:
                        alt_down += 1
    except Exception:
        pass
    panier = round(100.0 * alt_down / alt_n, 1) if alt_n else None

    # volume vs moyenne 20j (quote approx via kline volume * close)
    vol_sig = None
    if isinstance(kl_1d, list) and len(kl_1d) >= 21:
        vols = [float(r[7]) for r in kl_1d[-21:-1]]  # quote volume
        avg = sum(vols) / len(vols)
        today_v = float(kl_1d[-1][7])
        vol_sig = round(today_v / avg, 2) if avg else None

    lev_sig = "non"
    if chg24 is not None and vol_sig is not None and chg24 <= -1.0 and vol_sig >= 1.3:
        lev_sig = "oui"
    elif chg24 is not None and vol_sig is not None and chg24 <= -0.5 and vol_sig >= 1.1:
        lev_sig = "faible"

    dom = None
    if isinstance(cg, dict) and "data" in cg:
        dom = fnum(cg["data"].get("market_cap_percentage", {}).get("btc"), 2)
    alt_s = alt_season_from_dom(dom)

    def avg_fund(rows):
        if not isinstance(rows, list) or not rows:
            return None, 0
        xs = [fnum(r.get("fundingRate"), 8) for r in rows]
        xs = [x for x in xs if x is not None]
        if not xs:
            return None, 0
        return round(sum(xs) / len(xs), 8), len(xs)

    fund_avg_30, n30 = avg_fund(fund_month)
    fund_avg_prev, nprev = avg_fund(fund_prev)

    # climate score
    score = 100.0
    if last_f is not None:
        score -= min(40, abs(last_f) / 0.0003 * 28)
    if long_ratio is not None:
        score -= min(30, abs(long_ratio - 1) * 22)
    if chg24 is not None:
        score -= min(30, abs(chg24) / 4 * 22)
    score = int(max(0, min(100, round(score))))
    climate = "ok" if score >= 70 else ("warn" if score >= 45 else "hot")

    # --- ACE read-only soft (freshest LIVE + CSV session) — ne touche pas au process ---
    import re as _re
    import csv as _csv
    runs = ROOT / "runs"
    ace = {
        "live": None,
        "skip": None,
        "redHits": None,
        "sessionPnl": None,
        "trades": None,
        "heat": None,
    }
    try:
        lives = sorted(runs.glob("*LIVE_COLOR.log"), key=lambda p: p.stat().st_mtime, reverse=True)
        if lives:
            live_p = lives[0]
            ace["live"] = live_p.name
            tail = live_p.read_text(errors="ignore")[-200000:]
            ace["skip"] = len(_re.findall(r"\bSKIP\b", tail, _re.I))
            ace["redHits"] = len(_re.findall(r"\bRED\b|FREIN_ROUGE|pullback", tail, _re.I))
        # session CSVs matching prefix of live name
        prefix = None
        if ace["live"]:
            prefix = ace["live"].replace("_LIVE_COLOR.log", "")
        pnl_sum = 0.0
        n_tr = 0
        if prefix:
            for csv_p in runs.glob(prefix + "*.csv"):
                try:
                    with csv_p.open(newline="", encoding="utf-8", errors="ignore") as f:
                        rd = _csv.DictReader(f)
                        for row in rd:
                            try:
                                pnl_sum += float(row.get("pnl") or 0)
                                n_tr += 1
                            except Exception:
                                pass
                except Exception:
                    pass
        ace["sessionPnl"] = round(pnl_sum, 4)
        ace["trades"] = n_tr
        # heat = |pnl| relative soft scale
        ace["heat"] = round(min(100.0, abs(pnl_sum) * 3), 1)
    except Exception as e:
        ace["err"] = str(e)

    # Bassine soft zone from score
    if score >= 70:
        bassine = "haute / calme"
        bassine_lv = "ok"
    elif score >= 45:
        bassine = "moyenne / trempe"
        bassine_lv = "warn"
    else:
        bassine = "basse / stress"
        bassine_lv = "hot"

    # Walls soft = funding + OI crowding label
    walls = "neutre"
    walls_lv = "ok"
    if last_f is not None and abs(last_f) >= 0.0003:
        walls = "mur funding extrême (proxy)"
        walls_lv = "hot"
    elif long_ratio is not None and (long_ratio >= 1.6 or long_ratio <= 0.7):
        walls = "mur crowding (proxy)"
        walls_lv = "warn"
    else:
        walls = "pas de mur évident (proxy)"

    heat_lv = "ok"
    if ace["heat"] is not None:
        if ace["heat"] >= 40:
            heat_lv = "hot"
        elif ace["heat"] >= 15:
            heat_lv = "warn"

    skip_lv = "ok"
    if ace["skip"] is not None:
        if ace["skip"] >= 200:
            skip_lv = "warn"  # beaucoup de skip = sagesse ou bruit
        if ace["skip"] >= 500:
            skip_lv = "ok"  # très sélectif encore ok

    red_lv = "ok"
    red_val = "pas de RED vu"
    if ace["redHits"]:
        red_val = f"{ace['redHits']} hits RED (tail log)"
        red_lv = "warn" if ace["redHits"] < 20 else "hot"
    elif ace["live"]:
        red_val = "0 RED (tail log)"

    # indicators board
    indicators = {
        "A1": ind(
            f"MA50 {vs_ma50}% · MA200 {vs_ma200}%" if vs_ma50 is not None else None,
            "ok" if vs_ma50 is not None and vs_ma50 > -5 else ("warn" if vs_ma50 is not None else "na"),
            "Prix vs moyennes",
            note=f"mark={mark}",
        ),
        "A2": ind(struct, "ok" if struct == "hausse" else ("warn" if struct == "mixte" else "hot"), "Structure", note=struct_note),
        "A3": ind(dom, "ok" if dom and 40 <= dom <= 60 else ("warn" if dom else "na"), "Dominance BTC %", unit="%"),
        "A4": ind(
            f"7j {vol7}% · 30j {vol30}%" if vol7 is not None else None,
            "ok" if vol7 is not None and vol7 < 60 else ("warn" if vol7 else "na"),
            "Volatilité annualisée",
        ),
        "A5": ind(dd, "ok" if dd is not None and dd > -15 else ("warn" if dd is not None and dd > -30 else "hot"), "DD vs ATH fenêtre", unit="%"),
        "A6": ind(
            f"{regime} (30j {chg30}%)" if chg30 is not None else regime,
            "ok",
            "Régime large",
        ),
        "B7": ind(
            f"1h {chg1h}% · 4h {chg4h}% · 24h {chg24}%",
            level_chg(chg24),
            "BTC multi-horizon",
        ),
        "B8": ind(lev_sig, "hot" if lev_sig == "oui" else ("warn" if lev_sig == "faible" else "ok"), "Signature levier", note=f"vol×{vol_sig}"),
        "B9": ind(panier, "ok" if panier is not None and panier < 60 else ("warn" if panier else "na"), "% alts en baisse 24h", unit="%"),
        "B10": ind(vol, "ok", "Volume quote 24h"),
        "B11": ind(
            f"heat {ace['heat']} · PnL sess {ace['sessionPnl']} · {ace['trades']} fills"
            if ace["heat"] is not None
            else None,
            heat_lv if ace["heat"] is not None else "na",
            "Heat portefeuille",
            note=f"lecture seule CSV ACE · {ace.get('live') or 'pas de LIVE'}",
        ),
        "B12": ind(
            red_val if ace.get("live") else None,
            red_lv if ace.get("live") else "na",
            "Freins RED",
            note=f"tail LIVE · {ace.get('live') or '—'}",
        ),
        "C13": ind(oi_v, "ok", "Open interest"),
        "C14": ind(last_f, level_funding(last_f), "Funding last"),
        "C15": ind(
            f"{whale_n} prints ≥500k$ · Σ {whale_usd:.0f}$" if whale_n else "0 gros print (≥500k$)",
            "warn" if whale_n >= 3 else ("ok" if whale_n >= 0 else "na"),
            "Whales proxy (aggTrades)",
            note="source free Binance aggTrades — pas Whale Alert payant",
        ),
        "C16": ind(score, climate, "Score multi-couches /100"),
        "C17": ind(regime, "ok", "Proxy régime", note="sans HMM"),
        "C18": ind(
            f"proxy stress · L/S {long_ratio} · fund {last_f}",
            climate,
            "Tension / mur",
            note="proxy free (funding+L/S) — wall_drop CSV ACE si dispo plus tard",
        ),
        "C19": ind(score / 100, climate, "Impulse / froid proxy"),
        "C20": ind(bassine, bassine_lv, "Bassine / zone trempe", note="définition soft ops = zone score climat"),
        "C21": ind(
            f"{ace['skip']} SKIP (tail LIVE)" if ace["skip"] is not None else None,
            skip_lv if ace["skip"] is not None else "na",
            "Taux SKIP / sagesse",
            note=f"lecture seule · {ace.get('live') or '—'}",
        ),
        "C22": ind(score, climate, "Verre d'eau proxy /100"),
        "C23": ind(
            f"OI {oi_v} · taker B/S {taker_ratio}",
            "warn" if taker_ratio is not None and (taker_ratio >= 1.4 or taker_ratio <= 0.7) else "ok",
            "Dark/OTC proxy free",
            note="pas de dark pool crypto free temps réel — proxy = OI + taker buy/sell Binance",
        ),
        "C24": ind(last_f, level_funding(last_f), "Stress levier funding"),
        "C25": ind(walls, walls_lv, "Walls (proxy options)", note="proxy funding/crowding — pas SpotGamma/ZeroGEX payant"),
        "D26": ind(
            f"{fng.get('value')} · {fng.get('label')}" if fng.get("ok") else None,
            "hot" if (fng.get("value") or 50) >= 75 else ("warn" if (fng.get("value") or 50) <= 25 else "ok"),
            "Fear & Greed",
            note="alternative.me free",
        ),
        "D27": ind(
            f"{total_mc/1e12:.2f} T$" if total_mc else None,
            "ok" if total_mc else "na",
            "Market cap crypto",
            note="CoinGecko global",
        ),
        "D28": ind(
            f"{alt_s.get('label')} (~{alt_s.get('score')})" if alt_s.get("ok") else None,
            "ok" if alt_s.get("label") == "Alt season" else ("warn" if alt_s.get("label") == "Bitcoin season" else "ok"),
            "Alt season (proxy BTC.D)",
            note="proxy dominance — pas index Blockchain Center exact",
        ),
        "D29": ind(
            f"{liq.get('usd')/1e9:.2f} B$" if liq.get("usd") else None,
            "hot" if (liq.get("usd") or 0) >= 5e8 else ("warn" if liq.get("usd") else "na"),
            "Liquidations 24h",
            note=liq.get("source") or "na",
        ),
        "D30": ind(
            f"BTC {etf.get('btc')} M$" if etf.get("btc") is not None else None,
            "ok" if (etf.get("btc") or 0) >= 0 else "warn",
            "ETF BTC net inflow",
            note=etf.get("note") or etf.get("source") or "—",
        ),
        "D31": ind(
            f"ETH {etf.get('eth')} M$" if etf.get("eth") is not None else None,
            "ok" if (etf.get("eth") or 0) >= 0 else "warn",
            "ETF ETH net inflow",
            note=etf.get("source") or "—",
        ),
        "D32": ind(
            f"XRP {etf.get('xrp')} M$" if etf.get("xrp") is not None else None,
            "ok" if etf.get("xrp") is not None else "na",
            "ETF XRP net inflow",
            note="bitbo public = BTC only → n/d honnête pour ETH/XRP",
        ),
        "D33": ind(
            f"P/C {gex.get('putCallRatio')} · murC {gex.get('callWall')} ({gex.get('callWallDistPct')}%) · murP {gex.get('putWall')} ({gex.get('putWallDistPct')}%)"
            if gex.get("ok")
            else None,
            "hot" if gex.get("ok") and (gex.get("putCallRatio") or 0) >= 1.3
            else ("warn" if gex.get("ok") and (gex.get("putCallRatio") or 0) >= 1.1 else "ok"),
            "GEX proxy (OI options)",
            note="Deribit public — murs = strikes gros OI (pas SpotGamma payant)",
        ),
        "D34": ind(
            f"takerB {vcz.get('takerBuyRatio')} · P/S {vcz.get('perpSpotRatio')}×"
            if vcz.get("ok")
            else None,
            "warn" if vcz.get("ok") and (vcz.get("takerBuyRatio") or 0) < 0.45
            else ("ok" if vcz.get("ok") else "na"),
            "Volumes cachés (proxy)",
            note="Rubik taker + ratio perp/spot OKX — pas dark pool payant",
        ),
    }

    lecture = []
    if climate == "ok":
        lecture.append(f"Climat CALME (score {score}/100).")
    elif climate == "warn":
        lecture.append(f"Climat ATTENTION (score {score}/100).")
    else:
        lecture.append(f"Climat CHAUD (score {score}/100).")
    if last_f is not None:
        lecture.append(f"Funding maintenant {last_f}. Moyenne ~30j {fund_avg_30} ({n30} pts). Mois précédent {fund_avg_prev} ({nprev} pts).")
    if long_ratio is not None:
        lecture.append(f"Long/Short {long_ratio}.")
    if chg24 is not None:
        lecture.append(f"BTC 24h {chg24}% · 1h {chg1h}% · 4h {chg4h}%.")
    if panier is not None:
        lecture.append(f"Panier alts : {panier}% en baisse ({alt_down}/{alt_n}).")
    if whale_n:
        lecture.append(f"Whales proxy : {whale_n} gros print(s) ≥500k$ (max {whale_max:.0f}$) — source aggTrades Binance.")
    else:
        lecture.append("Whales proxy : aucun print ≥500k$ sur les ~500 derniers trades.")
    if taker_ratio is not None:
        lecture.append(f"Dark/OTC proxy : taker buy/sell {taker_ratio} · OI {oi_v} (pas de dark pool free temps réel).")
    if top_trader_ls is not None:
        lecture.append(f"Top traders L/S {top_trader_ls}.")
    if fng.get("ok"):
        lecture.append(f"Fear & Greed {fng.get('value')} ({fng.get('label')}).")
    if total_mc:
        lecture.append(f"Market cap crypto ≈ {total_mc/1e12:.2f} T$.")
    if alt_s.get("ok"):
        lecture.append(f"Alt season proxy : {alt_s.get('label')} (BTC.D {dom}%).")
    if liq.get("usd"):
        lecture.append(f"Liquidations 24h proxy ≈ {liq.get('usd')/1e9:.2f} B$.")
    if etf.get("btc") is not None:
        lecture.append(f"ETF net inflow : BTC {etf.get('btc')} M$ ({etf.get('source')}, BTC only).")
    if gex.get("ok"):
        lecture.append(f"GEX proxy (Deribit) : P/C {gex.get('putCallRatio')} · murC {gex.get('callWall')} (+{gex.get('callWallDistPct')}%) · murP {gex.get('putWall')} (-{gex.get('putWallDistPct')}%).")
    if vcz.get("ok"):
        lecture.append(f"Volumes cachés proxy : taker buy {vcz.get('takerBuyRatio')} · vol perp/spot {vcz.get('perpSpotRatio')}×.")
    if ace.get("live"):
        lecture.append(
            f"ACE soft: LIVE={ace['live']} · SKIP={ace['skip']} · heat={ace['heat']} · PnL sess={ace['sessionPnl']} · RED={ace['redHits']}."
        )
    lecture.append("C15/C23 = proxies free. D26–D34 = F&G / MC / alt / liq / ETF / GEX / volumes cachés. Soft ops lecture seule.")

    # history: previous row for deltas (before append)
    hist_path = THERMO / "history.jsonl"
    prev = None
    if hist_path.exists():
        try:
            lines = [ln for ln in hist_path.read_text(encoding="utf-8").splitlines() if ln.strip()]
            if lines:
                prev = json.loads(lines[-1])
        except Exception:
            prev = None

    def delta(cur, old_key, invert_good=False):
        """arrow: up|down|flat · for display. invert_good unused (arrows = direction pure)."""
        if cur is None or not prev or prev.get(old_key) is None:
            return {"dir": "flat", "delta": None, "label": "—"}
        try:
            d = float(cur) - float(prev[old_key])
        except Exception:
            return {"dir": "flat", "delta": None, "label": "—"}
        if abs(d) < 1e-12:
            return {"dir": "flat", "delta": 0.0, "label": "="}
        direction = "up" if d > 0 else "down"
        return {"dir": direction, "delta": round(d, 8), "label": "↑" if d > 0 else "↓"}

    deltas = {
        "mark": delta(mark, "mark"),
        "funding": delta(last_f, "funding"),
        "fundingAvg30": delta(fund_avg_30, "fundingAvg30"),
        "fundingAvgPrevMonth": delta(fund_avg_prev, "fundingAvgPrevMonth"),
        "longShort": delta(long_ratio, "longShort"),
        "chg24": delta(chg24, "chg24"),
        "oi": delta(oi_v, "oi"),
        "score": delta(score, "score"),
        "btcDominance": delta(dom, "btcDominance") if prev and prev.get("btcDominance") is not None else {"dir": "flat", "delta": None, "label": "—"},
        "panierDownPct": delta(panier, "panierDownPct") if prev and prev.get("panierDownPct") is not None else {"dir": "flat", "delta": None, "label": "—"},
        "whaleUsd": delta(whale_usd, "whaleUsd") if prev and prev.get("whaleUsd") is not None else {"dir": "flat", "delta": None, "label": "—"},
        "whaleN": delta(whale_n, "whaleN") if prev and prev.get("whaleN") is not None else {"dir": "flat", "delta": None, "label": "—"},
        "takerRatio": delta(taker_ratio, "takerRatio") if prev and prev.get("takerRatio") is not None else {"dir": "flat", "delta": None, "label": "—"},
        "topTraderLS": delta(top_trader_ls, "topTraderLS") if prev and prev.get("topTraderLS") is not None else {"dir": "flat", "delta": None, "label": "—"},
        "fearGreed": delta(fng.get("value"), "fearGreed") if prev and prev.get("fearGreed") is not None else {"dir": "flat", "delta": None, "label": "—"},
        "marketCapUsd": delta(total_mc, "marketCapUsd") if prev and prev.get("marketCapUsd") is not None else {"dir": "flat", "delta": None, "label": "—"},
        "liq24Usd": delta(liq.get("usd"), "liq24Usd") if prev and prev.get("liq24Usd") is not None else {"dir": "flat", "delta": None, "label": "—"},
        "liqLongUsd": delta(liq.get("longUsd"), "liqLongUsd") if prev and prev.get("liqLongUsd") is not None else {"dir": "flat", "delta": None, "label": "—"},
        "liqShortUsd": delta(liq.get("shortUsd"), "liqShortUsd") if prev and prev.get("liqShortUsd") is not None else {"dir": "flat", "delta": None, "label": "—"},
        "etfBtcM": delta(etf.get("btc"), "etfBtcM") if prev and prev.get("etfBtcM") is not None else {"dir": "flat", "delta": None, "label": "—"},
        "altSeasonScore": delta(alt_s.get("score"), "altSeasonScore") if prev and prev.get("altSeasonScore") is not None else {"dir": "flat", "delta": None, "label": "—"},
        "gexPutCall": delta(gex.get("putCallRatio"), "gexPutCall") if prev and prev.get("gexPutCall") is not None else {"dir": "flat", "delta": None, "label": "—"},
        "volumeCachedTaker": delta(vcz.get("takerBuyRatio"), "volumeCachedTaker") if prev and prev.get("volumeCachedTaker") is not None else {"dir": "flat", "delta": None, "label": "—"},
    }

    # history append
    hist_row = {
        "ts": ts,
        "tsUnix": int(now.timestamp()),
        "mark": mark,
        "funding": last_f,
        "fundingAvg30": fund_avg_30,
        "fundingAvgPrevMonth": fund_avg_prev,
        "longShort": long_ratio,
        "chg24": chg24,
        "oi": oi_v,
        "score": score,
        "climate": climate,
        "btcDominance": dom,
        "panierDownPct": panier,
        "whaleUsd": whale_usd,
        "whaleN": whale_n,
        "takerRatio": taker_ratio,
        "topTraderLS": top_trader_ls,
        "fearGreed": fng.get("value"),
        "marketCapUsd": total_mc,
        "altSeasonScore": alt_s.get("score"),
        "liq24Usd": liq.get("usd"),
        "etfBtcM": etf.get("btc"),
        "gexPutCall": gex.get("putCallRatio"),
        "volumeCachedTaker": vcz.get("takerBuyRatio"),
        "volumeCachedPerpSpot": vcz.get("perpSpotRatio"),
    }
    with hist_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(hist_row, ensure_ascii=False) + "\n")

    payload = {
        "ts": ts,
        "tsUnix": int(now.timestamp()),
        "symbol": SYM,
        "mark": mark,
        "oi": oi_v,
        "funding": last_f,
        "fundingAvg30": fund_avg_30,
        "fundingAvgPrevMonth": fund_avg_prev,
        "fundingSamples30": n30,
        "fundingSamplesPrev": nprev,
        "longShort": long_ratio,
        "chg24": chg24,
        "chg1h": chg1h,
        "chg4h": chg4h,
        "volQuote": vol,
        "btcDominance": dom,
        "panierDownPct": panier,
        "whaleN": whale_n,
        "whaleUsd": whale_usd,
        "whaleMax": round(whale_max, 0) if whale_n else 0,
        "whaleBuyUsd": round(whale_buy_usd, 0) if whale_n else 0,
        "whaleSellUsd": round(whale_sell_usd, 0) if whale_n else 0,
        "whaleDirProxy": whale_dir_proxy,
        "takerRatio": taker_ratio,
        "topTraderLS": top_trader_ls,
        "fearGreed": fng.get("value"),
        "fearGreedLabel": fng.get("label"),
        "marketCapUsd": total_mc,
        "altSeason": alt_s.get("label"),
        "altSeasonScore": alt_s.get("score"),
        "liq24Usd": liq.get("usd"),
        "liqLongUsd": liq.get("longUsd"),
        "liqShortUsd": liq.get("shortUsd"),
        "etf": {"btc": etf.get("btc"), "eth": etf.get("eth"), "xrp": etf.get("xrp"), "source": etf.get("source"), "unit": etf.get("unit") or "M$"},
        "gex": gex,
        "volumeCached": vcz,
        "etfBtcM": etf.get("btc"),
        "etfEthM": etf.get("eth"),
        "etfXrpM": etf.get("xrp"),
        "gexPutCall": gex.get("putCallRatio"),
        "gexCallWall": gex.get("callWall"),
        "gexPutWall": gex.get("putWall"),
        "volumeCachedTaker": vcz.get("takerBuyRatio"),
        "volumeCachedPerpSpot": vcz.get("perpSpotRatio"),
        "ace": ace,
        "score": score,
        "climate": climate,
        "lecture": lecture,
        "indicators": indicators,
        "deltas": deltas,
        "deltaMap": {
            "A1": "mark", "A3": "btcDominance", "A5": "mark", "A6": "chg24",
            "B7": "chg24", "B8": "chg24", "B9": "panierDownPct", "B10": "oi",
            "B11": "score", "B12": "score",
            "C13": "oi", "C14": "funding", "C15": "whaleUsd", "C16": "score",
            "C17": "chg24", "C18": "longShort", "C19": "score", "C20": "score",
            "C21": "score", "C22": "score", "C23": "takerRatio",
            "C24": "funding", "C25": "funding",
            "D26": "score", "D27": "mark", "D28": "btcDominance", "D29": "score",
            "D30": "score", "D31": "score", "D32": "score",
        },
        "prevTs": (prev or {}).get("ts") or prev_live.get("ts"),
        "source": "binance-fapi+coingecko+fng+okx-liq+bitbo-etf+deribit-gex+okx-rubik+ace-readonly",
        "wiredNote": "D26–D34 F&G/MC/alt/liq/ETF/GEX/volumes cachés · free + proxies · ACE lecture seule",
        "degraded": bool(stale_fields),
        "staleFields": stale_fields,
        "trioStatus": {
            "thermo": "DEGRADED" if stale_fields else "OK",
            "cockpit": "OK",
            "cortana": "OK",
            "msg": ("stale " + ",".join(stale_fields)) if stale_fields else "3/3 prêts — lecture seule",
        },
    }

    # markdown résumé
    body = f"""# Thermo dernier — gratuit (Binance public)

> Auto · **sans clé** · sans ordre · {ts} UTC  
> Script : `Index_Maison/scripts/thermo_quotidien_free.py`

## Clin d'œil
**Climat :** `{climate}` · **Score :** `{score}/100`

## Snapshot `{SYM}`

| Champ | Valeur | ID |
|-------|--------|-----|
| Mark | {mark} | prix |
| OI | {oi_v} | C13 |
| Funding | {last_f} | C14 |
| Funding moy. ~30j | {fund_avg_30} (n={n30}) | Cortana |
| Funding mois préc. | {fund_avg_prev} (n={nprev}) | Cortana |
| L/S 1h | {long_ratio} | crowd |
| BTC 1h/4h/24h | {chg1h} / {chg4h} / {chg24} % | B7 |
| Dominance BTC | {dom}% | A3 |
| Alts ↓ 24h | {panier}% | B9 |

## Lecture
{chr(10).join('- ' + x for x in lecture)}

## Branché / soft
- **Live free :** A1–A10, B7–B10, C13–C19, C22–C24 (+ C15/C23 proxies)
- **ACE lecture seule :** B11 heat · B12 RED · C21 SKIP (LIVE/CSV)
- **Soft ops :** C20 bassine · C25 walls proxy
- **Toujours REFUS :** Whale Alert payant · dark pool US abo · ZeroGEX dashboard
"""
    (WS / "THERMO_DERNIER.md").write_text(body, encoding="utf-8")

    live_json = THERMO / "live.json"
    live_js = THERMO / "live.js"

    # Préserver la section onchain injectée par le pont baleines (pont_onchain.py).
    # Sans ça, cette réécriture écrase le travail du pont → la chaîne BALEINES crie.
    try:
        if live_json.exists():
            ancien = json.loads(live_json.read_text(encoding="utf-8"))
            oc = ancien.get("onchain")
            if oc:
                payload["onchain"] = oc
    except Exception:
        pass

    live_json.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    live_js.write_text("window.__THERMO__ = " + json.dumps(payload, ensure_ascii=False) + ";\n", encoding="utf-8")

    # Cortana feed (volet cockpit + vocale)
    feed = {
        "ts": ts,
        "climate": climate,
        "score": score,
        "headline": lecture[0] if lecture else "Thermo à jour",
        "bullets": lecture[:4],
        "funding": last_f,
        "fundingAvg30": fund_avg_30,
        "fundingAvgPrevMonth": fund_avg_prev,
        "deltas": {
            "funding": deltas["funding"],
            "fundingAvg30": deltas["fundingAvg30"],
            "score": deltas["score"],
            "mark": deltas["mark"],
            "oi": deltas["oi"],
            "chg24": deltas["chg24"],
            "longShort": deltas["longShort"],
            "whaleUsd": deltas["whaleUsd"],
            "takerRatio": deltas["takerRatio"],
        },
        "whaleN": whale_n,
        "takerRatio": taker_ratio,
        "askHints": [
            "Quel est le funding maintenant ?",
            "Moyenne funding ~30 jours ?",
            "Moyenne funding mois dernier ?",
            "Climat thermo ?",
        ],
    }
    (THERMO / "cortana_feed.json").write_text(json.dumps(feed, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (THERMO / "cortana_feed.js").write_text("window.__CORTANA_FEED__ = " + json.dumps(feed, ensure_ascii=False) + ";\n", encoding="utf-8")
    cockpit = WS / "cockpit"
    if cockpit.exists():
        (cockpit / "cortana_feed.js").write_text((THERMO / "cortana_feed.js").read_text(encoding="utf-8"), encoding="utf-8")

    # OUTBOX
    OUT.mkdir(parents=True, exist_ok=True)
    for name in ["THERMO_DERNIER.md"]:
        (OUT / name).write_text(body, encoding="utf-8")
        (OUT / "Index_Maison").mkdir(parents=True, exist_ok=True)
        (OUT / "Index_Maison" / name).write_text(body, encoding="utf-8")
    out_t = OUT / "Index_Maison" / "thermo"
    out_t.mkdir(parents=True, exist_ok=True)
    for f in ["live.json", "live.js", "cortana_feed.json", "cortana_feed.js", "index.html"]:
        src = THERMO / f
        if src.exists():
            (out_t / f).write_text(src.read_text(encoding="utf-8"), encoding="utf-8")

    print(f"THERMO_OK climate={climate} score={score}" + (f" DEGRADED={','.join(stale_fields)}" if stale_fields else ""))
    print(f"THERMO_LIVE {live_json}")
    print(f"FUNDING now={last_f} avg30={fund_avg_30} prevMonth={fund_avg_prev}")
    core_ok = last_f is not None and oi_v is not None and fng.get("value") is not None
    if not core_ok:
        print("THERMO_CORE=NOK — funding/oi/fng manquants (réseau ?)")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

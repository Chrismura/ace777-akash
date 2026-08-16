#!/usr/bin/env python3
"""
Capteurs style ACE (copie d'idées, PAS le genesis) — MEXC spot only.

- spread / profondeur carnet
- déséquilibre bid/ask + « mur » (niveau dominant)
- tension = intensité de move court vs cadence
- aspiration (16/08 soir) : DOUBLE lecture du carnet → chute de murs (pattern V8 ACE :
  RADAR → FENÊTRE → MUR → ASPIRATION/SKIP — métaphores Christophe : bassine / verre d'eau / vortex)

Aucun import de GO_USINE / champion NUAGE.
"""
from __future__ import annotations

import time
import urllib.parse
from typing import Any, Callable, Optional


HttpJson = Callable[..., Any]


def book_sense(pair: str, http_json: HttpJson, limit: int = 20) -> dict:
    """Order book MEXC → spread, depths, imbalance, murs."""
    q = urllib.parse.urlencode({"symbol": pair, "limit": limit})
    j = http_json(f"https://api.mexc.com/api/v3/depth?{q}")
    bids = [(float(p), float(q_)) for p, q_ in j.get("bids", [])]
    asks = [(float(p), float(q_)) for p, q_ in j.get("asks", [])]
    if not bids or not asks:
        return {
            "ok": False,
            "reason": "empty_book",
            "spread_bps": 9999.0,
            "imbalance": 0.0,
            "bid_usdt": 0.0,
            "ask_usdt": 0.0,
            "wall_bid_usdt": 0.0,
            "wall_ask_usdt": 0.0,
        }
    best_bid, best_ask = bids[0][0], asks[0][0]
    mid = (best_bid + best_ask) / 2.0
    spread_bps = (best_ask - best_bid) / mid * 10000.0 if mid > 0 else 9999.0
    bid_usdt = sum(p * q_ for p, q_ in bids)
    ask_usdt = sum(p * q_ for p, q_ in asks)
    tot = bid_usdt + ask_usdt
    imbalance = (bid_usdt - ask_usdt) / tot if tot > 0 else 0.0  # >0 = bids plus lourds
    wall_bid = max((p * q_ for p, q_ in bids), default=0.0)
    wall_ask = max((p * q_ for p, q_ in asks), default=0.0)
    return {
        "ok": True,
        "reason": "ok",
        "spread_bps": round(spread_bps, 2),
        "imbalance": round(imbalance, 3),
        "bid_usdt": round(bid_usdt, 2),
        "ask_usdt": round(ask_usdt, 2),
        "wall_bid_usdt": round(wall_bid, 2),
        "wall_ask_usdt": round(wall_ask, 2),
        "best_bid": best_bid,
        "best_ask": best_ask,
    }


def aspiration_sense(
    pair: str,
    http_json: HttpJson,
    delay_s: float = 0.5,
    min_notional_usdt: float = 500.0,
    limit: int = 20,
) -> dict:
    """
    ASPIRATION (inspiration ACE V8) — DOUBLE lecture du carnet à ~delay_s d'écart.

    Métaphore « verre d'eau » (Christophe) : un mur qui fond = vide créé → le prix est
    aspiré vers lui. drop_bid = chute du mur bid (aspiration SELL), drop_ask = chute du
    mur ask (aspiration BUY). Pattern ACE : RADAR → FENÊTRE → MUR → ASPIRATION/SKIP.

    Mode OBSERVATION (décision famille 16/08) : renvoie les mesures, n'agit PAS sur le
    moteur. Fail-open : si la 2e lecture échoue (timeout MEXC fréquents), on renvoie la
    lecture simple sans aspiration — jamais de blocage.

    Retour : dict avec clés :
      ok, reason, spread_bps (2e lecture), drop_bid_pct, drop_ask_pct (chute brute %),
      drop_bid_pct_per_s, drop_ask_pct_per_s (chute NORMALISÉE par le temps réel écoulé,
      insensible au jitter réseau — correction GROK), max_drop_pct_per_s,
      aspiration_side (BUY si mur ask fond / SELL si mur bid fond), wall_bid_usdt,
      wall_ask_usdt, notional_drop_ok (mur ≥ min_notional_usdt — correction JUGE :
      <500$ = un ordre qui se retire, pas une aspiration), spread_delta_bps
      (correction JUGE : mur fond + spread resserré = vraie aspiration).
    """
    q = urllib.parse.urlencode({"symbol": pair, "limit": limit})

    def _one() -> dict:
        j = http_json(f"https://api.mexc.com/api/v3/depth?{q}")
        bids = [(float(p), float(q_)) for p, q_ in j.get("bids", [])]
        asks = [(float(p), float(q_)) for p, q_ in j.get("asks", [])]
        if not bids or not asks:
            return {"ok": False, "reason": "empty_book"}
        best_bid, best_ask = bids[0][0], asks[0][0]
        mid = (best_bid + best_ask) / 2.0
        spread_bps = (best_ask - best_bid) / mid * 10000.0 if mid > 0 else 9999.0
        wall_bid = max((p * q_ for p, q_ in bids), default=0.0)
        wall_ask = max((p * q_ for p, q_ in asks), default=0.0)
        return {
            "ok": True, "spread_bps": spread_bps,
            "wall_bid_usdt": wall_bid, "wall_ask_usdt": wall_ask,
        }

    try:
        d1 = _one()
        if not d1.get("ok"):
            return {"ok": False, "reason": d1.get("reason", "book1_fail")}
        t1 = time.time()
        time.sleep(delay_s)
        d2 = _one()
        t2 = time.time()
        if not d2.get("ok"):
            # fail-open : on garde la lecture 1 (le moteur continue avec book_sense)
            return {"ok": False, "reason": d2.get("reason", "book2_fail"), "partial": True}
    except Exception as e:
        # fail-open : timeout réseau → pas d'aspiration, jamais de blocage
        return {"ok": False, "reason": f"asp_err:{e}", "partial": True}

    dt = max(t2 - t1, 0.05)  # temps réel écoulé (jamais 0)

    def _drop(m1: float, m2: float) -> float:
        if m1 <= 0:
            return 0.0
        return (m1 - m2) / m1 * 100.0

    drop_bid = _drop(d1["wall_bid_usdt"], d2["wall_bid_usdt"])
    drop_ask = _drop(d1["wall_ask_usdt"], d2["wall_ask_usdt"])
    # NORMALISATION par le temps réel (correction GROK) : insensible au jitter réseau
    drop_bid_per_s = drop_bid / dt
    drop_ask_per_s = drop_ask / dt
    max_drop = max(drop_bid, drop_ask)
    max_drop_per_s = max_drop / dt

    # côté aspiré : le mur qui fond le plus vite (verre d'eau : le vide attire)
    aspiration_side = "BUY" if drop_ask >= drop_bid else "SELL"
    if max_drop <= 0.0:
        aspiration_side = "NONE"

    spread_delta_bps = d2["spread_bps"] - d1["spread_bps"]

    # correction JUGE : volume absolu min — un mur < min_notional = bruit, pas aspiration
    ref_wall = d1["wall_ask_usdt"] if aspiration_side == "BUY" else d1["wall_bid_usdt"]
    notional_drop_ok = ref_wall >= min_notional_usdt

    return {
        "ok": True,
        "reason": "ok",
        "spread_bps": round(d2["spread_bps"], 2),
        "spread_delta_bps": round(spread_delta_bps, 2),
        "drop_bid_pct": round(drop_bid, 2),
        "drop_ask_pct": round(drop_ask, 2),
        "drop_bid_pct_per_s": round(drop_bid_per_s, 2),
        "drop_ask_pct_per_s": round(drop_ask_per_s, 2),
        "max_drop_pct_per_s": round(max_drop_per_s, 2),
        "aspiration_side": aspiration_side,
        "wall_bid_usdt": round(d1["wall_bid_usdt"], 2),
        "wall_ask_usdt": round(d1["wall_ask_usdt"], 2),
        "notional_drop_ok": notional_drop_ok,
        "delay_s": round(dt, 3),
    }


def tension_score(move6_pct: float, cadence_pct: float, dd6_pct: float = 0.0) -> float:
    """
    Proxy tension ACE-like : move court / cadence (+ un peu de dd = énergie déjà consommée).
    ~0 = mort, >=2.5 = « orage » intéressant pour Hulk.
    """
    cad = max(float(cadence_pct or 1.0), 1.0)
    raw = abs(float(move6_pct or 0.0)) / cad
    raw += 0.15 * (abs(float(dd6_pct or 0.0)) / cad)
    return round(raw, 2)


def entry_gate(
    sense: dict,
    tension: float,
    cfg: dict,
    tier: str = "A",
    allow_wide_spike: bool = False,
) -> tuple[bool, str]:
    """
    Gate entrée inspiré filtres ACE (spread / mur / tension mini).
    allow_wide_spike: tier B spike (ex. QAIT) — spread plus toléré si tension haute.
    """
    max_spread = float(cfg.get("SENSE_MAX_SPREAD_BPS", "80"))
    if allow_wide_spike or tier == "B":
        max_spread = float(cfg.get("SENSE_MAX_SPREAD_BPS_SPIKE", "400"))
    min_depth = float(cfg.get("SENSE_MIN_DEPTH_USDT", "80"))
    min_tension = float(cfg.get("SENSE_MIN_TENSION", "1.2"))
    max_ask_wall_ratio = float(cfg.get("SENSE_MAX_ASK_WALL_RATIO", "8"))

    if not sense.get("ok"):
        return False, f"book_{sense.get('reason', 'fail')}"

    sp = float(sense.get("spread_bps") or 9999)
    if sp > max_spread:
        return False, f"spread_{sp:.0f}>{max_spread:.0f}bps"

    depth = min(float(sense.get("bid_usdt") or 0), float(sense.get("ask_usdt") or 0))
    if depth < min_depth and not allow_wide_spike:
        return False, f"thin_book_{depth:.0f}<{min_depth:.0f}"

    # mur ask énorme vs bid → difficile de sortir un long
    bid_w = float(sense.get("wall_bid_usdt") or 1)
    ask_w = float(sense.get("wall_ask_usdt") or 0)
    if bid_w > 0 and ask_w / bid_w > max_ask_wall_ratio and tension < min_tension * 2:
        return False, f"ask_wall_x{ask_w/bid_w:.1f}"

    if tension < min_tension and not allow_wide_spike:
        # cooling profond peut passer avec tension un peu basse si cfg le permet
        if cfg.get("SENSE_STRICT_TENSION", "1") not in ("0", "false", "False"):
            return False, f"tension_{tension}<{min_tension}"

    return True, f"ok_sp={sp:.0f} t={tension} imb={sense.get('imbalance')}"

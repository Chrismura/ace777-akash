#!/usr/bin/env python3
"""
Capteurs style ACE (copie d'idées, PAS le genesis) — MEXC spot only.

- spread / profondeur carnet
- déséquilibre bid/ask + « mur » (niveau dominant)
- tension = intensité de move court vs cadence

Aucun import de GO_USINE / champion NUAGE.
"""
from __future__ import annotations

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

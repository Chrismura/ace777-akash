#!/usr/bin/env python3
"""
Shadow Audit & Prediction - ETHUSDT
Architecture agentic observation-only:
- BETA (Scout): 500ms, defines trend "box"
- ALPHA (Hunter): 32ms, detects wall rupture
- Orchestrator: validates micro-vortex and regime via Qwen 1.5B
No orders are sent. This script only logs prediction quality.
"""

from __future__ import annotations

import csv
import json
import os
import signal
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from typing import Any, Dict


# === Mission constants (builder lock) ===
SCRIPT_VERSION = "shadow_agentic_v3"
RUN_ID = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
SYMBOL = os.environ.get("SYMBOL", "ETHUSDT")
BASE_URL = os.environ.get("BASE_URL", "https://testnet.binancefuture.com")
RADAR_THRESHOLD = float(os.environ.get("RADAR_THRESHOLD", "0.75"))   # Vortex frequency
MOMENTUM_THRESHOLD = float(os.environ.get("MOMENTUM_THRESHOLD", "0.92"))  # Instinct
BETA_DT_MS = int(os.environ.get("BETA_DT_MS", "500"))
ALPHA_DT_MS = int(os.environ.get("ALPHA_DT_MS", "32"))
MASS_ANCHOR = float(os.environ.get("MASS_ANCHOR", "1.618"))  # Golden anchor
WALL_DROP_REF_PCT = float(os.environ.get("WALL_DROP_REF_PCT", "6.5"))
DEPTH_LIMIT = int(os.environ.get("DEPTH_LIMIT", "20"))
REQUEST_TIMEOUT_SEC = float(os.environ.get("REQUEST_TIMEOUT_SEC", "8.0"))
LLM_GATE_ENABLED = os.environ.get("LLM_GATE_ENABLED", "TRUE").upper() == "TRUE"
# Queen 1.5B only (hard lock)
LLM_MODEL = "qwen2.5-coder:1.5b"
LLM_OLLAMA_URL = os.environ.get("LLM_OLLAMA_URL", "http://127.0.0.1:11434")
MICRO_VETO_MIN_TENSION = float(os.environ.get("MICRO_VETO_MIN_TENSION", "1.0"))
OUTPUT_CSV = os.environ.get(
    "OUTPUT_CSV",
    "runs/SHADOW_AUDIT_PREDICTION_ETH.csv",
)
SKIP_LOG_ENABLED = os.environ.get("SKIP_LOG_ENABLED", "TRUE").upper() == "TRUE"
_output_root, _output_ext = os.path.splitext(OUTPUT_CSV)
SKIP_LOG_CSV = os.environ.get("SKIP_LOG_CSV", f"{_output_root}_skips{_output_ext or '.csv'}")


RUNNING = True


def _handle_signal(_sig, _frame):
    global RUNNING
    RUNNING = False


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def fetch_json(path: str) -> dict:
    url = BASE_URL.rstrip("/") + path
    req = urllib.request.Request(url, method="GET")
    with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT_SEC) as resp:
        data = resp.read().decode("utf-8")
    return json.loads(data)


def post_json(url: str, payload: Dict[str, Any], timeout: float) -> Dict[str, Any]:
    raw = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=raw,
        method="POST",
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read().decode("utf-8")
    return json.loads(data)


def get_price(symbol: str) -> float:
    q = urllib.parse.urlencode({"symbol": symbol})
    j = fetch_json(f"/fapi/v1/ticker/price?{q}")
    return float(j["price"])


def get_depth(symbol: str, limit: int) -> dict:
    q = urllib.parse.urlencode({"symbol": symbol, "limit": limit})
    return fetch_json(f"/fapi/v1/depth?{q}")


def wall_mass(depth_side: list[list[str]]) -> float:
    # Sum quantities (consistent with lightweight wall pressure proxy)
    total = 0.0
    for lvl in depth_side:
        if len(lvl) >= 2:
            total += float(lvl[1])
    return total


def wall_drop_pct(prev_mass: float, next_mass: float) -> float:
    if prev_mass <= 0:
        return 0.0
    drop = (prev_mass - next_mass) / prev_mass * 100.0
    return drop if drop > 0 else 0.0


def bps_change(base: float, px: float) -> float:
    if base == 0:
        return 0.0
    return (px - base) / base * 10000.0


def detect_event(side: str, impulse_bps_s: float, tension_score: float) -> bool:
    # Core harmonic gate: radar + instinct
    if abs(impulse_bps_s) < MOMENTUM_THRESHOLD:
        return False
    if tension_score < RADAR_THRESHOLD:
        return False
    # Side coherence: BUY expects positive impulse, SELL expects negative impulse
    if side == "BUY" and impulse_bps_s <= 0:
        return False
    if side == "SELL" and impulse_bps_s >= 0:
        return False
    return True


def _extract_json_object(text: str) -> Dict[str, Any]:
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        return {}
    try:
        return json.loads(text[start:end + 1])
    except Exception:
        return {}


def llm_micro_validate(alpha: Dict[str, Any]) -> Dict[str, Any]:
    # Expected compact JSON:
    # {"micro_vortex":"GO|SKIP","direction":"BUY|SELL","confidence":0-1}
    side = alpha["side"]
    prompt = (
        "Tu es un validateur micro-vortex. Reponds UNIQUEMENT en JSON compact: "
        '{"micro_vortex":"GO|SKIP","direction":"BUY|SELL","confidence":0.0}. '
        f"Data: side={side} impulse_bps_s={alpha['impulse_bps_s']:.6f} "
        f"tension_score={alpha['tension_score']:.6f} anchor={alpha['anchor_score']:.6f} "
        f"radar_thr={RADAR_THRESHOLD} mom_thr={MOMENTUM_THRESHOLD}."
    )
    fallback = {
        "micro_vortex": "SKIP",
        "direction": side,
        "confidence": 0.0,
    }
    if not LLM_GATE_ENABLED:
        return fallback
    try:
        j = post_json(
            f"{LLM_OLLAMA_URL.rstrip('/')}/api/generate",
            {"model": LLM_MODEL, "prompt": prompt, "stream": False},
            timeout=10.0,
        )
        obj = _extract_json_object(str(j.get("response", "")))
        mv = str(obj.get("micro_vortex", fallback["micro_vortex"])).upper()
        if mv not in {"GO", "SKIP"}:
            mv = fallback["micro_vortex"]
        direction = str(obj.get("direction", side)).upper()
        if direction not in {"BUY", "SELL"}:
            direction = side
        conf = float(obj.get("confidence", fallback["confidence"]))
        conf = 0.0 if conf < 0 else (1.0 if conf > 1 else conf)
        return {"micro_vortex": mv, "direction": direction, "confidence": conf}
    except Exception:
        return fallback


def llm_regime_validate(beta: Dict[str, Any]) -> Dict[str, Any]:
    # Expected compact JSON:
    # {"regime":"TREND|CHOP","confidence":0-1}
    prompt = (
        "Tu es un detecteur de regime. Reponds UNIQUEMENT en JSON compact: "
        '{"regime":"TREND|CHOP","confidence":0.0}. '
        f"Data: beta_side={beta['side']} beta_impulse_bps_s={beta['impulse_bps_s']:.6f} "
        f"beta_tension={beta['tension_score']:.6f} radar_thr={RADAR_THRESHOLD} mom_thr={MOMENTUM_THRESHOLD}."
    )
    fallback_regime = (
        "TREND"
        if (abs(beta["impulse_bps_s"]) >= MOMENTUM_THRESHOLD and beta["tension_score"] >= RADAR_THRESHOLD)
        else "CHOP"
    )
    fallback = {"regime": fallback_regime, "confidence": 0.50}
    if not LLM_GATE_ENABLED:
        return fallback
    try:
        j = post_json(
            f"{LLM_OLLAMA_URL.rstrip('/')}/api/generate",
            {"model": LLM_MODEL, "prompt": prompt, "stream": False},
            timeout=10.0,
        )
        obj = _extract_json_object(str(j.get("response", "")))
        regime = str(obj.get("regime", fallback["regime"])).upper()
        if regime not in {"TREND", "CHOP"}:
            regime = fallback["regime"]
        conf = float(obj.get("confidence", fallback["confidence"]))
        conf = 0.0 if conf < 0 else (1.0 if conf > 1 else conf)
        return {"regime": regime, "confidence": conf}
    except Exception:
        return fallback


def snapshot(dt_ms: int) -> Dict[str, Any]:
    dt_sec = dt_ms / 1000.0
    p0 = get_price(SYMBOL)
    d0 = get_depth(SYMBOL, DEPTH_LIMIT)
    time.sleep(dt_sec)
    p1 = get_price(SYMBOL)
    d1 = get_depth(SYMBOL, DEPTH_LIMIT)

    mom_bps = bps_change(p0, p1)
    impulse_bps_s = mom_bps * (1000.0 / dt_ms)

    bid0 = wall_mass(d0.get("bids", []))
    ask0 = wall_mass(d0.get("asks", []))
    bid1 = wall_mass(d1.get("bids", []))
    ask1 = wall_mass(d1.get("asks", []))

    bid_drop = wall_drop_pct(bid0, bid1)
    ask_drop = wall_drop_pct(ask0, ask1)
    max_drop = bid_drop if bid_drop >= ask_drop else ask_drop
    tension_score = max_drop / WALL_DROP_REF_PCT if WALL_DROP_REF_PCT > 0 else 0.0
    anchor_score = tension_score * MASS_ANCHOR
    side = "SELL" if bid_drop >= ask_drop else "BUY"
    return {
        "p0": p0,
        "p1": p1,
        "mom_bps": mom_bps,
        "impulse_bps_s": impulse_bps_s,
        "bid_drop": bid_drop,
        "ask_drop": ask_drop,
        "tension_score": tension_score,
        "anchor_score": anchor_score,
        "side": side,
        "dt_ms": dt_ms,
    }


def ensure_csv(path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    expected_header = [
        "ts",
        "script_version",
        "run_id",
        "symbol",
        "beta_side",
        "alpha_side",
        "beta_dt_ms",
        "alpha_dt_ms",
        "radar_threshold",
        "momentum_threshold",
        "mass_anchor",
        "beta_price_t0",
        "beta_price_t1",
        "beta_impulse_bps_s",
        "beta_tension_score",
        "alpha_price_t0",
        "alpha_price_t1",
        "alpha_impulse_bps_s",
        "alpha_tension_score",
        "regime_v9",
        "regime_conf",
        "micro_vortex",
        "micro_conf",
        "price_500ms",
        "price_2s",
        "delta_500ms_bps_alpha",
        "delta_2s_bps_alpha",
        "slippage_theorique_price",
        "slippage_theorique_bps",
        "vortex_success",
        "friction_saved_bps",
    ]

    if os.path.exists(path):
        try:
            with open(path, "r", newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                first = next(reader, [])
            if first == expected_header:
                return
            # Prevent mixing old schema and new schema rows.
            backup = f"{path}.bak_{int(time.time())}"
            os.rename(path, backup)
            print(f"[info] Old CSV schema moved to: {backup}")
        except Exception:
            pass

    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(expected_header)


def append_event(path: str, row: list) -> None:
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(row)


def ensure_skip_csv(path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    expected_header = [
        "ts",
        "script_version",
        "run_id",
        "symbol",
        "skip_reason",
        "beta_side",
        "alpha_side",
        "beta_impulse_bps_s",
        "beta_tension_score",
        "alpha_impulse_bps_s",
        "alpha_tension_score",
        "radar_threshold",
        "momentum_threshold",
        "regime_v9",
        "micro_vortex",
        "micro_direction",
    ]
    if os.path.exists(path):
        try:
            with open(path, "r", newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                first = next(reader, [])
            if first == expected_header:
                return
            backup = f"{path}.bak_{int(time.time())}"
            os.rename(path, backup)
            print(f"[info] Old SKIP CSV schema moved to: {backup}")
        except Exception:
            pass
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(expected_header)


def append_skip(path: str, row: list) -> None:
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(row)


def verdict(v: float) -> str:
    if v > 0:
        return "GOOD"
    if v < 0:
        return "BAD"
    return "FLAT"


def main() -> int:
    signal.signal(signal.SIGINT, _handle_signal)
    signal.signal(signal.SIGTERM, _handle_signal)

    ensure_csv(OUTPUT_CSV)
    if SKIP_LOG_ENABLED:
        ensure_skip_csv(SKIP_LOG_CSV)

    print("=== SHADOW AUDIT & PREDICTION ===")
    print("Mode: OBSERVATION_ONLY")
    print(f"Symbol: {SYMBOL}")
    print(
        f"Constants: radar={RADAR_THRESHOLD} mom={MOMENTUM_THRESHOLD} "
        f"beta_dt={BETA_DT_MS}ms alpha_dt={ALPHA_DT_MS}ms mass={MASS_ANCHOR}"
    )
    print(f"Micro-veto: active only if tension>{MICRO_VETO_MIN_TENSION}")
    print(f"LLM: enabled={LLM_GATE_ENABLED} model={LLM_MODEL}")
    print(f"Script: {SCRIPT_VERSION} run_id={RUN_ID}")
    print(f"Output: {OUTPUT_CSV}")
    print(f"Skip log: enabled={SKIP_LOG_ENABLED} path={SKIP_LOG_CSV}")

    while RUNNING:
        try:
            beta = snapshot(BETA_DT_MS)
            alpha = snapshot(ALPHA_DT_MS)
        except Exception as e:
            print(f"[warn] market fetch error: {e}")
            time.sleep(0.25)
            continue

        # Hard gate first: no physical trigger => no event logged.
        event_detected = detect_event(alpha["side"], alpha["impulse_bps_s"], alpha["tension_score"])
        if not event_detected:
            if abs(alpha["impulse_bps_s"]) < MOMENTUM_THRESHOLD:
                skip_reason = "momentum_too_small"
            elif alpha["tension_score"] < RADAR_THRESHOLD:
                skip_reason = "tension_below_radar"
            elif alpha["side"] == "BUY" and alpha["impulse_bps_s"] <= 0:
                skip_reason = "buy_side_incoherent"
            elif alpha["side"] == "SELL" and alpha["impulse_bps_s"] >= 0:
                skip_reason = "sell_side_incoherent"
            else:
                skip_reason = "hard_gate_reject"
            if SKIP_LOG_ENABLED:
                append_skip(
                    SKIP_LOG_CSV,
                    [
                        utc_now_iso(),
                        SCRIPT_VERSION,
                        RUN_ID,
                        SYMBOL,
                        skip_reason,
                        beta["side"],
                        alpha["side"],
                        f"{beta['impulse_bps_s']:.8f}",
                        f"{beta['tension_score']:.8f}",
                        f"{alpha['impulse_bps_s']:.8f}",
                        f"{alpha['tension_score']:.8f}",
                        RADAR_THRESHOLD,
                        MOMENTUM_THRESHOLD,
                        "",
                        "",
                        "",
                    ],
                )
            continue
        regime_out = llm_regime_validate(beta)
        micro_veto_active = alpha["tension_score"] > MICRO_VETO_MIN_TENSION
        if micro_veto_active:
            micro_out = llm_micro_validate(alpha)
        else:
            # Keep hard-gate and regime gate, but bypass micro veto in weak-tension zones.
            micro_out = {"micro_vortex": "BYPASS", "direction": alpha["side"], "confidence": 1.0}
        # Regime veto: in CHOP we do not log predictive events.
        if regime_out["regime"] != "TREND":
            if SKIP_LOG_ENABLED:
                append_skip(
                    SKIP_LOG_CSV,
                    [
                        utc_now_iso(),
                        SCRIPT_VERSION,
                        RUN_ID,
                        SYMBOL,
                        "regime_chop",
                        beta["side"],
                        alpha["side"],
                        f"{beta['impulse_bps_s']:.8f}",
                        f"{beta['tension_score']:.8f}",
                        f"{alpha['impulse_bps_s']:.8f}",
                        f"{alpha['tension_score']:.8f}",
                        RADAR_THRESHOLD,
                        MOMENTUM_THRESHOLD,
                        regime_out["regime"],
                        micro_out["micro_vortex"],
                        micro_out["direction"],
                    ],
                )
            continue
        # If micro veto is enabled and not GO, skip event logging.
        if micro_veto_active and micro_out["micro_vortex"] != "GO":
            if SKIP_LOG_ENABLED:
                append_skip(
                    SKIP_LOG_CSV,
                    [
                        utc_now_iso(),
                        SCRIPT_VERSION,
                        RUN_ID,
                        SYMBOL,
                        "micro_veto_skip",
                        beta["side"],
                        alpha["side"],
                        f"{beta['impulse_bps_s']:.8f}",
                        f"{beta['tension_score']:.8f}",
                        f"{alpha['impulse_bps_s']:.8f}",
                        f"{alpha['tension_score']:.8f}",
                        RADAR_THRESHOLD,
                        MOMENTUM_THRESHOLD,
                        regime_out["regime"],
                        micro_out["micro_vortex"],
                        micro_out["direction"],
                    ],
                )
            continue
        # Direction mismatch veto (only when micro veto is enabled).
        if micro_veto_active and micro_out["direction"] != alpha["side"]:
            if SKIP_LOG_ENABLED:
                append_skip(
                    SKIP_LOG_CSV,
                    [
                        utc_now_iso(),
                        SCRIPT_VERSION,
                        RUN_ID,
                        SYMBOL,
                        "direction_mismatch",
                        beta["side"],
                        alpha["side"],
                        f"{beta['impulse_bps_s']:.8f}",
                        f"{beta['tension_score']:.8f}",
                        f"{alpha['impulse_bps_s']:.8f}",
                        f"{alpha['tension_score']:.8f}",
                        RADAR_THRESHOLD,
                        MOMENTUM_THRESHOLD,
                        regime_out["regime"],
                        micro_out["micro_vortex"],
                        micro_out["direction"],
                    ],
                )
            continue

        ts = utc_now_iso()
        try:
            signal_price = alpha["p1"]
            time.sleep(0.5)
            p500 = get_price(SYMBOL)
            time.sleep(1.5)
            p2s = get_price(SYMBOL)
        except Exception as e:
            print(f"[warn] follow-up price fetch error: {e}")
            time.sleep(0.25)
            continue

        d500 = bps_change(signal_price, p500)
        d2s = bps_change(signal_price, p2s)
        aligned500 = d500 if alpha["side"] == "BUY" else -d500
        aligned2s = d2s if alpha["side"] == "BUY" else -d2s
        slippage_price = signal_price - p500
        slippage_bps = bps_change(signal_price, p500)
        vortex_success = aligned500 > 0
        friction_saved_bps = aligned500 if aligned500 > 0 else 0.0

        row = [
            ts,
            SCRIPT_VERSION,
            RUN_ID,
            SYMBOL,
            beta["side"],
            alpha["side"],
            BETA_DT_MS,
            ALPHA_DT_MS,
            RADAR_THRESHOLD,
            MOMENTUM_THRESHOLD,
            MASS_ANCHOR,
            f"{beta['p0']:.8f}",
            f"{beta['p1']:.8f}",
            f"{beta['impulse_bps_s']:.8f}",
            f"{beta['tension_score']:.8f}",
            f"{alpha['p0']:.8f}",
            f"{alpha['p1']:.8f}",
            f"{alpha['impulse_bps_s']:.8f}",
            f"{alpha['tension_score']:.8f}",
            regime_out["regime"],
            f"{regime_out['confidence']:.4f}",
            micro_out["micro_vortex"],
            f"{micro_out['confidence']:.4f}",
            f"{p500:.8f}",
            f"{p2s:.8f}",
            f"{d500:.8f}",
            f"{d2s:.8f}",
            f"{slippage_price:.8f}",
            f"{slippage_bps:.8f}",
            "TRUE" if vortex_success else "FALSE",
            f"{friction_saved_bps:.8f}",
        ]
        append_event(OUTPUT_CSV, row)
        print(
            f"[{ts}] regime={regime_out['regime']} micro={micro_out['micro_vortex']} "
            f"alpha_side={alpha['side']} tension={alpha['tension_score']:.3f} "
            f"slip500={slippage_bps:.2f}bps vortex_success={vortex_success} "
            f"friction_saved={friction_saved_bps:.2f}bps"
        )

    print("Stopping observer.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

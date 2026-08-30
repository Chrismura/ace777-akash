#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ACE777 — Harnais de comparaison Hyperliquid testnet
====================================================
Réplique LA MÊME logique qu'ACE (champion scellé 37fca367) sur Hyperliquid testnet
pour comparer frais, partial fills, et PnL net vs Binance.

Params IDENTIQUES à ACE baseline (tout OFF par défaut : duo/swarm/v8/vortex).
LOG : même CSV qu'ACE pour comparaison facile.

Usage:
  python3 hl_compare.py [--duration HH:MM:SS] [--paper] [--verbose]
  python3 hl_compare.py --duration 02:00:00    # session 2h
  python3 hl_compare.py --paper                 # simulation (pas d'ordres réels)
"""

import os, sys, json, time, csv, signal, argparse, ssl, urllib.request
from datetime import datetime, timezone
from pathlib import Path

# ─── CONFIG (identique ACE baseline) ───────────────────────────────────────────
SYMBOL = "BTC"               # Hyperliquid: BTC (pas BTCUSDT)
BUY_USDT = 500.0             # taille d'entrée (identique ACE)
LEVERAGE = 5                 # levier (identique ACE)
SLEEP_SEC = 1.0              # pause entre cycles (identique ACE)
POLL_SEC = 0.5

# Core strategy (identique ACE)
MIN_PROFIT_BPS = 15.0        # take-profit net (après frais)
FEE_ROUND_TRIP_BPS = 2.0     # Hyperliquid: 0.01% taker × 2 = 2 bps (aller-retour)
STOP_LOSS_BPS = 10.0         # stop-loss (identique ACE)
MAX_HOLD_SEC = 150.0         # max hold (identique ACE)
MIN_HOLD_SEC = 15.0          # min hold avant exit (identique ACE)
TRAIL_ARM_BPS = 5.0          # trailing arm (identique ACE)
TRAIL_GIVEBACK_BPS = 3.0     # trailing giveback (identique ACE)

# Radar gates (identique ACE)
RADAR_MIN_CONF = 0.30
RADAR_MIN_MOM_BPS = 0.003   # plancher vortex ACE en pratique (pas le strict 0.01 baseline)
RADAR_DIR_BPS = 0.20
RADAR_MAX_SPREAD_BPS = 8.0
MOMENTUM_THRESHOLD = 0.01
MOMENTUM_SLEEP_SEC = 1.0     # délai entre p1 et p2 (identique ACE)
TREND_LOOKBACK_MIN = 3        # structure lookback (kline count)

# Sortie
ENABLE_ORDERS = True

# ─── Hyperliquid init ──────────────────────────────────────────────────────────
ENV_PATH = Path(__file__).parent / ".env"
if ENV_PATH.exists():
    for line in ENV_PATH.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())

from hyperliquid.info import Info
from hyperliquid.exchange import Exchange
from hyperliquid.utils import constants
from eth_account import Account as EthAccount

ACCOUNT = os.environ.get("HL_TESTNET_ADDR", "")
PRIVATE_KEY = os.environ.get("HL_TESTNET_KEY", "")

info = Info(constants.TESTNET_API_URL, skip_ws=True)
exchange = None
if ACCOUNT and PRIVATE_KEY:
    try:
        wallet = EthAccount.from_key(PRIVATE_KEY)
        exchange = Exchange(wallet, constants.TESTNET_API_URL)
    except Exception as e:
        print(f"[WARN] wallet HL non initialisé: {e}", file=sys.stderr)

# ─── Utilitaires (identiques ACE) ─────────────────────────────────────────────
def bps(p1: float, p2: float) -> float:
    """bps_change(base, px) — identique ACE"""
    if p1 <= 0:
        return 0.0
    return (p2 - p1) / p1 * 10000.0

def floor_step_qty(qty: float, step: float = 0.001) -> float:
    s = max(step, 0.001)
    return (qty // s) * s

def now_ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def now_sec() -> float:
    return time.time()

# ─── Marché (Hyperliquid testnet) ─────────────────────────────────────────────
def get_price() -> tuple:
    """Retourne (bid, ask) — via /info/allMids ou l2 book"""
    try:
        meta = info.meta()
        universe = meta.get("universe", [])
        if not universe:
            return 0.0, 0.0
        mids = info.all_mids()
        mid = float(mids.get("BTC", 0))
        # Hyperliquid testnet: spread ~0.01%, bid ≈ mid*0.9999, ask ≈ mid*1.0001
        spread_pct = 0.0001
        return mid * (1 - spread_pct), mid * (1 + spread_pct)
    except Exception as e:
        print(f"[WARN] get_price: {e}", file=sys.stderr)
        return 0.0, 0.0

def get_book() -> tuple:
    """Retourne (bid, ask) depuis L2 orderbook"""
    try:
        l2 = info.l2_snapshot("BTC")
        if l2 and l2.get("levels"):
            levels = l2["levels"]
            bids = [(float(l["px"]), float(l["sz"])) for l in levels[0]] if len(levels) > 0 else []
            asks = [(float(l["px"]), float(l["sz"])) for l in levels[1]] if len(levels) > 1 else []
            if bids and asks:
                return bids[0][0], asks[0][0]
    except Exception:
        pass
    return get_price()

def get_klines(limit: int = 5):
    """Klines proxy via candles_snapshot (peut être vide sur testnet)"""
    try:
        candles = info.candles_snapshot("BTC", "1m", 0, limit + 1)
        if not candles:
            return []
        # candles = [{t, i, o, h, l, c, v, n}, ...]
        return candles
    except:
        return []

def trend_bps_from_klines(klines) -> float:
    """Identique ACE: bps entre 1er open et dernier close"""
    if not klines or len(klines) < 2:
        return 0.0
    op = float(klines[0]["o"])
    cl = float(klines[-1]["c"])
    if op <= 0:
        return 0.0
    return (cl - op) / op * 10000.0

def get_mid_price() -> float:
    """Prix milieu via all_mids — proxy du ticker price Binance (p1/p2 d'ACE)"""
    try:
        mids = info.all_mids()
        return float(mids.get("BTC", 0))
    except:
        return 0.0

def get_binance_price() -> float:
    """Prix fin BTC depuis le ticker futures Binance — identique au p1/p2 d'ACE.
    ACE utilise /fapi/v1/ticker/price (futures, pas spot).
    En mode paper, le momentum vient de ce prix, les spreads du book HL."""
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        req = urllib.request.Request(
            "https://fapi.binance.com/fapi/v1/ticker/price?symbol=BTCUSDT",
            headers={"User-Agent": "ACE777-hl-compare/1.0"})
        with urllib.request.urlopen(req, timeout=5, context=ctx) as r:
            return float(json.loads(r.read().decode())["price"])
    except Exception:
        return 0.0

# ─── Radar (identique ACE check_radar) ─────────────────────────────────────────
def check_radar(mom_bps: float, spread_bps: float):
    """Réplique la logique RADAR_GATE d'ACE"""
    min_conf = RADAR_MIN_CONF
    min_mom = RADAR_MIN_MOM_BPS
    max_spread = RADAR_MAX_SPREAD_BPS
    dir_bps = RADAR_DIR_BPS

    # spread check
    if spread_bps > max_spread:
        return {"allow": False, "direction": "neutral", "reason": "spread_too_high",
                "confidence": round(max(0.0, 1.0 - spread_bps / max_spread), 4)}

    # momentum check — identique ACE (radar_gate.rb) : abs_mom < min_mom(0.003) → bloqué
    abs_mom = abs(mom_bps)

    # Flat-momentum baseline (radar_gate.rb ligne 74) : si spread sain et abs_mom==0,
    # on donne une conf minimale de 0.35 pour éviter de bloquer 100% des cycles.
    # ACE utilise cette baseline pour rester en veille et saisir les micro-mouvements.
    if abs_mom == 0.0 and spread_bps <= max_spread:
        conf = 0.35
    else:
        conf = min(1.0, abs_mom / max(dir_bps, 0.01))

    if abs_mom < min_mom:
        return {"allow": False, "direction": "neutral", "reason": "momentum_too_low",
                "confidence": round(conf, 4)}

    # direction (identique radar_gate.rb : |mom| ≥ dir_bps → long/short, sinon neutral)
    if mom_bps >= dir_bps:
        direction = "long"
    elif mom_bps <= -dir_bps:
        direction = "short"
    else:
        direction = "neutral"
    if conf < min_conf:
        return {"allow": False, "direction": direction, "reason": "confidence_too_low",
                "confidence": round(conf, 4)}

    return {"allow": True, "direction": direction, "reason": "ok",
            "confidence": round(conf, 4)}

# ─── Ordres Hyperliquid ────────────────────────────────────────────────────────
def place_order(side: str, price: float, sz: float) -> dict:
    """Place un ordre MARKET via Hyperliquid SDK. Retourne {fills, fee, avgPx}"""
    if not exchange:
        return {"error": "pas de wallet"}

    is_buy = side.upper() == "BUY"
    try:
        result = exchange.market_open(
            "BTC",             # coin
            is_buy,            # is_buy
            sz,                # sz
            None,              # limitPx (None = market)
            0.01,              # slippage = 1%
        )
        return _parse_result(result, sz)
    except Exception as e:
        # Fallback: utiliser l'API REST directement
        try:
            from hyperliquid.utils.signing import OrderRequest, order_spec_preprocessing, sign_l1_action
            order = OrderRequest(
                coin="BTC",
                is_buy=is_buy,
                sz=sz,
                order_type={"limit": {"tif": "Ioc"}},
                limit_px=str(round(price * 1.02, 1)) if is_buy else str(round(price * 0.98, 1)),
                reduce_only=False,
            )
            res = exchange.order(order)
            return _parse_result(res, sz)
        except Exception as e2:
            return {"error": str(e2)[:200]}

def _parse_result(result, sz) -> dict:
    """Extrait les infos de fill depuis la réponse Hyperliquid"""
    if not result:
        return {"filled": 0.0, "fee": 0.0, "avgPx": 0.0, "error": "resultat vide"}
    if isinstance(result, dict):
        if "error" in result or result.get("status") == "err":
            return {"filled": 0.0, "fee": 0.0, "avgPx": 0.0, "error": str(result.get("response", ""))[:120]}
        # Structure typique de réponse
        responses = result.get("response", {}).get("data", {}).get("statuses", [])
        if not responses:
            # Essai exchange.market_open: result contient directement les données
            if "statuses" in result:
                responses = result["statuses"]
        if responses and isinstance(responses, list) and len(responses) > 0:
            r = responses[0]
            if isinstance(r, dict):
                if r.get("error"):
                    return {"filled": 0.0, "fee": 0.0, "avgPx": 0.0, "error": str(r["error"])[:120]}
                filled = float(r.get("filled", {}).get("totalSz", r.get("totalSz", 0)))
                avg_px = float(r.get("filled", {}).get("avgPx", r.get("avgPx", 0)))
                fee = float(r.get("filled", {}).get("fee", r.get("fee", 0)))
                return {"filled": filled, "fee": fee, "avgPx": avg_px}
    return {"filled": 0.0, "fee": 0.0, "avgPx": 0.0, "error": "format inattendu"}

def close_position(sz: float) -> dict:
    """Ferme la position — sens opposé"""
    if not exchange:
        return {"error": "pas de wallet"}
    try:
        result = exchange.market_close("BTC", sz)
        return _parse_result(result, sz)
    except:
        return {"error": "close impossible"}

# ─── Boucle principale ─────────────────────────────────────────────────────────
def run_loop(duration_sec: float, paper: bool = False, verbose: bool = False):
    csv_path = Path(f"HL_COMPARE_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")
    csv_header = "ts,cycle,side,status,entryPrice,exitPrice,qty,bps,pnl,feeUsdt,pnlNet,exitReason,holdSec,msg"

    with open(csv_path, "w") as f:
        f.write(csv_header + "\n")

    t_start = now_sec()
    cycle = 0
    position = None  # {side, entry_px, qty, highest, entry_ts}
    pnl_total = 0.0
    fee_total = 0.0
    skip_count = 0

    print(f"=== ACE→HL harnais | {now_ts()} | duration={duration_sec}s | paper={paper} ===")
    print(f"CSV: {csv_path}")

    try:
        while now_sec() - t_start < duration_sec:
            cycle += 1

            # Check STOP file (identique ACE)
            if os.path.exists("STOP"):
                print(f"STOP détecté au cycle #{cycle} — arrêt propre.")
                break

            # 1. Prix + spread
            if paper:
                # Paper : tout sur Binance (même marché BTC, prix fins, spread réel).
                # Seuls les frais changent (HL 2 bps vs Binance 8 bps) → comparaison pure.
                p1 = get_binance_price()
                time.sleep(1.0)  # MOMENTUM_SLEEP_SEC = 1.0
                p2 = get_binance_price()
                momentum_signal = bps(p1, p2) if p1 > 0 and p2 > 0 else 0.0
                # Spread bid/ask réaliste BTC (~0.1 bps) — pour comparaison frais pure
                mid_px = p2 if p2 > 0 else p1
                bid = mid_px * 0.9999
                ask = mid_px * 1.0001
                spread_bps = (ask - bid) / ask * 10000.0 if ask > 0 else 0.0
            else:
                bid, ask = get_book()
                spread_bps = (ask - bid) / ask * 10000.0 if ask > 0 else 0.0
                p1 = get_mid_price()
                time.sleep(1.0)  # MOMENTUM_SLEEP_SEC = 1.0
                p2 = get_mid_price()
                momentum_signal = bps(p1, p2) if p1 > 0 and p2 > 0 else 0.0
            if bid <= 0 or ask <= 0:
                time.sleep(SLEEP_SEC)
                continue

            # 3. Structure direction (klines 1m — vide sur testnet → neutral)
            klines = get_klines(TREND_LOOKBACK_MIN)
            trend_bps = trend_bps_from_klines(klines)
            structure = "neutral"
            if trend_bps >= 1:
                structure = "long"
            elif trend_bps <= -1:
                structure = "short"

            # 4. Radar
            radar = check_radar(momentum_signal, spread_bps)

            if not radar["allow"]:
                skip_count += 1
                with open(csv_path, "a") as f:
                    f.write(f"{now_ts()},{cycle},SKIP,SKIPPED,,,,,0,,,reason={radar['reason']} conf={radar['confidence']} mom={momentum_signal:.4f} spread={spread_bps:.1f},0,\n")
                if verbose or skip_count <= 3 or skip_count % 100 == 0:
                    print(f"#{cycle} SKIP | {radar['reason']} conf={radar['confidence']} mom={momentum_signal:.2f} bps")
                time.sleep(SLEEP_SEC)
                continue

            # 5. Direction
            direction = radar["direction"]
            if structure != "neutral" and direction != structure:
                radar["allow"] = False
                radar["reason"] = "tactic_mismatch"

            if not radar["allow"]:
                skip_count += 1
                with open(csv_path, "a") as f:
                    f.write(f"{now_ts()},{cycle},SKIP,SKIPPED,,,,,0,,,reason={radar['reason']},0,\n")
                time.sleep(SLEEP_SEC)
                continue

            # 6. Entrée
            entry_px = ask if direction == "long" else bid
            qty = floor_step_qty(BUY_USDT / entry_px, 0.001)

            side = "BUY" if direction == "long" else "SELL"
            close_side = "SELL" if side == "BUY" else "BUY"

            if paper:
                # Mode paper: simuler fill parfait (comme CSV ACE, pour comparer)
                position = {
                    "side": side,
                    "entry_px": entry_px,
                    "qty": qty,
                    "highest": entry_px,
                    "lowest": entry_px,  # pour SHORT
                    "entry_ts": now_sec(),
                    "entry_cycle": cycle,
                }
                filled_fee = BUY_USDT * 0.0001  # 1 bps taker HL
                filled_qty = qty
                print(f"#{cycle} 📌 ENTRY {side} | px={entry_px:.1f} qty={qty:.4f} (PAPER)")
            else:
                order_result = place_order(side, entry_px, qty)
                if order_result.get("error") or order_result.get("filled", 0) <= 0:
                    print(f"#{cycle} ❌ ENTRY FAILED: {order_result.get('error', 'no fill')}")
                    with open(csv_path, "a") as f:
                        f.write(f"{now_ts()},{cycle},{side},FAILED,{entry_px},,,0,0,0,0,entry_error,0,{order_result.get('error','?')}\n")
                    time.sleep(SLEEP_SEC * 3)
                    continue

                pos = order_result
                filled_qty = pos.get("filled", qty)
                filled_fee = pos.get("fee", 0)
                avg_px = pos.get("avgPx", entry_px)

                position = {
                    "side": side,
                    "entry_px": avg_px,
                    "qty": filled_qty,
                    "highest": avg_px,
                    "lowest": avg_px,
                    "entry_ts": now_sec(),
                    "entry_cycle": cycle,
                }
                print(f"#{cycle} 📌 ENTRY {side} | px={avg_px:.1f} qty={filled_qty:.4f} fee={filled_fee:.4f} USDT")

            # 7. Trail / exit (identique ACE)
            hold_sec = 0
            exit_reason = "unknown"
            exit_px = 0.0

            while True:
                if now_sec() - t_start >= duration_sec:
                    exit_reason = "session_end"
                    exit_px = (bid_c if 'bid_c' in dir() and bid_c > 0 else position["entry_px"])
                    break
                time.sleep(POLL_SEC)
                hold_sec = now_sec() - position["entry_ts"]
                bid_c, ask_c = get_book()
                if bid_c <= 0:
                    continue

                if position["side"] == "BUY":
                    current_px = bid_c  # pour LONG, le prix de sortie est le bid
                    bps_from_entry = bps(position["entry_px"], current_px)
                    position["highest"] = max(position["highest"], current_px)

                    # Stop loss
                    if bps_from_entry <= -STOP_LOSS_BPS and hold_sec >= MIN_HOLD_SEC:
                        exit_reason = "stop_loss"
                        exit_px = current_px
                        break

                    # Take profit (seulement après MIN_HOLD)
                    if hold_sec >= MIN_HOLD_SEC:
                        gross_bps = bps_from_entry + FEE_ROUND_TRIP_BPS  # frais aller-retour
                        if gross_bps >= MIN_PROFIT_BPS and hold_sec >= MIN_HOLD_SEC:
                            exit_reason = "take_profit"
                            exit_px = current_px
                            break

                    # Trailing stop
                    if hold_sec >= MIN_HOLD_SEC:
                        trail_bps_from_high = bps(position["highest"], current_px)
                        trail_arm_triggered = bps(position["entry_px"], position["highest"]) >= TRAIL_ARM_BPS
                        if trail_arm_triggered and trail_bps_from_high <= -TRAIL_GIVEBACK_BPS:
                            exit_reason = "trailing_stop"
                            exit_px = current_px
                            break

                else:  # SELL / SHORT
                    current_px = ask_c
                    bps_from_entry = -bps(position["entry_px"], current_px)  # inversé pour SHORT
                    position["lowest"] = min(position["lowest"], current_px)

                    if bps_from_entry <= -STOP_LOSS_BPS and hold_sec >= MIN_HOLD_SEC:
                        exit_reason = "stop_loss"
                        exit_px = current_px
                        break

                    if hold_sec >= MIN_HOLD_SEC:
                        gross_bps = bps_from_entry + FEE_ROUND_TRIP_BPS
                        if gross_bps >= MIN_PROFIT_BPS:
                            exit_reason = "take_profit"
                            exit_px = current_px
                            break

                    if hold_sec >= MIN_HOLD_SEC:
                        trail_bps_from_low = -bps(position["lowest"], current_px)
                        trail_arm_triggered = -bps(position["entry_px"], position["lowest"]) >= TRAIL_ARM_BPS
                        if trail_arm_triggered and trail_bps_from_low <= -TRAIL_GIVEBACK_BPS:
                            exit_reason = "trailing_stop"
                            exit_px = current_px
                            break

                # Max hold
                if hold_sec >= MAX_HOLD_SEC:
                    exit_reason = "max_hold"
                    exit_px = current_px
                    break

            # 8. Sortie
            if paper:
                exit_fee = BUY_USDT * 0.0001  # 1 bps taker HL
                gross_pnl = (exit_px - position["entry_px"]) * position["qty"]
                if side == "SELL":
                    gross_pnl = -gross_pnl
                total_fee = filled_fee + exit_fee
                net_pnl = gross_pnl - total_fee
                filled_exit_qty = position["qty"]
            else:
                result = close_position(position["qty"])
                if result.get("error"):
                    exit_reason = "close_failed"
                    exit_px = position["entry_px"]
                else:
                    exit_fee = result.get("fee", 0)
                    exit_px = result.get("avgPx", exit_px)
                gross_pnl = (exit_px - position["entry_px"]) * position["qty"]
                if side == "SELL":
                    gross_pnl = -gross_pnl
                total_fee = filled_fee + (exit_fee if not result.get("error") else 0)
                net_pnl = gross_pnl - total_fee
                filled_exit_qty = position["qty"]

            pnl_total += net_pnl
            fee_total += total_fee
            final_bps = bps(position["entry_px"], exit_px)
            if side == "SELL":
                final_bps = -final_bps

            with open(csv_path, "a") as f:
                f.write(f"{now_ts()},{cycle},{side},{'LONG' if side == 'BUY' else 'SHORT'}," +
                        f"{position['entry_px']:.2f},{exit_px:.2f},{position['qty']:.4f}," +
                        f"{final_bps:.4f},{gross_pnl:.4f},{total_fee:.4f},{net_pnl:.4f}," +
                        f"{exit_reason},{hold_sec:.1f},paper_mode={'paper' if paper else 'testnet'}\n")

            status_symbol = "🟢" if net_pnl > 0 else "🔴"
            print(f"#{cycle} {status_symbol} EXIT {exit_reason} | hold={hold_sec:.0f}s " +
                  f"gross={gross_pnl:.2f} net={net_pnl:.2f} fee={total_fee:.4f} " +
                  f"cumul_pnl={pnl_total:.2f} cumul_fee={fee_total:.4f}")

            position = None

    except KeyboardInterrupt:
        print("\n⏹️ Interrompu par l'utilisateur.")

    # Résumé
    elapsed = now_sec() - t_start
    print(f"\n=== SESSION TERMINÉE | {now_ts()} | {elapsed:.0f}s ===")
    print(f"Cycles: {cycle} | Fills: {cycle - skip_count} | Skips: {skip_count}")
    print(f"PnL total: {pnl_total:.2f} USDT | Frais: {fee_total:.4f} USDT")
    print(f"CSV: {csv_path}")

    return {"cycles": cycle, "fills": cycle - skip_count, "skips": skip_count,
            "pnl": pnl_total, "fees": fee_total, "csv": str(csv_path)}

# ─── Main ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ACE→HL harnais comparatif")
    parser.add_argument("--duration", default="00:10:00", help="Durée HH:MM:SS (défaut 10min test)")
    parser.add_argument("--paper", action="store_true", help="Mode simulation (pas d'ordres)")
    parser.add_argument("--verbose", action="store_true", help="SKIPs détaillés")
    args = parser.parse_args()

    # Parse duration
    dur = args.duration
    if ":" in dur:
        h, m, s = dur.split(":")
        duration_sec = int(h) * 3600 + int(m) * 60 + int(s)
    else:
        duration_sec = int(dur)

    if not (ACCOUNT and PRIVATE_KEY):
        print("⚠️ Pas de wallet HL détecté — bascule en mode PAPER forcé.")
        args.paper = True

    result = run_loop(duration_sec, paper=args.paper, verbose=args.verbose)
    print(json.dumps(result, indent=2))
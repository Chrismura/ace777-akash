#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
diag_10_trades.py — Run diagnostic rayon X
==========================================
10 trades Binance testnet, même logique ACE, vérification ABSOLUE à chaque étape.
Compare le PnL CSV vs PnL réel (balance snapshot).

Usage:
  python3 diag_10_trades.py
  python3 diag_10_trades.py --trades 20
"""

import os, sys, json, time, hmac, hashlib, csv, ssl, urllib.request
from datetime import datetime, timezone
from pathlib import Path

# ─── Config (identique ACE baseline) ──────────────────────────────────────────
BASE_URL = os.environ.get("BASE_URL", os.environ.get("BINANCE_BASE_URL",
    "https://testnet.binancefuture.com"))
API_KEY = os.environ.get("BINANCE_API_KEY", "")
API_SECRET = os.environ.get("BINANCE_API_SECRET", "")
SYMBOL = "BTCUSDT"
LEVERAGE = 5
BUY_USDT = 200.0
SLEEP_SEC = 1.0
POLL_SEC = 0.5

# Radar (identique ACE, mais plus laxiste pour forcer trades test)
RADAR_MIN_MOM_BPS = 0.001
RADAR_MIN_CONF = 0.20
RADAR_MAX_SPREAD_BPS = 15.0
RADAR_DIR_BPS = 0.05

# Sortie (identique ACE)
MIN_PROFIT_BPS = 15.0
FEE_ROUND_TRIP_BPS = 8.0  # Binance: 0.04% × 2 = 8 bps
STOP_LOSS_BPS = 10.0
MAX_HOLD_SEC = 150.0
MIN_HOLD_SEC = 15.0
TRAIL_ARM_BPS = 5.0
TRAIL_GIVEBACK_BPS = 3.0

# SSL
_CTX = ssl.create_default_context()
_CTX.check_hostname = False
_CTX.verify_mode = ssl.CERT_NONE

# ─── Binance API ──────────────────────────────────────────────────────────────
def _sign(qs):
    return hmac.new(API_SECRET.encode(), qs.encode(), hashlib.sha256).hexdigest()

def _private_get(path, extra=""):
    ts = int(time.time() * 1000)
    qs = f"{extra}&timestamp={ts}&recvWindow=60000" if extra else f"timestamp={ts}&recvWindow=60000"
    sig = _sign(qs)
    url = f"{BASE_URL}{path}?{qs}&signature={sig}"
    req = urllib.request.Request(url, headers={"X-MBX-APIKEY": API_KEY})
    with urllib.request.urlopen(req, timeout=15, context=_CTX) as r:
        return json.loads(r.read())

def _private_post(path, body):
    ts = int(time.time() * 1000)
    body["timestamp"] = ts
    body["recvWindow"] = 60000
    qs = "&".join(f"{k}={v}" for k, v in sorted(body.items()))
    sig = _sign(qs)
    url = f"{BASE_URL}{path}?{qs}&signature={sig}"
    req = urllib.request.Request(url, data=b"", method="POST",
        headers={"X-MBX-APIKEY": API_KEY})
    with urllib.request.urlopen(req, timeout=15, context=_CTX) as r:
        return json.loads(r.read())

def get_price():
    """Last price via public ticker."""
    url = f"{BASE_URL}/fapi/v1/ticker/price?symbol={SYMBOL}"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=5, context=_CTX) as r:
        return float(json.loads(r.read())["price"])

def get_balance():
    """USDT balance (wallet + unrealized PnL)."""
    data = _private_get("/fapi/v2/balance")
    for asset in data:
        if asset["asset"] == "USDT":
            return {
                "balance": float(asset["balance"]),
                "available": float(asset["availableBalance"]),
                "unrealized_pnl": float(asset.get("crossUnPnl", 0)),
                "total_equity": float(asset["balance"]) + float(asset.get("crossUnPnl", 0)),
            }
    return None

def get_position():
    """Current BTCUSDT position."""
    data = _private_get("/fapi/v2/positionRisk", f"symbol={SYMBOL}")
    if isinstance(data, list):
        for p in data:
            if p["symbol"] == SYMBOL:
                return {
                    "qty": float(p["positionAmt"]),
                    "entry": float(p["entryPrice"]),
                    "unrealized_pnl": float(p["unRealizedProfit"]),
                    "leverage": int(p["leverage"]),
                    "side": "LONG" if float(p["positionAmt"]) > 0 else "SHORT" if float(p["positionAmt"]) < 0 else "NONE",
                }
    return {"qty": 0, "entry": 0, "unrealized_pnl": 0, "leverage": 0, "side": "NONE"}

def get_spread():
    """Bid/ask via orderbook depth."""
    url = f"{BASE_URL}/fapi/v1/depth?symbol={SYMBOL}&limit=5"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=5, context=_CTX) as r:
        data = json.loads(r.read())
    best_bid = float(data["bids"][0][0])
    best_ask = float(data["asks"][0][0])
    return best_bid, best_ask

def bps(p1, p2):
    if p1 <= 0:
        return 0.0
    return (p2 - p1) / p1 * 10000.0

def floor_step_qty(qty, step=0.001):
    s = max(step, 0.001)
    return (qty // s) * s

def now_ts():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# ─── Audit Trail ──────────────────────────────────────────────────────────────
class AuditTrail:
    def __init__(self):
        self.events = []
        self.balance_before = None
        self.balance_after = None
        self.csv_trades = []

    def log(self, event_type, detail, balance=None):
        entry = {
            "ts": now_ts(),
            "type": event_type,
            "detail": detail,
            "balance": balance,
        }
        self.events.append(entry)
        icon = {"BALANCE": "💰", "ENTRY": "📌", "EXIT": "📤", "VERIFY": "🔍",
                "MISMATCH": "🔴", "OK": "✅", "PHANTOM": "👻", "INFO": "ℹ️"}.get(event_type, "•")
        bal_str = f" bal={balance['total_equity']:.2f}" if balance else ""
        print(f"  {icon} [{event_type}] {detail}{bal_str}")

    def report(self):
        print("\n" + "=" * 60)
        print("📊 RAPPORT DIAGNOSTIC — RAYON X")
        print("=" * 60)

        if self.balance_before and self.balance_after:
            real_pnl = self.balance_after["total_equity"] - self.balance_before["total_equity"]
            print(f"\n  Balance avant:  {self.balance_before['total_equity']:.4f} USDT")
            print(f"  Balance après:  {self.balance_after['total_equity']:.4f} USDT")
            print(f"  PnL RÉEL:       {real_pnl:+.4f} USDT")
        else:
            real_pnl = 0
            print("  ⚠️ Pas de snapshots balance")

        # Compare with CSV
        csv_pnl = sum(t.get("pnl", 0) for t in self.csv_trades)
        csv_fees = sum(t.get("fee", 0) for t in self.csv_trades)

        print(f"\n  PnL CSV:        {csv_pnl:+.4f} USDT")
        print(f"  Frais CSV:      {csv_fees:+.4f} USDT")
        print(f"  Différence:     {real_pnl - csv_pnl:+.4f} USDT")

        # Verify each trade
        mismatches = [e for e in self.events if e["type"] == "MISMATCH"]
        ghosts = [e for e in self.events if e["type"] == "PHANTOM"]

        if mismatches:
            print(f"\n  🔴 {len(mismatches)} MISMATCH(es) détecté(s):")
            for m in mismatches:
                print(f"     {m['detail']}")

        if ghosts:
            print(f"\n  👻 {len(ghosts)} PHANTOM(s) détecté(s):")
            for g in ghosts:
                print(f"     {g['detail']}")

        if not mismatches and not ghosts:
            print(f"\n  ✅ Aucun mismatch ni phantom détecté")

        print(f"\n  Trades CSV:     {len(self.csv_trades)}")
        print(f"  Événements:     {len(self.events)}")
        print("=" * 60)

        return {"real_pnl": real_pnl, "csv_pnl": csv_pnl, "diff": real_pnl - csv_pnl,
                "mismatches": len(mismatches), "ghosts": len(ghosts)}

# ─── Main Loop ────────────────────────────────────────────────────────────────
def run(target_trades=10):
    audit = AuditTrail()

    print(f"{'=' * 60}")
    print(f"🔬 DIAG RAYON X — {target_trades} trades — {SYMBOL}")
    print(f"   Balance: {BASE_URL}")
    print(f"   Time: {now_ts()}")
    print(f"{'=' * 60}")

    # ─── CHECK 0: Préflight ───────────────────────────────────────────────────
    print("\n── CHECK 0: Préflight ──")
    pos = get_position()
    if pos["qty"] != 0:
        print(f"  ⚠️ Position existante: {pos['side']} {pos['qty']} @ {pos['entry']} (unPnl={pos['unrealized_pnl']:.4f})")
        print(f"  → Fermeture forcée avant de commencer...")
        close_side = "SELL" if pos["qty"] > 0 else "BUY"
        close_pos_side = "LONG" if pos["qty"] > 0 else "SHORT"
        try:
            _private_post("/fapi/v1/order", {
                "symbol": SYMBOL, "side": close_side, "type": "MARKET",
                "quantity": str(abs(pos["qty"])), "positionSide": close_pos_side
            })
            time.sleep(1)
            pos = get_position()
            audit.log("INFO", f"Position fermée: reste {pos['qty']}")
        except Exception as e:
            print(f"  ❌ Fermeture impossible: {e}")
            return audit.report()

    # Set leverage
    try:
        _private_post("/fapi/v1/leverage", {"symbol": SYMBOL, "leverage": LEVERAGE})
        audit.log("INFO", f"Leverage set: x{LEVERAGE}")
    except:
        pass

    # ─── CHECK 1: Balance initiale ────────────────────────────────────────────
    print("\n── CHECK 1: Balance initiale ──")
    audit.balance_before = get_balance()
    audit.log("BALANCE", f"Snapshot initial", audit.balance_before)

    # ─── CHECK 2: Test prix ───────────────────────────────────────────────────
    print("\n── CHECK 2: Test flux prix ──")
    prices = []
    for i in range(3):
        p = get_price()
        prices.append(p)
        print(f"  Prix #{i}: {p:.1f}")
        time.sleep(1)
    mom_bps = bps(prices[0], prices[-1]) if len(prices) >= 2 else 0
    print(f"  Momentum 3s: {mom_bps:.4f} bps")

    bid, ask = get_spread()
    spread_bps = (ask - bid) / ask * 10000 if ask > 0 else 0
    print(f"  Spread: {bid:.1f} / {ask:.1f} = {spread_bps:.1f} bps")

    if spread_bps > RADAR_MAX_SPREAD_BPS:
        print(f"  ⚠️ Spread trop large ({spread_bps:.1f} > {RADAR_MAX_SPREAD_BPS}) — attendra un spread sain")

    # ─── CHECK 3: Boucle de trades ────────────────────────────────────────────
    csv_path = Path(f"DIAG_10_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")
    csv_fields = ["ts", "cycle", "side", "status", "entryPrice", "exitPrice", "qty",
                  "bps", "pnl", "fee", "pnlNet", "exitReason", "holdSec",
                  "balance_before", "balance_after", "pos_verified"]

    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=csv_fields)
        writer.writeheader()

    cycle = 0
    fills = 0
    csv_data = []

    print(f"\n── CHECK 3: Boucle trades (0/{target_trades}) ──")

    while fills < target_trades:
        cycle += 1

        # Prix + spread
        bid, ask = get_spread()
        if bid <= 0 or ask <= 0:
            time.sleep(SLEEP_SEC)
            continue
        spread_bps = (ask - bid) / ask * 10000

        # Momentum
        p1 = get_price()
        time.sleep(1.0)
        p2 = get_price()
        mom = bps(p1, p2)

        # Radar
        abs_mom = abs(mom)
        if abs_mom < RADAR_MIN_MOM_BPS and abs_mom > 0:
            conf = min(1.0, abs_mom / RADAR_DIR_BPS)
        elif abs_mom == 0 and spread_bps <= RADAR_MAX_SPREAD_BPS:
            conf = 0.35
        else:
            conf = min(1.0, abs_mom / RADAR_DIR_BPS)

        allow = (spread_bps <= RADAR_MAX_SPREAD_BPS and
                 (abs_mom >= RADAR_MIN_MOM_BPS or conf >= RADAR_MIN_CONF))

        if not allow:
            print(f"  #{cycle} SKIP | spread={spread_bps:.1f} mom={mom:.4f} conf={conf:.4f}")
            time.sleep(SLEEP_SEC)
            continue

        # Direction
        if mom >= RADAR_DIR_BPS:
            direction = "LONG"
        elif mom <= -RADAR_DIR_BPS:
            direction = "SHORT"
        else:
            direction = "LONG" if mom >= 0 else "SHORT"  # force direction pour le test

        # ─── ENTRY ────────────────────────────────────────────────────────────
        entry_px = ask if direction == "LONG" else bid
        qty = floor_step_qty(BUY_USDT / entry_px, 0.001)
        bal_before_entry = get_balance()

        side = "BUY" if direction == "LONG" else "SELL"
        pos_side = "LONG" if direction == "LONG" else "SHORT"
        close_side = "SELL" if direction == "LONG" else "BUY"

        audit.log("ENTRY", f"#{cycle} {side} qty={qty:.4f} @ ~{entry_px:.1f}", bal_before_entry)

        try:
            result = _private_post("/fapi/v1/order", {
                "symbol": SYMBOL, "side": side, "type": "MARKET",
                "quantity": str(qty), "positionSide": pos_side
            })
            fill_px = float(result.get("avgPrice", result.get("price", entry_px)))
            fill_qty = float(result.get("executedQty", qty))
            fill_fee = float(result.get("commission", 0))
            order_status = result.get("status", "?")
        except Exception as e:
            audit.log("MISMATCH", f"#{cycle} ORDER FAILED: {e}")
            time.sleep(SLEEP_SEC * 3)
            continue

        # ─── VÉRIFICATION 1: Position existe ? ────────────────────────────────
        time.sleep(0.5)
        pos = get_position()
        if pos["qty"] == 0:
            audit.log("PHANTOM", f"#{cycle} ENTRY ghost: ordre FILLED mais position vide !")
            row = {"ts": now_ts(), "cycle": cycle, "side": side, "status": "PHANTOM_ENTRY",
                   "entryPrice": fill_px, "exitPrice": 0, "qty": fill_qty,
                   "bps": 0, "pnl": 0, "fee": fill_fee, "pnlNet": -fill_fee,
                   "exitReason": "phantom_entry", "holdSec": 0,
                   "balance_before": bal_before_entry["total_equity"],
                   "balance_after": 0, "pos_verified": "FAIL"}
            csv_data.append(row)
            fills += 1
            time.sleep(SLEEP_SEC)
            continue

        # Vérifier qty
        qty_diff = abs(pos["qty"] - fill_qty)
        if qty_diff > 0.0001:
            audit.log("MISMATCH", f"#{cycle} QTY mismatch: fill={fill_qty:.4f} position={pos['qty']:.4f} diff={qty_diff:.4f}")
        else:
            audit.log("VERIFY", f"#{cycle} Position OK: {pos['side']} {pos['qty']:.4f} @ {pos['entry']:.1f}")

        # ─── TRAILING + EXIT ──────────────────────────────────────────────────
        entry_time = time.time()
        highest = fill_px
        lowest = fill_px
        exit_reason = "unknown"
        exit_px = 0.0
        hold_sec = 0

        while True:
            if time.time() - entry_time >= MAX_HOLD_SEC:
                exit_reason = "max_hold"
                exit_px = get_price()
                break
            time.sleep(POLL_SEC)
            hold_sec = time.time() - entry_time
            current_px = get_price()

            if direction == "LONG":
                bps_from = bps(fill_px, current_px)
                highest = max(highest, current_px)
                if bps_from <= -STOP_LOSS_BPS and hold_sec >= MIN_HOLD_SEC:
                    exit_reason = "stop_loss"; exit_px = current_px; break
                if hold_sec >= MIN_HOLD_SEC:
                    gross = bps_from + FEE_ROUND_TRIP_BPS
                    if gross >= MIN_PROFIT_BPS:
                        exit_reason = "take_profit"; exit_px = current_px; break
                if hold_sec >= MIN_HOLD_SEC:
                    trail_from_high = bps(highest, current_px)
                    arm = bps(fill_px, highest) >= TRAIL_ARM_BPS
                    if arm and trail_from_high <= -TRAIL_GIVEBACK_BPS:
                        exit_reason = "trailing_stop"; exit_px = current_px; break
            else:
                bps_from = -bps(fill_px, current_px)
                lowest = min(lowest, current_px)
                if bps_from <= -STOP_LOSS_BPS and hold_sec >= MIN_HOLD_SEC:
                    exit_reason = "stop_loss"; exit_px = current_px; break
                if hold_sec >= MIN_HOLD_SEC:
                    gross = bps_from + FEE_ROUND_TRIP_BPS
                    if gross >= MIN_PROFIT_BPS:
                        exit_reason = "take_profit"; exit_px = current_px; break
                if hold_sec >= MIN_HOLD_SEC:
                    trail_from_low = -bps(lowest, current_px)
                    arm = -bps(fill_px, lowest) >= TRAIL_ARM_BPS
                    if arm and trail_from_low <= -TRAIL_GIVEBACK_BPS:
                        exit_reason = "trailing_stop"; exit_px = current_px; break

        # ─── EXIT ─────────────────────────────────────────────────────────────
        try:
            exit_result = _private_post("/fapi/v1/order", {
                "symbol": SYMBOL, "side": close_side, "type": "MARKET",
                "quantity": str(fill_qty), "positionSide": pos_side
            })
            exit_px_actual = float(exit_result.get("avgPrice", exit_result.get("price", exit_px)))
            exit_fee = float(exit_result.get("commission", 0))
        except Exception as e:
            audit.log("MISMATCH", f"#{cycle} EXIT FAILED: {e}")
            exit_px_actual = exit_px
            exit_fee = 0

        # ─── VÉRIFICATION 2: Position fermée ? ────────────────────────────────
        time.sleep(0.5)
        pos_after = get_position()
        if pos_after["qty"] != 0:
            audit.log("PHANTOM", f"#{cycle} EXIT ghost: ordre de sortie envoyé mais position encore {pos_after['side']} {pos_after['qty']:.4f} !")
            pos_verified = "FAIL"
        else:
            audit.log("VERIFY", f"#{cycle} Position fermée OK")
            pos_verified = "OK"

        # ─── CALCUL PNL ───────────────────────────────────────────────────────
        if direction == "LONG":
            raw_pnl = (exit_px_actual - fill_px) * fill_qty
        else:
            raw_pnl = (fill_px - exit_px_actual) * fill_qty
        total_fee = fill_fee + exit_fee
        net_pnl = raw_pnl - total_fee
        actual_bps = bps(fill_px, exit_px_actual) if direction == "LONG" else -bps(fill_px, exit_px_actual)

        bal_after = get_balance()
        real_pnl_so_far = bal_after["total_equity"] - audit.balance_before["total_equity"]

        # Logger
        pnl_icon = "🟢" if net_pnl > 0 else "🔴"
        audit.log("EXIT", f"#{cycle} {pnl_icon} {exit_reason} | hold={hold_sec:.0f}s "
                  f"raw={raw_pnl:.4f} fee={total_fee:.4f} net={net_pnl:.4f} | "
                  f"réel cumul={real_pnl_so_far:+.4f}", bal_after)

        row = {"ts": now_ts(), "cycle": cycle, "side": side, "status": "FILLED",
               "entryPrice": round(fill_px, 2), "exitPrice": round(exit_px_actual, 2),
               "qty": round(fill_qty, 6), "bps": round(actual_bps, 4),
               "pnl": round(raw_pnl, 6), "fee": round(total_fee, 6),
               "pnlNet": round(net_pnl, 6), "exitReason": exit_reason,
               "holdSec": round(hold_sec, 1),
               "balance_before": round(bal_before_entry["total_equity"], 4),
               "balance_after": round(bal_after["total_equity"], 4),
               "pos_verified": pos_verified}
        csv_data.append(row)
        audit.csv_trades.append({"pnl": raw_pnl, "fee": total_fee, "net": net_pnl})
        fills += 1

        # ─── VÉRIFICATION 3: Balance matche ? ─────────────────────────────────
        balance_change = bal_after["total_equity"] - bal_before_entry["total_equity"]
        expected_change = net_pnl
        diff = abs(balance_change - expected_change)
        if diff > 0.10:  # plus de 10 centimes de différence
            audit.log("MISMATCH", f"#{cycle} BALANCE MISMATCH: attendu={expected_change:+.4f} "
                      f"réel={balance_change:+.4f} diff={diff:.4f}")

        print(f"  → {fills}/{target_trades} trades")
        time.sleep(SLEEP_SEC)

    # ─── ÉCRITURE CSV ─────────────────────────────────────────────────────────
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=csv_fields)
        writer.writeheader()
        for row in csv_data:
            writer.writerow(row)
    print(f"\n  📄 CSV: {csv_path}")

    # ─── CHECK 4: Balance finale ──────────────────────────────────────────────
    print("\n── CHECK 4: Balance finale ──")
    audit.balance_after = get_balance()
    audit.log("BALANCE", f"Snapshot final", audit.balance_after)

    # Vérifier qu'aucune position ne reste
    pos_final = get_position()
    if pos_final["qty"] != 0:
        audit.log("PHANTOM", f"Position orpheline en fin de run: {pos_final['side']} {pos_final['qty']}")
    else:
        audit.log("OK", "Zéro position en fin de run")

    return audit.report()

# ─── Main ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Diagnostic rayon X — 10 trades")
    parser.add_argument("--trades", type=int, default=10, help="Nombre de trades (défaut 10)")
    args = parser.parse_args()

    if not API_KEY or not API_SECRET:
        print("❌ Clés Binance manquantes. Source ~/.binance_testnet.env")
        sys.exit(1)

    run(args.trades)
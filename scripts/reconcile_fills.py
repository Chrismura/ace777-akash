#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
reconcile_fills.py — Chasseur de ghost fills
=============================================
Compare chaque fill CSV ACE à la réalité Binance (trades + positions).
Détecte les « matched » fantômes (CSV ≠ exchange).

Usage:
  python3 reconcile_fills.py runs/MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv
  python3 reconcile_fills.py --all runs/MASTER_VORTEX_V2_COLLAB_4H

SÉCURITÉ: lecture seule — aucun ordre, aucun trade, aucune position.
"""

import os, sys, json, csv, time, hmac, hashlib, urllib.request, ssl
from datetime import datetime, timezone, timedelta
from collections import defaultdict
from pathlib import Path

# ─── Config ────────────────────────────────────────────────────────────────────
BINANCE_BASE = os.environ.get("BASE_URL", os.environ.get("BINANCE_BASE_URL",
    "https://testnet.binancefuture.com"))
API_KEY = os.environ.get("BINANCE_API_KEY", "")
API_SECRET = os.environ.get("BINANCE_API_SECRET", "")
SYMBOL = "BTCUSDT"

# Tolérance: un trade réel doit être dans cette fenêtre (secondes) du fill CSV
TIME_WINDOW_SEC = 120
# Tolérance prix: le prix Binance doit être dans ±1% du prix CSV
PRICE_TOLERANCE_PCT = 1.0

# ─── SSL ───────────────────────────────────────────────────────────────────────
_SSL_CTX = ssl.create_default_context()
_SSL_CTX.check_hostname = False
_SSL_CTX.verify_mode = ssl.CERT_NONE

# ─── Binance API (lecture seule) ───────────────────────────────────────────────
def _signed_get(path: str, extra_qs: str = "") -> dict:
    ts = int(time.time() * 1000)
    qs = f"{extra_qs}&timestamp={ts}&recvWindow=60000" if extra_qs else f"timestamp={ts}&recvWindow=60000"
    sig = hmac.new(API_SECRET.encode(), qs.encode(), hashlib.sha256).hexdigest()
    url = f"{BINANCE_BASE}{path}?{qs}&signature={sig}"
    req = urllib.request.Request(url, headers={"X-MBX-APIKEY": API_KEY})
    with urllib.request.urlopen(req, timeout=15, context=_SSL_CTX) as r:
        return json.loads(r.read().decode())

def get_positions() -> list:
    """Retourne les positions ouvertes sur BTCUSDT."""
    data = _signed_get("/fapi/v2/positionRisk", f"symbol={SYMBOL}")
    if isinstance(data, list):
        return [p for p in data if float(p.get("positionAmt", 0)) != 0]
    return []

def get_trades(start_ms: int, end_ms: int) -> list:
    """Récupère tous les trades entre deux timestamps (ms)."""
    all_trades = []
    page = 0
    max_pages = 10
    while page < max_pages:
        qs = f"symbol={SYMBOL}&startTime={start_ms}&endTime={end_ms}&limit=500"
        try:
            data = _signed_get("/fapi/v1/userTrades", qs)
        except Exception as e:
            print(f"  ⚠️  Erreur userTrades page {page}: {e}", flush=True)
            break
        if not isinstance(data, list) or not data:
            break
        all_trades.extend(data)
        # Repartir depuis le dernier trade pour la page suivante
        start_ms = data[-1].get("time", start_ms) + 1
        if len(data) < 500:
            break
        page += 1
        time.sleep(0.3)
    return all_trades

# ─── Parsing CSV ───────────────────────────────────────────────────────────────
def parse_csv(csv_path: str) -> list:
    """Extrait tous les fills (status=FILLED) d'un CSV ACE."""
    fills = []
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("status") == "FILLED":
                fills.append(row)
    return fills

def csv_timestamp_ms(row: dict) -> int:
    """Convertit le timestamp ISO du CSV en millisecondes Unix."""
    try:
        dt = datetime.strptime(row["ts"], "%Y-%m-%dT%H:%M:%SZ")
        return int(dt.replace(tzinfo=timezone.utc).timestamp() * 1000)
    except:
        return 0

# ─── Matching ──────────────────────────────────────────────────────────────────
def price_match(csv_px: float, trade_px: float) -> bool:
    """Vérifie que le prix du trade est proche du prix CSV."""
    if csv_px <= 0 or trade_px <= 0:
        return False
    pct = abs(csv_px - trade_px) / csv_px * 100
    return pct <= PRICE_TOLERANCE_PCT

def reconcile_single_fill(fill, trades_by_minute, now_ms, known_trades_empty):
    """Reconcile un seul fill. Retourne (status, detail)."""
    csv_ts = csv_timestamp_ms(fill)
    fill_pnl = float(fill.get("pnlNet", fill.get("pnl", 0)))
    fill_cycle = fill.get("cycle", "?")
    age_days = (now_ms - csv_ts) / 8_6400_000

    # Si le fill est trop vieux (>7j) et qu'aucun trade n'a été trouvé pour cette période
    if age_days > 7:
        if known_trades_empty:
            print(f"  ⚪ cycle#{fill_cycle} INCONNU | données trop anciennes ({age_days:.0f}j) | PnL CSV={fill_pnl:.4f}", flush=True)
            return ("INCONNU", fill_pnl)

    # Si on a des trades, chercher un match
    entry_trade = find_matching_trade(fill, trades_by_minute, "ENTRY")
    exit_trade = find_matching_trade(fill, trades_by_minute, "EXIT")

    if entry_trade and exit_trade:
        print(f"  ✅ cycle#{fill_cycle} OK | PnL={fill_pnl:.4f}", flush=True)
        return ("REAL", fill_pnl)
    elif entry_trade and not exit_trade:
        print(f"  👻 cycle#{fill_cycle} GHOST EXIT | entrée réelle, sortie fantôme | PnL CSV={fill_pnl:.4f}", flush=True)
        return ("GHOST_EXIT", fill_pnl)
    elif not entry_trade and exit_trade:
        print(f"  👻 cycle#{fill_cycle} GHOST ENTRY | sortie réelle, entrée fantôme | PnL CSV={fill_pnl:.4f}", flush=True)
        return ("GHOST_ENTRY", fill_pnl)
    else:
        # Pas de trades du tout — on ne sait pas si c'est ghost ou juste trop vieux
        if age_days <= 2 and not known_trades_empty:
            print(f"  👻 cycle#{fill_cycle} GHOST FULL | récent ({age_days:.1f}j), ni entrée ni sortie | PnL CSV={fill_pnl:.4f}", flush=True)
            return ("GHOST_FULL", fill_pnl)
        else:
            print(f"  ⚪ cycle#{fill_cycle} INCONNU | pas de trades Binance sur cette période | PnL CSV={fill_pnl:.4f}", flush=True)
            return ("INCONNU", fill_pnl)


def find_matching_trade(fill, trades, trade_type):
    """
    Cherche un trade qui match le fill CSV.
    trade_type: "ENTRY" (cherche le sens du fill, même sens que side)
                "EXIT"  (cherche le sens OPPOSÉ)
    """
    csv_ts = csv_timestamp_ms(fill)
    csv_px = float(fill.get("entryPrice", 0)) if trade_type == "ENTRY" else float(fill.get("exitPrice", 0))
    csv_qty = abs(float(fill.get("qty", 0)))
    csv_side = fill.get("side", "").upper()

    if trade_type == "ENTRY":
        target_side = "BUY" if csv_side == "BUY" else "SELL"
    else:
        target_side = "SELL" if csv_side == "BUY" else "BUY"  # sens opposé

    candidates = []
    for t in trades:
        t_ts = t.get("time", 0)
        if abs(t_ts - csv_ts) > TIME_WINDOW_SEC * 1000:
            continue
        t_side = "BUY" if t.get("buyer", False) else "SELL"
        if t_side != target_side:
            continue
        t_px = float(t.get("price", 0))
        if price_match(csv_px, t_px):
            t_qty = abs(float(t.get("qty", 0)))
            candidates.append((abs(t_qty - csv_qty), t))

    if candidates:
        candidates.sort(key=lambda x: x[0])  # plus proche en qty
        return candidates[0][1]
    return None

# ─── Rapport ───────────────────────────────────────────────────────────────────
def reconcile(csv_path: str) -> dict:
    """Lance la reconciliation complète sur un CSV."""
    fills = parse_csv(csv_path)
    if not fills:
        return {"csv": csv_path, "fills": 0, "ghosts": 0, "pnl_correction": 0, "details": "Aucun fill"}

    # Fenêtre temporelle : toutes les timestamps du CSV, avec padding 1h
    all_ts = sorted([csv_timestamp_ms(f) for f in fills if csv_timestamp_ms(f) > 0])
    if not all_ts:
        return {"csv": csv_path, "fills": len(fills), "ghosts": len(fills), "matched": 0, "details": "Timestamps invalides"}
    first_ts = all_ts[0]
    last_ts = all_ts[-1]
    trade_start = first_ts - 3600_000
    trade_end = last_ts + 3600_000

    # Sécurité: trade_start < trade_end
    if trade_start >= trade_end:
        trade_start, trade_end = trade_end, trade_start + 3600_000

    print(f"  📡 Récupération trades Binance {symbol_ts(trade_start)} → {symbol_ts(trade_end)}...", flush=True)
    trades = get_trades(trade_start, trade_end)
    print(f"  📊 {len(trades)} trades Binance, {len(fills)} fills CSV", flush=True)

    ghosts = []
    matched = []
    unknown = []
    now_ms = int(time.time() * 1000)
    known_trades_empty = len(trades) == 0

    for i, fill in enumerate(fills):
        status, fill_pnl = reconcile_single_fill(fill, trades, now_ms, known_trades_empty)
        fill_cycle = fill.get("cycle", "?")
        if status == "REAL":
            matched.append(fill)
        elif status == "INCONNU":
            unknown.append(fill)
        else:
            ghosts.append(fill)

    ghost_pnl = sum(float(g.get("pnlNet", g.get("pnl", 0))) for g in ghosts)
    real_pnl = sum(float(m.get("pnlNet", m.get("pnl", 0))) for m in matched)
    csv_pnl = ghost_pnl + real_pnl

    # Vérifier aussi les positions restantes
    positions = get_positions()
    orphan_pnl = 0.0
    if positions:
        print(f"  ⚠️  {len(positions)} position(s) encore ouverte(s):", flush=True)
        for p in positions:
            upnl = float(p.get("unRealizedProfit", 0))
            orphan_pnl += upnl
            print(f"     {p['symbol']} {p['positionAmt']} @ {p['entryPrice']} | unPnl={upnl} | lev={p['leverage']}", flush=True)

    return {
        "csv": csv_path,
        "fills": len(fills),
        "matched": len(matched),
        "ghosts": len(ghosts),
        "ghost_details": [{"cycle": g["cycle"], "pnl_csv": float(g.get("pnlNet", g.get("pnl", 0)))} for g in ghosts],
        "csv_pnl_total": round(csv_pnl, 4),
        "real_pnl": round(real_pnl, 4),
        "ghost_pnl_removed": round(ghost_pnl, 4),
        "orphan_positions": len(positions),
        "orphan_unpnl": round(orphan_pnl, 4),
        "corrected_pnl": round(real_pnl + orphan_pnl, 4),
    }

def symbol_ts(ms: int) -> str:
    if ms <= 0:
        return "?"
    return datetime.fromtimestamp(ms/1000, tz=timezone.utc).strftime("%H:%M")

# ─── Main ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Reconcile CSV fills vs Binance reality")
    parser.add_argument("csv", nargs="+", help="CSV file(s) or directory")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    if not API_KEY or not API_SECRET:
        print("❌ Clés Binance manquantes. Source ~/.binance_testnet.env d'abord.")
        sys.exit(1)

    csv_files = []
    for path in args.csv:
        p = Path(path)
        if p.is_dir():
            csv_files.extend(sorted(p.glob("*.csv")))
        elif p.suffix == ".csv":
            csv_files.append(p)

    if not csv_files:
        print("❌ Aucun CSV trouvé.")
        sys.exit(1)

    results = []
    for cf in csv_files:
        print(f"\n=== 🔍 Reconciliation: {cf} ===", flush=True)
        r = reconcile(str(cf))
        results.append(r)

        print(f"\n  📋 Résumé {cf.name}:")
        print(f"     Fills CSV:     {r['fills']}")
        print(f"     ✅ Réels:       {r['matched']}")
        print(f"     👻 Fantômes:    {r['ghosts']}")
        print(f"     PnL CSV:       {r['csv_pnl_total']:+.4f} USDT")
        print(f"     PnL réel:      {r['real_pnl']:+.4f} USDT")
        print(f"     PnL corrigé:   {r['corrected_pnl']:+.4f} USDT")

    # Résumé global
    total_fills = sum(r["fills"] for r in results)
    total_ghosts = sum(r["ghosts"] for r in results)
    total_ghost_pnl = sum(r["ghost_pnl_removed"] for r in results)
    total_corrected = sum(r["corrected_pnl"] for r in results)

    print(f"\n{'='*60}")
    print(f"🏁 TOTAL: {total_fills} fills, {total_ghosts} fantômes")
    print(f"   PnL fantômes supprimé: {total_ghost_pnl:+.4f} USDT")
    print(f"   PnL corrigé:           {total_corrected:+.4f} USDT")
    print(f"{'='*60}")

    if args.json:
        print(json.dumps(results, indent=2))
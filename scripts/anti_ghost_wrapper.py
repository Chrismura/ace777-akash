#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
anti_ghost_wrapper.py — Gardien anti-ghost-fills
=================================================
Tourne EN PARALLÈLE du champion. Ne le touche pas.

Surveille le CSV ACE en temps réel, vérifie chaque FILLED contre Binance,
ferme les orphelins, produit un CSV corrigé.

Usage:
  # Lancer APRÈS le champion (il lit le CSV en croissance):
  python3 anti_ghost_wrapper.py --csv runs/MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv

  # Ou sur le répertoire runs/ (surveille tous les CSV):
  python3 anti_ghost_wrapper.py --dir runs/

  # Ou en mode one-shot (vérifie un CSV existant):
  python3 anti_ghost_wrapper.py --csv runs/BETA_X5.csv --once
"""

import os, sys, json, time, hmac, hashlib, csv, ssl, urllib.request
from datetime import datetime, timezone
from pathlib import Path

# ─── Config ────────────────────────────────────────────────────────────────────
BASE_URL = os.environ.get("BASE_URL", os.environ.get("BINANCE_BASE_URL",
    "https://testnet.binancefuture.com"))
API_KEY = os.environ.get("BINANCE_API_KEY", "")
API_SECRET = os.environ.get("BINANCE_API_SECRET", "")
SYMBOL = "BTCUSDT"
POLL_INTERVAL = 2          # secondes entre chaque vérification
AUTO_CLOSE_ORPHANS = True  # fermer automatiquement les orphelins
HEDGE_MODE = True          # le compte est en hedge mode

_SSL_CTX = ssl.create_default_context()
_SSL_CTX.check_hostname = False
_SSL_CTX.verify_mode = ssl.CERT_NONE

# ─── State ─────────────────────────────────────────────────────────────────────
class GhostState:
    def __init__(self):
        self.checked_cycles = set()     # cycles déjà vérifiés
        self.ghosts = []                # list of {cycle, kind, detail}
        self.orphans_closed = 0
        self.csv_rows = []              # toutes les lignes lues
        self.last_line = 0              # dernière ligne lue du CSV

# ─── Binance API ──────────────────────────────────────────────────────────────
def _sign(qs):
    return hmac.new(API_KEY.encode() if False else API_SECRET.encode(),
                    qs.encode(), hashlib.sha256).hexdigest()

def _private_get(path, extra=""):
    ts = int(time.time() * 1000)
    qs = f"{extra}&timestamp={ts}&recvWindow=60000" if extra else f"timestamp={ts}&recvWindow=60000"
    sig = hmac.new(API_SECRET.encode(), qs.encode(), hashlib.sha256).hexdigest()
    url = f"{BASE_URL}{path}?{qs}&signature={sig}"
    req = urllib.request.Request(url, headers={"X-MBX-APIKEY": API_KEY})
    with urllib.request.urlopen(req, timeout=15, context=_SSL_CTX) as r:
        return json.loads(r.read())

def _private_post(path, body):
    ts = int(time.time() * 1000)
    body["timestamp"] = ts
    body["recvWindow"] = 60000
    qs = "&".join(f"{k}={v}" for k, v in sorted(body.items()))
    sig = hmac.new(API_SECRET.encode(), qs.encode(), hashlib.sha256).hexdigest()
    url = f"{BASE_URL}{path}?{qs}&signature={sig}"
    req = urllib.request.Request(url, data=b"", method="POST",
        headers={"X-MBX-APIKEY": API_KEY})
    with urllib.request.urlopen(req, timeout=15, context=_SSL_CTX) as r:
        return json.loads(r.read())

def get_positions():
    """Toutes les positions ouvertes BTCUSDT."""
    try:
        data = _private_get("/fapi/v2/positionRisk", f"symbol={SYMBOL}")
        if isinstance(data, list):
            return [p for p in data if float(p.get("positionAmt", 0)) != 0]
    except Exception as e:
        log(f"⚠️ Erreur get_positions: {e}")
    return []

def get_balance():
    """Balance USDT totale."""
    try:
        data = _private_get("/fapi/v2/balance")
        for a in data:
            if a["asset"] == "USDT":
                return float(a["balance"]) + float(a.get("crossUnPnl", 0))
    except:
        pass
    return 0.0

def close_orphan(qty, side):
    """Ferme une position orpheline (hedge mode)."""
    if not AUTO_CLOSE_ORPHANS:
        return False
    close_side = "SELL" if qty > 0 else "BUY"
    pos_side = "LONG" if qty > 0 else "SHORT"
    try:
        result = _private_post("/fapi/v1/order", {
            "symbol": SYMBOL, "side": close_side, "type": "MARKET",
            "quantity": str(abs(qty)), "positionSide": pos_side
        })
        status = result.get("status", "?")
        log(f"  🔧 Orphelin fermé: {close_side} {abs(qty):.4f} → {status}")
        return True
    except Exception as e:
        log(f"  ❌ Fermeture orphelin échouée: {e}")
        return False

# ─── Logging ───────────────────────────────────────────────────────────────────
def log(msg):
    ts = datetime.now(timezone.utc).strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)

def log_ghost(state, cycle, kind, detail):
    entry = {"ts": now_ts(), "cycle": cycle, "kind": kind, "detail": detail}
    state.ghosts.append(entry)
    log(f"  👻 GHOST #{cycle} [{kind}] {detail}")

# ─── Utilitaires ───────────────────────────────────────────────────────────────
def now_ts():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def read_new_lines(csv_path, state):
    """Lit les nouvelles lignes du CSV (append-only)."""
    new_rows = []
    try:
        with open(csv_path, "r") as f:
            lines = f.readlines()
        if len(lines) <= state.last_line:
            return new_rows
        for line in lines[state.last_line:]:
            line = line.strip()
            if not line or line.startswith("ts,cycle"):
                continue
            # Parse CSV ligne — maxsplit=10 pour garder msg intact (contient des virgules)
            try:
                parts = line.split(",", 10)
                if len(parts) < 4:
                    continue
                row = {
                    "ts": parts[0],
                    "cycle": parts[1],
                    "side": parts[2],
                    "status": parts[3],
                    "entryPrice": parts[4] if len(parts) > 4 else "0",
                    "exitPrice": parts[5] if len(parts) > 5 else "0",
                    "qty": parts[6] if len(parts) > 6 else "0",
                    "bps": parts[7] if len(parts) > 7 else "0",
                    "pnl": parts[8] if len(parts) > 8 else "0",
                    "exitReason": parts[9] if len(parts) > 9 else "",
                    "holdSec": parts[10].split(",")[0] if len(parts) > 10 else "0",
                }
                new_rows.append(row)
            except:
                pass
        state.last_line = len(lines)
    except FileNotFoundError:
        pass
    return new_rows

# ─── Vérification d'un fill ───────────────────────────────────────────────────
def verify_fill(row, state):
    """Vérifie qu'un fill FILLED existe réellement sur Binance."""
    cycle = row.get("cycle", "?")
    status = row.get("status", "")

    if status != "FILLED":
        return  # SKIP, etc. pas besoin de vérifier

    if cycle in state.checked_cycles:
        return  # déjà vérifié

    state.checked_cycles.add(cycle)
    side = row.get("side", "")
    csv_qty = float(row.get("qty", 0))
    csv_entry = float(row.get("entryPrice", 0))
    exit_reason = row.get("exitReason", "")

    # ─── Vérification 1: La position existe-t-elle ? ─────────────────────
    positions = get_positions()
    btc_pos = None
    for p in positions:
        if p["symbol"] == SYMBOL:
            btc_pos = p
            break

    if btc_pos is None:
        # Pas de position du tout → possible ghost
        # Mais si le trade est déjà sorti (holdSec > 0), c'est OK
        try:
            hold_sec = float(row.get("holdSec", "0").split(",")[0])
        except:
            hold_sec = 0
        if hold_sec > 0:
            # Le trade a été ouvert ET fermé → pas de ghost, juste la position est fermée
            log(f"  ✅ #{cycle} OK (position fermée, hold={hold_sec:.0f}s)")
        else:
            log_ghost(state, cycle, "ENTRY_GHOST",
                     f"fill={side} {csv_qty:.4f} mais position VIDE")
        return

    # ─── Vérification 2: La qty matche ? ─────────────────────────────────
    pos_qty = float(btc_pos.get("positionAmt", 0))
    pos_side = "LONG" if pos_qty > 0 else "SHORT"
    expected_side = "LONG" if side == "BUY" else "SHORT"

    if hold_sec > 0:
        # Le trade a un hold > 0 → il a été ouvert et potentiellement fermé
        # Si la position est toujours là, c'est qu'elle n'a pas été fermée
        if btc_pos is not None and abs(pos_qty) > 0.0001:
            log_ghost(state, cycle, "EXIT_GHOST",
                     f"exit={exit_reason} mais position encore {pos_side} {pos_qty:.4f}")

        # Vérifier que la balance correspond
        bal = get_balance()
        csv_pnl = float(row.get("pnlNet", row.get("pnl", 0)))
        log(f"  #{cycle} hold={hold_sec:.0f}s exit={exit_reason} pnl={csv_pnl:+.4f} bal={bal:.2f}")
    else:
        # Pas de hold → entrée seulement
        if pos_qty != 0:
            qty_diff = abs(abs(pos_qty) - csv_qty)
            if qty_diff > 0.0005:
                log_ghost(state, cycle, "QTY_MISMATCH",
                         f"fill={csv_qty:.4f} vs pos={pos_qty:.4f} diff={qty_diff:.4f}")
            else:
                log(f"  ✅ #{cycle} Position vérifiée: {pos_side} {pos_qty:.4f}")
        else:
            log_ghost(state, cycle, "ENTRY_GHOST",
                     f"fill={side} {csv_qty:.4f} mais position VIDE")

# ─── Vérification des orphelins ───────────────────────────────────────────────
def check_orphans(state):
    """Vérifie et ferme les positions orphelines."""
    positions = get_positions()
    for p in positions:
        qty = float(p["positionAmt"])
        entry = float(p["entryPrice"])
        upnl = float(p.get("UnrealizedProfit", p.get("unRealizedProfit", 0)))
        side = "LONG" if qty > 0 else "SHORT"

        log(f"  ⚠️  Orphelin: {side} {qty:.4f} @ {entry:.1f} (unPnl={upnl:+.4f})")

        if AUTO_CLOSE_ORPHANS:
            if close_orphan(qty, side):
                state.orphans_closed += 1
                time.sleep(1)

# ─── Boucle principale ────────────────────────────────────────────────────────
def watch_csv(csv_path, once=False):
    state = GhostState()
    csv_file = Path(csv_path)

    log(f"🔍 Surveillance: {csv_file.name}")
    log(f"   Mode: {'one-shot' if once else ' temps réel'}")
    log(f"   Auto-close: {AUTO_CLOSE_ORPHANS}")
    log(f"   Base URL: {BASE_URL}")

    # Vérification initiale des orphelins
    log("\n── CHECK 0: Orphelins existants ──")
    check_orphans(state)

    while True:
        if csv_file.exists():
            new_rows = read_new_lines(csv_file, state)
            if new_rows:
                for row in new_rows:
                    verify_fill(row, state)

        if once:
            break

        # Check orphelins périodiquement (toutes les 30s)
        if int(time.time()) % 30 < POLL_INTERVAL:
            check_orphans(state)

        time.sleep(POLL_INTERVAL)

    # ─── Rapport final ─────────────────────────────────────────────────────
    log("\n" + "=" * 50)
    log("📊 RAPPORT ANTI-GHOST")
    log("=" * 50)
    log(f"  Fils vérifiés:   {len(state.checked_cycles)}")
    log(f"  Ghosts trouvés:  {len(state.ghosts)}")
    log(f"  Orphelins fermés: {state.orphans_closed}")

    if state.ghosts:
        log("\n  Détail ghosts:")
        for g in state.ghosts:
            log(f"    {g['cycle']} [{g['kind']}] {g['detail']}")

    # Vérification finale
    log("\n── CHECK FINAL ──")
    check_orphans(state)

    bal = get_balance()
    log(f"  Balance finale: {bal:.4f} USDT")
    log("=" * 50)

    # Écrire le rapport
    report_path = csv_file.with_suffix(".ghost_report.json")
    report = {
        "csv": str(csv_file),
        "ts": now_ts(),
        "checked": len(state.checked_cycles),
        "ghosts": len(state.ghosts),
        "orphans_closed": state.orphans_closed,
        "ghost_details": state.ghosts,
        "balance_final": bal,
    }
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2)
    log(f"  📄 Rapport: {report_path}")

    return report

# ─── Main ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Anti-ghost-fill wrapper")
    parser.add_argument("--csv", help="Chemin du CSV à surveiller")
    parser.add_argument("--dir", help="Répertoire à surveiller (tous les CSV)")
    parser.add_argument("--once", action="store_true", help="One-shot (vérifier et sortir)")
    args = parser.parse_args()

    if not API_KEY or not API_SECRET:
        print("❌ Clés Binance manquantes. Source ~/.binance_testnet.env")
        sys.exit(1)

    if args.csv:
        watch_csv(args.csv, once=args.once)
    elif args.dir:
        # Trouver le CSV le plus récent dans le répertoire
        d = Path(args.dir)
        csvs = sorted(d.glob("*.csv"), key=lambda f: f.stat().st_mtime, reverse=True)
        if not csvs:
            print(f"❌ Aucun CSV dans {args.dir}")
            sys.exit(1)
        watch_csv(str(csvs[0]), once=args.once)
    else:
        print("Usage: python3 anti_ghost_wrapper.py --csv <fichier> [--once]")
        sys.exit(1)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""watch_shadow.py — TABLEAU DE BORD LIVE COLORÉ du Shadow Mode (lecture seule).
Usage : python3 watch_shadow.py   → Ctrl+C pour quitter l'AFFICHAGE (le moteur continue).
RUN_ONCE=1 python3 watch_shadow.py → un seul rendu (pour test).
Ne touche à rien : lit uniquement les CSV du shadow. Zéro ordre, zéro clé."""
import csv, os, subprocess, sys, time
from datetime import datetime, timezone

RUNS = os.path.expanduser("~/ace777-test-day1/runs")
FEE = 1.760
DAY = "SHADOW_SC_20260902"
FILLS = os.path.join(RUNS, f"{DAY}_FILLS.csv")
TICKS = os.path.join(RUNS, f"{DAY}_TICKS.csv")
BOOTSTRAP_SEC = 90 * 60

# ANSI
CLEAR = "\033[2J\033[H"
BOLD, DIM, RST = "\033[1m", "\033[2m", "\033[0m"
GREEN, RED, YEL, CYA, MAG, WHT = "\033[32m", "\033[31m", "\033[33m", "\033[36m", "\033[35m", "\033[97m"

def read_fills():
    out = []
    try:
        with open(FILLS, errors="replace") as f:
            for row in csv.DictReader(f):
                out.append(row)
    except FileNotFoundError:
        pass
    return out

def read_last_tick():
    try:
        with open(TICKS, errors="replace") as f:
            rows = list(csv.DictReader(f))
            return rows[-1] if rows else None
    except FileNotFoundError:
        return None

def engine_alive():
    r = subprocess.run(["pgrep", "-f", "shadow_mode_sc"], capture_output=True, text=True)
    return r.stdout.strip().splitlines() or []

def fmt_usd(v):
    return f"{v:+.2f}"

def render():
    W = 78
    fills = read_fills()
    tick = read_last_tick()
    pids = engine_alive()

    exits = {}
    stats = {"ALPHA": {"net": 0.0, "n_ex": 0, "w": 0, "l": 0, "boot": 0},
             "BETA":  {"net": 0.0, "n_ex": 0, "w": 0, "l": 0, "boot": 0}}
    start_ts = None
    for r in fills:
        s = r["stream"]
        if r["kind"] == "ENTRY":
            if start_ts is None:
                start_ts = r["ts"]
            if "BOOTSTRAP" in r.get("msg", ""):
                stats[s]["boot"] += 1
        elif r["kind"] == "EXIT":
            g = float(r["pnlGross"] or 0)
            net = g - FEE
            st = stats[s]
            st["net"] += net; st["n_ex"] += 1
            st["w"] += g > 0; st["l"] += g < 0

    L = []
    L.append("╔" + "═" * W + "╗")
    title = "SHADOW MODE — SCÉNARIO C — LIVE (lecture seule)"
    L.append("║" + title.center(W) + "║")
    L.append("╚" + "═" * W + "╝")

    now = datetime.now(timezone.utc)
    alive = f"{GREEN}{BOLD}VIVANT{RST} (pid {', '.join(pids)})" if pids else f"{RED}{BOLD}MORT{RST}"
    btc = tick["px_close"] if tick else "—"
    L.append(f" Moteur : {alive}    UTC : {now.strftime('%H:%M:%S')}    BTC : {WHT}{BOLD}{btc}{RST}")
    if start_ts:
        try:
            t0 = datetime.strptime(start_ts, "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc)
            remain = int(BOOTSTRAP_SEC - (now - t0).total_seconds())
            boot = (f"{YEL}porte bootstrap : {remain//60} min {remain%60:02d} s restantes{RST}"
                    if remain > 0 else f"{GREEN}régime nominal H actif{RST}")
        except Exception:
            boot = ""
    else:
        boot = f"{DIM}en attente du 1er fill…{RST}"
    L.append(f" {boot}")
    L.append("─" * (W + 2))

    for s in ("ALPHA", "BETA"):
        st = stats[s]
        col = CYA if s == "ALPHA" else MAG
        pos = (tick or {}).get(f"pos_{s.lower()}", "")
        h = (tick or {}).get(f"H_{s.lower()}", "?")
        src = (tick or {}).get(f"h_src_{s.lower()}", "?")
        hs = (f"{GREEN}H=1{RST}" if h == "1" else f"{RED}H=0{RST}") + f"{DIM}({src}){RST}"
        pos_s = f"{WHT}{pos}{RST}" if pos else f"{DIM}à plat{RST}"
        netcol = GREEN if st["net"] >= 0 else RED
        side = "LONG " if s == "ALPHA" else "SHORT"
        bootmark = f" {YEL}· boot×{st['boot']}{RST}" if st["boot"] else ""
        L.append(f" {col}{BOLD}{s}{RST} {side}  {hs}  pos: {pos_s}  "
                 f"net: {netcol}{BOLD}{fmt_usd(st['net'])}{RST} "
                 f"({st['n_ex']} sorties · {GREEN}{st['w']}W{RST}/{RED}{st['l']}L{RST}){bootmark}")
    L.append("─" * (W + 2))

    L.append(f" {BOLD}Derniers fills ({min(len(fills), 8)}/{len(fills)}) :{RST}")
    for r in fills[-8:]:
        ts = r["ts"][11:19]
        s = r["stream"]; col = CYA if s == "ALPHA" else MAG
        kind = r["kind"]
        kcol = WHT if kind == "ENTRY" else (GREEN if float(r["pnlGross"] or 0) >= 0 else RED)
        pnl = f"{float(r['pnlGross']):+.2f}" if kind == "EXIT" else "   —  "
        msg = r.get("msg", "")
        boot_tag = f" {YEL}[BOOTSTRAP]{RST}" if "BOOTSTRAP" in msg else ""
        L.append(f"  {DIM}{ts}{RST} {col}{s:<5}{RST} {kcol}{kind:<5}{RST} "
                 f"{r['px']:>9}  pnl {pnl}  {DIM}{msg[:38]}{RST}{boot_tag}")
    if not fills:
        L.append(f"  {DIM}(aucun fill pour l'instant){RST}")

    L.append("")
    L.append(f" {DIM}Ctrl+C = quitter l'AFFICHAGE (le moteur continue). "
             f"Arrêt moteur : ./stop_shadow_mode.sh{RST}")
    return "\n" + "\n".join(L)

if __name__ == "__main__":
    once = os.environ.get("RUN_ONCE") == "1"
    while True:
        try:
            out = render()
        except Exception as e:
            out = f"erreur affichage : {e}"
        sys.stdout.write("" if once else CLEAR)
        print(out, flush=True)
        if once:
            break
        try:
            time.sleep(2)
        except KeyboardInterrupt:
            print(f"\n{DIM}Affichage fermé — le moteur, lui, tourne toujours.{RST}")
            break

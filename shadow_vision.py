#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""shadow_vision.py — VISION MOTEUR v2 (mécanique détaillée) — lecture seule.
Rejoue EXACTEMENT la même math que shadow_mode_sc.py et EXPLIQUE chaque décision :
  - H : quels fills composent la somme des 2h (n, liste, total)
  - slots 5-min : entrée programmée / BOOTSTRAP / SKIP et pourquoi
  - position : entry, ext, règle du stop (ext − 30%×gain), cap (entry ± 50$), distances
  - sortie : quelle règle a touché (low/high vs stop/cap), pnl brut, frais, net, hold
Usage : python3 shadow_vision.py   (Ctrl+C : ferme l'affichage, moteur intact)
RUN_ONCE=1 → un bloc unique (test)."""
import csv, json, os, sys, time, urllib.request
from datetime import datetime, timezone

ROOT  = os.path.expanduser("~/ace777-test-day1")
RUNS  = os.path.join(ROOT, "runs")
DAY   = "SHADOW_SC_20260902"
FILLS = os.path.join(RUNS, f"{DAY}_FILLS.csv")
LOG   = os.path.join(RUNS, f"{DAY}.log")
QTY, FEE, RET = 0.10593, 1.760, 0.30
CAP_PX = 50.0 / QTY
HWIN   = 7200
URL = "https://fapi.binance.com/fapi/v1/klines?symbol=BTCUSDT&interval=1m&limit=180"

G, R, Y, C, M, D, B, W, RST = ("\033[32m", "\033[31m", "\033[33m", "\033[36m",
                               "\033[35m", "\033[2m", "\033[1m", "\033[97m", "\033[0m")

def uts(s):
    return datetime.strptime(s[:19], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc).timestamp()

def load_fills():
    try:
        with open(FILLS, errors="replace") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        return []

def engine_start_ts():
    try:
        with open(LOG, errors="replace") as f:
            for line in f:
                if "SHADOW MODE ON" in line:
                    return uts(line[:20])
    except Exception:
        pass
    return None

def fetch_klines():
    for a in range(3):
        try:
            with urllib.request.urlopen(URL, timeout=15) as r:
                rows = json.loads(r.read())
            return [(int(x[0]) // 1000, float(x[1]), float(x[2]), float(x[3]), float(x[4])) for x in rows]
        except Exception:
            time.sleep(1 + a)
    return []

def fmtpx(v):
    return f"{v:.2f}"

def render(kl, fills, now_ts, printed_upto, boot_dl):
    streams = {"ALPHA": ("LONG", C), "BETA": ("SHORT", M)}
    virt = {s: [(uts(r["ts"]), float(r["pnlGross"]))
                for r in fills if r["stream"] == s and r["kind"] == "EXIT"]
            for s in streams}

    def H(s, ts):
        vals = [(t, p) for t, p in virt[s] if ts - HWIN < t < ts]
        return sum(p for _, p in vals), vals

    open_pos = {}
    for s in streams:
        ent = [r for r in fills if r["stream"] == s and r["kind"] == "ENTRY"]
        ext_ = [r for r in fills if r["stream"] == s and r["kind"] == "EXIT"]
        if ent and (not ext_ or uts(ent[-1]["ts"]) > uts(ext_[-1]["ts"])):
            open_pos[s] = {"entry_ts": uts(ent[-1]["ts"]), "entry_px": float(ent[-1]["px"])}

    L, last_ts = [], printed_upto
    closed = kl[:-1]
    for t, o, h, l, c in closed:
        if t <= printed_upto:
            continue
        last_ts = t
        hhmmss = datetime.fromtimestamp(t, timezone.utc).strftime("%H:%M:%S")
        mmss_slot = f"prochain slot :{(t // 300 + 1) * 5 % 60:02d} (dans {((t // 300 + 1) * 300 - t)//60}min)"
        for s, (side, col) in streams.items():
            tag = f"{col}[{s}_{side}]{RST}"
            ssum, hvals = H(s, t)
            det = " ".join(f"{p:+.2f}" for _, p in hvals[-4:]) or "(vide)"
            hline = (f"H(2h): n={len(hvals)} [{D}{det}{RST}] = "
                     f"{G if ssum>0 else R}{B}{ssum:+.2f}{RST} → "
                     + (f"{G}H=1{RST}" if ssum > 0 else f"{R}H=0{RST}"))
            pos = open_pos.get(s)
            if pos is None:
                if t % 300 == 0:
                    if ssum > 0:
                        act = f"{W}{B}SLOT :5m → H=1 → ENTRY programmé sur open barre suivante{RST}"
                    elif t < boot_dl:
                        act = f"{Y}SLOT :5m → H=0 mais BOOTSTRAP → entrée forcée (taguée){RST}"
                    else:
                        act = f"{Y}SLOT :5m → H=0 → SKIP — attend que la somme 2h repasse > 0{RST}"
                    L.append(f"{tag} {D}{hhmmss}{RST} à plat | {hline} | {act}")
                else:
                    L.append(f"{tag} {D}{hhmmss}{RST} à plat | {hline} | {D}{mmss_slot}{RST}")
                continue
            e_ts, e_px = pos["entry_ts"], pos["entry_px"]
            if t <= e_ts:
                continue
            ext, armed, exit_line = e_px, False, None
            for t2, o2, h2, l2, c2 in closed:
                if t2 <= e_ts:
                    continue
                if t2 > t:
                    break
                ext = max(ext, h2) if side == "LONG" else min(ext, l2)
                armed = armed or (h2 > e_px if side == "LONG" else l2 < e_px)
                if armed:
                    if side == "LONG":
                        stop = max(e_px, ext - RET * (ext - e_px))
                        if l2 <= stop:
                            exit_line = ("trailing_stop", stop, t2, f"low {fmtpx(l2)} ≤ stop {fmtpx(stop)}")
                            break
                        if h2 >= e_px + CAP_PX:
                            exit_line = ("cap", e_px + CAP_PX, t2, f"high {fmtpx(h2)} ≥ cap {fmtpx(e_px+CAP_PX)}")
                            break
                    else:
                        stop = min(e_px, ext + RET * (e_px - ext))
                        if h2 >= stop:
                            exit_line = ("trailing_stop", stop, t2, f"high {fmtpx(h2)} ≥ stop {fmtpx(stop)}")
                            break
                        if l2 <= e_px - CAP_PX:
                            exit_line = ("cap", e_px - CAP_PX, t2, f"low {fmtpx(l2)} ≤ cap {fmtpx(e_px-CAP_PX)}")
                            break
                if (t2 - e_ts) % 300 == 0 and t2 > e_ts:
                    ssum2, _ = H(s, t2 - 1)
                    if ssum2 <= 0:
                        exit_line = ("h_gate_off", c2, t2, f"borne 5-min : somme H = {ssum2:+.2f} ≤ 0 → close {fmtpx(c2)}")
                        break
            if exit_line:
                why, px, t2, rule = exit_line
                pnl = ((px - e_px) if side == "LONG" else (e_px - px)) * QTY
                col2 = G if pnl >= 0 else R
                L.append(f"{tag} {D}{datetime.fromtimestamp(t2, timezone.utc).strftime('%H:%M:%S')}{RST} "
                         f"{col2}{B}EXIT {why}{RST} @ {fmtpx(px)} | règle : {rule} | "
                         f"pnl brut {col2}{pnl:+.4f}{RST} − frais {FEE:.2f} = net {col2}{pnl-FEE:+.4f}{RST} | "
                         f"hold {int(t2-e_ts)}s")
                continue
            gain = abs(ext - e_px)
            if side == "LONG":
                stop = max(e_px, ext - RET * gain)
                cap_px = e_px + CAP_PX
                dstop = (stop - c) * QTY
            else:
                stop = min(e_px, ext + RET * gain)
                cap_px = e_px - CAP_PX
                dstop = (c - stop) * QTY
            arm_txt = (f"{G}ARMÉ{RST} → stop = ext − 30%×gain({gain:.2f}) = {fmtpx(stop)} "
                       f"({Y}{dstop:+.2f}${RST} du close · {Y}{dcap:+.2f}${RST} du cap)") if armed else \
                      f"{Y}non ARMÉ{RST} — le stop n'existe pas tant que le prix n'a pas dépassé l'entry"
            L.append(f"{tag} {D}{hhmmss}{RST} pos @ {W}{B}{fmtpx(e_px)}{RST} | "
                     f"ext={fmtpx(ext)} | {arm_txt} | cap {fmtpx(cap_px)} (entry±50$) | {hline}")
    return L, last_ts

def state_block(kl, fills, boot_dl, now_ts):
    SEP = "═" * 100
    L = [SEP]
    L.append(f"{B}VISION MOTEUR v2 — la mécanique complète, décision par décision{RST} "
             f"{D}(lecture seule, moteur intact){RST}")
    remain = int(boot_dl - now_ts)
    if remain > 0:
        L.append(f" {Y}BOOTSTRAP actif — {remain//60} min {remain%60:02d} s restantes{RST}"
                 f" {D}(entrées forcées taguées, sorties toujours sous H){RST}")
    else:
        L.append(f" {G}Régime nominal H{RST}")
    for s, col in (("ALPHA", C), ("BETA", M)):
        ex = [r for r in fills if r["stream"] == s and r["kind"] == "EXIT"]
        tot = sum(float(r["pnlGross"]) - FEE for r in ex)
        wins = sum(1 for r in ex if float(r["pnlGross"]) > 0)
        netcol = G if tot >= 0 else R
        L.append(f" {col}[{s}]{RST} net virtuel : {netcol}{B}{tot:+.4f} USDT{RST} "
                 f"({len(ex)} sorties · {wins} bruts positifs · frais payés {len(ex)*FEE:.2f})")
    px = kl[-1][4] if kl else 0
    L.append(f" BTC (barre en formation) : {W}{B}{fmtpx(px)}{RST}")
    L.append(SEP)
    return L

def main():
    st_ts = engine_start_ts()
    boot_dl = (st_ts + 90 * 60) if st_ts else 0
    if os.environ.get("RUN_ONCE") == "1":
        kl = fetch_klines()
        fills = load_fills()
        now_ts = time.time()
        lines, _ = render(kl, fills, now_ts, 0, boot_dl)
        print("\n".join(state_block(kl, fills, boot_dl, now_ts)))
        print("\n".join(lines[-50:]))
        return
    print("═" * 100)
    print(f"{B}VISION MOTEUR v2 — flux détaillé en direct{RST} "
          f"{D}(Ctrl+C : affichage seul, moteur intact){RST}")
    print("═" * 100, flush=True)
    printed_upto = 0
    while True:
        kl = fetch_klines()
        fills = load_fills()
        if not kl:
            time.sleep(3); continue
        lines, printed_upto = render(kl, fills, time.time(), printed_upto, boot_dl)
        for ln in lines:
            print(ln, flush=True)
        try:
            time.sleep(3)
        except KeyboardInterrupt:
            print(f"\n{D}Affichage fermé — le moteur continue de tourner.{RST}")
            break

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Récupérer rétroactivement les durées de détention (hold_sec) des 3 runs.

Le CSV scellé n'écrit PAS la durée (elle est dans le slot holdSec à la place du
message). La durée vit dans le log live MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log
(ligne `[BETA_X5] entry=HH:MM:SS@prix x<lev> #<cycle> <side> ... hold=Ns sec=N | exit=prix ... pnl=...`).

Jointure robuste : (unité, cycle, exit_price, pnl) — les 4 champs sont issus des
mêmes variables ($i, $exit_price, $pnl_usdt) des deux côtés. En cas de collision
(cycle réinitialisé par session + prix/pnl identiques), on désambigüe par
l'heure de sortie (exit_time du log vs HH:MM:SS du ts CSV).

Lecture seule — n'écrit QUE des fichiers d'analyse neufs dans Index_Maison/.
"""
import csv
import os
import re
import statistics

ROOT = os.path.expanduser("~/ace777-test-day1")
LIVE = os.path.join(ROOT, "runs", "MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log")
SCELLE = os.path.join(ROOT, "runs", "SCELLE")
OUT_CSV = os.path.join(ROOT, "Index_Maison", "durees_restituees_3_runs_2026-08-15.csv")
OUT_MD = os.path.join(ROOT, "Index_Maison", "SYNTHESE_DUREES_3_RUNS_2026-08-15.md")

CSV_FILES = {
    "ALPHA_X13_BURST13": "MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13_20260815-054541Z.csv",
    "BETA_X5": "MASTER_VORTEX_V2_COLLAB_4H_BETA_X5_20260815-054542Z.csv",
}

RUNS = {
    "Run_4h_1": ("2026-08-14T12:51:00Z", "2026-08-14T15:57:59Z"),
    "Run_V2": ("2026-08-14T16:24:00Z", "2026-08-14T20:24:59Z"),
    "Run_Nuit": ("2026-08-14T21:45:00Z", "2026-08-15T05:44:59Z"),
}

ANSI = re.compile(r"\x1b\[[0-9;]*m")
# [BETA_X5] entry=05:41:25@63041.90000000 x5 #3548 SELL tension=... hold=5s sec=5 | exit=... exit_time=05:41:30 pnl=-0.00000000
RE = re.compile(
    r"\[([A-Z0-9_]+)\]\s+entry=(\d{2}:\d{2}:\d{2})(?:@([0-9.]+))?\s+x(\d+)\s+#(\d+)\s+(BUY|SELL)"
    r".*?hold=(\d+)s\s+sec=\d+.*?exit=([0-9.]+).*?exit_time=(\d{2}:\d{2}:\d{2})"
    r".*?pnl=(-?[0-9.]+)"
)


def parse_live():
    """dict key=(unit, cycle, exit_price, pnl) -> liste de matches."""
    out = {}
    with open(LIVE, encoding="utf-8", errors="replace") as f:
        for line in f:
            clean = ANSI.sub("", line)
            m = RE.search(clean)
            if not m:
                continue
            unit, entry_t, entry_p, lev, cycle, side, hold, exit_p, exit_t, pnl = m.groups()
            key = (unit, cycle, exit_p, pnl)
            out.setdefault(key, []).append({
                "hold": int(hold), "entry": entry_t, "entry_price": entry_p,
                "exit": exit_t, "side": side,
            })
    return out


def in_run(ts, run):
    lo, hi = RUNS[run]
    return lo <= ts <= hi


def main():
    live = parse_live()
    print(f"log live : {sum(len(v) for v in live.values())} trades avec durée, "
          f"{len(live)} clés uniques")

    rows_out = []
    matched = 0
    filled_total = 0
    ambiguous = 0
    per_run = {r: {u: [] for u in CSV_FILES} for r in RUNS}

    for unit, fn in CSV_FILES.items():
        with open(os.path.join(SCELLE, fn), encoding="utf-8", errors="replace") as f:
            reader = csv.reader(f)
            next(reader, None)
            for r in reader:
                if len(r) < 9:
                    continue
                ts, cycle, side, status = r[0], r[1], r[2], r[3]
                if status != "FILLED":
                    continue
                run = next((name for name in RUNS if in_run(ts, name)), None)
                if run is None:
                    continue
                filled_total += 1
                pnl = r[8]
                exit_price = r[5]
                cands = live.get((unit, cycle, exit_price, pnl), [])
                info = None
                if len(cands) == 1:
                    info = cands[0]
                elif len(cands) > 1:
                    # désambiguïser par l'heure de sortie (ts CSV: HH:MM:SS aux positions 11:19)
                    hhmmss = ts[11:19]
                    for c in cands:
                        if c["exit"] == hhmmss:
                            info = c
                            break
                    if info is None:
                        ambiguous += 1
                if info:
                    matched += 1
                    per_run[run][unit].append(info["hold"])
                rows_out.append({
                    "run": run, "ts": ts, "cycle": cycle, "unit": unit, "side": side,
                    "entryPrice": r[4], "exitPrice": exit_price, "qty": r[6],
                    "bps": r[7], "pnl": pnl, "exitReason": r[9],
                    "hold_sec": info["hold"] if info else "",
                    "entry_heure": info["entry"] if info else "",
                    "exit_heure": info["exit"] if info else "",
                })

    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=[
            "run", "ts", "cycle", "unit", "side", "entryPrice", "exitPrice",
            "qty", "bps", "pnl", "exitReason", "hold_sec", "entry_heure", "exit_heure"])
        w.writeheader()
        w.writerows(rows_out)

    lines = ["# Synthèse durées de détention récupérées (3 runs 14-15/08)",
             "",
             f"Match : {matched}/{filled_total} trades FILLED recollés "
             f"({round(100 * matched / filled_total, 1) if filled_total else 0}%) · "
             f"ambiguïtés non résolues : {ambiguous}",
             ""]
    for run in RUNS:
        lines.append(f"## {run}")
        for unit in CSV_FILES:
            hs = per_run[run][unit]
            if not hs:
                lines.append(f"- {unit}: 0 durée récupérée")
                continue
            avg = statistics.mean(hs)
            med = statistics.median(hs)
            buckets = {
                "<5s": sum(1 for h in hs if h < 5),
                "5-10s": sum(1 for h in hs if 5 <= h < 10),
                "10-30s": sum(1 for h in hs if 10 <= h < 30),
                "30-60s": sum(1 for h in hs if 30 <= h < 60),
                ">=60s": sum(1 for h in hs if h >= 60),
            }
            lines.append(
                f"- {unit}: n={len(hs)} moyenne={avg:.1f}s médiane={med:.0f}s "
                f"min={min(hs)}s max={max(hs)}s | répartition {buckets}")
        lines.append("")

    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"CSV reconstitué : {OUT_CSV} ({len(rows_out)} lignes)")
    print(f"Synthèse : {OUT_MD}")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Analyse BRUTE des 3 runs du 14-15/08 (Run 4h #1, Run V2, Run Nuit).

Refait l'analyse à partir des CSV scellés (append-only depuis le 08/07) :
- vérifie intégrité (sha256 vs signatures)
- confirme le préfixe identique octet-pour-octet
- détecte les sessions (reset du compteur cycle)
- isole les 3 fenêtres de run et recalcule toutes les stats
- cherche anomalies : lignes malformées, doublons, gaps, tailles incohérentes
- compare le "vocabulaire" (size_note, exitReason) entre les 3 runs
"""
import csv
import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict

SCELLE = os.path.expanduser("~/ace777-test-day1/runs/SCELLE")
FILES = {
    "ALPHA_14": "MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13_20260814-211907Z.csv",
    "ALPHA_15": "MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13_20260815-054541Z.csv",
    "BETA_14": "MASTER_VORTEX_V2_COLLAB_4H_BETA_X5_20260814-211907Z.csv",
    "BETA_15": "MASTER_VORTEX_V2_COLLAB_4H_BETA_X5_20260815-054542Z.csv",
}

# Fenêtres des 3 runs (UTC, inclusif)
RUNS = {
    "Run_4h_1": ("2026-08-14T12:51:00Z", "2026-08-14T15:57:59Z"),
    "Run_V2": ("2026-08-14T16:24:00Z", "2026-08-14T20:24:59Z"),
    "Run_Nuit": ("2026-08-14T21:45:00Z", "2026-08-15T05:44:59Z"),
}


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def load_sigs():
    sigs = {}
    for fn in os.listdir(SCELLE):
        if not fn.endswith(".SIGNATURE.txt"):
            continue
        with open(os.path.join(SCELLE, fn), encoding="utf-8") as f:
            txt = f.read()
        base = None
        for line in txt.splitlines():
            if line.startswith("fichier_scelle="):
                base = line.split("=", 1)[1]
            if line.startswith("sha256="):
                if base:
                    sigs[base] = line.split("=", 1)[1]
    return sigs


def parse_rows(path):
    """Parse le CSV et retourne la liste de dict + anomalies."""
    rows = []
    anom = []
    with open(path, encoding="utf-8", errors="replace") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        for i, r in enumerate(reader, start=2):
            if len(r) != 12:
                anom.append(("colcount", i, len(r), r[:4]))
                # tente de réparer : tout après l'index 9 = exitReason (10e)
                if len(r) > 12:
                    r = r[:11] + [",".join(r[11:])]
                elif len(r) < 12:
                    r = r + [""] * (12 - len(r))
            d = {
                "line": i,
                "ts": r[0],
                "cycle": r[1],
                "side": r[2],
                "status": r[3],
                "entryPrice": r[4],
                "exitPrice": r[5],
                "qty": r[6],
                "bps": r[7],
                "pnl": r[8],
                "exitReason": r[9],
                "holdSec": r[10],  # contient en réalité le message détaillé
                "msg": r[11],      # censé contenir le message, est vide
            }
            rows.append(d)
    return header, rows, anom


def fnum(s):
    try:
        return float(s)
    except (TypeError, ValueError):
        return None


def in_run(ts, run):
    lo, hi = RUNS[run]
    return lo <= ts <= hi


def analyze(name, rows, anom, run=None):
    """Stats pour un sous-ensemble (ou tout)."""
    sub = rows if run is None else [r for r in rows if in_run(r["ts"], run)]
    filled = [r for r in sub if r["status"] == "FILLED"]
    skips = [r for r in sub if r["status"] == "SKIPPED"]
    pnl_sum = sum(fnum(r["pnl"]) for r in filled if fnum(r["pnl"]) is not None)
    wins = [r for r in filled if (fnum(r["pnl"]) or 0) > 0]
    losses = [r for r in filled if (fnum(r["pnl"]) or 0) < 0]
    flats = [r for r in filled if (fnum(r["pnl"]) or 0) == 0]
    # flat strict : entry == exit
    flat_strict = [r for r in filled if r["entryPrice"] == r["exitPrice"] and r["entryPrice"] != ""]
    revenge = [r for r in filled if "revenge" in r["holdSec"].lower()]
    # size_note extraction
    size_notes = Counter()
    exit_reasons = Counter()
    for r in filled:
        m = re.search(r"size_note=(\S+)", r["holdSec"])
        if m:
            size_notes[m.group(1)] += 1
        exit_reasons[r["exitReason"]] += 1
    ts_list = [r["ts"] for r in sub]
    cycles = [int(r["cycle"]) for r in sub if r["cycle"].isdigit()]
    # détection resets de cycle dans ce sous-ensemble
    resets = 0
    prev = None
    for c in cycles:
        if prev is not None and c < prev:
            resets += 1
        prev = c
    return {
        "rows": len(sub),
        "filled": len(filled),
        "skips": len(skips),
        "other_status": Counter(r["status"] for r in sub if r["status"] not in ("FILLED", "SKIPPED")),
        "pnl_sum": round(pnl_sum, 4),
        "wins": len(wins), "losses": len(losses), "flats": len(flats),
        "flat_strict": len(flat_strict),
        "revenge": len(revenge),
        "revenge_pct": round(100 * len(revenge) / len(filled), 1) if filled else 0,
        "flat_pct": round(100 * len(flats) / len(filled), 1) if filled else 0,
        "size_notes": size_notes,
        "exit_reasons": exit_reasons,
        "ts_first": min(ts_list) if ts_list else None,
        "ts_last": max(ts_list) if ts_list else None,
        "cycle_min": min(cycles) if cycles else None,
        "cycle_max": max(cycles) if cycles else None,
        "cycle_resets": resets,
    }


def main():
    sigs = load_sigs()
    print("=" * 70)
    print("1) INTEGRITE (sha256 vs signatures)")
    for name, fn in FILES.items():
        p = os.path.join(SCELLE, fn)
        actual = sha256(p)
        expected = sigs.get(fn)
        ok = "OK" if expected and actual == expected else ("NO-SIG" if not expected else "MISMATCH")
        print(f"  {name}: {ok}  ({actual[:16]}…)")
        if expected and actual != expected:
            print(f"    ATTENDU: {expected[:16]}…")

    print("=" * 70)
    print("2) PREFIXE IDENTIQUE (octet pour octet)")
    for unit in ("ALPHA", "BETA"):
        p14 = os.path.join(SCELLE, FILES[f"{unit}_14"])
        p15 = os.path.join(SCELLE, FILES[f"{unit}_15"])
        with open(p14, "rb") as a, open(p15, "rb") as b:
            data14 = a.read()
            data15 = b.read()
        n = len(data14)
        match = 0
        for i in range(min(n, len(data15))):
            if data14[i] != data15[i]:
                break
            match += 1
        print(f"  {unit}: fichier 14 = {n} octets, fichier 15 = {len(data15)} octets, "
              f"prefixe identique = {match} octets ({match == n})")

    print("=" * 70)
    print("3) PARSING + ANOMALIES DE STRUCTURE")
    parsed = {}
    for name, fn in FILES.items():
        header, rows, anom = parse_rows(os.path.join(SCELLE, fn))
        parsed[name] = rows
        colcount = [a for a in anom if a[0] == "colcount"]
        print(f"  {name}: {len(rows)} lignes, malformees(col!=12)={len(colcount)}")
        for a in colcount[:5]:
            print(f"      ligne {a[1]}: {a[2]} colonnes")

    # Vérif msg vide / holdSec rempli
    for name in ("ALPHA_15", "BETA_15"):
        rows = parsed[name]
        msg_nonempty = sum(1 for r in rows if r["msg"].strip())
        hold_nonempty = sum(1 for r in rows if r["holdSec"].strip())
        print(f"  {name}: holdSec non-vide={hold_nonempty}, msg non-vide={msg_nonempty} "
              f"-> {'ANOMALIE confirmee (msg vide, detail dans holdSec)' if msg_nonempty == 0 else 'msg parfois rempli'}")

    print("=" * 70)
    print("4) SESSIONS (reset du compteur cycle) — fichier 15 entier")
    for name in ("ALPHA_15", "BETA_15"):
        rows = parsed[name]
        resets = []
        prev = None
        for r in rows:
            if not r["cycle"].isdigit():
                continue
            c = int(r["cycle"])
            if prev is not None and c < prev:
                resets.append((r["ts"], prev, c))
            prev = c
        print(f"  {name}: {len(resets)} resets de cycle")
        for ts, p, c in resets:
            print(f"      reset @ {ts}  cycle {p} -> {c}")

    print("=" * 70)
    print("5) STATS PAR RUN (fenêtres de temps)")
    for unit in ("ALPHA", "BETA"):
        rows = parsed[f"{unit}_15"]  # fichier le plus complet
        print(f"  --- {unit} (x13 si ALPHA, x5 si BETA) ---")
        for run in ("Run_4h_1", "Run_V2", "Run_Nuit"):
            s = analyze(unit, rows, [], run=run)
            print(f"    {run}: rows={s['rows']} filled={s['filled']} skips={s['skips']} "
                  f"pnl={s['pnl_sum']} W/L/F={s['wins']}/{s['losses']}/{s['flats']} "
                  f"flat%={s['flat_pct']} revenge={s['revenge']}({s['revenge_pct']}%)")
            print(f"         ts={s['ts_first']} -> {s['ts_last']}  cycle {s['cycle_min']}..{s['cycle_max']} resets={s['cycle_resets']}")
            print(f"         size_notes={dict(s['size_notes'])}")
            print(f"         exit_reasons={dict(s['exit_reasons'])}")
            print(f"         autres_status={dict(s['other_status'])}")

    print("=" * 70)
    print("6) COMPARAISON VOCABULAIRE ENTRE LES 3 RUNS (diffs de setup)")
    for unit in ("ALPHA", "BETA"):
        rows = parsed[f"{unit}_15"]
        per_run = {}
        for run in ("Run_4h_1", "Run_V2", "Run_Nuit"):
            filled = [r for r in rows if in_run(r["ts"], run) and r["status"] == "FILLED"]
            notes = set()
            reasons = set()
            for r in filled:
                m = re.search(r"size_note=(\S+)", r["holdSec"])
                if m:
                    notes.add(m.group(1))
                reasons.add(r["exitReason"])
            per_run[run] = (notes, reasons)
        all_notes = set().union(*[per_run[r][0] for r in per_run])
        all_reasons = set().union(*[per_run[r][1] for r in per_run])
        print(f"  {unit}: size_notes apparaissant dans un seul run:")
        for note in sorted(all_notes):
            in_which = [r for r in per_run if note in per_run[r][0]]
            if len(in_which) < 3:
                print(f"      {note}: {in_which}")
        print(f"  {unit}: exitReasons apparaissant dans un seul run:")
        for reason in sorted(all_reasons):
            in_which = [r for r in per_run if reason in per_run[r][1]]
            if len(in_which) < 3:
                print(f"      {reason}: {in_which}")

    print("=" * 70)
    print("7) ANOMALIES TEMPORELLES (doublons ts/cycle, gaps)")
    for unit in ("ALPHA", "BETA"):
        rows = parsed[f"{unit}_15"]
        seen = set()
        dups = 0
        for r in rows:
            k = (r["ts"], r["cycle"])
            if k in seen:
                dups += 1
            seen.add(k)
        print(f"  {unit}: doublons (ts,cycle) = {dups}")


if __name__ == "__main__":
    main()

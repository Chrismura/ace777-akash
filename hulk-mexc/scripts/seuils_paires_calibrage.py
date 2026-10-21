#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""seuils_paires_calibrage.py — GO 21/10 item 3 (lecture seule, 0 ordre).
Calibre l'interrupteur PAR PAIRE : pic 30 j + seuil = 2x range médian 7 j.
Sources : runs/replay_cache/*_1h_45j.json (bougies 1 h) + strategie/universe_profils.json (spreads).
Sortie : runs/seuils_paires_live.json {PAIRE: {spread_bps, range_med_7j_pct, seuil_interrupt_pct}}.
Le seuil est un AVIS (pas câblé au moteur) : au-delà, la paire est déclarée en tempête.
"""
import json, statistics
from pathlib import Path
RACINE = Path(__file__).resolve().parent.parent
CACHE = RACINE / "runs" / "replay_cache"
PROFILS = RACINE / "strategie" / "universe_profils.json"
OUT = RACINE / "runs" / "seuils_paires_live.json"

def range_med_7j(pair):
    f = CACHE / f"{pair}_1h_45j.json"
    if not f.exists():
        return None
    kl = json.load(open(f, encoding="utf-8"))
    H = [float(b["h"]) for b in kl]; L = [float(b["l"]) for b in kl]
    ranges = []
    for d0 in range(0, len(H), 24):
        hs, ls = H[d0:d0+24], L[d0:d0+24]
        if hs and ls and min(ls) > 0:
            ranges.append((max(hs)-min(ls))/min(ls)*100.0)
    if len(ranges) < 14:
        return round(statistics.median(ranges), 2) if ranges else None
    return round(statistics.median(ranges[-14:-7] or ranges), 2)

def main():
    prof = json.load(open(PROFILS, encoding="utf-8"))
    paires = [k for k in prof if k.endswith("USDT")]
    out = {}
    for p in sorted(paires):
        c = (prof[p].get("calib") or {})
        spread = float(c.get("spread_cout_bps") or 50.0)
        rm = range_med_7j(p)
        seuil = round(max(2*(rm or 0), 4*spread/100.0, 1.0), 2) if rm else round(max(4*spread/100.0, 3.0), 2)
        out[p] = {"spread_bps": spread, "range_med_7j_pct": rm, "seuil_interrupt_pct": seuil,
                  "source_range": "replay_cache 45j" if rm else "fallback spread (pas de cache)"}
    OUT.write_text(json.dumps({"paires": out, "n": len(out)}, ensure_ascii=False, indent=1), encoding="utf-8")
    for p, v in sorted(out.items()):
        print(f"{p:14s} spread {v['spread_bps']:6.2f}bps  range7j {str(v['range_med_7j_pct']):>6}  seuil {v['seuil_interrupt_pct']:5.2f}%")
    print(f"-> {OUT} ({len(out)} paires)")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())

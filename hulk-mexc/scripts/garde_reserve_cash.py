#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""garde_reserve_cash.py — GO execution etape survie (lecture seule, 0 ordre).
Lit mission.json (cash Hulk) + seuils. Si cash < RESERVE (200$) -> crie BLOQUE_ACHATS.
N'ecrit jamais dans le moteur : ecrit runs/garde_reserve_live.json pour cockpit/pont.
"""
import json, os, sys
from datetime import datetime, timezone
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MISSION = os.path.join(BASE, "..", "Index_Maison", "cockpit", "mission.json")
LIVE = os.path.join(BASE, "runs", "garde_reserve_live.json")
RESERVE = float(os.environ.get("RESERVE_CASH", "200"))
def utc(): return datetime.now(timezone.utc).isoformat(timespec="seconds")
def main():
    try:
        d = json.load(open(MISSION, encoding="utf-8"))
    except Exception as e:
        print(f"mission illisible: {e}"); return 2
    h = d.get("hulk", {}) or {}
    cash = float(h.get("cash") or 0)
    bloque = cash < RESERVE
    out = {"ok": True, "ts": utc(), "cash": round(cash, 2), "reserve": RESERVE,
           "bloque_achats": bloque,
           "message": f"cash {cash:.2f}$ {'< reserve '+str(RESERVE)+'$ -> BLOQUE_ACHATS (avis, non cable)' if bloque else '>= reserve -> OK'}"}
    try:
        json.dump(out, open(LIVE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    except Exception as e:
        print(f"ecriture live impossible: {e}"); return 2
    print(out["message"])
    return 0
if __name__ == "__main__":
    raise SystemExit(main())

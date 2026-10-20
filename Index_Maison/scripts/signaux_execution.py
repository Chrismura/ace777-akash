#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""signaux_execution.py — SIGNAUX D'EXÉCUTION (chantier 20/10, GO 1+2 Christophe).

1. ρ IMBALANCE (Cartea 2015, confirmé crypto 1,9M obs) : ρ = (bid-ask)/(bid+ask)
   sur les murs satellite. ρ>0 = pression acheteuse. Honnêteté lue à l'étude :
   le mouvement prédit est < spread, horizon secondes → usage = TIMER les
   entrées Hulk (l'embuscade), JAMAIS un avis 24h.
   Filtre spoof : notre spoof_pct par paire (universe) — ρ + spoof élevé = façade.
2. SIZING PAR VOL (Engle/GARCH, RiskMetrics EWMA λ=0.94 sur rendements daily) :
   mise_mult = clamp(vol_médiane_univers / vol_paire, 0.25, 2). Jour volatil =
   mise réduite. Klines cachées 12h (thermo/cache_klines_vol.json, R10-friendly).

Lecture seule du marché. Écrit thermo/signaux_execution.json (lu par la page
En vol — pour ne pas oublier, GO Christophe).
Usage : python3 signaux_execution.py
IA=Buffy (Muse Spark 1.3, Freebuff).
"""
from __future__ import annotations
import json, math, sys, time, urllib.request
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
THERMO = RACINE / "Index_Maison" / "thermo"
OUT = THERMO / "signaux_execution.json"
CACHE = THERMO / "cache_klines_vol.json"
LAMBDA = 0.94
CACHE_TTL = 12 * 3600


def klines_cached(sym: str) -> list[float]:
    now = time.time()
    cache = {}
    try:
        cache = json.loads(CACHE.read_text(encoding="utf-8"))
    except Exception:
        pass
    e = cache.get(sym)
    if e and now - float(e.get("ts", 0)) < CACHE_TTL:
        return [float(x) for x in e["closes"]]
    url = f"https://api.mexc.com/api/v3/klines?symbol={sym}&interval=1d&limit=100"
    req = urllib.request.Request(url, headers={"User-Agent": "signaux-exec/1.0"})
    with urllib.request.urlopen(req, timeout=20) as r:
        ks = json.loads(r.read())
    closes = [float(k[4]) for k in ks]
    cache[sym] = {"ts": now, "closes": closes}
    CACHE.write_text(json.dumps(cache), encoding="utf-8")
    return closes


def ewma_vol(closes: list[float]) -> float | None:
    rets = [math.log(closes[i + 1] / closes[i]) for i in range(len(closes) - 1) if closes[i] > 0]
    if len(rets) < 10:
        return None
    var = sum(r * r for r in rets[:10]) / 10
    for r in rets[10:]:
        var = LAMBDA * var + (1 - LAMBDA) * r * r
    return math.sqrt(var) * 100  # %/j


def main() -> int:
    sat = json.loads((RACINE / "hulk-mexc" / "runs" / "aspiration_live.json").read_text())
    paires = sat.get("paires") or {}
    try:
        univ = json.loads((RACINE / "hulk-mexc" / "strategie" / "universe_profils.json").read_text())
    except Exception:
        univ = {}
    vols: dict[str, float] = {}
    for sym in paires:
        try:
            v = ewma_vol(klines_cached(sym))
            if v:
                vols[sym] = v
        except Exception as ex:
            print(f"[signaux] vol {sym} HS : {ex}", file=sys.stderr)
    med = sorted(vols.values())[len(vols) // 2] if vols else 1.0
    lignes = []
    for sym, p in paires.items():
        bid = float(p.get("wall_bid_usdt") or 0.0)
        ask = float(p.get("wall_ask_usdt") or 0.0)
        rho = round((bid - ask) / (bid + ask), 3) if (bid + ask) > 0 else 0.0
        spoof = float((univ.get(sym) or {}).get("spoof_pct") or 0.0)
        vol = vols.get(sym)
        mult = round(max(0.25, min(2.0, med / vol)), 2) if vol else 1.0
        if abs(rho) >= 0.2 and spoof < 5.0:
            lect = f"pression {'acheteuse' if rho > 0 else 'vendeuse'} (entrée timer OK)"
        elif abs(rho) >= 0.2:
            lect = "imbalance FAÇADE probable (spoof élevé) — ne pas timer dessus"
        else:
            lect = "carnet équilibré — pas de timing"
        lignes.append({"pair": sym, "rho": rho, "wall_bid": round(bid), "wall_ask": round(ask),
                       "spoof_pct": spoof, "vol_pred": round(vol, 3) if vol else None,
                       "mise_mult": mult, "regime": p.get("regime", "?"), "lecture": lect})
    lignes.sort(key=lambda l: -abs(l["rho"]))
    OUT.write_text(json.dumps({"ts": datetime.now(timezone.utc).isoformat(),
                               "vol_mediane_univers": round(med, 3),
                               "lignes": lignes}, ensure_ascii=False, indent=1), encoding="utf-8")
    for l in lignes[:8]:
        print(l["pair"], "ρ=" + str(l["rho"]), "spoof=" + str(l["spoof_pct"]) + "%",
              "vol=" + str(l["vol_pred"]), "mise×" + str(l["mise_mult"]), "-", l["regime"])
    return 0


if __name__ == "__main__":
    sys.exit(main())

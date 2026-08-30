#!/usr/bin/env python3
"""
profil_liquidite.py — PROFIL DE VOLUME / LIQUIDITÉ BTC (28/08, GO Christophe).

Idée (Christophe, validée sur 300j de klines réelles) : la liquidité se voit dans
le VOLUME ÉCHANGÉ par niveau de prix. Les zones où le volume est dense = là où le
marché "vit" (support/ancrage). Les zones où il est vide = murs/résistance (le prix
y passe vite, ou y est bloqué).

Calcule et expose en JSON (pour le futur détecteur de régime) :
  - POC (Point of Control)      : le prix le plus échangé = l'ANCRAGE du marché
  - Zone de valeur (70%)        : la fourchette où 70% du volume s'est fait
  - Murs hauts / murs bas       : zones de faible volume qui bloquent (résistances)
                                  ou zones de volume massif qui soutiennent
  - Verdict                      : prix actuel vs ancrage + murs (au-dessus/en-dessous)

Données : klines 1j Binance (300j) — téléchargées si absentes, sinon cache.
Usage :
  python3 profil_liquidite.py            # calcule + affiche
  python3 profil_liquidite.py --json     # sortie JSON vers runs/liquidite_profil.json

OUTIL DE RECHERCHE + EXPOSITION — n'exécute rien sur le live.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNS = ROOT / "runs"
CACHE = Path("/tmp/btc_daily.json")
OUT = RUNS / "liquidite_profil.json"

BIN = 500  # taille du bin de prix en USDT (500$ de précision)


def fetch_btc_daily(days: int = 300) -> list[dict]:
    """Klines 1j BTC Binance, cache local /tmp/btc_daily.json."""
    if CACHE.exists():
        try:
            raw = json.loads(CACHE.read_text())
            if len(raw) >= days:
                return raw
        except Exception:
            pass
    url = (f"https://api.binance.com/api/v3/klines?"
           f"symbol=BTCUSDT&interval=1d&limit={days}")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    raw = json.load(urllib.request.urlopen(req, timeout=25))
    CACHE.write_text(json.dumps(raw))
    return raw


def volume_profile(raw: list[dict], bin_size: int = BIN) -> tuple[dict, float, float]:
    """Répartit le volume de chaque bougie sur sa fourchette de prix.

    Retour : (bins {prix: volume}, max_volume, volume_total).
    """
    bins: dict[int, float] = defaultdict(float)
    total = 0.0
    for k in raw:
        o, h, l, c = float(k[1]), float(k[2]), float(k[3]), float(k[4])
        v = float(k[5])
        lo = min(o, c, l)
        hi = max(o, c, h)
        lo_b = int(lo // bin_size) * bin_size
        hi_b = int(hi // bin_size) * bin_size
        n = max(1, (hi_b - lo_b) // bin_size)
        for b in range(lo_b, hi_b + bin_size, bin_size):
            bins[b] += v / n
            total += v / n
    maxv = max(bins.values()) if bins else 1.0
    return bins, maxv, total


def poc_and_value_area(bins: dict, total: float, pct: float = 0.70) -> dict:
    """POC = bin de volume max. Zone de valeur = fourchette contenant pct% du volume
    en partant du POC (méthode classique des profils de marché)."""
    poc = max(bins, key=bins.get)
    ordered = sorted(bins.items(), key=lambda kv: -kv[1])
    target = total * pct
    acc = 0.0
    core = []
    for b, v in ordered:
        core.append(b)
        acc += v
        if acc >= target:
            break
    va_lo = min(core)
    va_hi = max(core)
    return {
        "poc": poc,
        "va_lo": va_lo,
        "va_hi": va_hi,
        "n_bins": len(bins),
        "volume_total": total,
    }


def find_walls(bins: dict, va_lo: int, va_hi: int, last_price: float) -> dict:
    """Murs = transitions brutales de densité de volume au-dessus/en-dessous de la
    zone de valeur. Un mur HAUT = volume qui chute (vide = résistance). Un mur BAS
    = volume qui chute en dessous (peu d'échanges sous le support)."""
    prices = sorted(bins)
    # densité moyenne de la zone de valeur
    va_vals = [bins[p] for p in prices if va_lo <= p <= va_hi]
    va_density = sum(va_vals) / len(va_vals) if va_vals else 0

    # mur haut : premier "vide" de volume au-dessus du prix actuel (où le volume
    # chute sous 30% de la densité VA), cherché dans TOUT le profil au-dessus du prix.
    # Ça capte le mur immédiat (ex. 80k) même s'il est dans la zone de valeur.
    wall_high = None
    above_px = [(p, v) for p, v in sorted(bins.items()) if p > last_price]
    for p, v in above_px:
        if v < va_density * 0.30:
            wall_high = p
            break

    # étage suivant : là où le volume REMONTE au-dessus du mur (vraie résistance épaisse)
    second_floor = None
    if wall_high is not None:
        for p, v in above_px:
            if p > wall_high and v > va_density * 0.6:
                second_floor = p
                break

    below = [(p, bins[p]) for p in prices if p < va_lo]
    # mur bas : le prix le plus bas avec du volume significatif (le "sol")
    floor = None
    for p, v in reversed(below):
        if v > va_density * 0.5:
            floor = p
            break

    return {"wall_high": wall_high, "second_floor": second_floor, "floor": floor}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true", help="écrire runs/liquidite_profil.json")
    args = ap.parse_args()

    raw = fetch_btc_daily()
    closes = [float(k[4]) for k in raw]
    last = closes[-1]
    ts = raw[-1][0]

    bins, maxv, total = volume_profile(raw)
    va = poc_and_value_area(bins, total)
    walls = find_walls(bins, va["va_lo"], va["va_hi"], last)

    # verdict : prix vs structure
    rel = "au-dessus" if last > va["va_hi"] else ("dans" if last >= va["va_lo"] else "en-dessous")
    verdict = (
        f"Prix {last:,.0f}$ = {rel} de la zone de valeur "
        f"[{va['va_lo']:,.0f}-{va['va_hi']:,.0f}$], ancrage POC {va['poc']:,.0f}$"
    )
    if walls["wall_high"] and last < walls["wall_high"]:
        verdict += f" | SOUS le mur {walls['wall_high']:,.0f}$ → résistance au-dessus"
    if walls["floor"] and last > walls["floor"]:
        verdict += f" | support épais à {walls['floor']:,.0f}$"

    out = {
        "ts": datetime.fromtimestamp(ts / 1000, tz=timezone.utc).isoformat(),
        "btc_last": round(last, 2),
        "poc_anchor": va["poc"],
        "value_area": [va["va_lo"], va["va_hi"]],
        "walls": walls,
        "verdict": verdict,
        "note": "Profil de volume 300j (klines 1j Binance). POC = prix le plus échangé "
                "(ancrage). VA = zone de valeur 70%. wall_high = 1er mur de résistance, "
                "second_floor = étage suivant, floor = support épais.",
    }

    if args.json:
        RUNS.mkdir(parents=True, exist_ok=True)
        OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1))
        print(f"écrit {OUT}")

    print(f"BTC {datetime.fromtimestamp(ts/1000, tz=timezone.utc):%Y-%m-%d} — dernier {last:,.0f}$")
    print(f"  ANCRAGE (POC)      : {va['poc']:>10,.0f}$  ← le prix le plus échangé")
    print(f"  Zone de valeur 70% : [{va['va_lo']:,.0f}$ — {va['va_hi']:,.0f}$]")
    if walls["floor"]:
        print(f"  Support épais (sol) : {walls['floor']:>10,.0f}$")
    if walls["wall_high"]:
        print(f"  Mur haut (résist.)  : {walls['wall_high']:>10,.0f}$  ← le volume chute ici")
    if walls["second_floor"]:
        print(f"  Étage suivant       : {walls['second_floor']:>10,.0f}$  ← volume qui remonte")
    print(f"  VERDICT : {verdict}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

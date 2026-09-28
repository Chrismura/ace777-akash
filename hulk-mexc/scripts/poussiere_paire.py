#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""poussiere_paire.py — Poussière INDIVIDUELLE par paire (06/09/2026, consigne Christophe).

Le `poussiere_taux_fantome` du croisement est un indicateur PANIER (identique pour toutes
les paires au même instant — vérifié 06/09). Ce script calcule la poussière PROPRE à chaque
paire, directement dans le carnet MEXC :

- BANDE ±2% autour du mid (profondeur réelle) ;
- PART DE POUSSIÈRE : % de la valeur des niveaux bid/ask formés de petits ordres (< POUSSIERE_USD) ;
- ÉVANESCENCE (2ᵉ snapshot à +WAIT_S) : % de la valeur des petits niveaux qui a DISPARU
  → le vrai « fantôme » de cette paire (murs de paille qui s'effacent).

USAGE :
  python3 scripts/poussiere_paire.py            # CORE-20 complet
  python3 scripts/poussiere_paire.py CCUSDT ... # paires ciblées

Sorties : runs/poussiere_paires.json (dernier état) + runs/poussiere_paires_hist.jsonl (historique).
Ne modifie rien dans Hulk : pure mesure. À relancer « de temps en temps » (check-up fiches).
"""
import datetime
import json
import os
import sys
import time
import urllib.parse
import urllib.request

RUNS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "runs")

CORE_PAIRS = [
    "BTCUSDT", "ETHUSDT", "XRPUSDT", "HBARUSDT", "RIZEUSDT", "ZBCNUSDT",
    "WUSDT", "REDUSDT", "CCUSDT", "PYTHUSDT", "BIOUSDT", "KITEUSDT",
    "TELUSDT", "CHIPUSDT", "RWAINCUSDT", "EDELUSDT", "QNTUSDT", "FLUIDUSDT",
    "RWAUSDT", "MNSRYUSDT",
]

BANDE_PCT = 2.0        # bande autour du mid
POUSSIERE_USD = 200.0  # un niveau < 200$ = poussière
WAIT_S = 75            # délai entre les 2 snapshots (évanescence)


def gj(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=25) as resp:
        return json.loads(resp.read().decode("utf-8"))


def depth(pair, limit=1000):
    q = urllib.parse.urlencode({"symbol": pair, "limit": limit})
    try:
        return gj(f"https://api.mexc.com/api/v3/depth?{q}")
    except Exception:
        return None


def ticker(pair):
    q = urllib.parse.urlencode({"symbol": pair})
    try:
        d = gj(f"https://api.mexc.com/api/v3/ticker/24hr?{q}")
        return float(d.get("lastPrice") or 0)
    except Exception:
        return None


def bande(sides, mid, band_pct):
    """Agrège les niveaux d'un côté du book dans la bande ±bande_pct. → stats."""
    lo, hi = mid * (1 - band_pct / 100), mid * (1 + band_pct / 100)
    total_v = dust_v = 0.0
    n_levels = n_dust = 0
    levels = []
    for price_s, qty_s in sides:
        price = float(price_s)
        if price <= 0:
            continue
        if not (lo <= price <= hi):
            continue
        v = price * float(qty_s)
        levels.append((price, v))
        total_v += v
        n_levels += 1
        if v < POUSSIERE_USD:
            dust_v += v
            n_dust += 1
    levels.sort(key=lambda x: x[0], reverse=True)  # pour les bids (côté proche du mid)
    return {
        "n_levels": n_levels, "valeur_usd": round(total_v, 1),
        "n_poussiere": n_dust,
        "part_poussiere_pct": round(dust_v / total_v * 100, 1) if total_v > 0 else None,
        "mur_top_usd": round(max(v for _, v in levels), 1) if levels else None,
        "_levels": {f"{p:.10g}": v for p, v in levels},  # pour la comparaison P2
    }


def mesure(pair):
    mid = ticker(pair)
    if not mid:
        return None
    d = depth(pair, 1000)
    if not d:
        return None
    bids = bande(d.get("bids") or [], mid, BANDE_PCT)
    asks = bande(d.get("asks") or [], mid, BANDE_PCT)
    return {"mid": mid, "bids": bids, "asks": asks}


def evanescence(p1, p2):
    """% de la valeur des petits niveaux bids P1 disparus en P2 (mêmes prix)."""
    l1, l2 = p1["bids"].get("_levels") or {}, p2["bids"].get("_levels") or {}
    dust1 = {p: v for p, v in l1.items() if v < POUSSIERE_USD}
    if not dust1:
        return None
    gone = sum(v for p, v in dust1.items() if p not in l2)
    return round(gone / sum(dust1.values()) * 100, 1)


def main():
    pairs = sys.argv[1:] or CORE_PAIRS
    now = datetime.datetime.now(datetime.timezone.utc)
    print(f"[..] phase 1 : profondeur ±{BANDE_PCT}% pour {len(pairs)} paires…")
    snap1 = {}
    for p in pairs:
        m = mesure(p)
        if m:
            snap1[p] = m
            b, a = m["bids"], m["asks"]
            print(f"  {p:12s} mid {m['mid']:.10g} · pouss bid {b['part_poussiere_pct']}% "
                  f"({b['n_poussiere']}/{b['n_levels']} niv) · ask {a['part_poussiere_pct']}% · "
                  f"mur bid {b['mur_top_usd']}$ · prof bid {b['valeur_usd']}$")
        else:
            print(f"  {p:12s} [ERR] pas de données")
    print(f"[..] attente {WAIT_S}s pour le 2ᵉ snapshot (évanescence)…")
    time.sleep(WAIT_S)
    out = {"ts": now.strftime("%Y-%m-%dT%H:%M:%SZ"), "bande_pct": BANDE_PCT,
           "poussiere_usd": POUSSIERE_USD, "wait_s": WAIT_S, "paires": {}}
    for p, m in snap1.items():
        m2 = mesure(p)
        ev = evanescence(m, m2) if m2 else None
        rec = {
            "mid": m["mid"],
            "poussiere_bid_pct": m["bids"]["part_poussiere_pct"],
            "poussiere_ask_pct": m["asks"]["part_poussiere_pct"],
            "niveaux_bid": m["bids"]["n_levels"], "niveaux_ask": m["asks"]["n_levels"],
            "profondeur_bid_usd": m["bids"]["valeur_usd"],
            "profondeur_ask_usd": m["asks"]["valeur_usd"],
            "mur_bid_top_usd": m["bids"]["mur_top_usd"],
            "evanescence_bid_pct": ev,
        }
        out["paires"][p] = rec
        print(f"[OK] {p}: poussière bid {rec['poussiere_bid_pct']}% · évanescence {ev}%")
    with open(os.path.join(RUNS, "poussiere_paires.json"), "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    with open(os.path.join(RUNS, "poussiere_paires_hist.jsonl"), "a", encoding="utf-8") as fh:
        fh.write(json.dumps(out, ensure_ascii=False) + "\n")
    print(f"[OK] runs/poussiere_paires.json + hist ({len(out['paires'])} paires)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

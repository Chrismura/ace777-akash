#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
couts_communs.py — §24 (28/10/2026, ORDRE Christophe « fini le bidouillage »).
================================================================================
LE modèle de coûts unique, partagé par le chiffrage ET le cockpit.
Avant : 3 chiffres coexistaient — cockpit « frais » 4,99 $ (5bps/fill, spread
ignoré → net 39,28 $ surestimé), chiffrage 15,11 $ (bookings seuls), colonne
journal 20,74 $ (partielle, 350/653 fills). Plus jamais ça.

RÈGLE DÉCLARÉE : chaque gain réalisé (booking) porte son aller-retour —
  coût = notional × (2 × 5 bps + spread),
spread = colonne `spread_bps` si présente, sinon médiane du profil, sinon 15 bps.
Les achats encore en sac ne portent rien (coût payé à la sortie, avec le gain).
Frais et spread sont rendus SÉPARÉS pour que chaque tableau montre la même
décomposition : brut − frais − spread = net.
Lecture seule, 0 ordre.
"""
from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path

FEE_BPS_COTE = 5.0
SEUIL_BOOKING = 1e-9
SPREAD_DEFAUT_BPS = 15.0


def _profils(racine_hulk: Path) -> dict:
    try:
        d = json.loads((racine_hulk / "strategie" / "universe_profils.json").read_text(encoding="utf-8"))
        return {k: v for k, v in d.items() if isinstance(v, dict) and "calib" in v}
    except Exception:
        return {}


def spread_bps(row: dict, profils: dict) -> tuple[float, bool]:
    """(spread, mesure_vraie). Colonne d'abord, profil ensuite, défaut sinon."""
    sp = (row.get("spread_bps") or "").strip()
    if sp:
        try:
            return float(sp), ((row.get("spread_source") or "").strip() == "asp")
        except ValueError:
            pass
    try:
        return float((profils.get(row.get("pair")) or {}).get("spread_bps_med") or SPREAD_DEFAUT_BPS), False
    except Exception:
        return SPREAD_DEFAUT_BPS, False


def couts_journal(csv_path: Path, racine_hulk: Path) -> dict:
    """Coûts du journal, modèle unique. Un booking = |pnl_usdt| > 0."""
    profils = _profils(racine_hulk)
    frais = spread = brut = 0.0
    n = n_mesure = 0
    par_paire: dict[str, dict] = defaultdict(lambda: {"n": 0, "frais": 0.0, "spread": 0.0})
    with open(csv_path, encoding="utf-8", errors="replace") as f:
        for r in csv.DictReader(f):
            try:
                pnl = float(r.get("pnl_usdt") or 0.0)
            except (TypeError, ValueError):
                continue
            if abs(pnl) <= SEUIL_BOOKING:
                continue
            try:
                notional = float(r.get("qty") or 0.0) * float(r.get("price") or 0.0)
            except (TypeError, ValueError):
                notional = 0.0
            if notional <= 0:
                continue
            sp, mesure = spread_bps(r, profils)
            c_frais = notional * (2 * FEE_BPS_COTE) / 10000.0
            c_spread = notional * sp / 10000.0
            brut += pnl
            frais += c_frais
            spread += c_spread
            n += 1
            n_mesure += 1 if mesure else 0
            d = par_paire[r.get("pair") or "?"]
            d["n"] += 1
            d["frais"] += c_frais
            d["spread"] += c_spread
    couts = frais + spread
    return {
        "brut": round(brut, 2), "frais": round(frais, 2), "spread": round(spread, 2),
        "couts": round(couts, 2), "net": round(brut - couts, 2),
        "n_bookings": n, "n_spread_mesure": n_mesure,
        "par_paire": {p: {"n": d["n"], "frais": round(d["frais"], 2),
                          "spread": round(d["spread"], 2),
                          "couts": round(d["frais"] + d["spread"], 2)}
                      for p, d in par_paire.items()},
    }

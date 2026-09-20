#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ofi_calc.py — CALCULATEUR OFI NORMALISÉ (09/09/2026, GO Christophe prop.1).

Lit la QUEUE du ledger L2 SNAPS (runs/L2_20260903_SNAPS.csv, snaps ~1 s écrits
par le superviseur L2) et calcule l'OFI top-of-book au sens
Cont–Kukanov–Stoikov, NORMALISÉ par la profondeur visible.

Règle d'art issue du test du 08/09 (150 000 snaps réels) : l'OFI BRUT est du
bruit (corr −0.012, signe correct 52 %) → la normalisation par la profondeur
est OBLIGATOIRE avant toute interprétation.

Fenêtre : 120 derniers snaps (~2 min), découpée en 4 agrégats de 30 s.
Détection ABSORPTION (candidat iceberg) : sur une fenêtre 30 s,
|ofi_norm| ≥ 0.15 ET |Δprix| ≤ 1 bps (le prix stagne alors que le flow
s'accélère) — à CONFIRMER par le re-remplissage au même prix dans
L2_20260903_MURS.csv (cf. module cortana_microstructure).

OBSERVATION SEULE : ce script n'émet AUCUNE alerte (Cortana décide,
verdicteur_micro.py mesure). Stdlib, lecture par queue (économique),
fail-open, idempotent, plist com.ace777.ofi-calc (60 s).
Sorties : data/ofi_latest.json + data/ofi_historique.jsonl
"""
import csv
import io
import json
import os
import sys
import argparse
from datetime import datetime, timezone

HOME = os.path.expanduser("~")
INDEX = os.path.join(HOME, "ace777-test-day1", "Index_Maison")
DATA = os.path.join(INDEX, "data")
SNAPS = os.path.join(HOME, "ace777-test-day1", "runs", "L2_20260903_SNAPS.csv")
OUT_LATEST = os.path.join(DATA, "ofi_latest.json")
OUT_HIST = os.path.join(DATA, "ofi_historique.jsonl")

TAIL_BYTES = 1_200_000      # queue du CSV lue à chaque passage (~économique)
WINDOW_SNAPS = 120          # fenêtre d'analyse (~2 min à 1 snap/s)
CHUNK = 30                  # agrégats de 30 s
ABS_ORB = 0.15              # seuil |ofi_norm| pour candidate absorption
ABS_BPS = 1.0               # |Δprix| max (bps) pour prix « stagnant »


def lire_queue_snaps(n_max=WINDOW_SNAPS * 2):
    """Lit les dernières lignes du CSV SNAPS (lecture partielle, robuste)."""
    try:
        size = os.path.getsize(SNAPS)
        with open(SNAPS, "rb") as f:
            f.seek(max(0, size - TAIL_BYTES))
            brut = f.read().decode("utf-8", errors="replace")
        lignes = brut.splitlines()
        HEADER = "ts,mid,spread,bid1_px,bid1_sz,ask1_px,ask1_sz,med_notional,mur_seuil,n_bids,n_asks"
        if lignes and "ts,mid" in lignes[0]:
            pass  # la queue tombe sur le header : on le garde
        else:
            lignes = lignes[1:] if len(lignes) > 1 else []  # 1re ligne tronquée → jetée
            lignes.insert(0, HEADER)
        rows = []
        for r in csv.DictReader(io.StringIO("\n".join(lignes))):
            try:
                rows.append({
                    "ts": r["ts"],
                    "mid": float(r["mid"]),
                    "bid_px": float(r["bid1_px"]),
                    "ask_px": float(r["ask1_px"]),
                    "bid_sz": float(r["bid1_sz"]),
                    "ask_sz": float(r["ask1_sz"]),
                })
            except (KeyError, ValueError):
                continue
        return rows[-n_max:]
    except FileNotFoundError:
        return []


def _e(prev, cur):
    db = (cur["bid_sz"] - prev["bid_sz"]) if cur["bid_px"] >= prev["bid_px"] else 0.0
    da = (cur["ask_sz"] - prev["ask_sz"]) if cur["ask_px"] <= prev["ask_px"] else 0.0
    return db - da


def agreger(rows):
    """OFI normalisé + Δprix sur une liste de snaps consécutifs."""
    if len(rows) < 3:
        return None
    e_sum = 0.0
    depth_sum = 0.0
    for p, c in zip(rows, rows[1:]):
        e_sum += _e(p, c)
        depth_sum += p["bid_sz"] + p["ask_sz"]
    if depth_sum <= 0:
        return None
    ofi_norm = e_sum / depth_sum
    d_bps = (rows[-1]["mid"] - rows[0]["mid"]) / rows[0]["mid"] * 1e4
    return {"n": len(rows), "ofi_norm": round(ofi_norm, 4),
            "delta_bps": round(d_bps, 2)}


def verdict_fenetre(agg):
    """Classification honnête (NEUTRE par défaut — discipline module)."""
    if agg is None:
        return "DONNEES_INSUFFISANTES"
    if abs(agg["ofi_norm"]) < ABS_ORB or abs(agg["delta_bps"]) > ABS_BPS:
        # soit le flow est faible, soit le prix BOUGE déjà (pas une absorption)
        if abs(agg["ofi_norm"]) >= ABS_ORB:
            return "PRESSION_ACHAT" if agg["ofi_norm"] > 0 else "PRESSION_VENTE"
        return "NEUTRE"
    return "ABSORPTION_SUSPECTE_ACHAT" if agg["ofi_norm"] > 0 else "ABSORPTION_SUSPECTE_VENTE"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--silencieux", action="store_true")
    args = ap.parse_args()

    rows = lire_queue_snaps()
    if len(rows) < CHUNK * 2:
        out = {"ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
               "ok": False, "detail": f"snaps insuffisants ({len(rows)})"}
        with open(OUT_LATEST, "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=1)
        return 0

    # fenêtre principale = 120 derniers snaps, 4 agrégats de 30 s
    fen = rows[-WINDOW_SNAPS:]
    agg_global = agreger(fen)
    chunks = []
    for i in range(0, WINDOW_SNAPS, CHUNK):
        a = agreger(fen[i:i + CHUNK])
        if a:
            a["verdict"] = verdict_fenetre(a)
            chunks.append(a)

    out = {
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": os.path.basename(SNAPS),
        "ok": True,
        "methode": "OFI top-of-book CKS normalisé par profondeur — brut interdit (test 08/09)",
        "fenetre_globale": {**(agg_global or {}), "verdict": verdict_fenetre(agg_global)},
        "agregats_30s": chunks,
        "absorption_candidate": any(c["verdict"].startswith("ABSORPTION") for c in chunks),
        "note": "absorption à confirmer par re-remplissage MURS — Cortana décide, jamais ce script",
    }
    with open(OUT_LATEST, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    with open(OUT_HIST, "a", encoding="utf-8") as f:
        f.write(json.dumps(out, ensure_ascii=False) + "\n")

    if not args.silencieux:
        g = out["fenetre_globale"]
        print(f"[ofi] fenêtre {g.get('n','?')} snaps | ofi_norm={g.get('ofi_norm')} "
              f"| Δ={g.get('delta_bps')} bps → {g.get('verdict')}")
        for c in chunks:
            print(f"  30s: ofi_norm={c['ofi_norm']:+.4f} Δ={c['delta_bps']:+.2f}bps → {c['verdict']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

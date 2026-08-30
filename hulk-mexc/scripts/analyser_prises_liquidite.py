#!/usr/bin/env python3
"""
analyser_prises_liquidite.py — ANALYSE des prises de liquidité sur les données
EXISTANTES (la sonde aspiration collecte depuis le 16/08 : ASPIRATION_CALIB_*.csv
+ OBSERVATION_MURS_*.csv = ~60k lignes).

Thèse de Christophe (28/08) : « un trend peut se déclencher sur la PRISE de
liquidité ». Deux cas :
  - PRISE AU SUD  (mur bid fondu, drop_bid_pct_per_s ≥ seuil) : le prix a balayé
    les achats → soit REBOND (dernier vendeur épuisé = retournement) soit
    CONTINUATION baissière (le mur cède, le prix descend à travers).
  - PRISE AU NORD (mur ask fondu, drop_ask_pct_per_s ≥ seuil) : symétrique.

Pour chaque prise détectée dans les CSVs, ce script :
  1. calcule la DESCENTE AVANT (% du prix sur ~30 min avant la prise) — le contexte
  2. calcule le MOUVEMENT APRÈS (+1h et +3h) depuis la série de prix de la paire
  3. classe REBOND / CONTINUATION / PLAT
  4. agrège par côté, par vitesse (sèche vs lente), par descente avant → verdict

AUCUN process en plus : lit les CSVs que la sonde du moteur écrit déjà.
Usage :
  python3 analyser_prises_liquidite.py [--seuil 5.0] [--min-mur 200]
"""
from __future__ import annotations

import argparse
import csv
import glob
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNS = ROOT / "runs"


def parse_ts(s: str) -> datetime:
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def load_series() -> tuple[list[dict], dict[str, list[tuple[datetime, float]]]]:
    """Charge tous les CSVs. Retour : (événements bruts triés, séries prix par paire)."""
    events: list[dict] = []
    series: dict[str, list[tuple[datetime, float]]] = defaultdict(list)
    files = sorted(glob.glob(str(RUNS / "ASPIRATION_CALIB_*.csv"))) + \
            sorted(glob.glob(str(RUNS / "OBSERVATION_MURS_*.csv")))
    for f in files:
        try:
            with open(f, newline="") as fh:
                for r in csv.DictReader(fh):
                    ts = r.get("ts", "")
                    pair = (r.get("pair") or "").strip().upper()
                    if not ts or not pair:
                        continue
                    try:
                        t = parse_ts(ts)
                    except Exception:
                        continue
                    def fnum(*keys):
                        for k in keys:
                            v = r.get(k)
                            if v not in (None, ""):
                                try:
                                    return float(v)
                                except Exception:
                                    pass
                        return None
                    px = fnum("price")
                    if px:
                        series[pair].append((t, px))
                    events.append({
                        "ts": t, "pair": pair,
                        "db": fnum("drop_bid_pct_per_s") or 0.0,
                        "da": fnum("drop_ask_pct_per_s") or 0.0,
                        "wb": fnum("wall_bid_usdt") or 0.0,
                        "wa": fnum("wall_ask_usdt") or 0.0,
                        "px": px,
                    })
        except Exception:
            continue
    for p in series:
        series[p].sort(key=lambda x: x[0])
    events.sort(key=lambda x: x["ts"])
    return events, series


def descente_avant(series: list[tuple[datetime, float]], t: datetime,
                   fenetre: timedelta = timedelta(minutes=30)) -> float | None:
    """% de baisse du prix dans la fenêtre avant t (les échantillons les plus vieux
    de la fenêtre vs le plus récent avant t)."""
    before = [(tt, px) for tt, px in series if t - fenetre <= tt < t]
    if len(before) < 5:
        return None
    first_px = before[0][1]
    last_px = before[-1][1]
    if first_px <= 0:
        return None
    return (last_px / first_px - 1) * 100


def px_after(series: list[tuple[datetime, float]], t: datetime,
             hours: float) -> float | None:
    target = t + timedelta(hours=hours)
    for tt, px in series:
        if tt >= target:
            return px
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seuil", type=float, default=5.0, help="seuil de prise %/s (défaut 5.0)")
    ap.add_argument("--min-mur", type=float, default=200.0, help="mur min USDT (défaut 200)")
    args = ap.parse_args()

    events, series = load_series()
    print(f"CSVs lus : {len(events)} mesures, {len(series)} paires "
          f"({min(e['ts'] for e in events):%m-%d} → {max(e['ts'] for e in events):%m-%d})")

    # détecter les prises : un événement où un mur fond vite ET le mur est assez gros
    prises = []
    for e in events:
        max_drop = max(e["db"], e["da"])
        if max_drop < args.seuil:
            continue
        if max(e["wb"], e["wa"]) < args.min_mur:
            continue
        cote = "SUD" if e["db"] >= e["da"] else "NORD"
        mur = e["wb"] if cote == "SUD" else e["wa"]
        prises.append({**e, "cote": cote, "mur": mur, "vitesse": max_drop})

    # dédup : plusieurs mesures du même événement (même paire, même prise sur ~60s)
    dedup: list[dict] = []
    for p in prises:
        if dedup and dedup[-1]["pair"] == p["pair"] and \
           (p["ts"] - dedup[-1]["ts"]).total_seconds() < 60 and \
           dedup[-1]["cote"] == p["cote"]:
            continue
        dedup.append(p)
    prises = dedup

    print(f"Prises détectées : {len(prises)} (seuil {args.seuil}%/s, mur ≥ {args.min_mur}$)\n")

    if not prises:
        print("Aucune prise avec ces seuils — essaie --seuil plus bas (ex. 3.0).")
        return 0

    print(f"{'ts':<22}{'pair':<12}{'cote':<5}{'vit':>6}{'mur$':>10}{'descAv':>8}{'+1h':>8}{'+3h':>8}  verdict")
    print("-" * 90)
    by_cote: dict[str, list] = defaultdict(list)
    for p in prises:
        s = series.get(p["pair"], [])
        desc = descente_avant(s, p["ts"])
        px1 = px_after(s, p["ts"], 1)
        px3 = px_after(s, p["ts"], 3)
        m1 = (px1 / p["px"] - 1) * 100 if px1 and p["px"] else None
        m3 = (px3 / p["px"] - 1) * 100 if px3 and p["px"] else None
        if m1 is None and m3 is None:
            verdict = "?"
        else:
            best = max([m for m in (m1, m3) if m is not None])
            worst = min([m for m in (m1, m3) if m is not None])
            verdict = "REBOND" if best > 0.3 else ("CONTINUATION" if worst < -0.3 else "PLAT")
        p.update({"desc": desc, "m1": m1, "m3": m3, "verdict": verdict})
        by_cote[p["cote"]].append(p)

        desc_s = f"{desc:.1f}%" if desc is not None else "—"
        m1_s = f"{m1:+.1f}%" if m1 is not None else "—"
        m3_s = f"{m3:+.1f}%" if m3 is not None else "—"
        print(f"{p['ts']:%m-%d %H:%M}{'':<5}{p['pair']:<12}{p['cote']:<5}"
              f"{p['vitesse']:>5.1f}%{p['mur']:>10,.0f}{desc_s:>8}{m1_s:>8}{m3_s:>8}  {verdict}")

    print("\n=== VERDICT PAR CÔTÉ ===")
    for cote in ("SUD", "NORD"):
        arr = by_cote.get(cote, [])
        if not arr:
            print(f"  {cote}: aucune prise")
            continue
        n = len(arr)
        reb = sum(1 for r in arr if r["verdict"] == "REBOND")
        cont = sum(1 for r in arr if r["verdict"] == "CONTINUATION")
        print(f"  {cote}: {n} prises | REBOND {reb} ({reb/n*100:.0f}%) "
              f"| CONTINUATION {cont} ({cont/n*100:.0f}%) | PLAT {n-reb-cont}")

    print("\n=== THÈSE (prise SUD → rebond ?) ===")
    sud = by_cote.get("SUD", [])
    if sud:
        reb = sum(1 for r in sud if r["verdict"] == "REBOND")
        print(f"  Prise SUD → REBOND : {reb}/{len(sud)} = {reb/len(sud)*100:.0f}%")
        print(f"  (objectif : >50% sur ≥30 prises pour valider la thèse)")
        # croisement descente avant
        print("\n  Croisement avec la descente avant :")
        for seuil in (2.0, 5.0):
            sub = [r for r in sud if r.get("desc") is not None and r["desc"] <= -seuil]
            if sub:
                reb2 = sum(1 for r in sub if r["verdict"] == "REBOND")
                print(f"    descente ≥ {seuil:.0f}% avant : REBOND {reb2}/{len(sub)} = {reb2/len(sub)*100:.0f}%")
        # croisement vitesse (prise sèche vs lente)
        print("\n  Croisement avec la vitesse (sèche vs lente) :")
        sec = [r for r in sud if r["vitesse"] >= 15]
        lent = [r for r in sud if r["vitesse"] < 15]
        if sec:
            reb3 = sum(1 for r in sec if r["verdict"] == "REBOND")
            print(f"    PRISE SÈCHE (≥15%/s) : REBOND {reb3}/{len(sec)} = {reb3/len(sec)*100:.0f}%")
        if lent:
            reb4 = sum(1 for r in lent if r["verdict"] == "REBOND")
            print(f"    PRISE LENTE (<15%/s) : REBOND {reb4}/{len(lent)} = {reb4/len(lent)*100:.0f}%")
    else:
        print("  aucune prise SUD détectée avec ces seuils")

    print("\nNB : les données existent depuis le 16/08 — plus les jours passent, plus")
    print("l'échantillon grossit (objectif 30+ prises SUD pour une conclusion solide).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

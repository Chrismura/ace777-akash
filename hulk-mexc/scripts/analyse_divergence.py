#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""analyse_divergence.py — PROTOCOLE DIVERGENCE (29/08, Buffy).

Ce script est la MACHINE d'analyse répétable du patron « divergence avance/retard »
trouvé le 29/08 sur les données Hulk. Il se relance quand on veut (chaque jour,
chaque 6h) sur les données déjà accumulées dans runs/croisement_contexte.jsonl
(écrit par le moteur à chaque tick, ~1 point/pair/minute).

CE QUE ÇA DÉTECTE (3 angles complémentaires) :
  1. DIVERGENCE ACTUELLE  : chaque crypto vs la moyenne du panier (m6_pct),
     fenêtre 6h récentes vs 30h passées → qui surperforme / sousperforme.
  2. TIMING (lag)         : corrélation croisée horaire crypto vs panier, lag -4h..+4h
     → qui PRÉCÈDE le marché (signal) / qui SUIT (retardataire).
  3. SIGNAL DIRECTIONNEL  : corr(m6 crypto à H, delta panier H→H+4h)
     → + = la crypto précède une HAUSSE du panier (leader haussier)
       - = la crypto précède une BAISSE du panier (pompe-piège / sommet)

ARCHIVAGE : écrit runs/DIVERGENCE_<ts>.md (lisible par une autre IA) + console.

USAGE : python3 scripts/analyse_divergence.py
"""
import datetime
import json
import os
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "runs" / "croisement_contexte.jsonl"
OUTDIR = ROOT / "runs"
NOW = datetime.datetime.now(datetime.timezone.utc)

# ---- fenêtres (modifiables) ----
RECENT_H = 6          # fenêtre « récente » de divergence
PAST_H = 30           # fenêtre « passé » de comparaison
LAG_MIN, LAG_MAX = -4, 4   # plage de décalage horaire testée
FWD_H = 4             # horizon du signal directionnel
PIC_SEUIL = 6.0       # seuil de « pic » (m6 %) pour l'analyse pics précurseurs
SEUIL_SIGNAL = 0.15   # |corr| au-delà = signal retenu


def load():
    rows = []
    with open(SRC, encoding="utf-8") as f:
        for l in f:
            try:
                rows.append(json.loads(l))
            except Exception:
                pass
    return rows


def series(rows):
    by = {}
    for r in rows:
        p, ts, m6 = r.get("pair"), r.get("ts"), r.get("m6_pct")
        if p is None or ts is None or m6 is None:
            continue
        by.setdefault(p, {})[ts] = float(m6)
    return by


def hourly(by):
    """Bucket horaire par paire → moyenne m6."""
    hb = defaultdict(dict)
    for p, v in by.items():
        acc = defaultdict(list)
        for ts, m in v.items():
            acc[ts - (ts % 3600)].append(m)
        hb[p] = {h: sum(vv) / len(vv) for h, vv in acc.items()}
    return hb


def panier(hb, h):
    vals = [hb[p][h] for p in hb if h in hb[p]]
    return sum(vals) / len(vals) if vals else None


def corr(xs, ys):
    n = len(xs)
    if n < 5:
        return None
    mx, my = sum(xs) / n, sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    dx = sum((x - mx) ** 2 for x in xs) ** 0.5
    dy = sum((y - my) ** 2 for y in ys) ** 0.5
    return num / (dx * dy) if dx > 0 and dy > 0 else None


def main():
    rows = load()
    if not rows:
        print(f"[ERR] aucune donnée dans {SRC}")
        return 1
    by = series(rows)
    hb = hourly(by)
    hours = sorted(set().union(*[set(v.keys()) for v in hb.values()]))
    pan = {h: panier(hb, h) for h in hours}
    now = max(hours)
    h = 3600

    out = []
    out.append(f"# RAPPORT DIVERGENCE — {NOW.strftime('%Y-%m-%d %H:%MZ')}")
    out.append(f"\nSource : `{SRC.name}` · {len(rows)} points · {len(by)} paires · "
               f"fenêtres {RECENT_H}h vs {PAST_H}h · lag {LAG_MIN}h..{LAG_MAX}h · signal +{FWD_H}h")
    out.append("Interprétation : voir docs/PROTOCOLE_DIVERGENCE_20260829.md (relire avant d'utiliser).\n")

    # ---- 1. Divergence actuelle ----
    out.append("## 1. DIVERGENCE ACTUELLE (m6 vs panier)")
    res1 = []
    for p, v in by.items():
        pts = sorted(v.items())
        rec = [m for ts, m in pts if ts >= now - RECENT_H * h]
        past = [m for ts, m in pts if ts < now - RECENT_H * h]
        if not rec or not past:
            continue
        mrec = sum(pan.get(ts, 0) for ts in v if ts >= now - RECENT_H * h) / max(
            1, len([t for t in v if t >= now - RECENT_H * h]))
        mpast = sum(pan.get(ts, 0) for ts in v if ts < now - RECENT_H * h) / max(
            1, len([t for t in v if t < now - RECENT_H * h]))
        rec_m, past_m = sum(rec) / len(rec), sum(past) / len(past)
        res1.append((p, rec_m, past_m, rec_m - mrec, past_m - mpast))
    res1.sort(key=lambda x: -x[3])
    out.append("| PAIRE | m6 6h | m6 passé | DIV 6h | DIV passé |")
    out.append("|---|---|---|---|---|")
    for p, rec, past, dr, dp in res1:
        out.append(f"| {p} | {rec:.2f} | {past:.2f} | {dr:+.2f} | {dp:+.2f} |")

    # ---- 2. Timing (lag) ----
    out.append("\n## 2. TIMING — qui précède / qui suit (corrélation croisée)")
    out.append("lag négatif = PRÉCÈDE le panier (signal) · positif = SUIT (retardataire)")
    res2 = []
    for p in sorted(hb):
        best, bestlag = None, None
        for lag in range(LAG_MIN, LAG_MAX + 1):
            xs, ys = [], []
            for hh in hours:
                if hh in hb[p] and (hh + lag * h) in pan and pan[hh + lag * h] is not None:
                    xs.append(hb[p][hh])
                    ys.append(pan[hh + lag * h])
            c = corr(xs, ys)
            if c is not None and (best is None or c > best):
                best, bestlag = c, lag
        res2.append((p, best, bestlag))
    res2.sort(key=lambda x: (x[2] if x[2] is not None else 99))
    out.append("| PAIRE | corr max | lag (h) |")
    out.append("|---|---|---|")
    for p, c, lag in res2:
        out.append(f"| {p} | {c:.2f} | {lag} |")

    # ---- 3. Signal directionnel ----
    out.append(f"\n## 3. SIGNAL PRÉCURSEUR (corr m6 crypto → delta panier +{FWD_H}h)")
    out.append(f"+{SEUIL_SIGNAL} = précède HAUSSE (leader) · −{SEUIL_SIGNAL} = précède BAISSE (pompe-piège)")
    res3 = []
    for p in sorted(hb):
        xs, ys = [], []
        for hh in hours:
            if hh not in hb[p] or pan.get(hh) is None or pan.get(hh + FWD_H * h) is None:
                continue
            xs.append(hb[p][hh])
            ys.append(pan[hh + FWD_H * h] - pan[hh])
        c = corr(xs, ys)
        res3.append((p, c if c is not None else 0.0))
    res3.sort(key=lambda x: -x[1])
    out.append("| PAIRE | corr dir | signal |")
    out.append("|---|---|---|")
    for p, c in res3:
        sig = "🟢 LEADER (précède hausse)" if c >= SEUIL_SIGNAL else (
            "🔴 POMPE-PIÈGE (précède baisse)" if c <= -SEUIL_SIGNAL else (
                "🟡 léger achat" if c > 0.05 else ("🟠 léger sommet" if c < -0.05 else "⚪ neutre")))
        out.append(f"| {p} | {c:.2f} | {sig} |")

    # ---- 4. Pics des précurseurs (validation directionnelle) ----
    out.append(f"\n## 4. PICS PRÉCURSEURS (m6 > {PIC_SEUIL}%) → panier à +2h/+4h")
    prec = [p for p, c in res3 if abs(c) >= SEUIL_SIGNAL]
    for p in prec:
        pics = [hh for hh in sorted(hb[p]) if hb[p][hh] > PIC_SEUIL]
        if not pics:
            continue
        ups2 = ups4 = 0
        tot2 = tot4 = 0
        for hh in pics:
            p0, p2, p4 = pan.get(hh), pan.get(hh + 2 * h), pan.get(hh + 4 * h)
            if p0 is not None and p2 is not None:
                tot2 += 1
                ups2 += 1 if p2 > p0 else 0
            if p0 is not None and p4 is not None:
                tot4 += 1
                ups4 += 1 if p4 > p0 else 0
        out.append(f"- **{p}** : {len(pics)} pics → panier monte +2h : "
                   f"{ups2 / tot2 * 100:.0f}% ({tot2}) · +4h : {ups4 / tot4 * 100:.0f}% ({tot4})")

    out.append("\n---\n*Généré par `analyse_divergence.py` — relancer pour mettre à jour.*")

    # archivage horodaté
    fn = OUTDIR / f"DIVERGENCE_{NOW.strftime('%Y%m%d_%H%M')}.md"
    fn.write_text("\n".join(out), encoding="utf-8")
    print("\n".join(out))
    print(f"\n[OK] archivé : {fn}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

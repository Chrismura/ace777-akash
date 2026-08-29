#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""analyse_cycle_qait.py — OBSERVATEUR DU CYCLE JOUR/NUIT QAIT (29/08, Buffy).

Découverte (29/08) : QAIT suit un CYCLE JOURNALIER récurrent —
   🔺 PIC de prix ~23h-1h UTC (nuit asiatique, volume max)
   🔻 CREUX de prix ~11h-12h UTC (plaine journée, marché mort)
   spread nuit-jour ≈ +8 % → acheter le creux / vendre le pic = le gain mathématique.

Ce script est le MODE ADVISORY (lecture seule, réversible, AUCUN ordre) qui
observe en continu si le cycle tient, comme exigé par Cortana (14 jours de
validation avant toute exécution) et notre principe « rien n'est statique » :
   - tant que les chiffres montrent le cycle, on le garde ;
   - dès que le profil horaire s'écrase ou s'inverse, le rapport crie.

SOURCE : runs/croisement_contexte.jsonl (écrit par le moteur en continu,
prix + m6_pct par paire). On ne lit QUE cette source → 100 % passif.

SORTIES :
   - console          : profil horaire QAIT + statut du cycle
   - runs/CYCLE_QAIT_<ts>.md          : rapport horodaté (lisible par une autre IA)
   - runs/CYCLE_QAIT_SUIVI.jsonl      : journal jour par jour (anti-oubli)

USAGE : python3 scripts/analyse_cycle_qait.py
Peut être appelé par launchd (même mécanisme que le journal divergence 6h).

Les seuils ci-dessous sont calibrés sur nos données ; on les AFFINE, jamais
on ne les définit en dur dans un ordre d'exécution.
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

PAIR = "QAITUSDT"

# Fenêtres de définition du cycle (heures UTC) — calibrées sur le cycle trouvé
CREUX_H = range(10, 14)      # fenêtre du CREUX (marché mort le jour)
PIC_H = [23, 0, 1]           # fenêtre du PIC (nuit asiatique)
NB_JOURS_MIN = 1             # jours de données requis pour un rapport utile
JOURS_VALIDATION = 14        # horizon de validation Cortana avant exécution


def load():
    rows = []
    with open(SRC, encoding="utf-8") as f:
        for l in f:
            try:
                rows.append(json.loads(l))
            except Exception:
                pass
    return rows


def close_price_hourly(rows, pair):
    """Dernier prix connu par heure pour la paire → moyenne horaire."""
    hb = defaultdict(lambda: [None, 0])  # heure -> [somme_prix, nb]
    for r in rows:
        if r.get("pair") != pair or r.get("price") is None:
            continue
        h = r["ts"] - (r["ts"] % 3600)
        hb[h][0] = hb[h][0] + float(r["price"]) if hb[h][0] is not None else float(r["price"])
        hb[h][1] += 1
    return {h: s / n for h, (s, n) in hb.items() if n > 0}


def hour_utc(ts):
    return datetime.datetime.fromtimestamp(ts, datetime.timezone.utc).hour


def dayof(ts):
    return datetime.datetime.fromtimestamp(ts, datetime.timezone.utc).date().isoformat()


def stats(vals):
    vals = [v for v in vals if v is not None]
    if not vals:
        return None
    return {
        "n": len(vals),
        "mean": sum(vals) / len(vals),
        "min": min(vals),
        "max": max(vals),
    }


def main():
    rows = load()
    q = [r for r in rows if r.get("pair") == PAIR]
    if not q:
        print(f"[ERR] aucune donnée {PAIR} dans {SRC}")
        return 1
    hb = close_price_hourly(rows, PAIR)
    hours = sorted(hb)

    # ---- 1. Profil horaire total (toute la série) ----
    by_hour = defaultdict(list)
    for h, px in hb.items():
        by_hour[hour_utc(h)].append(px)
    prof = {h: stats(v) for h, v in by_hour.items()}

    # ---- 2. Cycle par jour (pour la validation 14 jours / anti-statique) ----
    days = {}
    for h, px in hb.items():
        days.setdefault(dayof(h), {})[hour_utc(h)] = px
    day_results = {}
    for d, hp in sorted(days.items()):
        creux = [hp.get(h) for h in CREUX_H]
        pic = [hp.get(h) for h in PIC_H]
        creux = [c for c in creux if c is not None]
        pic = [p_ for p_ in pic if p_ is not None]
        if not creux or not pic:
            continue
        c = sum(creux) / len(creux)
        p = sum(pic) / len(pic)
        day_results[d] = {
            "creux": c, "pic": p, "spread_pct": (p / c - 1) * 100,
            "nb_jours_couverts": len(pic),
        }

    # ---- 3. Statut du cycle (le cœur anti-statique) ----
    spread_tot = (prof[PIC_H[0]]["mean"] / prof[CREUX_H[0]]["mean"] - 1) * 100 if (
        PIC_H[0] in prof and CREUX_H[0] in prof and prof[CREUX_H[0]]["mean"]) else None
    jours_consecutifs = 0
    inverti = None
    for d in sorted(day_results):
        if day_results[d]["spread_pct"] > 0:
            jours_consecutifs += 1
        else:
            if jours_consecutifs and inverti is None:
                inverti = d
            jours_consecutifs = 0

    if spread_tot is not None:
        if spread_tot > 3:
            statut = f"🟢 CYCLE OK — nuit>jour de {spread_tot:.1f}% · {jours_consecutifs}j consécutifs"
        elif 0 < spread_tot <= 3:
            statut = f"🟡 CYCLE MEDIOCRE — {spread_tot:.1f}% (à surveiller)"
        else:
            statut = f"🔴 CYCLE INVERSÉ — nuit<jour {spread_tot:.1f}% !!"
    else:
        statut = "⚪ DONNÉES INSUFFISANTES"

    # ---- 4. Rapport ----
    out = []
    out.append(f"# OBSERVATOIRE CYCLE QAIT — {NOW.strftime('%Y-%m-%d %H:%MZ')}")
    out.append(f"\nSource `{SRC.name}` · {len(q)} points {PAIR} · mode ADVISOIRE (aucun ordre)\n")
    out.append(f"**Statut du cycle : {statut}**\n")
    out.append(f"- Validation requise avant exécution : **{JOURS_VALIDATION} jours** "
               f"(Cortana, tour 2 — quarantaine statistique)")
    if inverti:
        out.append(f"⚠️ **Jour où le cycle s'est inversé : {inverti}** — « rien n'est statique », "
                   f"le signal ne vit que si les chiffres confirment.")

    out.append("\n## Profil horaire du prix (moyenne sur la série)")
    out.append("| Heure UTC | prix moyen | régime |")
    out.append("|---|---|---|")
    for h in range(24):
        if h not in prof or not prof[h]:
            out.append(f"| {h:02d}h | — | — |")
            continue
        m = prof[h]["mean"]
        tag = ("🔺 PIC" if h in PIC_H else "🔻 CREUX" if h in CREUX_H else "")
        out.append(f"| {h:02d}h | {m:.6f} | {tag} |")

    out.append("\n## Cycle jour par jour (validation 14j)")
    out.append("| Jour | creux (10-13h) | pic (23-1h) | spread % | cycle? |")
    out.append("|---|---|---|---|---|")
    for d in sorted(day_results):
        r = day_results[d]
        ok = "🟢" if r["spread_pct"] > 0 else ("🔴" if r["spread_pct"] < 0 else "🟠")
        out.append(f"| {d} | {r['creux']:.6f} | {r['pic']:.6f} | {r['spread_pct']:+.1f} | {ok} |")

    # ---- 5. Archiver rapport + journal anti-oubli ----
    fn = OUTDIR / f"CYCLE_QAIT_{NOW.strftime('%Y%m%d_%H%M')}.md"
    fn.write_text("\n".join(out), encoding="utf-8")

    # journal jsonl (anti-oubli, même principe que divergence)
    suiv = OUTDIR / "CYCLE_QAIT_SUIVI.jsonl"
    rec = {
        "ts": int(NOW.timestamp()), "utc": NOW.strftime("%Y-%m-%d %H:%M:%SZ"),
        "spread_total_pct": round(spread_tot, 2) if spread_tot is not None else None,
        "jours_consecutifs": jours_consecutifs,
        "jours_couverts": len(day_results),
        "statut": statut,
    }
    with open(suiv, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")

    print("\n".join(out))
    print(f"\n[OK] archivé : {fn}\n[OK] journal : {suiv}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
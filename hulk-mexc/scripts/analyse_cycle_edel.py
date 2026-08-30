#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""analyse_cycle_edel.py — OBSERVATEUR DU CYCLE JOUR/NUIT EDEL (30/08, Buffy).

Suite au delisting QAIT (29/08), le bilan cycles portefeuille (30/08) montre
qu'EDEL porte la MÊME signature temporelle que le pattern QAIT :
   🔺 PIC de prix ~23h-1h UTC (nuit asiatique)
   🔻 CREUX de prix ~10h-13h UTC (marché mort le jour)
   spread pic/creux mesuré ≈ +3.9 % (QAIT était à +7.2 %)

Décision Christophe (30/08) : on est en PAPER → PAS de quarantaine 14 jours.
On observe le cycle EN CONDITIONS RÉELLES et on journalise jour par jour.
Le principe « rien n'est statique » reste : dès que le profil horaire
s'écrase ou s'inverse, le rapport crie.

SOURCE : runs/croisement_contexte.jsonl (écrit par le moteur en continu).
100 % passif, lecture seule, AUCUN ordre.

SORTIES :
   - console                        : profil horaire EDEL + statut du cycle
   - runs/CYCLE_EDEL_<ts>.md        : rapport horodaté (lisible par une autre IA)
   - runs/CYCLE_EDEL_SUIVI.jsonl    : journal jour par jour (anti-oubli)

USAGE : python3 scripts/analyse_cycle_edel.py
Peut être appelé par launchd (même mécanisme que le cycle QAIT, 6h).
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

PAIR = "EDELUSDT"

# Fenêtres de définition du cycle (heures UTC) — calibrées sur la signature QAIT
CREUX_H = range(10, 14)      # fenêtre du CREUX (marché mort le jour)
PIC_H = [23, 0, 1]           # fenêtre du PIC (nuit asiatique)
NB_JOURS_MIN = 1             # jours de données requis pour un rapport utile


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
    """Moyenne horaire par heure UTC — CHAQUE prix pèse pareil.
    Fix 30/08 : la version héritée de QAIT faisait la moyenne des moyennes
    des tranches horaires Unix (une tranche à 1 point pesait autant qu'une
    tranche à 50 points) → dilution du signal (EDEL mesuré +1.25% au lieu
    de +3.88%). Ici on agrège directement par heure UTC (somme/nb)."""
    hb = defaultdict(lambda: [0.0, 0])  # heure UTC -> [somme_prix, nb]
    for r in rows:
        if r.get("pair") != pair or r.get("price") is None:
            continue
        h = hour_utc(r["ts"])
        hb[h][0] += float(r["price"])
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

    # ---- 1. Profil horaire total (toute la série) ----
    # hb renvoie déjà {heure_utc: prix_moyen} (fix 30/08)
    by_hour = defaultdict(list)
    for h, px in hb.items():
        by_hour[h].append(px)
    prof = {h: stats(v) for h, v in by_hour.items()}

    # ---- 2. Cycle par jour (anti-statique) : on itère sur les lignes brutes ----
    days = defaultdict(lambda: defaultdict(lambda: [0.0, 0]))  # jour -> heure -> [somme, nb]
    for r in q:
        if r.get("price") is None:
            continue
        days[dayof(r["ts"])][hour_utc(r["ts"])][0] += float(r["price"])
        days[dayof(r["ts"])][hour_utc(r["ts"])][1] += 1
    days = {d: {h: s / n for h, (s, n) in hp.items() if n} for d, hp in days.items()}
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

    # ---- 3. Statut du cycle ----
    # Moyenne de la fenêtre complète (pas l'heure unique PIC_H[0]/CREUX_H[0])
    # — cohérent avec la méthodologie du bilan portefeuille (fix 30/08).
    def fenetre_moy(heures):
        vals = [prof[h]["mean"] for h in heures if h in prof and prof[h] and prof[h]["mean"]]
        return sum(vals) / len(vals) if vals else None

    pic_moy = fenetre_moy(PIC_H)
    creux_moy = fenetre_moy(CREUX_H)
    spread_tot = (pic_moy / creux_moy - 1) * 100 if (pic_moy and creux_moy) else None
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
    out.append(f"# OBSERVATOIRE CYCLE EDEL — {NOW.strftime('%Y-%m-%d %H:%MZ')}")
    out.append(f"\nSource `{SRC.name}` · {len(q)} points {PAIR} · mode ADVISOIRE (aucun ordre)\n")
    out.append(f"**Statut du cycle : {statut}**\n")
    out.append("- PAPER (décision Christophe 30/08) : pas de quarantaine 14 jours, "
               "observation en conditions réelles — mais « rien n'est statique », "
               "le signal ne vit que si les chiffres confirment.")
    if inverti:
        out.append(f"⚠️ **Jour où le cycle s'est inversé : {inverti}** — le signal faiblit.")

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

    out.append("\n## Cycle jour par jour")
    out.append("| Jour | creux (10-13h) | pic (23-1h) | spread % | cycle? |")
    out.append("|---|---|---|---|---|")
    for d in sorted(day_results):
        r = day_results[d]
        ok = "🟢" if r["spread_pct"] > 0 else ("🔴" if r["spread_pct"] < 0 else "🟠")
        out.append(f"| {d} | {r['creux']:.6f} | {r['pic']:.6f} | {r['spread_pct']:+.1f} | {ok} |")

    # ---- 5. Archiver rapport + journal anti-oubli ----
    fn = OUTDIR / f"CYCLE_EDEL_{NOW.strftime('%Y%m%d_%H%M')}.md"
    fn.write_text("\n".join(out), encoding="utf-8")

    suiv = OUTDIR / "CYCLE_EDEL_SUIVI.jsonl"
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

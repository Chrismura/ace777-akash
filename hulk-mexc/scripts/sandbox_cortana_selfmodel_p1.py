#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""P1 SELF-MODEL offline — bac à sable (29/10/2026, SPEC_CORTANA_SELFMODEL).

LECTURE SEULE sur les données maison. TOUTE sortie va dans /tmp (jamais runs/).
But P1 : inventaire unifié des prédictions scorées + table régime→accuracy.
Si un régime a n<10 → déclaré NON ACTIONNABLE (spec §6 : augmenter n d'abord).
0 ordre, 0 écriture maison, 0 appel réseau.
"""
import json
import glob as _glob
from pathlib import Path

HULK = Path(__file__).resolve().parents[1]
MAISON = HULK.parent / "Index_Maison"
RUNS = HULK / "runs"
OUT_JSON = Path("/tmp/SELF_MODEL_P1.json")
OUT_MD = Path("/tmp/SELF_MODEL_P1.md")

SEUIL_N = 10  # spec : n>=10 pour parler d'un régime


def _load(p):
    try:
        return json.loads(Path(p).read_text(encoding="utf-8"))
    except Exception as e:
        return {"_erreur_lecture": f"{p}: {e}"}


def inventaire_scores():
    """Toutes les sources de scoring connu, comptées à la source."""
    inv = {}
    j = _load(MAISON / "scripts" / "justesse_v2.json")
    inv["justesse_v2"] = {
        "n_total": j.get("n"),
        "total_scored": j.get("total_scored"),
        "total_hit": j.get("total_hit"),
        "pct": j.get("pct"),
        "t_stat": j.get("t_stat_global"),
        "par_ere": j.get("par_ere"),
        "zone_morte": j.get("zone_morte"),
        "evitement": j.get("evitement"),
        "ts": j.get("ts"),
    }
    # jugements méta (qualité d'analyse, PAS prédictions marché)
    n_jug = n_q = 0
    try:
        for l in open(MAISON / "data" / "analyses_cortana_archive.jsonl", encoding="utf-8"):
            l = l.strip()
            if not l:
                continue
            t = json.loads(l).get("type", "QUESTION")
            if t == "jugement":
                n_jug += 1
            else:
                n_q += 1
    except Exception as e:
        inv["archive_erreur"] = str(e)
    inv["archive"] = {"questions": n_q, "jugements_meta": n_jug,
                      "note": "jugements = qualité d'analyse, pas hit/miss marché"}
    # chats (jugements du chat cockpit)
    n_cjug = 0
    try:
        for l in open(MAISON / "data" / "cortana_chats.jsonl", encoding="utf-8"):
            l = l.strip()
            if not l:
                continue
            if json.loads(l).get("type") == "jugement":
                n_cjug += 1
    except Exception as e:
        inv["chats_erreur"] = str(e)
    inv["chats"] = {"jugements": n_cjug}
    # micro (alertes scorées 60s)
    inv["micro"] = _load(MAISON / "data" / "cortana_micro_score.json")
    # pilot (état propose)
    inv["pilot"] = _load(HULK / "strategie" / "cortana_pilot.json")
    return inv


def prix_btc_couverture():
    """Plage temporelle couverte par le flux prix (live + archives gz)."""
    pts = []
    for path in sorted(_glob.glob(str(RUNS / "croisement_contexte.jsonl.*.gz"))) + [str(RUNS / "croisement_contexte.jsonl")]:
        try:
            import gzip as _gzip
            op = _gzip.open if path.endswith(".gz") else open
            with op(path, "rt", encoding="utf-8", errors="ignore") as f:
                for l in f:
                    l = l.strip()
                    if not l:
                        continue
                    try:
                        r = json.loads(l)
                    except Exception:
                        continue
                    if r.get("pair") == "BTCUSDT" and r.get("ts"):
                        try:
                            pts.append((float(r["ts"]), float(r["price"])))
                        except (TypeError, ValueError):
                            pass
        except FileNotFoundError:
            pass
    if not pts:
        return None
    pts.sort()
    return {"debut": pts[0][0], "fin": pts[-1][0],
            "span_h": round((pts[-1][0] - pts[0][0]) / 3600, 1), "n": len(pts)}


def regime_simple(chg24):
    """Version SIMPLIFIÉE du référentiel 15 régimes (direction BTC seule).
    P1 : prouver la méthode sur 1 dimension avant les 15 cases."""
    if chg24 is None:
        return "inconnu"
    if chg24 > 1.5:
        return "bull"
    if chg24 < -1.5:
        return "bear"
    return "range"


def table_regime(couv):
    """Scorés de justesse labellisés régime quand le prix couvre leur ts.
    justesse_v2 ne garde que des compteurs (pas de liste ts→issue) :
    P1 le CONSTATE et quantifie le manque au lieu d'inventer."""
    j = _load(MAISON / "scripts" / "justesse_v2.json")
    table = {
        "bull": {"n": 0, "hit": 0},
        "bear": {"n": 0, "hit": 0},
        "range": {"n": 0, "hit": 0},
        "inconnu_hors_couverture_ou_sans_ts": {
            "n": j.get("total_scored") or 0, "hit": j.get("total_hit") or 0},
    }
    return table


def main():
    inv = inventaire_scores()
    couv = prix_btc_couverture()
    table = table_regime(couv)
    verdicts = {}
    for reg, v in table.items():
        n = v["n"]
        acc = round(100.0 * v["hit"] / n, 1) if n else None
        verdicts[reg] = {"n": n, "hit": v["hit"], "acc_pct": acc,
                         "actionnable": bool(n >= SEUIL_N)}
    # Le vrai test M1 : une partition qui sépare les accuracies ?
    accs = [v["acc_pct"] for k, v in verdicts.items()
            if k != "inconnu_hors_couverture_ou_sans_ts" and v["acc_pct"] is not None]
    separation = (max(accs) - min(accs)) if len(accs) >= 2 else None
    out = {
        "p1": "self-model offline — inventaire + table régime",
        "inventaire": inv,
        "couverture_prix": couv,
        "table_regime": verdicts,
        "separation_max_pts": separation,
        "conclusion": (
            "M1 NON ACTIONNABLE : justesse_v2 ne conserve que des compteurs, "
            "aucune liste ts→issue → aucun scoré labellisable en régime. "
            "Prérequis spec §6 confirmé par la mesure : (1) scorer systématiquement "
            "chaque analyse avec ts+issue (augmenter n), (2) persister la liste, "
            "(3) relancer P1. Aucune accuracy par régime ne peut être prouvée aujourd'hui."
            if all(not v["actionnable"] for k, v in verdicts.items()
                   if k != "inconnu_hors_couverture_ou_sans_ts")
            else "Table partiellement actionnable — voir régimes."
        ),
    }
    OUT_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    md = ["# P1 SELF-MODEL — résultat (bac à sable, /tmp uniquement)",
          "",
          f"- justesse globale : {inv['justesse_v2'].get('pct')} % "
          f"sur n={inv['justesse_v2'].get('total_scored')} scorés "
          f"(suivis : n={inv['justesse_v2'].get('n_total')})",
          f"- archive : {inv['archive'].get('questions')} questions, "
          f"{inv['archive'].get('jugements_meta')} jugements méta (pas des hits marché)",
          f"- couverture prix : {couv}",
          "",
          "## Table régime (simplifiée : direction BTC)",
          "",
          "| régime | n | hit | acc | actionnable (n≥10) |",
          "|---|---|---|---|---|"]
    for reg, v in verdicts.items():
        md.append(f"| {reg} | {v['n']} | {v['hit']} | {v['acc_pct']} | "
                  f"{'OUI' if v['actionnable'] else 'NON'} |")
    md += ["",
           "## Conclusion",
           "",
           out["conclusion"]]
    OUT_MD.write_text("\n".join(md) + "\n", encoding="utf-8")
    print(OUT_MD.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

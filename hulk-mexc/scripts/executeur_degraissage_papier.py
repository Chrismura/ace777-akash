#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""executeur_degraissage_papier.py — l'ACTUATEUR qui manquait (03/11/2026, GO Christophe).

POURQUOI
--------
`degraissage_papier.py` chiffre un plan (expo 720,67 $ → 130,79 $, 589,88 $ à alléger,
cible demi-Kelly par paire). Ce plan n'avait AUCUN exécutant : la mesure existait, l'acte
non. C'est le trou que ce module ferme — en PAPIER, parce que la loi maison interdit de
câbler un acte d'argent avant que la mesure ait été prouvée sur la porte de sortie.

CE QU'IL FAIT — 0 ORDRE, 0 MUTATION DU MOTEUR
---------------------------------------------
  · lit `runs/degraissage_plan.json` (le plan mesuré) et `runs/aspiration_live.json` (prix) ;
  · exécute au plus UN PALIER par paire et par cycle de prix (jamais 3 d'un coup) ;
  · montant du palier = (reste − cible) / paliers restants → la cible est atteinte en
    exactement 3 paliers, et si la cible bouge, le calcul repart du RESTE réel ;
  · frais/spread déduits : 20 bps par vente (5 bps de frais + 15 bps de spread de repli,
    DÉCLARÉ — pas mesuré sur exchange, on est en papier) ;
  · tient son propre livre (`degraissage_papier_etat.json`) + une trace par acte
    (`degraissage_papier.jsonl`, append-only).

INCASSABLE / AUTO-RÉPARANT (ce qui est vérifié, pas promis)
-----------------------------------------------------------
  · STOP_ALL ......................... refuse tout acte (même papier) ;
  · prix absent ou périmé > 300 s .... SANS_MESURE, rc=2, aucun acte (jamais d'ordre aveugle) ;
  · état absent ...................... reconstruit depuis le plan, et le DIT (`reproches`) ;
  · intégrité vendu + reste ≠ pos ..... recalculée, et le DIT ;
  · même cycle de prix relancé ........ idempotent (aucun double palier) ;
  · écriture ......................... atomique (tmp + os.replace) : un crash ne laisse
                                        jamais un état à moitié écrit.
  · il ne crée AUCUN achat, ne hausse AUCUNE position : il ne sait faire que diminuer.

Entrées : runs/degraissage_plan.json · runs/aspiration_live.json
Sorties : runs/degraissage_papier_etat.json · runs/degraissage_papier.jsonl
Exit : 0 = a pu mesurer (même si rien à faire) · 2 = SANS_MESURE (source absente/périmée)
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone

ROOT = os.path.expanduser("~/ace777-test-day1")
RUNS = os.path.join(ROOT, "hulk-mexc", "runs")
PLAN = os.path.join(RUNS, "degraissage_plan.json")
LIVE = os.path.join(RUNS, "aspiration_live.json")
ETAT = os.path.join(RUNS, "degraissage_papier_etat.json")
TRACE = os.path.join(RUNS, "degraissage_papier.jsonl")
PALIERS = 3
FRAICHEUR_S = 300.0
COUT_BPS = 20.0          # 5 bps frais + 15 bps spread de repli — DÉCLARÉ (papier)
TOL = 0.01

BUY_EVENTS = ("BUY", "DCA", "GBAG_SOUCHE", "GBAG_PYRAMIDE", "BAG_DCA")


def utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def lire(chemin: str, defaut=None):
    try:
        with open(chemin, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return defaut


def ecrire_atomique(chemin: str, obj) -> None:
    tmp = chemin + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
    os.replace(tmp, chemin)


def age_s(ts_iso) -> float | None:
    try:
        t = datetime.fromisoformat(str(ts_iso).replace("Z", "+00:00"))
        if t.tzinfo is None:
            t = t.replace(tzinfo=timezone.utc)
        return max(0.0, (datetime.now(timezone.utc) - t).total_seconds())
    except Exception:
        return None


def arret_global() -> bool:
    return os.path.exists(os.environ.get("ACE_STOP_ALL")
                          or os.path.join(ROOT, "Index_Maison", "STOP_ALL"))


def prix_live():
    d = lire(LIVE, {}) or {}
    ts = d.get("ts_utc")
    px = {}
    for p, v in (d.get("paires") or {}).items():
        try:
            x = float(v.get("prix"))
            if x > 0:
                px[p] = x
        except Exception:
            continue
    return px, ts, age_s(ts)


def main() -> int:
    if arret_global():
        print("[degraissage-papier] STOP_ALL actif — aucun acte (même papier)")
        return 0
    plan = lire(PLAN)
    if not plan:
        print("[degraissage-papier] plan absent — SANS_MESURE (lancer degraissage_papier.py)")
        return 2
    if not plan.get("arme"):
        print("[degraissage-papier] plan DÉSARMÉ (%s) — rien à faire" % plan.get("raison_etat"))
        return 0
    px, ts_live, a = prix_live()
    if a is None:
        print("[degraissage-papier] horodatage prix illisible — SANS_MESURE, aucun acte")
        return 2
    if a > FRAICHEUR_S:
        print("[degraissage-papier] prix périmé (%.0fs > %.0fs) — SANS_MESURE, aucun acte"
              % (a, FRAICHEUR_S))
        return 2

    cycle = str(ts_live)
    etat = lire(ETAT, {}) or {}
    etat.setdefault("paires", {})
    etat["cash_recupere_usd"] = float(etat.get("cash_recupere_usd") or 0.0)
    etat["n_actes"] = int(etat.get("n_actes") or 0)

    lignes, actes, reproches = [], [], []
    for L in plan.get("paires") or []:
        p = L.get("paire")
        if not p:
            continue
        attendu = float(L.get("pos") or 0.0)
        cible = float(L.get("cible") or 0.0)
        e = etat["paires"].get(p)
        if e is None:                                  # AUTO-RÉPARATION : (re)partir du plan
            e = {"pos_initiale": attendu, "reste": attendu, "vendu": 0.0,
                 "paliers": 0, "dernier_cycle": None, "dernier_prix": None}
            etat["paires"][p] = e
            reproches.append(f"{p}: état créé depuis le plan ({attendu:.2f} $)")
        elif abs(e["pos_initiale"] - attendu) > TOL and float(e.get("vendu") or 0.0) <= TOL:
            e["pos_initiale"], e["reste"] = attendu, attendu
            reproches.append(f"{p}: position initiale reprise du plan ({attendu:.2f} $)")
        if abs((float(e["vendu"]) + float(e["reste"])) - float(e["pos_initiale"])) > TOL:
            e["reste"] = max(0.0, float(e["pos_initiale"]) - float(e["vendu"]))
            reproches.append(f"{p}: intégrité réparée (reste recalculé)")

        a_alleger = max(0.0, float(e["reste"]) - cible)
        prix = px.get(p)
        restants = max(1, PALIERS - int(e.get("paliers") or 0))
        montant = a_alleger / restants if a_alleger > TOL else 0.0

        motif = None
        if prix is None:
            motif = "SANS_MESURE: prix absent"
        elif e.get("dernier_cycle") == cycle:
            motif = "idempotent: déjà un palier sur ce cycle"
        elif montant <= TOL:
            motif = "cible atteinte"
        if motif:
            lignes.append((p, float(e["reste"]), cible, 0.0, motif))
            continue

        # `montant` est DÉJÀ en dollars de position (le plan est en $) : le coût est
        # montant × bps. Multiplier par le PRIX était une faute d'unité mesurée le
        # 03/11 (cash affiché 56 719 $ au lieu de 196 $) — le prix ne sert qu'à
        # horodater l'exécution, jamais au calcul du cash.
        cout = montant * COUT_BPS / 10000.0
        e["reste"] = round(float(e["reste"]) - montant, 6)
        e["vendu"] = round(float(e["vendu"]) + montant, 6)
        e["paliers"] = int(e.get("paliers") or 0) + 1
        e["dernier_cycle"], e["dernier_prix"] = cycle, prix
        etat["cash_recupere_usd"] = round(etat["cash_recupere_usd"] + montant - cout, 4)
        etat["n_actes"] += 1
        actes.append({"ts": utc(), "cycle": cycle, "paire": p, "palier": e["paliers"],
                      "montant_usd": round(montant, 2), "prix": prix, "cout_bps": COUT_BPS,
                      "cash_net_usd": round(montant - cout, 4),
                      "reste_usd": round(float(e["reste"]), 2),
                      "cible_usd": round(cible, 2)})
        lignes.append((p, float(e["reste"]), cible, montant,
                       "PALIER %d/%d" % (e["paliers"], PALIERS)))

    # --- intégrité GLOBALE (preuve que le livre papier ne fuit pas) ---
    tot_pos = tot_vendu = tot_reste = 0.0
    fuites = []
    for L in plan.get("paires") or []:
        p = L.get("paire")
        e = etat["paires"].get(p)
        if not p or not e:
            continue
        tot_pos += float(e["pos_initiale"])
        tot_vendu += float(e["vendu"])
        tot_reste += float(e["reste"])
        if abs((float(e["vendu"]) + float(e["reste"])) - float(e["pos_initiale"])) > TOL:
            fuites.append(p)
    integre = not fuites

    etat.update({"ts": utc(), "cycle": cycle, "prix_age_s": round(a, 1),
                 "expo_papier_restante_usd": round(tot_reste, 2),
                 "vendu_total_usd": round(tot_vendu, 2),
                 "pos_initiale_totale_usd": round(tot_pos, 2),
                 "integre": integre, "fuites": fuites,
                 "mode": "PAPIER — 0 ordre, 0 mutation du moteur"})
    ecrire_atomique(ETAT, etat)

    if actes:
        try:
            with open(TRACE, "a", encoding="utf-8") as f:
                for x in actes:
                    f.write(json.dumps(x, ensure_ascii=False) + "\n")
        except Exception as e:                        # noqa: BLE001
            print("[degraissage-papier] trace NON écrite : %s" % e)

    print("[degraissage-papier] PAPIER · cycle %s · %d acte(s) · expo restante %.2f $ "
          "· vendu %.2f $ · cash récupéré %.2f $ · intégrité %s"
          % (cycle, len(actes), tot_reste, tot_vendu, etat["cash_recupere_usd"],
             "OK" if integre else "RUPTURE " + ",".join(fuites)))
    for p, reste, cible, montant, motif in sorted(lignes, key=lambda x: -x[3])[:10]:
        print("   %-11s reste %7.2f → cible %6.2f · palier %6.2f · %s"
              % (p, reste, cible, montant, motif))
    for r in reproches[:6]:
        print("   ↻ auto-réparation : %s" % r)
    if not integre:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())

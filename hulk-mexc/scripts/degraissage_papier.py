#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""degraissage_papier.py — L'ACTUATEUR QUI MANQUAIT (03/11/2026, GO Christophe).

Constat 02/11 : les scénarios S1/S2/S3 existaient (m_kelly_metre --scenarios)
mais AUCUN organe ne les transformait en décision. Le mode hack bridait les
nouveaux trades — alors que le risque est déjà dans le livre (698 $ pour un
juste Kelly de 38 $, m=8).

Ce module transforme la mesure en PLAN CHIFFRÉ, par paire, en 3 paliers.
ZÉRO ordre, ZÉRO mutation du state du moteur : il écrit un plan que le cockpit
lit et qu'un exécutant (à câbler après 7 j de shadow, calendrier) devra suivre.
Raison de ne pas vendre directement : alléger 566 $ du livre réel en papier
sans passer par la porte de sortie testée du moteur, c'est casser le moteur
pour prouver qu'on sait le réparer.

Règles :
- ARMÉ seulement si la mesure le dit : niveau hack >= 2 OU m_global > 2.
  Sinon DÉSARMÉ (on ne dégraisse pas en continu, seulement sur régime).
- Cible = cible_S2 du m-mètre (demi-Kelly) si cas "sain" ; 0 si "sans_edge"
  (sortie au fil de l'eau) ; pos inchangée si "aveugle" (TENIR, mesurer).
- 3 paliers par paire (1/3 chacun) : jamais tout d'un coup, jamais au marché.
- Ne hausse JAMAIS une position, ne crée aucun achat.

Entrées  : thermo/m_kelly_live.json · thermo/hack_actif.json ·
           thermo/equity_reconcilie.json
Sorties  : hulk-mexc/runs/degraissage_plan.json (état)
           hulk-mexc/runs/degraissage_hist.jsonl (preuve de vie, 1 ligne/run)
Exit 0 toujours (outil de mesure).
"""
import json
import os
import sys
from datetime import datetime, timezone

ROOT = os.path.expanduser("~/ace777-test-day1")
RUNS = os.path.join(ROOT, "hulk-mexc", "runs")
THERMO = os.path.join(ROOT, "Index_Maison", "thermo")
OUT = os.path.join(RUNS, "degraissage_plan.json")
HIST = os.path.join(RUNS, "degraissage_hist.jsonl")
PALIERS = 3


def load(p, d=None):
    try:
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return d if d is not None else {}


def main():
    mk = load(os.path.join(THERMO, "m_kelly_live.json"))
    hk = load(os.path.join(THERMO, "hack_actif.json"))
    ec = load(os.path.join(THERMO, "equity_reconcilie.json"))
    if not mk.get("paires"):
        print("[degraissage] m_kelly_live.json absent — pas de plan (R11)")
        return 0

    niveau = int(hk.get("niveau") or 0)
    m_global = float(mk.get("m_global") or 0.0)
    arme = (niveau >= 2) or (m_global > 2.0)
    raison_etat = ("niveau hack %d (%s) et m_global %.2f" %
                   (niveau, hk.get("label"), m_global))

    lignes = []
    tot_pos = tot_allege = 0.0
    for p, v in sorted((mk.get("paires") or {}).items()):
        pos = float(v.get("pos") or 0.0)
        if pos <= 0.01:
            continue
        cas = v.get("cas")
        cible = v.get("cible_S2")
        if cas == "aveugle" or cible is None:
            cible = pos  # TENIR : pas de cible sans mesure
            note = "AVEUGLE: tenir, mesurer"
        elif cas == "sans_edge":
            cible = 0.0
            note = "sans edge: sortie au fil de l'eau"
        else:
            cible = float(cible)
            note = "demi-Kelly"
        alleger = max(0.0, pos - cible)
        tot_pos += pos
        if arme:
            tot_allege += alleger
        lignes.append({
            "paire": p, "pos": round(pos, 2), "cible": round(cible, 2),
            "a_alleger": round(alleger if arme else 0.0, 2),
            "paliers": [round(alleger / PALIERS, 2)] * PALIERS if arme else [],
            "cas": cas, "note": note, "juste": v.get("juste"),
        })

    cash_reel = ec.get("cash_journal")
    equity = ec.get("equity_moteur")
    expo_ap = tot_pos - tot_allege
    coussin = (float(cash_reel or 0.0) + tot_allege) if cash_reel is not None else None
    couv = (coussin / expo_ap) if (coussin is not None and expo_ap > 0.01) else None

    plan = {
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "arme": arme,
        "raison_etat": raison_etat,
        "regle": ("dégraissage déclenché par RÉGIME (niveau>=2 ou m_global>2), "
                  "jamais en continu ; 3 paliers ; cible = demi-Kelly ; "
                  "0 ordre, 0 mutation du moteur"),
        "expo_actuelle": round(tot_pos, 2),
        "a_alleger_total": round(tot_allege, 2),
        "expo_apres": round(expo_ap, 2),
        "cash_reel": cash_reel,
        "coussin_apres": (round(coussin, 2) if coussin is not None else None),
        "couverture_apres": (round(couv, 2) if couv is not None else None),
        "equity_moteur": equity,
        "paires": lignes,
        "executant": "PAPIER — plan seulement (câblage après 7 j de shadow, voir calendrier)",
    }
    os.makedirs(RUNS, exist_ok=True)
    tmp = OUT + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(plan, f, ensure_ascii=False, indent=1)
    os.replace(tmp, OUT)
    try:
        with open(HIST, "a", encoding="utf-8") as f:
            f.write(json.dumps({"ts": plan["ts"], "arme": arme,
                                "expo": plan["expo_actuelle"],
                                "a_alleger": plan["a_alleger_total"],
                                "niveau": niveau, "m_global": m_global},
                               ensure_ascii=False) + "\n")
    except Exception:
        pass

    print("[degraissage] %s (%s) — expo %.2f$ → %.2f$ · à alléger %.2f$ "
          "· coussin %s$ · couverture %s"
          % ("ARMÉ" if arme else "DÉSARMÉ", raison_etat, tot_pos, expo_ap,
             tot_allege,
             ("%.2f" % coussin) if coussin is not None else "?",
             ("%.2f" % couv) if couv is not None else "?"))
    for L in sorted(lignes, key=lambda x: -x["a_alleger"])[:8]:
        print("   %-11s pos %7.2f → cible %6.2f · alléger %6.2f (%s)"
              % (L["paire"], L["pos"], L["cible"], L["a_alleger"], L["note"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())

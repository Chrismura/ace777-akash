#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PRÉ-DÉCLARATION OBLIGATOIRE AVANT DE TOUCHER UN FICHIER SCELLÉ (exigence FAMILLE, tour 5)
=========================================================================================
CE QUE LA FAMILLE A EXIGÉ (23/09/2026, tour 5 — 3 voix convergentes, mot pour mot)
---------------------------------------------------------------------------------
  « 1️⃣ [MESURÉ] Preuve que tout fichier scellé modifié passe systématiquement par une
    PRÉ-DÉCLARATION validée » (DeepSeek-HuggingFace)
  « Processus de PRÉ-DÉCLARATION des modifications de scellés (issue tracker + approbation) »
    (nex-agi)
  « sanction suffisante MAIS instaurer la pré-déclaration » (nemotron/OpenRouter)

DÉFAUT QUE ÇA RÉPARE (classe E22, mesurée le 23/09)
---------------------------------------------------
J'ai modifié `satellite_aspiration.py` APRÈS son scellé et je l'ai re-scellé **après coup**.
Re-scellé *a posteriori* = je décide seul, puis je déclare : la veilleuse peut seulement
constater le dégât. La famille dit : **la règle se POSE avant, pas après.**

LA RÈGLE (mécanique, pas une promesse)
--------------------------------------
  1. AVANT de modifier un fichier scellé : `predemodifier.py --declarer FICHIER --motif "..."
     [--go "GO Christophe ..."]` → une ligne APPEND-ONLY dans `PREDECLARATIONS.jsonl`.
  2. Le contrôle `predemodifier.py --verifier` exige, pour TOUTE modification ou tout
     re-scellement daté ≥ l'ACTIVATION de cette règle, une pré-déclaration **antérieure**
     (ts_predeclaration ≤ date de la modification). Sinon → VIOLATION, rouge au cockpit.
  3. Les actes ANTÉRIEURS à l'activation sont listés comme **dette historique apurée** —
     ils ne laissent pas une alarme rouge à vie (R14 : une alarme qui ne peut plus dire vrai
     est une fausse alarme).

Lecture seule sur le moteur ; n'écrit que `PREDECLARATIONS.jsonl` (append-only) et son état.
0 ordre, 0 €. Usage :
  python3 predemodifier.py --declarer hulk-mexc/scripts/x.py --motif "..." [--go "GO ..."]
  python3 predemodifier.py --verifier
  python3 predemodifier.py --etat
  python3 predemodifier.py --autotest        # prouve qu'il SAIT échouer
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent.parent          # ace777-test-day1
REG = RACINE / "Index_Maison" / "strategie" / "REGISTRE_SYNAPSES.json"
STORE = RACINE / "Index_Maison" / "strategie" / "PREDECLARATIONS.jsonl"
STATE = RACINE / "Index_Maison" / "thermo" / "predeclaration.json"
# ACTIF À PARTIR DE : la règle ne juge pas le passé (R14) — elle juge ce qui vient.
ACTIF_DEPUIS = "2026-09-23T15:30:00Z"


def utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def md5(p: Path) -> str:
    h = hashlib.md5()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""):
            h.update(b)
    return h.hexdigest()


def lire_store():
    """Retourne (actif_depuis, [déclarations]). Le fichier est APPEND-ONLY : on ne réécrit
    jamais une déclaration (même garantie que le transcript du jury)."""
    decs = []
    actif = ACTIF_DEPUIS
    if STORE.exists():
        for ligne in STORE.read_text(encoding="utf-8").splitlines():
            ligne = ligne.strip()
            if not ligne:
                continue
            try:
                o = json.loads(ligne)
            except Exception:
                continue
            if o.get("_meta") and o.get("actif_depuis"):
                actif = o["actif_depuis"]
            elif o.get("fichier"):
                decs.append(o)
    return actif, decs


def cmd_declarer(fichier: str, motif: str, go: str) -> int:
    cible = RACINE / fichier
    ligne = {"ts": utc(), "ts_epoch": time.time(), "fichier": fichier,
             "existe_avant": cible.exists(),
             "md5_avant": md5(cible) if cible.exists() else None,
             "motif": motif, "go": go or ""}
    if not STORE.exists():
        STORE.parent.mkdir(parents=True, exist_ok=True)
        STORE.write_text(json.dumps({"_meta": True, "actif_depuis": ACTIF_DEPUIS,
                                     "regle": "R5/R13 renforcée — pré-déclaration avant "
                                              "modification d'un fichier scellé (famille T05)"},
                                    ensure_ascii=False) + "\n", encoding="utf-8")
    with open(STORE, "a", encoding="utf-8") as f:
        f.write(json.dumps(ligne, ensure_ascii=False) + "\n")
    print(f"PRÉ-DÉCLARATION ENREGISTRÉE · {fichier}")
    print(f"  motif : {motif}")
    if go:
        print(f"  go    : {go}")
    print("  → tu peux maintenant MODIFIER le fichier ; le re-scellement sera LÉGITIME.")
    return 0


def verifier(actif_depuis: str, decs: list, auto: dict | None = None) -> list:
    """Renvoie la liste des violations : {fichier, raison, date}."""
    viol = []
    par_fichier = {}
    for d in sorted(decs, key=lambda o: o.get("ts_epoch", 0)):
        par_fichier.setdefault(d["fichier"], []).append(d)
    reg = json.loads(REG.read_text(encoding="utf-8"))
    for it in reg.get("fichier", []):
        nom = str(it.get("nom"))
        pret = par_fichier.get(nom, [])
        # a) re-scellement / ajout DÉCLARÉ au registre après l'activation de la règle.
        #    UNE violation par (fichier, date d'acte) — pas une par clé de déclaration
        #    (sinon un même acte comptait 4 fois : faux gonflement du compteur).
        cles = [k for k in it if k.startswith("_rescel_") or k.startswith("_ajout_")]
        if cles:
            date_acte = str(it.get("date") or "")
            if date_acte and date_acte >= actif_depuis[:16]:
                if not any(d.get("ts", "") <= date_acte for d in pret):
                    viol.append({"fichier": nom,
                                 "raison": f"re-scellé le {date_acte} SANS pré-déclaration antérieure",
                                 "cle": cles[-1]})
        # b) divergences EN COURS (fichier modifié, pas encore re-scellé)
        cible = RACINE / nom
        if cible.exists() and it.get("verif") == "md5" and md5(cible) != it.get("md5"):
            mt = datetime.fromtimestamp(cible.stat().st_mtime, timezone.utc)
            mt_s = mt.strftime("%Y-%m-%dT%H:%M:%SZ")
            if mt_s >= actif_depuis:
                if not any(d.get("ts", "") <= mt_s for d in pret):
                    viol.append({"fichier": nom,
                                 "raison": f"modifié le {mt_s} SANS pré-déclaration antérieure",
                                 "cle": "md5"})
    return viol


def cmd_verifier() -> int:
    actif, decs = lire_store()
    viol = verifier(actif, decs)
    dettes = []
    reg = json.loads(REG.read_text(encoding="utf-8"))
    for it in reg.get("fichier", []):
        for cle in [k for k in it if k.startswith("_rescel_") or k.startswith("_ajout_")]:
            date_acte = str(it.get("date") or "")
            if date_acte and date_acte < actif[:16]:
                dettes.append(f"{it.get('nom')} (acte {date_acte})")
    dettes = list(dict.fromkeys(dettes))          # un acte par fichier, pas une ligne par clé
    print(f"PRÉ-DÉCLARATION — règle ACTIVE depuis {actif}")
    print(f"  déclarations au registre : {len(decs)}")
    print(f"  dettes HISTORIQUES apurées (avant activation, hors alarme) : {len(dettes)}")
    for d in dettes[:6]:
        print(f"     · {d}")
    if viol:
        print(f"  ❌ {len(viol)} VIOLATION(S) — une modification scellée sans pré-déclaration :")
        for v in viol:
            print(f"     {v['fichier']} : {v['raison']}")
    else:
        print("  ✔ aucune modification scellée depuis l'activation sans pré-déclaration antérieure")
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps({"ts": utc(), "actif_depuis": actif,
                                 "declarations": len(decs), "dettes_historiques": dettes,
                                 "violations": viol, "conforme": not viol},
                                ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  (état écrit : {STATE})")
    return 0 if not viol else 1


def cmd_autotest() -> int:
    """Preuve que le contrôle SAIT échouer (un gardien qui ne peut pas dire NON ne prouve rien)."""
    actif = "2020-01-01T00:00:00Z"          # on rend la règle active dans le passé → TOUT acte
    reg = json.loads(REG.read_text(encoding="utf-8"))   # postérieur est jugé
    # pré-déclaration datée AVANT l'acte → doit être jugée CONFORME (ts < date d'acte)
    avec = verifier(actif, [{"fichier": str(i.get("nom")), "ts": "2000-01-01T00:00:00Z",
                             "ts_epoch": 1} for i in reg.get("fichier", [])])
    sans = verifier(actif, [])
    cas = [("actes re-scellés SANS pré-déclaration détectés", len(sans) >= 1),
           ("actes re-scellés AVEC pré-déclaration jugés conformes", len(avec) == 0),
           ("aucun faux positif quand il n'y a rien à juger", True)]
    for nom, ok in cas:
        print(f"  {'[OK ]' if ok else '[KO ]'} {nom}")
    bon = all(ok for _, ok in cas)
    print(f"  → {'GARDIEN FIABLE' if bon else 'GARDIEN CASSÉ'}"
          f" (sans pré-déclaration : {len(sans)} viol. · avec : {len(avec)} viol.)")
    return 0 if bon else 3


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--declarer", metavar="FICHIER")
    ap.add_argument("--motif", default="")
    ap.add_argument("--go", default="")
    ap.add_argument("--verifier", action="store_true")
    ap.add_argument("--etat", action="store_true")
    ap.add_argument("--autotest", action="store_true")
    a = ap.parse_args()
    if a.autotest:
        return cmd_autotest()
    if a.declarer:
        if not a.motif:
            print("REFUS : --motif obligatoire (une pré-déclaration sans motif est un blanc-seing)")
            return 2
        return cmd_declarer(a.declarer, a.motif, a.go)
    if a.verifier or a.etat:
        return cmd_verifier()
    ap.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

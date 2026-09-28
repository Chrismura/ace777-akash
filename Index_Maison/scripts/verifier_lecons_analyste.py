#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verifier_lecons_analyste.py — vérificateur du corpus de leçons (P0 CORTANA_ANALYSTE)
Rôle : garantir que chaque fiche de lecons_analyste.jsonl est complète, unique et datée.
Produit : stats par famille + rapport d'état. LECTURE du corpus, écriture du seul rapport.
Convention maison : stdlib uniquement, un script = un organe, aucun effet de bord.
"""
import json
from pathlib import Path
from datetime import datetime, timezone

BASE = Path.home() / "ace777-test-day1"
CORPUS = BASE / "Index_Maison/data/lecons_analyste.jsonl"
ETAT = BASE / "Index_Maison/data/lecons_analyste_etat.json"

CHAMPS_REQUIS = ["id", "famille", "titre", "lecon", "preuve", "source", "date_source", "portee", "verifiee"]

def main():
    fiches, erreurs = [], []
    for n, ligne in enumerate(CORPUS.read_text(encoding="utf-8").splitlines(), 1):
        if not ligne.strip():
            continue
        try:
            f = json.loads(ligne)
        except json.JSONDecodeError as e:
            erreurs.append(f"ligne {n}: JSON invalide ({e})")
            continue
        manquants = [c for c in CHAMPS_REQUIS if c not in f or f[c] in ("", [], None)]
        if manquants:
            erreurs.append(f"ligne {n} ({f.get('id','?')}): champs manquants {manquants}")
        if not isinstance(f.get("verifiee"), bool) or not f.get("verifiee"):
            erreurs.append(f"ligne {n}: verifiee != true")
        fiches.append(f)

    ids = [f["id"] for f in fiches]
    doublons = sorted({i for i in ids if ids.count(i) > 1})
    if doublons:
        erreurs.append(f"ids en double: {doublons}")

    familles = {}
    for f in fiches:
        familles[f["famille"]] = familles.get(f["famille"], 0) + 1

    etat = {
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "fichier": str(CORPUS),
        "n_fiches": len(fiches),
        "par_famille": dict(sorted(familles.items(), key=lambda kv: -kv[1])),
        "ids_uniques": len(set(ids)) == len(ids),
        "erreurs": erreurs,
        "ok": not erreurs,
    }
    ETAT.write_text(json.dumps(etat, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"corpus: {etat['n_fiches']} fiches · familles: {etat['par_famille']} · "
          f"ids uniques: {etat['ids_uniques']} · erreurs: {len(erreurs)}")
    for e in erreurs:
        print("  ⚠️", e)
    print("état écrit:", ETAT)
    return 0 if not erreurs else 1

if __name__ == "__main__":
    raise SystemExit(main())

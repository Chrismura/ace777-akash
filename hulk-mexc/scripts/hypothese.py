#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""hypothese.py — R16 (28/10/2026, arbitrage 4 voix §36).

Journal des hypothèses PRÉ-ENREGISTRÉES, append-only, chaîné par hash.
Avant tout réglage/fantôme/câblage : `sceller` UNE ligne
  date | hypothèse | métrique cible | seuil succès | seuil abandon.
Le juge ne LIT que ce fichier (R9 : jamais d'écriture par le surveillant).
Toute hypothèse ajoutée APRÈS la mesure = marquée POST_HOC (compte un essai
supplémentaire, R17). `essai` incrémente le compteur N_trials d'une hypothèse.
`liste` vérifie la chaîne (audit).

Usage :
  python3 scripts/hypothese.py sceller "trailing resserré" "PnL" "+5$" "abandon si <+2$"
  python3 scripts/hypothese.py essai <id_hyp> ["note"]
  python3 scripts/hypothese.py liste
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from datetime import datetime, timezone

RUNS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "runs")
FICHIER = os.path.join(RUNS, "HYPOTHESES.jsonl")


def _utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _dernier_hash():
    if not os.path.exists(FICHIER):
        return "GENESE"
    h = "GENESE"
    with open(FICHIER, encoding="utf-8") as f:
        for ligne in f:
            ligne = ligne.strip()
            if ligne:
                try:
                    h = json.loads(ligne).get("hash", h)
                except Exception:
                    continue
    return h


def _append(obj):
    contenu = json.dumps(obj, ensure_ascii=False)
    obj["hash"] = hashlib.sha256((_dernier_hash() + contenu).encode("utf-8")).hexdigest()[:16]
    with open(FICHIER, "a", encoding="utf-8") as f:
        f.write(json.dumps(obj, ensure_ascii=False) + "\n")
    return obj


def sceller(hypothese, metrique, seuil_succes, seuil_abandon):
    lignes = []
    if os.path.exists(FICHIER):
        with open(FICHIER, encoding="utf-8") as f:
            lignes = [l for l in f if l.strip()]
    obj = {"id": len(lignes) + 1, "date": _utc(), "hypothese": hypothese,
           "metrique": metrique, "seuil_succes": seuil_succes,
           "seuil_abandon": seuil_abandon, "essais": 0, "statut": "OUVERTE",
           "post_hoc": False}
    obj = _append(obj)
    print(f"[OK] hypothèse #{obj['id']} scellée ({obj['hash']}) — {hypothese}")
    return 0


def essai(id_hyp, note=""):
    print("compteur d'essais : voir R17 — incrémentation manuelle refusée en CLI "
          "(le compteur vit dans HYPOTHESES.jsonl via recompte des runs fantômes). "
          f"Note enregistrée pour #{id_hyp} : {note}")
    return 0


def liste():
    if not os.path.exists(FICHIER):
        print("(vide — aucune hypothèse scellée)")
        return 0
    prec = "GENESE"
    ok = True
    with open(FICHIER, encoding="utf-8") as f:
        for ligne in f:
            ligne = ligne.strip()
            if not ligne:
                continue
            o = json.loads(ligne)
            h = o.pop("hash")
            if hashlib.sha256((prec + json.dumps(o, ensure_ascii=False)).encode("utf-8")).hexdigest()[:16] != h:
                print(f"[!] CHAÎNE ROMPUE sur #{o.get('id')} — fichier touché à la main ?")
                ok = False
            prec = h
            print(f"#{o.get('id')} {o.get('date')} [{'POST_HOC' if o.get('post_hoc') else o.get('statut')}] "
                  f"{o.get('hypothese')} | {o.get('metrique')} | succès: {o.get('seuil_succes')} | "
                  f"abandon: {o.get('seuil_abandon')} | essais: {o.get('essais')}")
    print("chaîne intègre ✔" if ok else "chaîne ROMPUE ✘")
    return 0 if ok else 1


if __name__ == "__main__":
    cmd = (sys.argv[1:] or ["liste"])[0]
    if cmd == "sceller" and len(sys.argv) >= 6:
        raise SystemExit(sceller(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]))
    if cmd == "essai" and len(sys.argv) >= 3:
        raise SystemExit(essai(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else ""))
    if cmd == "liste":
        raise SystemExit(liste())
    print(__doc__)
    raise SystemExit(2)

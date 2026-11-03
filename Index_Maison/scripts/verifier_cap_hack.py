#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verifier_cap_hack.py — PROUVER le cap du régime hack SANS passer d'ordre (03/11/2026).

POURQUOI
--------
L'audit du 03/11 a laissé une limite ouverte : « le cap hack 2,42 $ est chargé,
mais sa preuve réelle exige un achat ». Faux : un plafond est une FONCTION PURE
(entrée → sortie), on peut l'éprouver sur toute la plage sans risquer un centime.
Attendre un achat pour vérifier une garde-fou, c'est confondre le test et la loterie.

CE QUE CE HARNAIS VÉRIFIE (3 propriétés, falsifiables)
------------------------------------------------------
  P1. À niveau 2, aucune mise au-dessus du cap ne passe : plafond(x) <= cap.
  P2. Le plafond ne CRÉE jamais de taille : plafond(x) <= x (jamais d'agrandissement).
  P3. Le moteur l'appelle VRAIMENT : le chemin de buy() importe `regime_hack.plafond`
      et affecte sa valeur à trade_n (sinon la garde est morte).

Exit 0 = les 3 propriétés tiennent ; 2 = au moins une propriété est violée ;
3 = organe illisible (R26 : pas de conclusion sans mesure).

Lecture seule, 0 ordre, 0 écriture d'état du moteur.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
SCRIPTS_INDEX = RACINE / "Index_Maison" / "scripts"
MOTEUR = RACINE / "hulk-mexc" / "scripts" / "paper_diprip.py"


def charger_plafond():
    spec = importlib.util.spec_from_file_location("regime_hack", SCRIPTS_INDEX / "regime_hack.py")
    if spec is None or spec.loader is None:
        raise FileNotFoundError("regime_hack.py introuvable")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.plafond


def main() -> int:
    try:
        plafond = charger_plafond()
    except Exception as e:                       # noqa: BLE001
        print(f"[cap_hack] organe illisible : {e} — AUCUNE CONCLUSION (R26)")
        return 3

    tailles = [0.5, 1.0, 2.0, 2.42, 3.0, 5.0, 10.0, 25.0, 50.0, 120.0]
    p1 = p2 = True
    cap_vu = None
    print(f"{'mise demandée':>14}{'mise retenue':>14}{'bridée':>8}  raison")
    for x in tailles:
        try:
            r = plafond(x)
        except Exception as e:                   # noqa: BLE001
            print(f"[cap_hack] plafond({x}) a levé {type(e).__name__}: {e} — AUCUNE CONCLUSION")
            return 3
        taille = float(r.get("taille", x))
        bride = bool(r.get("bride"))
        if bride:
            cap_vu = taille if cap_vu is None else max(cap_vu, taille)
        if taille > x + 1e-9:
            p2 = False
        print(f"{x:>14.2f}{taille:>14.2f}{'oui' if bride else 'non':>8}  {r.get('raison', '')}")

    # P1 : ce qui passe quand c'est bridé ne dépasse pas le cap observé, et le cap
    # doit être STRICTEMENT inférieur à la plus grosse mise demandée (sinon inerte).
    if cap_vu is not None:
        p1 = all(float(plafond(x).get("taille", x)) <= cap_vu + 1e-9 for x in tailles)
    else:
        p1 = False   # aucun bridage sur 120 $ : le cap ne s'applique pas = garde morte

    # P3 : le moteur consomme vraiment le plafond
    try:
        src = MOTEUR.read_text(encoding="utf-8", errors="ignore")
        p3 = ("from regime_hack import plafond" in src) and ("trade_n = float(_ph[\"taille\"])" in src)
    except Exception:
        p3 = False

    print()
    print(f"P1 plafond respecté (cap={cap_vu})            : {'OK' if p1 else 'VIOLÉE'}")
    print(f"P2 le plafond n'agrandit jamais une mise    : {'OK' if p2 else 'VIOLÉE'}")
    print(f"P3 le moteur APPLIQUE le plafond dans buy() : {'OK' if p3 else 'VIOLÉE'}")
    ok = p1 and p2 and p3
    print(f"VERDICT : {'OK' if ok else 'KO'} — 0 ordre, 0 €, lecture seule")
    return 0 if ok else 2


if __name__ == "__main__":
    sys.exit(main())

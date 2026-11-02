#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""rituel_calendrier.py — RITUEL (02/11, GO Christophe).

L'oubli est un problème (historique maison) : ce script est l'œil qui ne
dort jamais. Lit Index_Maison/calendrier.json et sort :
- EN RETARD (échéance passée, statut ouvert) → alerte discipline,
- DÛS (échéance ≤ 2j ou quotidien) → rappel du jour,
- MÉMOIRE (clos) → ce qu'on a déjà testé/payé, pour ne pas le refaire.
Lecture seule, fail-open, exit 0. Branché en étape 1i de discipline_quotidienne.
"""
import json
import os
import sys
from datetime import date, datetime

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAL = os.path.join(BASE, "calendrier.json")
OUT = os.path.join(BASE, "thermo", "calendrier_rituel.json")
HOME = os.path.expanduser("~")

# Moteurs qui ne doivent JAMAIS être aveugles (02/11 : le guetteur a été
# aveugle 3 jours, le fantôme n'avait aucun moteur — « c'était à toi de voir »).
# (nom, chemin, âge max en minutes)
FRAICHEUR = [
    ("guetteur", "ace777-test-day1/Index_Maison/data/sommet_proche_live.json", 30),
    ("fantome", "ace777-test-day1/hulk-mexc/runs/short_shadow_live.json", 30),
    ("whales", "ace777-test-day1/Index_Maison/data/whales_scan_latest.json", 30),
    ("thermo", "ace777-test-day1/Index_Maison/thermo/live.json", 30),
    ("shorts", "ace777-test-day1/hulk-mexc/runs/short_btc_live.json", 30),
    ("flux48", "ace777-test-day1/Index_Maison/data/flux_nets_latest.json", 120),
    ("geopol-gratuit", "ace777-test-day1/Index_Maison/thermo/geopol_gratuit_live.json", 180),
]


def charger():
    try:
        return json.load(open(CAL, encoding="utf-8")).get("items", [])
    except Exception:
        return []


def main() -> int:
    items = charger()
    auj = date.today().isoformat()
    en_retard, dus, a_venir, memoire = [], [], [], []
    for it in items:
        if not isinstance(it, dict):
            continue
        if it.get("statut") == "clos":
            memoire.append(it)
            continue
        ech = str(it.get("echeance") or "")
        if ech == "quotidien":
            dus.append({**it, "raison": "quotidien"})
        elif ech == "sans-date":
            a_venir.append(it)
        else:
            try:
                delta = (date.fromisoformat(ech) - date.fromisoformat(auj)).days
            except ValueError:
                a_venir.append(it)
                continue
            if delta < 0:
                en_retard.append({**it, "jours_retard": -delta})
            elif delta <= 2:
                dus.append({**it, "raison": f"J-{delta}"})
            else:
                a_venir.append({**it, "raison": f"J-{delta}"})
    import subprocess as _sp
    import time as _time
    # 02/11 boucle-source : le matin même, 5 fichiers avaient dérivé du registre
    # sans que personne ne le voie (la veilleuse criait, personne ne rescellait).
    # Le rituel rejoue --liste (lecture seule) : un écart = 🔴 au réveil.
    scelles_ecarts = []
    try:
        _r = _sp.run(["/usr/bin/python3",
                      os.path.join(HOME, "ace777-test-day1/Index_Maison/scripts/resceler.py"),
                      "--liste"], capture_output=True, text=True, timeout=120)
        for _l in (_r.stdout or "").splitlines():
            _l = _l.strip()
            if _l.startswith("écarts") and "0" not in _l.split("→")[0]:
                scelles_ecarts.append(_l)
    except Exception as _e:
        scelles_ecarts.append(f"resceler --liste inexécutable : {_e}")
    aveugles = []
    maintenant = _time.time()
    for nom, chemin, max_min in FRAICHEUR:
        p = chemin if os.path.isabs(chemin) else os.path.join(HOME, chemin)
        try:
            age_min = (maintenant - os.path.getmtime(p)) / 60.0
        except OSError:
            aveugles.append({"moteur": nom, "age_min": None, "raison": "fichier absent"})
            continue
        if age_min > max_min:
            aveugles.append({"moteur": nom, "age_min": round(age_min),
                             "raison": f"vieux de {age_min:.0f} min (max {max_min})"})
    res = {"ts": datetime.now().astimezone().isoformat(timespec="seconds"),
           "en_retard": en_retard, "dus": dus, "a_venir": a_venir,
           "moteurs_aveugles": aveugles,
           "scelles_ecarts": scelles_ecarts,
           "memoire": [{"id": m.get("id"), "titre": m.get("titre"),
                        "origine": m.get("origine")} for m in memoire]}
    try:
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        with open(OUT, "w", encoding="utf-8") as f:
            json.dump(res, f, ensure_ascii=False, indent=1)
    except Exception:
        pass
    print(f"[rituel] EN RETARD={len(en_retard)} DÛS={len(dus)} "
          f"À VENIR={len(a_venir)} AVEUGLES={len(aveugles)} MÉMOIRE={len(memoire)}")
    for a in aveugles:
        print(f"  🔇 MOTEUR AVEUGLE : {a['moteur']} — {a['raison']}")
    for _e in scelles_ecarts:
        print(f"  🔴 SCELLÉ DÉRIVÉ : {_e} — resceler avant midi")
    for it in en_retard:
        print(f"  🔴 EN RETARD {it['jours_retard']}j : {it['titre']} "
              f"(échéance {it['echeance']}, {it.get('origine', '')})")
    for it in dus:
        print(f"  🟡 DÛ ({it.get('raison', '')}) : {it['titre']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

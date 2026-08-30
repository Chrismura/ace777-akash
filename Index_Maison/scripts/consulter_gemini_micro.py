#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation GEMINI SEULE — 6 micro-questions (reponses <= 80 mots).
Usage : python3 consulter_gemini_micro.py <1..6>
"""
import json
import sys
import time
import urllib.request
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = Path(__file__).resolve().parent / "CONSULTATION_GEMINI_PROTOCOLE_20260823"

SYSTEM = ("Tu es GEMINI, auditrice SRE senior ACE777. Sceptique : chaque regle + point faible + garde-fou. "
          "Francais, factuel, SEUILS CHIFFRES, zero bla-bla. Respecte strictement le max de mots.")

CTX = ("ACE777 : hub IA -> detecteurs mempool -> indice -> analyses IA -> evaluation. "
       "Pannes recurrentes : plists boucle, ban API, SYN black-hole, score sature, carnet vide, "
       "mort silencieuse, detecteur aveugle, eval faussee, briefs vides, corrections ecrasees.\n\n")

QUESTIONS = {
    1: CTX + "Q1 : UNE regle d'or d'execution (la plus importante) contre la plu part de ces pannes. Bulletins : regle + seuil + erreur neutralisee + point faible + garde-fou. Max 70 mots.",
    2: CTX + "Q2 : Protocole reseau increvable contre ban API et SYN black-hole (timeout socket inoperant). Bulletins : cadence appelle, repli sources, garde-fou anti-blocage, duree max run. Max 70 mots.",
    3: CTX + "Q3 : Table detection 6 pannes (mort silencieuse, donnees figees, score sature, carnet vide, aveugle, zombie). Format ligne : panne -> signal -> seuil -> frequence. Max 90 mots.",
    4: CTX + "Q4 : Qui surveille le surveillant ? 1 mecanisme increvable : quoi ecrire, quel fichier, age max, qui relit. Max 60 mots.",
    5: CTX + "Q5 : Scoring honnete : cas indecis (ni up ni down) = ?, N minimal pour conclure ?, donnees manquantes ? Bulletins. Max 60 mots.",
    6: CTX + "Q6 : Verdict d'un signal : condition minimale 'il voit le marche' vs 'debrancher' (N, justesse, periode) + reevaluation auto. Max 70 mots.",
}

NAMES = {1: "Q1_regles_dor", 2: "Q2_repli_reseau", 3: "Q3_table_detection",
         4: "Q4_surveillant", 5: "Q5_scoring", 6: "Q6_verdict"}


def ask(q, max_tokens=250, timeout=165):
    body = json.dumps({
        "task": "gemini.analyse",
        "messages": [{"role": "system", "content": SYSTEM},
                     {"role": "user", "content": q}],
        "max_tokens": max_tokens, "temperature": 0.2,
    }).encode()
    req = urllib.request.Request(HUB, data=body,
                                 headers={"Content-Type": "application/json"})
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        d = json.loads(resp.read().decode())
    return d["choices"][0]["message"]["content"].strip(), d.get("provider", "?"), time.time() - t0


def main():
    idx = int(sys.argv[1])
    OUT.mkdir(parents=True, exist_ok=True)
    name = NAMES[idx]
    f = OUT / ("AVIS_GEMINI_" + name + ".md")
    if f.exists():
        print("[DEJA FAIT] " + name)
        return 0
    print("[ENVOI] " + name + "...", flush=True)
    for t in (1, 2, 3):
        try:
            txt, prov, dt = ask(QUESTIONS[idx])
            f.write_text("# AVIS GEMINI · " + name + " (" + prov + " · " + str(int(dt)) + "s)\n\n" + txt + "\n",
                         encoding="utf-8")
            print("[OK] " + name + " (" + prov + " · " + str(int(dt)) + "s · " + str(len(txt)) + " car.)", flush=True)
            return 0
        except Exception as e:
            print("[ERREUR] " + name + " tentative " + str(t) + " : " + type(e).__name__ + " : " + str(e), flush=True)
            time.sleep(3)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
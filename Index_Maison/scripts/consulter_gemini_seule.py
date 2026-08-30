#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation GEMINI SEULE (Christophe : « gemini c tout »).
3 parties A/B/C, contexte condense, reponses <= 900 mots (budget hub 180 s)."""
import json
import sys
import time
import urllib.request
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = Path(__file__).resolve().parent / "CONSULTATION_GEMINI_PROTOCOLE_20260823"

SYSTEM = """Tu es GEMINI, auditeur en chef de la famille ACE777. Tu cherches les angles morts, tu structures, tu ne te contentes pas du premier recit. Diagnostic forensique = ton terrain.

EXIGENCE DE BRILLANCE (Christophe insiste) : Tu ne rends PAS une reponse generique de consultant. Tu es ingenieur Fiabilite Senior (SRE) + concepteur de systemes auto-detectables + sceptique permanent. Pour CHAQUE regle, demande-toi comment un bug trivial, une boucle, un process zombie ou un fichier fige pourrait la contourner — et neutralise-le avec un garde-fou supplementaire. Hierarchise par risque : les FAUSSES ANALYSES (le plus grave) avant le bruit. Contrainte : Mac M1 8 Go, Python stdlib uniquement, free tiers API. Reponse en francais, factuelle, structuree, avec des regles actionnables et des seuils precis, pas de generalites. Max 900 mots par reponse."""

CONTEXTE = """Systeme ACE777 : chaine hub IA -> detecteurs mempool -> indice onchain -> analyses IA (Cortana) -> evaluation.
10 erreurs recurrentes observees (15/08->23/08) :
(1) plists KeepAlive en boucle (scripts 50x trop souvent, ecreasement des corrections)
(2) bombardement API (creusage ~50 appels/2min -> ban, 8h muet)
(3) SYN black-hole reseau (timeout socket ne se declenche pas)
(4) score menteur : cumul 48h sature -> 100 meme avec 0 poussiere (fausses correlations)
(5) artefact carnet vide -> taux 100% (echec de mesure lu comme signal max)
(6) mort silencieuse (detecteur vivant, donnees figees 8h, logs inchanges)
(7) detecteur aveugle (endpoint 404 des jours sans que personne ne signale)
(8) evaluation faussee (cas indecis comptes comme echec : 46% au lieu de 59%)
(9) briefs en boucle (agents qui generent du vide qui consomme des credits)
(10) corrections non durables (un script ecrase le fix d'un autre)."""

QUESTIONS = {
    "A_bon_fonctionnement": CONTEXTE + """

PARTIE A - PROTOCOLE DE BON FONCTIONNEMENT INCASSABLE :
Regles d'or d'execution pour chaque brique (detecteurs mempool, indice, analyses IA) : cadence, ecriture atomique, age maximum des donnees avant invalidation, repli reseau, gestion des ressources (M1 8 Go), comportement en cas d'echec partiel. Pour CHAQUE regle precise : (1) la regle elle-meme, (2) l'erreur du catalogue qu'elle neutralise, (3) son point faible et le garde-fou supplementaire qui le neutralise. Max 850 mots.""",
    "B_detection": CONTEXTE + """

PARTIE B - PROTOCOLE DE DETECTION AUTOMATIQUE DES DERIVES :
Pour CHACUN des 10 modes de panne (1-10) : donne LE DETECTEUR dedie (quel fichier ou signal surveiller, quel seuil, quelle frequence) ET le canal d'alerte. Puis un « tableau de bord sante » minimal : 1 seul fichier JSON qui res tume l'etat de toute la chaine en feux vert/orange/rouge (champs proposes inclus). Dis aussi qui execute ces verifications et comment eviter que le surveillant lui-meme meure en silence. Max 900 mots.""",
    "C_evaluation": CONTEXTE + """

PARTIE C - PROTOCOLE D'EVALUATION HONNETE :
Comment mesurer la justesse reelle de la chaine (analyses IA, pepite, indice) SANS biais : regles de scoring (que fait-on des cas indecis, des echantillons trop petits, des series de donnees manquantes ou artefacts), taille d'echantillon minimale pour tirer une conclusion, fenetre de reference, procedure de verdict « il voit le marche » vs « il ne voit rien -> debrancher », et comment re-evaluer automatiquement sans intervention humaine. Max 850 mots.""",
}


def ask(task, system, user, max_tokens=1200, timeout=175):
    payload = json.dumps({
        "task": task,
        "messages": [{"role": "system", "content": system},
                     {"role": "user", "content": user}],
        "max_tokens": max_tokens, "temperature": 0.3,
    }).encode()
    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        d = json.loads(resp.read().decode())
    return d["choices"][0]["message"]["content"].strip(), d.get("provider", "?")


def summary(arg):
    for name, user in QUESTIONS.items():
        if (OUT / ("AVIS_GEMINI_" + name + ".md")).exists():
            print("[DEJA FAIT] " + name, flush=True)
            continue
        print("[ENVOI] " + name + "...", flush=True)
        try:
            txt, prov = ask("gemini.analyse", SYSTEM, user)
            (OUT / ("AVIS_GEMINI_" + name + ".md")).write_text(
                "# AVIS GEMINI · " + name + " (" + prov + ")\n\n" + txt + "\n", encoding="utf-8")
            print("[OK] " + name + " (" + prov + " · " + str(len(txt)) + " car.)", flush=True)
        except Exception as e:
            print("[ERREUR] " + name + ": " + type(e).__name__ + ": " + str(e), flush=True)
            return 1
    print("[FIN]", flush=True)
    return 0


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    sys.exit(summary([k for k in QUESTIONS]))
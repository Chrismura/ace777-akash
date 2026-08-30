#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dialogue GEMINI SEULE — MEME conversation, historique conserve.

Usage : python3 dialogue_gemini_protocole.py <tour 1..4>
Chaque invocation relit l'etat (messages accumules) et envoie le tour demande.
C'est UNE SEULE session : les messages role=assistant precedents sont reinjectes
a chaque tour (l'historique compte).

Sortie : CONSULTATION_GEMINI_DIALOGUE_20260823/ (etat.json + TOUR*.md)
"""
import json
import sys
import time
import urllib.request
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
HUB = "http://127.0.0.1:11435/v1/chat/completions"
DIR = Path(__file__).resolve().parent / "CONSULTATION_GEMINI_DIALOGUE_20260823"
ETAT = DIR / "etat.json"

SYSTEM = (
    "Tu es GEMINI, auditrice en chef de la famille ACE777. Tu cherches les angles "
    "morts, tu structures, tu ne te contentes pas du premier recit. Diagnostic "
    "forensique = ton terrain. SRE senior : pour CHAQUE regle proposee, identifie "
    "son point faible ET le garde-fou qui le neutralise. Contrainte : Mac M1 8 Go, "
    "Python stdlib uniquement, free tiers API. Reponse en francais, factuelle, "
    "seuils precis, zero bla-bla. Respecte strictement le max de mots demande."
)

CONF_INITIAL = (
    "SYSTEME ACE777 (Mac M1 8 Go, macOS, Python stdlib, plists launchd, hub IA local) : "
    "hub IA -> detecteurs mempool (pepite = tx jamais vues dans la mempool publique, "
    "dust) -> indice onchain -> analyses IA (Cortana) -> evaluation.\n"
    "10 erreurs recurrentes (15/08->23/08) : (1) plists en boucle 50x, (2) ban API par "
    "bombardement, (3) SYN black-hole sans timeout socket, (4) score=cumul 48h sature->100 "
    "a 0, (5) carnet vide->100%, (6) mort silencieuse donnees figees 8h, (7) detecteur "
    "aveugle 404, (8) evaluation faussee (cas indecis=ech ec), (9) briefs vides en boucle, "
    "(10) corrections ecrasees par un autre script.\n\n"
    "PROTOCOLE ACTUEL (etabli avec toi en 6 questions) :\n"
    "R1 Fraicheur bloquante : aucun score/analyse si now - derniere donnee > TTL "
    "(15 min detecteurs, 20 min indice, 1 h analyses) -> STALE, pas de valeur.\n"
    "R2 Ecriture atomique (mkstemp+os.replace) + horodatage + checksum ; hash identique "
    "3 cycles = fige -> alerte.\n"
    "R3 Repli multi-source persistant (mempool.space <-> blockstream.info), bascule "
    "memorisee dans un fichier (survit aux relances launchd), quorum 2/3.\n"
    "R4 Ceinture anti-blocage : SIGALRM sur chaque connexion (prouvee 5.0 s pile) + duree "
    "max run 25-40 s, zero retry infini, kill-switch STOP_ALL.\n"
    "R5 Budget API : max 1 appel/2 s, backoff 2/4/8/16, creusage du detail seulement si "
    "le seuil du signal est franchi (pas sur le bruit de fond).\n"
    "R6 Canari du surveillant : superviseur ecrit watchdog/heartbeat.json (ts, pid, hash) ; "
    "age max 60 s ; relu toutes les 20 s par 2 relecteurs independants ; relance auto si "
    "age > 60 s ou relecture muette 120 s.\n"
    "R7 Budget ressources : run max 25-40 s, memoire max 300 Mo, nbre max de process python "
    "borne ; depassement -> arret + alerte.\n"
    "DETECTION (1 detecteur par panne) : mort silencieuse -> heartbeat age>90 s ; donnees "
    "figees -> hash identique 3 cycles ; score sature 0/100 constant 5 min ; carnet vide "
    "-> 60 s ; aveugle -> 3 erreurs API ; zombie -> 2 min ; corrections ecrasees -> "
    "checksum 1 h.\n"
    "EVALUATION : indecis = 0 point (NI BON NI MAUVAIS, tag NEUTRE) ; N < 30 -> ABSTENTION ; "
    "manquants > 20% -> score NULL ; verdict : voit le marche si N>=30 sur 7 j ET justesse "
    ">= 60% ET pas d'aveugle > 15 min ; debrancher si < 50% ou silence > 15 min ; "
    "re-evaluation auto toutes les 5 min (fenetre 7 j), journal immuable.\n\n"
    "TACHE : passe ce protocole au crible, DEFIE chaque regle, trouve pour chacune la "
    "faille resistante qui reste et neutralise-la par un garde-fou de niveau 2. Puis "
    "donne un PROTOCOLE FINAL INCASSABLE, structure : (A) fonctionnement, (B) detection, "
    "(C) evaluation — avec seuils chiffres. Max 700 mots."
)

RELANCE_2 = (
    "C'est constructif, mais tu peux creuser beaucoup plus profond. Defie maintenant TES "
    "propres regles : pour chaque garde-fou, trouve la maniere EXACTE dont un bug trivial, "
    "une boucle, un process zombie ou un fichier fige peut encore le contourner — et "
    "neutralise ce contournement par un garde-fou de niveau 2. Concentre-toi ensuite sur "
    "ce qui est LE PLUS DANGEREUX pour nous : (B) la DETECTION (comment detecter avant "
    "que soit trop tard, seuils chiffres, qui surveille quoi, qui surveille le "
    "surveillant) et (C) l'EVALUATION (le score sans biais qui ne se laisse ni tromper ni "
    "truquer par un acteur menteur). Ajoute les regles que tu juges VITALES et qui "
    "manquent. Max 700 mots."
)

RELANCE_3 = (
    "Encore plus profond. Pousse jusqu'au plafond : qu'est-ce qui peut encore t'echapper ? "
    "Cherche les angles morts extremes : un etat qui n'a pas de fichier, DEUX pannes "
    "simultanneees, un acteur qui ment EN DISANT qu'il est sain (counterfeit healthy). "
    "Coordonne chaque angle mort et tes remparts. Puis conclue franchement : as-tu atteint "
    "le maximum de ce qu'on peut exiger ? Si oui, ecris TOUT L'UN des deux EXACTEMENT en "
    "tete de reponse : soit 'ON NE PEUT PLUS FAIRE MIEUX' et donne ta conclusion d'ensemble "
    "(3-4 lignes max), soit 'ENCORE UNE AMELIORATION :' et fais-la. Max 600 mots."
)

TOURS_TEXTE = {1: CONF_INITIAL, 2: RELANCE_2, 3: RELANCE_3}


def charger_etat():
    if ETAT.exists():
        return json.loads(ETAT.read_text(encoding="utf-8"))
    return {"messages": [], "tours": [], "reponses": {}}


def sauver_etat(d):
    DIR.mkdir(parents=True, exist_ok=True)
    ETAT.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")


def ask(msgs, max_tokens=800, timeout=290):
    body = json.dumps({
        "task": "gemini.analyse",
        "messages": msgs,
        "max_tokens": max_tokens, "temperature": 0.3,
    }).encode()
    req = urllib.request.Request(HUB, data=body, headers={"Content-Type": "application/json"})
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        d = json.loads(resp.read().decode())
    return d["choices"][0]["message"]["content"].strip(), d.get("provider", "?"), time.time() - t0


def main():
    tour = int(sys.argv[1])
    if tour not in TOURS_TEXTE:
        print("Tour invalide :", tour)
        return 2
    state = charger_etat()
    if tour in state.get("tours", []):
        print("[DEJA FAIT] tour", tour)
        return 0
    msgs = list(state["messages"])
    if not msgs:
        msgs = [{"role": "system", "content": SYSTEM}]
    msgs.append({"role": "user", "content": TOURS_TEXTE[tour]})
    for t in range(1, 4):
        print("[ENVOI] tour " + str(tour) + " (tentative " + str(t) + ")", flush=True)
        try:
            rep, prov, dt = ask(msgs)
            msgs.append({"role": "assistant", "content": rep})
            state["messages"] = msgs
            state["tours"] = state.get("tours", []) + [tour]
            state["reponses"][str(tour)] = {"provider": prov, "duree_s": round(dt), "len": len(rep)}
            sauver_etat(state)
            fichier = DIR / ("TOUR" + str(tour) + ".md")
            fichier.write_text(
                "# TOUR " + str(tour) + " (" + prov + " · " + str(int(dt)) + "s)\n\n" + rep + "\n",
                encoding="utf-8")
            print("[OK] tour " + str(tour) + " · " + str(int(dt)) + "s · " + str(len(rep)) + " car.", flush=True)
            return 0
        except Exception as e:
            print("[ERREUR] " + type(e).__name__ + ": " + str(e), flush=True)
            time.sleep(3)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
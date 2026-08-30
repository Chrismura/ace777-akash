#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dialogue GEMINI SEULE — MEME conversation, historique conserve.
Appel DIRECT a l'API Gemini (pas le hub) : c'est Gemini ou rien.
Attend le reset du quota (429) si besoin, puis enchaîne les 3 tours.
Chaque reponse est sauvegardee immediatement (reprise sans perte).

Usage : python3 dialogue_gemini_direct.py   (peut tourner des heures)
Sortie : CONSULTATION_GEMINI_DIALOGUE_20260823/ (etat.json + TOUR*.md)
"""
import json
import os
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
ENV_PATH = Path(__file__).resolve().parent.parent.parent / "prise-ia" / ".env"
if not ENV_PATH.exists():
    ENV_PATH = Path(os.path.expanduser("~/prise-ia/.env"))
URL = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"
MODEL = "gemini-flash-lite-latest"
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
    ", (5) carnet vide->100%, (6) mort silencieuse donnees figees 8h, (7) detecteur "
    "aveugle 404, (8) evaluation faussee (cas indecis=ech ec), (9) briefs vides en boucle, "
    "(10) corrections ecrasees par un autre script.\n\n"
    "PROTOCOLE ACTUEL (etabli avec toi en 6 questions) :\n"
    "R1 Fraicheur bloquante : aucun score/analyse si now - derniere donnee > TTL "
    "(15 min detecteurs, 20 min indice, 1 h analyses) -> STALE, pas de valeur.\n"
    "R2 Ecriture atomique (mkstemp+os.replace) + horodatage + checksum ; hash identique "
    "3 cycles = fige -> alerte.\n"
    "R3 Repli multi-source persistant (mempool.space <-> blockstream.info), bascule "
    "memorisee dans un fichier (survit aux relances launchd).\n"
    "R4 Ceinture anti-blocage : SIGALRM sur chaque connexion + duree max run 25-40 s, "
    "zero retry infini, kill-switch STOP_ALL.\n"
    "R5 Budget API : max 1 appel/2 s, backoff 2/4/8/16, creusage du detail seulement si "
    "le seuil du signal est franchi.\n"
    "R6 Canari du surveillant : superviseur ecrit heartbeat (ts, pid, hash), age max 60 s, "
    "relu par 2 relecteurs, relance auto si age > 60 s.\n"
    "R7 Budget ressources : run max 25-40 s, memoire max 300 Mo, nombre process borne.\n"
    "DETECTION : mort silencieuse -> heartbeat age>90 s ; figees -> hash 3 cycles ; score "
    "sature 0/100 5 min ; carnet vide -> 60 s ; aveugle -> 3 erreurs API ; zombie -> 2 min ; "
    "corrections ecrasees -> checksum 1 h.\n"
    "EVALUATION : indecis = 0 point (NI BON NI MAUVAIS) ; N < 30 -> ABSTENTION ; manquants "
    "> 20% -> NULL ; verdict : voit le marche si N>=30 sur 7 j ET justesse >= 60% ET pas "
    "d'aveugle > 15 min ; debrancher si < 50% ou silence > 15 min ; re-eval auto 5 min, "
    "journal immuable.\n\n"
    "TACHE : passe ce protocole au crible (auditeur en chef). Defie les regles, trouve la "
    "faille qui reste sur CHACUNE et neutralise-la par un garde-fou de niveau 2. Donne le "
    "PROTOCOLE FINAL INCASSABLE structure : (A) fonctionnement, (B) detection, (C) "
    "evaluation — seuils chiffres. Max 700 mots."
)

RELANCE_2 = (
    "C'est constructif, mais tu peux creuser beaucoup plus profond. Defie maintenant TES "
    "propres regles : pour chaque garde-fou, trouve la maniere EXACTE dont un bug trivial, "
    "une boucle, un process zombie, un temps partiel ou un fichier fige peut encore le "
    "contourner — et neutralise-le (garde-fou niveau 2). Puis attaque (B) la DETECTION : "
    "comment detecter AVANT qu'il soit trop tard, seuils chiffres, qui surveille qui, qui "
    "surveille le surveillant. Et (C) l'EVALUATION : le score sans biais qui ne se laisse "
    "ni tromper ni truquer par un acteur menteur. Ajoute ce que tu juges VITAL et qui "
    "manque. Max 700 mots."
)

RELANCE_3 = (
    "Encore plus profond. Pousse jusqu'au plafond : qu'est-ce qui peut encore t'echapper ? "
    "Les extremes : un etat sans fichier, DEUX pannes simultanees, un acteur qui ment EN "
    "DISANT qu'il est sain (counterfeit healthy). Decris chaque angle mort ET le rempart "
    "qui le neutralise. Puis conclus franchement : as-tu atteint le maximum exigeable ? "
    "Si oui, commences ta reponse EXACTEMENT par 'ON NE PEUT PLUS FAIRE MIEUX' et donne ta "
    "conclusion d'ensemble (3-4 lignes). Sinon commence par 'ENCORE UNE AMELIORATION :' "
    "et fais-la. Max 600 mots."
)

# TOUR 4 — CLOTURE (24/08) : la reponse du tour 3 s'est arretee au milieu de la
# section (C) Evaluation, sans conclusion. On reprend exactement la pour finir :
# completer (C) puis conclure — la condition de fin est verifiee apres coup.
RELANCE_4 = (
    "Ta reponse precedente s'est arretee au milieu de la section (C) Evaluation, sans "
    "conclusion. Reprends exactement la : complete (C) Evaluation (le cas echeant) puis "
    "conclus franchement. As-tu atteint le maximum exigeable ? Si oui, ta reponse doit "
    "commencer EXACTEMENT par 'ON NE PEUT PLUS FAIRE MIEUX' puis donner la conclusion "
    "d'ensemble (3-4 lignes). Sinon commence par 'ENCORE UNE AMELIORATION :' et fais-la. "
    "Ne repete pas ce qui est deja dit aux tours precedents. Max 400 mots."
)

TOURS = {1: CONF_INITIAL, 2: RELANCE_2, 3: RELANCE_3, 4: RELANCE_4}


def charger_etat():
    if ETAT.exists():
        return json.loads(ETAT.read_text(encoding="utf-8"))
    return {"messages": [], "tours": [], "reponses": {}}


def sauver_etat(d):
    DIR.mkdir(parents=True, exist_ok=True)
    ETAT.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")


def lire_cle():
    if not ENV_PATH.exists():
        print("PAS DE .env", flush=True)
        return ""
    for l in ENV_PATH.read_text(encoding="utf-8").splitlines():
        l = l.strip()
        if l.startswith("GEMINI_API_KEY="):
            return l.split("=", 1)[1].strip()
    return ""


def ask_direct(msgs, max_tokens=760, timeout=290):
    """Appel direct Gemini. Retourne (contenu, duree_s) ou leve une exception."""
    cle = lire_cle()
    body = json.dumps({
        "model": MODEL,
        "messages": msgs,
        "max_tokens": max_tokens,
        "temperature": 0.3,
    }).encode()
    req = urllib.request.Request(
        URL, data=body,
        headers={"Content-Type": "application/json", "Authorization": "Bearer " + cle})
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            d = json.loads(resp.read().decode())
        content = d["choices"][0]["message"]["content"].strip()
        return content, time.time() - t0
    except urllib.error.HTTPError as e:
        if e.code == 429:
            raise QuotaError()
        raise
    except Exception as e:
        raise


class QuotaError(Exception):
    pass


def main():
    etat = charger_etat()
    msgs = list(etat["messages"])
    if not msgs:
        msgs = [{"role": "system", "content": SYSTEM}]
    for tour in sorted(TOURS):
        if tour in etat.get("tours", []):
            continue
        msgs.append({"role": "user", "content": TOURS[tour]})
        while True:
            try:
                rep, dt = ask_direct(msgs)
                msgs.append({"role": "assistant", "content": rep})
                etat["messages"] = msgs
                etat["tours"] = etat.get("tours", []) + [tour]
                etat["reponses"][str(tour)] = {"duree_s": round(dt), "len": len(rep)}
                sauver_etat(etat)
                (DIR / ("TOUR%d.md" % tour)).write_text(
                    "# TOUR %d (%.0f s)\n\n%s\n" % (tour, dt, rep), encoding="utf-8")
                print("[OK] tour %d : %.0f s, %d car." % (tour, dt, len(rep)), flush=True)
                break
            except QuotaError:
                print("[429] quota Gemini epuise — attente 15 min...", flush=True)
                time.sleep(900)
            except Exception as e:
                print("[ERREUR] %s: %s — attente 60 s..." % (type(e).__name__, str(e)[:120]), flush=True)
                time.sleep(60)
    print("=== DIALOGUE TERMINE (%d tours) ===" % len(etat.get("tours", [])), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dialogue interactif GEMINI — consultation POUSSIÈRE / BLOCS PRIVATISÉS (24/08).
Directeur d'entretien : un TOUR à la fois. Le directeur (Buffy) lit chaque
réponse, analyse la compréhension du concept, et décide du message suivant
(indice / redirection / confrontation). Rien d'automatique au-delà d'un tour.

Usage :
  python3 dialogue_gemini_poussiere.py                  # TOUR 1 (contexte généraliste, zéro valeur)
  python3 dialogue_gemini_poussiere.py --msg "texte"    # tour suivant (message direct)
  python3 dialogue_gemini_poussiere.py --file f.md      # tour suivant (message depuis un fichier)
  python3 dialogue_gemini_poussiere.py --resume         # affiche l'état sans appeler l'API

Sortie : CONSULTATION_GEMINI_POUSSIERE_20260824/ (etat.json + TOURn.md)
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
DIR = Path(__file__).resolve().parent / "CONSULTATION_GEMINI_POUSSIERE_20260824"
ETAT = DIR / "etat.json"

SYSTEM = (
    "Tu es GEMINI, conceptrice de systèmes de détection onchain pour la famille ACE777. "
    "Ton terrain : la mempool Bitcoin, les blocs minés, les transactions privées (OTC). "
    "Tu conçois un instrument de mesure, pas un gadget : chaque paramètre doit être "
    "justifié par la physique du marché (résolution temporelle, turnover de la mempool, "
    "taille des blocs, frais, volume). Tu donnes des VALEURS CHIFFRÉES précises, jamais "
    "des généralités. Contrainte : Mac M1 8 Go, Python stdlib uniquement, API gratuites "
    "sans clé (mempool.space / blockstream.info), budget API limité (on ne fait JAMAIS "
    "N appels pour N transactions). Réponds en français, factuel, structuré."
)

# TOUR 1 — contexte généraliste, AUCUNE valeur de notre côté.
TOUR1 = (
    "SYSTÈME ACE777 — détecteur de blocs privatisés / transactions fantômes.\n\n"
    "Le concept à mesurer : une transaction incluse dans un bloc miné mais ABSENTE de la "
    "mempool publique = transaction privée (OTC) ou CPFP masqué (Child Pays For Parent). "
    "C'est un instrument de détection utilisé par les gros acteurs. Le taux de « fantômes » "
    "d'un bloc (tx du bloc jamais vues dans la mempool publique) est le signal central.\n\n"
    "L'architecture actuelle (à challenger, pas à valider) :\n"
    "1. Un détecteur prend des SNAPSHOTS de la mempool publique (liste des txids) à intervalle "
    "régulier et les conserve dans un carnet local (fenêtre glissante).\n"
    "2. Pour chaque bloc miné, il compare les txids du bloc à ce carnet : toute tx du bloc "
    "jamais vue dans la fenêtre = « fantôme ».\n"
    "3. Il en sort un TAUX (%) par bloc + un volume échantillonné.\n"
    "4. Ce signal alimente un INDICE onchain unifié avec d'autres signaux (poussière à frais "
    "bas, z-score, baleines) pour donner une note 0-100.\n\n"
    "Leçons apprises (à intégrer à ton design) :\n"
    "- La résolution d'échantillonnage est cruciale : si l'intervalle entre snapshots est trop "
    "long, des transactions normales entrent ET sont minées entre deux snapshots → faussement "
    "« fantômes » (bruit de résolution).\n"
    "- Un carnet vide (démarrage, coupure réseau) a déjà produit un faux taux de 100 % → "
    "fausse alerte. Le design doit intégrer une notion de FIABILITÉ de la mesure.\n"
    "- Les API sont gratuites et sans clé : on ne peut pas télécharger le détail de toutes les "
    "transactions d'un bloc (plusieurs milliers). Le volume doit être estimé sans exploser l'API.\n\n"
    "TA CHE : conçois le setup OPTIMAL pour mesurer ce signal. Donne-moi TON design complet "
    "avec TES valeurs chiffrées pour chacun de ces points :\n"
    "(a) l'intervalle de snapshot (résolution temporelle) et la fenêtre du carnet ;\n"
    "(b) le seuil de fiabilité (quand la mesure devient-elle exploitable, et comment éviter "
    "le faux 100 % sur carnet vide) ;\n"
    "(c) comment estimer le volume d'une tx fantôme sans télécharger tout le détail ;\n"
    "(d) les seuils d'alerte (taux + volume) qui distinguent un VRAI événement privé du bruit ;\n"
    "(e) la méthode de validation (comment prouver que l'indicateur marche) ;\n"
    "(f) tout garde-fou que tu juges vital pour que la mesure ne mente jamais.\n"
    "Justifie CHAQUE valeur par la physique du marché (turnover mempool, taille de bloc, "
    "frais). Maximum 700 mots."
)

TOURS = {1: TOUR1}


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


def ask_direct(msgs, max_tokens=1400, timeout=290):
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

    args = sys.argv[1:]
    if "--resume" in args:
        print("Tours faits :", etat.get("tours", []))
        for t in etat.get("tours", []):
            r = etat.get("reponses", {}).get(str(t), {})
            print(f"  TOUR {t} : {r.get('duree_s')}s, {r.get('len')} car.")
        return 0

    # Déterminer le message à envoyer
    if "--msg" in args:
        i = args.index("--msg")
        msg = args[i + 1]
        tour = max(etat.get("tours", []) or [0]) + 1
    elif "--file" in args:
        i = args.index("--file")
        f = Path(args[i + 1])
        msg = f.read_text(encoding="utf-8")
        tour = max(etat.get("tours", []) or [0]) + 1
    else:
        # TOUR 1 : contexte initial
        if etat.get("tours"):
            print("Tour 1 déjà fait — utilisez --msg ou --file pour le tour suivant.", flush=True)
            return 1
        msg = TOUR1
        tour = 1

    msgs.append({"role": "user", "content": msg})
    print(f"[ENVOI] TOUR {tour}...", flush=True)
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
            print("[OK] TOUR %d : %.0f s, %d car." % (tour, dt, len(rep)), flush=True)
            print("=" * 60, flush=True)
            print(rep, flush=True)
            return 0
        except QuotaError:
            print("[429] quota Gemini épuisé — attente 15 min...", flush=True)
            time.sleep(900)
        except Exception as e:
            print("[ERREUR] %s: %s — attente 60 s..." % (type(e).__name__, str(e)[:120]), flush=True)
            time.sleep(60)


if __name__ == "__main__":
    sys.exit(main())
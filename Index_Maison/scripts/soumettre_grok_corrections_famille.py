#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""soumettre_grok_corrections_famille.py — 10/08 : soumet les 11 CORRECTIONS
du JUGEMENT FAMILLE à GROK pour la SPEC V2 du setup des 3 étages.

Etape 1 de la liste famille (JUGEMENT_3ETAGES_2026-08-10/SYNTHESE.md) :
« Faire corriger la spec par Grok (v2) avec les 11 points C1-C11. »
Ne RIEN executer avant la validation explicite de Christophe (etape 2).

Envoie a Grok (via le hub, model puter-grok) :
1. l'etat REEL mesure mecaniquement a l'instant T
2. les 11 points du jugement famille (C1-C11) a integrer
3. la demande : la spec v2 CORRIGEE (pas un plan, la spec)

Reponse -> ~/ace777-test-day1/Index_Maison/ARCHITECTURE_GROK_2026-08-09/REPONSE_GROK_SPECV2_CORRIGEE.md
"""

import json
import os
import subprocess
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUTBOX = "/Users/christophe/ace777-test-day1/Index_Maison/OUTBOX_OBSIDIAN/A_Mon_Attention"
ARCHIVE_DIR = "/Users/christophe/ace777-test-day1/Index_Maison/ARCHITECTURE_GROK_2026-08-09"
BRIEF_PATH = os.path.join(OUTBOX, "BRIEF_GROK_CORRECTIONS_FAMILLE_2026-08-10.md")
OUT = os.path.join(ARCHIVE_DIR, "REPONSE_GROK_SPECV2_CORRIGEE.md")


def run(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, text=True,
                                       timeout=15).strip()
    except Exception:
        return ""


def etat_reel():
    """Mesures mecaniques, pas de memoire."""
    hub = run("curl -s --max-time 10 http://127.0.0.1:11435/health")
    services = run("launchctl list | grep -ci ace777")
    vivants = run(
        "launchctl list | grep ace777 | awk '$1 ~ /^[0-9]+$/ {print $3}' | tr '\\n' ' '")
    superviseur = run("launchctl list | grep superviseur")
    ram = run("memory_pressure 2>/dev/null | head -2")
    date = run("date '+%Y-%m-%d %H:%M:%S %Z'")
    return {
        "date": date,
        "hub_health": hub or "PAS DE REPONSE",
        "nb_services_charge": services or "?",
        "services_vivants": vivants or "aucun",
        "superviseur": superviseur or "absent",
        "ram": ram or "?",
    }


CORRECTIONS = """\
CONTEXTE : Tu as concu REPONSE_GROK_3ETAGES.md (spec setup des 3 etages) puis
REPONSE_GROK_V2_HARMONIE.md et REPONSE_GROK_V21_BRUT.md. La FAMILLE COMPLETE
(GEMINI + DEEPSEEK + JUGE + ULTRA) a juge ta spec le 10/08 : VERDICT
« VALIDE AVEC MODIFICATIONS » (unanime) — 11 points de consensus a integrer.
Ta mission : produire la SPEC V2 CORRIGEE, pas un plan : le texte spec exact,
pret a executer, avec les 11 corrections integrees POINT PAR POINT.

LES 11 CORRECTIONS (JUGEMENT FAMILLE 10/08, consensus des 4 membres) :

C1. INVENTAIRE EXACT AVANT TOUTE SUPPRESSION (Etape 0) : launchctl list + launchctl
    print par service + dependances inter-services + budget RAM mesure par
    service. (Sans inventaire, la reduction 27->13 = tir a l'aveugle.)

C2. KeepAlive:false + ThrottleInterval:1800 = FAUX : launchd ne relancera JAMAIS
    le superviseur apres sa sortie -> il ne tourne qu'une fois. Remplacer par
    StartInterval:1800 (ou KeepAlive:true + boucle interne sleep 60-120s).
    Un heartbeat a 30 min n'en est plus un.

C3. BACKUP PLISTS OBLIGATOIRE avant Etape 4 : copie tar de ~/Library/LaunchAgents
    + checksums + test de reversibilite (restore + reload) AVANT de continuer.

C4. NE PAS TOUCHER cockpit-http/pont au depart : cockpit.py doit d'abord
    LIRE/cohabiter avec eux, ne les remplacer qu'apres avoir expose la meme API
    et bascule les consommateurs.

C5. UNLOAD UN PAR UN avec test 10 min : un service desactive a la fois + delai
    de test + audit des dependances avant chaque suppression.

C6. Mode probatoire C6 + boucle 30 min = CONTRADICTION : 48 cycles/jour vs
    1 action/jour. Solution : compteur journalier persistant dans state.json
    (ou C6 = « 1 type d'action/jour », ou observation seule dry-run).

C7. C1 = detection + alerte, JAMAIS chmod auto : chmod 444 EST une ecriture,
    le superviseur violerait C1 en l'appliquant. C1 = stat + alerte + journal
    + sanction via C5 (unload service fautif).

C8. RAM < 25 Mo irrealiste en Python : Python + libs ≈ 35-50 Mo RSS. Stdlib
    only (urllib, subprocess vm_stat/launchctl) OU cible < 50 Mo assumee.

C9. TEST DE CHARGE AVANT activation pleine : 1h de superviseur avec 13 services,
    mesurer RAM/CPU, /health reste OK + metriques de reference AVANT pour
    comparer APRES.

C10. GESTION DU CRASH DU SUPERVISEUR : qui le relance s'il meurt ? Wrapper
     KeepAlive:true ou watchdog dedie.

C11. TIMEOUT PAR PROVIDER dans cockpit.py : max 2s/provider pour ne jamais
     bloquer le cockpit.

CONTRAT DE SORTIE : reponds avec 1) SPEC V2 CORRIGEE complete (le texte spec
exact, etape par etape, avec les 11 corrections marquees [C1]...[C11] a
l'endroit ou elles s'appliquent) 2) une ligne finale : VERDICT SPEC V2 : OK.
"""

BASE = """\
Systeme ACE777 - Mac 8 Go, hub local port 11435, 9 providers gratuits.
Setup des 3 etages en cours (27 services launchd -> cible 12-14).

ETAT REEL (mesure mecaniquement, pas de memoire) :
- date : %(date)s
- hub /health : %(hub_health)s
- nb services ace777 charges : %(nb_services_charge)s
- services vivants : %(services_vivants)s
- superviseur : %(superviseur)s
- ram : %(ram)s

%(corrections)s
"""


def main():
    ctx = etat_reel()
    brief = BASE % dict(ctx, corrections=CORRECTIONS)
    os.makedirs(OUTBOX, exist_ok=True)
    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    with open(BRIEF_PATH, "w", encoding="utf-8") as f:
        f.write("# BRIEF GROK — CORRECTIONS FAMILLE SPEC V2 (3 etages) — 10/08\n\n")
        f.write(brief)

    payload = {
        "model": "puter-grok",
        "messages": [
            {"role": "system", "content": (
                "Tu es GROK, architecte externe de la famille ACE777. La famille "
                "a juge ta spec : VALIDE AVEC MODIFICATIONS. Produis la SPEC V2 "
                "CORRIGEE avec les 11 corrections, point par point, sans les "
                "oublier. Spec exacte, pas un plan vague. Ne touche JAMAIS au "
                "hub (port 11435).")},
            {"role": "user", "content": brief},
        ],
        "temperature": 0.3,
        "max_tokens": 8000,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    contenu = d["choices"][0]["message"]["content"]
    provider = d.get("provider", "?")
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("# REPONSE GROK — SPEC V2 CORRIGEE (via %s) — 10/08/2026\n\n%s\n"
                % (provider, contenu))
    print("[OK] reponse Grok (%d chars) via %s -> %s" % (len(contenu), provider, OUT))


if __name__ == "__main__":
    main()

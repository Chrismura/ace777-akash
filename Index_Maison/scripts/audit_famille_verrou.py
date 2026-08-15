#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audit_famille_verrou.py — 13/08 : AUDIT FAMILLE du code
« verrou famille + mode tempête + budget dynamique » (loi 1quinquies).

Flux : SPEC (superviseur) -> codeur du hub -> AUDIT FAMILLE -> intégration -> GO Christophe.

LA FAMILLE COMPLETE (décision Christophe 10/08 : un check-up de modifications
mérite toute l'attention possible) :
  - GEMINI   -> task audit.protocol  (gemini)
  - DEEPSEEK -> task mission         (nvidia / deepseek-v4-flash)
  - JUGE     -> task signets.juge    (openrouter-juge)
  - ULTRA    -> task ultra.analyse   (openrouter-ultra)

Loi du brut : on soumet le RÉEL (le code complet), pas un résumé.

Réponses -> ~/ace777-test-day1/Index_Maison/AUDIT_PREFLIGHT_2026-08-13/<MEMBRE>.md
"""
import json
import os
import subprocess
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
AUDIT_DIR = "/Users/christophe/ace777-test-day1/Index_Maison/AUDIT_PREFLIGHT_2026-08-13"
CODE_PATH = "/Users/christophe/ace777-test-day1/CODE_preflight_check_reserve_v1.md"
SPEC_PATH = "/Users/christophe/ace777-test-day1/SPEC_preflight_check_reserve_v1.md"
GEMINI_TASK = "audit.protocol"
DEEPSEEK_TASK = "mission"
JUGE_TASK = "signets.juge"
ULTRA_TASK = "ultra.analyse"


def run(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, text=True,
                                       timeout=20).strip()
    except Exception:
        return ""


def contexte():
    c = {}
    c["code"] = run("cat %s" % CODE_PATH)
    c["spec"] = run("cat %s" % SPEC_PATH)
    c["hub"] = run("curl -s --max-time 10 http://127.0.0.1:11435/health")
    c["proc"] = run("pgrep -lf 'soumettre_hub_illimite' || echo '(aucun)'")
    return c


BASE = """\
Systeme ACE777 - Mac 8 Go, hub 11435, providers gratuits. LOI 1quinquies (contrat autogestion) : LE CODEUR DU HUB CODE, le superviseur SPECIFIE/INTEGRE/TESTE.

CONTEXTE DU CHANTIER (13/08) :
Le 13/08, une boucle famille incontrolee (launchd cortana.urgent toutes les 10s -> cockpit_mission_feed -> ada_gardienne.scan() -> consulter_famille() -> trio hub) a consomme ~900 appels cloud/h de 11:58Z a 12:55Z, explosant le budget (480) a 1310. Cause racine : l'anti-spam 5 min etait ecrit a la FIN de la consultation (thread detache), donc chaque appel 10s relancait une consultation pendant que le trio tournait.

PRINCIPE FONDATEUR (decision Christophe) : ACE777 est une machine de tempete, il doit fonctionner de sa forme dans les tempetes. Les garde-fous protegent le calme, ils ne doivent JAMAIS ralentir la reaction a une tempete. Le budget n'est PAS une valeur fixe : il se recalcule CHAQUE JOUR au moment du check, une fois que le hub a decide sa rotation de modeles. Les providers GRATUITS ne se coupent jamais (bascule meme famille).

CE QUI EST SOUMIS A TON AUDIT (le REEL, loi du brut) :
- SPEC_preflight_check_reserve_v1.md : la spec du chantier
- CODE_preflight_check_reserve_v1.md : le code produit par le codeur (3 livrables : famille_session.py, budget_hub.py, tests)

REGLES D'AUDIT :
- Verrou anti-doublon : le verrou doit etre pose AU DEBUT et TENIR PENDANT TOUTE la consultation (le trio prend 30-60s). POINT DE VIGILANCE DU SUPERVISEUR : dans le code livre, le lock est relache dans finally apres time.sleep(0.1) alors que le thread trio tourne encore — verifier si un appel 10s plus tard peut repasser (ce serait le bug original qui reste).
- Anti-spam : ecrit au debut, meme en cas d'echec du trio.
- Mode tempete : declencheurs (zone ROUGE/PRENDS_LA_PERTE, alarme, vortex>=2) -> consultation immediate, anti-spam 60s, cap horaire desactive. Jamais bloque par le cap.
- Budget : recalcul quotidien, table CAPACITES completee (puter-grok, inferx-coder, openrouter-ultra, openrouter-juge), gratuits jamais coupes, reserve storm 20%, jamais de local (C9).
- Le code doit etre Python 3.9 stdlib, non fatal, commentaires en francais.
- Verifie aussi : le code est-il INTEGRABLE tel quel, ou manque-t-il des morceaux (le trio hub reel est-il present ou remplace par un placeholder 'pass' ?) ?

Reponds en francais : verdict GO / GO AVEC RESERVES / NON, avec reserves concretes (fichier + ligne si possible).

Hub /health : %%HUB%%
--- SPEC ---
%%SPEC%%
--- CODE ---
%%CODE%%
--- processus actifs ---
%%PROC%%
"""


def soumettre(task, sysprompt, outfile):
    ctx = contexte()
    mission = (BASE
               .replace("%%HUB%%", ctx["hub"] or "PAS DE REPONSE")
               .replace("%%SPEC%%", ctx["spec"] or "(illisible)")
               .replace("%%CODE%%", ctx["code"] or "(illisible)")
               .replace("%%PROC%%", ctx["proc"] or "(vide)"))
    payload = {
        "task": task,
        "messages": [
            {"role": "system", "content": sysprompt},
            {"role": "user", "content": mission},
        ],
        "temperature": 0.2,
        "max_tokens": 2500,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    contenu = d["choices"][0]["message"]["content"]
    provider = d.get("provider", "?")
    os.makedirs(AUDIT_DIR, exist_ok=True)
    with open(outfile, "w", encoding="utf-8") as f:
        f.write("# AVIS %s (task %s)\n\nprovider: %s\n\n%s\n"
                % (os.path.basename(outfile).replace(".md", ""), task, provider, contenu))
    print("[OK] %s -> %s (%d chars)" % (outfile, provider, len(contenu)))


def main():
    print("== Soumission GEMINI (audit.protocol) ==")
    soumettre(GEMINI_TASK,
              "Tu es GEMINI, membre de la famille ACE777 (auditeur de protocole). "
              "Audite le code verrou/tempete/budget avec un oeil critique : "
              "le verrou tient-il pendant toute la consultation ? l'anti-spam est-il "
              "ecrit au debut ? le mode tempete protege-t-il la machine sans la "
              "ralentir ? le code est-il integrable (pas de placeholder) ?",
              os.path.join(AUDIT_DIR, "GEMINI.md"))
    print("== Soumission DEEPSEEK (mission) ==")
    soumettre(DEEPSEEK_TASK,
              "Tu es DEEPSEEK, membre senior de la famille ACE777. Audite ce code. "
              "Tu es critique, factuel, tu ne valides pas par complaisance : "
              "verrou reel (flock) pendant toute la duree, anti-spam au debut meme "
              "en echec, mode tempete (ROUGE/alarme/vortex) jamais bloque, budget "
              "quotidien dynamique, gratuits jamais coupes, Python 3.9 stdlib, "
              "code integrable sans placeholder.",
              os.path.join(AUDIT_DIR, "DEEPSEEK.md"))
    print("== Soumission JUGE (signets.juge) ==")
    soumettre(JUGE_TASK,
              "Tu es le JUGE, verificateur independant ACE777. Tu valides ou "
              "invalides ce code. Exigeant sur : la cause racine est-elle vraiment "
              "corrigee (un appel 10s plus tard ne relance plus une consultation "
              "pendant que le trio tourne) ? le principe tempete est-il respecte "
              "(reaction rapide en tempete, protection en calme) ? Verdict clair : "
              "GO / GO AVEC RESERVES / NON.",
              os.path.join(AUDIT_DIR, "JUGE.md"))
    print("== Soumission ULTRA (ultra.analyse) ==")
    soumettre(ULTRA_TASK,
              "Tu es ULTRA, membre expert de la famille ACE777 (analyse profonde). "
              "Analyse ce code en profondeur : coherence globale entre la spec et "
              "le code, failles restantes, integration sans casse du flux existant "
              "(famille_session.py, budget_hub.py, cockpit). Le code est-il pret "
              "pour l'integration et les tests hermetiques ?",
              os.path.join(AUDIT_DIR, "ULTRA.md"))


if __name__ == "__main__":
    main()

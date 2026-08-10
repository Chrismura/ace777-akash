#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audit_famille_codeur.py — 10/08 : AUDIT FAMILLE COMPLET du FLUX CODEUR (loi 1quinquies).

Valide les 3 scripts du flux « le codeur du hub code, Ada ne code pas » :
- deleguer_codeur.py  (point d'entrée unique : spec -> codeur -> réponse)
- soumettre_hub_illimite.py (timeout=None, retry 3x, erreurs HTTP différenciées)
- lancer_detache.py   (start_new_session macOS, logs vers fichier)

Contexte soumis : revue experte du codeur (6 corrections) + corrections v2
(revue tiers) + tests réels (3 échecs propres + flux valide OK).

Loi du brut : on soumet le RÉEL (les scripts complets), pas un résumé.

LA FAMILLE COMPLETE (decision Christophe 10/08 : un check-up de modifications
merite toute l'attention possible, pas 2 membres sur 4) :
  - GEMINI   -> task audit.protocol  (gemini)
  - DEEPSEEK -> task mission         (nvidia / deepseek-v4-flash-0731)
  - JUGE     -> task signets.juge    (openrouter-juge)
  - ULTRA    -> task ultra.analyse   (openrouter-ultra)

Réponses -> ~/ace777-test-day1/Index_Maison/AUDIT_CODEUR_2026-08-10/<MEMBRE>.md
"""
import json
import os
import subprocess
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
AUDIT_DIR = "/Users/christophe/ace777-test-day1/Index_Maison/AUDIT_CODEUR_2026-08-10"
SCRIPTS_DIR = "/Users/christophe/ace777-test-day1/Index_Maison/scripts"
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
    c["deleguer"] = run("cat %s/deleguer_codeur.py" % SCRIPTS_DIR)
    c["soumettre"] = run("cat %s/soumettre_hub_illimite.py" % SCRIPTS_DIR)
    c["lancer"] = run("cat %s/lancer_detache.py" % SCRIPTS_DIR)
    c["spec_v2"] = run("cat %s/SPEC_revue_scripts_timeout_v2.md" % SCRIPTS_DIR)
    c["hub"] = run("curl -s --max-time 10 http://127.0.0.1:11435/health")
    c["proc"] = run("pgrep -lf 'soumettre_hub_illimite' || echo '(aucun processus actif)'")
    return c


BASE = """\
Systeme ACE777 - Mac 8 Go, hub 11435, 9 providers. LOI 1quinquies (contrat autogestion, 10/08) : LE CODEUR DU HUB CODE, ADA SPECIFIE/INTEGRE/TESTE — Ada n'ecrit pas de code. Decision Christophe : « ce que je voulais, c'est faire coder au codeur, pas TOI. Il est l'expert. »

CE QUI EST SOUMIS A TON AUDIT (le REEL, loi du brut) :
1. deleguer_codeur.py : point d'entree UNIQUE du flux. Verifie spec (existante + >20 octets, refus spec vide AVANT lancement), ecrit la mission (verifiee non vide), lance le codeur DETACHE (lancer_detache.py), timeout lancement 60s avec gestion TimeoutExpired.
2. soumettre_hub_illimite.py : timeout=None (illimite, jamais coupe une IA en plein raisonnement), retry 3x avec erreurs HTTP DIFFERENCIEES (429/5xx retryables, 4xx non-retryables exit 1), requete reconstruite a chaque essai, garde mission existante/non vide (plus de traceback), ecrit la reponse dans un fichier pollable.
3. lancer_detache.py : start_new_session=True (equivalent macOS de setsid qui N'EXISTE PAS sur Mac), stdout/stderr rediriges vers fichier de log (diagnostic), le processus SURVIT a la mort du shell.

HISTORIQUE : le codeur du hub a fait une revue experte de ces scripts -> 6 corrections integrees (requete reconstruite, erreurs HTTP retryables, logs detache, verification mission, timeout 60s, import urllib.error). Un reviewer tiers a trouve 2 failles -> resoumises AU CODEUR -> corrections v2 (spec <20 octets refuse, mission inexistante/vide refusee).

TESTS REELS effectues : 3 cas d'echec propres (spec vide exit 1, spec 10 octets exit 1, mission absente exit 1 - messages clairs, zero traceback) + flux valide OK (spec -> delegue -> codeur nvidia -> reponse complete en 10-20s).

REGLES D'AUDIT :
- Verifie que le flux respecte la loi 1quinquies : le codeur code, Ada integre/teste, rien d'autre.
- Verifie la robustesse : timeout illimite, retries, erreurs HTTP, detachement, gardes d'entree.
- Verifie l'ABSENCE de faille qui couterait du temps/des credits (le probleme de fond du 10/08).
- Verifie que rien ne peut plus etre coupe en plein milieu (la persecution des timeouts).

Reponds en francais : verdict GO / GO AVEC RESERVES / NON, avec reserves concretes (fichier + ligne si possible).

Hub /health : %s
--- deleguer_codeur.py ---
%s
--- soumettre_hub_illimite.py ---
%s
--- lancer_detache.py ---
%s
--- SPEC_revue_scripts_timeout_v2.md (les 2 failles corrigees) ---
%s
--- processus actifs ---
%s
"""


def soumettre(task, sysprompt, outfile):
    ctx = contexte()
    mission = BASE % (ctx["hub"] or "PAS DE REPONSE",
                      ctx["deleguer"] or "(illisible)",
                      ctx["soumettre"] or "(illisible)",
                      ctx["lancer"] or "(illisible)",
                      ctx["spec_v2"] or "(illisible)",
                      ctx["proc"] or "(vide)")
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
              "Audite le flux codeur loi 1quinquies avec un oeil critique sur : "
              "respect de la regle (le codeur code, Ada ne code pas), robustesse "
              "anti-timeout, gardes d'entree, zero perte de temps/credits.",
              os.path.join(AUDIT_DIR, "GEMINI.md"))
    print("== Soumission DEEPSEEK (mission) ==")
    soumettre(DEEPSEEK_TASK,
              "Tu es DEEPSEEK, membre senior de la famille ACE777. Audite le flux "
              "codeur loi 1quinquies. Tu es critique, factuel, tu ne valides pas "
              "par complaisance : robustesse reelle, gardes d'entree, "
              "detachement macOS, zero perte de temps/credits.",
              os.path.join(AUDIT_DIR, "DEEPSEEK.md"))
    print("== Soumission JUGE (signets.juge) ==")
    soumettre(JUGE_TASK,
              "Tu es le JUGE, verificateur independant ACE777. Tu valides ou "
              "invalides le flux codeur. Exigeant sur : respect de la loi "
              "1quinquies, robustesse reelle (timeout illimite, retries, "
              "detachement), gardes d'entree, absence de faille coutante.",
              os.path.join(AUDIT_DIR, "JUGE.md"))
    print("== Soumission ULTRA (ultra.analyse) ==")
    soumettre(ULTRA_TASK,
              "Tu es ULTRA, membre de la famille ACE777 (analyse profonde). "
              "Audite le flux codeur loi 1quinquies en profondeur : architecture, "
              "robustesse, gardes d'entree, detachement, cas limites.",
              os.path.join(AUDIT_DIR, "ULTRA.md"))


if __name__ == "__main__":
    main()

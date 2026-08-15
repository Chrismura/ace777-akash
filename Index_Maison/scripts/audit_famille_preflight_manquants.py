#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audit_famille_preflight_manquants.py — 13/08 : complète l'audit famille
du bloc preflight (GEMINI a déjà répondu dans le premier run)."""
import json
import os
import subprocess
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
AUDIT_DIR = "/Users/christophe/ace777-test-day1/Index_Maison/AUDIT_PREFLIGHT_2026-08-13"
CODE_PATH = "/Users/christophe/ace777-test-day1/CODE_preflight_check_reserve_v1.md"
SPEC_PATH = "/Users/christophe/ace777-test-day1/SPEC_preflight_check_reserve_v1.md"


def run(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, text=True, timeout=20).strip()
    except Exception:
        return ""


def contexte():
    c = {}
    c["code"] = run("cat %s" % CODE_PATH)
    c["spec"] = run("cat %s" % SPEC_PATH)
    c["hub"] = run("curl -s --max-time 10 http://127.0.0.1:11435/health")
    c["proc"] = run("pgrep -lf 'preflight_ace777' || echo '(aucun)'")
    return c


BASE = """\
Systeme ACE777 - Mac 8 Go, hub 11435, providers gratuits. LOI 1quinquies (contrat autogestion) : LE CODEUR DU HUB CODE, le superviseur SPECIFIE/INTEGRE/TESTE.

CONTEXTE DU CHANTIER (13/08) : le bug de boucle famille a ete corrige (verrou flock + TTL + mode tempete), le budget est dynamique (recalcul quotidien, gratuits jamais coupes, reserve storm 20%), et un prechauffage de la reserve (prechauffage_reserve.py) verifie la reserve storm a l'avance. Dernier chantier : ajouter au preflight (check avant chaque run) la verification que la reserve storm est en place et fonctionnelle au decollage.

PRINCIPE FONDATEUR (Christophe) : « qu'on soit sur un peu a l'avance que la reserve tempete soit effectivement fonctionnelle — qu'on ne bascule pas dessus en tempete et qu'il n'y ait personne. » Le preflight est le check avant decollage : il doit verifier budget, gratuits dynamiques, rapport de prechauffage recent, et executable, SANS bloquer le run (warning non fatal).

CE QUI EST SOUMIS A TON AUDIT (le REEL, loi du brut) :
- SPEC_preflight_check_reserve_v1.md : la spec (R1 budget/reserve, R2 gratuits, R3 rapport recent, R4 executable)
- CODE_preflight_check_reserve_v1.md : le bloc shell produit par le codeur, a inserer dans scripts/preflight_ace777.sh avant la section Ruby

REGLES D'AUDIT :
- Le bloc utilise les helpers existants ok()/warn() du preflight (ok -> PREFLIGHT_OK, warn -> PREFLIGHT_WARN non fatal).
- Non fatal : un warning ne bloque pas le run, mais doit etre clair.
- Chemins ~/prise-ia/ corrects (routing.json, providers.json, prechauffage_reserve.json, prechauffage_reserve.py).
- Ne casse pas les checks existants du preflight (champion, Binance, orphelines, vortex, Ruby).
- Bash macOS compatible (set -euo pipefail dans le script parent — verifier que les commandes ne font pas planter le script si un fichier manque).
- Verifie : le bloc est-il integrable tel quel ? Les parseurs python inline sont-ils robustes (fichier absent, JSON invalide) ?

Reponds en francais : verdict GO / GO AVEC RESERVES / NON, avec reserves concretes (ligne du bloc si possible).

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
    print("== DEEPSEEK (mission) ==")
    soumettre("mission",
              "Tu es DEEPSEEK, membre senior de la famille ACE777. Audite ce bloc "
              "shell preflight. Tu es critique, factuel, tu ne valides pas par "
              "complaisance : helpers ok/warn corrects, non fatal, chemins justes, "
              "parseurs robustes (fichier absent/JSON invalide sans crash), "
              "integration sans casse des checks existants.",
              os.path.join(AUDIT_DIR, "DEEPSEEK.md"))
    print("== JUGE (signets.juge) ==")
    soumettre("signets.juge",
              "Tu es le JUGE, verificateur independant ACE777. Tu valides ou "
              "invalides ce bloc preflight. Exigeant sur : le check decollage "
              "repond-il au principe (savoir a l'avance si la reserve storm est "
              "fonctionnelle) ? le bloc ne casse-t-il pas le preflight existant ? "
              "Verdict clair : GO / GO AVEC RESERVES / NON.",
              os.path.join(AUDIT_DIR, "JUGE.md"))
    print("== ULTRA (ultra.analyse) ==")
    soumettre("ultra.analyse",
              "Tu es ULTRA, membre expert de la famille ACE777 (analyse profonde). "
              "Analyse ce bloc preflight en profondeur : coherence avec la spec "
              "R1-R4, failles restantes (chemins, robustesse bash sous set -euo "
              "pipefail, formats), et coherence avec le chantier reserve storm "
              "deja integre (famille_session, budget_hub, prechauffage). Pret "
              "pour l'integration ?",
              os.path.join(AUDIT_DIR, "ULTRA.md"))


if __name__ == "__main__":
    main()

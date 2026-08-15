#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audit_famille_6_hub.py — 13/08 : AUDIT FAMILLE COMPLETE (6 cerveaux)
du HUB EN TOUT ET POUR TOUT (hub_prise_ia.py, 540 lignes), découpé en 3
morceaux logiques pour un audit profond (objectif Christophe : zéro défaut,
niveau hedge fund suisse — on n'y revient plus).

Découpe (lignes de hub_prise_ia.py) :
  - MORCEAU 1 : lignes 1-160 — coeur réseau (_raw_call, load_config, usage, log)
  - MORCEAU 2 : lignes 161-380 — blacklist/backoff, gratuits dynamiques,
                 mode tempête, contexte vivant, routage + budget dans chat_completions
  - MORCEAU 3 : lignes 381-540 — fin chat_completions (filet de sécurité),
                 serveur HTTP (Handler), main

Famille (6 cerveaux) : GEMINI (audit.protocol), DEEPSEEK (mission),
JUGE (signets.juge), ULTRA (ultra.analyse), INFERX (inferx.analyse),
GROK (supervise.decision).

Réponses -> Index_Maison/AUDIT_HUB_6_2026-08-13/<MORCEAU>/<MEMBRE>.md
"""
import json
import os
import subprocess
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
AUDIT_DIR = "/Users/christophe/ace777-test-day1/Index_Maison/AUDIT_HUB_6_2026-08-13"
HUB_PATH = "/Users/christophe/prise-ia/hub_prise_ia.py"
ROUTING_PATH = "/Users/christophe/prise-ia/routing.json"
PROVIDERS_PATH = "/Users/christophe/prise-ia/providers.json"

# 3 morceaux : (nom, début ligne, fin ligne)
MORCEAUX = [
    ("M1_coeur_reseau", 1, 160,
     "coeur réseau : imports, blacklist/backoff, load_env, load_config, log_event, "
     "load_routing, usage_today, log_usage, _raw_call (appel direct provider, API "
     "native Ollama vs OpenAI)."),
    ("M2_routage_budget", 161, 380,
     "routage + budget + tempête : _gratuits_actifs, _mode_tempete_actif, "
     "_is_blacklisted, _backoff_duree, _register_result, call_provider (patience), "
     "contexte vivant, chat_completions (routage par complexité, budget calme "
     "atteint -> gratuits jamais coupés, réserve storm en tempête)."),
    ("M3_serveur_final", 381, 540,
     "fin chat_completions (filet de sécurité dernier recours), Handler HTTP "
     "(health, models, events, usage, routing, chat), main."),
]

MEMBRES = [
    ("GEMINI", "audit.protocol",
     "Tu es GEMINI, membre de la famille ACE777 (auditeur de protocole). Audite ce "
     "morceau du hub avec un oeil critique : robustesse, conformite au protocole, "
     "chemins absolus, non-fatalite, zero dependance, thread-safe."),
    ("DEEPSEEK", "mission",
     "Tu es DEEPSEEK, membre senior de la famille ACE777. Tu es critique, factuel, "
     "tu ne valides pas par complaisance : cherche les bugs reels (fuites, races, "
     "exceptions avalees, chemins relatifs, valeurs figees, cas limites)."),
    ("JUGE", "signets.juge",
     "Tu es le JUGE, verificateur independant ACE777. Tu valides ou invalides ce "
     "morceau. Exigeant sur : peut-il casser un run de production ? une valeur "
     "figee pourrait-elle faire couler en tempete ? Verdict clair : GO / GO AVEC "
     "RESERVES / NON."),
    ("ULTRA", "ultra.analyse",
     "Tu es ULTRA, membre expert de la famille ACE777 (analyse profonde). Analyse ce "
     "morceau en profondeur : coherence avec les autres morceaux, failles restantes, "
     "impact sur le flux existant (famille, budget, cockpit)."),
    ("INFERX", "inferx.analyse",
     "Tu es INFERX, membre de la famille ACE777. Audite ce morceau avec un oeil "
     "independant : signale TOUTE incoherence, meme mineure, tout cas limite non "
     "gere, toute hypothese fragile. Objectif : zero defaut."),
    ("GROK", "supervise.decision",
     "Tu es GROK, membre de la famille ACE777 (decision). Regarde ce morceau en "
     "superviseur operationnel : est-il sur pour un demon 24/7 ? risque de panne "
     "silencieuse ? risque de coupure inutile en tempete ? Verdict : GO / GO AVEC "
     "RESERVES / NON."),
]


def run(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, text=True, timeout=20).strip()
    except Exception:
        return ""


def contexte():
    c = {}
    with open(HUB_PATH, encoding="utf-8") as f:
        c["hub_complet"] = f.read()
    try:
        c["routing"] = open(ROUTING_PATH, encoding="utf-8").read()
        c["providers"] = open(PROVIDERS_PATH, encoding="utf-8").read()
    except Exception as e:
        c["routing"] = c["providers"] = "(illisible: %s)" % e
    c["health"] = run("curl -s --max-time 10 http://127.0.0.1:11435/health")
    c["events"] = run("curl -s --max-time 10 'http://127.0.0.1:11435/events' | head -c 600")
    c["py"] = run("cd %s && python3 -m py_compile hub_prise_ia.py && echo COMPILE_OK" % os.path.dirname(HUB_PATH))
    return c


def extraire(lignes, debut, fin):
    return "".join(lignes[debut - 1:fin])


BASE_PROMPT = """\
Systeme ACE777 - Mac 8 Go, hub 11435, providers gratuits. LOI 1quinquies : le codeur code, le superviseur SPECIFIE/INTEGRE/TESTE, la FAMILLE VALIDE. HUB = passerelle LLM unique (C9 : jamais de local).

CONTEXTE (13/08) : ce hub est le CERVEAU RESEAU d'ACE777. Aujourd'hui ont ete integres (valides famille en v1-v6) : blacklist backoff progressif (3 echecs -> pause x2), budget DYNAMIQUE quotidien (cloud_daily_budget calcule par budget_hub.py apres rotation, actuellement 624 + reserve storm 156), gratuits DYNAMIQUES (champ free dans providers.json — jamais de liste figee dans le code), mode tempete (ROUGE/alarme/vortex>=2 -> reserve storm, aucune coupure des taches prioritaires), contexte vivant injecte aux taches de decision, patience (retry x3 pour les providers lents), filet de securite dernier recours si tous blacklistes.

PRINCIPE FONDATEUR (Christophe) : « Valeur fixe -> on coule. » En tempete on s'arrange au mieux, les garde-fous protegent le calme sans jamais ralentir la tempete. Objectif : ZERO defaut, niveau hedge fund suisse — on ne doit plus y revenir.

CE QUI EST SOUMIS A TON AUDIT : le MORCEAU %%MORCEAU%% (lignes %%DEBUT%%-%%FIN%%) du hub (%%MORCEAU_DESC%%). Le code complet est fourni pour le contexte global, mais audite en priorite TON morceau.

REGLES D'AUDIT :
- Robustesse demon 24/7 : exceptions avalees silencieusement, fuites (fichiers, sockets, threads), chemins absolus (pas de cwd dependant), non-fatalite.
- Thread-safe : le hub est un ThreadingHTTPServer (requetes concurrentes) — toute variable globale partagee doit etre protegee (_blacklock).
- Zero valeur figee : rien ne doit etre cale en dur alors que la donnee vit dans providers.json / routing.json.
- Zero dependance : stdlib Python uniquement (pas de lib externe).
- Tempete : aucune coupure des taches prioritaires en tempete ; gratuits jamais coupes.
- Le morceau est-il coherent avec le reste du hub ? (le code complet est fourni).

Hub /health : %%HEALTH%%
Compilation : %%PY%%
Derniers events : %%EVENTS%%

--- routing.json (extrait) ---
%%ROUTING%%

--- providers.json (extrait) ---
%%PROVIDERS%%

--- MORCEAU AUDITE (lignes %%DEBUT%%-%%FIN%%) ---
%%MORCEAU_CODE%%

--- HUB COMPLET (contexte global) ---
%%HUB%%
"""


def soumettre(membre, task, sysprompt, outfile, morceau_nom, debut, fin, desc, ctx):
    lignes = ctx["hub_complet"].splitlines(keepends=True)
    code = extraire(lignes, debut, fin)
    mission = (BASE_PROMPT
               .replace("%%MORCEAU%%", morceau_nom)
               .replace("%%DEBUT%%", str(debut))
               .replace("%%FIN%%", str(fin))
               .replace("%%MORCEAU_DESC%%", desc)
               .replace("%%HEALTH%%", ctx["health"] or "PAS DE REPONSE")
               .replace("%%PY%%", ctx["py"] or "(inconnu)")
               .replace("%%EVENTS%%", ctx["events"] or "(vide)")
               .replace("%%ROUTING%%", ctx["routing"][:2500])
               .replace("%%PROVIDERS%%", ctx["providers"][:2500])
               .replace("%%MORCEAU_CODE%%", code)
               .replace("%%HUB%%", ctx["hub_complet"]))
    payload = {
        "task": task,
        "messages": [
            {"role": "system", "content": sysprompt},
            {"role": "user", "content": mission},
        ],
        "temperature": 0.2,
        "max_tokens": 3000,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    contenu = d["choices"][0]["message"]["content"]
    provider = d.get("provider", "?")
    os.makedirs(os.path.dirname(outfile), exist_ok=True)
    with open(outfile, "w", encoding="utf-8") as f:
        f.write("# AVIS %s (task %s, morceau %s)\n\nprovider: %s\n\n%s\n"
                % (membre, task, morceau_nom, provider, contenu))
    print("[OK] %s/%s -> %s (%d chars)" % (morceau_nom, membre, provider, len(contenu)))


def main():
    ctx = contexte()
    for morceau_nom, debut, fin, desc in MORCEAUX:
        for membre, task, sysp in MEMBRES:
            print("== %s/%s (%s) ==" % (morceau_nom, membre, task))
            outfile = os.path.join(AUDIT_DIR, morceau_nom, membre + ".md")
            soumettre(membre, task, sysp, outfile, morceau_nom, debut, fin, desc, ctx)
    print("AUDIT HUB 6 TERMINE")


if __name__ == "__main__":
    main()

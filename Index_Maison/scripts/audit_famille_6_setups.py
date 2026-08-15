#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audit_famille_6_setups.py — 13/08 : AUDIT FAMILLE COMPLETE (6 cerveaux)
des SETUPS du jour : verrou famille + budget dynamique + réserve storm + preflight.

Famille élargie (décision Christophe 13/08 : 6 cerveaux > 2) :
  - GEMINI  -> audit.protocol  (gemini)
  - DEEPSEEK-> mission         (nvidia / deepseek-v4-flash)
  - JUGE    -> signets.juge    (gemini -> openrouter-juge nemotron-120b)
  - ULTRA   -> ultra.analyse   (gemini -> openrouter-ultra nemotron-550b)
  - INFERX  -> inferx.analyse  (nvidia -> gemini)
  - GROK    -> supervise.decision (puter-grok)

Loi du brut : on soumet le RÉEL (les fichiers installés, pas des résumés).
Réponses -> Index_Maison/AUDIT_SETUPS_6_2026-08-13/<MEMBRE>.md
"""
import json
import os
import subprocess
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
AUDIT_DIR = "/Users/christophe/ace777-test-day1/Index_Maison/AUDIT_SETUPS_6_2026-08-13"
BASE = "/Users/christophe"

FILES = {
    "famille_session.py": BASE + "/ace777-test-day1/Index_Maison/scripts/famille_session.py",
    "budget_hub.py": BASE + "/prise-ia/budget_hub.py",
    "prechauffage_reserve.py": BASE + "/prise-ia/prechauffage_reserve.py",
    "bloc_hub_budget": BASE + "/ace777-test-day1/SPEC_verrou_famille_mode_tempete.md",
    "preflight": BASE + "/ace777-test-day1/scripts/preflight_ace777.sh",
    "routing.json": BASE + "/prise-ia/routing.json",
    "providers.json": BASE + "/prise-ia/providers.json",
}

MEMBRES = [
    ("GEMINI", "audit.protocol",
     "Tu es GEMINI, membre de la famille ACE777 (auditeur de protocole). Audite les "
     "setups du jour avec un oeil critique : le verrou tient-il pendant toute la "
     "consultation ? l'anti-spam est-il ecrit au debut ? le mode tempete protege-t-il "
     "sans ralentir ? le budget est-il dynamique et jamais coupant pour les gratuits ? "
     "le preflight verifie-t-il la reserve au decollage ?"),
    ("DEEPSEEK", "mission",
     "Tu es DEEPSEEK, membre senior de la famille ACE777. Tu es critique, factuel, "
     "tu ne valides pas par complaisance : verrou reel (flock) pendant toute la duree, "
     "anti-spam au debut meme en echec, mode tempete jamais bloque, budget quotidien "
     "dynamique, gratuits dynamiques depuis providers.json, reserve storm et preflight "
     "coherents. Python 3.9 stdlib, code integrable sans placeholder."),
    ("JUGE", "signets.juge",
     "Tu es le JUGE, verificateur independant ACE777. Tu valides ou invalides. "
     "Exigeant sur : la cause racine du 13/08 est-elle vraiment corrigee (un appel "
     "10s plus tard ne relance plus une consultation pendant que le trio tourne) ? "
     "le principe tempete est-il respecte ? le budget est-il dynamique (pas de valeur "
     "fixe) ? Verdict clair : GO / GO AVEC RESERVES / NON."),
    ("ULTRA", "ultra.analyse",
     "Tu es ULTRA, membre expert de la famille ACE777 (analyse profonde). Analyse en "
     "profondeur : coherence globale entre spec et code, failles restantes, integration "
     "sans casse du flux existant (ada_gardienne, hub, cockpit, preflight). Le tout "
     "est-il pret pour un niveau hedge fund suisse (zero defaut) ?"),
    ("INFERX", "inferx.analyse",
     "Tu es INFERX, membre de la famille ACE777. Audite ces setups avec un oeil "
     "independant et factuel : les garde-fous (verrou, TTL, cap horaire) protegent-ils "
     "le calme sans jamais ralentir la tempete ? le budget et la reserve storm sont-ils "
     "reellement dynamiques et sans valeur figee ? signale toute incoherence, meme "
     "mineure."),
    ("GROK", "supervise.decision",
     "Tu es GROK, membre de la famille ACE777 (decision). Regarde ces setups en "
     "superviseur operationnel : un run peut-il partir demain matin avec ces fichiers "
     "sans risque ? la reserve storm est-elle verifiee avant decollage (preflight) ? "
     "y a-t-il une seule valeur fixe qui pourrait faire couler en tempete ? "
     "Verdict : GO / GO AVEC RESERVES / NON."),
]


def run(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, text=True, timeout=20).strip()
    except Exception:
        return ""


def contenu_fichier(path, maxl=900):
    try:
        with open(path, encoding="utf-8") as f:
            lignes = f.readlines()
        if len(lignes) > maxl:
            return "".join(lignes[:maxl]) + "\n...[TRONQUE: %d lignes au total]...\n" % len(lignes)
        return "".join(lignes)
    except Exception as e:
        return "(illisible: %s)" % e


def contexte():
    c = {}
    for nom, path in FILES.items():
        c[nom] = contenu_fichier(path)
    c["hub"] = run("curl -s --max-time 10 http://127.0.0.1:11435/health")
    c["etat"] = run("cat %s/ace777-test-day1/Index_Maison/strategie/famille_derniere.json 2>/dev/null || echo '(absent)'" % BASE)
    c["preflight"] = run("cd %s/ace777-test-day1 && bash -n scripts/preflight_ace777.sh && echo SYNTAXE_OK" % BASE)
    return c


BASE_PROMPT = """\
Systeme ACE777 - Mac 8 Go, hub 11435, providers gratuits. LOI 1quinquies : le codeur code, le superviseur SPECIFIE/INTEGRE/TESTE, la FAMILLE VALIDE.

CONTEXTE (13/08) : le 13/08 une boucle famille incontrollee (cortana.urgent 10s -> cockpit_mission_feed -> ada_gardienne.scan() -> consulter_famille() -> trio hub) a consomme ~900 appels/h, explosant le budget (480) a 1310. Cause racine : anti-spam ecrit a la FIN de la consultation (thread detache). CORRIGE aujourd'hui par un chantier valide famille (v1->v6) : verrou flock tenu par le thread, TTL au debut, mode tempete (ROUGE/alarme/vortex>=2 -> 60s, bypass cap), budget DYNAMIQUE quotidien (recalcule par budget_hub.py apres rotation), GRATUITS DYNAMIQUES (champ free dans providers.json, jamais une liste figee dans le code), reserve storm 20%, prechauffage reserve, et check reserve dans le preflight (decollage).

PRINCIPE FONDATEUR (Christophe) : ACE777 est une machine de tempete. Les garde-fous protegent le calme, ils ne ralentissent JAMAIS la tempete. « Valeur fixe -> on coule » : ni budget fige, ni liste figee. En tempete on s'arrange au mieux (reserve + toutes les options).

CE QUI EST SOUMIS A TON AUDIT (le REEL installe, loi du brut) :
- famille_session.py : verrou + trio + mode tempete (installe dans Index_Maison/scripts/)
- budget_hub.py : budget dynamique quotidien + gratuits dynamiques + reserve storm
- prechauffage_reserve.py : verifie la reserve a l'avance (C1-C4)
- preflight_ace777.sh : check reserve au decollage (R1-R4, avant la section Ruby)
- routing.json / providers.json : valeurs actuelles (budget 624 + reserve 156, gratuits marques free)

REGLES D'AUDIT :
- Verrou : pose AU DEBUT, tenu par le thread PENDANT TOUTE la consultation (30-60s), jamais relache apres 0.1s.
- Anti-spam TTL : ecrit au debut, jamais supprime a la fin, conserve en cas d'echec.
- Mode tempete : declencheurs reels (zone ROUGE/PRENDS_LA_PERTE, alarme, vortex>=2) -> 60s + bypass cap. Jamais bloque par le cap horaire.
- Budget : recalcul quotidien dynamique, gratuits lus depuis providers.json (champ free), reserve storm, jamais de valeur fixe, jamais de local (C9).
- Preflight : R1 budget/reserve, R2 gratuits, R3 rapport recent, R4 executable. Non fatal (warn), ne casse pas les checks existants.
- Le code est-il INTEGRABLE et ROBUSTE pour un demon 24/7 (fuite de descripteurs, chemins absolus, erreurs non fatales) ?

Hub /health : %%HUB%%
Etat famille actuel : %%ETAT%%
Preflight syntaxe : %%PREFLIGHT%%

--- famille_session.py ---
%%famille_session.py%%

--- budget_hub.py ---
%%budget_hub.py%%

--- prechauffage_reserve.py ---
%%prechauffage_reserve.py%%

--- preflight_ace777.sh ---
%%preflight%%

--- routing.json ---
%%routing.json%%

--- providers.json ---
%%providers.json%%
"""


def soumettre(membre, task, sysprompt, outfile):
    ctx = contexte()
    mission = (BASE_PROMPT
               .replace("%%HUB%%", ctx["hub"] or "PAS DE REPONSE")
               .replace("%%ETAT%%", ctx["etat"] or "(vide)")
               .replace("%%PREFLIGHT%%", ctx["preflight"] or "(inconnu)")
               .replace("%%famille_session.py%%", ctx["famille_session.py"])
               .replace("%%budget_hub.py%%", ctx["budget_hub.py"])
               .replace("%%prechauffage_reserve.py%%", ctx["prechauffage_reserve.py"])
               .replace("%%preflight%%", ctx["preflight"])
               .replace("%%routing.json%%", ctx["routing.json"])
               .replace("%%providers.json%%", ctx["providers.json"]))
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
    os.makedirs(AUDIT_DIR, exist_ok=True)
    with open(outfile, "w", encoding="utf-8") as f:
        f.write("# AVIS %s (task %s)\n\nprovider: %s\n\n%s\n"
                % (membre, task, provider, contenu))
    print("[OK] %s -> %s (%d chars)" % (membre, provider, len(contenu)))


def main():
    for membre, task, sysp in MEMBRES:
        print("== %s (%s) ==" % (membre, task))
        soumettre(membre, task, sysp, os.path.join(AUDIT_DIR, membre + ".md"))


if __name__ == "__main__":
    main()

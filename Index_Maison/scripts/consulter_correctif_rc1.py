#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consulter FAMILLE (8) + JUGE : cause racine mort rc=1 prouvee + correctif.
Preuves machine + cinematiques completes. Rien n'est modifie avant validation."""
import json, os, sys, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSTAT_RC1_CORRECTIF_20260814")
os.makedirs(OUT, exist_ok=True)

BRIEF = """CONTEXTE (fait verifie par superviseur, 14/08/2026, run 4h testnet en cours) :

PROBLEME : le moteur ACE777 (bash genesis, set -euo pipefail) meurt en rc=1 SILENCIEUX
en plein cycle : zero FATAL_RC1, zero stderr, trap ERR jamais declenche. 4 morts
capturees aujourd'hui (12:06, 12:07, 12:14, 12:17 UTC) + 4 ce matin.

CAUSE RACINE PROUVEE (3 preuves) :
1) PREUVE MACHINE : la fonction swarm_neighbor_load() se termine par un SI dont la
   derniere commande peut retourner 1 :
     [ "$post_delta" -le "$post_grace_i" ] && swarm_shockwave_post_solo=1
   Quand la grace post-shockwave (20 cycles) est depassee, cette commande retourne 1
   -> la FONCTION retourne 1. Reproduit en harnais : cycle dans la grace = survit,
   cycle au-dela = meurt rc=1 SANS trap ERR (le genesis n'a pas set -E / errtrace,
   donc un echec DANS une fonction ne declenche pas le trap ERR du shell parent).
2) PREUVE CINETIQUE : crash dump 12:14 -> perte -8.60 -> "shockwave alpha->beta
   until_cycle=49" -> ALPHA meurt ~1 min apres, BETA meurt quand son cycle depasse
   until+grace(20). Timing cohérent.
3) PREUVE CONTRASTE : le run actuel tourne depuis 20+ min avec 0 shockwave -> 0 mort
   (les morts arrivent a 8-17 min quand des shockwaves sont broadcastées).

CHAINE DE LA MORT :
- perte/stop_loss -> swarm_broadcast_shockwave (ligne 2477) arme shockwave_until_cycle
- le voisin lit la telemetrie -> swarm_shockwave_until_cycle > 0
- quand cycle > until + grace -> le SI final retourne 1 -> swarm_neighbor_load retourne 1
- swarm_apply_coupling l'appelle SANS || (ligne 621) -> set -e tue rc=1
- pas de set -E -> trap ERR muet -> mort silencieuse

IMPORTANT : ce SI existe dans le VRAI champion scelle 37fca367 (md5 verifie) -> ce
n'est PAS un ajout exterieur, c'est un BUG LATENT : le champion gagnait -> pas de
pertes -> pas de shockwaves -> jamais declenche. Le testnet lent d'aujourd'hui
provoque des pertes -> le bug se reveille.

CORRECTIF PROPOSE (le plus propre) : ajouter "return 0" explicite a la fin de
swarm_neighbor_load() (la fonction fait du bookkeeping, elle ne doit JAMAIS etre
une source d'erreur). Alternative : "swarm_neighbor_load \"$cycle\" || true" a la
ligne 621. Option complementaire : set -E pour rendre les futures erreurs LOUD.

QUESTION : validez-vous le correctif "return 0" en fin de swarm_neighbor_load ?
Donnez : GO / GO AVEC RESERVES / NON + justification technique courte + meilleure
logique si vous en voyez une (contrainte : NE PAS casser le moteur rentable +126$)."""

MODELS = ["gemini", "deepseek", "juge", "ultra", "inferx", "grok", "nvidia", "oss20"]

def ask(model):
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": BRIEF}],
        "max_tokens": 1400, "temperature": 0.2,
    }).encode()
    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    return d["choices"][0]["message"]["content"], d.get("provider", "?")

results = []
for m in MODELS:
    try:
        t0 = time.time()
        content, provider = ask(m)
        dur = round(time.time() - t0, 1)
        results.append({"model": m, "provider": provider, "dur": dur, "content": content})
        verdict = "GO" if "GO" in content[:200] else "?"
        print(f"[{m}] ({provider}, {dur}s) -> {len(content)} chars | debut: {content[:90].strip()!r}")
    except Exception as e:
        results.append({"model": m, "provider": "ERR", "dur": 0, "content": f"ERROR: {e}"})
        print(f"[{m}] ERROR: {e}")

with open(os.path.join(OUT, "CONSULTATION_RC1_CORRECTIF.json"), "w") as f:
    json.dump({"brief": BRIEF, "results": results}, f, ensure_ascii=False, indent=2)
md = [f"# CONSULTATION RC=1 CORRECTIF — {len(results)} reponses\n",
      f"\n## Question\n{BRIEF}\n"]
for r in results:
    md.append(f"\n## [{r['model']}] ({r['provider']}, {r['dur']}s)\n{r['content']}\n")
open(os.path.join(OUT, "CONSULTATION_RC1_CORRECTIF.md"), "w").write("\n".join(md))
print(f"\nDossier: {OUT}")

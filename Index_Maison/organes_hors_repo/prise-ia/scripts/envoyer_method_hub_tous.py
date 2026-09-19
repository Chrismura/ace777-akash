#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Envoie METHODE_HUB_POINT_FINAL au CODEUR (code.ia) + FAMILLE/JUGE (signets.juge).
Prompts spécialisés par rôle. Écrit les réponses dans REPONSE_*_HUB_2026-08-16.md"""
import json, os, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

HUB = "http://127.0.0.1:11435/v1/chat/completions"
METHODE = open(os.path.expanduser(
    "~/ace777-test-day1/Index_Maison/METHODE_HUB_POINT_FINAL_2026-08-16.md")).read()

# État de l'implémentation (pour que codeur/juge vérifient sur du concret)
ETAT = """=== ÉTAT DE L'IMPLÉMENTATION (fait aujourd'hui 16/08, par Buffy en codeur externe) ===
Fichier modifié : ~/prise-ia/hub_prise_ia.py (backup : hub_prise_ia.py.bak-failover-20260816)
R1 Filet universel : après la chaîne de la tâche, si tout a échoué -> essayer TOUS les providers actifs
   (triés par order), chacun avec une part du budget. Testé : chaîne 100% morte -> réponse via Gemini. OK.
R2 429 = bascule immédiate : 429 ajouté aux erreurs non-retryable, pas de retry, pause 60s (ou Retry-After). OK.
R3 Budget PAR provider : 180s ÷ nb providers restants (plancher 15s), retry borné par cette part. OK.
R4 Anti-tempête par tâche : 3 échecs en 10 min -> pause 5 min de la tâche. OK.
Validation : python3 -m py_compile OK. Hub redémarré sous launchd, répond HTTP 200.
Ne PAS toucher à providers.json ni routing.json (les chaînes restent la préférence)."""

def appeler(task, system, prompt, out_path):
    payload = json.dumps({
        "model": task,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        "max_tokens": 6000, "temperature": 0.2,
    }).encode()
    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"}, method="POST")
    print(f"[{task}] envoi...", flush=True)
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=420) as resp:
        d = json.loads(resp.read().decode())
    content = d["choices"][0]["message"]["content"]
    dur = round(time.time() - t0, 1)
    prov = d.get("provider", "?")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"# Réponse {task} — méthode hub (provider {prov}, {dur}s)\n\n{content}\n")
    print(f"[OK] {task} répondu via {prov} ({dur}s) -> {out_path}", flush=True)
    return out_path

# ---- PROMPT CODEUR ----
PROMPT_CODEUR = f"""Tu es le CODEUR ACE777. La méthode de refonte du failover hub ci-dessous a été appliquée
par un codeur externe (Buffy). Ton rôle : VERIFIER que l'implémentation est saine et COMPLETER si besoin.

{METHODE}

{ETAT}

=== TA MISSION ===
1. Lis la méthode et l'état d'implémentation. Vérifie la cohérence : les 4 règles couvrent-elles bien les
   3 trous décrits ? Y a-t-il une faille ou un cas non couvert (ex. provider qui répond mais renvoie du
   vide, timeouts globaux, filet qui s'auto-bloque, budget déjà consommé) ?
2. Réponds en 3 sections :
   a) VERDICT : méthode saine / à corriger (1 phrase).
   b) FAIBLESSES : les points faibles réels que tu vois (max 5, chacun 2-3 lignes, priorisés).
   c) CORRECTIFS PROPOSÉS : le code exact (bloc ```python) des correctifs prioritaires, prêt à appliquer.
3. RÈGLES : stdlib uniquement, ne pas toucher providers.json ni routing.json, ne rien casser de la
   tuyauterie existante (blacklist, budget 624/j, PATIENCE). Réponds en français, factuel, concis."""

# ---- PROMPT FAMILLE / JUGE ----
PROMPT_FAMILLE = f"""Tu es la FAMILLE/JUGE ACE777 (maker != checker : le codeur a fait, toi tu juges).
Une méthode de refonte du hub LLM t'est soumise pour VALIDATION. Elle a déjà été implémentée par un
codeur externe et testée en réel (chaîne morte -> réponse via filet universel).

{METHODE}

{ETAT}

=== TA MISSION ===
1. Évalue la méthode en tant que garde-fou d'exploitation : est-elle proportionnée ? Crée-t-elle un
   risque (coût, latence, providers gratuits surchargés, dépendance accrue au cloud) ?
2. Réponds en 3 sections :
   a) VERDICT : VALIDÉ / VALIDÉ AVEC RÉSERVES / REJETÉ (1 phrase).
   b) RÉSERVES : les points qui te chiffonnent (max 4, chacun 2-3 lignes).
   c) CONDITIONS : les conditions à poser avant GO (si réserves), sinon "aucune".
3. Réponds en français, factuel, concis."""

os.makedirs(os.path.expanduser("~/ace777-test-day1/Index_Maison"), exist_ok=True)
BASE = os.path.expanduser("~/ace777-test-day1/Index_Maison")
jobs = [
    ("code.ia", "Tu es le codeur senior du projet ACE777. Code propre, stdlib, robuste, vérification rigoureuse.",
     PROMPT_CODEUR, os.path.join(BASE, "REPONSE_CODEUR_HUB_2026-08-16.md")),
    ("signets.juge", "Tu es le juge/famille ACE777. Tu valides ou rejettes les méthodes, tu ne codes pas.",
     PROMPT_FAMILLE, os.path.join(BASE, "REPONSE_FAMILLE_HUB_2026-08-16.md")),
]

with ThreadPoolExecutor(max_workers=2) as ex:
    futs = [ex.submit(appeler, *j) for j in jobs]
    for f in futs:
        f.result()  # propage les erreurs

print("=== Terminé. Réponses écrites. ===", flush=True)

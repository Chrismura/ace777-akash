#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validation finale : renvoie au CODEUR + FAMILLE les 2 correctifs appliqués
(suite à leurs réserves), avec le diff réel, pour verdict final."""
import json, os, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

HUB = "http://127.0.0.1:11435/v1/chat/completions"

DIFF = """=== CORRECTIFS APPLIQUÉS (suite à vos réserves du 16/08) — hub_prise_ia.py ===

CORRECTIF 1 (famille, condition 1 — budget cloud = coupe-circuit absolu pour le filet) :
Après construction de la liste providers (chaîne + filet), si budget cloud atteint
(usage.cloud >= cloud_daily_budget) et pas de tempête :
    chaine  = providers de la chaîne (déjà réduits aux gratuits par la logique existante)
    filet   = providers hors-chaîne ET gratuits uniquement
    providers = chaine + filet
-> le filet ne peut PLUS re-injecter un provider payant en dessous de la chaîne.
Log : "Budget atteint -> filet restreint aux gratuits".

CORRECTIF 2 (famille, condition 2 — traçabilité) :
Quand un provider HORS chaîne répond (filet universel), on logue un évènement
distinct : kind="filet-universel", titre "[FILET UNIVERSEL] « provider » a répondu
hors chaîne" -> repérer immédiatement une tâche qui recourt trop souvent au filet
(signe d'une chaîne routing.json obsolète).

=== VÉRIFICATIONS FAITES (par le codeur externe) ===
- Réponse vide : déjà géré (raise "Reponse vide" dans _raw_call + retry x3).
- Blacklist : la boucle saute déjà les providers blacklistés, y compris dans le filet.
- py_compile OK. Hub redémarré, répond HTTP 200.
- Les 3 correctifs du codeur (validate_llm_response, get_fallback_chain_extended)
  étaient redondants avec le code existant -> non appliqués, documenté ici.
"""

PROMPT_COMMUN = f"""Suite à vos verdicts du 16/08, les correctifs ont été appliqués. Voici le diff réel :

{DIFF}

Confirme en 3 lignes max : 1) votre verdict final sur CES correctifs, 2) un point
faible restant éventuel, 3) GO / PAS GO. Réponds en français, factuel."""

def appeler(task, system, prompt, out_path):
    payload = json.dumps({
        "model": task,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        "max_tokens": 1500, "temperature": 0.2,
    }).encode()
    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"}, method="POST")
    print(f"[{task}] envoi...", flush=True)
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=300) as resp:
        d = json.loads(resp.read().decode())
    content = d["choices"][0]["message"]["content"]
    dur = round(time.time() - t0, 1)
    prov = d.get("provider", "?")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"# Validation finale {task} — hub (provider {prov}, {dur}s)\n\n{content}\n")
    print(f"[OK] {task} -> {out_path} ({prov}, {dur}s)", flush=True)

BASE = os.path.expanduser("~/ace777-test-day1/Index_Maison")
jobs = [
    ("code.ia", "Tu es le codeur senior ACE777. Verdict final technique, concis.",
     PROMPT_COMMUN, os.path.join(BASE, "VALIDATION_FINALE_CODEUR_HUB_2026-08-16.md")),
    ("signets.juge", "Tu es la famille/juge ACE777 (maker != checker). Verdict final, concis.",
     PROMPT_COMMUN, os.path.join(BASE, "VALIDATION_FINALE_FAMILLE_HUB_2026-08-16.md")),
]
with ThreadPoolExecutor(max_workers=2) as ex:
    for f in [ex.submit(appeler, *j) for j in jobs]:
        f.result()
print("=== Terminé ===", flush=True)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Envoie les 2 specs vigie (mempool pépite + correctif superviseur) au CODEUR via le hub.
Réponses écrites dans REPONSE_CODEUR_SPEC_*_2026-08-16.md"""
import json, os, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

HUB = "http://127.0.0.1:11435/v1/chat/completions"
BASE = os.path.expanduser("~/ace777-test-day1/Index_Maison")

REGLE = """=== RÈGLES DE CODE ACE777 ===
- Python 3.9+, stdlib uniquement (pas de dépendances externes).
- Encodage UTF-8, docstring de rôle en tête de chaque fichier.
- Écriture ATOMIQUE (mkstemp + os.replace) pour tout fichier JSON.
- Kill-switch : vérifier Index_Maison/strategie/STOP et ~/ace777-test-day1/Index_Maison/STOP_ALL
  avant toute écriture.
- Robustesse : aucun crash si fichier manquant/corrompu (repli propre).
- Idempotence : relançable sans doublons.
- NE PAS toucher au moteur Hulk (paper_diprip.py) NI à surveiller_whales.py (scan actuel INCHANGÉ).
- Réponds en français, factuel. Pour chaque fichier : bloc ```python complet précédé du chemin.
- Pour les MODIFS : bloc ```diff EXACT (avant → après). Une section NOTES finale."""

def appeler(spec_path, out_name, mission):
    spec = open(os.path.join(BASE, spec_path), encoding="utf-8").read()
    prompt = f"""Tu es le CODEUR ACE777. Une SPEC validée t'est confiée.
{mission}

{spec}

{REGLE}"""
    payload = json.dumps({
        "model": "code.ia",
        "messages": [
            {"role": "system", "content": "Tu es le codeur senior du projet ACE777. Code propre, stdlib, robuste."},
            {"role": "user", "content": prompt},
        ],
        "max_tokens": 8000, "temperature": 0.2,
    }).encode()
    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"}, method="POST")
    print(f"[{spec_path}] envoi...", flush=True)
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=420) as resp:
        d = json.loads(resp.read().decode())
    content = d["choices"][0]["message"]["content"]
    dur = round(time.time() - t0, 1)
    prov = d.get("provider", "?")
    out = os.path.join(BASE, out_name)
    with open(out, "w", encoding="utf-8") as f:
        f.write(f"# Réponse codeur — {spec_path} (provider {prov}, {dur}s)\n\n{content}\n")
    print(f"[OK] {out_name} ({prov}, {dur}s)", flush=True)

jobs = [
    ("SPEC_VIGIE_MEMPOOL_2026-08-16.md", "REPONSE_CODEUR_SPEC_VIGIE_MEMPOOL_2026-08-16.md",
     "Mission : produis le code demandé pour la vigie mempool (détecteur bloc privatisé / tx fantômes) "
     "avec le correctif anti-faux-positifs (carnet de txids vus sur plusieurs minutes)."),
    ("SPEC_CORRECTIF_VIGIE_SUPERVISEUR_2026-08-16.md", "REPONSE_CODEUR_SPEC_SUPERVISEUR_2026-08-16.md",
     "Mission : applique les 3 correctifs demandés (timeout WebSocket vigie_live.py, pkill avant relance "
     "dans superviseur.sh, cooldown analyste persistant) en donnant les diffs EXACTS avant/après."),
]
with ThreadPoolExecutor(max_workers=2) as ex:
    for f in [ex.submit(appeler, *j) for j in jobs]:
        f.result()
print("=== Terminé ===", flush=True)

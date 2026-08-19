#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Envoie la SPEC VIGIE MEMPOOL (pépite de Christophe) au CODEUR via le hub."""
import json, os, time, urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
SPEC = open(os.path.expanduser(
    "~/ace777-test-day1/Index_Maison/SPEC_VIGIE_MEMPOOL_2026-08-16.md")).read()

PROMPT = f"""Tu es le CODEUR ACE777. Une SPEC approuvée famille + supervision t'est confiée.
Lis-la ATTENTIVEMENT puis produis le code demandé.

=== RÈGLES DE CODE ACE777 ===
- Python 3.9+, stdlib uniquement (pas de dépendances externes).
- Encodage UTF-8, docstring de rôle en tête de chaque fichier.
- Écriture ATOMIQUE (mkstemp + os.replace) pour tout fichier JSON.
- Kill-switch : vérifier Index_Maison/strategie/STOP et ~/ace777-test-day1/Index_Maison/STOP_ALL
  avant toute écriture.
- Robustesse : aucun crash si fichier manquant/corrompu (repli propre).
- Idempotence : relançable sans doublons.
- NE PAS toucher à detecter_cpfp.py, surveiller_whales.py, pont_onchain.py, ni au moteur Hulk.

=== SPEC À IMPLÉMENTER ===
{SPEC}

=== FORMAT DE RÉPONSE EXIGÉ ===
- Un bloc ```python complet et fermé, précédé du chemin du fichier.
- Une seule section « NOTES » finale : choix faits, points d'attention, fenêtre d'historique
  retenue, comportement du pré-filtre API.
- Réponds en français, factuel."""

payload = json.dumps({
    "model": "gemini",
    "messages": [
        {"role": "system", "content": "Tu es le codeur senior du projet ACE777. Code propre, stdlib, robuste."},
        {"role": "user", "content": PROMPT},
    ],
    "max_tokens": 8000, "temperature": 0.2,
}).encode()

req = urllib.request.Request(HUB, data=payload,
                             headers={"Content-Type": "application/json"}, method="POST")
print("Envoi de la spec VIGIE MEMPOOL au codeur...", flush=True)
t0 = time.time()
try:
    with urllib.request.urlopen(req, timeout=600) as resp:
        d = json.loads(resp.read().decode())
except Exception as e:
    print(f"[ERREUR] appel hub échoué : {e}")
    raise SystemExit(1)

content = d["choices"][0]["message"]["content"]
dur = round(time.time() - t0, 1)
out = os.path.expanduser("~/ace777-test-day1/Index_Maison/REPONSE_CODEUR_VIGIE_MEMPOOL_2026-08-16.md")
with open(out, "w", encoding="utf-8") as f:
    f.write(f"# Réponse codeur — chantier VIGIE MEMPOOL (provider {d.get('provider','?')}, {dur}s)\n\n{content}\n")
print(f"[OK] Réponse écrite ({dur}s) : {out}")

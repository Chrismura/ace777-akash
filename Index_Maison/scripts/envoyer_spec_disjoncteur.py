#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Envoie la SPEC DISJONCTEUR (urgence famille) au CODEUR via le hub."""
import json, os, time, urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
SPEC = open(os.path.expanduser(
    "~/ace777-test-day1/Index_Maison/SPEC_DISJONCTEUR_2026-08-16.md")).read()

PROMPT = f"""Tu es le CODEUR ACE777. Une SPEC validée FAMILLE + supervision (verdict : « VALIDÉ ET RATIFIÉ SANS RÉSERVE. Application immédiate ») t'est confiée. C'est l'URGENCE 1 de la maison : le Disjoncteur Unique.

{SPEC}

Produis le code demandé : disjoncteur.py complet + diffs exacts d'intégration + notes. Réponds en français, factuel."""

payload = json.dumps({
    "model": "code.ia",
    "messages": [
        {"role": "system", "content": "Tu es le codeur senior du projet ACE777. Code propre, stdlib, robuste, déterministe."},
        {"role": "user", "content": PROMPT},
    ],
    "max_tokens": 8000, "temperature": 0.2,
}).encode()

req = urllib.request.Request(HUB, data=payload,
                             headers={"Content-Type": "application/json"}, method="POST")
print("Envoi de la spec DISJONCTEUR au codeur...", flush=True)
t0 = time.time()
with urllib.request.urlopen(req, timeout=420) as resp:
    d = json.loads(resp.read().decode())
content = d["choices"][0]["message"]["content"]
dur = round(time.time() - t0, 1)
prov = d.get("provider", "?")
out = os.path.expanduser("~/ace777-test-day1/Index_Maison/REPONSE_CODEUR_DISJONCTEUR_2026-08-16.md")
with open(out, "w", encoding="utf-8") as f:
    f.write(f"# Réponse codeur — Disjoncteur (provider {prov}, {dur}s)\n\n{content}\n")
print(f"[OK] {out} ({prov}, {dur}s)")

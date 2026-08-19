#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Envoie la spec tier/rip HULK + le diff au codeur (task=code.ia) — mode VALIDATION."""
import json, os, sys, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
SPEC = os.path.join(ROOT, "..", "..", "hulk-mexc", "docs", "SPEC_FIX_TIER_RIP_2026-08-16.md")
DIFF = os.path.join(ROOT, "diff_tier_rip_20260816.patch")
OUT = os.path.join(ROOT, "..", "REPONSE_CODEUR_FIX_TIER_RIP_2026-08-16.md")
HUB = "http://127.0.0.1:11435/v1/chat/completions"

spec = open(SPEC, encoding="utf-8").read()
diff = open(DIFF, encoding="utf-8").read()

prompt = f"""{spec}

=== DIFF RÉEL À VALIDER (produit par Buffy, intégrateur) ===
{diff}

MISSION (mode VALIDATION, loi 1quinquies) :
Validez ce diff par rapport à la spec : repérez toute erreur de syntaxe, d'indentation,
de logique ou tout écart avec la spec (4 blocs + configs). Ne réécrivez pas le code,
ne proposez pas d'améliorations hors spec. Répondez :
- VERDICT : VALIDE | VALIDE-AVEC-RÉSERVES | INVALIDE
- Points vérifiés (liste)
- Réserves / corrections nécessaires (liste, précises)
- CONFIANCE : 0-100%
Factuel, concis, français."""

payload = json.dumps({
    "task": "code.ia",
    "messages": [
        {"role": "system", "content": "Tu es le codeur de confiance d'ACE777. Tu VALIDES le diff fourni (repérer toute erreur de syntaxe, d'indentation ou de logique), sans réécrire ni inventer."},
        {"role": "user", "content": prompt},
    ],
    "max_tokens": 3000,
    "temperature": 0.1,
}).encode()

req = urllib.request.Request(HUB, data=payload,
                             headers={"Content-Type": "application/json"}, method="POST")
t0 = time.time()
try:
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    content = d["choices"][0]["message"]["content"]
    provider = d.get("provider", "?")
    secs = round(time.time() - t0, 1)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(f"# Réponse codeur (provider {provider}, {secs}s)\n\n{content}\n")
    print(f"[OK] provider={provider} ({secs}s)")
    print(f"Réponse : {OUT}")
except Exception as e:
    print(f"[ERR] {e}")
    sys.exit(1)

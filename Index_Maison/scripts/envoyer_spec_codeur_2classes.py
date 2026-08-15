#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Envoie la spec 2 classes de paires au codeur (task=code.ia)."""
import json, os, sys, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
SPEC = os.path.join(ROOT, "..", "SPEC_2CLASSES_HULK_2026-08-15.md")
OUT = os.path.join(ROOT, "..", "REPONSE_CODEUR_2CLASSES_HULK_2026-08-15.md")
HUB = "http://127.0.0.1:11435/v1/chat/completions"

spec = open(SPEC, encoding="utf-8").read()

payload = json.dumps({
    "task": "code.ia",
    "messages": [
        {"role": "system", "content": "Tu es le codeur de confiance d'ACE777. Tu VALIDES le diff fourni (erreur de syntaxe, d'indentation, de logique ou de casse), sans réécrire ni inventer."},
        {"role": "user", "content": spec},
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
except Exception as e:
    print(f"[ERR] {e}")
    sys.exit(1)

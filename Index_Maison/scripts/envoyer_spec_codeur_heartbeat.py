#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Envoie la spec fix-heartbeat au codeur (task=code.ia) et sauvegarde sa réponse."""
import json, os, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
SPEC = os.path.join(ROOT, "..", "SPEC_FIX_HEARTBEAT_CODER_2026-08-15.md")
OUT = os.path.join(ROOT, "..", "REPONSE_CODEUR_FIX_HEARTBEAT_2026-08-15.md")
HUB = "http://127.0.0.1:11435/v1/chat/completions"

spec = open(SPEC, encoding="utf-8").read()

payload = json.dumps({
    "task": "code.ia",
    "messages": [
        {"role": "system", "content": "Tu es le codeur de confiance d'ACE777. Tu produis des diffs exacts, sans paraphrase, sans inventer. Tu ne modifies jamais autre chose que ce qui est demandé. Si une info manque, tu réponds « information insuffisante »."},
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
    print(f"Réponse : {OUT}")
except Exception as e:
    print(f"[ERR] {e}")
    raise SystemExit(1)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Complément consultation famille — récupère les avis manquants.

Les 4 premiers avis (grok/deepseek/juge/ultra) ont fait 502 car ces noms ne
correspondaient à aucun provider ACTIF de providers.json :
  juge    -> openrouter-juge  (nemotron-3-super-120b free)   [OK testé]
  ultra   -> openrouter-ultra (nemotron-3-ultra-550b free)   [OK testé]
  deepseek-> nvidia (déjà couvert : deepseek-v4-flash via nvidia)
  grok    -> puter-grok (HTTP 402 Payment Required, indisponible)

Réutilise le même BRIEF que consulter_famille_moteur_identique.py (import sans
exécuter main)."""
import importlib.util
import json
import os
import time
import urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_MOTEUR_IDENTIQUE_20260815")

# Charger BRIEF depuis le script principal sans exécuter son main()
_spec = importlib.util.spec_from_file_location(
    "cf_main", os.path.join(ROOT, "consulter_famille_moteur_identique.py"))
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
BRIEF = _mod.BRIEF

MODELS = ["openrouter-juge", "openrouter-ultra"]


def ask(model):
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": BRIEF}],
        "max_tokens": 2200,
        "temperature": 0.2,
    }).encode()
    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"},
                                 method="POST")
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    return d["choices"][0]["message"]["content"], d.get("provider", "?"), round(time.time() - t0, 1)


def main():
    for m in MODELS:
        try:
            content, provider, secs = ask(m)
            f = os.path.join(OUT, f"AVIS_{m}.md")
            with open(f, "w", encoding="utf-8") as fh:
                fh.write(f"# AVIS {m} (provider {provider}, {secs}s)\n\n{content}\n")
            print(f"[OK] {m} -> {f} ({secs}s)")
        except Exception as e:
            print(f"[ERR] {m}: {e}")
        time.sleep(2)


if __name__ == "__main__":
    main()

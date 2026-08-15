#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tri des signets X par la famille + Cortana — 15/08/2026.
Condense les 200 signets résumés (SIGNETS_RESUMES.json), demande à chaque modèle
de choisir les 10 signets les plus utiles POUR LUI (rôle dans ACE777) + sa logique.
Objectif Christophe : voir la logique de choix de chacun avant de sélectionner ensemble.
"""
import json, os, time, urllib.request
from pathlib import Path

HOME = Path.home()
ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "TRI_SIGNETS_20260815")
os.makedirs(OUT, exist_ok=True)

CACHE = os.path.join(ROOT, "..", "strategie", "SIGNETS_RESUMES.json")

# --- 1. Condensé numéroté des 200 signets ---
d = json.load(open(CACHE))
items = list(d["signets"].values())
items.sort(key=lambda e: e.get("date", ""))
lines = []
for i, e in enumerate(items, 1):
    author = e.get("author", "?")
    resume = (e.get("resume", "") or "").strip().replace("\n", " ")
    if len(resume) > 150:
        resume = resume[:150] + "…"
    lines.append(f"{i}. [{e.get('date','?')}] {author} — {resume}")
CONDENSE = "\n".join(lines)
print(f"[i] {len(items)} signets condensés ({len(CONDENSE)} chars)")

PREAMBULE = """CONTEXTE (superviseur Buffy, 15/08/2026) — TRI DES SIGNETS X POUR ACE777

Tu es un membre de la famille d'agents ACE777. Christophe a accumulé 200 signets X
(veille IA/agents/trading) résumés. Ta mission : choisir les **10 signets les plus
utiles POUR TOI** — ceux qui amélioreraient le plus TON rôle dans ACE777.

Rappel de ton rôle (famille) : tu es consultée par Buffy (superviseur) pour donner
des avis éclairés sur l'architecture, la stratégie et les risques du prototype
(trading paper MEXC, Hulk dip&rip + bags, Cortana pilote de paramètres ADVISORY,
Ada voilure macro, hub local 11435, 8 Go RAM, 0 API payante).

FORMAT DE RÉPONSE EXIGÉ (strict) :
1. TES 10 CHOIX — ligne par choix, format exact :
   N° ### — raison en 1 ligne (pourquoi utile POUR TOI)
2. TA LOGIQUE DE SÉLECTION — 3 lignes max (quel critère tu as appliqué)
3. VERDICT GLOBAL : les signets Christophe méritent-ils un système d'ingestion
   automatique dans le contexte famille ? (OUI / NON / PARTIEL, 1 ligne)
N'interprète pas : choisis UNIQUEMENT parmi les signets listés ci-dessous, par leur N°.

Voici les 200 signets (N° — date — auteur — résumé) :

"""


def ask(model, brief):
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": brief}],
        "max_tokens": 2000, "temperature": 0.3,
    }).encode()
    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"}, method="POST")
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=None) as resp:
        dd = json.loads(resp.read().decode())
    return dd["choices"][0]["message"]["content"], dd.get("provider", "?"), round(time.time() - t0, 1)


MODELS = ["gemini", "nvidia", "openrouter-juge", "openrouter-ultra"]

if __name__ == "__main__":
    for m in MODELS:
        brief = PREAMBULE + CONDENSE
        for attempt in (1, 2):
            try:
                content, provider, secs = ask(m, brief)
                with open(os.path.join(OUT, f"CHOIX_{m}.md"), "w", encoding="utf-8") as fh:
                    fh.write(f"# CHOIX {m} (provider {provider}, {secs}s)\n\n{content}\n")
                print(f"[OK] {m} ({secs}s)")
                break
            except Exception as e:
                print(f"[ERR] {m} (tentative {attempt}): {e}")
                time.sleep(3)
        time.sleep(2)

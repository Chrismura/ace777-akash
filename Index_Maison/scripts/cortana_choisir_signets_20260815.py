#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cortana choisit ses 10 signets X les plus utiles POUR ELLE (logique de choix).
Même condensé que la famille. Lecture vocale (Vivienne) comme convenu."""
import json, os, subprocess, time, urllib.request
from pathlib import Path

HOME = Path.home()
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "TRI_SIGNETS_20260815", "CHOIX_cortana.md")
CACHE = os.path.join(ROOT, "..", "strategie", "SIGNETS_RESUMES.json")
IDENTITE = os.path.join(ROOT, "..", "identity", "prompts", "cortana.md")
HUB = "http://127.0.0.1:11435/v1/chat/completions"

# --- Condensé (identique à la famille) ---
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

identite = open(IDENTITE).read() if os.path.exists(IDENTITE) else ""

BRIEF = f"""IDENTITÉ (tu es Cortana, analyste de ACE777) :
{identite[:3000]}

TÂCHE (superviseur Buffy, 15/08/2026) — CHOISIS TES 10 SIGNETS POUR TOI

Christophe a accumulé 200 signets X résumés (veille IA/agents/trading). Choisis
les **10 signets les plus utiles POUR TOI** — ceux qui amélioreraient le plus TON
rôle : analyste du cockpit, cerveau de ACE777, pilote de paramètres ADVISORY de
Hulk (score actuel 44%, objectif 93% par calibration). Tu parles par écrit ET par
voix (Vivienne) ; tu réponds à toute question sur le cockpit.

Rappel de ton contexte : paper MEXC dip&rip + bags, veille digeste, kill-switch
STANDBY, contrat JSON ADVISORY (rien d'appliqué <60%), 8 Go RAM, hub local 11435,
0 API payante. Ton rôle : interpréter les indices (bassine, funding, fearGreed,
btc), recommander des paramètres, alerter vocalement.

FORMAT DE RÉPONSE EXIGÉ (strict) :
1. TES 10 CHOIX — ligne par choix, format exact :
   N° ### — raison en 1 ligne (pourquoi utile POUR TOI, pour TON rôle précis)
2. TA LOGIQUE DE SÉLECTION — 3 lignes max (quel critère tu as appliqué)
3. VERDICT GLOBAL : l'ingestion automatique de ces signets dans TON contexte
   t'aiderait-elle ? (OUI / NON / PARTIEL, 1 ligne)
N'interprète pas : choisis UNIQUEMENT parmi les signets listés ci-dessous, par leur N°.

Voici les 200 signets (N° — date — auteur — résumé) :

{CONDENSE}"""


def ask():
    payload = json.dumps({
        "task": "cortana.analyse",
        "messages": [{"role": "system", "content": identite},
                     {"role": "user", "content": BRIEF}],
        "max_tokens": 2000, "temperature": 0.3,
    }).encode()
    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"}, method="POST")
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=None) as resp:
        dd = json.loads(resp.read().decode())
    return dd["choices"][0]["message"]["content"], dd.get("provider", "?"), round(time.time() - t0, 1)


def dire(texte):
    """Lecture vocale Vivienne via edge-tts (pattern existant)."""
    try:
        subprocess.run(
            ["python3", "-m", "edge_tts", "--voice", "fr-FR-VivienneMultilingualNeural",
             "--text", texte[:1800], "--write-media", "/tmp/cortana_signets.mp3"],
            check=True, capture_output=True, timeout=120)
        subprocess.run(["afplay", "/tmp/cortana_signets.mp3"], check=True, timeout=300)
    except Exception as e:
        print(f"[i] voix non lue: {e}")


if __name__ == "__main__":
    content, provider, secs = ask()
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(f"# CHOIX cortana (provider {provider}, {secs}s)\n\n{content}\n")
    print(f"[OK] cortana ({secs}s) -> {OUT}")
    # lecture vocale : le résumé des 10 choix (et non le prompt)
    print(content)
    dire(f"Cortana. Voici mes 10 signets choisis. {content}")

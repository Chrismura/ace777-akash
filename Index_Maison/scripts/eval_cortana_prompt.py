#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""eval_cortana_prompt.py — MINI-HARNAIS d'assertions sur le prompt Cortana
(remplaçant léger de promptfoo, voir SNIFF_GITHUB_OBSIDIAN_20260905.md).

Pourquoi pas promptfoo : l'installation npm a téléchargé 1,7 Go sans finir sur
la ligne de l'alpage (21:25-21:42, 17 min) — dette réelle, essence chère.
Cet équivalent fait le MÊME contrat : envoyer le prompt canon à un LLM local
(Ollama = zéro budget hub), vérifier les SORTIES OBLIGATOIRES par assertions.

Contrat vérifié (cortana.md, "Tes sorties"):
  1. AVIS STRICT : LONG | SHORT | NEUTRE  (3 lignes exactes)
  2. HORIZON : 24h | 48h | 1 semaine
  3. CONFIANCE : haute | moyenne | faible
  4. Aucun verbe d'ordre (achète/vends/achètez/vendez/ordre)
  5. Règle score_justesse < 60% -> CONFIANCE faible obligatoire

Usage :
  python3 eval_cortana_prompt.py              # Ollama local (qwen2.5-coder:1.5b, léger)
  python3 eval_cortana_prompt.py --model qwen3.5:4b
  python3 eval_cortana_prompt.py --hub        # via le hub (budget cloud)
Sortie : 0 = tout passe, 1 = au moins une assertion échoue.
Note : qwen3.5:4b charge en >5s de load sur le Mac en alpage (agents en parallèle)
-> le 1,5b (986 Mo, souvent chaud) est le défaut par défaut.
"""
import argparse
import json
import os
import re
import subprocess
import sys

INDEX = os.path.expanduser("~/ace777-test-day1/Index_Maison")
PROMPT_CANON = os.path.join(INDEX, "identity", "prompts", "cortana.md")

# ── Assertions (le contrat de sortie) ──
RE_AVIS = re.compile(r"AVIS\s+STRICT\s*:\s*(LONG|SHORT|NEUTRE)", re.IGNORECASE)
RE_HORIZON = re.compile(r"HORIZON\s*:\s*(24h|48h|1\s*semaine|semaine)", re.IGNORECASE)
RE_CONFIANCE = re.compile(r"CONFIANCE\s*:\s*(haute|moyenne|faible)", re.IGNORECASE)
VERBES_ORDRE = ["achète", "vends", "achetez", "vendez", "passer un ordre",
                "j'ai ouvert", "j'ai vendu", "j'ai acheté"]


def lire_prompt():
    with open(PROMPT_CANON, encoding="utf-8") as f:
        return f.read()


def appel_ollama(system, user, model):
    """Ollama local — zéro budget, zéro clé. Contrat API simple (no stream)."""
    payload = json.dumps({"model": model, "messages": [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ], "stream": False}).encode()
    p = subprocess.run(["curl", "-s", "-m", "240", "http://127.0.0.1:11434/api/chat",
                       "-H", "Content-Type: application/json", "-d", payload],
                       capture_output=True, text=True, timeout=260)
    if p.returncode != 0 or not p.stdout.strip():
        raise RuntimeError(f"Ollama timeout/vide (rc={p.returncode}, stderr={p.stderr[:120]!r})")
    d = json.loads(p.stdout)
    return d["message"]["content"]


def appel_hub(system, user):
    """Via le hub ACE777 (budget cloud) — fallback si pas d'Ollama."""
    import urllib.request
    payload = json.dumps({"task": "analyse.profonde", "messages": [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ], "max_tokens": 600, "temperature": 0.3}).encode()
    req = urllib.request.Request("http://127.0.0.1:11435/v1/chat/completions",
                                 data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=200) as r:
        d = json.loads(r.read().decode())
    return d["choices"][0]["message"]["content"]


def verifier(content):
    """Retourne (ok: bool, raisons: list[str])."""
    raisons = []
    if not RE_AVIS.search(content):
        raisons.append("AVIS STRICT (LONG|SHORT|NEUTRE) manquant")
    if not RE_HORIZON.search(content):
        raisons.append("HORIZON (24h|48h|1 semaine) manquant")
    if not RE_CONFIANCE.search(content):
        raisons.append("CONFIANCE (haute|moyenne|faible) manquante")
    for v in VERBES_ORDRE:
        if re.search(r"\b" + re.escape(v), content, re.IGNORECASE):
            raisons.append(f"verbe d'ordre détecté : « {v} »")
    return (not raisons), raisons


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="qwen2.5-coder:1.5b")
    ap.add_argument("--hub", action="store_true")
    args = ap.parse_args()

    prompt = lire_prompt()
    # Cas de test : un état marché neutre-ish + score_justesse < 60% (exige CONFIANCE faible)
    user = (
        "FAITS (marché réel, chiffres exacts) :\n"
        "- BTC 77 850 USDT, -0,4 % sur 24 h, vol 24 h 18,2 Md$\n"
        "- Régime : CHOP (vortex_control), tension BETA 1,66, ALPHA 1,78\n"
        "- Fills du jour : BETA 2 (-2,96 brut, -4,15 net), ALPHA 0\n"
        "- score_justesse (indice analysé) : 52 % (SUR CET INDICE)\n\n"
        "Produis ton analyse selon ta structure obligatoire (FAITS, LECTURE "
        "PHYSIQUE, INTERPRÉTATION, MISE EN RELATION, PATTERN, OPINION, "
        "AVIS STRICT, SOURCES)."
    )

    print(f"[eval_cortana] modèle={args.model} {'(hub)' if args.hub else '(Ollama local)'}")
    if args.hub:
        content = appel_hub(prompt, user)
    else:
        content = appel_ollama(prompt, user, args.model)
    print("──── réponse ────")
    print(content[:1200])
    print("──── assertions ────")
    ok, raisons = verifier(content)
    for r in raisons:
        print(f"  ❌ {r}")
    if ok:
        print("  ✅ structure obligatoire respectée")
    # Règle 5 : score < 60% => CONFIANCE faible exigée
    m = RE_CONFIANCE.search(content)
    if m and m.group(1).lower() != "faible":
        print("  ❌ score_justesse 52% < 60% : CONFIANCE devrait être « faible »")
        ok = False
    print(f"\nVERDICT : {'PASS ✅' if ok else 'ÉCHEC ❌'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""skill_trading.py — Envoie un skill trading au hub prise-ia.
Usage: python3 skill_trading.py <nom-skill> [--contexte]
Exemple: python3 skill_trading.py slippage
"""
import json, os, sys, time, urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
SKILLS_PATH = os.path.expanduser(
    "~/ace777-test-day1/Index_Maison/strategie/SKILLS_TRADING.md")

SKILLS = {
    "slippage": 1, "exit": 2, "kelly": 3, "walkforward": 4, "risk": 5,
    "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
}

def _extraire_skill(nom):
    """Extrait le prompt d'un skill depuis SKILLS_TRADING.md."""
    with open(SKILLS_PATH, encoding="utf-8") as f:
        texte = f.read()

    # Mapping nom → section
    sections = texte.split("## ")
    for s in sections:
        s_clean = s.strip()
        # Cherche le numéro correspondant
        for key, num in SKILLS.items():
            if key == nom and s_clean.startswith(f"{num}."):
                # Extrait le bloc entre ``` et ```
                parties = s_clean.split("```\n")
                if len(parties) >= 2:
                    return parties[1].strip()
                # Fallback : tout le texte après le titre
                lignes = s_clean.split("\n")
                return "\n".join(lignes[1:]).strip()

    raise ValueError(f"Skill '{nom}' introuvable dans {SKILLS_PATH}")

def envoyer_skill(skill_nom, contexte=None):
    """Envoie le prompt au hub."""
    prompt = _extraire_skill(skill_nom)
    if contexte:
        prompt += f"\n\nCONNAISSANCE CONTEXTUELLE :\n{contexte}"

    messages = [
        {"role": "user", "content": prompt},
    ]

    payload = json.dumps({
        "model": "trading.skills",
        "messages": messages,
        "task": "trading.skills",
        "temperature": 0.3,
        "max_tokens": 3000,
    }).encode()

    print(f"[trading.skills] Envoi skill '{skill_nom}' au hub...", flush=True)
    t0 = time.time()

    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"},
                                 method="POST")
    try:
        with urllib.request.urlopen(req, timeout=420) as resp:
            data = json.loads(resp.read().decode())
    except Exception as e:
        print(f"[ERREUR] Hub injoignable : {e}")
        sys.exit(1)

    content = data["choices"][0]["message"]["content"]
    provider = data.get("provider", "?")
    attempts = data.get("attempts", [])
    dur = round(time.time() - t0, 1)

    print(f"[OK] Répondu via {provider} ({dur}s)")
    if attempts:
        print(f"     Tentatives : {' → '.join(attempts)}")
    print()
    print("=" * 60)
    print(content)
    print("=" * 60)

    # --- MEMOIRE AUTO-ÉCRITE (Rohit ⑥, 22/08) ---
    MEMOIRE = os.path.expanduser("~/ace777-test-day1/Index_Maison/MEMOIRE_COLLAB.md")
    try:
        ts = time.strftime("%Y-%m-%dT%H%MZ", time.gmtime())
        resume = content.split("\n")[0][:120] if content else "(vide)"
        with open(MEMOIRE, "a", encoding="utf-8") as mf:
            mf.write(f"| {ts} | skill:{skill_nom} | ★ | trading.skills → {provider} | {resume}\n")
    except Exception:
        pass

    return content

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Skill trading → hub prise-ia")
    parser.add_argument("skill", help="Nom du skill (slippage/exit/kelly/walkforward/risk)")
    parser.add_argument("--contexte", "-c", help="Contexte additionnel (fichier ou texte)")
    parser.add_argument("--save", "-s", help="Sauvegarder la réponse dans ce fichier")
    args = parser.parse_args()

    if args.skill not in SKILLS:
        print(f"Skills disponibles : {', '.join(SKILLS.keys())}")
        sys.exit(1)

    contexte = None
    if args.contexte:
        if os.path.exists(os.path.expanduser(args.contexte)):
            with open(os.path.expanduser(args.contexte), encoding="utf-8") as f:
                contexte = f.read()[:4000]
        else:
            contexte = args.contexte[:4000]

    reponse = envoyer_skill(args.skill, contexte)

    if args.save:
        path = os.path.expanduser(args.save)
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# Réponse skill '{args.skill}' — trading.skills\n\n{reponse}\n")
        print(f"[SAVE] {path}")
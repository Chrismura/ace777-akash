#!/usr/bin/env python3
"""qwen_elabore.py — Qwen solo : élabore des idées d'amélioration depuis le coffre.

Lecture: vault (CHANTIERS + MEMOIRE_COLLAB récente + journal des erreurs)
-> hub (tâche qwen.elabore, Qwen local gratuit) -> fiches déposées dans OUTBOX/AUTO_EVOL/IDEES.md

Règle d'or : Qwen PROPOSE, elle ne décide jamais. Ada relit + trie, Christophe GO.

Fix 08/08 (TCC) : les jobs launchd ne peuvent PAS écrire dans ~/Documents (PermissionError).
-> écriture redirigée vers OUTBOX_OBSIDIAN/AUTO_EVOL/IDEES.md (hors ~/Documents, autorisé).
-> le pont _sync_now.sh (run via terminal, TCC OK) copie ensuite vers le vault.
-> lecture : OUTBOX en priorité (copies récentes), vault en repli.

Usage:
    python3 qwen_elabore.py                     # élaboration générale (sujets par défaut)
    python3 qwen_elabore.py --sujet "hub"       # élaboration sur un sujet précis
    python3 qwen_elabore.py --json              # sortie brute JSON
"""
import argparse
import datetime
import json
import os
import sys
import urllib.request

VAULT = os.path.expanduser("~/Documents/Obsidian_ACE777")
OUTBOX = os.path.expanduser("~/ace777-test-day1/Index_Maison/OUTBOX_OBSIDIAN")
IDEES = os.path.join(OUTBOX, "AUTO_EVOL", "IDEES.md")
HUB = "http://127.0.0.1:11435/v1/chat/completions"
TASK = "qwen.elabore"
MAX_READ = 4000  # chars par fichier lu


def read_head(path: str, limit: int = MAX_READ) -> str:
    try:
        with open(path, errors="replace") as f:
            return f.read(limit)
    except OSError:
        return ""


def read_best(rel: str, limit: int = MAX_READ) -> str:
    """Lit le fichier relatif : OUTBOX (miroir, TCC OK) puis vault (repli)."""
    txt = read_head(os.path.join(OUTBOX, rel), limit)
    if txt:
        return txt
    return read_head(os.path.join(VAULT, rel), limit)


def build_contexte(sujet: str) -> str:
    ch = read_best("CHANTIERS.md")
    mem = read_best("MEMOIRE_COLLAB.md", 6000)
    err = read_best("journal_erreurs.md")
    if not err:
        err = read_best("JOURNAL_ERREURS_TEST.md")
    return f"""COFFRE (extraits) :
--- CHANTIERS.md ---
{ch[:2000]}

--- MEMOIRE_COLLAB.md (tête) ---
{mem[:2000]}

--- journal des erreurs ---
{err[:1500]}

SUJET D'ÉLABORATION : {sujet}
"""


def ask_hub(sujet: str) -> dict:
    payload = {
        "task": TASK,
        "messages": [
            {"role": "system", "content": (
                "Tu es QWEN, l'élaboratrice en chef du système ACE777 (Mac Air 8 Go, "
                "zéro budget cloud gaspillé). Tu PROPOSES, tu ne décides jamais. "
                "À partir du coffre fourni, élabore 2 à 3 idées CONCRÈTES et NOUVELLES "
                "d'amélioration (structure, intelligence, vitesse, plomberie). "
                "Format EXACT, pour chaque idée — avec un VRAI titre précis en français, "
                "jamais de placeholder ni de chevrons :\n"
                "### Titre précis de l'idée\n"
                "- **Quoi :** ...\n"
                "- **Pourquoi :** ...\n"
                "- **Effort :** faible/moyen/fort\n"
                "- **Risque :** ...\n"
                "Interdit : toucher au moteur de trading (ACE/Hulk), inventer des chiffres, "
                "proposer de la pub ou des outils payants sans justification. "
                "En français. Réaliste pour 8 Go de RAM."
            )},
            {"role": "user", "content": build_contexte(sujet)},
        ],
        "temperature": 0.7,
        "max_tokens": 2000,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=None) as resp:
        return json.loads(resp.read().decode())


def depose(contenu: str, sujet: str, provider: str) -> None:
    now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%MZ")
    date = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    bloc = (
        f"\n\n---\n\n"
        f"## 🌙 Qwen solo — {now} (sujet : {sujet}) · provider {provider}\n\n"
        f"{contenu.strip()}\n"
    )
    os.makedirs(os.path.dirname(IDEES), exist_ok=True)
    with open(IDEES, "a") as f:
        f.write(bloc)
    print(f"depose OK -> {IDEES} (bloc {date})")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sujet", default="améliorations structure/intelligence/vitesse de la plomberie")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    result = ask_hub(args.sujet)
    content = result["choices"][0]["message"]["content"]
    provider = result.get("provider", "?")

    if args.json:
        print(json.dumps({"provider": provider, "sujet": args.sujet,
                          "contenu": content}, ensure_ascii=False, indent=2))
        return 0

    depose(content, args.sujet, provider)
    print(f"provider: {provider}")
    print(content[:1200])
    return 0


if __name__ == "__main__":
    sys.exit(main())

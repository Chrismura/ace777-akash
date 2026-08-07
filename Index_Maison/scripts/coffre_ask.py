#!/usr/bin/env python3
"""coffre_ask.py — le coffre interactif (RAG léger, zéro dépendance).

Question -> recherche dans le vault Obsidian_ACE777 -> extraits sourcés
-> hub prise-ia (task coffre.ask) -> réponse avec citations de fichiers.

Usage:
    python3 coffre_ask.py "quelle est notre politique d'oubli ?"
    python3 coffre_ask.py "état du master analyste" --top 8

Sortie: réponse du hub + section SOURCES (fichiers cités, avec chemins).
"""
import argparse
import json
import os
import re
import sys
import urllib.request
from collections import Counter

VAULT = os.path.expanduser("~/Documents/Obsidian_ACE777")
HUB = "http://127.0.0.1:11435/v1/chat/completions"
TASK = "coffre.ask"
SKIP_DIRS = {".obsidian", ".git", ".trash", "node_modules", ".DS_Store"}
SKIP_PREFIX = ("Archives_Signets", "_ARCHIVE", "Archive")
MAX_FILE_BYTES = 400_000          # ne pas lire les fichiers géants
TOP_FILES = 6                     # nb de fichiers retenus
EXTRACT_CHARS = 1600              # extrait max par fichier

STOPWORDS = {
    "avec", "cette", "dans", "est", "mais", "nous", "pour", "quoi", "sont",
    "tout", "une", "vous", "être", "avoir", "fait", "faire", "plus", "dans",
    "comment", "quelle", "quand", "où", "qui", "quel", "peut", "être",
}


def tokenize(text: str) -> list:
    words = re.findall(r"[a-zà-ÿ0-9]{3,}", text.lower())
    return [w for w in words if w not in STOPWORDS]


def walk_md_files():
    for root, dirs, files in os.walk(VAULT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS
                   and not d.startswith(SKIP_PREFIX)]
        for name in files:
            if name.endswith(".md") and not name.startswith("."):
                yield os.path.join(root, name)


def score_file(path: str, keywords: Counter) -> tuple:
    """Retourne (score, extraits). Score = poids des mots-clés trouvés."""
    try:
        if os.path.getsize(path) > MAX_FILE_BYTES:
            return 0, []
        with open(path, errors="replace") as f:
            text = f.read()
    except OSError:
        return 0, []
    if not text.strip():
        return 0, []

    title = os.path.basename(path)[:-3]
    content = text
    score = 0
    for kw, weight in keywords.items():
        n_title = title.lower().count(kw)
        n_content = content.lower().count(kw)
        if n_content:
            score += min(n_content, 20) * weight
        if n_title:
            score += n_title * weight * 3

    # Extraits : lignes contenant un mot-clé, ±1 ligne autour
    lines = content.splitlines()
    hits = [i for i, ln in enumerate(lines) if any(
        kw in ln.lower() for kw in keywords)]
    if not hits:
        return score, []
    extracts, budget = [], EXTRACT_CHARS
    for i in hits[:8]:
        block = "\n".join(lines[max(0, i - 1): i + 2]).strip()
        if len(block) > budget:
            block = block[:budget]
        if block:
            extracts.append(block)
            budget -= len(block)
        if budget <= 0:
            break
    return score, extracts


def ask_hub(question: str, context: str) -> dict:
    payload = {
        "task": TASK,
        "messages": [
            {"role": "system", "content": (
                "Tu es le COFFRE INTERACTIF d'Obsidian (vault ACE777). "
                "Tu réponds en français, factuel, structuré. Tu réponds UNIQUEMENT "
                "à partir des extraits fournis : si l'info n'y est pas, dis-le "
                "clairement (jamais d'invention). Cite les fichiers sources entre "
                "crochets, ex : [POLITIQUE_OUBLI.md]."
            )},
            {"role": "user", "content": (
                f"QUESTION : {question}\n\n"
                f"EXTRAITS DU COFFRE (recherche par mots-clés) :\n\n{context}"
            )},
        ],
        "temperature": 0.3,
        "max_tokens": 1200,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=600) as resp:
        return json.loads(resp.read().decode())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("question")
    ap.add_argument("--top", type=int, default=TOP_FILES)
    ap.add_argument("--json", action="store_true", help="sortie brute JSON")
    args = ap.parse_args()

    keywords = Counter(tokenize(args.question))
    if not keywords:
        print("Question trop courte ou vide.")
        return 1
    # Pondération : les mots rares pèsent plus
    total = sum(keywords.values())
    weights = Counter({k: max(1, round(v * 4 / total) or 1)
                       for k, v in keywords.items()})

    # Scan du vault
    scored = []
    n_files = 0
    for path in walk_md_files():
        n_files += 1
        s, extracts = score_file(path, weights)
        if s > 0:
            scored.append((s, path, extracts))
    scored.sort(key=lambda x: -x[0])

    if not scored:
        print("Aucun fichier du coffre ne correspond à la question.")
        return 1

    # Contexte = extraits des top fichiers
    context_parts = []
    for s, path, extracts in scored[:args.top]:
        rel = os.path.relpath(path, VAULT)
        context_parts.append(f"--- [{rel}] (score {s}) ---")
        context_parts.extend(extracts[:4])
    context = "\n".join(context_parts)[:9000]

    # Hub
    result = ask_hub(args.question, context)
    content = result["choices"][0]["message"]["content"]
    provider = result.get("provider", "?")

    if args.json:
        print(json.dumps({
            "question": args.question,
            "provider": provider,
            "files_scanned": n_files,
            "sources": [os.path.relpath(p, VAULT)
                        for _, p, _ in scored[:args.top]],
            "answer": content,
        }, ensure_ascii=False, indent=2))
        return 0

    print(f"🔍 {n_files} fichiers du coffre scannés — {len(scored)} pertinents")
    print(f"🤖 Réponse ({provider}) :")
    print()
    print(content)
    print()
    print("📚 SOURCES :")
    for s, path, _ in scored[:args.top]:
        print(f"  • {os.path.relpath(path, VAULT)} (score {s})")
    return 0


if __name__ == "__main__":
    sys.exit(main())

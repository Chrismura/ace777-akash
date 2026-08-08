#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""atelier_liens.py — crée les connexions entre les notes du vault (Obsidian).

Problème constaté 08/08 (Christophe) : le graphe Obsidian ne bouge pas car les
notes (signets, évaluations, tableaux) sont ajoutées SANS liens [[...]].
→ 435 signets créés en août = 0 lien. Le graphe ne dessine que ce qui existe.

Cet atelier (mode usine) :
1. Indexe les notes du vault par mots-clés (titre + contenu, stopwords filtrés).
2. Pour chaque note cible, trouve les N notes les plus proches par thème partagé.
3. Ajoute une section "## 🔗 Connexions" en pied de note (3-5 liens max, jamais
   de doublon, jamais de lien vers elle-même).
4. Idempotent : relançable, ne ré-écrit pas les notes déjà connectées.

Usage:
  python3 atelier_liens.py --dry-run --limit 10      # montre ce qui serait fait
  python3 atelier_liens.py --limit 100               # applique aux 100 notes récentes
  python3 atelier_liens.py --all                     # tout le vault (prudent : gros)
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

VAULT = Path.home() / "Documents" / "Obsidian_ACE777"

SKIP_DIRS = {".git", ".obsidian", "thermo", "cockpit", "graph_cerveau",
             ".trash", ".DS_Store", "node_modules", "OUTBOX_OBSIDIAN"}
SKIP_FILES = {"INVENTAIRE_COMPLET.md"}  # généré, ne pas éditer

MAX_LINKS = 5
MIN_SCORE = 2          # intersections de mots-clés minimales pour lier
MIN_WORD = 4           # longueur minimale d'un mot-clé

STOP = {
    # français
    "dans", "avec", "cette", "cet", "ces", "pour", "mais", "donc", "alors",
    "quand", "bien", "tout", "tous", "toute", "toutes", "être", "avoir",
    "faire", "fait", "pas", "plus", "moins", "comme", "leur", "leurs", "nous",
    "vous", "ils", "elles", "cela", "cette", "celui", "celle", "entre", "chez",
    "aussi", "très", "peu", "assez", "trop", "sans", "sous", "sur", "vers",
    "contre", "depuis", "pendant", "avant", "après", "durant", "parce", "car",
    "puis", "ainsi", "encore", "toujours", "jamais", "souvent", "parfois",
    "aujourd", "demain", "hier", "année", "mois", "jour", "jours", "heure",
    "heures", "page", "pages", "fichier", "fichiers", "note", "notes",
    "vault", "obsidian", "https", "http", "com", "www", "avec", "pour",
    # anglais
    "that", "this", "with", "from", "have", "been", "will", "would", "could",
    "should", "into", "your", "they", "them", "there", "their", "what",
    "when", "where", "which", "these", "those", "about", "because", "after",
    "before", "while", "again", "more", "most", "some", "such", "only",
    "very", "just", "also", "than", "then", "than", "was", "were", "are",
    "you", "its", "our", "his", "her", "has", "had", "does", "did", "being",
    "been", "can", "may", "might", "must", "shall", "new", "use", "used",
    "using", "one", "two", "make", "made", "like", "time", "times", "way",
    "ways", "thing", "things", "people", "good", "great", "best", "really",
    "first", "last", "said", "says", "know", "knows", "need", "needs", "want",
    "wants", "work", "works", "working", "live", "lives", "post", "posts",
    "link", "links", "read", "reading", "write", "writing", "give", "gives",
}


def tokens(text: str) -> list:
    """Mots-clés significatifs d'un texte (minuscules, stopwords filtrés)."""
    out = []
    for w in re.findall(r"[a-zàâäéèêëîïôöùûüç0-9]{4,}", text.lower()):
        if w not in STOP and not w.isdigit():
            out.append(w)
    return out


def title_of(path: Path) -> str:
    """Titre court = nom du fichier sans date ni id twitter."""
    name = path.stem
    # "2026-08-01 @auteur - Sujet (id).md" → garde "Sujet"
    name = re.sub(r"^2026-\d{2}-\d{2}\s*", "", name)
    name = re.sub(r"@\w+\s*-?\s*", "", name)
    name = re.sub(r"\s*\(\d+\)$", "", name)
    return name.strip() or path.stem


def scan_notes() -> list:
    notes = []
    for p in VAULT.rglob("*.md"):
        if any(seg in SKIP_DIRS for seg in p.parts):
            continue
        if p.name in SKIP_FILES:
            continue
        notes.append(p)
    return notes


def build_index(notes):
    """note -> Counter(mots-clés)  et  mot -> set(notes)."""
    profils = {}
    index = defaultdict(set)
    for p in notes:
        try:
            txt = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        # titre + contenu (frontmatter inclus, tags utiles)
        ws = tokens(p.stem + " " + txt)
        if not ws:
            continue
        c = Counter(ws)
        profils[p] = c
        for w in c:
            index[w].add(p)
    return profils, index


def voisins(p, profils, index, k=MAX_LINKS):
    """Les k notes les plus proches par mots-clés partagés."""
    c = profils[p]
    scores = Counter()
    for w, f in c.items():
        for q in index.get(w, ()):
            if q == p:
                continue
            # poids : fréquence ici × présence chez l'autre
            scores[q] += f + profils[q][w]
    if not scores:
        return []
    return [q for q, s in scores.most_common(k + 3) if s >= MIN_SCORE][:k]


def add_connexions(p: Path, vois: list, dry: bool) -> bool:
    txt = p.read_text(encoding="utf-8", errors="replace")
    if "## 🔗 Connexions" in txt:
        return False
    # évite les doublons déjà présents dans le corps
    existants = set(re.findall(r"\[\[([^\]|]+)", txt))
    liens = []
    for q in vois:
        if q.stem in existants:
            continue
        liens.append(f"- [[{q.stem}]] — {title_of(q)[:60]}")
    if not liens:
        return False
    bloc = "\n\n## 🔗 Connexions\n\n" + "\n".join(liens[:MAX_LINKS]) + "\n"
    if dry:
        return True
    txt = txt.rstrip() + bloc
    p.write_text(txt, encoding="utf-8")
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="ne rien écrire")
    ap.add_argument("--limit", type=int, default=0,
                    help="ne traiter que les N notes les plus récentes")
    ap.add_argument("--all", action="store_true", help="tout le vault")
    args = ap.parse_args()

    toutes = scan_notes()
    # L'INDEX couvre TOUT le vault (pour des voisins riches), les CIBLES =
    # sous-ensemble sélectionné (récentes, ou tout si --all).
    profils, index = build_index(toutes)
    if args.all:
        notes = toutes
    elif args.limit:
        notes = sorted(toutes, key=lambda p: p.stat().st_mtime,
                       reverse=True)[:args.limit]
    else:
        notes = toutes
    print(f"Index : {len(profils)}/{len(toutes)} notes, "
          f"{sum(len(v) for v in index.values())} occurrences · Cibles : {len(notes)}")

    fait, deja, sans = 0, 0, 0
    for p in sorted(notes):
        if p not in profils:
            sans += 1
            continue
        v = voisins(p, profils, index)
        if add_connexions(p, v, args.dry_run):
            fait += 1
        else:
            deja += 1

    mode = "DRY-RUN (rien écrit)" if args.dry_run else "APPLIQUÉ"
    print(f"\n[{mode}] connectées : {fait} · déjà connectées / sans lien : {deja} · non indexées : {sans}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère le DIFF EXACT du correctif CSV depuis le fichier réel (aucune hallucination).

Ne modifie PAS le genesis : produit uniquement un fichier de revue avec before/after."""
import os

ROOT = os.path.expanduser("~/ace777-test-day1")
GEN = os.path.join(ROOT, "genesis_manifest.txt")
OUT = os.path.join(ROOT, "Index_Maison", "DIFF_EXACT_FIX_CSV_2026-08-15.md")

LINES = [1523, 1537, 1706, 1801, 1813, 1821, 1835, 1851, 1869, 1931,
         1981, 2039, 2067, 2119, 2441, 2507]

src = open(GEN, encoding="utf-8").read().splitlines()

# Transformation : insérer un champ juste après le 10e champ (exitReason).
# Pour FILLED (2507) -> $hold_done ; sinon champ vide.
def transform(line, is_filled):
    # la ligne est un echo "...CSV..." >> "$LOG_FILE"
    # on ne touche que le contenu entre le 1er et le 2e guillemet
    q1 = line.index('"')
    q2 = line.index('"', q1 + 1)
    body = line[q1 + 1:q2]
    parts = body.split(",")
    # fields: 0..9 = 10 premiers, 10 = exitReason, 11.. = message
    insert = "$hold_done" if is_filled else ""
    new_parts = parts[:10] + [insert] + parts[10:]
    new_body = ",".join(new_parts)
    return line[:q1 + 1] + new_body + line[q2:]


lines_out = ["# DIFF EXACT — correctif CSV (16 lignes) — généré depuis le fichier réel",
             "",
             "Règle : insérer un champ après le 10e (exitReason).",
             "FILLED → `$hold_done` · autres → champ vide.",
             ""]

for ln in LINES:
    before = src[ln - 1]
    after = transform(before, is_filled=(ln == 2507))
    ok = after.count(",") - before.count(",") == 1
    lines_out.append(f"## L{ln}  (insertion {'$hold_done' if ln == 2507 else 'vide'}, +1 virgule: {'OK' if ok else 'CHECK'})")
    lines_out.append("```diff")
    lines_out.append(f"-{before.strip()}")
    lines_out.append(f"+{after.strip()}")
    lines_out.append("```")
    lines_out.append("")

open(OUT, "w", encoding="utf-8").write("\n".join(lines_out))

# vérification : nb de virgules avant/après pour chaque ligne
print("Diff exact généré :", OUT)
for ln in LINES:
    before = src[ln - 1]
    after = transform(before, ln == 2507)
    b = before.count(",")
    a = after.count(",")
    flag = "OK" if a - b == 1 else "ERREUR"
    print(f"L{ln}: virgules {b} -> {a} ({flag})")

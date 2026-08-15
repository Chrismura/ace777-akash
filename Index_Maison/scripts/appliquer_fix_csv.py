#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Appliquer le correctif CSV (16 lignes) au genesis — avec backup + vérification.

Fixe les écritures CSV (11 -> 12 champs) pour que la durée $hold_done atterrisse
dans holdSec (FILLED) et le message dans msg. Ne touche que ces 16 lignes."""
import hashlib
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone

ROOT = os.path.expanduser("~/ace777-test-day1")
GEN = os.path.join(ROOT, "genesis_manifest.txt")

LINES = [1523, 1537, 1706, 1801, 1813, 1821, 1835, 1851, 1869, 1931,
         1981, 2039, 2067, 2119, 2441, 2507]


def transform(line, is_filled):
    q1 = line.index('"')
    q2 = line.index('"', q1 + 1)
    body = line[q1 + 1:q2]
    parts = body.split(",")
    insert = "$hold_done" if is_filled else ""
    new_parts = parts[:10] + [insert] + parts[10:]
    new_body = ",".join(new_parts)
    return line[:q1 + 1] + new_body + line[q2:]


def md5(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def main():
    old_md5 = md5(GEN)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    bak = f"{GEN}.BAK_avant_fix_csv_{ts}"
    shutil.copy2(GEN, bak)
    print(f"Backup : {bak}")

    src = open(GEN, encoding="utf-8").read().splitlines()

    # vérification préalable : chaque ligne cible a exactement 10 virgules (11 champs)
    for ln in LINES:
        c = src[ln - 1].count(",")
        if c != 10:
            print(f"ABORT: L{ln} a {c} virgules (attendu 10) — fichier inattendu")
            sys.exit(1)

    out = list(src)
    for ln in LINES:
        out[ln - 1] = transform(src[ln - 1], ln == 2507)

    # vérification : seules les 16 lignes ont changé
    changed = [i for i in range(len(src)) if src[i] != out[i]]
    if changed != [l - 1 for l in LINES]:
        print(f"ABORT: lignes modifiées inattendues: {[c + 1 for c in changed]}")
        sys.exit(1)

    open(GEN, "w", encoding="utf-8").write("\n".join(out) + "\n")

    new_md5 = md5(GEN)
    print(f"md5 avant: {old_md5}")
    print(f"md5 après: {new_md5}")
    print(f"16 lignes modifiées, chacune 11 -> 12 champs")

    # syntaxe bash
    r = subprocess.run(["bash", "-n", GEN], capture_output=True, text=True)
    if r.returncode != 0:
        print("ABORT: bash -n a échoué :")
        print(r.stderr)
        sys.exit(1)
    print("bash -n: OK (syntaxe valide)")


if __name__ == "__main__":
    main()

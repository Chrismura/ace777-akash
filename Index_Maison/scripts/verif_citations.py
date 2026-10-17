#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verif_citations.py — GATE 11 roadmap @de1lymoon (GO 17/10, lecture seule).

Toute phrase entre "..." dans un brouillon DOIT etre une sous-chaine EXACTE
d'une source citee (pas flou, pas semantique). Sinon = FLAG, ne shippe pas.
Usage : python3 verif_citations.py BROUILLON.md SOURCE1.md [SOURCE2.md ...]
        python3 verif_citations.py --autotest   (5 cas, rc=0 si tout passe)
Stdlib uniquement, lecture seule.
"""
import re
import sys

GUILLEMETS = re.compile(r'"([^"\n]{4,300})"')


def citations(draft):
    return GUILLEMETS.findall(draft)


def verifier(draft, sources):
    """Retourne (ok_list, flag_list). ok=(citation, source_idx)."""
    corpus = [(i, s) for i, s in enumerate(sources)]
    ok, flag = [], []
    for c in citations(draft):
        trouve = next((i for i, s in corpus if c in s), None)
        (ok if trouve is not None else flag).append((c, trouve))
    return ok, flag


def autotest():
    src = "Le chat dort. Ceci est une phrase source exacte."
    cas = [
        ('Il dit "Ceci est une phrase source exacte."', [src], 1, 0),
        ('Il dit "le ciel est vert."', [src], 0, 1),
        ("Pas de guillemets ici.", [src], 0, 0),
        ('Il dit "Le chat dort."', ["rien.", src], 1, 0),
        ('Il dit "ceci EST une phrase source exacte."', [src], 0, 1),
    ]
    n = 0
    for draft, sources, want_ok, want_flag in cas:
        ok, flag = verifier(draft, sources)
        assert len(ok) == want_ok and len(flag) == want_flag, (draft, ok, flag)
        n += 1
    print(f"autotest {n}/{len(cas)} OK")
    return 0


def main():
    if len(sys.argv) == 2 and sys.argv[1] == "--autotest":
        return autotest()
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    draft = open(sys.argv[1], encoding="utf-8").read()
    sources = [open(p, encoding="utf-8").read() for p in sys.argv[2:]]
    ok, flag = verifier(draft, sources)
    for c, i in ok:
        print(f'OK   [{sys.argv[2 + i]}] "{c[:70]}"')
    for c, _ in flag:
        print(f'FLAG (absente des sources) "{c[:70]}"')
    print(f"--- {len(ok)} sourcées, {len(flag)} FLAG sur {len(ok) + len(flag)} citations ---")
    return 0


if __name__ == "__main__":
    sys.exit(main())

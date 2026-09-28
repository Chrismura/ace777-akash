#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""harnais_reseau_injoignable.py — HARNAIS « RÉSEAU INJOIGNABLE » (28/09/2026, ALPAGE).

CE QU'IL PROUVE : quand une source externe est injoignable, les 4 organes réparés le
28/09 sortent avec leur CODE DÉCLARÉ (3) et un MESSAGE CLAIR — plus JAMAIS un traceback.
Pourquoi ça compte : un traceback = code 1 NON DÉCLARÉ = la page vol peignait « échec
réel » un organe intact (faux positif, R14), et personne ne savait qu'il s'agissait d'un
simple hoquet DNS de 2 s (cause MESURÉE le 28/09 : tether iPhone endormi, `URLError Errno 8`).

COMMENT : on remplace `urllib.request.urlopen` par une fonction qui lève l'erreur RÉELLE
mesurée, puis on LANCE le vrai script (inchangé sur disque) et on lit son code de sortie.
Le backoff est réellement attendu — c'est la preuve que les essais ont bien lieu.

LECTURE SEULE sur le repo : aucun fichier modifié, aucun ordre, 0 €.

Usage : python3 Index_Maison/scripts/harnais_reseau_injoignable.py
Sortie : rc=0 si les 4 organes sont conformes (code déclaré, aucun traceback).
"""
import os
import re
import subprocess
import sys

REPO = os.path.expanduser("~/ace777-test-day1")

# (nom, chemin relatif au repo, code de sortie ATTENDU = celui déclaré au contrat)
ORGANES = [
    ("kronos-ombre", "Index_Maison/scripts/kronos_ombre.py", 3),
    ("sniffer-vieux-btc", "Index_Maison/scripts/sniffer_vieux_btc.py", 3),
    ("xrpl-gouvernance", "Index_Maison/scripts/collecter_gouvernance_xrpl.py", 3),
    ("sonde-volume-panier", "hulk-mexc/scripts/sonde_volume_panier.py", 3),
]

# Le patch vit dans un -c : il n'écrit RIEN sur le disque, il ne fait que simuler un DNS muet.
PATCH = r'''
import runpy, sys, urllib.request, urllib.error
cible = sys.argv[1]
sys.argv = [cible]
def _boom(*a, **k):
    raise urllib.error.URLError(OSError(8, "nodename nor servname provided, or not known"))
urllib.request.urlopen = _boom
runpy.run_path(cible, run_name="__main__")
'''


def main() -> int:
    ok = True
    print("== HARNAIS RÉSEAU INJOIGNABLE — 4 organes, source externe muette ==")
    for nom, chemin, code_attendu in ORGANES:
        p = os.path.join(REPO, chemin)
        if not os.path.exists(p):
            print(f"❌ {nom:22s} SCRIPT ABSENT : {chemin}")
            ok = False
            continue
        r = subprocess.run([sys.executable, "-c", PATCH, p],
                           capture_output=True, text=True,
                           cwd=os.path.dirname(p), timeout=180)
        sortie = (r.stdout or "") + (r.stderr or "")
        traceback = "Traceback (most recent call last)" in (r.stderr or "")
        declare = bool(re.search(r"DECLARE|DÉCLARÉ|déclaré", sortie))
        bon_code = (r.returncode == code_attendu)
        bon = bon_code and not traceback and declare
        ok = ok and bon
        print(f"{'✅' if bon else '❌'} {nom:22s} code={r.returncode} (attendu {code_attendu}) · "
              f"traceback={'OUI' if traceback else 'non'} · message déclaré={'oui' if declare else 'NON'}")
        for l in [x for x in sortie.splitlines() if x.strip()][-2:]:
            print(f"     └ {l[:150]}")
    print("\nVERDICT : " + ("FIABLE — les 4 organes sortent proprement avec leur code DÉCLARÉ, "
                            "aucun traceback, aucun code non déclaré."
                            if ok else "ÉCHEC — voir ci-dessus."))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

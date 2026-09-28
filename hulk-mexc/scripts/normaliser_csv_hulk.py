#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""normaliser_csv_hulk.py — NORMALISATION du journal paper Hulk (27/09/2026).

PROBLÈME MESURÉ (point du 27/09) : PAPER_V1_20260923_114444.csv mélange DEUX schémas.
Le writer (paper_diprip.py) écrit 16 colonnes depuis le 23/09 10:53 ; tout l'historique
d'avant est en 11 colonnes. Résultat : 76 162 lignes à 11 champs pour 3 843 à 16 — un
lecteur qui suppose 16 colonnes lit FAUX en silence. S'ajoutent 263 lignes strictement
dupliquées.

CE QUE FAIT CE SCRIPT (et rien d'autre) :
  - pad chaque ligne à la largeur de l'entête (colonnes manquantes -> vides) ;
  - supprime les lignes STRICTEMENT dupliquées (garde la 1re occurrence, ordre préservé) ;
  - sauvegarde puis écriture ATOMIQUE (tmp + os.replace) ;
  - idempotent : relancé, il ne change plus rien.

SÉCURITÉ (ne casse JAMAIS le run en cours) :
  - DÉFAUT = dry-run (montre, n'écrit pas) ;
  - `--apply` REFUSE d'écrire si un process paper_diprip tourne (le fichier est ouvert en
    append : un os.replace pendant un run perdrait les écritures du process). Il faut alors
    le lancer Hulk arrêté, ou forcer explicitement `--apply --force` en connaissance de cause.

Usage :
  python3 normaliser_csv_hulk.py                       # dry-run sur le dernier run
  python3 normaliser_csv_hulk.py --csv <chemin>        # dry-run sur un fichier donné
  python3 normaliser_csv_hulk.py --apply               # écrit (si Hulk est arrêté)
"""
import argparse
import csv
import io
import os
import shutil
import subprocess
import sys
import time

RUNS = os.path.join(os.path.expanduser('~'), 'ace777-test-day1', 'hulk-mexc', 'runs')


def dernier_csv():
    best, best_m = None, -1
    try:
        for f in os.listdir(RUNS):
            if f.startswith('PAPER_V1_') and f.endswith('.csv'):
                m = os.path.getmtime(os.path.join(RUNS, f))
                if m > best_m:
                    best, best_m = f, m
    except FileNotFoundError:
        return None
    return os.path.join(RUNS, best) if best else None


def paper_tourne():
    """Vrai si un process paper_diprip est vivant (pgrep, lecture seule)."""
    try:
        out = subprocess.run(['pgrep', '-fl', 'paper_diprip'],
                             capture_output=True, text=True).stdout
        return 'paper_diprip' in out
    except Exception:
        return False


def lire(chemin):
    with io.open(chemin, 'r', encoding='utf-8', errors='replace', newline='') as fh:
        rows = list(csv.reader(fh))
    return rows


def analyser(rows):
    """Retourne (entete, largeur_cible, stats)."""
    entete = rows[0]
    cible = len(entete)
    mal = sum(1 for r in rows[1:] if len(r) > cible)
    largeurs = {}
    for r in rows[1:]:
        largeurs[len(r)] = largeurs.get(len(r), 0) + 1
    return entete, cible, {'mal': mal, 'largeurs': largeurs}


def normaliser(rows, cible):
    """Pad + dédup. Retourne (nouvelles_lignes, nb_pad, nb_dup)."""
    vues = set()
    out = [rows[0]]
    nb_pad = nb_dup = 0
    for r in rows[1:]:
        key = tuple(r)
        if key in vues:
            nb_dup += 1
            continue
        vues.add(key)
        if len(r) < cible:
            nb_pad += 1
            r = r + [''] * (cible - len(r))
        out.append(r)
    return out, nb_pad, nb_dup


def ecrire_atomique(chemin, rows, entete):
    """Backup horodaté + écriture atomique. Séparateur : entête décide (',' ; déjà le cas)."""
    bak = '%s.bak-avant-normalisation-%s' % (chemin, time.strftime('%Y%m%d-%H%M%S'))
    shutil.copy2(chemin, bak)
    tmp = chemin + '.tmp-normalisation'
    with io.open(tmp, 'w', encoding='utf-8', newline='') as fh:
        w = csv.writer(fh, lineterminator='\r\n')
        w.writerows(rows)
    os.replace(tmp, chemin)
    return bak


def main():
    ap = argparse.ArgumentParser(description='Normalise le CSV paper Hulk (pad 16 col + dédup).')
    ap.add_argument('--csv', default=None, help='chemin du CSV (défaut : dernier run)')
    ap.add_argument('--apply', action='store_true', help='écrit réellement (défaut : dry-run)')
    ap.add_argument('--force', action='store_true', help='écrire même si paper_diprip tourne (DANGEREUX)')
    args = ap.parse_args()

    chemin = args.csv or dernier_csv()
    if not chemin or not os.path.exists(chemin):
        print('[ERREUR] CSV introuvable:', chemin, file=sys.stderr)
        sys.exit(2)

    rows = lire(chemin)
    if not rows:
        print('[ERREUR] CSV vide:', chemin, file=sys.stderr)
        sys.exit(2)
    entete, cible, stats = analyser(rows)
    nouvelles, nb_pad, nb_dup = normaliser(rows, cible)

    print('CSV            :', chemin)
    print('entête         :', cible, 'colonnes')
    print('lignes données :', len(rows) - 1)
    print('largeurs       :', dict(sorted(stats['largeurs'].items())))
    print('lignes >%d col : %d (laissées telles quelles)' % (cible, stats['mal']))
    print('à padder       :', nb_pad)
    print('doublons exacts:', nb_dup)
    print('après          :', len(nouvelles) - 1, 'lignes')
    print('Hulk actif     :', 'OUI' if paper_tourne() else 'non')

    if not args.apply:
        print('\n[DRY-RUN] rien écrit. Relancer avec --apply (Hulk arrêté) pour appliquer.')
        return

    if paper_tourne() and not args.force:
        print('\n[REFUS] paper_diprip tourne : le fichier est ouvert en append. '
              'Arrêter Hulk avant --apply, ou --apply --force en connaissance de cause.',
              file=sys.stderr)
        sys.exit(3)

    bak = ecrire_atomique(chemin, nouvelles, entete)
    # vérification : relire et confirmer
    relu = lire(chemin)
    ok = (len(relu) == len(nouvelles)
          and all(len(r) == cible for r in relu[1:])
          and len(set(tuple(r) for r in relu[1:])) == len(relu) - 1)
    print('\n[APPLIQUÉ] backup :', bak)
    print('[VÉRIF] cohérent :', 'OUI' if ok else 'NON — à inspecter')
    if not ok:
        sys.exit(4)


if __name__ == '__main__':
    main()

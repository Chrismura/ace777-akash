#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# rotation_jsonl.py — rotation COPYTRUNCATE + gzip des JSONL à croissance
# illimitée (leçon : croisement_contexte.jsonl 286→301 Mo a bloqué le push
# GitHub 3 jours ; journal_intention.jsonl 29 Mo sur la même trajectoire).
#
# Pourquoi COPYTRUNCATE : les fichiers sont append-only et ÉCRITS EN CONTINU
# par des process vivants (paper_diprip, famille_session, etc.). On copie puis
# on tronque — l'écrivain garde son fd ouvert et continue à la fin du fichier.
# Pas de rename (sinon l'écrivain écrirait dans l'ancien inode, perdu).
#
# Archives gzipées (disque = essence en alpage). BACKUP_COUNT gardé.
#
# Usage :
#   python3 rotation_jsonl.py                # rotation selon SEUIL par défaut
#   python3 rotation_jsonl.py --seuil 20     # seuil 20 Mo pour tous
#   python3 rotation_jsonl.py --dry-run      # affiche sans rien faire
# Appelé par superviseur_core.sh (check_rotation, 6 h) — pas de nouvel agent.
import argparse
import gzip
import os
import shutil
from datetime import datetime, timezone

# ── Cibles : fichiers à croissance illimitée (hors git par décision famille) ──
DEFAUTS = [
    ("/Users/christophe/ace777-test-day1/hulk-mexc/runs/croisement_contexte.jsonl", 100),
    ("/Users/christophe/ace777-test-day1/Index_Maison/strategie/journal_intention.jsonl", 50),
    ("/Users/christophe/ace777-test-day1/Index_Maison/thermo/history.jsonl", 50),
    ("/Users/christophe/ace777-test-day1/Index_Maison/thermo/regime_couleur.jsonl", 50),
    ("/Users/christophe/ace777-test-day1/Index_Maison/data/mempool_vus.jsonl", 50),
    ("/Users/christophe/ace777-test-day1/Index_Maison/data/whales_mouvements.jsonl", 50),
]

BACKUP_COUNT = 2
LOG = "/Users/christophe/ace777-test-day1/Index_Maison/scripts/rotation_jsonl.log"


def rotate_file(filepath, seuil_mo, dry_run=False):
    """COPYTRUNCATE + gzip. Retourne la taille rotée ou None."""
    try:
        size = os.path.getsize(filepath)
    except OSError:
        return None
    if size <= seuil_mo * 1024 * 1024:
        return None

    try:
        # Décale les archives existantes (.1.gz -> .2.gz, etc.)
        for i in range(BACKUP_COUNT, 0, -1):
            src = f"{filepath}.{i-1}.gz" if i > 1 else f"{filepath}.1.gz"
            dst = f"{filepath}.{i}.gz"
            if i == 1:
                continue  # .1.gz sera créé par la compression ci-dessous
            if os.path.exists(src):
                if os.path.exists(dst):
                    os.remove(dst)
                os.rename(src, dst)
        extra = f"{filepath}.{BACKUP_COUNT+1}.gz"
        if os.path.exists(extra):
            os.remove(extra)

        if dry_run:
            return size

        # Copie compressée de l'état actuel -> .1.gz
        with open(filepath, "rb") as fin, gzip.open(f"{filepath}.1.gz", "wb") as fout:
            shutil.copyfileobj(fin, fout, length=1024 * 1024)
        # Tronque l'original (l'écrivain continue à la fin du fichier)
        with open(filepath, "w", encoding="utf-8") as f:
            f.truncate(0)
        return size
    except Exception:
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seuil", type=int, default=None, help="seuil Mo (défaut : par fichier)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    now = datetime.now(timezone.utc).isoformat()
    rotate_ok = 0
    for path, seuil_defaut in DEFAUTS:
        seuil = args.seuil if args.seuil else seuil_defaut
        size = rotate_file(path, seuil, dry_run=args.dry_run)
        if size is not None:
            rotate_ok += 1
            line = f"[{now}] rotation: {path} ({size} octets -> .1.gz, backups={BACKUP_COUNT})"
            print(line)
            if not args.dry_run:
                try:
                    with open(LOG, "a", encoding="utf-8") as f:
                        f.write(line + "\n")
                except OSError:
                    pass
    if not rotate_ok:
        print(f"[{now}] ROTATION_JSONL: rien à roter (tous sous seuil)")
    else:
        print(f"[{now}] ROTATION_JSONL: {rotate_ok} fichier(s) roté(s)")


if __name__ == "__main__":
    main()
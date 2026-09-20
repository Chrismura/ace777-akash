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
import re
import shutil
import time
from datetime import datetime, timezone

# ── Cibles : fichiers à croissance illimitée (hors git par décision famille) ──
DEFAUTS = [
    ("/Users/christophe/ace777-test-day1/hulk-mexc/runs/croisement_contexte.jsonl", 100),
    ("/Users/christophe/ace777-test-day1/Index_Maison/strategie/journal_intention.jsonl", 50),
    ("/Users/christophe/ace777-test-day1/Index_Maison/thermo/history.jsonl", 50),
    ("/Users/christophe/ace777-test-day1/Index_Maison/thermo/regime_couleur.jsonl", 50),
    ("/Users/christophe/ace777-test-day1/Index_Maison/data/mempool_vus.jsonl", 50),
    ("/Users/christophe/ace777-test-day1/Index_Maison/data/whales_mouvements.jsonl", 50),
    # [C5] collecteur RWA (GO Christophe 11/09) — rotation dès la création (leçon journal_radar.log)
    ("/Users/christophe/ace777-test-day1/Index_Maison/data/rwa_yields_hist.jsonl", 50),
    # Shadow plancher confirmé (GO direct Christophe 11/09, papier) — même leçon
    ("/Users/christophe/ace777-test-day1/Index_Maison/data/plancher_confirme_hist.jsonl", 50),
    ("/Users/christophe/ace777-test-day1/Index_Maison/data/paternes_btc_hist.jsonl", 50),
    ("/Users/christophe/ace777-test-day1/Index_Maison/data/croisements_indices_hist.jsonl", 50),
    # [C5] collecteur TROUPEAU-INV (GO Christophe 13/09) — rotation dès la création
    ("/Users/christophe/ace777-test-day1/Index_Maison/data/troupeau_inv_hist.jsonl", 50),
    # [C5] collecteur ONCHAIN XRPL (GO Christophe 14/09) — rotation dès la création
    ("/Users/christophe/ace777-test-day1/Index_Maison/data/xrpl_onchain_hist.jsonl", 50),
    # [C5] RADAR AGENTIQUE x402 (GO Christophe 14/09) — rotation dès la création
    ("/Users/christophe/ace777-test-day1/Index_Maison/data/x402_agentic_hist.jsonl", 50),
    # VIGIE marché (19/09) — la leçon « journal_radar.log 3,3 Go » (citée en tête de
    # ce fichier) n'avait jamais été appliquée À CE LOG : la vigie y écrit à chaque
    # tick (append) et il était passé à 3,7 Go. Ajouté à la rotation (seuil 100 Mo).
    ("/Users/christophe/ace777-test-day1/Index_Maison/strategie/journal_radar.log", 100),
    # WATCHDOGS HULK (19/09) — MÊME CANCER, 3e occurrence : watchdog_hulk_ghost.sh lance
    # `nohup python3 … >> runs/*_STDOUT.log 2>&1` (append) pour des process de plusieurs
    # jours. PAPER = 95 Mo, DIGEST = 26 Mo, écrits EN DIRECT, hors rotation. Truncature
    # sans risque (redirection O_APPEND), seuil 50 Mo.
    ("/Users/christophe/ace777-test-day1/hulk-mexc/runs/PAPER_WATCHDOG_STDOUT.log", 50),
    ("/Users/christophe/ace777-test-day1/hulk-mexc/runs/DIGEST_WATCHDOG_STDOUT.log", 50),
]

BACKUP_COUNT = 2
LOG = "/Users/christophe/ace777-test-day1/Index_Maison/scripts/rotation_jsonl.log"

# ── FENÊTRE GARDÉE (réparation 20/09/2026) ──────────────────────────────────
# POURQUOI : la rotation détruisait l'HISTORIQUE RÉCENT, et un consommateur vit de
# cet historique. Prouvé le 20/09 : rotation de croisement_contexte.jsonl à
# 13:12:21Z (113,7 Mo) → le fichier ne contenait plus que 5 heures ; or le signal
# short BTC (hulk-mexc/scripts/short_btc.py) exige ≥ 10 heures distinctes pour
# calculer son score → score nul, détail « historique insuffisant », donc AVEUGLE
# pendant ~10 h — sans que le plist (exit 0), le chien (« short-btc vivant ») ou la
# veilleuse (verte) ne le voient. Un organe qui tourne mais ne peut plus décider
# est un mort qui ne dit pas son nom (famille R14).
#
# RÈGLE : sur un fichier dont un lecteur a besoin d'une fenêtre, on GARDE les
# dernières <heures> et on n'archive QUE ce qui SORT de la fenêtre. 0 = comportement
# historique (tout archiver, tout tronquer) — inchangé pour les logs sans lecteur
# (les .log texte n'ont pas d'horodatage machine-lisible : on ne devine pas).
GARDER_HEURES = {
    "/Users/christophe/ace777-test-day1/hulk-mexc/runs/croisement_contexte.jsonl": 24,
}
# Plafond du fichier VIVANT après rotation (Mo) : la fenêtre gardée ne doit jamais
# recréer le problème d'origine (un JSONL de 286-301 Mo qui bloquait le push GitHub).
# On garde « les 24 dernières heures, MAIS pas plus de X Mo » : le plus contraignant gagne.
GARDER_MAX_MO = 60

_RE_TS = re.compile(rb'"ts"\s*:\s*(\d+(?:\.\d+)?)')

# ── AUDIT DE DÉCOUVERTE (19/09) ─────────────────────────────────────────────
# Le trou de fond n'était pas un fichier précis : c'était d'AVOIR UNE LISTE.
# Une liste ne protège que ce dont on s'est souvenu. Donc on cherche AUSSI tout
# seul les fichiers qui gonflent : > 200 Mo et NON listés ci-dessus = cancer en
# formation, signalé dans thermo/GROS_FICHIERS.json (même si personne n'y pense).
AUDIT_SEUIL_MO = 200
AUDIT_JSON = "/Users/christophe/ace777-test-day1/Index_Maison/thermo/GROS_FICHIERS.json"
AUDIT_RACINE = "/Users/christophe/ace777-test-day1"
AUDIT_EXCLUS = (
    "/.git/", "/.venv", "/venv/", "/site-packages/", "/node_modules/",
    "/_ARCHIVE", "/_archives", "/.Trash",
)


def _decaler_archives(filepath):
    """Décale les archives existantes (.1.gz -> .2.gz, etc.)."""
    for i in range(BACKUP_COUNT, 1, -1):
        src = f"{filepath}.{i-1}.gz"
        dst = f"{filepath}.{i}.gz"
        if os.path.exists(src):
            if os.path.exists(dst):
                os.remove(dst)
            os.rename(src, dst)
    extra = f"{filepath}.{BACKUP_COUNT+1}.gz"
    if os.path.exists(extra):
        os.remove(extra)


def _offset_fenetre(filepath, heures, max_mo=None):
    """Offset (en octets) du premier octet à GARDER.

    Fenêtre = les <heures> dernières heures, BORNÉE à max_mo Mo (le plus contraignant
    gagne). Les lignes sans ts exploitable comptent comme HORS fenêtre : on archive
    plutôt que de deviner. Retourne 0 si tout le fichier est dans la fenêtre.
    """
    limite = time.time() - heures * 3600
    try:
        taille = os.path.getsize(filepath)
    except OSError:
        return 0

    offset_temps = None
    pos = 0
    with open(filepath, "rb") as f:
        for ligne in f:
            if offset_temps is None:
                m = _RE_TS.search(ligne[:400])
                if m:
                    try:
                        if float(m.group(1)) >= limite:
                            offset_temps = pos
                    except ValueError:
                        pass
            pos += len(ligne)
    offset = offset_temps if offset_temps is not None else taille

    if max_mo:
        offset_cap = max(0, taille - int(max_mo * 1024 * 1024))
        if offset_cap > offset:
            # Aligne sur le début de la ligne suivante (on ne coupe jamais une ligne).
            with open(filepath, "rb") as f:
                f.seek(offset_cap)
                bloc = f.read(65536)
            nl = bloc.find(b"\n")
            offset = offset_cap + nl + 1 if nl >= 0 else taille
    return offset


def rotate_file(filepath, seuil_mo, dry_run=False, garder_heures=0):
    """COPYTRUNCATE + gzip. Retourne la taille rotée, ou None.

    garder_heures > 0 → on n'archive QUE la partie ancienne et on GARDE la fenêtre
    récente dans le fichier vivant (voir GARDER_HEURES). garder_heures = 0 →
    comportement historique (tout archiver, tout tronquer).
    """
    try:
        size = os.path.getsize(filepath)
    except OSError:
        return None
    if size <= seuil_mo * 1024 * 1024:
        return None

    try:
        if garder_heures > 0 and not dry_run:
            offset = _offset_fenetre(filepath, garder_heures, GARDER_MAX_MO)
            if offset <= 0:
                # Tout le fichier est encore dans la fenêtre : rien à archiver.
                # (Le plafond GARDER_MAX_MO garantit que ça ne dure pas : dès que la
                #  fenêtre dépasse le plafond, l'offset devient > 0.)
                return None
            _decaler_archives(filepath)
            # 1) L'ANCIEN (hors fenêtre) part en archive gzipée
            with open(filepath, "rb") as fin, gzip.open(f"{filepath}.1.gz", "wb") as fout:
                restant = offset
                while restant > 0:
                    bloc = fin.read(min(1024 * 1024, restant))
                    if not bloc:
                        break
                    fout.write(bloc)
                    restant -= len(bloc)
            # 2) La QUEUE (dans la fenêtre) est réécrite EN PLACE, dans le MÊME inode :
            #    les écrivains gardent leur descripteur ouvert et continuent à la fin
            #    (leçon COPYTRUNCATE : un rename les ferait écrire dans l'inode perdu).
            with open(filepath, "rb") as fin:
                fin.seek(offset)
                queue = fin.read()
            with open(filepath, "r+b") as f:
                f.seek(0)
                f.write(queue)
                f.truncate()
                f.flush()
                os.fsync(f.fileno())
            return size

        _decaler_archives(filepath)

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


def auditer_gros_fichiers():
    """Découvre les fichiers > AUDIT_SEUIL_MO. Retourne la liste + les non couverts."""
    seuil = AUDIT_SEUIL_MO * 1024 * 1024
    couverts = {p for p, _ in DEFAUTS}
    trouves = []
    for racine, dirs, fichiers in os.walk(AUDIT_RACINE):
        dirs[:] = [d for d in dirs if not any(e in os.path.join(racine, d) + "/" for e in AUDIT_EXCLUS)]
        for nom in fichiers:
            if nom.endswith(".gz"):
                continue
            chemin = os.path.join(racine, nom)
            try:
                taille = os.path.getsize(chemin)
            except OSError:
                continue
            if taille > seuil:
                trouves.append({
                    "chemin": chemin,
                    "mo": round(taille / 1024 / 1024, 1),
                    "couvert": chemin in couverts,
                })
    trouves.sort(key=lambda x: -x["mo"])
    non_couverts = [t for t in trouves if not t["couvert"]]
    return trouves, non_couverts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seuil", type=int, default=None, help="seuil Mo (défaut : par fichier)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    now = datetime.now(timezone.utc).isoformat()
    rotate_ok = 0
    for path, seuil_defaut in DEFAUTS:
        seuil = args.seuil if args.seuil else seuil_defaut
        garder = GARDER_HEURES.get(path, 0)
        size = rotate_file(path, seuil, dry_run=args.dry_run, garder_heures=garder)
        if size is not None:
            rotate_ok += 1
            fenetre = f", fenêtre={garder} h GARDÉE (max {GARDER_MAX_MO} Mo)" if garder else ""
            line = f"[{now}] rotation: {path} ({size} octets -> .1.gz, backups={BACKUP_COUNT}{fenetre})"
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

    # ── Audit de découverte : ce qui gonfle SANS être dans la liste ──────────
    trouves, non_couverts = auditer_gros_fichiers()
    etat = {
        "ts": now,
        "seuil_mo": AUDIT_SEUIL_MO,
        "fichiers": trouves,
        "non_couverts": [t["chemin"] for t in non_couverts],
    }
    try:
        import json as _json
        tmp = AUDIT_JSON + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            _json.dump(etat, f, ensure_ascii=False, indent=2)
        os.replace(tmp, AUDIT_JSON)
    except OSError:
        pass
    if non_couverts:
        line = (f"[{now}] AUDIT_GROS_FICHIERS: {len(non_couverts)} fichier(s) > {AUDIT_SEUIL_MO} Mo "
                f"HORS ROTATION -> " + ", ".join(f"{t['chemin']} ({t['mo']} Mo)" for t in non_couverts[:5]))
        print(line)
        if not args.dry_run:
            try:
                with open(LOG, "a", encoding="utf-8") as f:
                    f.write(line + "\n")
            except OSError:
                pass
    else:
        print(f"[{now}] AUDIT_GROS_FICHIERS: 0 fichier > {AUDIT_SEUIL_MO} Mo hors rotation "
              f"({len(trouves)} gros fichier(s) vu(s), tous expliqués)")


if __name__ == "__main__":
    main()
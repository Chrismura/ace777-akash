#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
heartbeats.py — HEARTBEATS PAR SERVICE (exigence famille, PAA-ACE777 20/08).

Ajout 1 du protocole unique (JUGE + ULTRA) : le double check launchctl+pgrep
détecte les process morts mais PAS les « zombies fonctionnels » (process
vivant, launchd OK, mais figé dans une boucle — sortie plus produite).
C'est l'angle mort restant identifié au tour 2.

Mécanisme :
- Pour chaque service critique, vérifie TROIS conditions :
    (a) plist chargée (launchctl list)           -> pas un mort
    (b) process répond (pgrep -fl)               -> pas un fantôme
    (c) sortie de vie FRAÎCHE (fichier propre)   -> pas un zombie fonctionnel
- Si les 3 sont vraies : écrit `data/heartbeat/[service].ts` (timestamp epoch).
- Si le process vit mais la sortie est figée : N'écrit PAS (le .ts vieillit)
  et signale ZOMBIE_FONCTIONNEL — la veille de dégradation et le DMS le
  détectent via la fraîcheur du .ts.

Sortie : Index_Maison/etat/heartbeats.json (lu par veille_degradation/sante_index).
Stdlib uniquement, écriture atomique, kill-switch, idempotent.
"""
import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

HOME = Path.home()
ROOT = HOME / "ace777-test-day1"
IM = ROOT / "Index_Maison"
HB_DIR = IM / "data" / "heartbeat"
ETAT_DIR = IM / "etat"
ETAT_JSON = ETAT_DIR / "heartbeats.json"
STOP_ALL = IM / "STOP_ALL"
STOP_STRAT = IM / "strategie" / "STOP"

# Chaque service : (label, label launchd, pattern pgrep, fichier de vie,
#                    âge max s, permanent)
#   permanent=True  : daemon qui tourne EN CONTINU (vigie) -> pgrep obligatoire
#   permanent=False : service à CYCLE (StartInterval) -> s'exécute, écrit, sort ;
#                     la vie = fraîcheur de sa sortie, pas un process permanent
SERVICES = [
    # vigie marché : daemon continu, sa « vie » = journal_radar.log à chaque tick
    ("vigie", "com.ace777.vigie-live", "vigie_live.py",
     IM / "strategie" / "journal_radar.log", 300, True),
    # brique veille : à cycle (60 s), sa vie = son rapport d'état
    ("veille", "com.ace777.veille-degradation", "veille_degradation.py",
     IM / "etat" / "veille_degradation_etat.json", 300, False),
    # Dead Man's Switch : à cycle (60 s), sa vie = son rapport
    ("dms", "com.ace777.dms-veille", "dms_veille.py",
     IM / "data" / "alertes" / "DMS_VEILLE.json", 300, False),
    # pré-vol des index : à cycle (5 min), sa vie = son rapport
    ("sante", "com.ace777.sante-index", "sante_index.py",
     IM / "thermo" / "sante_index.json", 600, False),
    # superviseur core : à CYCLE (launchd StartInterval — les checks
    # s'exécutent puis se terminent : "VIGIE: fin", "QUOTAS: fin"), sa vie =
    # son log (/tmp, LOG_CORE défini ligne 25 de superviseur_core.sh)
    ("superviseur_core", "com.ace777.superviseur-core", "superviseur_core.sh",
     Path("/tmp") / "superviseur-core.log", 1800, False),
    # baleines : à cycle (5 min), sa vie = scan frais
    ("whales", "com.ace777.whales", "surveiller_whales.py",
     IM / "data" / "whales_scan_latest.json", 900, False),
]


def check_kill_switch():
    for s in (STOP_ALL, STOP_STRAT):
        if s.exists():
            print(f"[HB] Kill-switch actif : {s} — sortie.", file=sys.stderr)
            sys.exit(0)


def ecrire_atomique(chemin: Path, data: dict):
    check_kill_switch()
    chemin.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(chemin.parent), text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        os.replace(tmp, chemin)
    except Exception:
        if os.path.exists(tmp):
            try:
                os.remove(tmp)
            except Exception:
                pass
        raise


def etat_service(svc):
    """svc = (label, label_launchd, pgrep_pattern, fichier_vie, age_max_s)."""
    label, label_ld, pgrep_pat, vie_path, age_max, permanent = svc
    # (a) plist chargée ?
    try:
        out = subprocess.run(["launchctl", "list"], capture_output=True,
                             text=True, timeout=5)
        plist_ok = label_ld in (out.stdout or "")
    except Exception:
        plist_ok = False
    if not plist_ok:
        return False, f"plist {label_ld} NON CHARGÉE"

    # (b) process répond ? (obligatoire pour les daemons PERMANENTS ;
    #     pour les services à CYCLE, le process s'exécute et sort — on ne
    #     teste pas un process permanent, on teste la fraîcheur de la sortie)
    if svc[5]:  # permanent
        try:
            out = subprocess.run(["pgrep", "-fl", pgrep_pat], capture_output=True,
                                 text=True, timeout=5)
            proc_ok = pgrep_pat in (out.stdout or "")
        except Exception:
            proc_ok = False
        if not proc_ok:
            return False, f"process {pgrep_pat} introuvable (plist chargée mais mort)"

    # (c) sortie de vie fraîche ? (le vrai test anti-zombie)
    if not vie_path.exists():
        return False, f"process vivant mais fichier de vie ABSENT ({vie_path.name})"
    age = time.time() - vie_path.stat().st_mtime
    if age > age_max:
        return False, (f"ZOMBIE FONCTIONNEL : process vivant mais sortie figée "
                       f"({age:.0f}s > {age_max}s) — {vie_path.name}")
    return True, f"OK (vie {int(age)}s)"


def main():
    check_kill_switch()
    now = int(time.time())
    HB_DIR.mkdir(parents=True, exist_ok=True)
    resultats = {}
    zombies = []
    for svc in SERVICES:
        ok, detail = etat_service(svc)
        resultats[svc[0]] = {"ok": ok, "detail": detail}
        if ok:
            # battement écrit SEULEMENT si vivant ET productif
            f = HB_DIR / f"{svc[0]}.ts"
            fd, tmp = tempfile.mkstemp(dir=str(HB_DIR), text=True)
            with os.fdopen(fd, "w") as fh:
                fh.write(str(now))
            os.replace(tmp, f)
        else:
            zombies.append(f"{svc[0]}: {detail}")

    rapport = {
        "timestamp": now,
        "date": time.strftime("%Y-%m-%d %H:%M:%S"),
        "source": "heartbeats (PAA-ACE777 ajout 1, 20/08)",
        "services": resultats,
        "zombies_fonctionnels": zombies,
        "statut": "ALERTE" if zombies else "SAIN",
    }
    ecrire_atomique(ETAT_JSON, rapport)
    if zombies:
        print(f"[HB] ALERTE — {len(zombies)} service(s) : {' ; '.join(zombies)[:200]}")
    else:
        print(f"[HB] SAIN — {len(resultats)}/{len(resultats)} services battent.")


if __name__ == "__main__":
    main()

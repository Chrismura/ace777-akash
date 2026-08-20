#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
veille_degradation.py — BRIQUE « DÉTECTION DE DÉGRADATION » générique (20/08).

Issue de la méta-analyse des 484 audits (INDEX_AUDITS_ET_META_ANALYSE_2026-08-20.md)
: le pattern dominant est la DÉGRADATION SILENCIEUSE — chaque organe peut tomber ou
se tromper sans alerte, avec une fausse sécurité issue de mesures mal calibrées.
Le CODEUR (via hub) a produit la v1 ; Buffy a corrigé les chemins, le bug `true`,
et intégré les 4 classes + les leçons du 20/08.

Vérifie en continu (launchd, ~60 s) :
  (a) plists critiques CHARGÉES (launchctl)            — classe 2 (garde-fou inactif)
  (b) fichiers heartbeat/état FRAIS (st_mtime ≤ seuil) — classe 1 (dégradation silencieuse)
  (c) indicateurs dans leur plage de calibration       — classe 3 (fausse sécurité)
Sortie : Index_Maison/etat/veille_degradation_etat.json — lu par sante_index/cockpit.
Stdlib uniquement, écriture atomique, kill-switch, idempotent, zéro dépendance.
"""
import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

# --- CONFIGURATION (chemins réels vérifiés 20/08) ---------------------------
HOME = Path.home()
ROOT = HOME / "ace777-test-day1"
INDEX = ROOT / "Index_Maison"
STRATEGIE = INDEX / "strategie"
ETAT_DIR = INDEX / "etat"
ETAT_JSON = ETAT_DIR / "veille_degradation_etat.json"

STOP_ALL = INDEX / "STOP_ALL"
STOP_STRAT = STRATEGIE / "STOP"
LAUNCH_AGENTS = HOME / "Library" / "LaunchAgents"

# (a) Plists critiques (classe 2 — le trou du 19/08 : écrites mais jamais chargées)
PLISTS_CRITIQUES = [
    "com.ace777.vigie-live",
    "com.ace777.superviseur-process",
    "com.ace777.superviseur-core",
    "com.ace777.bloc-privatise",
    "com.ace777.macro-tempete",
    "com.ace777.cpfp",
    "com.ace777.whales",
    "com.ace777.pont-onchain",
    "com.ace777.sante-index",
    "com.ace777.veille-degradation",  # la brique se surveille elle-même (leçon 8 : vérifier même ses propres garde-fous)
]

# (b) Heartbeats / fichiers d'état + âge max (secondes) — classe 1
HEARTBEATS = {
    "journal_radar": {"path": STRATEGIE / "journal_radar.log", "seuil": 300},   # vigie marché
    "live_json": {"path": INDEX / "thermo" / "live.json", "seuil": 900},        # thermo
    "mission_json": {"path": INDEX / "cockpit" / "mission.json", "seuil": 900}, # run ACE
    "macro_tempete": {"path": ROOT / "runs" / "macro_tempete.json", "seuil": 300},
}

# (c) Indicateurs + plage de calibration valide — classe 3 (fausse sécurité)
#     Le taux fantôme dense (60-120 s) observé le 20/08 : 0,5-8,3 % → plage saine.
INDICATEURS = {
    "taux_fantome": {
        "path": INDEX / "data" / "bloc_privatise.json",
        "cle": "taux_fantome",
        "min": 0.0,
        "max": 25.0,   # au-delà = soit bruit (mauvaise résolution) soit anomalie réelle
        "nb": "indicateur blocs privatisés (résolution 120 s)",
    },
}


def check_kill_switch():
    for s in (STOP_ALL, STOP_STRAT):
        if s.exists():
            print(f"[VEILLE_DEG] Kill-switch actif : {s} — sortie.", file=sys.stderr)
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


def verifier_plists() -> dict:
    """(a) Classe 2 — les plists attendues sont-elles réellement chargées ?"""
    try:
        out = subprocess.run(["launchctl", "list"], capture_output=True,
                             text=True, timeout=5)
        lignes = out.stdout or ""
    except Exception as e:
        return {p: f"ERREUR_EXEC {e}" for p in PLISTS_CRITIQUES}
    res = {}
    for p in PLISTS_CRITIQUES:
        res[p] = "OK" if p in lignes else "NON_CHARGEE_ALERTE"
    return res


def verifier_heartbeats() -> dict:
    """(b) Classe 1 — les fichiers de vie sont-ils frais ?"""
    res = {}
    now = time.time()
    for nom, cfg in HEARTBEATS.items():
        p = cfg["path"]
        if not p.exists():
            res[nom] = "ABSENT_ALERTE"
            continue
        age = now - p.stat().st_mtime
        res[nom] = (f"OK ({int(age)}s)" if age <= cfg["seuil"]
                    else f"STALE_ALERTE ({int(age)}s > {cfg['seuil']}s)")
    return res


def verifier_indicateurs() -> dict:
    """(c) Classe 3 — les indicateurs actifs sont-ils dans leur plage saine ?"""
    res = {}
    for nom, cfg in INDICATEURS.items():
        p = cfg["path"]
        if not p.exists():
            res[nom] = "ABSENT"
            continue
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
            val = data.get(cfg["cle"])
            if val is None:
                res[nom] = "CLE_INTROUVABLE"
            elif not (cfg["min"] <= val <= cfg["max"]):
                res[nom] = (f"HORS_PLAGE_ALERTE ({cfg['nb']} = {val}, "
                            f"attendu [{cfg['min']}, {cfg['max']}])")
            else:
                res[nom] = f"OK ({val})"
        except Exception as e:
            res[nom] = f"ERREUR_LECTURE {e}"
    return res


def main():
    check_kill_switch()
    rapport = {
        "timestamp": int(time.time()),
        "date": time.strftime("%Y-%m-%d %H:%M:%S"),
        "source": "veille_degradation (brique méta-analyse 20/08)",
        "plists": verifier_plists(),
        "heartbeats": verifier_heartbeats(),
        "indicateurs": verifier_indicateurs(),
    }
    alerte = False
    for cat in ("plists", "heartbeats", "indicateurs"):
        for v in rapport[cat].values():
            if "ALERTE" in str(v):
                alerte = True
    rapport["statut_global"] = "ALERTE_DEGRADATION_SILENCIEUSE" if alerte else "SAIN"
    ecrire_atomique(ETAT_JSON, rapport)
    print(f"[VEILLE_DEG] statut_global={rapport['statut_global']} "
          f"(plists {sum(1 for v in rapport['plists'].values() if v=='OK')}/"
          f"{len(rapport['plists'])})")


if __name__ == "__main__":
    main()

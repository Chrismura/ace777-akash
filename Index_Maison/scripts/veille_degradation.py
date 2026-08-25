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
SCRIPTS_DIR = INDEX / "scripts"
ANALYSES_DIR = INDEX / "thermo" / "analyses"

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
    "com.ace777.dms-veille",          # le Dead Man's Switch qui surveille la brique (famille 20/08 : qui surveille la surveillante ?)
    # CHAÎNE D'APPRENTISSAGE (ajout 23/08 — la brique couvrait le trading mais PAS
    # l'apprentissage : la coupure des briefs du 19/08 avait emporté la production
    # des analyses + le professeur SANS que personne ne le voie pendant 5 jours).
    "com.ace777.analyste-cadence",    # production des analyses Cortana (08:30 + 20:30)
    "com.ace777.discipline-quotidienne",  # le professeur (re-note + alerte boucle affamée)
    "com.ace777.scoreur-registre",    # le scoreur du registre mécanique (07:30) — ajout 23/08
]

# (b) Heartbeats / fichiers d'état + âge max (secondes) — classe 1
HEARTBEATS = {
    "journal_radar": {"path": STRATEGIE / "journal_radar.log", "seuil": 300},   # vigie marché
    "live_json": {"path": INDEX / "thermo" / "live.json", "seuil": 900},        # thermo
    "mission_json": {"path": INDEX / "cockpit" / "mission.json", "seuil": 900}, # run ACE
    "macro_tempete": {"path": ROOT / "runs" / "macro_tempete.json", "seuil": 300},
    # Chaîne d'apprentissage (ajout 23/08) : si aucune analyse Cortana depuis 48h
    # → STALE_ALERTE (c'était l'alerte "boucle affamée" du professeur, coupée 19→23/08).
    "analyses_cortana": {"path": ANALYSES_DIR, "seuil": 48 * 3600},
    # justesse_v2.json : le professeur doit être re-calculé chaque jour (07:15).
    "justesse_v2": {"path": SCRIPTS_DIR / "justesse_v2.json", "seuil": 36 * 3600},
    # JUSTESSE_REGISTRE.json : le scoreur du registre doit tourner chaque jour
    # (07:30) — s'il meurt, on le voit (ajout 23/08, plus de mort silencieuse).
    "justesse_registre": {"path": STRATEGIE / "JUSTESSE_REGISTRE.json", "seuil": 48 * 3600},  # 48h (scoreur 1x/jour 07:30, couvre 2 nuits de sleep)
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


def verifier_pattern_boucle() -> dict:
    """(d) Classe 4 — detection du pattern KeepAlive+intervalle (ajout 23/08).

    Decouverte du 23/08 : le plist com.ace777.observatoire avait KeepAlive=true
    duplique DANS StartCalendarInterval -> launchd relancait le script en boucle
    infinie (toutes les ~2 min au lieu de 1x/jour), qui reecrivait providers.json
    a chaque cycle (987 rollbacks, fichier gonfle 368 Ko -> 377 Ko, correctifs
    ecrases). La famille (audit 23/08, 4/4) demande une detection automatique :
    un script one-shot (StartInterval/StartCalendarInterval) ne doit JAMAIS avoir
    KeepAlive, sinon boucle infinie silencieuse.
    Exception legitime : daemon a boucle interne (superviseur-core) — on ne peut
    pas le detecter ici, donc on liste les exclusions connues.
    """
    # Daemons legitimes a boucle interne (KeepAlive voulu) : ne PAS alerter.
    # superviseur-core: boucle while true interne, KeepAlive=relance apres crash.
    EXCLUS_DAEMONS = {"com.ace777.superviseur-core"}
    try:
        import plistlib
    except Exception:
        return {"pattern_boucle": "ERREUR_IMPORT_PLISTLIB"}
    if not LAUNCH_AGENTS.exists():
        return {"pattern_boucle": "DOSSIER_ABSENT"}
    suspects = []
    for pf in sorted(LAUNCH_AGENTS.glob("com.ace777.*.plist")):
        try:
            with open(pf, "rb") as f:
                d = plistlib.load(f)
        except Exception:
            suspects.append((pf.name, "XML_ILLISIBLE_ALERTE"))
            continue
        label = d.get("Label", pf.name)
        if label in EXCLUS_DAEMONS:
            continue
        keep = d.get("KeepAlive")
        si = d.get("StartInterval")
        sci = d.get("StartCalendarInterval")
        if keep and (si or sci):
            suspects.append((label, "KEEPALIVE+INTERVALLE_ALERTE"))
    if suspects:
        return {"pattern_boucle": "; ".join(f"{l} ({r})" for l, r in suspects)}
    return {"pattern_boucle": "OK (aucun KeepAlive+intervalle)"}


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
            # FIX 23/08 : ne PAS alerter sur un indicateur que le détecteur
            # lui-même marque « non fiable » (carnet en reconstitution / artefact
            # de mesure, ex. taux 100 % sur 1 snapshot). On le note mais on ne
            # crie pas — évite les fausses alertes pendant les interruptions de
            # collecte légitimes (tests, redémarrages).
            if data.get("taux_non_fiable") is True:
                res[nom] = f"OK_NON_FIABLE ({cfg['nb']} = {val}, marqué non fiable par le détecteur — ignoré)"
            elif val is None:
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
        "pattern_boucle": verifier_pattern_boucle(),
    }
    alerte = False
    for cat in ("plists", "heartbeats", "indicateurs", "pattern_boucle"):
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

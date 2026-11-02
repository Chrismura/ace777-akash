#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nom du module : disjoncteur.py
Projet       : ACE777 (URGENCE 1 - Le Disjoncteur Unique)Rôle       : Juge & Risk Guardian (Python pur, stdlib, déterministe, sans LLM).
               - Bridage dynamique des tailles d'ordres (hard cap à la volée).
               - Coupure d'urgence (Mur de Fer) sur seuil MESURÉ (k × σ_20j,
                 §73 : les fixes 11,67 %/25 % n'ont jamais tiré en 88 j).
               - AUCUN seuil en dur : mur_mesure.json (quotidien) + preuve de vie.
                 Cache stale > 26 h → SANS_MESURE (pas de coupe, R11).
               - Écriture atomique, verrouillage global (STOP_ALL), persistance JSON/JSONL.
Vérifié      : 16/08 par Buffy (superviseur) — 2 bugs de la réponse codeur corrigés :
               (1) import pathlib cassé, (2) chemin en dur faux (/Users/macbookpro -> détection auto).
"""

import os
import sys
import json
import time
import argparse
import tempfile
from datetime import datetime, timezone
from pathlib import Path

# Chemins ancrés sur la structure ACE777 (détection auto, pas de chemin en dur)
_BASE_DIR = Path(__file__).resolve().parent.parent  # .../Index_Maison
if not (_BASE_DIR / "strategie").exists():
    _BASE_DIR = Path.home() / "ace777-test-day1" / "Index_Maison"
BASE_DIR = _BASE_DIR
STRATEGIE_DIR = BASE_DIR / "strategie"
CONFIG_PATH = STRATEGIE_DIR / "disjoncteur_config.json"
STATE_PATH = STRATEGIE_DIR / "disjoncteur_state.json"
HISTORY_PATH = STRATEGIE_DIR / "disjoncteur_history.jsonl"
# FIX 09/09 : DEUX conventions STOP_ALL coexistaient dans la maison — le disjoncteur
# écrivait dans strategie/ alors que HULK (paper_diprip.py:83) et sante_index lisent
# la RACINE Index_Maison/. Résultat : même branché le 16/08, le Mur de Fer ne couvrait
# pas HULK. Désormais : pose + lecture + réarmement sur LES DEUX chemins.
STOP_ALL_PATH = STRATEGIE_DIR / "STOP_ALL"
STOP_ALL_ROOT_PATH = BASE_DIR / "STOP_ALL"
STOP_PATH = STRATEGIE_DIR / "STOP"
REARMER_FILE = STRATEGIE_DIR / "REARMER_DISJONCTEUR"

DEFAULT_CONFIG = {
    # §73 — ZÉRO SEUIL EN DUR (R26 : aucun défaut silencieux). k vit UNIQUEMENT
    # dans disjoncteur_config.json avec son k_origine ; absent -> le Mur ne se
    # calcule pas (SANS_MESURE). Les fixes pct_journalier/max_global_dd_pct /
    # plafond_trade_pct sont archivés (.bak-avant-mesure-20261102) et IGNORÉS.
    "mode": "obeir",
    "seed_usdt": 150,
    "cloturer_sur_mur_de_fer": 0
}
MUR_MESURE_PATH = BASE_DIR / "thermo" / "mur_mesure.json"
M_KELLY_LIVE_PATH = BASE_DIR / "thermo" / "m_kelly_live.json"
MUR_FRAIS_MAX_H = 26.0
M_KELLY_FRAIS_MAX_H = 30.0


def atomic_write(file_path, data):
    """Écriture atomique robuste via mkstemp + os.replace (jamais de fichier corrompu)."""
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(dir=str(file_path.parent), prefix="tmp_atomic_")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            if isinstance(data, (dict, list)):
                json.dump(data, f, indent=2, ensure_ascii=False)
            else:
                f.write(str(data))
        os.replace(tmp_path, file_path)
    except Exception as e:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
        raise RuntimeError("Échec écriture atomique sur %s: %s" % (file_path, e))


def load_json(file_path, default=None):
    if default is None:
        default = {}
    path = Path(file_path)
    if not path.exists():
        return default
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default


def get_config():
    cfg = load_json(CONFIG_PATH, DEFAULT_CONFIG)
    for k, v in DEFAULT_CONFIG.items():
        if k not in cfg:
            cfg[k] = v
    return cfg


def is_stopped():
    """Vrai si un verrou global est présent (STOP_ALL / STOP) ou si déjà déclenché."""
    if STOP_ALL_PATH.exists() or STOP_ALL_ROOT_PATH.exists() or STOP_PATH.exists():
        return True
    etat = load_json(STATE_PATH, {})
    return bool(etat.get("declenche", False))


def _frais_depuis_heures(chemin, max_h):
    """Vrai si le fichier existe et est plus frais que max_h (preuve de vie)."""
    try:
        age_h = (time.time() - os.path.getmtime(str(chemin))) / 3600.0
        return age_h <= max_h
    except Exception:
        return False


def _mur_mesure():
    """Seuil mesuré du jour, ou None si pas de preuve de vie (anti-aveugle)."""
    try:
        if not _frais_depuis_heures(MUR_MESURE_PATH, MUR_FRAIS_MAX_H):
            return None
        mur = json.loads(MUR_MESURE_PATH.read_text(encoding="utf-8"))
        if float(mur.get("seuil_jour_pct", 0)) <= 0:
            return None
        return mur
    except Exception:
        return None


def _m_kelly_live():
    """Plafonds S2 du jour, ou None si pas de preuve de vie."""
    try:
        if not _frais_depuis_heures(M_KELLY_LIVE_PATH, M_KELLY_FRAIS_MAX_H):
            return None
        return json.loads(M_KELLY_LIVE_PATH.read_text(encoding="utf-8"))
    except Exception:
        return None


def _historiser_sans_mesure():
    """Trace le refus de couper sans mesure (pas de silence)."""
    try:
        with open(HISTORY_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps({"event": "SANS_MESURE",
                                "ts": datetime.now(timezone.utc).isoformat(),
                                "raison": "mur_mesure.json stale/absent : pas de coupe"}) + "\n")
    except Exception:
        pass


def declencher_mur_de_fer(raison, perte_pct):
    """Active le Mur de Fer : verrous, état, alerte cockpit, historique."""
    now = datetime.now(timezone.utc).isoformat()
    config = get_config()
    STRATEGIE_DIR.mkdir(parents=True, exist_ok=True)
    STOP_ALL_PATH.touch(exist_ok=True)
    STOP_ALL_ROOT_PATH.touch(exist_ok=True)  # convention HULK + sante_index
    if REARMER_FILE.exists():
        REARMER_FILE.unlink()
    etat = {
        "declenche": True,
        "raison": raison,
        "ts": now,
        "perte_journaliere_pct": perte_pct,
        "cloture_effectuee": bool(config.get("cloturer_sur_mur_de_fer", 0)),
    }
    atomic_write(STATE_PATH, etat)
    atomic_write(STRATEGIE_DIR / ".urgent_alert.json", {
        "niveau": "CRITIQUE",
        "module": "disjoncteur.py",
        "message": "MUR DE FER DÉCLENCHÉ : %s" % raison,
        "ts": now,
    })
    with open(HISTORY_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps({"event": "MUR_DE_FER_DECLENCHE", "ts": now,
                            "raison": raison, "perte": perte_pct}) + "\n")
    print("[ALERTE ROUGE ACE777] MUR DE FER DÉCLENCHÉ : %s" % raison, file=sys.stderr)


def verifier_et_brigader(taille_proposee, capital_total, perte_journaliere_pct):
    """
    Point d'entrée unique : état disjoncteur, Mur de Fer, bridage dynamique.
    Déterministe, sans LLM. Ne crée JAMAIS d'ordre (C3) : réduit ou rejette.
    """
    config = get_config()
    now = datetime.now(timezone.utc).isoformat()
    etat_actuel = load_json(STATE_PATH, {
        "declenche": False, "raison": "", "ts": now, "perte_journaliere_pct": 0.0})

    if etat_actuel.get("declenche", False) or is_stopped():
        return {
            "autorise": False,
            "taille_corrigee": 0.0,
            "raison": "DISJONCTEUR OUVERT (Mur de Fer actif): %s"
                      % etat_actuel.get("raison", "STOP global"),
            "declenche": True,
        }

    mur = _mur_mesure()
    if mur is None:
        # R11 + anti-aveugle (§73) : sans mesure fraîche, on ne coupe PAS.
        # Le rituel crie sur la fraîcheur — pas de silence, pas de coupe aveugle.
        _historiser_sans_mesure()
        return {
            "autorise": True,
            "taille_corrigee": float(taille_proposee),
            "bride": False,
            "raison": "SANS_MESURE (mur_mesure.json stale/absent) : pas de coupe "
                      "sans mesure (R11) — rituel alerté",
            "declenche": False,
        }
    seuil_journalier = float(mur["seuil_jour_pct"])
    if perte_journaliere_pct >= seuil_journalier:
        raison = ("Mur MESURÉ atteint: perte %.2f%% ≥ k×σ=%.2f%% "
                  "(k=%.1f, σ20j=%.2f%%, equity=%s$)" %
                  (perte_journaliere_pct, seuil_journalier, mur["k"],
                   mur["sigma_20j_pct"], mur["equity"]))
        declencher_mur_de_fer(raison, perte_journaliere_pct)
        return {"autorise": False, "taille_corrigee": 0.0, "raison": raison, "declenche": True}

    # Cap per-trade MESURÉ : plus grosse cible S2 du jour (m_kelly_live.json).
    # Stale/absent -> pas de cap (fail-open) + note (le rituel surveille).
    mk = _m_kelly_live()
    taille_proposee = float(taille_proposee)
    if mk is not None and mk.get("maxS2"):
        plafond_capital = float(mk["maxS2"])
        taille_autorisee = min(taille_proposee, plafond_capital)
        bride = taille_autorisee < taille_proposee
        raison = ("OK" if not bride else
                  "Bridé par le plafond mesuré (maxS2=%.2f$ du m-mètre)" % plafond_capital)
    else:
        taille_autorisee, bride = taille_proposee, False
        raison = "OK (pas de cap : m_kelly_live.json stale/absent — rituel alerté)"
    return {
        "autorise": True,
        "taille_corrigee": round(taille_autorisee, 4),
        "bride": bride,
        "raison": raison,
        "declenche": False,
    }


def rearmer():
    """Réarmement MANUEL exclusif (jamais auto)."""
    now = datetime.now(timezone.utc).isoformat()
    for p in [STOP_ALL_PATH, STOP_ALL_ROOT_PATH, STOP_PATH, REARMER_FILE]:
        if p.exists():
            p.unlink()
    atomic_write(STATE_PATH, {
        "declenche": False, "raison": "Réarmement manuel effectué", "ts": now,
        "perte_journaliere_pct": 0.0})
    with open(HISTORY_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps({"event": "DISJONCTEUR_REARME", "ts": now}) + "\n")
    print("[ACE777] Disjoncteur réarmé avec succès à %s." % now)


def main():
    parser = argparse.ArgumentParser(description="Disjoncteur Unique ACE777 (Juge & Risk Guardian)")
    parser.add_argument("--check", action="store_true", help="État global (0 = OK, 1 = déclenché)")
    parser.add_argument("--bridage", type=float, help="Taille d'ordre à tester")
    parser.add_argument("--capital", type=float, default=10000.0, help="Capital de référence")
    parser.add_argument("--perte-jour", type=float, default=0.0, help="Perte journalière en %")
    parser.add_argument("--rearmer", action="store_true", help="Réarme manuellement")
    parser.add_argument("--etat", action="store_true", help="État courant en JSON")
    args = parser.parse_args()

    STRATEGIE_DIR.mkdir(parents=True, exist_ok=True)
    if not CONFIG_PATH.exists():
        atomic_write(CONFIG_PATH, DEFAULT_CONFIG)

    if args.rearmer:
        rearmer()
        sys.exit(0)
    if args.etat:
        print(json.dumps(load_json(STATE_PATH, {"declenche": False, "raison": "Initié"}), indent=2))
        sys.exit(0)
    if args.check:
        etat = load_json(STATE_PATH, {"declenche": False})
        if is_stopped() or etat.get("declenche", False):
            print(json.dumps({"statut": "DECLENCHE", "details": etat}))
            sys.exit(1)
        print(json.dumps({"statut": "OK"}))
        sys.exit(0)
    if args.bridage is not None:
        res = verifier_et_brigader(args.bridage, args.capital, args.perte_jour)
        print(json.dumps(res, indent=2))
        sys.exit(0 if res["autorise"] else 1)

    parser.print_help()


if __name__ == "__main__":
    main()

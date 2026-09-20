#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nom du module : nourrir_disjoncteur.py
Projet       : ACE777 (Disjoncteur C7 — le capteur qui lui donne des oreilles)
Rôle         : Le disjoncteur est DÉTERMINISTE ET SOURD (design 16/08) : il ne mesure
               rien lui-même, il exécute. Ce module mesure la perte journalière réelle
               de HULK et la lui porte. Sans ce module, brancher le disjoncteur ne
               recrée qu'une illusion de protection (leçon 09/09).
Source de vérité : .hulk_resume_pointer → state live HULK (« pnl_total », réalisé pur).
Contrat      :
  - Perte journalière = max(0, pnl_pivot_du_jour − pnl_actuel) / seed × 100
  - Pivot du jour = 1er state vu après 00:00 UTC (persisté atomiquement).
  - mode=obeir (défaut) : perte ≥ pct_journalier → MUR DE FER via le disjoncteur
    (STOP_ALL + état + historique + alerte). mode=OBS : mesure + alerte, jamais de coupe.
  - Fail-safe : HULK muet > STALE_S → aucune mesure, AUCUNE invention — événement
    MESURE_IMPOSSIBLE. Jamais de coupure sur données absentes (C3).
  - Ne crée JAMAIS d'ordre (C3). Réarmement MANUEL uniquement (--rearmer du disjoncteur).
"""
import os
import sys
import json
import time
import tempfile
from datetime import datetime, timezone
from pathlib import Path

_ROOT = Path.home() / "ace777-test-day1"
IM = _ROOT / "Index_Maison"
SCRIPTS = IM / "scripts"
STRATEGIE_DIR = IM / "strategie"
RUNS = _ROOT / "hulk-mexc" / "runs"
POINTER = RUNS / ".hulk_resume_pointer"
PIVOT_PATH = STRATEGIE_DIR / "disjoncteur_pivot.json"
HISTORY_PATH = STRATEGIE_DIR / "disjoncteur_history.jsonl"
CONFIG_PATH = STRATEGIE_DIR / "disjoncteur_config.json"
sys.path.insert(0, str(SCRIPTS))

STALE_S = 180.0        # state HULK muet au-delà → mesure impossible (fail-safe)
RATE_LIMIT_S = 600.0   # max 1 événement MESURE / 10 min si rien ne change


def atomic_write_json(file_path, data):
    """Écriture atomique (même pattern que le disjoncteur : mkstemp + os.replace)."""
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(file_path.parent), prefix="tmp_nourrisseur_")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        os.replace(tmp, file_path)
    except Exception:
        if os.path.exists(tmp):
            os.remove(tmp)
        raise


def load_json(path, default=None):
    if default is None:
        default = {}
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception:
        return default


def lire_state_live():
    """State live HULK via le pointeur canonique ; filet = state le plus récent."""
    nom = ""
    try:
        nom = POINTER.read_text(encoding="utf-8").strip()
    except Exception:
        nom = ""
    chemin = None
    if nom:
        p = RUNS / nom
        if p.exists():
            chemin = p
    if chemin is None:
        try:
            cands = sorted(RUNS.glob("*_state.json"),
                           key=lambda p: p.stat().st_mtime, reverse=True)
            if cands:
                chemin = cands[0]
        except Exception:
            return None
    if chemin is None:
        return None
    try:
        st = json.loads(chemin.read_text(encoding="utf-8"))
    except Exception:
        return None
    return {
        "path": chemin.name,
        "pnl_total": float(st.get("pnl_total") or 0.0),
        "age_s": time.time() - chemin.stat().st_mtime,
    }


def ecrire_histoire(event, rate_limit=RATE_LIMIT_S):
    """Journalise dans l'historique du disjoncteur, avec garde anti-tempête."""
    try:
        derniere = ""
        if HISTORY_PATH.exists():
            with open(HISTORY_PATH, "r", encoding="utf-8") as f:
                for derniere in f:
                    pass  # dernière ligne non vide
        if derniere.strip():
            try:
                prec = json.loads(derniere)
                same = prec.get("event") == event.get("event")
                if same and prec.get("statut") == event.get("statut"):
                    t_prec = datetime.fromisoformat(prec.get("ts"))
                    if (datetime.now(timezone.utc) - t_prec).total_seconds() < rate_limit:
                        return  # rien ne change → on n'écrit pas
            except Exception:
                pass
        with open(HISTORY_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(event, ensure_ascii=False) + "\n")
    except Exception:
        pass  # la journalisation ne doit jamais casser la mesure


def main():
    cfg = load_json(CONFIG_PATH, {})
    seed = float(os.environ.get("NOURRISSEUR_SEED") or cfg.get("seed_usdt") or 150.0)
    mode = (os.environ.get("NOURRISSEUR_MODE") or cfg.get("mode") or "obeir").strip().upper()
    stale = float(os.environ.get("NOURRISSEUR_STALE") or STALE_S)
    now = datetime.now(timezone.utc)
    jour = now.strftime("%Y-%m-%d")

    st = lire_state_live()
    if st is None or st["age_s"] > stale:
        ecrire_histoire({"event": "MESURE_IMPOSSIBLE", "ts": now.isoformat(),
                         "raison": "state HULK absent ou muet > %.0fs" % stale})
        print(json.dumps({"perte_journaliere_pct": None, "mode": mode,
                          "statut": "SANS_MESURE", "state": (st or {}).get("path"),
                          "age_s": round((st or {}).get("age_s") or -1, 1)}))
        return 0

    # Pivot du jour : le 1er state vu après 00:00 UTC devient la référence
    pivot = load_json(PIVOT_PATH, {})
    if pivot.get("date_utc") != jour or pivot.get("pnl_pivot") is None:
        pivot = {"date_utc": jour, "pnl_pivot": st["pnl_total"], "state": st["path"]}
        atomic_write_json(PIVOT_PATH, pivot)

    perte = max(0.0, (float(pivot["pnl_pivot"]) - st["pnl_total"]) / seed * 100.0)
    seuil = float(cfg.get("pct_journalier", 11.67))

    statut, declenche = "OK", False
    if mode == "OBS":
        if perte >= seuil:
            statut = "SEUIL_ATTEINT_OBS"
            try:
                from cortana_thermo import write_urgent_alert
                write_urgent_alert(
                    "Disjoncteur C7 (OBS) : perte journalière %.2f%% ≥ seuil %.2f%% "
                    "(pnl %.2f$, pivot %.2f$, seed %.0f$)"
                    % (perte, seuil, st["pnl_total"], float(pivot["pnl_pivot"]), seed),
                    source="nourrir_disjoncteur", level="URGENT",
                    title="DISJONCTEUR C7 (OBS)")
            except Exception:
                pass
    else:
        from disjoncteur import verifier_et_brigader
        # taille_proposee=0 : le nourrisseur ne brigue rien (C3) — il laisse le
        # disjoncteur évaluer le seuil ; si perte ≥ seuil → Mur de Fer complet.
        res = verifier_et_brigader(0.0, seed, perte)
        declenche = bool(res.get("declenche"))
        statut = "MUR_DE_FER" if declenche else "OK"

    ecrire_histoire({"event": "MESURE", "ts": now.isoformat(),
                     "perte_pct": round(perte, 4), "pnl": st["pnl_total"],
                     "pivot": pivot["pnl_pivot"], "seed": seed,
                     "mode": mode, "statut": statut})
    print(json.dumps({"perte_journaliere_pct": round(perte, 3), "seuil": seuil,
                      "mode": mode, "statut": statut, "state": st["path"],
                      "age_s": round(st["age_s"], 1)}))
    return 1 if declenche else 0


if __name__ == "__main__":
    sys.exit(main())

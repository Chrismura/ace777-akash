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


def etat_exploitable(st: dict) -> bool:
    """False si le state ne permet PAS une mesure de perte fiable (fail-safe).

    Un état « pas encore repris » ne dit pas « pnl = 0 » : il dit « je ne sais pas
    encore ». Le lire comme une perte nulle a déjà produit un faux Mur de Fer
    (21/09, 13,93 %). Deux formes, même famille :
      - VIDE   : écrit au boot par le moteur avant que son --resume ait repris
                 (pnl 0, aucune position, aucun bag) ;
      - VIERGE : artefact de re-seed (0 trade, 0 cash de paire, pnl ≈ 0, pas de
                 bags) — la forme qui avait écrasé les bags le 24/08.
    Définition alignée sur paper_diprip._est_vierge, mais RE-VÉRIFIÉE ici de façon
    indépendante (règle d'or #9 : un gardien ne juge pas avec la mesure qu'il garde).
    """
    if not (st.get("positions") or {}) and not (st.get("bags") or {}):
        return False  # état VIDE (boot avant reprise)
    if (int(st.get("trades") or 0) == 0
            and abs(float(st.get("pnl_total") or 0.0)) <= 0.01
            and not any(v > 0 for v in (st.get("pair_cash") or {}).values())
            and not (st.get("bags") or st.get("bag_dca"))):
        return False  # re-seed VIERGE
    return True


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
    # GARDE 21/09/2026 (renforcée 22/09/2026) : un state non encore repris n'est PAS une
    # mesure. La garde du 21/09 ne couvrait que le state VIDE (pnl 0 + 0 position) ; il
    # restait la VIERGE de re-seed (positions présentes, 0 trade, pnl 0) — lue telle
    # quelle elle donnerait « perte (pivot 30,04 − 0)/150 = 20 % » → Mur de Fer → STOP_ALL.
    # Dans le doute on ne décide pas (R11) : SANS_MESURE, jamais de coupe.
    if not etat_exploitable(st):
        return None
    # §73 anti-aveugle : le Mur regardait le RÉALISÉ pur (pnl_total) et restait
    # aveugle aux crashes de bags (latent -71 $ le 29/10). On mesure l'EQUITY :
    # cash des paires + quantités (positions + bags) valorisées au DIGEST.
    qty = {}
    for cont in (st.get("positions") or {}, st.get("bags") or {}):
        for p, v in (cont or {}).items():
            try:
                q = float((v or {}).get("qty") or 0.0)
            except Exception:
                q = 0.0
            if q > 0:
                qty[p] = qty.get(p, 0.0) + q
    cash = 0.0
    for v in (st.get("pair_cash") or {}).values():
        try:
            cash += float(v or 0.0)
        except Exception:
            continue
    return {
        "path": chemin.name,
        "pnl_total": float(st.get("pnl_total") or 0.0),
        "age_s": time.time() - chemin.stat().st_mtime,
        "qty": qty,
        "cash": cash,
    }


def lire_marks_fraiches(max_age_h=3.0):
    """Marks + preuve de vie. ANTI-AVEUGLE §73 (boucle source 02/11) : le
    scanner digest NE RÉÉCRIT PAS quand le signal est inchangé — un vieux
    DIGEST_*.json n'est donc PAS une donnée périmée. La preuve de vie, c'est
    le heartbeat (log watchdog + DIGEST_LATEST.md) ; les marks, le dernier
    JSON. Les deux, ou SANS_MESURE."""
    try:
        cands = sorted(RUNS.glob("DIGEST_*.json"),
                       key=lambda p: p.stat().st_mtime, reverse=True)
        if not cands:
            return None, None
        heartbeats = []
        for hb in (RUNS / "DIGEST_WATCHDOG_STDOUT.log", RUNS / "DIGEST_LATEST.md"):
            try:
                heartbeats.append((time.time() - hb.stat().st_mtime) / 3600.0)
            except Exception:
                continue
        if not heartbeats or min(heartbeats) > max_age_h:
            return None, (min(heartbeats) if heartbeats else None)
        d = json.loads(cands[0].read_text(encoding="utf-8"))
        px = {}
        for e in (d.get("pairs") or []):
            try:
                if e.get("pair") and float(e.get("last") or 0) > 0:
                    px[e["pair"]] = float(e["last"])
            except Exception:
                continue
        # FIX 03/11 (boucle source, faux Mur) : le DIGEST change de PÉRIMÈTRE d'un
        # scan à l'autre. Le 03/11 07:10Z il ne portait pas QNT/FLUID/RWA -> ils
        # étaient valorisés 0 -> equity 691,95 $ au lieu de 794,84 $ -> « perte
        # 13,35 % » -> Mur de Fer + STOP_ALL + moteur coupé. Un prix manquant n'est
        # pas un prix nul : on complète avec le dernier mark CONNU (40 DIGEST max).
        for f in cands[1:41]:
            if len(px) >= 30:
                break
            try:
                d2 = json.loads(f.read_text(encoding="utf-8"))
            except Exception:
                continue
            for e in (d2.get("pairs") or []):
                try:
                    _p = e.get("pair")
                    _v = float(e.get("last") or 0)
                except Exception:
                    continue
                if _p and _p not in px and _v > 0:
                    px[_p] = _v
        return px, min(heartbeats)
    except Exception:
        return None, None


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

    # Equity live : cash + quantités × marks fraîches (§73 : le réalisé seul
    # est aveugle aux crashes de bags). Marks > 3 h -> SANS_MESURE (R11).
    marks, marks_age_h = lire_marks_fraiches()
    if marks is None:
        ecrire_histoire({"event": "MESURE_IMPOSSIBLE", "ts": now.isoformat(),
                         "raison": "DIGEST absent ou vieux (> 3 h)"})
        print(json.dumps({"perte_journaliere_pct": None, "mode": mode,
                          "statut": "SANS_MESURE", "state": st["path"]}))
        return 0
    equity = st["cash"] + sum(q * marks.get(p, 0.0) for p, q in st["qty"].items())
    # R11 (03/11) : si une seule paire détenue n'a AUCUN mark connu, l'equity est
    # fausse -> SANS_MESURE. On ne coupe jamais le moteur sur un chiffre incomplet.
    _manquants = sorted(p for p in st["qty"] if p not in marks)
    if _manquants:
        ecrire_histoire({"event": "SANS_MESURE", "ts": now.isoformat(),
                         "raison": "paire(s) détenue(s) sans mark connu : %s"
                                   % ",".join(_manquants[:6])})
        print(json.dumps({"perte_journaliere_pct": None, "mode": mode,
                          "statut": "SANS_MESURE", "state": st["path"],
                          "manquants": _manquants}))
        return 0

    # Pivot du jour : le 1er state vu après 00:00 UTC devient la référence.
    # Migration §73 : l'ancien pivot (réalisé pur) est remplacé par l'equity.
    pivot = load_json(PIVOT_PATH, {})
    if pivot.get("date_utc") != jour or pivot.get("eq_pivot") is None:
        pivot = {"date_utc": jour, "pnl_pivot": st["pnl_total"],
                 "eq_pivot": equity, "state": st["path"]}
        atomic_write_json(PIVOT_PATH, pivot)

    base = float(pivot["eq_pivot"]) if pivot.get("eq_pivot") else seed
    perte = max(0.0, (base - equity) / base * 100.0) if base > 1e-9 else 0.0
    # Seuil MESURÉ (§73) : mur_mesure.json frais (< 26 h), sinon SANS_MESURE.
    seuil = None
    try:
        mur = json.loads((IM / "thermo" / "mur_mesure.json").read_text(encoding="utf-8"))
        age_mur_h = (time.time() - (IM / "thermo" / "mur_mesure.json").stat().st_mtime) / 3600.0
        if age_mur_h <= 26.0 and float(mur.get("seuil_jour_pct", 0)) > 0:
            seuil = float(mur["seuil_jour_pct"])
    except Exception:
        seuil = None
    if seuil is None:
        ecrire_histoire({"event": "SANS_MESURE", "ts": now.isoformat(),
                         "raison": "mur_mesure.json stale/absent : pas de coupe"})
        print(json.dumps({"perte_journaliere_pct": round(perte, 3), "seuil": None,
                          "mode": mode, "statut": "SANS_MESURE",
                          "equity": round(equity, 2)}))
        return 0

    statut, declenche = "OK", False
    if mode == "OBS":
        if perte >= seuil:
            statut = "SEUIL_ATTEINT_OBS"
            try:
                from cortana_thermo import write_urgent_alert
                write_urgent_alert(
                    "Disjoncteur C7 (OBS) : perte journalière %.2f%% ≥ seuil %.2f%% "
                    "(equity %.2f$, pivot %.2f$)"
                    % (perte, seuil, equity, float(pivot["eq_pivot"])),
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
                     "equity": round(equity, 2),
                     "pivot": pivot.get("eq_pivot"), "seed": seed,
                     "mode": mode, "statut": statut})
    print(json.dumps({"perte_journaliere_pct": round(perte, 3), "seuil": seuil,
                      "mode": mode, "statut": statut, "state": st["path"],
                      "equity": round(equity, 2),
                      "age_s": round(st["age_s"], 1)}))
    return 1 if declenche else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rôle (ACE777) : LEÇONS AUTO — la boucle E4 de l'AGORA.
Chaque analyse notée de Cortana (HIT/MISS/FLAT par indice) devient une LEÇON
actionnable dans la base de connaissance. Boucle : erreur → leçon → réinjectée
→ moins d'erreurs.

2 temps (famille nvidia) :
  --scan     : lit strategie/justesse_v2.json → écrit strategie/lecons_brutes.json
              (STAGING : constats bruts par indice, classés par fiabilité).
              NE TOUCHE PAS à la base.
  --valider  : lit le staging → construit les AXIOMES au format
              « [indice] → [constat] → [action recommandée] » (≤20 mots, PAS de
              chiffres bruts) → TTL 7 jours → fusionne dans
              strategie/CONNAISSANCE_PROJETS.json sous « lecons_agora »
              (namespace "cortana"). Idempotent.

Doctrine : stdlib uniquement, écriture atomique, kill-switch, robuste.
"""

import os
import sys
import json
import tempfile
from datetime import datetime, timezone, timedelta

# ============================================================
# CHEMINS (convention ACE777 — repo racine ~/ace777-test-day1)
# ============================================================
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
INDEX_MAISON = os.path.join(BASE_DIR, "Index_Maison")
STRATEGIE_DIR = os.path.join(INDEX_MAISON, "strategie")

JUSTESSE_PATH = os.path.join(INDEX_MAISON, "scripts", "justesse_v2.json")
LECONS_BRUTES_PATH = os.path.join(STRATEGIE_DIR, "lecons_brutes.json")
CONNAISSANCE_PATH = os.path.join(STRATEGIE_DIR, "CONNAISSANCE_PROJETS.json")

STOP_LOCAL = os.path.join(STRATEGIE_DIR, "STOP")
STOP_GLOBAL = os.path.join(INDEX_MAISON, "STOP_ALL")

# ============================================================
# SEUILS (spec AGORA + famille)
# ============================================================
TTL_DAYS = 7            # TTL des leçons avant validation en règle structurelle (gemini)
N_MIN = 5               # minimum d'analyses notées pour qu'une leçon existe (spec §3.3)
T_SEUIL_BAS = 70.0      # taux < 70% → axiome « corroborer »
T_SEUIL_HAUT = 75.0     # taux > 75% → axiome « confiance »
MAX_MOTS = 20           # longueur max d'un axiome (famille Q2)


def verifier_kill_switch():
    if os.path.exists(STOP_LOCAL) or os.path.exists(STOP_GLOBAL):
        print("[KILL] Kill switch activé. Arrêt propre.", file=sys.stderr)
        sys.exit(1)


def ecriture_atomique(chemin, donnees):
    verifier_kill_switch()
    d = os.path.dirname(chemin)
    if d:
        os.makedirs(d, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=d or ".", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(donnees, f, ensure_ascii=False, indent=2)
        os.replace(tmp, chemin)
    except Exception:
        if os.path.exists(tmp):
            try:
                os.remove(tmp)
            except Exception:
                pass
        raise


def charger_json(chemin, defaut):
    if not os.path.exists(chemin):
        return defaut
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return defaut


# ============================================================
# TEMPS 1 — SCAN (staging brut, ne touche pas à la base)
# ============================================================
def action_scan():
    justesse = charger_json(JUSTESSE_PATH, {})
    par_indice = justesse.get("par_indice", {}) or {}

    constats = []
    for indice, stats in par_indice.items():
        if not isinstance(stats, dict):
            continue
        hit = int(stats.get("hit", 0) or 0)
        n = int(stats.get("n", 0) or 0)
        taux = round((hit / n * 100.0), 1) if n > 0 else 0.0
        if n >= N_MIN:
            fiabilite = "haute" if taux > T_SEUIL_HAUT else ("faible" if taux < T_SEUIL_BAS else "neutre")
        else:
            fiabilite = "insuffisante"
        constats.append({
            "indice": indice,
            "hit": hit,
            "n": n,
            "taux_pct": taux,
            "fiabilite": fiabilite,
        })

    constats.sort(key=lambda c: c["taux_pct"])
    payload = {
        "date_scan": datetime.now(timezone.utc).isoformat(),
        "source": "score_justesse (HIT/MISS Cortana)",
        "constats_bruts": constats,
    }
    ecriture_atomique(LECONS_BRUTES_PATH, payload)
    print(f"[LEÇONS] Staging écrit : {LECONS_BRUTES_PATH} ({len(constats)} constats)")


# ============================================================
# TEMPS 2 — VALIDATION (axiomes → base, TTL 7j, idempotent)
# ============================================================
def action_valider():
    staging = charger_json(LECONS_BRUTES_PATH, {})
    constats = staging.get("constats_bruts", []) or []

    now = datetime.now(timezone.utc)
    ttl_expire = (now + timedelta(days=TTL_DAYS)).isoformat()

    nouveaux = []
    for c in constats:
        indice = str(c.get("indice", "inconnu"))
        n = int(c.get("n", 0) or 0)
        taux = float(c.get("taux_pct", 0.0) or 0.0)
        if n < N_MIN:
            continue
        if taux < T_SEUIL_BAS:
            constat_desc = "Taux de réussite insuffisant"
            action_rec = "corroborer avec un autre indice avant de te positionner"
        elif taux > T_SEUIL_HAUT:
            constat_desc = "Taux de réussite élevé"
            action_rec = "tu peux t'appuyer dessus avec confiance"
        else:
            continue  # zone neutre 70-75% : pas d'axiome strict (spec §3.3)

        axiome = f"[{indice}] → [{constat_desc}] → [{action_rec}]"
        if len(axiome.split()) > MAX_MOTS:
            continue
        nouveaux.append({
            "id": f"lecon_{indice}_{int(now.timestamp())}",
            "namespace": "cortana",      # cloisonnement strict (famille Q3)
            "axiome": axiome,
            "ttl_expire": ttl_expire,
            "source": "HIT/MISS",
            "cree_le": now.isoformat(),
        })

    # Fusion idempotente dans la base
    connaissance = charger_json(CONNAISSANCE_PATH, {"projets": {}, "lecons_agora": []})
    existants = connaissance.get("lecons_agora", []) or []
    if not isinstance(existants, list):
        existants = []

    # 1) Nettoyage TTL + déduplication
    gardes = []
    vus = set()
    for item in existants:
        exp = item.get("ttl_expire")
        if exp:
            try:
                if datetime.fromisoformat(str(exp).replace("Z", "+00:00")) < now:
                    continue  # expiré → purgé
            except Exception:
                pass
        ax = item.get("axiome")
        if ax and ax not in vus:
            vus.add(ax)
            gardes.append(item)

    # 2) Ajout des nouveaux (idempotent : pas de doublon d'axiome)
    ajoutes = 0
    for na in nouveaux:
        if na["axiome"] not in vus:
            vus.add(na["axiome"])
            gardes.append(na)
            ajoutes += 1

    connaissance["lecons_agora"] = gardes
    connaissance["updated"] = now.isoformat()
    ecriture_atomique(CONNAISSANCE_PATH, connaissance)
    print(f"[LEÇONS] Base mise à jour : {ajoutes} nouvel(le)(s) leçon(s) · {len(gardes)} actives (TTL {TTL_DAYS}j)")


# ============================================================
# MAIN
# ============================================================
def main():
    verifier_kill_switch()
    if len(sys.argv) < 2 or sys.argv[1] not in ("--scan", "--valider"):
        print("Usage: python3 lecons_auto.py [--scan | --valider]", file=sys.stderr)
        sys.exit(1)
    if sys.argv[1] == "--scan":
        action_scan()
    else:
        action_valider()
    return 0


if __name__ == "__main__":
    sys.exit(main())

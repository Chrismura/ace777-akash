#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
veille_presence_paires.py — SONDE PRÉSENCE PAIRES MEXC (30/08, GO Christophe)
=============================================================================
Contexte : QAITUSDT a été delisté de MEXC le 29/08 à 14:03Z (HTTP 400 sur tout,
absent d'exchangeInfo). Le moteur a gaspillé 548 appels/jour en retries pendant
7h avant qu'on le voie. Leçon : il faut VÉRIFIER la présence des paires, pas
attendre les erreurs.

Cette sonde :
  1. Lit la liste des paires de hulk-mexc/config/defaults.env
     (PAPER_PAIRS + PAPER_EXTRA_PAIRS + PAPER_WATCH_PAIRS).
  2. Vérifie chaque paire contre MEXC exchangeInfo (status + isSpotTradingAllowed).
  3. Écrit data/presence_paires_etat.json + cockpit/presence_paires.js.
  4. Si une paire a DISPARU (absente ou st=true) → alerte vocale + fichier alerte.
  5. Journalise l'historique (data/presence_paires_hist.jsonl, append-only).

Doctrine maison : stdlib uniquement, écriture atomique, kill-switch,
idempotent, gratuit (API publique MEXC, 1 appel exchangeInfo). 1 appel API
par run — léger, peut tourner toutes les 6h (delisting = rare, pas besoin de
plus).

USAGE : python3 veille_presence_paires.py [--check]   (--check = un seul passage
sans alerte vocale, pour test manuel)
"""

import os
import sys
import json
import time
import tempfile
import urllib.request

# ============================================================
# CHEMINS (convention ACE777 — repo racine ~/ace777-test-day1)
# ============================================================
HOME = os.path.expanduser("~")
REPO = os.path.join(HOME, "ace777-test-day1")
IM = os.path.join(REPO, "Index_Maison")
HULK = os.path.join(REPO, "hulk-mexc")
DATA_DIR = os.path.join(IM, "data")
COCKPIT_DIR = os.path.join(IM, "cockpit")
ALERTES_DIR = os.path.join(DATA_DIR, "alertes")

STOP_LOCAL = os.path.join(IM, "strategie", "STOP")
STOP_GLOBAL = os.path.join(IM, "STOP_ALL")
ENV_FILE = os.path.join(HULK, "config", "defaults.env")

ETAT_OUT = os.path.join(DATA_DIR, "presence_paires_etat.json")
JS_OUT = os.path.join(COCKPIT_DIR, "presence_paires.js")
HIST = os.path.join(DATA_DIR, "presence_paires_hist.jsonl")
ALERTE_VOCALE = os.path.join(IM, "scripts", "alerte_vocale.py")

MEXC_EXCHANGE_INFO = "https://api.mexc.com/api/v3/exchangeInfo"
USER_AGENT = "ACE777-presence/1.0"


def kill_switch_actif():
    return os.path.exists(STOP_LOCAL) or os.path.exists(STOP_GLOBAL)


def ecriture_atomique(chemin, contenu):
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(chemin), text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(contenu)
        os.replace(tmp, chemin)
    except Exception:
        if os.path.exists(tmp):
            try:
                os.remove(tmp)
            except Exception:
                pass
        raise


def lire_paires_env():
    """Extrait PAPER_PAIRS + PAPER_EXTRA_PAIRS + PAPER_WATCH_PAIRS de defaults.env."""
    paires = []
    if not os.path.exists(ENV_FILE):
        return paires
    try:
        with open(ENV_FILE, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                k = k.strip()
                if k in ("PAPER_PAIRS", "PAPER_EXTRA_PAIRS", "PAPER_WATCH_PAIRS"):
                    for p in v.split(","):
                        p = p.strip().upper()
                        if p and p not in paires:
                            paires.append(p)
    except Exception:
        pass
    return paires


def get_exchange_info():
    req = urllib.request.Request(MEXC_EXCHANGE_INFO, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read().decode("utf-8"))


def alerte_vocale(msgs):
    """Lance alerte_vocale.py détaché (anti-empilement maison)."""
    try:
        import subprocess
        out = subprocess.check_output(["pgrep", "-f", "alerte_vocale.py"], text=True,
                                      stderr=subprocess.DEVNULL)
        if out.strip():
            return False  # une boucle crie déjà
    except Exception:
        pass
    try:
        ts = int(time.time())
        msg = "Alerte ACE777. " + " ; ".join(msgs)[:300]
        subprocess.Popen(["python3", ALERTE_VOCALE, "--message", msg, "--id", str(ts)],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                         start_new_session=True)
        return True
    except Exception:
        return False


def main():
    if "--check" in sys.argv:
        alerter = False
    else:
        alerter = True
    if kill_switch_actif():
        print("[PRESENCE_PAIRES] Kill-switch actif — sortie.")
        return 0

    paires = lire_paires_env()
    if not paires:
        print("[PRESENCE_PAIRES] Aucune paire trouvée dans defaults.env — sortie.")
        return 0

    try:
        info = get_exchange_info()
    except Exception as e:
        # Fail-open réseau : on ne crie PAS (ce serait un faux positif wifi),
        # on écrit un état "inconnu" et on journalise.
        etat = {"ts": time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime()),
                "verdict": "INCONNU", "erreur": str(e),
                "nb_paires": len(paires), "paires_manquantes": [],
                "paires": []}
        ecriture_atomique(ETAT_OUT, json.dumps(etat, ensure_ascii=False, indent=2))
        ecriture_atomique(JS_OUT, "window.__PRESENCE_PAIRES__ = " + json.dumps(etat, ensure_ascii=False) + ";\n")
        print(f"[PRESENCE_PAIRES] API MEXC injoignable: {e} — état INCONNU (pas d'alerte).")
        return 0

    syms = {s["symbol"]: s for s in info.get("symbols", [])}
    lignes = []
    manquantes = []
    for p in paires:
        s = syms.get(p)
        if not s:
            lignes.append({"pair": p, "presente": False, "st": None,
                           "spot": None, "note": "DELISTÉE — absente d'exchangeInfo"})
            manquantes.append(p)
            continue
        st = bool(s.get("st"))
        spot = bool(s.get("isSpotTradingAllowed"))
        note = "OK"
        if st or not spot:
            note = "SUSPENDUE/DELIST EN COURS"
            manquantes.append(p)
        lignes.append({"pair": p, "presente": True, "st": st, "spot": spot, "note": note})

    verdict = "OK"
    if manquantes:
        verdict = "ALERTE"
    etat = {"ts": time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime()),
            "verdict": verdict,
            "nb_paires": len(paires),
            "nb_manquantes": len(manquantes),
            "paires_manquantes": manquantes,
            "paires": lignes}
    ecriture_atomique(ETAT_OUT, json.dumps(etat, ensure_ascii=False, indent=2))
    ecriture_atomique(JS_OUT, "window.__PRESENCE_PAIRES__ = " + json.dumps(etat, ensure_ascii=False) + ";\n")

    # Historique append-only
    try:
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(HIST, "a", encoding="utf-8") as f:
            f.write(json.dumps({"ts": etat["ts"], "verdict": verdict,
                                "manquantes": manquantes}, ensure_ascii=False) + "\n")
    except Exception:
        pass

    if manquantes:
        # Fichier alerte (pour la veilleuse/cockpit)
        try:
            os.makedirs(ALERTES_DIR, exist_ok=True)
            ecriture_atomique(os.path.join(ALERTES_DIR, "ALERTE_PRESENCE_PAIRES.json"),
                              json.dumps({"ts": etat["ts"], "manquantes": manquantes},
                                         ensure_ascii=False, indent=2))
        except Exception:
            pass
        msgs = [f"La paire {p} a disparu de MEXC. Vérifie le portefeuille." for p in manquantes]
        if alerter:
            alerte_vocale(msgs)
        print(f"[PRESENCE_PAIRES] {verdict} — manquantes: {', '.join(manquantes)}")
    else:
        print(f"[PRESENCE_PAIRES] OK — {len(paires)} paires présentes sur MEXC.")
    return 1 if manquantes else 0


if __name__ == "__main__":
    sys.exit(main())

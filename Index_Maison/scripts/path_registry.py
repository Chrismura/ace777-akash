#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
path_registry.py — PathRegistry centralisé (FIX famille n°4, 29/08, GO)
=======================================================================
Barrière structurelle contre les erreurs répétées (chemins relatifs/absolus
qui plantent en plist, processus silencieux qui meurent sans alerte).

Deux services :

  1. PATHES — registre centralisé des chemins absolus de la maison.
     Chaque script peut faire `path_registry.verifier("signal3")` au démarrage :
     si un chemin attendu manque → sys.exit(1) (arrêt propre, PAS de plantage
     silencieux 5 lignes plus loin). C'est le "validée au démarrage" famille.

  2. wrapper_plist — enveloppe une commande pour être lancée par launchd :
     - rejette stderr dans un log daté,
     - écrit un heartbeat (dernier run OK) consommé par sante_index,
     - fail-safe : si le processus meurt 3 fois en 5 min → on s'arrête (évite
       la boucle de redémarrage automatique launchd qui masque le crash).

Usage ligne de commande (plist) :
  python3 path_registry.py run --heartbeat data/heartbeat_x.json -- script.py [args...]
En Python :
  import path_registry as pr
  pr.print si --noexit
  ok, manquants = pr.verifier("signal3")
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Racine de la maison (résolue une fois, jamais relative dans les plists)
# ---------------------------------------------------------------------------

# Chemin absolu détecté : on remonte de path_registry.py → Index_Maison/scripts
# → Index_Maison → ace777-test-day1
IM_SCRIPTS = Path(__file__).resolve().parent          # .../Index_Maison/scripts
IM = IM_SCRIPTS.parent                                 # .../Index_Maison
RACINE = IM.parent                                     # ace777-test-day1
HULK = RACINE / "hulk-mexc"

# ---------------------------------------------------------------------------
# Registre centralisé des chemins critiques par œuvre
# ---------------------------------------------------------------------------

PATHES: dict = {
    # (chemin, obligatoire ?) — obligatoire = fichier/dossier attendu pour vivre
    "croisement": [
        (IM_SCRIPTS / "croiser_donnees_externes.py", True),
        (IM / "data" / "croisement_externe_etat.json", False),
    ],
    "signal3": [
        (HULK / "scripts" / "signal3_livre_ecorche.py", True),
        (HULK / "runs" / "murs_observations.json", True),
        (HULK / "runs", True),
    ],
    "sapi": [
        (IM_SCRIPTS / "silent_drain_index.py", True),
        (IM / "data" / "sapi_etat.json", False),     # se recrée au 1er run
        (HULK / "runs" / "murs_observations.json", True),  # proxy carnet
    ],
    "pont_onchain": [
        (IM_SCRIPTS / "pont_onchain.py", True),
        (IM / "data" / "sdi_latest.json", False),
    ],
    "thermo": [
        (IM_SCRIPTS / "thermo_quotidien_free.py", True),
        (IM / "data" / "live.json", False),
    ],
}


def verifier(oeuvre: str, exit_: bool = True):
    """Valide les chemins d'une œuvre au démarrage. Si un chemin OBLIGATOIRE
    manque → listé ; si exit_ → sys.exit(1) (arrêt propre immédiat, sans
    plantage silencieux plus loin). Retourne (ok: bool, manquants: list[str])."""
    manquants = []
    for chemin, obligatoire in PATHES.get(oeuvre, []):
        if not Path(chemin).exists() and obligatoire:
            manquants.append(str(chemin))
    ok = not manquants
    if manquants:
        print(f"[PathRegistry:{oeuvre}] ÉCHEC validation : chemins manquants :",
              file=sys.stderr)
        for m in manquants:
            print(f"  - {m}", file=sys.stderr)
        if exit_:
            print(f"[PathRegistry:{oeuvre}] Arrêt (sys.exit(1)).", file=sys.stderr)
            sys.exit(1)
    elif os.environ.get("PATHREG_VERBOSE"):
        print(f"[PathRegistry:{oeuvre}] validation OK.", file=sys.stderr)
    return ok, manquants


# ---------------------------------------------------------------------------
# Wrapper plist : heartbeat + fail-safe + log daté
# ---------------------------------------------------------------------------

def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")


def _heartbeat_path(heartbeat: str) -> Path:
    p = Path(heartbeat)
    if not p.is_absolute():
        p = IM / p
    return p


def wrapper_plist(argv: list) -> int:
    """Usage : path_registry.py run --heartbeat relatif.json [--noexit] -- CMD...
    Lance CMD, journalise, écrit un heartbeat. Fail-safe : 3 morts en 5 min
    → arrêt (pas de reset launchd infini qui masque le crash)."""
    # Parse --heartbeat / --noexit / old-style -- (echo exit code)
    heartbeat = None
    no_exit = "--noexit" in argv
    argv = [a for a in argv if a != "--noexit"]

    if "--heartbeat" in argv:
        i = argv.index("--heartbeat")
        heartbeat = argv[i + 1]
        argv = argv[:i] + argv[i + 2:]
    # On prend tout ce qui suit le dernier "--" (séparateur perl-style) sinon tout
    if "--" in argv:
        cmd = argv[argv.index("--") + 1:]
    else:
        cmd = argv[1:] if argv and argv[0] == "run" else argv

    if not cmd:
        print("PathRegistry.wrapper: aucune commande. Usage : ... run --heartbeat X -- CMD", file=sys.stderr)
        return 2

    # Heartbeat : marque le début du run (frais = le processus est vivant)
    if heartbeat:
        hb = _heartbeat_path(heartbeat)
        try:
            hb.parent.mkdir(parents=True, exist_ok=True)
            hb.write_text(json.dumps({
                "ts": time.time(), "utc": _now_iso(),
                "cmd": cmd, "statut": "run",
            }), encoding="utf-8")
        except OSError:
            pass

    t0 = time.time()
    try:
        res = subprocess.run(cmd, capture_output=True, text=True)
    except FileNotFoundError as e:
        print(f"PathRegistry.wrapper: exécutable introuvable : {e}", file=sys.stderr)
        res = None

    if res is not None:
        sys.stdout.write(res.stdout)
        if res.returncode != 0:
            sys.stderr.write(res.stderr)
        else:
            # Heartbeat de fin réussi (statut ok)
            if heartbeat:
                hb = _heartbeat_path(heartbeat)
                try:
                    hb.write_text(json.dumps({
                        "ts": time.time(), "utc": _now_iso(),
                        "cmd": cmd, "statut": "ok",
                        "durée_s": round(time.time() - t0, 1),
                    }), encoding="utf-8")
                except OSError:
                    pass
        return res.returncode

    # --noexit : on ne fait PAS sysexit même si échec (pour les œuvres
    # pré-validées par verifier() ou pour debug). Sinon arrêt propre.
    if no_exit:
        return 0
    sys.exit(1)


def main_cli() -> int:
    if len(sys.argv) >= 2 and sys.argv[1] == "run":
        return wrapper_plist(sys.argv[2:])
    if len(sys.argv) >= 3 and sys.argv[1] == "verifier":
        oeuvre = sys.argv[2]
        ok, manquants = verifier(oeuvre, exit_=("-f" not in sys.argv))
        print("OK" if ok else f"MANQUANTS: {manquants}")
        return 0 if ok else 1
    print(__doc__)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main_cli())
    except KeyboardInterrupt:
        sys.exit(130)
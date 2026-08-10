#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""lancer_detache.py — lance un processus DÉTACHÉ sur macOS (10/08).

`setsid` n'existe pas sur macOS. L'équivalent natif est
`subprocess.Popen(..., start_new_session=True)` qui crée une nouvelle
session (exactement comme setsid sous Linux) : le processus survit à la
mort du shell qui l'a lancé. C'est LE correctif du problème
« nohup tué avec le basher » qui nous a fait perdre des appels IA entiers.

USAGE :
    python3 lancer_detache.py <commande...>

EXEMPLE :
    python3 lancer_detache.py python3 soumettre_hub_illimite.py code.ia mission.txt reponse.md

Le PID du processus détaché est imprimé. La commande retourne immédiatement.
"""
import os
import subprocess
import sys
import tempfile

if len(sys.argv) < 2:
    print("Usage: lancer_detache.py <commande...>")
    sys.exit(2)

cmd = sys.argv[1:]
try:
    # start_new_session=True : nouvelle session, détaché du process group du parent
    log_path = os.path.join(tempfile.gettempdir(), "ace777_detache_%d.log" % os.getpid())
    with open(log_path, "w") as log_f:
        p = subprocess.Popen(
            cmd,
            start_new_session=True,
            stdin=subprocess.DEVNULL,
            stdout=log_f,
            stderr=subprocess.STDOUT,
        )
    print("[OK] processus détaché (PID %d) : %s" % (p.pid, " ".join(cmd)))
    print("[LOG] sorties dans %s" % log_path)
except Exception as e:
    print("[ECHEC] %s" % e, file=sys.stderr)
    sys.exit(1)

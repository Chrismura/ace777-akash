#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
voix_piste.py — VERROU DE PISTE UNIQUE GLOBAL (31/08, GO Christophe)
====================================================================
Cause du bug (alarmes Cortana qui se chevauchent / chafouillent) :
chacun des chemins vocaux (cortana_voice, cortana_brief, le bridge
cortana_cockpit_bridge._speak_texte, alerte_vocale) générait son .mp3 avec
edge_tts EN PARALLÈLE, puis jouait via afplay/say. Le « killall afplay »
local ne couvre que l'instant de lecture, pas la collision de génération :
deux agents → deux .mp3 → deux voix superposées.

Fix : un SEUL lock inter-processus (fcntl.flock) partagé par TOUS les
chemins, tenu pendant TOUTE la durée génération+lecture. Tant qu'un agent
parle, les autres attendent (et refusent après timeout court) au lieu de
se chevaucher. `stop_piste()` tue violemment la piste en cours (barge-in).

Le lock dure au plus PISTE_MAX_S — au-delà on tue la piste (un brief ne
peut pas monopoliser à vie).

Usage :
    with voix_piste.piste_verrou(paquet="cortana_brief"):
        ... générer le .mp3 ...
        ... jouer avec afplay / say ...

    voix_piste.stop_piste()   # coupe toute voix en cours (barge-in)
"""
from __future__ import annotations

import fcntl
import os
import subprocess
import time
from contextlib import contextmanager
from pathlib import Path

# Fichier de lock commun (mapé sur le lock déjà utilisé par cortana_voice).
SPEAK_LOCK = Path("/tmp/ace777_swarm_pids/.cortana_speak.lock")

# Durée max d'une piste (s) : au-delà on considère le lock un held-up et on
# coupe la piste pour libérer la parole.
PISTE_MAX_S = 120

# Commandes audio utilisées par la maison.
AFPLAY = "/usr/bin/afplay"
SAY = "/usr/bin/say"


def _silence_players() -> None:
    """Coupe toute lecture en cours (afplay + say) — filet de sécurité, en
    plus du lock. Ne couvre pas la génération, c'est le lock qui le fait."""
    subprocess.run(["killall", "afplay"], check=False, capture_output=True)
    subprocess.run(["killall", "say"], check=False, capture_output=True)


def stop_piste() -> str:
    """Coupe toute voix en cours (barge-in global)."""
    _silence_players()
    return "Piste coupée."


@contextmanager
def piste_verrou(paquet: str = "voix", timeout: float | None = None):
    """Verrou inter-processus unique tenu pendant génération + lecture.

    timeout=None → attente bloquante (un brief en cours finit puis on parle).
    timeout>0   → durée max d'attente ; si le lock est pris au-delà, on coupe
                  la piste en cours et on prend la main (urgence).
    """
    SPEAK_LOCK.parent.mkdir(parents=True, exist_ok=True)
    lf = SPEAK_LOCK.open("a+")
    try:
        if timeout is not None:
            # Verrou non bloquant + attente bornée ; en urgence on reprend la main.
            attente = 0.0
            while not _try_lock(lf):
                if attente >= timeout:
                    stop_piste()
                    _try_lock(lf)  # le lock est libéré par notre kill
                    break
                time.sleep(0.2)
                attente += 0.2
        else:
            fcntl.flock(lf.fileno(), fcntl.LOCK_EX)
        yield
    finally:
        try:
            fcntl.flock(lf.fileno(), fcntl.LOCK_UN)
        finally:
            lf.close()


def _try_lock(lf):
    try:
        fcntl.flock(lf.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        return True
    except OSError:
        return False
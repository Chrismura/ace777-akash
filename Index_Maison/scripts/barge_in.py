#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""barge_in.py — COUPE LA PAROLE a Cortana avec le micro du Mac (ffmpeg natif).

Zero dependance a installer : ffmpeg est deja la (/opt/homebrew/bin/ffmpeg).
Micro : "MacBook Air Microphone" (avfoundation device :0).

Mecanique (anti-faux-positifs) :
  1. CALIBRATION EN SILENCE : preparer() lance la calibration de l'ambiant
     en arriere-plan PENDANT la generation du mp3 (edge_tts ne joue rien).
     -> l'ambiant mesure le vrai silence de la piece, pas la voix de Cortana.
  2. ADAPTATION ECHO (1,5 s) pendant qu'elle parle : niveau de SA voix qui
     revient par les haut-parleurs -> pour ne pas se couper toute seule.
  3. SURVEILLANCE : toutes les ~0,25 s on mesure le micro ; si le niveau
     depasse le seuil (ambiant + marge, OU echo + marge) pendant 2
     echantillons consecutifs -> on tue afplay.
     "Ca marche de pres" : il faut parler assez fort / proche du Mac.

Désactivation : BARGE_IN=0 dans l'environnement.
"""
import os
import re
import subprocess
import sys
import threading
import time

DEVICE = ":0"
FFMPEG = "/opt/homebrew/bin/ffmpeg"
MARGE_AMBIANT = 8.0    # dB au-dessus de l'ambiant = "on parle"
MARGE_ECHO = 4.0       # dB au-dessus de l'echo de sa propre voix
PLAFOND = -42.0        # ne jamais declarer "parole" en dessous (clics, souffle)
DUREE_SAMPLE = 0.22    # duree de chaque echantillon micro (s)
PERSISTANCE = 2        # nb d'echantillons >= seuil parmi les 3 derniers
INTER_SAMPLE = 0.05    # pause entre 2 echantillons (echantillonnage dense)
ADAPT_ECHO = 1.5       # duree d'adaptation de l'echo (s)

_AMBIANT = None  # calibration faite en silence pendant la generation mp3
DEBUG = os.environ.get("BARGE_IN_DEBUG", "0") == "1"


def _log(msg):
    if DEBUG:
        print("[barge_in] " + msg, flush=True)


FLAG_OFF = "/tmp/ace777_ecoute.off"  # créé par le bouton ÉCOUTE du cockpit


def activ() -> bool:
    """Écoute active ? (BARGE_IN != 0 ET pas de flag OFF)."""
    if os.environ.get("BARGE_IN", "1") == "0":
        return False
    return not os.path.exists(FLAG_OFF)


def ecoute_activer() -> bool:
    """Réactive le micro (supprime le flag). Renvoie True (écoute active)."""
    if os.path.exists(FLAG_OFF):
        os.remove(FLAG_OFF)
    return True


def ecoute_couper() -> bool:
    """Coupe le micro (crée le flag). Renvoie False (écoute coupée)."""
    with open(FLAG_OFF, "w") as f:
        f.write("1")
    return False


def preparer():
    """Calibre l'ambiant EN SILENCE (pendant la generation mp3), en fond."""
    global _AMBIANT
    _AMBIANT = None
    if not activ():
        return
    _log("preparer() : lancement calibration ambiant en fond")
    threading.Thread(target=_calibrer_en_fond, daemon=True).start()


def _calibrer_en_fond():
    global _AMBIANT
    _AMBIANT = calibrer_ambiant()
    _log("calibration terminee : ambiant = %.1f dB" % _AMBIANT)


def niveau(duree=DUREE_SAMPLE) -> float:
    """Niveau moyen du micro en dB. -999 si echec (permission/absent)."""
    try:
        r = subprocess.run(
            [FFMPEG, "-f", "avfoundation", "-i", DEVICE, "-t", "%.2f" % duree,
             "-af", "volumedetect", "-f", "null", "-"],
            capture_output=True, text=True, timeout=duree + 4)
    except Exception:
        return -999.0
    m = re.search(r"mean_volume:\s*(-?[\d.]+) dB", r.stderr)
    return float(m.group(1)) if m else -999.0


def calibrer_ambiant(n=4, duree=DUREE_SAMPLE) -> float:
    """Niveau ambiant = le MAX de n echantillons (pire cas du silence)."""
    vals = [niveau(duree) for _ in range(n)]
    vals = [v for v in vals if v > -900.0]
    return max(vals) if vals else -999.0


def surveiller(player, duree_max=240.0) -> None:
    """Surveille le micro pendant que 'player' (afplay) tourne. Coupe si on parle."""
    global _AMBIANT
    if not activ():
        return
    ambiant = _AMBIANT if _AMBIANT is not None else calibrer_ambiant()
    _AMBIANT = None  # la calibration est consommee
    _log("surveiller() : ambiant = %.1f dB" % ambiant)
    if ambiant < -900:
        return  # micro injoignable -> barge-in indisponible, on laisse parler
    # 2) adaptation echo (sa propre voix pendant ~1,5 s)
    echo = ambiant
    t_fin = time.time() + ADAPT_ECHO
    while time.time() < t_fin and player.poll() is None:
        v = niveau()
        if v > echo:
            echo = v
        time.sleep(DUREE_SAMPLE)
    seuil = max(ambiant + MARGE_AMBIANT, echo + MARGE_ECHO, PLAFOND)
    _log("surveiller() : echo = %.1f dB, seuil = %.1f dB (plafond %s)" % (echo, seuil, PLAFOND))
    # 3) surveillance : declenche si >= PERSISTANCE echantillons sur les 3
    #    derniers depassent le seuil (2/3 = fiable meme si la voix fluctue)
    fenetre = []
    while player.poll() is None:
        v = niveau()
        au_dessus = v >= seuil
        fenetre.append(au_dessus)
        if len(fenetre) > 3:
            fenetre.pop(0)
        if au_dessus:
            _log("niveau %.1f dB >= seuil %.1f dB (%d/3)" % (v, seuil, sum(fenetre)))
            if sum(fenetre) >= PERSISTANCE:
                _log("COUPURE : on tue afplay !")
                try:
                    player.terminate()
                except Exception:
                    pass
                return
        time.sleep(INTER_SAMPLE)


def mode_veille(duree=8.0):
    """Affiche les niveaux en continu (diagnostic / reglage du seuil)."""
    ambiant = calibrer_ambiant()
    print("Ambiant: %.1f dB" % ambiant)
    t_fin = time.time() + duree
    while time.time() < t_fin:
        print("  niveau: %.1f dB  (parle devant le micro pour voir le seuil bouger)" % niveau())
        time.sleep(0.3)


if __name__ == "__main__":
    mode_veille(duree=float(sys.argv[1]) if len(sys.argv) > 1 else 8.0)

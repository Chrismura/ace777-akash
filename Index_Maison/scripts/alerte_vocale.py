#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rôle (ACE777) : ALERTE VOCALE EN BOUCLE — répète un message à voix haute toutes les 30s
jusqu'à EXTINCTION MANUELLE (volonté stricte de Christophe, 24h/24).
- Voix : edge_tts fr-FR-VivienneMultilingualNeural (pattern maison existant).
- Piste unique : killall say + killall edge_tts avant chaque lecture (règle maison).
- Extinction : `touch STOP_ALERTE` (global) OU `touch STOP_ALERTE_<id>` (précis)
  OU `--arret` OU Ctrl+C. La boucle s'arrête proprement et nettoie son fichier d'arrêt.
- Journal : data/alertes/ALERTE_[id].json (message, cause, heure).
- Boucle INFINIE — aucune limite de temps (décision Christophe ; la limite de sécurité
  24h est désactivée par défaut, réactivable si Christophe change d'avis).
Stdlib uniquement.
"""

import os
import sys
import time
import json
import tempfile
import argparse
import subprocess
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent.parent  # repo racine (~/ace777-test-day1)
IM = RACINE / "Index_Maison"
ALERTES_DIR = IM / "data" / "alertes"
AUDIO_TMP = IM / "data" / "temp_alerte.mp3"

# FIX 31/08 : UNE SEULE boucle par alerte (dé-duplication par contenu).
# Les lanceurs démarrent alerte_vocale.py sans tuer les boucles précédentes du
# même événement → accumulation de N processus identiques qui répètent le même
# message (le bug du « chafouin »). Ici, chaque démarrage tue les boucles qui
# jouent le MÊME message normalisé, puis prend la main. Une seule voix par
# événement, quel que soit le nombre de relances du lanceur.
import hashlib as _hashlib
DEDUP_DIR = ALERTES_DIR / ".dedup"


def _cle_dedup(message: str) -> str:
    """Clé stable par MESSAGE normalisé (peu sensible au cas/aux espaces et
    aux préfixes Alerte/Attention) pour grouper les doublons du même événement."""
    norm = " ".join(message.lower().replace("alerte", "").replace("attention.", "")
                    .split())
    return _hashlib.sha256(norm.encode("utf-8")).hexdigest()[:24]


def tuer_doublons(message: str) -> None:
    """Tue les autres boucles alerte_vocale qui jouent le même contenu.
    Au démarrage d'une nouvelle boucle, remplace l'éventuelle ancienne qui
    tourne encore (remplacement propre au lieu d'accumulation)."""
    cle = _cle_dedup(message)
    DEDUP_DIR.mkdir(parents=True, exist_ok=True)
    pid_file = DEDUP_DIR / f"{cle}.pid"
    if pid_file.exists():
        try:
            ancien = int(pid_file.read_text(encoding="utf-8").strip())
        except Exception:
            ancien = None
        if ancien and ancien != os.getpid():
            try:
                os.kill(ancien, 15)  # SIGTERM : la boucle écrit proprement son arrêt
            except Exception:
                pass
            try:
                pid_file.unlink()
            except Exception:
                pass
    # Écrire/rafraîchir son propre pid dès le départ ; on le nettoiera à la fin.
    try:
        ecriture_atomique(pid_file, str(os.getpid()))
    except Exception:
        pass


VOIX = "fr-FR-DeniseNeural"  # français pur (Vivienne multilingue → accent espagnol, 19/08)
INTERVALLE_SEC = 30  # répétition du message
PAUSE_SEC = 5        # tranches de pause (réactivité à l'arrêt)


def ecriture_atomique(chemin: Path, contenu: str):
    chemin.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(dir=str(chemin.parent), text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(contenu)
        os.replace(tmp_path, chemin)
    except Exception:
        if os.path.exists(tmp_path):
            try:
                os.remove(tmp_path)
            except Exception:
                pass
        raise


def fichiers_arret(id_alerte: str):
    return [
        IM / f"STOP_ALERTE_{id_alerte}",
        IM / "STOP_ALERTE",
        ALERTES_DIR / f"STOP_ALERTE_{id_alerte}",
        ALERTES_DIR / "STOP_ALERTE",
    ]


def verifier_arret(id_alerte: str) -> bool:
    for f in fichiers_arret(id_alerte):
        if f.exists():
            try:
                f.unlink()
            except Exception:
                pass
            return True
    return False


def parler(message: str):
    """Lit le message à voix haute (edge_tts → mp3 → afplay), une seule piste.
    FIX 31/08 : génération + lecture sous le verrou global voix_piste — plus
    d'alerte vocale qui chevauche les autres voix Cortana."""
    import voix_piste
    with voix_piste.piste_verrou("alerte_vocale"):
        try:
            AUDIO_TMP.parent.mkdir(parents=True, exist_ok=True)
            subprocess.run(
                ["python3", "-m", "edge_tts", "--voice", VOIX, "--text", message,
                 "--write-media", str(AUDIO_TMP)],
                check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            player = "afplay" if sys.platform == "darwin" else "mpg123"
            subprocess.run([player, str(AUDIO_TMP)],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception as e:
            print(f"[ALERTE VOCALE ERREUR] {e}", file=sys.stderr)


def main():
    ap = argparse.ArgumentParser(description="Alerte vocale en boucle ACE777")
    ap.add_argument("--message", required=True, help="Message à répéter à voix haute")
    ap.add_argument("--id", required=True, help="Identifiant unique de l'alerte")
    ap.add_argument("--arret", action="store_true", help="Forcer l'arrêt immédiat")
    args = ap.parse_args()

    if args.arret:
        for f in fichiers_arret(args.id):
            try:
                f.unlink()
            except Exception:
                pass
        print(f"Arrêt forcé demandé pour l'alerte {args.id}.")
        sys.exit(0)

    # Journal d'alerte
    try:
        ALERTES_DIR.mkdir(parents=True, exist_ok=True)
        ecriture_atomique(
            ALERTES_DIR / f"ALERTE_{args.id}.json",
            json.dumps({
                "id": args.id,
                "message": args.message,
                "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "status": "actif",
            }, ensure_ascii=False, indent=2))
    except Exception:
        pass

    # FIX 31/08 : remplacer toute boucle du même message avant de démarrer.
    tuer_doublons(args.message)
    cle_dedup = _cle_dedup(args.message)
    pid_file_dedup = DEDUP_DIR / f"{cle_dedup}.pid"

    print(f"🔊 Alerte vocale en boucle (id {args.id}). "
          "Arrêt : touch STOP_ALERTE ou arret_alerte.", file=sys.stderr)

    # DISTINCTION ALARME vs RAPPEL (31/08, GO Christophe) : la 1re lecture est
    # l'alarme ; chaque répétition suivante (toutes les 30s) est PRÉCÉDÉE de
    # "Rappels. " pour qu'on sache que c'est la MÊME alerte qui se répète,
    # pas un nouvel événement. Plus de confusion "est-ce nouveau ?".
    iteration = 0
    while True:
        if verifier_arret(args.id):
            try:
                subprocess.run(["killall", "edge_tts"], stderr=subprocess.DEVNULL,
                               stdout=subprocess.DEVNULL)
            except Exception:
                pass
            print(f"Arrêt de l'alerte vocale {args.id}.", file=sys.stderr)
            sys.exit(0)

        if iteration == 0:
            texte = args.message
        else:
            texte = f"Rappels. {args.message}"
        parler(texte)
        iteration += 1

        # Pause découpée en tranches pour réagir vite à l'arrêt
        for _ in range(INTERVALLE_SEC // PAUSE_SEC):
            if verifier_arret(args.id) or _liberer_si_remplace(pid_file_dedup):
                print(f"Arrêt de l'alerte vocale {args.id}.", file=sys.stderr)
                sys.exit(0)
            time.sleep(PAUSE_SEC)


def _liberer_si_remplace(pid_file_dedup) -> bool:
    """Vrai si notre pid_file a été repris par un AUTRE process (la boucle
    a été remplacée par une nouvelle instance du même message) → on s'arrête."""
    try:
        if not pid_file_dedup.exists():
            return False
        cur = pid_file_dedup.read_text(encoding="utf-8").strip()
        return cur != str(os.getpid())
    except Exception:
        return False


if __name__ == "__main__":
    main()

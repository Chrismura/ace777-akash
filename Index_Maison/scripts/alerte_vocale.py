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
    """Lit le message à voix haute (edge_tts → mp3 → afplay), une seule piste."""
    try:
        subprocess.run(["killall", "say"], stderr=subprocess.DEVNULL,
                       stdout=subprocess.DEVNULL)
        subprocess.run(["killall", "edge_tts"], stderr=subprocess.DEVNULL,
                       stdout=subprocess.DEVNULL)
    except Exception:
        pass
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

    print(f"🔊 Alerte vocale en boucle (id {args.id}). "
          "Arrêt : touch STOP_ALERTE ou arret_alerte.", file=sys.stderr)

    while True:
        if verifier_arret(args.id):
            try:
                subprocess.run(["killall", "edge_tts"], stderr=subprocess.DEVNULL,
                               stdout=subprocess.DEVNULL)
            except Exception:
                pass
            print(f"Arrêt de l'alerte vocale {args.id}.", file=sys.stderr)
            sys.exit(0)

        parler(args.message)

        # Pause découpée en tranches pour réagir vite à l'arrêt
        for _ in range(INTERVALLE_SEC // PAUSE_SEC):
            if verifier_arret(args.id):
                print(f"Arrêt de l'alerte vocale {args.id}.", file=sys.stderr)
                sys.exit(0)
            time.sleep(PAUSE_SEC)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cortana_yeux.py — Les YEUX de Cortana (prototype 11/08)
========================================================
Vision A LA DEMANDE, 100% hub, 0 IA locale.

Flux :  capture ecran (ou image donnee) -> redimensionnement sips
        -> base64 -> hub (task=cortana.yeux -> Gemini vision)
        -> analyse en francais -> lecture vocale Vivienne (option)

Cortana ne regarde QUE quand on le lui demande. Jamais en continu.
Aucune dependance Python supplementaire (edge_tts deja installe
pour cortana_brief.py ; screencapture/sips natifs macOS).

Usage :
  python3 cortana_yeux.py                    # regarde et affiche
  python3 cortana_yeux.py --speak            # + lecture vocale Vivienne
  python3 cortana_yeux.py --question "..."   # question personnalisee
  python3 cortana_yeux.py --image photo.png  # analyser une image donnee
  python3 cortana_yeux.py --out /tmp/note.md # sauver l'analyse

Confidentialite : l'image (capture d'ecran) part en base64 vers Gemini
(hub cloud). A ne lancer que quand on accepte de montrer l'ecran au cloud.
"""

import argparse
import base64
import json
import os
import shutil
import subprocess
import sys
import threading
import urllib.request

import barge_in  # micro : coupe la parole si on parle (natif, ffmpeg)

HUB = "http://127.0.0.1:11435/v1/chat/completions"
HEALTH = HUB.replace("/v1/chat/completions", "/health")
TASK = "cortana.yeux"          # routage hub : gemini (vision)
VOICE = "fr-FR-VivienneMultilingualNeural"
RATE = os.environ.get("EDGE_TTS_RATE", "-25%")  # style Cortana : plus calme
MAX_PX = 1280                  # taille max cote le plus long
MAX_OCTETS = 3 * 1024 * 1024   # garde anti-payload geant
TMP_RAW = "/tmp/cortana_yeux_raw.png"
TMP_JPG = "/tmp/cortana_yeux.jpg"
TMP_IMG = "/tmp/cortana_yeux_img.jpg"
TMP_MP3 = "/tmp/cortana_yeux.mp3"

HUB = "http://127.0.0.1:11435/v1/chat/completions"
TASK = "cortana.yeux"          # routage hub : gemini (vision)
VOICE = "fr-FR-VivienneMultilingualNeural"
RATE = os.environ.get("EDGE_TTS_RATE", "-25%")  # style Cortana : plus calme

QUESTION_DEFAUT = (
    "Tu es les yeux de Cortana, l'assistante vocale de la maison ACE777. "
    "Regarde ce qui est affiche a l'ecran et decris-le en 2 a 4 phrases courtes, "
    "en francais, factuel et precis : quelles fenetres/onglets sont visibles, "
    "quelles donnees ou chiffres, et l'etat general. Si tu vois une alerte ou "
    "un probleme (erreur, rouge, crash), signale-le clairement."
)


def speak_text(text, voice=VOICE, rate=RATE):
    """Lecture vocale Vivienne via python3 -m edge_tts (meme mecanisme que cortana_brief)."""
    try:
        if barge_in.activ():
            barge_in.preparer()  # calibration ambiant EN SILENCE, pendant la generation
        subprocess.run(
            ["python3", "-m", "edge_tts", "--voice", voice, f"--rate={rate}",
             "--text", text, "--write-media", TMP_MP3],
            check=True, capture_output=True, timeout=120)
        player = subprocess.Popen(["afplay", TMP_MP3])
        if barge_in.activ():
            threading.Thread(target=barge_in.surveiller, args=(player,), daemon=True).start()
        player.wait(timeout=120)
        return True
    except subprocess.CalledProcessError as e:
        detail = (e.stderr or b"").decode(errors="replace").strip()
        print(f"  [i] lecture vocale impossible : {e}{' — ' + detail if detail else ''}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"  [i] lecture vocale impossible : {e}", file=sys.stderr)
        return False


def preparer_image(src, out, max_px=MAX_PX):
    """Redimensionne (sips natif) en JPEG <= max_px. Verifie la taille finale."""
    subprocess.run(["sips", "-Z", str(max_px), "-s", "format", "jpeg", src,
                    "--out", out], check=True, capture_output=True)
    size = os.path.getsize(out)
    if size > MAX_OCTETS:
        raise RuntimeError(f"image trop grosse : {size} octets")
    return out


def capture_ecran():
    """Capture l'ecran (screencapture natif) et la prepare. JPEG ~90 Ko."""
    subprocess.run(["screencapture", "-x", TMP_RAW], check=True, capture_output=True)
    return preparer_image(TMP_RAW, TMP_JPG)


def nettoyer_tmp():
    """Supprime les fichiers temporaires de la session (sauf si l'image source est dedans)."""
    for p in (TMP_RAW, TMP_JPG, TMP_IMG, TMP_MP3):
        try:
            os.remove(p)
        except FileNotFoundError:
            pass


def image_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def call_hub(image_b64, question):
    payload = {
        "task": TASK,   # routage : gemini vision (quota 30/j)
        "messages": [{
            "role": "user",
            "content": [
                {"type": "text", "text": question},
                {"type": "image_url", "image_url": {
                    "url": "data:image/jpeg;base64," + image_b64}},
            ],
        }],
        "max_tokens": 500,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    content = d["choices"][0]["message"]["content"]
    return content, d.get("provider", "?")


def main():
    ap = argparse.ArgumentParser(description="Les yeux de Cortana (vision a la demande via hub)")
    ap.add_argument("--speak", action="store_true", help="lire l'analyse a voix haute (Vivienne)")
    ap.add_argument("--question", default=QUESTION_DEFAUT, help="question/consigne personnalisee")
    ap.add_argument("--image", default=None, help="analyser une image donnee au lieu de capturer l'ecran")
    ap.add_argument("--out", default=None, help="sauver l'analyse dans ce fichier")
    args = ap.parse_args()

    # 1) hub vivant ?
    try:
        with urllib.request.urlopen(HEALTH, timeout=5) as r:
            json.loads(r.read().decode())
    except Exception:
        print("[X] Hub :11435 injoignable. Lance le hub, puis relance.", file=sys.stderr)
        sys.exit(1)

    # 2) capture ou image donnee
    try:
        if args.image:
            src = args.image
            if not os.path.isfile(src):
                print(f"[X] image introuvable : {src}", file=sys.stderr)
                sys.exit(1)
            # normalise en JPEG resize pour rester leger
            img = preparer_image(src, TMP_IMG)
            print("[i] analyse de l'image fournie ...")
        else:
            img = capture_ecran()
            print("[i] capture ecran ...")
    except subprocess.CalledProcessError as e:
        print(f"[X] capture/redimensionnement impossible : {e}", file=sys.stderr)
        print("    (Permission d'enregistrement d'ecran requise : Systeme > Confidentialite > Enregistrement d'ecran)", file=sys.stderr)
        sys.exit(1)

    size_kb = os.path.getsize(img) // 1024
    print(f"[i] image pret : {size_kb} Ko")

    # 3) vision via hub
    try:
        print("[i] la Reine regarde (hub -> Gemini vision) ...")
        b64 = image_to_base64(img)
        analyse, provider = call_hub(b64, args.question)
    except urllib.error.HTTPError as e:
        print(f"[X] le hub a repondu HTTP {e.code} : {e.read().decode()[:300]}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"[X] vision impossible : {e}", file=sys.stderr)
        sys.exit(1)

    # 4) affichage + sauvegarde + voix
    print("")
    print("━━━ 👁️ CORTANA A REGARDÉ ━━━")
    print(analyse)
    print(f"━━━━ (provider : {provider}) ━━━━")
    print("")

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write("# Cortana — vision à la demande\n\n" + analyse + "\n")
        print(f"[OK] analyse sauvee : {args.out}")

    if args.speak:
        print("  ▶ lecture vocale (Vivienne)...", file=sys.stderr)
        speak_text(analyse)

    nettoyer_tmp()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""cortana_brief.py — briefs vocaux ENRICHIS par IA (via hub Prise IA)
========================================================================
Cortana est aujourd'hui 100 % à base de règles (cortana_thermo.py).
Ce script ajoute une couche LLM OPTIONNELLE : il prend le brief brut
et le reformule en langage naturel via le hub (routage task=cortana.brief
-> Qwen local par défaut, privé et gratuit ; --model gemini pour comparer).

Usage :
  python3 cortana_brief.py                 # brief horaire enrichi (Qwen local)
  python3 cortana_brief.py --model gemini  # force Gemini (comparaison qualité)
  python3 cortana_brief.py --text "..."    # enrichir un texte arbitraire

La voix reste gérée par cortana_voice.py (TTS). Ce script ne parle JAMAIS.
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile
import urllib.request

SCRIPTS = os.path.expanduser("~/ace777-test-day1/Index_Maison/scripts")
HUB = "http://127.0.0.1:11435/v1/chat/completions"

SYSTEM = (
    "Tu es la voix de Cortana, l'assistante vocale de la maison ACE777. "
    "Reformule le brief ci-dessous en 3-4 phrases naturelles, vivantes et concises, "
    "prêtes à être lues à voix haute. Garde les chiffres clés mais évite les listes "
    "techniques. Pas de préambule, pas de markdown, pas d'emoji."
)


def speak_text(text, voice="fr-FR-VivienneMultilingualNeural", rate="-15%"):
    """Voix Vivienne via python3 -m edge_tts (meme mecanisme que cortana_voice)."""
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
        path = f.name
    cmd = [
        "python3", "-m", "edge_tts",
        "--voice", voice,
        f"--rate={rate}",
        "--text", text,
        "--write-media", path,
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=90, check=False)
    if proc.returncode != 0 or not os.path.exists(path) or os.path.getsize(path) < 100:
        print("  ✘ generation voix echouee", file=sys.stderr)
        if os.path.exists(path):
            os.unlink(path)
        return 1
    subprocess.run(["afplay", path], check=False, timeout=180)
    os.unlink(path)
    return 0


def rule_brief():
    """Brief brut actuel (logique existante, texte seul — aucun son)."""
    r = subprocess.run(
        [sys.executable, os.path.join(SCRIPTS, "cortana_thermo.py"), "horaire"],
        capture_output=True, text=True, timeout=180,
    )
    out = (r.stdout or "").strip()
    return out or "(brief horaire indisponible)"


def call_hub(text, force_gemini=False):
    payload = {
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": text},
        ],
        "temperature": 0.5,
        "max_tokens": 400,
    }
    if force_gemini:
        payload["model"] = "gemini"
    else:
        payload["task"] = "cortana.brief"  # routage : Qwen local par défaut
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=None) as resp:
        data = json.load(resp)
    content = data["choices"][0]["message"]["content"]
    return content, data.get("provider", "?")


def main():
    ap = argparse.ArgumentParser(description="Brief Cortana enrichi par IA")
    ap.add_argument("--model", choices=["auto", "gemini"], default="auto",
                    help="auto = routage du hub (Qwen local) ; gemini = force Gemini")
    ap.add_argument("--text", default=None, help="texte arbitraire à enrichir")
    ap.add_argument("--speak", action="store_true", help="lire le resultat a voix haute (Vivienne)")
    a = ap.parse_args()

    text = a.text if a.text else rule_brief()
    content, provider = call_hub(text, force_gemini=(a.model == "gemini"))
    print("[provider: %s]" % provider, file=sys.stderr)
    if a.speak:
        print("  ▶ lecture vocale (Vivienne)...", file=sys.stderr)
        return speak_text(content)
    print(content)
    return 0


if __name__ == "__main__":
    sys.exit(main())

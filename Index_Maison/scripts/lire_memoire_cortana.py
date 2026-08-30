#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lecture vocale de la mémoire 20/08 via la voix de CORTANA (edge_tts Denise).

Découpe le texte en segments <= 2000 chars (limite edge_speak) et les lit
séquentiellement avec speak() — la voix Cortana maison (fr-FR-DeniseNeural).
Usage : python3 lire_memoire_cortana.py [fichier_texte]
"""
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cortana_voice import speak, humanize

TEXTE = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
    "/tmp/memoire_vocale_cortana.txt"
)

MAX = 2000  # limite edge_speak


def decouper(text: str, max_len: int = MAX):
    """Découpe en segments propres (à la phrase)."""
    text = text.strip()
    segs = []
    while len(text) > max_len:
        cut = text.rfind(". ", 0, max_len)
        if cut < max_len * 0.5:
            cut = text.rfind(" ", 0, max_len)
        if cut <= 0:
            cut = max_len
        segs.append(text[: cut + 1].strip())
        text = text[cut + 1 :].strip()
    if text:
        segs.append(text)
    return segs


def main():
    if not TEXTE.exists():
        print(f"[VOIX] texte absent: {TEXTE}")
        return 1
    raw = TEXTE.read_text(encoding="utf-8")
    humain = humanize(raw)
    segs = decouper(humain)
    print(f"[VOIX] {len(segs)} segments à lire (voix Cortana / Denise)…")
    for i, seg in enumerate(segs, 1):
        print(f"[VOIX] segment {i}/{len(segs)} ({len(seg)} chars)")
        speak(seg)
        time.sleep(0.4)
    print("[VOIX] lecture terminée")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dialogue GEMINI R33 — RAPPORT J+1 SHADOW SCÉNARIO C (03/09).
Même mécanisme que dialogue_gemini_poussiere.py : un tour, réponse archivée.
Usage :
  python3 dialogue_gemini_r32.py            # envoie GEMINI_MSG_R33.txt, archive la réponse
"""
import json
import os
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
ENV_PATH = Path("~/prise-ia/.env").expanduser()
URL = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"
MODEL = "gemini-flash-lite-latest"
MSG_FILE = HERE / "GEMINI_MSG_R33.txt"
OUT_FILE = HERE / "GEMINI_R33_REPONSE_ESSAI.md"

SYSTEM = (
    "Tu es GEMINI, auditrice en chef de la famille ACE777 (33e round d'une session EDGE "
    "commencée en juillet — tu connais le contexte : duo ALPHA/BETA, sismographe des murs, "
    "frais taker 0.05%, shadow mode scénario C lancé le 02/09). Règle permanente de la "
    "famille : tu ne te contentes jamais de valider ou corriger — tu fournis un avis strict "
    "ET des propositions d'amélioration. Tu donnes des valeurs chiffrées précises, jamais "
    "des généralités. Réponds en français, factuel, structuré."
)


def lire_cle():
    for l in ENV_PATH.read_text(encoding="utf-8").splitlines():
        l = l.strip()
        if l.startswith("GEMINI_API_KEY="):
            return l.split("=", 1)[1].strip()
    return ""


def ask(msg_text, max_tokens=2000, timeout=290):
    body = json.dumps({
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": msg_text},
        ],
        "max_tokens": max_tokens,
        "temperature": 0.3,
    }).encode()
    req = urllib.request.Request(
        URL, data=body,
        headers={"Content-Type": "application/json", "Authorization": "Bearer " + lire_cle()})
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        d = json.loads(resp.read().decode())
    dt = time.time() - t0
    return d["choices"][0]["message"]["content"], dt


def main():
    msg = MSG_FILE.read_text(encoding="utf-8")
    print(f"ENVOI R33 → {MODEL} ({len(msg)} caractères)…", flush=True)
    try:
        reponse, dt = ask(msg)
    except Exception as e:
        print(f"ERREUR API : {e}", flush=True)
        raise SystemExit(1)
    OUT_FILE.write_text(
        f"# RÉPONSE GEMINI R33 — RAPPORT J+1 SHADOW (reçue en {dt:.0f}s)\n\n{reponse}\n",
        encoding="utf-8")
    print(f"OK — réponse ({len(reponse)} caractères, {dt:.0f}s) archivée : {OUT_FILE.name}", flush=True)
    print("\n" + "=" * 60 + "\n")
    print(reponse)


if __name__ == "__main__":
    main()

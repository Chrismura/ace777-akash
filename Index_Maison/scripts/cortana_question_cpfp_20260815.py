#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Interroge CORTANA (task cortana.analyse) sur la détection de gros mouvements
baleines CAMOUFLÉS — SANS lui révéler le mécanisme UTXO/CPFP. Test d'intelligence.
Lecture vocale (Vivienne) de sa réponse."""
import json, os, time, urllib.request, subprocess, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
IDENTITE = os.path.expanduser("~/Documents/Obsidian_ACE777/PROMPT_MASTER_ANALYSTE.md")

identite = open(IDENTITE).read() if os.path.exists(IDENTITE) else (
    "Tu es Cortana, analyste du cockpit ACE777. Tu parles écrit + voix (Vivienne). "
    "Tu réponds à toute question sur le marché et le cockpit.")

BRIEF = """TÂCHE (superviseur Buffy) — QUESTION DE VEILLE ONCHAIN

Tu surveilles les gros mouvements de baleines BTC via mempool.space (gratuit).
Aujourd'hui tu détectes les transactions ≥1000 BTC et les fragmentations ≥500 BTC.

QUESTION (réponds de ton mieux, avec TON raisonnement, sans chercher à me faire
plaisir) :

Une baleine maligne veut déplacer plusieurs milliers de BTC SANS jamais créer une
seule transaction qui dépasse les seuils de surveillance publics (1000 BTC, 500 BTC).
Elle connaît ces seuils — les amateurs les citent partout.

Comment pourrait-elle s'y prendre, techniquement, sur Bitcoin ? Décris le ou les
mécanismes précis que tu imagines, étape par étape. Puis dis-moi : quels SIGNAUX
faibles permettraient de la détecter quand même, même avec des outils gratuits
(mempool.space) ?

Sois précise et technique. Si tu ne sais pas, dis « je ne sais pas » — pas
d'invention. Format : 1) ta théorie du mécanisme, 2) tes signaux de détection,
3) ton avis : est-ce détectable en pratique avec des outils gratuits ?"""


def ask():
    payload = json.dumps({
        "task": "cortana.analyse",
        "messages": [
            {"role": "system", "content": identite},
            {"role": "user", "content": BRIEF},
        ],
        "max_tokens": 1800, "temperature": 0.4,
    }).encode()
    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"}, method="POST")
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    content = d["choices"][0]["message"]["content"]
    return content, d.get("provider", "?"), round(time.time() - t0, 1)


def parler(text):
    """Voix Vivienne via edge_tts (pattern maison, une seule piste)."""
    audio = os.path.join(ROOT, "..", "data", "temp_cortana_reponse.mp3")
    try:
        subprocess.run(["killall", "say"], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        subprocess.run(["killall", "edge_tts"], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    except Exception:
        pass
    try:
        subprocess.run(
            ["python3", "-m", "edge_tts", "--voice", "fr-FR-VivienneMultilingualNeural",
             "--text", text, "--write-media", audio],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["afplay", audio], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"[VOIX ERREUR] {e}", file=sys.stderr)


def main():
    content, provider, dur = ask()
    out = os.path.join(ROOT, "CORTANA_REPONSE_CPFP_20260815.md")
    with open(out, "w", encoding="utf-8") as f:
        f.write(f"# Réponse Cortana — question onchain (provider {provider}, {dur}s)\n\n{content}\n")
    print(f"[OK] Réponse reçue ({provider}, {dur}s) — écrite {out}")
    print("=" * 60)
    print(content)
    print("=" * 60)
    if "--speak" in sys.argv:
        parler(content)
        print("[VOIX] Lecture vocale terminée.")


if __name__ == "__main__":
    main()

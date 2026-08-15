#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Révèle à CORTANA la pépite UTXO/CPFP (camouflage de baleines) — elle l'a méritée.
Lecture vocale (Vivienne) + question : quels signaux précis surveillerait-elle maintenant ?"""
import json, os, time, urllib.request, subprocess, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
IDENTITE = os.path.expanduser("~/Documents/Obsidian_ACE777/PROMPT_MASTER_ANALYSTE.md")
identite = open(IDENTITE).read() if os.path.exists(IDENTITE) else (
    "Tu es Cortana, analyste du cockpit ACE777. Tu parles écrit + voix (Vivienne).")

BRIEF = """SUITE DE NOTRE ÉCHANGE (superviseur Buffy) — TU AS BIEN RÉPONDU, VOICI LA PÉPITE COMPLÈTE

Tu as identifié le fractionnement, les frais identiques et le clustering — très bon.
Mais il manquait le MÉCANISME PRÉCIS que Christophe a trouvé (sa pépite). Le voici :

LE CAMOUFLAGE UTXO + CPFP (le vrai coup des baleines malignes) :

1. LE BILLET (UTXO) : un UTXO est INDIVISIBLE. Pour déplacer plusieurs milliers de
   BTC, la baleine ne peut pas « couper » — elle dépense le billet entier et reçoit
   le reste en « monnaie rendue » (change).

2. LE CAMOUFLAGE : elle éclate le tout en un ARBRE de milliers de micro-transactions
   de POUSSIÈRE (dust) à FRAIS QUASI NULS. Elles dorment invisibles au fond de la
   mempool (frais trop bas = jamais incluses, donc jamais analysées).

3. LE DÉCLENCHEUR (CPFP = Child Pays For Parent) : elle crée une transaction « ENFANT »
   finale avec des FRAIS ASTRONOMIQUES, qui dépend d'une sortie de l'arbre de poussière.

4. L'EXÉCUTION : le mineur est ÉCONOMIQUEMENT OBLIGÉ de valider tout l'arbre parent
   (même à frais zéro) pour encaisser la prime de la transaction enfant. Le bloc se
   règle d'un coup.

5. L'EXPULSION : ce bloc massif instantané s'accapare tout l'espace, expulsant les
   frais et les transactions des petits porteurs hors du bloc.

CONSÉQUENCE : une baleine déplace des milliers de BTC SANS JAMAIS créer une seule
transaction ≥ 1000 BTC. Les seuils fixes sont aveugles.

MAINTENANT — TA MISSION (à voix haute et par écrit) :
Sachant que les frais astronomiques de l'enfant sont INCONTOURNABLES (c'est le
mécanisme lui-même), et que la poussière s'accumule pendant des heures/jours AVANT
l'exécution : quels SIGNAUX PRÉCIS surveillerais-tu sur mempool.space (gratuit) pour
détecter ce camouflage en avance ? Donne tes 3 meilleurs signaux, avec pour chacun :
le seuil concret et la fiabilité (forte/moyenne/faible). Sois précise."""


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
    audio = os.path.join(ROOT, "..", "data", "temp_cortana_cpfp.mp3")
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
    out = os.path.join(ROOT, "CORTANA_REPONSE_CPFP_V2_20260815.md")
    with open(out, "w", encoding="utf-8") as f:
        f.write(f"# Réponse Cortana v2 — après révélation de la pépite (provider {provider}, {dur}s)\n\n{content}\n")
    print(f"[OK] Réponse v2 reçue ({provider}, {dur}s) — écrite {out}")
    print("=" * 60)
    print(content)
    print("=" * 60)
    if "--speak" in sys.argv:
        parler(content)
        print("[VOIX] Lecture vocale terminée.")


if __name__ == "__main__":
    main()

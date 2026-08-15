#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Soumet la SPEC relance duo harmonie au CODEUR (task code.ia).

Circuit : famille 6/6 -> JUGE GO AVEC RESERVES -> codeur -> grille -> famille
-> GO Christophe -> retest. Clause permanente Christophe : prouver la
meilleure logique.
"""
import json
import os
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
ROOT = "/Users/christophe/ace777-test-day1"
SPEC_PATH = os.path.join(ROOT, "SPEC_relance_duo_harmonie_v1.md")
OUT = os.path.join(ROOT, "Index_Maison", "CODE_relance_duo_harmonie.md")

with open(SPEC_PATH, encoding="utf-8") as f:
    SPEC = f.read()

PROMPT = """\
Tu es le CODEUR de la famille ACE777 (task code.ia). Ecris le code demande,
borne a la tache, rien d'autre. Aucune reecriture, aucune feature.

CLAUDE PERMANENTE (Christophe, 14/08 — a respecter a CHAQUE correction) :
« Prouve la meilleure logique et applique-la dans la correction et
l'amelioration si possible. »
→ Tu dois (1) PROUVER que ta correction est la meilleure logique (pas une
rustine), et (2) proposer/appliquer UNE amelioration si elle est PROUVEE
(mesurable, bornee, sans effet de bord). Rien au-dela de la SPEC.

================
LA SPEC A EXECUTER (validee par le JUGE — GO AVEC RESERVES)
================
""" + SPEC + """

================
LIVRABLES (contrat de sortie — section 5 de la SPEC)
================
1. Code bash complet : fonction reset_duo_harmony() + les 2 points d'insertion
   (GO_VORTEX_V2.sh avant exec ; launch_vortex_v2_collab_4h_binance.sh au debut
   de la boucle) + le bloc STOP double mort. Compatible bash 3.2 macOS.
2. La section PREUVE « meilleure logique » (obligatoire).
3. L'amelioration prouvee proposee (UNE, optionnelle si prouvee).
4. Rien d'autre.

RENDS : ton code + preuve, en francais, concis.
"""


def main():
    payload = {
        "task": "code.ia",
        "messages": [{"role": "user", "content": PROMPT}],
        "max_tokens": 3000,
        "temperature": 0.2,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    print("=== CODEUR (code.ia) — RELANCE DUO HARMONIE ===", flush=True)
    try:
        with urllib.request.urlopen(req, timeout=None) as resp:
            d = json.loads(resp.read().decode("utf-8"))
        rep = d["choices"][0]["message"]["content"].strip()
        provider = d.get("provider", "?")
    except Exception as e:
        rep = "[CODEUR INJOIGNABLE] " + str(e)[:200]
        provider = "?"
    print("provider: " + provider + "\n")
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("# RÉPONSE CODEUR (task code.ia · " + provider + ") — " + __import__("datetime").datetime.utcnow().isoformat() + "Z\n\n" + rep + "\n")
    print(rep)
    print("\n[OK] écrit dans " + OUT, flush=True)


if __name__ == "__main__":
    main()

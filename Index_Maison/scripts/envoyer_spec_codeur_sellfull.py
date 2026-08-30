#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""envoyer_spec_codeur_sellfull.py — Envoie la SPEC v2 (SELL full cascade) au CODEUR.

Circuit validé : SPEC v2 (famille SOUS CONDITION + verrous) → CODEUR (task code.ia)
→ relecture Buffy (chef scientifique) → GO Christophe → test --resume → déploiement.

Le codeur produit des DIFFS EXACTS, bornés à la SPEC, avec la section PREUVE
(clause permanente Christophe 14/08 : « prouve la meilleure logique »).
"""
import json
import os
import sys
import time
import urllib.request
from datetime import datetime, timezone

ROOT = "/Users/christophe/ace777-test-day1"
HUB = "http://127.0.0.1:11435/v1/chat/completions"
SPEC_PATH = os.path.join(ROOT, "hulk-mexc/docs/SPEC_FIX_SELL_FULL_v2_2026-08-29.md")
TARGET = os.path.join(ROOT, "hulk-mexc/scripts/paper_diprip.py")
OUT = os.path.join(ROOT, "hulk-mexc/docs/CODE_SELL_FULL_2026-08-29.md")


def main():
    spec = open(SPEC_PATH, encoding="utf-8").read()
    # Contexte du fichier cible : les lignes autour des déclencheurs (pour ancrer le diff)
    lines = open(TARGET, encoding="utf-8").read().splitlines()
    ctx_1894 = "\n".join(f"{i+1}: {l}" for i, l in enumerate(lines[1885:1900]))
    ctx_1918 = "\n".join(f"{i+1}: {l}" for i, l in enumerate(lines[1910:1925]))
    ctx_1940 = "\n".join(f"{i+1}: {l}" for i, l in enumerate(lines[1932:1946]))
    ctx_sell = "\n".join(f"{i+1}: {l}" for i, l in enumerate(lines[1645:1675]))

    prompt = (
        "Tu es le CODEUR de confiance de la maison ACE777 (task code.ia).\n"
        "Tu produis des DIFFS EXACTS, sans paraphrase, sans inventer, sans réécrire autre "
        "chose que ce qui est demandé. Aucune feature au-delà de la SPEC.\n\n"
        "CLAUDE PERMANENTE (Christophe, 14/08) : « Prouve la meilleure logique et applique-la "
        "dans la correction et l'amélioration si possible. »\n"
        "→ Tu dois (1) PROUVER que ta correction est la meilleure logique (avec la simulation "
        "chiffrée demandée dans la SPEC), et (2) proposer/appliquer UNE amélioration si elle est "
        "PROUVEE (mesurable, bornée, sans effet de bord). Rien au-delà de la SPEC.\n\n"
        "========== LA SPEC À EXÉCUTER (validée SOUS CONDITION par la famille + Cortana) ==========\n"
        + spec +
        "\n\n========== CONTEXTE DU FICHIER CIBLE (lignes réelles actuelles, pour ancrer le diff) ==========\n"
        "--- sell_trade (l.1645-1675) ---\n" + ctx_sell +
        "\n--- zone stop 1 (l.1886-1900) ---\n" + ctx_1894 +
        "\n--- zone stop 2 (l.1911-1925) ---\n" + ctx_1918 +
        "\n--- zone trailing (l.1933-1946) ---\n" + ctx_1940 +
        "\n\n========== LIVRABLES (contrat de sortie) ==========\n"
        "1. Les DIFFS exacts à appliquer dans paper_diprip.py (les 4 blocs + 3 verrous de la "
        "SPEC v2), avec les numéros de lignes avant/après.\n"
        "2. La section PREUVE « meilleure logique » OBLIGATOIRE : simule sur les données passées "
        "combien les -153$ de SELL full se seraient réduits avec la règle (méthode : appliquer "
        "la garde aux 166 SELL full réels enregistrés, amplitude >12% → partiel 50%).\n"
        "3. Les paramètres à ajouter dans defaults.env (config réversible).\n"
        "4. UNE amélioration prouvée (optionnelle si prouvée).\n"
        "5. Rien d'autre.\n\n"
        "RENDS : les diffs + la preuve, en français, concis."
    )

    payload = {
        "task": "code.ia",
        "messages": [
            {"role": "system", "content":
             "Tu es le codeur de confiance d'ACE777. Tu produis des diffs exacts, sans "
             "paraphrase, sans inventer. Tu ne modifies jamais autre chose que ce qui est demandé."},
            {"role": "user", "content": prompt},
        ],
        "max_tokens": 4000,
        "temperature": 0.1,
    }
    print("=== ENVOI AU CODEUR (task code.ia) — SPEC v2 SELL FULL ===", flush=True)
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode("utf-8"))
    content = d["choices"][0]["message"]["content"].strip()
    provider = d.get("provider", "?")
    secs = round(time.time() - t0, 1)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(f"# Réponse codeur — SPEC v2 SELL FULL (provider {provider}, {secs}s, "
                f"{datetime.now(timezone.utc).isoformat()})\n\n{content}\n")
    print(f"[OK] provider={provider} ({secs}s)\nRéponse sauvegardée : {OUT}", flush=True)


if __name__ == "__main__":
    main()
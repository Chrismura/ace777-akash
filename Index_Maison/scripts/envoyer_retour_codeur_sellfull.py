#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""envoyer_retour_codeur_sellfull.py — 2e passe CODEUR (SELL full).

Chef scientifique (Buffy) a relu le diff du codeur et trouvé 2 corrections
obligatoires (sc hors scope → crash ; configs jamais chargées → verrou 3 non
respecté). On renvoie au codeur : le diff original + le retour, il produit le
diff corrigé complet et appliquable. Circuit : codeur → relecture Buffy →
GO Christophe → test --resume sur copie → déploiement.
"""
import json
import os
import time
import urllib.request
from datetime import datetime, timezone

ROOT = "/Users/christophe/ace777-test-day1"
HUB = "http://127.0.0.1:11435/v1/chat/completions"
DIFF_ORIG = os.path.join(ROOT, "hulk-mexc/docs/CODE_SELL_FULL_2026-08-29.md")
RETOUR = os.path.join(ROOT, "hulk-mexc/docs/RETOUR_CODEUR_SELL_FULL_2e_passe.md")
TARGET = os.path.join(ROOT, "hulk-mexc/scripts/paper_diprip.py")
OUT = os.path.join(ROOT, "hulk-mexc/docs/CODE_SELL_FULL_v2_CORRIGE_2026-08-29.md")


def main():
    diff_orig = open(DIFF_ORIG, encoding="utf-8").read()
    retour = open(RETOUR, encoding="utf-8").read()
    lines = open(TARGET, encoding="utf-8").read().splitlines()
    # Ancrage : le début de manage_open + le chargement des configs dans __init__
    ctx_manage = "\n".join(f"{i+1}: {l}" for i, l in enumerate(lines[1871:1880]))
    ctx_init = "\n".join(f"{i+1}: {l}" for i, l in enumerate(lines[525:535]))

    prompt = (
        "Tu es le CODEUR de confiance de la maison ACE777 (task code.ia).\n"
        "Ton diff précédent a été relu par le chef scientifique et REFUSÉ en l'état :\n"
        "2 corrections obligatoires (détail complet dans le RETOUR ci-dessous).\n\n"
        "CLAUDE PERMANENTE (Christophe, 14/08) : « Prouve la meilleure logique et applique-la "
        "dans la correction et l'amélioration si possible. »\n"
        "→ Tu produis des DIFFS EXACTS, sans paraphrase, sans inventer, bornés à la SPEC v2 "
        "et au retour. Aucune feature au-delà. Rien d'autre que ce qui est demandé.\n\n"
        "========== TON DIFF PRÉCÉDENT (à corriger) ==========\n"
        + diff_orig +
        "\n\n========== LE RETOUR DU CHEF SCIENTIFIQUE (à intégrer intégralement) ==========\n"
        + retour +
        "\n\n========== CONTEXTE RÉEL DU FICHIER CIBLE (pour ancrer les corrections) ==========\n"
        "--- début de manage_open (l.1872-1880) ---\n" + ctx_manage +
        "\n--- chargement des configs dans __init__ (l.526-535) ---\n" + ctx_init +
        "\n\n========== LIVRABLES (contrat de sortie) ==========\n"
        "1. Le diff COMPLET et APPLIQUABLE (les 2 hunks corrigés + le bloc __init__ avec les "
        "5 attributs chargés + defaults.env), avec numéros de lignes avant/après.\n"
        "2. Correction 1 OBLIGATOIRE : `sc = self.scores.get(pair) or {}` en tête de manage_open "
        "(juste après `p = self.pos[pair]`).\n"
        "3. Correction 2 OBLIGATOIRE : les 5 attributs chargés dans __init__ via cfg.get, et "
        "remplacer les getattr par des lectures directes self.*.\n"
        "4. Section PREUVE conservée et mise à jour si besoin (économie ~84,74 $).\n"
        "5. Rien d'autre.\n\n"
        "RENDS : le diff corrigé complet, en français, concis."
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
    print("=== ENVOI AU CODEUR (2e passe) — corrections SELL FULL ===", flush=True)
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
        f.write(f"# Réponse codeur — 2e passe SELL FULL corrigée (provider {provider}, {secs}s, "
                f"{datetime.now(timezone.utc).isoformat()})\n\n{content}\n")
    print(f"[OK] provider={provider} ({secs}s)\nRéponse sauvegardée : {OUT}", flush=True)


if __name__ == "__main__":
    main()

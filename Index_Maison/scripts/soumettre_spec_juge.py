#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""VALIDATION SPEC CORRECTION PANNE ALPHA rc=1 par le JUGE (14/08).

Circuit : JUGE valide la SPEC -> codeur (code.ia) -> grille test -> famille -> GO Christophe -> retest.
Ici : le JUGE tranche sur la SPEC_correction_panne_alpha_v1.md
(1) verdict GO / GO AVEC RESERVES / NON, (2) la SPEC est-elle bornee et conforme
C1 (genesis intouchable) ?, (3) le wrapper safe_call est-il la meilleure logique ?
(4) reserves / ameliorations GO-sized, (5) la grille de test est-elle suffisante ?
"""
import json
import os
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
ROOT = "/Users/christophe/ace777-test-day1"
SPEC_PATH = os.path.join(ROOT, "SPEC_correction_panne_alpha_v1.md")
OUT = os.path.join(ROOT, "Index_Maison", "VALIDATION_SPEC_PANNE_2026-08-14")
os.makedirs(OUT, exist_ok=True)

with open(SPEC_PATH, encoding="utf-8") as f:
    SPEC = f.read()

CONTEXTE = f"""\
VALIDATION DE LA SPEC DE CORRECTION — ALPHA meurt en rc=1 (mort silencieuse par
sous-shell sous set -e). Tu es le JUGE : tu tranches si la SPEC est bonne à
envoyer au codeur.

================
RAPPEL DES FAITS (preuves reelles, pas un recit)
================
1. RUN TEST 14/08 (GEMINI_TEST + crash dump, testnet) : ALPHA rc=1 a
   07:49:10Z, ~8 min apres le depart, juste apres le fill #42. BETA survit.
   Pattern identique au 13/08. Crash dump capture la fenetre de mort mais
   FATAL_RC1 VIDE (le trap ERR ne se propage pas dans les sous-shells /
   substitutions $(...) / pipelines sous set -e — angle mort GROK confirme).
2. Famille 6/6 (AUDIT_PANNE_2026-08-14) : zone fautive = public_get /
   curl_with_retry NON PROTEGES dans des substitutions $(...) (1599-1615 p1/
   depth_1/p2/depth_2, 1733-1745 book/klines) + helpers json_get (454) /
   num_* (677-684). Timing 9 s = 3 tentatives x 5 s de curl_with_retry.
3. Contrainte C1 : champion genesis INTANGIBLE — on ne modifie QUE le lanceur
   (wrapper). bash 3.2 macOS. Zéro changement du comportement nominal.
4. Clause permanente Christophe : « Prouver la meilleure logique et l'appliquer
   dans la correction et l'amelioration si possible » — a chaque consultation.

================
LA SPEC A VALIDER (SPEC_correction_panne_alpha_v1.md)
================
{SPEC}

================
TA MISSION (5 reponses nettes, JUGE)
================
1. VERDICT : GO / GO AVEC RESERVES / NON + raison courte et nette.
2. La SPEC est-elle BORNEE et conforme C1 (jamais genesis) ? Oui/non + 1 point faible eventuel.
3. safe_call est-il la MEILLEURE logique vs les alternatives (|| true brut,
   sous-shell, wrapper par ligne) ? Tranche.
4. RESERVES eventuelles (GO-sized, minimales) avant envoi au codeur.
5. La grille de test (5 items) est-elle SUFFISANTE pour valider le correctif ?
Reponds en francais, court et net, sans blabla.
"""


def ask():
    payload = {
        "task": "juge.tranche",
        "messages": [
            {"role": "system", "content": "Tu es le JUGE de la famille ACE777. Tu tranches formellement : GO / GO AVEC RESERVES / NON. Tu es exigeant, tu donnes une raison courte et nette."},
            {"role": "user", "content": CONTEXTE},
        ],
        "max_tokens": 1500,
        "temperature": 0.3,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=None) as resp:
            d = json.loads(resp.read().decode("utf-8"))
        return d["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"[INJOIGNABLE] {str(e)[:120]}"


if __name__ == "__main__":
    print("=== VALIDATION SPEC PANNE — JUGE ===\n", flush=True)
    rep = ask()
    print(rep, flush=True)
    with open(os.path.join(OUT, "AVIS_JUGE.md"), "w", encoding="utf-8") as f:
        f.write(f"# JUGE — Validation SPEC correction panne ALPHA rc=1\n\n{rep}\n")
    print(f"\n[OK] écrit dans {OUT}/AVIS_JUGE.md", flush=True)

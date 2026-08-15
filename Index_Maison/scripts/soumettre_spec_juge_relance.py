#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validation JUGE — SPEC relance duo harmonie (14/08).

Circuit : famille 6/6 (diagnostic) -> JUGE valide cette SPEC -> codeur ->
grille -> famille -> GO Christophe -> retest.
"""
import json
import os
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
ROOT = "/Users/christophe/ace777-test-day1"
SPEC_PATH = os.path.join(ROOT, "SPEC_relance_duo_harmonie_v1.md")
OUT = os.path.join(ROOT, "Index_Maison", "VALIDATION_SPEC_RELANCE_2026-08-14")
os.makedirs(OUT, exist_ok=True)

with open(SPEC_PATH, encoding="utf-8") as f:
    SPEC = f.read()

CONTEXTE = """\
VALIDATION DE LA SPEC RELANCE DUO (14/08) — tu es le JUGE : GO / GO AVEC
RESERVES / NON sur cette SPEC avant envoi au codeur.

RAPPEL (faits verifies famille 6/6, AUDIT_RUN_DUO_2026-08-14) :
- Correctif anti-mort safe_call VALIDE (genesis d6977337) : plus de crash
  technique, mais mort RELATIONNELLE duo (BETA shock_inversion_stop -> ALPHA
  stale_state TTL 20s -> mort en chaine). C'etait une sortie metier, pas un bug.
- Nouveau probleme (5/6, these Christophe) : la relance auto 4H ne resynchronise
  PAS le contrat duo. Session #2 : ALPHA voit tensions 1.5-6.03 mais bloque
  no_trigger/no_state 130+ cycles, zero fill. Le rm -f seul laisse une race
  window (etat SCOUT residuel / TTL perime lu par le nouvel ALPHA).
- Correctif propose (SPEC) : reset_duo_harmony() atomique (etat INIT/RESET
  explicite ecrit AVANT spawn) + STOP si double mort duo dans 300s (pas de
  relance sur marche mort). Cibles : GO_VORTEX_V2.sh + launch_vortex_v2_collab_
  4h_binance.sh. JAMAIS genesis. Bash 3.2. Zero changement nominal.

================
LA SPEC A VALIDER
================
""" + SPEC + """

================
TA MISSION (5 reponses nettes, JUGE)
================
1. VERDICT : GO / GO AVEC RESERVES / NON + raison courte.
2. La SPEC est-elle BORNEE et conforme C1 (genesis jamais touche) ?
3. Le reset d'harmonie + STOP double mort = meilleure logique ? Tranche vs
   alternatives (rm seul, etat vide, sleep avant spawn, desactiver relance).
4. RESERVES eventuelles (GO-sized) avant envoi au codeur.
5. La grille de test (5 items) suffit-elle ?
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
    print("=== VALIDATION SPEC RELANCE DUO — JUGE ===\n", flush=True)
    rep = ask()
    print(rep, flush=True)
    with open(os.path.join(OUT, "AVIS_JUGE.md"), "w", encoding="utf-8") as f:
        f.write("# JUGE — Validation SPEC relance duo harmonie\n\n" + rep + "\n")
    print("\n[OK] écrit dans " + OUT + "/AVIS_JUGE.md", flush=True)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Soumet la SPEC de correction panne ALPHA rc=1 au CODEUR (task code.ia).

Circuit : JUGE a validé la SPEC (GO AVEC RÉSERVES) -> codeur écrit le patch ->
grille test -> famille -> GO Christophe -> retest.
Clause permanente (Christophe, 14/08) : « Prouver la meilleure logique et
l'appliquer dans la correction et l'amélioration si possible » — le codeur doit
prouver QUE safe_call est la meilleure logique ET proposer UNE amélioration
prouvée, sans déborder de la SPEC.
"""
import json
import os
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
ROOT = "/Users/christophe/ace777-test-day1"
SPEC_PATH = os.path.join(ROOT, "SPEC_correction_panne_alpha_v3.md")
OUT = os.path.join(ROOT, "Index_Maison", "CODE_correction_panne_alpha_v3.md")

with open(SPEC_PATH, encoding="utf-8") as f:
    SPEC = f.read()

PROMPT = f"""\
Tu es le CODEUR de la famille ACE777 (task code.ia). Écris le code demandé,
borné à la tâche, rien d'autre. Aucune réécriture, aucune feature.

CLAUDE PERMANENTE (Christophe, 14/08 — à respecter à CHAQUE correction) :
« Prouve la meilleure logique et applique-la dans la correction et
l'amélioration si possible. »
→ Tu dois (1) PROUVER que ta correction est la meilleure logique (pas une
rustine : pourquoi pas `|| true` brut, sous-shell, wrapper par ligne ?),
et (2) proposer/appliquer UNE amélioration si elle est PROUVÉE (mesurable,
bornée, sans effet de bord). Rien au-delà de la SPEC.

================
LA SPEC À EXÉCUTER (validée par le JUGE — GO AVEC RÉSERVES)
================
{SPEC}

================
LIVRABLES (contrat de sortie — section 5 de la SPEC)
================
1. Code bash complet : fonction `safe_call` + encapsulation des zones listées
   (v8_5 ET GEMINI_TEST) — patch prêt à insérer, compatible bash 3.2 macOS.
2. La section PREUVE « meilleure logique » (obligatoire).
3. L'amélioration prouvée proposée (UNE, optionnelle si prouvée).
4. Rien d'autre.

RENDS : ton code + preuve, en français, concis.
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
    print("=== CODEUR (code.ia) — CORRECTION PANNE ALPHA rc=1 ===", flush=True)
    try:
        with urllib.request.urlopen(req, timeout=None) as resp:
            d = json.loads(resp.read().decode("utf-8"))
        rep = d["choices"][0]["message"]["content"].strip()
        provider = d.get("provider", "?")
    except Exception as e:
        rep = f"[CODEUR INJOIGNABLE] {str(e)[:200]}"
        provider = "?"
    print(f"provider: {provider}\n")
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(f"# RÉPONSE CODEUR (task code.ia · {provider}) — {__import__('datetime').datetime.utcnow().isoformat()}Z\n\n{rep}\n")
    print(rep)
    print(f"\n[OK] écrit dans {OUT}", flush=True)


if __name__ == "__main__":
    main()

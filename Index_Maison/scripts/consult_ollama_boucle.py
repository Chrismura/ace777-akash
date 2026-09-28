#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""consult_ollama_boucle.py — consultation des IA LOCALES Ollama (mandat Christophe 12/09).
Correction du propriétaire : « locale = dans mon ordi » (le hub 11435 route vers des IA externes).
Buffy = coursier : transmet le mandat d'audit indépendant, écrit les réponses verbatim.
Zéro ordre, zéro écriture maison hors le fichier de consultation lui-même."""
import json
import subprocess
import time
from pathlib import Path
from datetime import datetime, timezone

MANDAT_SYSTEM = "IA locale de la maison ACE777, audit indépendant sans complaisance, français, concis."
MANDAT_USER = """Depuis 6 mois la maison teste des moteurs de trading (testnet). Le propriétaire décrit une boucle: espoir -> test rigoureux -> verdict négatif -> oubli -> nouvel espoir. 3 cycles datés: (1) WR 60-80% juillet -> recomptage 08/09: petits échantillons, WR réel 54%. (2) 13 gros coups +371$ sur 221597 trades -> audit: loterie à frais, net moteur -17241$. (3) V2-REPLAY 12/09: 17 trades WR 58.8%, 4/5 critères économiques passent, échec formel car 17<30.

Réponds EXACTEMENT dans cet ordre, 2 phrases max par point:
1. Cette boucle est-elle une fatalité ou un défaut de méthode réparable ?
2. Des trades de 5 secondes peuvent-ils devenir rentables net de frais, ou est-ce structurellement mort ?
3. Le propriétaire doit-il tout arrêter ou garder UNE seule piste ? Laquelle ?
4. Remarque libre: une chose que ni le propriétaire ni Buffy n'ont vue."""

MODELES = ["qwen3.5:4b", "QWEEN_V9:latest"]
OUT = Path.home() / "ace777-test-day1/Index_Maison/CONSULTATION_OLLAMA_BOUCLE_20260912.md"


def demander(model: str, timeout_s: int = 600) -> str:
    payload = {
        "model": model, "stream": False, "options": {"num_predict": 500},
        "messages": [{"role": "system", "content": MANDAT_SYSTEM},
                     {"role": "user", "content": MANDAT_USER}],
    }
    t0 = time.time()
    try:
        r = subprocess.run(
            ["curl", "-s", "-m", str(timeout_s), "http://127.0.0.1:11434/api/chat",
             "-H", "Content-Type: application/json", "-d", json.dumps(payload)],
            capture_output=True, text=True, timeout=timeout_s + 10)
        rep = json.loads(r.stdout)["message"]["content"].strip()
    except Exception as e:
        rep = f"ERREUR ({model}): {e}"
    return rep + f"\n\n*(généré en {int(time.time()-t0)} s)*"


def main():
    reps = {}
    for m in MODELES:
        print(f"[consult] {m} ...", flush=True)
        reps[m] = demander(m)
        print(f"[consult] {m} OK", flush=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    corps = "\n\n".join(
        f"## Réponse — {m}\n\n{reps[m]}" for m in MODELES
    )
    OUT.write_text(f"""# CONSULTATION OLLAMA (LOCALE, dans l'ordinateur) — la boucle des tests
> Correction de Christophe 12/09 : « locale = dans mon ordi » — le hub (11435) route vers des IA EXTERNES.
> Ici : Ollama 127.0.0.1:11434 (v0.34), modèles LOCAUX, même mandat indépendant pour chacun · {now}
> Buffy = coursier, pas auteur des réponses. Modèles 1-5B : consultations citoyennes, pas expertises.

{corps}

---
*Consultation lecture-seule. Chaque réponse engage son modèle, pas la famille.*
""", encoding="utf-8")
    print("[consult] écrit:", OUT, flush=True)


if __name__ == "__main__":
    main()

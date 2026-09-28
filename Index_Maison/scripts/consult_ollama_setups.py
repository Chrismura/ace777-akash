#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""consult_ollama_setups.py — mandat Christophe 12/09 (2e tour).
« Je voulais que l'IA locale analyse les données des setups WR gagnants, pas qu'elle valide
le concept de la boucle — moi c'est les chiffres que je veux, la SOURCE. »
Buffy = coursier : extrait les trades bruts des 8 runs, les donne tels quels aux IA locales,
écrit leurs réponses verbatim. Aucune interprétation de Buffy dans le mandat.
Zéro ordre, zéro écriture maison hors le fichier de consultation."""
import json
import subprocess
import time
from pathlib import Path
from datetime import datetime, timezone

DONNEES = Path("/tmp/donnees_brutes_setups.txt").read_text()

MANDAT_SYSTEM = "IA locale de la maison ACE777, analyse de données brutes, français, concis, chiffres seulement."

MANDAT_USER = f"""TÂCHE : analyse de DONNÉES BRUTES de trades, pas de philosophie, pas d'opinion générale.
Ci-dessous TOUS les trades réellement exécutés (319) de 8 runs du moteur, avec pour chacun :
date_heure, side (LONG/SHORT), prix d'entrée, prix de sortie, bps captés, pnl en $, raison de sortie.
Contexte minimal : 2 runs dits gagnants (ALPHA_HUNTER, MINIPATCH_ALPHA_HUNTER), leurs miroirs dits perdants
(BETA_SCOUT, MINIPATCH_BETA_SCOUT), et 4 runs plus longs (V1 1h, V2 6h). Sélectivité = % de refus avant trade.

RÉPONDS EN CHIFFRES, à ces 5 questions, max 8 lignes par question :
1. Recompte toi-même le WR (wins/trades) de CHAQUE run. Les chiffres annoncés (61,1%, 81,8%, 44,7%) tiennent-ils ?
2. Dans les 2 gagnants : quelle part du pnl total vient des 3 plus gros gains ? Le gain est-il réparti ou concentré ?
3. Gagnants vs perdants : que disent les données comme différence concrète (répartition trailing/timeout/stop, side, durée, bps moyen) ?
4. Les 4 runs longs (V1/V2) confirment-ils ou affaiblissent-ils le profil des gagnants ? Chiffres à l'appui.
5. UN chiffre précis que le propriétaire ne peut pas voir à l'œil et qui compte pour monter en échelle (V2).

=== DONNÉES BRUTES (source : CSV des runs, colonnes réelles) ===
{DONNEES}"""

MODELES = [
    ("qwen3.5:4b", {"think": False}),   # mode réflexion coupé (1er tour : sortie vide sinon)
    ("QWEEN_V9:latest", None),
]
OUT = Path.home() / "ace777-test-day1/Index_Maison/CONSULTATION_OLLAMA_SETUPS_20260912.md"


def demander(model, extra, timeout_s=900):
    payload = {
        "model": model, "stream": False, "options": {"num_predict": 900},
        "messages": [{"role": "system", "content": MANDAT_SYSTEM},
                     {"role": "user", "content": MANDAT_USER}],
    }
    if extra:
        payload.update(extra)
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
    for m, extra in MODELES:
        print(f"[consult-setups] {m} ...", flush=True)
        reps[m] = demander(m, extra)
        print(f"[consult-setups] {m} OK", flush=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    corps = "\n\n".join(f"## Réponse — {m}\n\n{reps[m]}" for m, _e in MODELES)
    OUT.write_text(f"""# CONSULTATION OLLAMA (LOCALE) — ANALYSE DES DONNÉES BRUTES DES SETUPS GAGNANTS
> Mandat Christophe 12/09 (2e tour) : « c'est les chiffres que je veux, la SOURCE » — pas de philosophie.
> Données : 319 trades FILLED, 8 runs, colonnes réelles des CSV (entrée/sortie/bps/pnl/raison/durée).
> Ollama 127.0.0.1:11434 · Buffy = coursier, pas auteur des réponses · {now}

{corps}

---
*Consultation lecture-seule. Chaque réponse engage son modèle, pas la famille.*
""")
    print(f"[consult-setups] écrit : {OUT}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Soumet le point d'insertion HULK du disjoncteur au codeur (validation technique) + famille (verdict).
Le disjoncteur.py est DÉJÀ codé, testé et branché (launchd). Reste : où l'accrocher dans HULK sans
toucher à la logique de paper_diprip.py."""
import json, os, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

HUB = "http://127.0.0.1:11435/v1/chat/completions"
BASE = os.path.expanduser("~/ace777-test-day1/Index_Maison")

CONTEXTE = """=== ÉTAT ACTUEL ===
- Disjoncteur Unique (scripts/disjoncteur.py) : CODÉ, testé (5 cas OK), branché launchd (check/60s).
  Commandes : --check / --bridage <taille> --capital <cap> --perte-jour <pct> / --rearmer / --etat.
- Il pose STOP_ALL + disjoncteur_state.json + .urgent_alert.json en cas de perte >= 1.5% (ou >= 8% global).
- Le bridage : taille_autorisee = min(proposee, capital * plafond_trade_pct/100). Ne crée JAMAIS d'ordre (C3).

=== CE QU'IL RESTE ===
Accrocher le disjoncteur dans HULK (hulk-mexc/scripts/paper_diprip.py) : avant tout fill, appeler
--bridage. MAIS la spec interdit de modifier la logique interne de paper_diprip.py (moteur HULK).

=== PROPOSITION DU CODEUR (diff à valider) ===
Dans paper_diprip.py, au point d'exécution d'ordre :
def verifier_via_disjoncteur(taille_proposee, capital_ref):
    subprocess.run(['python3', '<chemin>/disjoncteur.py', '--bridage', str(taille), '--capital', str(capital_ref)],
                   capture_output=True, text=True, timeout=2)
    -> si returncode != 0 : rejet ; sinon taille_corrigee
def executer_ordre(taille, prix, symbole):
    check = verifier_via_disjoncteur(taille)
    if not check['autorise']: return False   # bloqué (Mur de Fer)
    placer_ordre_interne(check['taille_corrigee'], prix, symbole)

=== QUESTIONS PRÉCISES ===
1. Le wrapper subprocess dans paper_diprip.py est-il le point le moins invasif, ou un import direct
   (from disjoncteur import verifier_et_brigader) est-il préférable (même process, pas de subprocess) ?
2. Où EXACTEMENT dans paper_diprip.py appeler le check (à quel endroit du flux de fill) ?
3. Quelle valeur de capital_ref passer (le capital paper HULK réel, pas un 10000 en dur) ?
4. Que faire si le disjoncteur est injoignable (subprocess crash) : rejeter (fail-closed, recommandé) ?
"""

def appeler(task, system, prompt, out_path):
    payload = json.dumps({
        "model": task,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        "max_tokens": 3000, "temperature": 0.2,
    }).encode()
    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"}, method="POST")
    print(f"[{task}] envoi...", flush=True)
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=300) as resp:
        d = json.loads(resp.read().decode())
    content = d["choices"][0]["message"]["content"]
    dur = round(time.time() - t0, 1)
    prov = d.get("provider", "?")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"# {task} — insertion HULK disjoncteur (provider {prov}, {dur}s)\n\n{content}\n")
    print(f"[OK] {task} -> {out_path} ({prov}, {dur}s)", flush=True)

PROMPT_CODEUR = f"""Tu es le CODEUR ACE777. Le disjoncteur est déjà codé/testé/branché. Tu dois valider
le POINT D'INSERTION dans HULK (sans toucher à la logique moteur de paper_diprip.py).

{CONTEXTE}

Réponds en 3 sections : 1) RÉPONSES aux 4 questions (choisis wrapper subprocess OU import direct, justifie),
2) DIFF EXACT avant/après minimal pour paper_diprip.py, 3) NOTES (risques, ce qu'on ne touche pas).
Français, factuel, concis."""

PROMPT_FAMILLE = f"""Tu es la FAMILLE/JUGE ACE777. Le disjoncteur (règle d'airain « l'IA propose, le code
dispose ») est codé et branché. Le point d'insertion dans HULK te est soumis pour verdict.

{CONTEXTE}

Réponds en 3 sections : 1) VERDICT : VALIDÉ / VALIDÉ AVEC RÉSERVES / REJETÉ,
2) RÉSERVES éventuelles, 3) CONDITIONS avant GO (ex. fail-closed obligatoire, capital réel, ne pas
toucher à la logique HULK). Français, factuel, tranché."""

jobs = [
    ("code.ia", "Tu es le codeur senior ACE777. Code propre, stdlib, robuste, vérification rigoureuse.",
     PROMPT_CODEUR, os.path.join(BASE, "VALIDATION_INSERTION_HULK_CODEUR_2026-08-16.md")),
    ("signets.juge", "Tu es le juge/famille ACE777. Tu valides ou rejettes, tu ne codes pas.",
     PROMPT_FAMILLE, os.path.join(BASE, "VALIDATION_INSERTION_HULK_FAMILLE_2026-08-16.md")),
]
with ThreadPoolExecutor(max_workers=2) as ex:
    for f in [ex.submit(appeler, *j) for j in jobs]:
        f.result()
print("=== Terminé ===", flush=True)

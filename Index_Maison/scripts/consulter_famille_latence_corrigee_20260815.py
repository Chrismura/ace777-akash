#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Re-consultation FAMILLE — robustesse latence, chiffres CORRIGÉS (15/08/2026).

Protocole §C #9 Multi-Perspective + #5 Confidence-Weighted + AMÉLIORATIONS.
"""
import json, os, time, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_LATENCE_CORRIGEE_20260815")
os.makedirs(OUT, exist_ok=True)

BRIEF = """CONTEXTE (superviseur Buffy, 15/08/2026) — CONSULTATION CORRIGÉE : robustesse à la latence réseau

=== CORRECTION D'UN DIAGNOSTIC PRÉCÉDENT ===
Une consultation antérieure a conclu « infra d'abord » sur la base d'E-STALE=1032 + E-PROC=75.
Ces chiffres étaient FAUX : le rapport d'erreurs auto utilisait le mauvais tag (NUAGE_PROD_4H,
l'usine) au lieu du run réellement testé. Correction vérifiée dans les logs :

| Indicateur | Faux (rapport NUAGE) | VRAI (run vortex 15/08) |
|---|---|---|
| tension_stale (latence feed) | 1032 | **0** |
| process_die / process_exit | 75 | **0** |
| spread_too_wide | — | 2551 (marché calme) |
| duo no_trigger/stale | — | 1612 (marché calme) |

=> Le run vortex du 15/08 n'avait AUCUN problème d'infra. L'« endormissement » constaté = marché
FÉRIÉ calme (tension moyenne la plus basse des 4 jours), pas une panne.

=== LES DEUX CHEMINS (architecture réelle) ===
1. **Chemin VORTEX (le test actuel)** : moteur = `genesis_manifest.txt`. Il lit la tension via
   `vortex_radar_read.rb` (fichier vortex_control.json) avec une garde de fraîcheur
   `VORTEX_JSON_MAX_AGE_SEC`. PAS de gate « tension_stale » (mécanisme différent).
2. **Chemin USINE NUAGE (production)** : launcher `launch_vide_froid_4h_binance_NUAGE_*.sh` +
   `GO_USINE_NUAGE.sh`. Il lit `duo_state.ts_ms` avec gate FIXE `NUAGE_TENSION_MAX_AGE_MS=800ms`
   → SKIP « tension_stale » si l'âge dépasse 800ms. Log NUAGE_PROD_4H : **1811 tension_stale**
   historiques (1-8% des skips) = latence réseau RÉELLE (WiFi/téléphone/alpage).

=== CONTRAINTE PERMANENTE (non négociable) ===
L'environnement de Christophe est en WiFi/téléphone/alpage : la latence réseau est RÉELLE,
PROUVÉE et PERMANENTE. On ne peut PAS l'éliminer. Le bot doit être ROBUSTE à cette latence
(dégrader gracieusement, attendre, repartir), pas « corriger le WiFi ».

=== LE BUG DÉJÀ CORRIGÉ (pour mémoire) ===
Le revenge ALPHA était permanent car `duo_touch_heartbeat` rafraîchissait `ts_ms` à chaque cycle
→ TTL 20s inopérant. Corrigé (fix conditionné à « perte non close »), smoke test OK, rescellé.

=== VOTRE MISSION (format EXACT exigé) ===
Analysez sous 3 angles :
  • Technique : le chemin vortex est-il correctement protégé contre la latence (sa garde
    VORTEX_JSON_MAX_AGE_SEC suffit-elle), ou a-t-il un TROU de fraîcheur de tension ? Le chemin
    NUAGE avec gate fixe 800ms sur-skippe-t-il à tort sous latence alpine (faux positifs) ?
  • Risque/Impact : que faut-il pour « vivre sur WiFi/alpage » : gate ADAPTIVE (seuil qui suit
    la cadence réelle, comme suggéré dans MATRICE_QUANT_ROBERT_ENGLE) ? Ou garder le SKIP
    prudent tel quel (sûr mais = occasions manquées) ?
  • Priorité : avec les chiffres corrigés, quel est l'ordre réel (heartbeat fait → quoi ensuite) ?

Puis donnez :
  VERDICT : GO | NO-GO | GO-AVEC-RÉSERVE (sur « ouvrir un chantier robustesse latence », préciser)
  CONFIANCE : 0-100 %
  HYPOTHÈSES : 2-3 hypothèses
  CE QUI CHANGERAIT L'AVIS : le(s) fait(s) qui ferait/faisaient basculer
  AMÉLIORATION PROPOSÉE : 1-3 idées concrètes (ou « aucune »)

SYNTHÈSE (5 lignes max) : diagnostic + ordre des actions.

Factuel, concis, français. Si une info manque : « information insuffisante ». Vous DONNEZ UN AVIS :
ne touchez à rien, n'écrivez aucun code."""

MODELS = ["gemini", "nvidia", "openrouter-juge", "openrouter-ultra"]


def ask(model):
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": BRIEF}],
        "max_tokens": 2400, "temperature": 0.3,
    }).encode()
    req = urllib.request.Request(HUB, data=payload,
                                 headers={"Content-Type": "application/json"}, method="POST")
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    return d["choices"][0]["message"]["content"], d.get("provider", "?"), round(time.time() - t0, 1)


def main():
    for m in MODELS:
        for attempt in (1, 2):
            try:
                content, provider, secs = ask(m)
                with open(os.path.join(OUT, f"AVIS_{m}.md"), "w", encoding="utf-8") as fh:
                    fh.write(f"# AVIS {m} (provider {provider}, {secs}s)\n\n{content}\n")
                print(f"[OK] {m} ({secs}s)")
                break
            except Exception as e:
                print(f"[ERR] {m} (tentative {attempt}): {e}")
                time.sleep(3)
        time.sleep(2)


if __name__ == "__main__":
    main()

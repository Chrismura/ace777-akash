# VERDICT FAMILLE — Fondations des acteurs (15/08/2026)

> 4/4 avis (gemini, nvidia, juge, ultra) — **convergents**. Protocole §C respecté (multi-perspective + confiance + améliorations).

## Verdict global : GO, exécuter dans l'ordre F1 → F2 → F3 → F4 → F5

| Fondation | Verdict | Confiance (moy) | Priorité |
|---|---|---|---|
| **F1** Réparer la justesse | ✅ GO (4/4) | ~95 % | **1ʳᵉ** — la boussole |
| **F2** Carte d'identité ACE777 | ✅ GO (4/4) | ~99 % | 2ᵉ |
| **F3** Cortana = dashboard (ACE+Hulk) | 🟡 GO-AVEC-RÉSERVE (RAM, schéma des données, SPOF) | ~85 % | 3ᵉ |
| **F4** Un seul aiguilleur (hub) | 🟡 GO-AVEC-RÉSERVE (repli hors-ligne à prouver avant de supprimer brain.rs) | ~83 % | 4ᵉ |
| **F5** Nettoyer prompt voix | ✅ GO (4/4) — fusionnable avec F2 | ~99 % | 5ᵉ |

**Risque n°1 (unanime)** : F4 — ne pas retirer la logique locale de `brain.rs` tant que le hub n'a pas **prouvé** son repli hors-ligne (timeout + santé Ollama), sinon cockpit muet en cas de coupure.

## Améliorations proposées par la famille (stacking functions)

**F1 — justesse**
- Versionner la sortie (`justesse_v2.json`) + **backfill** : recalculer les 93 analyses existantes sur la nouvelle logique (ultra).
- Colonne « régime de marché » (trend/range) pour segmenter la justesse future (ultra).
- Rapport de **dérive/biais par indice** (détecter les instruments non prédictifs) (nvidia).
- Test de régression : NEUTRE bien noté + courbe de stabilité du seuil 0,3 % (juge).
- Journal d'audit des faux positifs au seuil (gemini).

**F2 — carte d'identité**
- `config/identity/ace777_core.md` + `prompts/{ada,cortana,qwen}.md` (ultra).
- Hash **SHA-256** de l'identité dans les logs de boot (gemini, nvidia, ultra) + versioning git.
- Champ `version_strategie` pour la bascule saison d'Ada (ultra).

**F3 — dashboard**
- **Module de normalisation** des données (schéma unique fills ACE + paper Hulk) avant l'analyse (nvidia, juge).
- Sortie standardisée `cortana_snapshot_{ts}.json` consommable par hub/voix (ultra).
- Nettoyage/rotation auto des anciens rapports CSV (gemini) · métrique « PnL attribué par régime » (ultra).

**F4 — aiguilleur**
- Test d'intégration simulant la **panne du hub** (cargo test) pour valider le repli hors-ligne (4/4).
- Métriques `hub_latency_ms` / `hub_fallback_count` loggées (ultra).
- **Supprimer `puter-grok` (402) du routing** — déjà identifié par Buffy (ultra confirme).

**F5 — prompt voix**
- Assertion au démarrage : mots-clés interdits absents (« exécute », « ordre », « Binance ») (gemini).
- Clause explicite « observateur en lecture seule, action = validation humaine » (ultra) + versionner `voice_prompt_v3.md`.

## Prochaine étape (après GO Christophe)
F1 d'abord (justesse) : refactor `score_justesse.py` (juger chaque indice contre lui-même + NEUTRE + seuil 0,3 % + fix `derniere`) + backfill des 93 analyses + test de régression. Le code partira au codeur (spec + diff exact), Buffy supervise.

# ⚖️ SYNTHESE FAMILLE — REVISION TUYAUTERIE — 2026-08-09 16:15Z

## Verdicts REELS des familles (corrigé 16:25Z — vérité du journal hub, pas la version optimiste)

> ⚠️ **CORRECTION IMPORTANTE** : les avis « JUGE » et « ULTRA » n'ont PAS été rendus par les vrais Nemotron Juge/Ultra (quota :free TOUJOURS épuisé). La blacklist a basculé sur le fallback NVIDIA qui sert **deepseek-v4-flash** — donc ces 2 avis sont en réalité des avis **DeepSeek V4 Flash** (preuves usage.jsonl : 13:52:26 et 13:54:10, model=deepseek-ai/deepseek-v4-flash-0731).

| Étiquette | VRAI modèle qui a répondu | Verdict | Confiance |
|---|---|---|---|
| GEMINI | gemini-flash-lite-latest (13:47:02) ✓ | OK AVEC RESERVES | moyenne |
| DEEPSEEK V4 | deepseek-v4-flash-0731 (13:49:58) ✓ | A CORRIGER | moyenne |
| ~~NEMOTRON JUGE~~ | ❌ deepseek-v4-flash (fallback, PAS nemotron) | A CORRIGER (mais = DeepSeek) | - |
| ~~NEMOTRON ULTRA~~ | ❌ deepseek-v4-flash (fallback, PAS nemotron) | A CORRIGER (mais = DeepSeek) | - |

**Consensus réel = 2 modèles distincts : Gemini + DeepSeek V4 Flash** (les 3 avis « deepseek/juge/ultra » proviennent du même modèle avec des prompts différents). Le Juge et l'Ultra sont TOUJOURS muets — à rejouer quand leur quota revient.

**Consensus famille :** la liste des faits est juste et sourcée (C1-C5, R1-R5 validés). MAIS elle est **incomplète** : 6 points manquants (M1-M6) identifiés par les 4 familles de façon convergente.

## ORDRE FINAL ÉTABLI PAR ADA (fusion des 4 avis + logique)

### 🚨 PHASE 1 — CRITIQUE (aujourd'hui)
| # | Correctif | Note famille |
|---|---|---|
| **1. C4** | Vigie : réparer le plist (HOME/PATH manquant → exit 2) | Ultra : « le point le plus dangereux, on croit être protégé » |
| **2. C1** | Timeout superviseur : **mesurer la latence réelle du hub d'abord**, puis aligner sur PATIENCE (660s selon Juge, ou adaptatif selon DeepSeek) + circuit breaker 3 timeouts → alerte | Tous : « le superviseur est aveugle » · A1=180s **REJETÉ** (arbitraire) |
| **3. C3** | `test-freebuff` → git init + commit + push (5 min) | DeepSeek/Ultra : « bombe à retardement » |
| **4. C2** | Jauge énergie : plist avec cadence 30 min + RunAtLoad | Gemini : « besoin métier non satisfait depuis des jours » |
| **5. C5** | Autopilote : log dans reports/ au lieu de /tmp | Ultra : « 2 minutes, crucial pour la confiance » |

### 🟠 PHASE 2 — ROBUSTESSE (48h)
6. **R1** BrokenPipeError → attrape propre dans le Handler
7. **R2** Rotation logs (SYNC_LOG 132Ko, hub_events 112Ko)
8. **R3** `.bak` sorti de LaunchAgents
9. **M4** Vérifier environnement (HOME/PATH) des 28 plists (C4 = symptôme systémique)
10. **M5** Plan de rollback documenté (avant toute correction)

### 🟡 PHASE 3 — ARCHITECTURE (semaine)
11. **A5** Healthcheck mtime **seuil ×1.5** (pas ×3 — DeepSeek) → vérificateur auto
12. **A4** Inventaire CADENCES.md + vérificateur plists vs déclaré
13. **A6** Rotation généralisée
14. **A1** Timeout adaptatif (suite de C1, après mesure)
15. **M3** Test de charge du hub (28 services simultanés)
16. **M1** Test de reprise après crash (kill -9)
17. **M6** Métrique de santé globale (taux succès décisions, latence)
18. **M2** Cohérence des données entre les 3 repos

### ⏸️ NE PAS TOUCHER (consensus famille)
- **R4** Doublon nvidia/inferx = fallback VOLONTAIRE (résilience) → documenter, ne pas retirer
- **R5** Providers désactivés → garder documentés
- **MÉCANISMES À NE SURTOUT PAS CASSER** : gatekeeper, heartbeat, blacklist — chaque correction testée avec eux ACTIFS

## Preuves
- Avis complets : `REVISION_FAMILLE_2026-08-09/AVIS_{gemini,deepseek,juge,ultra}.md` (juge+ultra = en-tête « via NVIDIA » = fallback)
- Preuve envoi : usage.jsonl (13:47-13:54) — gemini ✓, deepseek ✓, juge/ultra = nvidia/deepseek-v4-flash ❌
- **Leçon** : ne jamais étiqueter un avis « famille X » sans vérifier le modèle réel dans usage.jsonl (loi 1septies : preuve avant affirmation)

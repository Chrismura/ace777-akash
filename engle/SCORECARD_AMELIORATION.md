# ACE777 — Scorecard amélioration (réf. 2026-07-20)

Verdict global : **7/10** — intelligent et productif par moments, pas encore « appuie et oublie ».

| # | Axe | Note | Cible | Statut |
|---|-----|------|-------|--------|
| 1 | Idée (scout/hunter, bus RAM) | 8–9 | garder / clarifier | à traiter |
| 2 | Discipline usine (sterile, champion, GO) | 8 | 9 | à traiter |
| 3 | Exécution live / robustesse | 5–6 | 8 | **priorité** |
| 4 | Plus-value prouvée | 6–7 | 8 | à traiter |
| 5 | Portabilité / simplicité | 4 | 6 | plus tard |

## Ordre de travail proposé

1. **#3 Robustesse** — duo PID, morts BETA/ALPHA, heartbeat, moins de fantômes
2. **#4 Plus-value** — ALPHA convertit + **STORM latch** (mèches) — voir `engle/PLAN_STORM_WICK.md`
3. **#2 Discipline** — renforcer preflight / coffre / protocoles déjà bons
4. **#1 Idée** — documenter le vrai modèle (anti Gemini) ; pas de sync co-entrée
5. **#5 Portabilité** — seulement quand 3+4 tiennent

## Règles de campagne

- Un axe à la fois ; pas de double setup parallèle
- Mesure avant/après sur run 4h usine (`GO_USINE_NUAGE`)
- Champion `genesis_manifest` intouchable sans GO explicite
- Patchs runtime réversibles d’abord (`GO_USINE`, env flags)

## Journal des sessions

| Date | Axe | Action | Résultat |
|------|-----|--------|----------|
| 2026-07-20 | — | Scorecard créée | baseline 7/10 |
| 2026-07-20 | #4 | Flag `NUAGE_BIDIR_SIDES` (défaut OFF) | prêt A/B — voir `engle/BIDIR_SIDES.md` |
| 2026-07-20 | #4 | Plan STORM/mèche (K1 latch, K2 hunter) | `engle/PLAN_STORM_WICK.md` |
| 2026-07-20 | #4 | Run bidir stoppé +8.65 · journal erreurs | `engle/JOURNAL_ERREURS.md` |
| 2026-07-20 | #4 | K1 `NUAGE_STORM_LATCH` runtime | prêt test — commande dans PLAN_STORM |
| 2026-07-20 | #3 | `PROCESS_EXIT`/`PROCESS_DIE` (raison mort process) | GO toujours ON — `engle/PROCESS_EXIT_LOG.md` |
| 2026-07-21 | #4 | `NUAGE_MIN_ENTRY_TENSION` (filtre vacuum) | prêt A/B — `engle/MIN_ENTRY_TENSION.md` |
| 2026-07-21 | #4 | K3 `NUAGE_STORM_SCOUT_HOLD` (min hold 20s) | prêt test — `engle/PLAN_STORM_WICK.md` |
| 2026-07-21 | #4 | Brief session `SESSION_AMELIORATION_GROK` | cible fills ALPHA ≥29 $ |
| 2026-07-21 | #4 | K2 `NUAGE_STORM_HUNTER` + fix set -e post_delta | shippé runtime — run live |
| 2026-07-21 | #4 | **K2v2** live arm + export env (E13) | dry-run OK — relancer |
| 2026-07-22 | #4 | **K3v2** hold scout+hunter (ALPHA ≥20s) | dry-run OK — commande terminal |
| 2026-07-22 | #4 | Run 4h 06:41–10:41Z ALPHA **−10.56 $** | hunter OK ; hold trop court |
| 2026-07-22 | #3 | `rapport_erreurs_session.sh` (hygiène E15) | LIVE+PROCESS+WATCHDOG → md |
| 2026-07-22 | #3 | E16 watchdog : stale+ALIVE → skip kill | TIMER_WAIT semantic |

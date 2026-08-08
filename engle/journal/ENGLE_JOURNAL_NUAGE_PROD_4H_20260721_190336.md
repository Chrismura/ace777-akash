# JOURNAL ENGLE — NUAGE_PROD_4H

- Généré: `2026-07-21T19:03:36Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-21T19:01:21Z`
- CSV: `NUAGE_PROD_4H_BETA_X5.csv` · `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 0 | 0.0% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 0 | 0.0% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 1 | 100.0% | 1 | +0.0000 |

- Courant (proxy): **CLUSTER (tension haute — proxy)** · μ=4.1158 · σ=0.0000 · n=1

## Posture recommandée (conseil — pas appliquée)

- Code: `HUNT_WINDOW`
- Tension haute (proxy) — candidature future B3 gate/soft, pas encore appliqué.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 1 | 1 | 0 | +0.0000 | `2026-07-21T19:02:03Z` → `2026-07-21T19:02:03Z` |
| ALPHA | 4 | 0 | 4 | +0.0000 | `2026-07-21T19:01:34Z` → `2026-07-21T19:02:01Z` |
| **TOTAL** | | 1 | | **+0.0000** | |

## SKIP BETA (top)

*Aucun SKIP classé.*

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 4 | 100.0% |

## Lecture courte (marché calme)

1. Part de **CLUSTER** non négligeable — candidature future B3 (un knobs).
2. Comparer fills ALPHA vs runs calmes avant tout GO knobs.
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

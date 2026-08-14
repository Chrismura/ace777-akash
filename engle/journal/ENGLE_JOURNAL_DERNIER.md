# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-14T07:56:34Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-14T07:40:59Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 39 | 50.6% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 28 | 36.4% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 10 | 13.0% | 10 | +0.1240 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.3280 · σ=0.5299 · n=77

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 77 | 10 | 67 | +0.1240 | `2026-08-14T07:41:10Z` → `2026-08-14T07:56:26Z` |
| ALPHA | 43 | 2 | 41 | +2.9474 | `2026-08-14T07:41:12Z` → `2026-08-14T07:49:00Z` |
| **TOTAL** | | 12 | | **+3.0714** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 37 | 55.2% |
| `wall_not_collapsed` | 16 | 23.9% |
| `radar_block` | 12 | 17.9% |
| `tactic_mismatch` | 2 | 3.0% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 25 | 61.0% |
| `wall_not_collapsed` | 10 | 24.4% |
| `radar_block` | 6 | 14.6% |

## Lecture courte (marché calme)

1. Régime mixte — journaliser encore 1–2 runs 4h avant B3.
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

# JOURNAL ENGLE — NUAGE_PROD_4H

- Généré: `2026-07-19T12:53:07Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-19T12:38:02Z`
- CSV: `NUAGE_PROD_4H_BETA_X5.csv` · `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 39 | 52.7% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 19 | 25.7% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 16 | 21.6% | 16 | +0.1345 |

- Courant (proxy): **TRANSITOIRE (bruit retail)** · μ=0.8395 · σ=1.7817 · n=74

## Posture recommandée (conseil — pas appliquée)

- Code: `WATCH`
- Bruit retail — observer ; pas de knobs B3.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 74 | 16 | 58 | +0.1345 | `2026-07-19T12:38:14Z` → `2026-07-19T12:52:57Z` |
| ALPHA | 57 | 3 | 54 | -0.0275 | `2026-07-19T12:38:21Z` → `2026-07-19T12:49:36Z` |
| **TOTAL** | | 19 | | **+0.1070** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 34 | 58.6% |
| `wall_not_collapsed` | 15 | 25.9% |
| `radar_block` | 6 | 10.3% |
| `tactic_mismatch` | 3 | 5.2% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 32 | 59.3% |
| `radar_block` | 10 | 18.5% |
| `wall_not_collapsed` | 8 | 14.8% |
| `duo_wait` | 4 | 7.4% |

## Lecture courte (marché calme)

1. Régime mixte — journaliser encore 1–2 runs 4h avant B3.
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

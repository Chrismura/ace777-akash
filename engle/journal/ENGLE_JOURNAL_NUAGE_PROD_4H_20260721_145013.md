# JOURNAL ENGLE — NUAGE_PROD_4H

- Généré: `2026-07-21T14:50:13Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-21T10:40:06Z`
- CSV: `NUAGE_PROD_4H_BETA_X5.csv` · `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 747 | 57.7% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 303 | 23.4% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 245 | 18.9% | 105 | -0.2726 |

- Courant (proxy): **TRANSITOIRE (bruit retail)** · μ=0.7737 · σ=1.8913 · n=1295

## Posture recommandée (conseil — pas appliquée)

- Code: `WATCH`
- Bruit retail — observer ; pas de knobs B3.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 1295 | 105 | 1190 | -0.2726 | `2026-07-21T10:40:16Z` → `2026-07-21T14:39:59Z` |
| ALPHA | 1597 | 2 | 1595 | -1.9521 | `2026-07-21T10:40:19Z` → `2026-07-21T14:40:12Z` |
| **TOTAL** | | 107 | | **-2.2247** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 680 | 57.1% |
| `wall_not_collapsed` | 212 | 17.8% |
| `radar_block` | 172 | 14.5% |
| `vacuum_filter` | 120 | 10.1% |
| `tactic_mismatch` | 6 | 0.5% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 769 | 48.2% |
| `wall_not_collapsed` | 264 | 16.6% |
| `radar_block` | 257 | 16.1% |
| `vacuum_filter` | 152 | 9.5% |
| `duo_wait` | 103 | 6.5% |
| `tension_stale` | 36 | 2.3% |
| `tactic_mismatch` | 14 | 0.9% |

## Lecture courte (marché calme)

1. Régime mixte — journaliser encore 1–2 runs 4h avant B3.
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

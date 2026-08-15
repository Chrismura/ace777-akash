# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-14T09:31:21Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-14T09:29:30Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 5 | 50.0% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 4 | 40.0% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 1 | 10.0% | 1 | +0.0376 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.5993 · σ=1.3984 · n=10

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 10 | 1 | 9 | +0.0376 | `2026-08-14T09:29:45Z` → `2026-08-14T09:31:18Z` |
| ALPHA | 11 | 0 | 11 | +0.0000 | `2026-08-14T09:29:42Z` → `2026-08-14T09:31:15Z` |
| **TOTAL** | | 1 | | **+0.0376** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 5 | 55.6% |
| `wall_not_collapsed` | 3 | 33.3% |
| `radar_block` | 1 | 11.1% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 7 | 63.6% |
| `duo_wait` | 2 | 18.2% |
| `wall_not_collapsed` | 1 | 9.1% |
| `tactic_mismatch` | 1 | 9.1% |

## Lecture courte (marché calme)

1. Régime mixte — journaliser encore 1–2 runs 4h avant B3.
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

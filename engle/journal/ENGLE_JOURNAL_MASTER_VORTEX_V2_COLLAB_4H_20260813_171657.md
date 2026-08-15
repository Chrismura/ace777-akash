# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-13T17:16:57Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-13T16:44:57Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 98 | 58.0% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 35 | 20.7% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 36 | 21.3% | 26 | +1.6350 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.8880 · σ=1.8905 · n=169

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 169 | 26 | 143 | +1.6350 | `2026-08-13T16:45:07Z` → `2026-08-13T17:16:48Z` |
| ALPHA | 139 | 14 | 125 | +1.6663 | `2026-08-13T16:45:11Z` → `2026-08-13T17:11:07Z` |
| **TOTAL** | | 40 | | **+3.3014** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 73 | 51.0% |
| `radar_block` | 48 | 33.6% |
| `wall_not_collapsed` | 20 | 14.0% |
| `tactic_mismatch` | 2 | 1.4% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 59 | 47.2% |
| `radar_block` | 35 | 28.0% |
| `wall_not_collapsed` | 23 | 18.4% |
| `duo_wait` | 5 | 4.0% |
| `stase_ecoute` | 2 | 1.6% |
| `tactic_mismatch` | 1 | 0.8% |

## Lecture courte (marché calme)

1. Régime mixte — journaliser encore 1–2 runs 4h avant B3.
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

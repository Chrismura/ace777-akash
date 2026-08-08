# JOURNAL ENGLE — NUAGE_PROD_4H

- Généré: `2026-07-22T14:32:39Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-22T11:44:55Z`
- CSV: `NUAGE_PROD_4H_BETA_X5.csv` · `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 620 | 67.9% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 157 | 17.2% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 136 | 14.9% | 51 | -0.7306 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.5949 · σ=1.7163 · n=913

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 913 | 51 | 862 | -0.7306 | `2026-07-22T11:45:04Z` → `2026-07-22T14:22:52Z` |
| ALPHA | 1013 | 5 | 1008 | +0.1696 | `2026-07-22T11:45:06Z` → `2026-07-22T14:20:52Z` |
| **TOTAL** | | 56 | | **-0.5609** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 560 | 65.0% |
| `radar_block` | 128 | 14.8% |
| `wall_not_collapsed` | 98 | 11.4% |
| `vacuum_filter` | 71 | 8.2% |
| `tactic_mismatch` | 5 | 0.6% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 585 | 58.0% |
| `radar_block` | 165 | 16.4% |
| `wall_not_collapsed` | 109 | 10.8% |
| `vacuum_filter` | 77 | 7.6% |
| `tension_stale` | 67 | 6.6% |
| `tactic_mismatch` | 5 | 0.5% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

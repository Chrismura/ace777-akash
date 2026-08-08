# JOURNAL ENGLE — NUAGE_TEST_4H_0729b

- Généré: `2026-07-29T15:08:57Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-29T13:21:36Z`
- CSV: `NUAGE_TEST_4H_0729b_BETA_X5.csv` · `NUAGE_TEST_4H_0729b_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 421 | 64.4% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 124 | 19.0% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 109 | 16.7% | 34 | -0.0119 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.6277 · σ=1.5035 · n=654

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 654 | 34 | 620 | -0.0119 | `2026-07-29T13:21:46Z` → `2026-07-29T15:08:52Z` |
| ALPHA | 709 | 5 | 704 | +7.5013 | `2026-07-29T13:21:50Z` → `2026-07-29T15:08:54Z` |
| **TOTAL** | | 39 | | **+7.4893** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 340 | 54.8% |
| `radar_block` | 151 | 24.4% |
| `wall_not_collapsed` | 79 | 12.7% |
| `vacuum_filter` | 49 | 7.9% |
| `tactic_mismatch` | 1 | 0.2% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 375 | 53.3% |
| `radar_block` | 162 | 23.0% |
| `wall_not_collapsed` | 62 | 8.8% |
| `vacuum_filter` | 59 | 8.4% |
| `tension_stale` | 41 | 5.8% |
| `tactic_mismatch` | 5 | 0.7% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

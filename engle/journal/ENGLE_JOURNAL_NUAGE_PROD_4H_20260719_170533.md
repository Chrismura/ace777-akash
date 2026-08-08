# JOURNAL ENGLE — NUAGE_PROD_4H

- Généré: `2026-07-19T17:05:33Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-19T15:41:07Z`
- CSV: `NUAGE_PROD_4H_BETA_X5.csv` · `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 283 | 74.7% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 61 | 16.1% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 35 | 9.2% | 35 | +0.3914 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.4298 · σ=1.4662 · n=379

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 379 | 35 | 344 | +0.3914 | `2026-07-19T15:41:17Z` → `2026-07-19T16:44:37Z` |
| ALPHA | 422 | 4 | 418 | +13.5605 | `2026-07-19T15:41:21Z` → `2026-07-19T16:49:20Z` |
| **TOTAL** | | 39 | | **+13.9519** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 261 | 75.9% |
| `wall_not_collapsed` | 50 | 14.5% |
| `radar_block` | 29 | 8.4% |
| `tactic_mismatch` | 3 | 0.9% |
| `stase_ecoute` | 1 | 0.3% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 242 | 57.9% |
| `radar_block` | 89 | 21.3% |
| `wall_not_collapsed` | 46 | 11.0% |
| `duo_wait` | 28 | 6.7% |
| `tension_stale` | 11 | 2.6% |
| `tactic_mismatch` | 2 | 0.5% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

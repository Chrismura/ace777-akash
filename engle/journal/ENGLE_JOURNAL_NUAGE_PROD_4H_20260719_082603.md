# JOURNAL ENGLE — NUAGE_PROD_4H

- Généré: `2026-07-19T08:26:03Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-19T07:19:13Z`
- CSV: `NUAGE_PROD_4H_BETA_X5.csv` · `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 310 | 73.6% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 87 | 20.7% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 24 | 5.7% | 24 | +1.0033 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.2445 · σ=0.8295 · n=421

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 421 | 24 | 397 | +1.0033 | `2026-07-19T07:19:29Z` → `2026-07-19T08:24:40Z` |
| ALPHA | 411 | 1 | 410 | -0.0260 | `2026-07-19T07:19:33Z` → `2026-07-19T08:25:59Z` |
| **TOTAL** | | 25 | | **+0.9772** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 298 | 75.1% |
| `wall_not_collapsed` | 68 | 17.1% |
| `radar_block` | 31 | 7.8% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 289 | 70.5% |
| `wall_not_collapsed` | 53 | 12.9% |
| `radar_block` | 39 | 9.5% |
| `duo_wait` | 17 | 4.1% |
| `tension_stale` | 12 | 2.9% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

# JOURNAL ENGLE — NUAGE_PROD_4H

- Généré: `2026-07-19T15:37:18Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-19T13:59:38Z`
- CSV: `NUAGE_PROD_4H_BETA_X5.csv` · `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 340 | 72.0% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 84 | 17.8% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 48 | 10.2% | 48 | +1.0295 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.3951 · σ=1.2387 · n=472

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 472 | 48 | 424 | +1.0295 | `2026-07-19T13:59:51Z` → `2026-07-19T15:16:52Z` |
| ALPHA | 631 | 3 | 628 | -0.4312 | `2026-07-19T13:59:53Z` → `2026-07-19T15:37:12Z` |
| **TOTAL** | | 51 | | **+0.5983** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 321 | 75.7% |
| `wall_not_collapsed` | 61 | 14.4% |
| `radar_block` | 41 | 9.7% |
| `stase_ecoute` | 1 | 0.2% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 371 | 59.1% |
| `radar_block` | 99 | 15.8% |
| `wall_not_collapsed` | 87 | 13.9% |
| `duo_wait` | 45 | 7.2% |
| `tension_stale` | 23 | 3.7% |
| `tactic_mismatch` | 3 | 0.5% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

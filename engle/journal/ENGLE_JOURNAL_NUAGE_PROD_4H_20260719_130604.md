# JOURNAL ENGLE — NUAGE_PROD_4H

- Généré: `2026-07-19T13:06:04Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-19T12:53:13Z`
- CSV: `NUAGE_PROD_4H_BETA_X5.csv` · `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 53 | 79.1% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 3 | 4.5% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 11 | 16.4% | 11 | -0.0222 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.3575 · σ=1.0456 · n=67

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 67 | 11 | 56 | -0.0222 | `2026-07-19T12:53:37Z` → `2026-07-19T13:05:55Z` |
| ALPHA | 65 | 3 | 62 | -0.1628 | `2026-07-19T12:53:32Z` → `2026-07-19T13:05:47Z` |
| **TOTAL** | | 14 | | **-0.1849** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 49 | 87.5% |
| `radar_block` | 5 | 8.9% |
| `stase_ecoute` | 1 | 1.8% |
| `wall_not_collapsed` | 1 | 1.8% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 37 | 59.7% |
| `radar_block` | 14 | 22.6% |
| `duo_wait` | 6 | 9.7% |
| `wall_not_collapsed` | 5 | 8.1% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

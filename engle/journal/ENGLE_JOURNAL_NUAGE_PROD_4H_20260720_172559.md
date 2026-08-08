# JOURNAL ENGLE — NUAGE_PROD_4H

- Généré: `2026-07-20T17:25:59Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-20T16:57:40Z`
- CSV: `NUAGE_PROD_4H_BETA_X5.csv` · `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 25 | 65.8% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 4 | 10.5% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 9 | 23.7% | 9 | +0.5754 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.6513 · σ=1.2628 · n=38

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 38 | 9 | 29 | +0.5754 | `2026-07-20T16:58:12Z` → `2026-07-20T17:05:55Z` |
| ALPHA | 159 | 1 | 158 | -2.0494 | `2026-07-20T16:57:53Z` → `2026-07-20T17:25:51Z` |
| **TOTAL** | | 10 | | **-1.4739** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 22 | 75.9% |
| `wall_not_collapsed` | 4 | 13.8% |
| `radar_block` | 2 | 6.9% |
| `stase_ecoute` | 1 | 3.4% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 73 | 46.2% |
| `duo_wait` | 37 | 23.4% |
| `wall_not_collapsed` | 19 | 12.0% |
| `radar_block` | 19 | 12.0% |
| `tension_stale` | 7 | 4.4% |
| `tactic_mismatch` | 2 | 1.3% |
| `stase_ecoute` | 1 | 0.6% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

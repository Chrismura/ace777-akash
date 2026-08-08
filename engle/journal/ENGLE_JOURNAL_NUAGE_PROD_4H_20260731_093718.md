# JOURNAL ENGLE — NUAGE_PROD_4H

- Généré: `2026-07-31T09:37:18Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-31T05:15:51Z`
- CSV: `NUAGE_PROD_4H_BETA_X5.csv` · `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 614 | 65.8% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 181 | 19.4% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 138 | 14.8% | 47 | +1.5350 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.4825 · σ=1.2148 · n=933

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 933 | 47 | 886 | +1.5350 | `2026-07-31T05:16:31Z` → `2026-07-31T09:15:43Z` |
| ALPHA | 993 | 2 | 991 | -3.3345 | `2026-07-31T05:16:04Z` → `2026-07-31T09:15:56Z` |
| **TOTAL** | | 49 | | **-1.7995** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 561 | 63.3% |
| `wall_not_collapsed` | 140 | 15.8% |
| `radar_block` | 95 | 10.7% |
| `vacuum_filter` | 85 | 9.6% |
| `tactic_mismatch` | 5 | 0.6% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 617 | 62.3% |
| `wall_not_collapsed` | 146 | 14.7% |
| `radar_block` | 101 | 10.2% |
| `vacuum_filter` | 68 | 6.9% |
| `tension_stale` | 55 | 5.5% |
| `tactic_mismatch` | 4 | 0.4% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

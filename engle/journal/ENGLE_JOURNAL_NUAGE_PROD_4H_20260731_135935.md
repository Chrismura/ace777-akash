# JOURNAL ENGLE — NUAGE_PROD_4H

- Généré: `2026-07-31T13:59:35Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-31T09:38:01Z`
- CSV: `NUAGE_PROD_4H_BETA_X5.csv` · `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 804 | 87.0% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 81 | 8.8% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 39 | 4.2% | 37 | +0.6630 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.1562 · σ=0.8013 · n=924

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 924 | 37 | 886 | +0.6630 | `2026-07-31T09:38:15Z` → `2026-07-31T13:01:25Z` |
| ALPHA | 916 | 2 | 914 | +8.0032 | `2026-07-31T09:38:18Z` → `2026-07-31T13:01:26Z` |
| **TOTAL** | | 39 | | **+8.6662** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 738 | 83.3% |
| `radar_block` | 99 | 11.2% |
| `wall_not_collapsed` | 44 | 5.0% |
| `stase_ecoute` | 3 | 0.3% |
| `tactic_mismatch` | 2 | 0.2% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 725 | 79.3% |
| `radar_block` | 101 | 11.1% |
| `wall_not_collapsed` | 42 | 4.6% |
| `tension_stale` | 23 | 2.5% |
| `duo_wait` | 21 | 2.3% |
| `tactic_mismatch` | 2 | 0.2% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

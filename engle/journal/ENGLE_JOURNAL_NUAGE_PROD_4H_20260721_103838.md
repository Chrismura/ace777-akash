# JOURNAL ENGLE — NUAGE_PROD_4H

- Généré: `2026-07-21T10:38:38Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-21T07:57:10Z`
- CSV: `NUAGE_PROD_4H_BETA_X5.csv` · `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 327 | 63.0% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 109 | 21.0% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 83 | 16.0% | 39 | -0.3664 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.6249 · σ=1.6413 · n=519

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 519 | 39 | 480 | -0.3664 | `2026-07-21T07:57:20Z` → `2026-07-21T09:32:36Z` |
| ALPHA | 1009 | 2 | 1007 | +0.1057 | `2026-07-21T07:57:22Z` → `2026-07-21T10:34:52Z` |
| **TOTAL** | | 41 | | **-0.2607** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 305 | 63.5% |
| `wall_not_collapsed` | 85 | 17.7% |
| `radar_block` | 47 | 9.8% |
| `vacuum_filter` | 43 | 9.0% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 549 | 54.5% |
| `radar_block` | 211 | 21.0% |
| `wall_not_collapsed` | 116 | 11.5% |
| `vacuum_filter` | 74 | 7.3% |
| `duo_wait` | 45 | 4.5% |
| `tension_stale` | 11 | 1.1% |
| `tactic_mismatch` | 1 | 0.1% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

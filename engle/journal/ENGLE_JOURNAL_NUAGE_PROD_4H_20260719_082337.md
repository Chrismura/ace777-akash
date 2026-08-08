# JOURNAL ENGLE — NUAGE_PROD_4H

- Généré: `2026-07-19T08:23:37Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-19T07:19:13Z`
- CSV: `NUAGE_PROD_4H_BETA_X5.csv` · `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 308 | 73.7% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 87 | 20.8% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 23 | 5.5% | 23 | +0.1301 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.2327 · σ=0.7889 · n=418

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 418 | 23 | 395 | +0.1301 | `2026-07-19T07:19:29Z` → `2026-07-19T08:23:33Z` |
| ALPHA | 400 | 0 | 400 | +0.0000 | `2026-07-19T07:19:33Z` → `2026-07-19T08:23:29Z` |
| **TOTAL** | | 23 | | **+0.1301** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 296 | 74.9% |
| `wall_not_collapsed` | 68 | 17.2% |
| `radar_block` | 31 | 7.8% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 283 | 70.8% |
| `wall_not_collapsed` | 52 | 13.0% |
| `radar_block` | 38 | 9.5% |
| `duo_wait` | 15 | 3.8% |
| `tension_stale` | 12 | 3.0% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

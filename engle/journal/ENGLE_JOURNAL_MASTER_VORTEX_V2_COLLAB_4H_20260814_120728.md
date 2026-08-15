# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-14T12:07:28Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-14T11:57:07Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 44 | 64.7% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 17 | 25.0% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 7 | 10.3% | 7 | +0.1379 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.4903 · σ=1.3215 · n=68

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 68 | 7 | 61 | +0.1379 | `2026-08-14T11:57:16Z` → `2026-08-14T12:07:19Z` |
| ALPHA | 64 | 2 | 62 | -0.0402 | `2026-08-14T11:57:19Z` → `2026-08-14T12:06:17Z` |
| **TOTAL** | | 9 | | **+0.0977** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 39 | 63.9% |
| `wall_not_collapsed` | 12 | 19.7% |
| `radar_block` | 9 | 14.8% |
| `tactic_mismatch` | 1 | 1.6% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 40 | 64.5% |
| `wall_not_collapsed` | 13 | 21.0% |
| `radar_block` | 5 | 8.1% |
| `duo_wait` | 3 | 4.8% |
| `tactic_mismatch` | 1 | 1.6% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

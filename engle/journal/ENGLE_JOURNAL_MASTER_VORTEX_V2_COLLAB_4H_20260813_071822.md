# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-13T07:18:22Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-13T07:01:25Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 96 | 81.4% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 12 | 10.2% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 10 | 8.5% | 10 | +0.0088 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.2938 · σ=1.0799 · n=118

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 118 | 10 | 108 | +0.0088 | `2026-08-13T07:01:34Z` → `2026-08-13T07:18:14Z` |
| ALPHA | 110 | 5 | 105 | +0.4031 | `2026-08-13T07:01:36Z` → `2026-08-13T07:17:03Z` |
| **TOTAL** | | 15 | | **+0.4119** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 83 | 76.9% |
| `radar_block` | 14 | 13.0% |
| `wall_not_collapsed` | 8 | 7.4% |
| `tactic_mismatch` | 3 | 2.8% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 76 | 72.4% |
| `radar_block` | 14 | 13.3% |
| `wall_not_collapsed` | 9 | 8.6% |
| `duo_wait` | 5 | 4.8% |
| `tactic_mismatch` | 1 | 1.0% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

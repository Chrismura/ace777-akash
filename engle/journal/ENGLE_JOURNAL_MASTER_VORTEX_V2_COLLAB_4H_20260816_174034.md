# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-16T17:40:34Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-16T17:26:51Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 16 | 88.9% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 1 | 5.6% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 1 | 5.6% | 1 | +0.0000 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.1481 · σ=0.4731 · n=18

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 18 | 1 | 17 | +0.0000 | `2026-08-16T17:28:08Z` → `2026-08-16T17:40:02Z` |
| ALPHA | 25 | 0 | 25 | +0.0000 | `2026-08-16T17:28:15Z` → `2026-08-16T17:39:23Z` |
| **TOTAL** | | 1 | | **+0.0000** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `gap_guard_pause` | 8 | 47.1% |
| `momentum_too_small` | 7 | 41.2% |
| `radar_block` | 1 | 5.9% |
| `wall_not_collapsed` | 1 | 5.9% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `gap_guard_pause` | 16 | 64.0% |
| `momentum_too_small` | 6 | 24.0% |
| `duo_wait` | 2 | 8.0% |
| `radar_block` | 1 | 4.0% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

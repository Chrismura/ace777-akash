# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-15T12:47:51Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-15T10:45:30Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 607 | 74.8% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 139 | 17.1% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 66 | 8.1% | 66 | +0.5182 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.3150 · σ=1.0249 · n=812

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 812 | 66 | 746 | +0.5182 | `2026-08-15T10:45:40Z` → `2026-08-15T12:47:46Z` |
| ALPHA | 809 | 41 | 768 | -0.3393 | `2026-08-15T10:45:43Z` → `2026-08-15T12:47:47Z` |
| **TOTAL** | | 107 | | **+0.1789** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 579 | 77.6% |
| `wall_not_collapsed` | 106 | 14.2% |
| `radar_block` | 58 | 7.8% |
| `tactic_mismatch` | 2 | 0.3% |
| `stase_ecoute` | 1 | 0.1% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 553 | 72.0% |
| `wall_not_collapsed` | 107 | 13.9% |
| `radar_block` | 61 | 7.9% |
| `duo_wait` | 43 | 5.6% |
| `stase_ecoute` | 2 | 0.3% |
| `tactic_mismatch` | 2 | 0.3% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

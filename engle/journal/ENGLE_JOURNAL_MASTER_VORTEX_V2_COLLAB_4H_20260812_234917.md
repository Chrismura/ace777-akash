# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-12T23:49:17Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-12T23:27:36Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 63 | 79.7% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 9 | 11.4% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 7 | 8.9% | 7 | -0.1175 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.2893 · σ=0.8834 · n=79

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 79 | 7 | 72 | -0.1175 | `2026-08-12T23:28:00Z` → `2026-08-12T23:43:47Z` |
| ALPHA | 94 | 5 | 89 | +0.3771 | `2026-08-12T23:28:03Z` → `2026-08-12T23:49:08Z` |
| **TOTAL** | | 12 | | **+0.2596** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 30 | 41.7% |
| `gap_guard_pause` | 27 | 37.5% |
| `wall_not_collapsed` | 7 | 9.7% |
| `radar_block` | 5 | 6.9% |
| `stase_ecoute` | 2 | 2.8% |
| `tactic_mismatch` | 1 | 1.4% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 74 | 83.1% |
| `wall_not_collapsed` | 11 | 12.4% |
| `radar_block` | 3 | 3.4% |
| `duo_wait` | 1 | 1.1% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

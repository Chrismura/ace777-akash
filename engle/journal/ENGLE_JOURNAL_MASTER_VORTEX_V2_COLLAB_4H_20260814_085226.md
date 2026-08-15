# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-14T08:52:26Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-14T08:31:24Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 61 | 69.3% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 8 | 9.1% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 19 | 21.6% | 19 | -0.1249 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.7739 · σ=1.6300 · n=88

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 88 | 19 | 69 | -0.1249 | `2026-08-14T08:31:45Z` → `2026-08-14T08:49:20Z` |
| ALPHA | 108 | 13 | 95 | +6.6727 | `2026-08-14T08:31:37Z` → `2026-08-14T08:52:17Z` |
| **TOTAL** | | 32 | | **+6.5478** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 54 | 78.3% |
| `radar_block` | 6 | 8.7% |
| `wall_not_collapsed` | 6 | 8.7% |
| `tactic_mismatch` | 3 | 4.3% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 63 | 66.3% |
| `radar_block` | 16 | 16.8% |
| `wall_not_collapsed` | 10 | 10.5% |
| `duo_wait` | 4 | 4.2% |
| `tactic_mismatch` | 2 | 2.1% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

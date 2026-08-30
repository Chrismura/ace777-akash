# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-21T10:37:24Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-21T10:08:07Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 109 | 80.7% | 19 | +1.1297 |
| TRANSITOIRE (bruit retail) | 25 | 18.5% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 1 | 0.7% | 0 | +0.0000 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.0970 · σ=0.2654 · n=135

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 135 | 19 | 115 | +1.1297 | `2026-08-21T10:08:17Z` → `2026-08-21T10:37:21Z` |
| ALPHA | 142 | 13 | 129 | +7.9826 | `2026-08-21T10:08:21Z` → `2026-08-21T10:37:15Z` |
| **TOTAL** | | 32 | | **+9.1124** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 74 | 64.3% |
| `radar_block` | 19 | 16.5% |
| `wall_not_collapsed` | 17 | 14.8% |
| `tactic_mismatch` | 3 | 2.6% |
| `stase_ecoute` | 2 | 1.7% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 82 | 63.6% |
| `radar_block` | 22 | 17.1% |
| `wall_not_collapsed` | 14 | 10.9% |
| `duo_wait` | 5 | 3.9% |
| `stase_ecoute` | 3 | 2.3% |
| `tactic_mismatch` | 3 | 2.3% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

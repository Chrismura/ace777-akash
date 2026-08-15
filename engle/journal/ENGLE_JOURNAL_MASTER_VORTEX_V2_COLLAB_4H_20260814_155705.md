# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-14T15:57:05Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-14T12:51:05Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 918 | 73.8% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 167 | 13.4% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 159 | 12.8% | 155 | +0.3956 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.4896 · σ=1.4285 · n=1244

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 1244 | 155 | 1089 | +0.3956 | `2026-08-14T12:51:14Z` → `2026-08-14T15:57:03Z` |
| ALPHA | 1320 | 65 | 1255 | +28.2570 | `2026-08-14T12:51:16Z` → `2026-08-14T15:56:59Z` |
| **TOTAL** | | 220 | | **+28.6526** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 859 | 78.9% |
| `wall_not_collapsed` | 113 | 10.4% |
| `radar_block` | 101 | 9.3% |
| `tactic_mismatch` | 11 | 1.0% |
| `stase_ecoute` | 5 | 0.5% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 883 | 70.4% |
| `wall_not_collapsed` | 117 | 9.3% |
| `radar_block` | 114 | 9.1% |
| `duo_wait` | 114 | 9.1% |
| `tactic_mismatch` | 21 | 1.7% |
| `stase_ecoute` | 6 | 0.5% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-18T04:20:41Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-18T00:41:22Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 1032 | 91.0% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 34 | 3.0% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 68 | 6.0% | 67 | +7.1211 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.2072 · σ=0.9409 · n=1134

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 1134 | 67 | 1059 | +7.1211 | `2026-08-18T00:41:41Z` → `2026-08-18T04:20:38Z` |
| ALPHA | 1138 | 28 | 1110 | +28.9414 | `2026-08-18T00:41:41Z` → `2026-08-18T04:20:34Z` |
| **TOTAL** | | 95 | | **+36.0625** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 1008 | 95.2% |
| `wall_not_collapsed` | 22 | 2.1% |
| `radar_block` | 19 | 1.8% |
| `tactic_mismatch` | 7 | 0.7% |
| `stase_ecoute` | 3 | 0.3% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 1003 | 90.4% |
| `duo_wait` | 56 | 5.0% |
| `wall_not_collapsed` | 23 | 2.1% |
| `radar_block` | 19 | 1.7% |
| `tactic_mismatch` | 9 | 0.8% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

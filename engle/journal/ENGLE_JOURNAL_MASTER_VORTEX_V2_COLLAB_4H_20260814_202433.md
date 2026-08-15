# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-14T20:24:33Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-14T19:54:23Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 115 | 68.0% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 32 | 18.9% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 22 | 13.0% | 22 | +0.2811 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.3834 · σ=0.9828 · n=169

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 169 | 22 | 147 | +0.2811 | `2026-08-14T19:54:34Z` → `2026-08-14T20:24:28Z` |
| ALPHA | 177 | 11 | 166 | +7.5524 | `2026-08-14T19:54:36Z` → `2026-08-14T20:24:30Z` |
| **TOTAL** | | 33 | | **+7.8336** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 108 | 73.5% |
| `wall_not_collapsed` | 22 | 15.0% |
| `radar_block` | 14 | 9.5% |
| `tactic_mismatch` | 3 | 2.0% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 123 | 74.1% |
| `wall_not_collapsed` | 16 | 9.6% |
| `radar_block` | 13 | 7.8% |
| `duo_wait` | 11 | 6.6% |
| `tactic_mismatch` | 3 | 1.8% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

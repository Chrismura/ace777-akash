# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-22T19:13:18Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-22T15:44:10Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 259 | 95.2% | 13 | -0.7378 |
| TRANSITOIRE (bruit retail) | 12 | 4.4% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 1 | 0.4% | 0 | +0.0000 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.0383 · σ=0.2200 · n=272

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 272 | 13 | 257 | -0.7378 | `2026-08-22T15:44:53Z` → `2026-08-22T19:12:57Z` |
| ALPHA | 259 | 9 | 249 | +2.0052 | `2026-08-22T15:45:04Z` → `2026-08-22T19:12:26Z` |
| **TOTAL** | | 22 | | **+1.2674** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `gap_guard_pause` | 222 | 86.4% |
| `regime_gate` | 19 | 7.4% |
| `wall_not_collapsed` | 9 | 3.5% |
| `radar_block` | 4 | 1.6% |
| `tactic_mismatch` | 3 | 1.2% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `gap_guard_pause` | 193 | 77.5% |
| `regime_gate` | 27 | 10.8% |
| `duo_wait` | 9 | 3.6% |
| `wall_not_collapsed` | 9 | 3.6% |
| `tactic_mismatch` | 6 | 2.4% |
| `radar_block` | 4 | 1.6% |
| `stase_ecoute` | 1 | 0.4% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-13T16:44:48Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-13T16:16:22Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 116 | 66.3% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 35 | 20.0% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 24 | 13.7% | 21 | -0.3269 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.4832 · σ=1.1826 · n=175

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 175 | 21 | 154 | -0.3269 | `2026-08-13T16:16:32Z` → `2026-08-13T16:44:40Z` |
| ALPHA | 153 | 4 | 149 | +2.3134 | `2026-08-13T16:16:34Z` → `2026-08-13T16:39:36Z` |
| **TOTAL** | | 25 | | **+1.9866** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 101 | 65.6% |
| `wall_not_collapsed` | 30 | 19.5% |
| `radar_block` | 22 | 14.3% |
| `stase_ecoute` | 1 | 0.6% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 98 | 65.8% |
| `wall_not_collapsed` | 19 | 12.8% |
| `duo_wait` | 18 | 12.1% |
| `radar_block` | 11 | 7.4% |
| `tactic_mismatch` | 3 | 2.0% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

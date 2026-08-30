# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-20T14:32:51Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-20T14:06:28Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 81 | 84.4% | 18 | +0.2532 |
| TRANSITOIRE (bruit retail) | 15 | 15.6% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 0 | 0.0% | 0 | +0.0000 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.0837 · σ=0.2378 · n=96

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 96 | 18 | 78 | +0.2532 | `2026-08-20T14:06:39Z` → `2026-08-20T14:32:47Z` |
| ALPHA | 133 | 12 | 121 | -3.8409 | `2026-08-20T14:06:42Z` → `2026-08-20T14:32:41Z` |
| **TOTAL** | | 30 | | **-3.5877** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 49 | 62.8% |
| `radar_block` | 14 | 17.9% |
| `wall_not_collapsed` | 11 | 14.1% |
| `stase_ecoute` | 3 | 3.8% |
| `tactic_mismatch` | 1 | 1.3% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 44 | 36.4% |
| `gap_guard_pause` | 42 | 34.7% |
| `radar_block` | 16 | 13.2% |
| `wall_not_collapsed` | 11 | 9.1% |
| `tactic_mismatch` | 5 | 4.1% |
| `stase_ecoute` | 2 | 1.7% |
| `duo_wait` | 1 | 0.8% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

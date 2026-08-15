# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-13T08:41:34Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-13T07:18:30Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 574 | 88.0% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 43 | 6.6% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 35 | 5.4% | 34 | -0.0528 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.1407 · σ=0.5163 · n=652

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 652 | 34 | 618 | -0.0528 | `2026-08-13T07:18:40Z` → `2026-08-13T08:41:29Z` |
| ALPHA | 69 | 2 | 67 | +1.6361 | `2026-08-13T07:18:42Z` → `2026-08-13T07:28:16Z` |
| **TOTAL** | | 36 | | **+1.5833** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 307 | 49.7% |
| `radar_block` | 203 | 32.8% |
| `gap_guard_pause` | 75 | 12.1% |
| `wall_not_collapsed` | 32 | 5.2% |
| `stase_ecoute` | 1 | 0.2% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 49 | 73.1% |
| `wall_not_collapsed` | 7 | 10.4% |
| `duo_wait` | 5 | 7.5% |
| `radar_block` | 4 | 6.0% |
| `tactic_mismatch` | 2 | 3.0% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

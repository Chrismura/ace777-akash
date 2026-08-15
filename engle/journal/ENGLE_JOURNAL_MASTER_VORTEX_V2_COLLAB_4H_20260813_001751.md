# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-13T00:17:51Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-13T00:03:14Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 55 | 79.7% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 9 | 13.0% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 5 | 7.2% | 5 | -0.0948 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.2694 · σ=0.7013 · n=69

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 69 | 5 | 64 | -0.0948 | `2026-08-13T00:03:31Z` → `2026-08-13T00:17:42Z` |
| ALPHA | 50 | 5 | 45 | +4.7418 | `2026-08-13T00:03:28Z` → `2026-08-13T00:14:51Z` |
| **TOTAL** | | 10 | | **+4.6470** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 49 | 76.6% |
| `wall_not_collapsed` | 9 | 14.1% |
| `radar_block` | 5 | 7.8% |
| `tactic_mismatch` | 1 | 1.6% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 31 | 68.9% |
| `radar_block` | 9 | 20.0% |
| `wall_not_collapsed` | 5 | 11.1% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-13T00:42:53Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-13T00:17:59Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 96 | 87.3% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 8 | 7.3% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 6 | 5.5% | 5 | -0.4116 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.1956 · σ=1.1429 · n=110

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 110 | 5 | 105 | -0.4116 | `2026-08-13T00:18:12Z` → `2026-08-13T00:40:39Z` |
| ALPHA | 115 | 7 | 108 | +3.0258 | `2026-08-13T00:18:20Z` → `2026-08-13T00:42:44Z` |
| **TOTAL** | | 12 | | **+2.6142** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 84 | 80.0% |
| `radar_block` | 15 | 14.3% |
| `wall_not_collapsed` | 3 | 2.9% |
| `tactic_mismatch` | 2 | 1.9% |
| `stase_ecoute` | 1 | 1.0% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 76 | 70.4% |
| `radar_block` | 18 | 16.7% |
| `wall_not_collapsed` | 10 | 9.3% |
| `duo_wait` | 2 | 1.9% |
| `stase_ecoute` | 1 | 0.9% |
| `tactic_mismatch` | 1 | 0.9% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

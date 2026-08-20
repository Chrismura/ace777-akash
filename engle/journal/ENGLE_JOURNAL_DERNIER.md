# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-20T19:42:05Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-20T19:14:14Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 102 | 77.9% | 21 | -0.9346 |
| TRANSITOIRE (bruit retail) | 29 | 22.1% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 0 | 0.0% | 0 | +0.0000 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.1042 · σ=0.2287 · n=131

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 131 | 21 | 110 | -0.9346 | `2026-08-20T19:14:26Z` → `2026-08-20T19:42:02Z` |
| ALPHA | 132 | 15 | 117 | +5.2772 | `2026-08-20T19:14:28Z` → `2026-08-20T19:41:49Z` |
| **TOTAL** | | 36 | | **+4.3426** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 74 | 67.3% |
| `wall_not_collapsed` | 24 | 21.8% |
| `radar_block` | 8 | 7.3% |
| `stase_ecoute` | 2 | 1.8% |
| `tactic_mismatch` | 2 | 1.8% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 86 | 73.5% |
| `wall_not_collapsed` | 20 | 17.1% |
| `tactic_mismatch` | 6 | 5.1% |
| `radar_block` | 5 | 4.3% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

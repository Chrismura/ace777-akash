# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-14T19:53:49Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-14T19:36:09Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 92 | 83.6% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 13 | 11.8% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 5 | 4.5% | 4 | +0.0033 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.2353 · σ=0.9839 · n=110

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 110 | 4 | 106 | +0.0033 | `2026-08-14T19:36:21Z` → `2026-08-14T19:53:46Z` |
| ALPHA | 111 | 0 | 111 | +0.0000 | `2026-08-14T19:36:23Z` → `2026-08-14T19:53:45Z` |
| **TOTAL** | | 4 | | **+0.0033** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 91 | 85.8% |
| `wall_not_collapsed` | 9 | 8.5% |
| `radar_block` | 6 | 5.7% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 95 | 85.6% |
| `radar_block` | 9 | 8.1% |
| `wall_not_collapsed` | 7 | 6.3% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

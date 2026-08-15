# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-12T23:12:30Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-12T22:41:31Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 60 | 68.2% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 19 | 21.6% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 9 | 10.2% | 9 | +0.0600 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.4414 · σ=1.3970 · n=88

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 88 | 9 | 79 | +0.0600 | `2026-08-12T22:41:56Z` → `2026-08-12T23:12:25Z` |
| ALPHA | 86 | 7 | 79 | -1.9393 | `2026-08-12T22:41:59Z` → `2026-08-12T23:12:23Z` |
| **TOTAL** | | 16 | | **-1.8794** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 55 | 69.6% |
| `wall_not_collapsed` | 12 | 15.2% |
| `radar_block` | 11 | 13.9% |
| `tactic_mismatch` | 1 | 1.3% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 56 | 70.9% |
| `wall_not_collapsed` | 12 | 15.2% |
| `radar_block` | 6 | 7.6% |
| `duo_wait` | 5 | 6.3% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-13T17:34:21Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-13T17:17:51Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 68 | 71.6% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 13 | 13.7% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 14 | 14.7% | 12 | -0.0870 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.3953 · σ=0.9007 · n=95

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 95 | 12 | 83 | -0.0870 | `2026-08-13T17:18:01Z` → `2026-08-13T17:34:13Z` |
| ALPHA | 67 | 9 | 58 | +3.3333 | `2026-08-13T17:18:03Z` → `2026-08-13T17:30:20Z` |
| **TOTAL** | | 21 | | **+3.2463** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 58 | 69.9% |
| `radar_block` | 17 | 20.5% |
| `wall_not_collapsed` | 7 | 8.4% |
| `tactic_mismatch` | 1 | 1.2% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 27 | 46.6% |
| `radar_block` | 16 | 27.6% |
| `wall_not_collapsed` | 8 | 13.8% |
| `duo_wait` | 6 | 10.3% |
| `tactic_mismatch` | 1 | 1.7% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

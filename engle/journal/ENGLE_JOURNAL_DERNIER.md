# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-19T20:57:06Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-19T13:13:56Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 1336 | 66.5% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 356 | 17.7% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 318 | 15.8% | 255 | -4.2185 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.6408 · σ=1.6709 · n=2010

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 2010 | 255 | 1698 | -4.2185 | `2026-08-19T13:14:23Z` → `2026-08-19T20:57:02Z` |
| ALPHA | 2104 | 119 | 1963 | -44.4402 | `2026-08-19T13:14:11Z` → `2026-08-19T20:56:58Z` |
| **TOTAL** | | 374 | | **-48.6587** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 805 | 47.4% |
| `radar_block` | 354 | 20.8% |
| `gap_guard_pause` | 253 | 14.9% |
| `wall_not_collapsed` | 219 | 12.9% |
| `tactic_mismatch` | 40 | 2.4% |
| `stase_ecoute` | 27 | 1.6% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 854 | 43.5% |
| `radar_block` | 323 | 16.5% |
| `wall_not_collapsed` | 264 | 13.4% |
| `duo_wait` | 244 | 12.4% |
| `gap_guard_pause` | 224 | 11.4% |
| `tactic_mismatch` | 35 | 1.8% |
| `stase_ecoute` | 19 | 1.0% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

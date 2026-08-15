# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-14T19:35:48Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-14T16:24:21Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 887 | 72.4% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 206 | 16.8% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 132 | 10.8% | 131 | +1.6846 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.4020 · σ=1.2458 · n=1225

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 1225 | 131 | 1094 | +1.6846 | `2026-08-14T16:24:30Z` → `2026-08-14T19:35:45Z` |
| ALPHA | 1371 | 26 | 1345 | +9.0607 | `2026-08-14T16:24:31Z` → `2026-08-14T19:35:45Z` |
| **TOTAL** | | 157 | | **+10.7453** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 844 | 77.1% |
| `wall_not_collapsed` | 132 | 12.1% |
| `radar_block` | 99 | 9.0% |
| `tactic_mismatch` | 14 | 1.3% |
| `stase_ecoute` | 5 | 0.5% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 927 | 68.9% |
| `wall_not_collapsed` | 144 | 10.7% |
| `duo_wait` | 103 | 7.7% |
| `radar_block` | 96 | 7.1% |
| `gap_guard_pause` | 59 | 4.4% |
| `tactic_mismatch` | 15 | 1.1% |
| `stase_ecoute` | 1 | 0.1% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

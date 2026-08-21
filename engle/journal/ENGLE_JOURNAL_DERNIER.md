# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-21T23:22:01Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-21T19:44:48Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 1150 | 94.5% | 64 | -16.4899 |
| TRANSITOIRE (bruit retail) | 60 | 4.9% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 7 | 0.6% | 0 | +0.0000 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.0511 · σ=0.3749 · n=1217

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 1217 | 64 | 1149 | -16.4899 | `2026-08-21T19:45:49Z` → `2026-08-21T23:21:25Z` |
| ALPHA | 1172 | 40 | 1132 | +38.5450 | `2026-08-21T19:45:36Z` → `2026-08-21T23:21:47Z` |
| **TOTAL** | | 104 | | **+22.0551** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `gap_guard_pause` | 934 | 81.3% |
| `regime_gate` | 113 | 9.8% |
| `wall_not_collapsed` | 46 | 4.0% |
| `radar_block` | 21 | 1.8% |
| `stase_ecoute` | 19 | 1.7% |
| `tactic_mismatch` | 16 | 1.4% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `gap_guard_pause` | 779 | 68.8% |
| `regime_gate` | 176 | 15.5% |
| `wall_not_collapsed` | 66 | 5.8% |
| `duo_wait` | 39 | 3.4% |
| `tactic_mismatch` | 31 | 2.7% |
| `radar_block` | 26 | 2.3% |
| `stase_ecoute` | 15 | 1.3% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

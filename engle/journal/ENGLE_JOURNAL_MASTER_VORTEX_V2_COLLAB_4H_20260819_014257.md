# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-19T01:42:57Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-18T19:33:49Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 1146 | 66.4% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 351 | 20.3% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 229 | 13.3% | 226 | +3.4574 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.5194 · σ=1.4329 · n=1726

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 1726 | 226 | 1499 | +3.4574 | `2026-08-18T19:34:20Z` → `2026-08-19T01:42:54Z` |
| ALPHA | 1876 | 61 | 1815 | +0.1371 | `2026-08-18T19:34:25Z` → `2026-08-19T01:42:53Z` |
| **TOTAL** | | 287 | | **+3.5944** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 921 | 61.4% |
| `wall_not_collapsed` | 245 | 16.3% |
| `gap_guard_pause` | 163 | 10.9% |
| `radar_block` | 156 | 10.4% |
| `tactic_mismatch` | 9 | 0.6% |
| `stase_ecoute` | 5 | 0.3% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 1045 | 57.6% |
| `wall_not_collapsed` | 289 | 15.9% |
| `duo_wait` | 213 | 11.7% |
| `radar_block` | 131 | 7.2% |
| `gap_guard_pause` | 124 | 6.8% |
| `tactic_mismatch` | 11 | 0.6% |
| `stase_ecoute` | 2 | 0.1% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

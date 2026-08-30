# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-21T09:40:56Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-21T09:24:57Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 245 | 88.4% | 18 | -1.1129 |
| TRANSITOIRE (bruit retail) | 30 | 10.8% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 2 | 0.7% | 0 | +0.0000 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.0769 · σ=0.2412 · n=277

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 277 | 18 | 259 | -1.1129 | `2026-08-21T09:25:13Z` → `2026-08-21T09:40:52Z` |
| ALPHA | 252 | 16 | 236 | +3.7674 | `2026-08-21T09:25:15Z` → `2026-08-21T09:40:53Z` |
| **TOTAL** | | 34 | | **+2.6546** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `gap_guard_pause` | 165 | 63.7% |
| `momentum_too_small` | 41 | 15.8% |
| `radar_block` | 24 | 9.3% |
| `wall_not_collapsed` | 24 | 9.3% |
| `tactic_mismatch` | 3 | 1.2% |
| `stase_ecoute` | 2 | 0.8% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `gap_guard_pause` | 138 | 58.5% |
| `momentum_too_small` | 31 | 13.1% |
| `radar_block` | 24 | 10.2% |
| `wall_not_collapsed` | 19 | 8.1% |
| `duo_wait` | 14 | 5.9% |
| `tactic_mismatch` | 5 | 2.1% |
| `stase_ecoute` | 5 | 2.1% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

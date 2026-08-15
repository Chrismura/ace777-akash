# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-14T12:40:35Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-14T12:17:37Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 110 | 73.8% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 15 | 10.1% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 24 | 16.1% | 24 | +0.0177 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.6152 · σ=1.5550 · n=149

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 149 | 24 | 125 | +0.0177 | `2026-08-14T12:17:45Z` → `2026-08-14T12:40:26Z` |
| ALPHA | 148 | 7 | 141 | +3.5478 | `2026-08-14T12:17:48Z` → `2026-08-14T12:37:50Z` |
| **TOTAL** | | 31 | | **+3.5656** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 102 | 81.6% |
| `wall_not_collapsed` | 11 | 8.8% |
| `radar_block` | 10 | 8.0% |
| `stase_ecoute` | 1 | 0.8% |
| `tactic_mismatch` | 1 | 0.8% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 99 | 70.2% |
| `wall_not_collapsed` | 23 | 16.3% |
| `radar_block` | 11 | 7.8% |
| `duo_wait` | 6 | 4.3% |
| `tactic_mismatch` | 2 | 1.4% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-20T19:13:13Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-20T18:50:34Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 73 | 82.0% | 17 | +2.2137 |
| TRANSITOIRE (bruit retail) | 16 | 18.0% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 0 | 0.0% | 0 | +0.0000 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.0972 · σ=0.2275 · n=89

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 89 | 17 | 72 | +2.2137 | `2026-08-20T18:50:45Z` → `2026-08-20T19:13:10Z` |
| ALPHA | 98 | 9 | 89 | -1.1247 | `2026-08-20T18:50:48Z` → `2026-08-20T19:11:24Z` |
| **TOTAL** | | 26 | | **+1.0889** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 44 | 61.1% |
| `wall_not_collapsed` | 13 | 18.1% |
| `radar_block` | 12 | 16.7% |
| `tactic_mismatch` | 3 | 4.2% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 56 | 62.9% |
| `wall_not_collapsed` | 13 | 14.6% |
| `radar_block` | 12 | 13.5% |
| `tactic_mismatch` | 4 | 4.5% |
| `duo_wait` | 3 | 3.4% |
| `stase_ecoute` | 1 | 1.1% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

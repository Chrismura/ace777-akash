# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-17T06:58:59Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-16T19:08:26Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 2066 | 67.1% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 549 | 17.8% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 465 | 15.1% | 303 | +0.4979 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.5987 · σ=1.5977 · n=3080

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 3080 | 303 | 2775 | +0.4979 | `2026-08-16T19:08:40Z` → `2026-08-17T06:58:46Z` |
| ALPHA | 3254 | 0 | 3118 | +0.0000 | `2026-08-16T19:08:42Z` → `2026-08-17T06:58:45Z` |
| **TOTAL** | | 303 | | **+0.4979** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 1873 | 67.5% |
| `wall_not_collapsed` | 382 | 13.8% |
| `radar_block` | 257 | 9.3% |
| `price_stasis` | 150 | 5.4% |
| `gap_guard_pause` | 64 | 2.3% |
| `tactic_mismatch` | 33 | 1.2% |
| `stase_ecoute` | 16 | 0.6% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 1886 | 60.5% |
| `wall_not_collapsed` | 501 | 16.1% |
| `duo_wait` | 359 | 11.5% |
| `radar_block` | 295 | 9.5% |
| `tactic_mismatch` | 40 | 1.3% |
| `price_stasis` | 37 | 1.2% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

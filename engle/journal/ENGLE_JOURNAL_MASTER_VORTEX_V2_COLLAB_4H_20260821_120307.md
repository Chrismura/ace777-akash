# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-21T12:03:07Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-21T11:04:45Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 507 | 97.1% | 11 | +3.0040 |
| TRANSITOIRE (bruit retail) | 15 | 2.9% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 0 | 0.0% | 0 | +0.0000 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.0163 · σ=0.1040 · n=522

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 522 | 11 | 509 | +3.0040 | `2026-08-21T11:04:53Z` → `2026-08-21T12:02:05Z` |
| ALPHA | 413 | 6 | 406 | +13.3590 | `2026-08-21T11:04:55Z` → `2026-08-21T12:02:23Z` |
| **TOTAL** | | 17 | | **+16.3631** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `gap_guard_pause` | 435 | 85.5% |
| `regime_gate` | 52 | 10.2% |
| `wall_not_collapsed` | 13 | 2.6% |
| `tactic_mismatch` | 4 | 0.8% |
| `stase_ecoute` | 3 | 0.6% |
| `radar_block` | 2 | 0.4% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `gap_guard_pause` | 250 | 61.6% |
| `regime_gate` | 84 | 20.7% |
| `duo_wait` | 40 | 9.9% |
| `wall_not_collapsed` | 23 | 5.7% |
| `radar_block` | 6 | 1.5% |
| `tactic_mismatch` | 3 | 0.7% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

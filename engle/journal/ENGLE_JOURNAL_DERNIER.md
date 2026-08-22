# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-22T11:32:54Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-22T07:32:28Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 463 | 94.7% | 22 | +0.0114 |
| TRANSITOIRE (bruit retail) | 24 | 4.9% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 2 | 0.4% | 0 | +0.0000 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.0437 · σ=0.3991 · n=489

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 489 | 22 | 467 | +0.0114 | `2026-08-22T07:33:00Z` → `2026-08-22T11:32:46Z` |
| ALPHA | 526 | 14 | 512 | -2.3637 | `2026-08-22T07:33:01Z` → `2026-08-22T11:32:44Z` |
| **TOTAL** | | 36 | | **-2.3523** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `gap_guard_pause` | 351 | 75.2% |
| `regime_gate` | 78 | 16.7% |
| `wall_not_collapsed` | 19 | 4.1% |
| `radar_block` | 7 | 1.5% |
| `tactic_mismatch` | 7 | 1.5% |
| `stase_ecoute` | 5 | 1.1% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `gap_guard_pause` | 278 | 54.3% |
| `regime_gate` | 140 | 27.3% |
| `wall_not_collapsed` | 36 | 7.0% |
| `duo_wait` | 25 | 4.9% |
| `radar_block` | 17 | 3.3% |
| `tactic_mismatch` | 11 | 2.1% |
| `stase_ecoute` | 5 | 1.0% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

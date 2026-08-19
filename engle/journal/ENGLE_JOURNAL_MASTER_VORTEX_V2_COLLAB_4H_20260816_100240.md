# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-16T10:02:40Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-16T08:02:31Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 548 | 79.7% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 69 | 10.0% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 71 | 10.3% | 23 | +0.0565 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.4336 · σ=1.3709 · n=688

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 688 | 23 | 665 | +0.0565 | `2026-08-16T08:02:41Z` → `2026-08-16T10:02:37Z` |
| ALPHA | 677 | 3 | 672 | -1.0421 | `2026-08-16T08:02:44Z` → `2026-08-16T10:02:30Z` |
| **TOTAL** | | 26 | | **-0.9856** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 528 | 79.4% |
| `wall_not_collapsed` | 51 | 7.7% |
| `price_stasis` | 48 | 7.2% |
| `radar_block` | 34 | 5.1% |
| `stase_ecoute` | 2 | 0.3% |
| `tactic_mismatch` | 2 | 0.3% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 511 | 76.0% |
| `duo_wait` | 60 | 8.9% |
| `wall_not_collapsed` | 47 | 7.0% |
| `radar_block` | 47 | 7.0% |
| `price_stasis` | 4 | 0.6% |
| `tactic_mismatch` | 3 | 0.4% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

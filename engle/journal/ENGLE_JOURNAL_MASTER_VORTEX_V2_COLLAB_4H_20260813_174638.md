# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-13T17:46:38Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-13T17:34:30Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 53 | 75.7% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 5 | 7.1% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 12 | 17.1% | 10 | -0.1961 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.5660 · σ=1.4555 · n=70

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 70 | 10 | 60 | -0.1961 | `2026-08-13T17:34:41Z` → `2026-08-13T17:46:31Z` |
| ALPHA | 46 | 5 | 41 | -6.5615 | `2026-08-13T17:34:43Z` → `2026-08-13T17:42:33Z` |
| **TOTAL** | | 15 | | **-6.7576** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 42 | 70.0% |
| `radar_block` | 12 | 20.0% |
| `wall_not_collapsed` | 4 | 6.7% |
| `tactic_mismatch` | 1 | 1.7% |
| `stase_ecoute` | 1 | 1.7% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 25 | 61.0% |
| `radar_block` | 8 | 19.5% |
| `wall_not_collapsed` | 5 | 12.2% |
| `duo_wait` | 1 | 2.4% |
| `tactic_mismatch` | 1 | 2.4% |
| `stase_ecoute` | 1 | 2.4% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

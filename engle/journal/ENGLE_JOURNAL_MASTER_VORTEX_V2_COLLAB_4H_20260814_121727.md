# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-14T12:17:27Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-14T12:07:37Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 54 | 78.3% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 8 | 11.6% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 7 | 10.1% | 6 | +0.0569 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.2422 · σ=0.6330 · n=69

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 69 | 6 | 63 | +0.0569 | `2026-08-14T12:07:46Z` → `2026-08-14T12:17:19Z` |
| ALPHA | 45 | 4 | 41 | -8.6278 | `2026-08-14T12:07:48Z` → `2026-08-14T12:14:17Z` |
| **TOTAL** | | 10 | | **-8.5708** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 51 | 81.0% |
| `radar_block` | 7 | 11.1% |
| `wall_not_collapsed` | 4 | 6.3% |
| `tactic_mismatch` | 1 | 1.6% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 29 | 70.7% |
| `duo_wait` | 5 | 12.2% |
| `wall_not_collapsed` | 3 | 7.3% |
| `radar_block` | 3 | 7.3% |
| `tactic_mismatch` | 1 | 2.4% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-12T22:41:19Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-12T22:23:54Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 41 | 75.9% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 8 | 14.8% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 5 | 9.3% | 3 | +0.0767 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.3060 · σ=0.8140 · n=54

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 54 | 3 | 51 | +0.0767 | `2026-08-12T22:24:08Z` → `2026-08-12T22:41:01Z` |
| ALPHA | 63 | 5 | 58 | -5.0264 | `2026-08-12T22:24:12Z` → `2026-08-12T22:38:16Z` |
| **TOTAL** | | 8 | | **-4.9497** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 39 | 76.5% |
| `wall_not_collapsed` | 6 | 11.8% |
| `radar_block` | 5 | 9.8% |
| `tactic_mismatch` | 1 | 2.0% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `gap_guard_pause` | 29 | 50.0% |
| `momentum_too_small` | 20 | 34.5% |
| `wall_not_collapsed` | 6 | 10.3% |
| `radar_block` | 2 | 3.4% |
| `duo_wait` | 1 | 1.7% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

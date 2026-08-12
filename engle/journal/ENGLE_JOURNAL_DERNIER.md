# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-12T21:00:03Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-12T16:59:39Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 663 | 77.7% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 113 | 13.2% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 77 | 9.0% | 77 | +1.2569 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.3127 · σ=0.9705 · n=853

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 853 | 77 | 776 | +1.2569 | `2026-08-12T17:00:07Z` → `2026-08-12T20:59:57Z` |
| ALPHA | 64 | 1 | 63 | +1.2663 | `2026-08-12T17:00:21Z` → `2026-08-12T17:18:12Z` |
| **TOTAL** | | 78 | | **+2.5232** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 385 | 49.6% |
| `gap_guard_pause` | 228 | 29.4% |
| `wall_not_collapsed` | 87 | 11.2% |
| `radar_block` | 71 | 9.1% |
| `stase_ecoute` | 3 | 0.4% |
| `tactic_mismatch` | 2 | 0.3% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `gap_guard_pause` | 34 | 54.0% |
| `momentum_too_small` | 21 | 33.3% |
| `wall_not_collapsed` | 5 | 7.9% |
| `tactic_mismatch` | 1 | 1.6% |
| `duo_wait` | 1 | 1.6% |
| `radar_block` | 1 | 1.6% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

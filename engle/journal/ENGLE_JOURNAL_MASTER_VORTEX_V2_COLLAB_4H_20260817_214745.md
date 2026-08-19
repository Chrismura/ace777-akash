# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-17T21:47:45Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-17T21:28:06Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 79 | 76.0% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 15 | 14.4% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 10 | 9.6% | 10 | +0.1222 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.2692 · σ=0.7686 · n=104

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 104 | 10 | 83 | +0.1222 | `2026-08-17T21:28:24Z` → `2026-08-17T21:47:38Z` |
| ALPHA | 101 | 6 | 89 | +0.3891 | `2026-08-17T21:28:20Z` → `2026-08-17T21:47:29Z` |
| **TOTAL** | | 16 | | **+0.5113** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 66 | 79.5% |
| `wall_not_collapsed` | 9 | 10.8% |
| `radar_block` | 8 | 9.6% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 65 | 73.0% |
| `wall_not_collapsed` | 9 | 10.1% |
| `radar_block` | 8 | 9.0% |
| `duo_wait` | 7 | 7.9% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

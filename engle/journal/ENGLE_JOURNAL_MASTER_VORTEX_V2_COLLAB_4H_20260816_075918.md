# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-16T07:59:18Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-16T07:19:59Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 186 | 84.5% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 23 | 10.5% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 11 | 5.0% | 11 | -0.0769 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.3483 · σ=1.6869 · n=220

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 220 | 11 | 209 | -0.0769 | `2026-08-16T07:20:24Z` → `2026-08-16T07:59:08Z` |
| ALPHA | 221 | 0 | 220 | +0.0000 | `2026-08-16T07:20:14Z` → `2026-08-16T07:59:09Z` |
| **TOTAL** | | 11 | | **-0.0769** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 182 | 87.1% |
| `radar_block` | 15 | 7.2% |
| `wall_not_collapsed` | 12 | 5.7% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 181 | 82.3% |
| `duo_wait` | 15 | 6.8% |
| `wall_not_collapsed` | 12 | 5.5% |
| `radar_block` | 12 | 5.5% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

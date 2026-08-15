# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-14T09:29:21Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-14T08:52:36Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 158 | 73.8% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 33 | 15.4% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 23 | 10.7% | 23 | +0.1764 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.3577 · σ=0.9780 · n=214

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 214 | 23 | 191 | +0.1764 | `2026-08-14T08:52:47Z` → `2026-08-14T09:29:12Z` |
| ALPHA | 203 | 3 | 200 | +0.4620 | `2026-08-14T08:52:49Z` → `2026-08-14T09:24:56Z` |
| **TOTAL** | | 26 | | **+0.6384** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 145 | 75.9% |
| `radar_block` | 24 | 12.6% |
| `wall_not_collapsed` | 21 | 11.0% |
| `stase_ecoute` | 1 | 0.5% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 142 | 71.0% |
| `duo_wait` | 23 | 11.5% |
| `wall_not_collapsed` | 19 | 9.5% |
| `radar_block` | 16 | 8.0% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-18T19:33:12Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-18T09:41:14Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 2317 | 65.7% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 705 | 20.0% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 502 | 14.2% | 466 | +14.4528 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.6033 · σ=1.6767 · n=3524

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 3524 | 466 | 3058 | +14.4528 | `2026-08-18T09:41:25Z` → `2026-08-18T19:31:25Z` |
| ALPHA | 3578 | 139 | 3439 | +40.8847 | `2026-08-18T09:41:26Z` → `2026-08-18T19:33:09Z` |
| **TOTAL** | | 605 | | **+55.3375** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 1724 | 56.4% |
| `wall_not_collapsed` | 514 | 16.8% |
| `radar_block` | 381 | 12.5% |
| `gap_guard_pause` | 377 | 12.3% |
| `tactic_mismatch` | 40 | 1.3% |
| `stase_ecoute` | 22 | 0.7% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 1957 | 56.9% |
| `wall_not_collapsed` | 585 | 17.0% |
| `duo_wait` | 401 | 11.7% |
| `radar_block` | 388 | 11.3% |
| `tactic_mismatch` | 53 | 1.5% |
| `gap_guard_pause` | 41 | 1.2% |
| `stase_ecoute` | 14 | 0.4% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

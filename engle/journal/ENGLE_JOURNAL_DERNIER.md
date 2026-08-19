# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-19T12:10:12Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-19T01:43:43Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 2106 | 64.3% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 705 | 21.5% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 462 | 14.1% | 459 | +0.1058 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.5667 · σ=1.4885 · n=3273

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 3273 | 459 | 2814 | +0.1058 | `2026-08-19T01:43:53Z` → `2026-08-19T12:09:58Z` |
| ALPHA | 3603 | 73 | 3431 | +14.1288 | `2026-08-19T01:43:55Z` → `2026-08-19T12:10:02Z` |
| **TOTAL** | | 532 | | **+14.2346** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 1803 | 64.1% |
| `wall_not_collapsed` | 468 | 16.6% |
| `radar_block` | 331 | 11.8% |
| `gap_guard_pause` | 164 | 5.8% |
| `tactic_mismatch` | 30 | 1.1% |
| `stase_ecoute` | 18 | 0.6% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 2044 | 59.6% |
| `wall_not_collapsed` | 541 | 15.8% |
| `duo_wait` | 398 | 11.6% |
| `radar_block` | 367 | 10.7% |
| `tactic_mismatch` | 38 | 1.1% |
| `gap_guard_pause` | 38 | 1.1% |
| `stase_ecoute` | 5 | 0.1% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

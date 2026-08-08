# JOURNAL ENGLE — NUAGE_PROD_4H

- Généré: `2026-07-22T11:42:26Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-22T06:41:50Z`
- CSV: `NUAGE_PROD_4H_BETA_X5.csv` · `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 984 | 70.0% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 251 | 17.9% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 171 | 12.2% | 66 | +0.1266 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.4223 · σ=1.2059 · n=1406

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 1406 | 66 | 1340 | +0.1266 | `2026-07-22T06:42:00Z` → `2026-07-22T10:41:50Z` |
| ALPHA | 1529 | 9 | 1520 | -10.5614 | `2026-07-22T06:42:01Z` → `2026-07-22T10:41:51Z` |
| **TOTAL** | | 75 | | **-10.4348** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 862 | 64.3% |
| `radar_block` | 205 | 15.3% |
| `wall_not_collapsed` | 173 | 12.9% |
| `vacuum_filter` | 98 | 7.3% |
| `tactic_mismatch` | 2 | 0.1% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 937 | 61.6% |
| `wall_not_collapsed` | 197 | 13.0% |
| `radar_block` | 193 | 12.7% |
| `vacuum_filter` | 125 | 8.2% |
| `tension_stale` | 66 | 4.3% |
| `tactic_mismatch` | 2 | 0.1% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

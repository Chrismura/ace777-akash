# JOURNAL ENGLE — NUAGE_PROD_4H

- Généré: `2026-07-20T04:47:01Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-19T19:52:13Z`
- CSV: `NUAGE_PROD_4H_BETA_X5.csv` · `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 932 | 66.6% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 267 | 19.1% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 200 | 14.3% | 179 | -0.4235 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.5238 · σ=1.4434 · n=1399

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 1399 | 179 | 1220 | -0.4235 | `2026-07-19T19:52:29Z` → `2026-07-19T23:52:13Z` |
| ALPHA | 1556 | 3 | 1553 | +8.9146 | `2026-07-19T19:52:35Z` → `2026-07-19T23:52:19Z` |
| **TOTAL** | | 182 | | **+8.4911** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 871 | 71.4% |
| `wall_not_collapsed` | 189 | 15.5% |
| `radar_block` | 139 | 11.4% |
| `tactic_mismatch` | 15 | 1.2% |
| `stase_ecoute` | 6 | 0.5% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 826 | 53.2% |
| `radar_block` | 326 | 21.0% |
| `wall_not_collapsed` | 180 | 11.6% |
| `duo_wait` | 145 | 9.3% |
| `tension_stale` | 66 | 4.2% |
| `tactic_mismatch` | 10 | 0.6% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

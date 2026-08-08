# JOURNAL ENGLE — NUAGE_PROD_4H

- Généré: `2026-07-31T18:19:29Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-31T14:07:12Z`
- CSV: `NUAGE_PROD_4H_BETA_X5.csv` · `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 757 | 65.3% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 205 | 17.7% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 198 | 17.1% | 161 | -5.9965 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.6541 · σ=1.7318 · n=1160

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 1160 | 161 | 999 | -5.9965 | `2026-07-31T14:07:21Z` → `2026-07-31T18:07:10Z` |
| ALPHA | 1329 | 6 | 1323 | +2.8561 | `2026-07-31T14:07:24Z` → `2026-07-31T18:07:07Z` |
| **TOTAL** | | 167 | | **-3.1405** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 612 | 61.3% |
| `radar_block` | 196 | 19.6% |
| `wall_not_collapsed` | 141 | 14.1% |
| `stase_ecoute` | 25 | 2.5% |
| `tactic_mismatch` | 25 | 2.5% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 715 | 54.0% |
| `radar_block` | 202 | 15.3% |
| `wall_not_collapsed` | 165 | 12.5% |
| `duo_wait` | 112 | 8.5% |
| `tension_stale` | 74 | 5.6% |
| `tactic_mismatch` | 50 | 3.8% |
| `stase_ecoute` | 5 | 0.4% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

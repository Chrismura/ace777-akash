# JOURNAL ENGLE — NUAGE_PROD_4H

- Généré: `2026-07-19T12:36:09Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-19T08:28:07Z`
- CSV: `NUAGE_PROD_4H_BETA_X5.csv` · `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 1003 | 70.1% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 279 | 19.5% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 148 | 10.3% | 146 | +2.8032 |

- Courant (proxy): **TRANSITOIRE (bruit retail)** · μ=0.4120 · σ=1.2614 · n=1430

## Posture recommandée (conseil — pas appliquée)

- Code: `WATCH`
- Bruit retail — observer ; pas de knobs B3.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 1430 | 146 | 1284 | +2.8032 | `2026-07-19T08:28:26Z` → `2026-07-19T12:28:07Z` |
| ALPHA | 1534 | 5 | 1529 | +3.1706 | `2026-07-19T08:28:28Z` → `2026-07-19T12:28:06Z` |
| **TOTAL** | | 151 | | **+5.9738** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 934 | 72.7% |
| `wall_not_collapsed` | 203 | 15.8% |
| `radar_block` | 136 | 10.6% |
| `stase_ecoute` | 8 | 0.6% |
| `tactic_mismatch` | 3 | 0.2% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 942 | 61.6% |
| `wall_not_collapsed` | 208 | 13.6% |
| `radar_block` | 206 | 13.5% |
| `duo_wait` | 118 | 7.7% |
| `tension_stale` | 45 | 2.9% |
| `tactic_mismatch` | 10 | 0.7% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

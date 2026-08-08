# JOURNAL ENGLE — NUAGE_PROD_4H

- Généré: `2026-07-19T13:53:19Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-19T13:06:11Z`
- CSV: `NUAGE_PROD_4H_BETA_X5.csv` · `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 111 | 68.5% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 31 | 19.1% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 20 | 12.3% | 20 | +0.7054 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.4345 · σ=1.1567 · n=162

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 162 | 20 | 142 | +0.7054 | `2026-07-19T13:06:23Z` → `2026-07-19T13:36:39Z` |
| ALPHA | 173 | 5 | 168 | +1.5079 | `2026-07-19T13:06:31Z` → `2026-07-19T13:51:59Z` |
| **TOTAL** | | 25 | | **+2.2133** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 102 | 71.8% |
| `wall_not_collapsed` | 24 | 16.9% |
| `radar_block` | 15 | 10.6% |
| `tactic_mismatch` | 1 | 0.7% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 94 | 56.0% |
| `radar_block` | 31 | 18.5% |
| `wall_not_collapsed` | 20 | 11.9% |
| `duo_wait` | 13 | 7.7% |
| `gap_guard_pause` | 10 | 6.0% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

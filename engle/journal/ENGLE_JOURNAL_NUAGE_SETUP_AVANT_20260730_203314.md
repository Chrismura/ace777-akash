# JOURNAL ENGLE — NUAGE_SETUP_AVANT

- Généré: `2026-07-30T20:33:14Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-30T18:42:10Z`
- CSV: `NUAGE_SETUP_AVANT_BETA_X5.csv` · `NUAGE_SETUP_AVANT_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 244 | 74.8% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 49 | 15.0% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 33 | 10.1% | 33 | -0.5433 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.4084 · σ=1.4418 · n=326

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 326 | 33 | 293 | -0.5433 | `2026-07-30T18:42:20Z` → `2026-07-30T19:38:57Z` |
| ALPHA | 357 | 1 | 356 | -0.0804 | `2026-07-30T18:42:22Z` → `2026-07-30T19:38:25Z` |
| **TOTAL** | | 34 | | **-0.6237** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 233 | 79.5% |
| `wall_not_collapsed` | 35 | 11.9% |
| `radar_block` | 24 | 8.2% |
| `tactic_mismatch` | 1 | 0.3% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 262 | 73.6% |
| `wall_not_collapsed` | 31 | 8.7% |
| `radar_block` | 25 | 7.0% |
| `tension_stale` | 20 | 5.6% |
| `duo_wait` | 16 | 4.5% |
| `tactic_mismatch` | 2 | 0.6% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

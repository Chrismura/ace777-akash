# JOURNAL ENGLE — NUAGE_PROD_4H

- Généré: `2026-07-19T19:48:57Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-19T17:10:55Z`
- CSV: `NUAGE_PROD_4H_BETA_X5.csv` · `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 677 | 73.2% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 138 | 14.9% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 110 | 11.9% | 108 | +0.6500 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.3942 · σ=1.0796 · n=925

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 925 | 108 | 817 | +0.6500 | `2026-07-19T17:11:20Z` → `2026-07-19T19:48:40Z` |
| ALPHA | 1031 | 1 | 1030 | -6.2972 | `2026-07-19T17:11:08Z` → `2026-07-19T19:48:42Z` |
| **TOTAL** | | 109 | | **-5.6472** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 633 | 77.5% |
| `wall_not_collapsed` | 104 | 12.7% |
| `radar_block` | 73 | 8.9% |
| `tactic_mismatch` | 6 | 0.7% |
| `stase_ecoute` | 1 | 0.1% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 649 | 63.0% |
| `radar_block` | 144 | 14.0% |
| `wall_not_collapsed` | 112 | 10.9% |
| `duo_wait` | 88 | 8.5% |
| `tension_stale` | 29 | 2.8% |
| `tactic_mismatch` | 8 | 0.8% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

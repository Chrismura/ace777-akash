# JOURNAL ENGLE — NUAGE_PROD_4H

- Généré: `2026-07-20T16:56:59Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-20T13:34:23Z`
- CSV: `NUAGE_PROD_4H_BETA_X5.csv` · `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 336 | 58.3% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 86 | 14.9% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 154 | 26.7% | 133 | +1.2110 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.9683 · σ=1.9331 · n=576

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 576 | 133 | 443 | +1.2110 | `2026-07-20T13:34:34Z` → `2026-07-20T15:24:38Z` |
| ALPHA | 705 | 9 | 696 | +4.2744 | `2026-07-20T13:34:38Z` → `2026-07-20T15:25:23Z` |
| **TOTAL** | | 142 | | **+5.4854** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 290 | 65.5% |
| `radar_block` | 77 | 17.4% |
| `wall_not_collapsed` | 59 | 13.3% |
| `tactic_mismatch` | 12 | 2.7% |
| `stase_ecoute` | 5 | 1.1% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 281 | 40.4% |
| `radar_block` | 219 | 31.5% |
| `duo_wait` | 91 | 13.1% |
| `wall_not_collapsed` | 55 | 7.9% |
| `tension_stale` | 40 | 5.7% |
| `tactic_mismatch` | 10 | 1.4% |

## Lecture courte (marché calme)

1. Part de **CLUSTER** non négligeable — candidature future B3 (un knobs).
2. Comparer fills ALPHA vs runs calmes avant tout GO knobs.
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

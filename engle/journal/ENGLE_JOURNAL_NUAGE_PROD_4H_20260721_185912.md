# JOURNAL ENGLE — NUAGE_PROD_4H

- Généré: `2026-07-21T18:59:12Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-21T14:50:20Z`
- CSV: `NUAGE_PROD_4H_BETA_X5.csv` · `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 843 | 62.8% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 249 | 18.6% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 250 | 18.6% | 94 | -0.3582 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.6316 · σ=1.4901 · n=1342

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 1342 | 94 | 1248 | -0.3582 | `2026-07-21T14:50:32Z` → `2026-07-21T18:50:05Z` |
| ALPHA | 1583 | 10 | 1573 | +11.4667 | `2026-07-21T14:50:35Z` → `2026-07-21T18:50:26Z` |
| **TOTAL** | | 104 | | **+11.1085** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 761 | 61.0% |
| `wall_not_collapsed` | 177 | 14.2% |
| `radar_block` | 175 | 14.0% |
| `vacuum_filter` | 127 | 10.2% |
| `tactic_mismatch` | 8 | 0.6% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 866 | 55.1% |
| `wall_not_collapsed` | 217 | 13.8% |
| `radar_block` | 193 | 12.3% |
| `vacuum_filter` | 154 | 9.8% |
| `tension_stale` | 130 | 8.3% |
| `tactic_mismatch` | 13 | 0.8% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

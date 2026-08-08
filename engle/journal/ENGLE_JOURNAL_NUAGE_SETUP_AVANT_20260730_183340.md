# JOURNAL ENGLE — NUAGE_SETUP_AVANT

- Généré: `2026-07-30T18:33:40Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-30T15:58:15Z`
- CSV: `NUAGE_SETUP_AVANT_BETA_X5.csv` · `NUAGE_SETUP_AVANT_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 527 | 72.6% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 106 | 14.6% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 93 | 12.8% | 26 | +0.2552 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.4220 · σ=1.1496 · n=726

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 726 | 26 | 700 | +0.2552 | `2026-07-30T15:58:26Z` → `2026-07-30T17:58:14Z` |
| ALPHA | 773 | 3 | 770 | -1.5139 | `2026-07-30T15:58:28Z` → `2026-07-30T17:58:18Z` |
| **TOTAL** | | 29 | | **-1.2587** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 499 | 71.3% |
| `wall_not_collapsed` | 79 | 11.3% |
| `vacuum_filter` | 65 | 9.3% |
| `radar_block` | 53 | 7.6% |
| `tactic_mismatch` | 4 | 0.6% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 513 | 66.6% |
| `wall_not_collapsed` | 89 | 11.6% |
| `vacuum_filter` | 71 | 9.2% |
| `radar_block` | 70 | 9.1% |
| `tension_stale` | 23 | 3.0% |
| `tactic_mismatch` | 4 | 0.5% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

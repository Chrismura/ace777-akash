# JOURNAL ENGLE — MASTER_BASE_V8_6_FORTRESS_1H30

- Généré: `2026-09-07T22:30:18Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-09-07T21:00:13Z`
- CSV: `MASTER_BASE_V8_6_FORTRESS_1H30_BETA_X5.csv` · `MASTER_BASE_V8_6_FORTRESS_1H30_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 457 | 87.2% | 18 | +2.1619 |
| TRANSITOIRE (bruit retail) | 64 | 12.2% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 3 | 0.6% | 0 | +0.0000 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.0616 · σ=0.2301 · n=524

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 524 | 18 | 499 | +2.1619 | `2026-09-07T21:00:23Z` → `2026-09-07T22:30:16Z` |
| ALPHA | 837 | 6 | 831 | -3.0685 | `2026-09-07T21:00:23Z` → `2026-09-07T22:30:16Z` |
| **TOTAL** | | 24 | | **-0.9066** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `regime_gate` | 430 | 86.2% |
| `wall_not_collapsed` | 44 | 8.8% |
| `radar_block` | 23 | 4.6% |
| `tactic_mismatch` | 2 | 0.4% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `regime_gate` | 702 | 84.5% |
| `wall_not_collapsed` | 64 | 7.7% |
| `duo_wait` | 39 | 4.7% |
| `radar_block` | 25 | 3.0% |
| `tactic_mismatch` | 1 | 0.1% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

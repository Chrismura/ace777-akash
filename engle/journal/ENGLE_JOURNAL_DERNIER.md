# JOURNAL ENGLE — ACE_RADAR_ALIGNED_V3_15M

- Généré: `2026-09-01T23:25:55Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-09-01T23:10:50Z`
- CSV: `ACE_RADAR_ALIGNED_V3_15M_BETA_X5.csv` · `ACE_RADAR_ALIGNED_V3_15M_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 21 | 72.4% | 4 | +0.7205 |
| TRANSITOIRE (bruit retail) | 8 | 27.6% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 0 | 0.0% | 0 | +0.0000 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.1265 · σ=0.2360 · n=29

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 29 | 4 | 25 | +0.7205 | `2026-09-01T23:13:26Z` → `2026-09-01T23:25:51Z` |
| ALPHA | 59 | 2 | 57 | -1.0718 | `2026-09-01T23:10:59Z` → `2026-09-01T23:25:52Z` |
| **TOTAL** | | 6 | | **-0.3514** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `regime_gate` | 15 | 60.0% |
| `wall_not_collapsed` | 6 | 24.0% |
| `radar_block` | 2 | 8.0% |
| `tactic_mismatch` | 2 | 8.0% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `regime_gate` | 42 | 73.7% |
| `radar_block` | 6 | 10.5% |
| `wall_not_collapsed` | 5 | 8.8% |
| `duo_wait` | 3 | 5.3% |
| `tactic_mismatch` | 1 | 1.8% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

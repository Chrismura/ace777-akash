# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-22T03:31:18Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-21T23:22:11Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 997 | 96.1% | 52 | -4.8682 |
| TRANSITOIRE (bruit retail) | 41 | 3.9% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 0 | 0.0% | 0 | +0.0000 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.0195 · σ=0.1089 · n=1038

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 1038 | 52 | 986 | -4.8682 | `2026-08-21T23:22:41Z` → `2026-08-22T03:30:52Z` |
| ALPHA | 913 | 36 | 877 | +16.1714 | `2026-08-21T23:23:10Z` → `2026-08-22T03:31:06Z` |
| **TOTAL** | | 88 | | **+11.3032** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `gap_guard_pause` | 793 | 80.4% |
| `regime_gate` | 123 | 12.5% |
| `wall_not_collapsed` | 31 | 3.1% |
| `tactic_mismatch` | 19 | 1.9% |
| `radar_block` | 10 | 1.0% |
| `stase_ecoute` | 10 | 1.0% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `gap_guard_pause` | 605 | 69.0% |
| `regime_gate` | 143 | 16.3% |
| `duo_wait` | 51 | 5.8% |
| `wall_not_collapsed` | 40 | 4.6% |
| `radar_block` | 17 | 1.9% |
| `tactic_mismatch` | 15 | 1.7% |
| `stase_ecoute` | 6 | 0.7% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

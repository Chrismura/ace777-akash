# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-21T11:01:11Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-21T10:49:48Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 53 | 91.4% | 11 | -0.3150 |
| TRANSITOIRE (bruit retail) | 5 | 8.6% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 0 | 0.0% | 0 | +0.0000 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.0220 · σ=0.0942 · n=58

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 58 | 11 | 47 | -0.3150 | `2026-08-21T10:49:56Z` → `2026-08-21T11:00:38Z` |
| ALPHA | 62 | 8 | 54 | +1.7298 | `2026-08-21T10:49:58Z` → `2026-08-21T11:00:29Z` |
| **TOTAL** | | 19 | | **+1.4148** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `regime_gate` | 40 | 85.1% |
| `radar_block` | 3 | 6.4% |
| `tactic_mismatch` | 2 | 4.3% |
| `wall_not_collapsed` | 2 | 4.3% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `regime_gate` | 44 | 81.5% |
| `wall_not_collapsed` | 5 | 9.3% |
| `radar_block` | 3 | 5.6% |
| `tactic_mismatch` | 2 | 3.7% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

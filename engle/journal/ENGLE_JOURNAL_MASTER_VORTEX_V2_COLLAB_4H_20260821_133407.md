# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-21T13:34:07Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-21T12:03:20Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 722 | 97.4% | 21 | -9.9141 |
| TRANSITOIRE (bruit retail) | 18 | 2.4% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 1 | 0.1% | 0 | +0.0000 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.0157 · σ=0.1104 · n=741

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 741 | 21 | 716 | -9.9141 | `2026-08-21T12:03:28Z` → `2026-08-21T13:34:04Z` |
| ALPHA | 619 | 11 | 604 | +8.5782 | `2026-08-21T12:03:31Z` → `2026-08-21T13:33:49Z` |
| **TOTAL** | | 32 | | **-1.3360** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `gap_guard_pause` | 624 | 87.2% |
| `regime_gate` | 69 | 9.6% |
| `wall_not_collapsed` | 14 | 2.0% |
| `radar_block` | 5 | 0.7% |
| `stase_ecoute` | 3 | 0.4% |
| `tactic_mismatch` | 1 | 0.1% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `gap_guard_pause` | 389 | 64.4% |
| `regime_gate` | 140 | 23.2% |
| `duo_wait` | 31 | 5.1% |
| `wall_not_collapsed` | 25 | 4.1% |
| `radar_block` | 10 | 1.7% |
| `tactic_mismatch` | 9 | 1.5% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-16T14:54:32Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-16T10:46:52Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 841 | 79.6% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 170 | 16.1% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 45 | 4.3% | 20 | +0.0739 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.1896 · σ=0.8781 · n=1056

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 1056 | 20 | 1036 | +0.0739 | `2026-08-16T10:47:06Z` → `2026-08-16T14:54:26Z` |
| ALPHA | 887 | 0 | 884 | +0.0000 | `2026-08-16T10:47:07Z` → `2026-08-16T14:54:11Z` |
| **TOTAL** | | 20 | | **+0.0739** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 546 | 52.7% |
| `gap_guard_pause` | 264 | 25.5% |
| `radar_block` | 110 | 10.6% |
| `wall_not_collapsed` | 91 | 8.8% |
| `price_stasis` | 25 | 2.4% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 537 | 60.7% |
| `radar_block` | 126 | 14.3% |
| `gap_guard_pause` | 83 | 9.4% |
| `wall_not_collapsed` | 75 | 8.5% |
| `duo_wait` | 59 | 6.7% |
| `tactic_mismatch` | 2 | 0.2% |
| `price_stasis` | 2 | 0.2% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

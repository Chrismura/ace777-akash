# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-16T06:03:23Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-15T21:52:47Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 1743 | 78.3% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 324 | 14.5% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 160 | 7.2% | 160 | +0.3553 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.2643 · σ=0.9205 · n=2227

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 2227 | 160 | 2066 | +0.3553 | `2026-08-15T21:53:12Z` → `2026-08-16T06:03:07Z` |
| ALPHA | 2240 | 12 | 2201 | -0.0755 | `2026-08-15T21:53:15Z` → `2026-08-16T06:03:13Z` |
| **TOTAL** | | 172 | | **+0.2798** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 1554 | 75.2% |
| `wall_not_collapsed` | 237 | 11.5% |
| `radar_block` | 184 | 8.9% |
| `gap_guard_pause` | 87 | 4.2% |
| `tactic_mismatch` | 4 | 0.2% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 1588 | 72.1% |
| `wall_not_collapsed` | 271 | 12.3% |
| `radar_block` | 203 | 9.2% |
| `duo_wait` | 137 | 6.2% |
| `tactic_mismatch` | 2 | 0.1% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

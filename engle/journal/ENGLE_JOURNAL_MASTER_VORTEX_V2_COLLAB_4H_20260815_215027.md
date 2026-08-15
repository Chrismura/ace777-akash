# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-15T21:50:27Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-15T14:05:47Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 2104 | 75.4% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 452 | 16.2% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 233 | 8.4% | 229 | +1.3640 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.4027 · σ=1.5181 · n=2789

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 2789 | 229 | 2557 | +1.3640 | `2026-08-15T14:05:57Z` → `2026-08-15T21:50:19Z` |
| ALPHA | 2891 | 36 | 2851 | +0.8073 | `2026-08-15T14:06:00Z` → `2026-08-15T21:50:00Z` |
| **TOTAL** | | 265 | | **+2.1713** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 1919 | 75.0% |
| `radar_block` | 299 | 11.7% |
| `wall_not_collapsed` | 278 | 10.9% |
| `gap_guard_pause` | 51 | 2.0% |
| `tactic_mismatch` | 5 | 0.2% |
| `stase_ecoute` | 5 | 0.2% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 2056 | 72.1% |
| `wall_not_collapsed` | 317 | 11.1% |
| `radar_block` | 263 | 9.2% |
| `duo_wait` | 206 | 7.2% |
| `tactic_mismatch` | 9 | 0.3% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

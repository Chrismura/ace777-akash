# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-13T15:45:02Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-13T12:37:04Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 915 | 73.8% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 181 | 14.6% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 143 | 11.5% | 131 | -0.0996 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.4279 · σ=1.3085 · n=1239

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 1239 | 131 | 1108 | -0.0996 | `2026-08-13T12:37:12Z` → `2026-08-13T15:45:00Z` |
| ALPHA | 64 | 0 | 64 | +0.0000 | `2026-08-13T12:37:15Z` → `2026-08-13T12:45:59Z` |
| **TOTAL** | | 131 | | **-0.0996** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 813 | 73.4% |
| `radar_block` | 144 | 13.0% |
| `wall_not_collapsed` | 121 | 10.9% |
| `gap_guard_pause` | 13 | 1.2% |
| `tactic_mismatch` | 11 | 1.0% |
| `stase_ecoute` | 6 | 0.5% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 40 | 62.5% |
| `wall_not_collapsed` | 10 | 15.6% |
| `radar_block` | 9 | 14.1% |
| `duo_wait` | 5 | 7.8% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-13T12:22:10Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-13T08:44:57Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 1355 | 85.6% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 87 | 5.5% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 141 | 8.9% | 90 | +0.5060 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.3906 · σ=1.4759 · n=1583

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 1583 | 90 | 1493 | +0.5060 | `2026-08-13T08:45:06Z` → `2026-08-13T12:22:08Z` |
| ALPHA | 185 | 0 | 185 | +0.0000 | `2026-08-13T08:45:10Z` → `2026-08-13T09:09:51Z` |
| **TOTAL** | | 90 | | **+0.5060** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 781 | 52.3% |
| `radar_block` | 649 | 43.5% |
| `wall_not_collapsed` | 44 | 2.9% |
| `tactic_mismatch` | 10 | 0.7% |
| `stase_ecoute` | 9 | 0.6% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 134 | 72.4% |
| `radar_block` | 47 | 25.4% |
| `duo_wait` | 4 | 2.2% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

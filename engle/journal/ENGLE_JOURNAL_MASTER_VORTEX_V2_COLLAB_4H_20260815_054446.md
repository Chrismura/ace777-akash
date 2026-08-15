# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-15T05:44:46Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-14T21:44:51Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 3037 | 85.1% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 327 | 9.2% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 205 | 5.7% | 205 | +2.5071 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.2109 · σ=0.9139 · n=3569

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 3569 | 205 | 3364 | +2.5071 | `2026-08-14T21:45:05Z` → `2026-08-15T05:44:44Z` |
| ALPHA | 3629 | 56 | 3573 | +8.6068 | `2026-08-14T21:45:03Z` → `2026-08-15T05:44:41Z` |
| **TOTAL** | | 261 | | **+11.1140** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 2942 | 87.5% |
| `wall_not_collapsed` | 225 | 6.7% |
| `radar_block` | 188 | 5.6% |
| `tactic_mismatch` | 6 | 0.2% |
| `stase_ecoute` | 3 | 0.1% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 2916 | 81.6% |
| `wall_not_collapsed` | 264 | 7.4% |
| `radar_block` | 208 | 5.8% |
| `duo_wait` | 173 | 4.8% |
| `tactic_mismatch` | 12 | 0.3% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

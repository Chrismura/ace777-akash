# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-21T17:48:46Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-21T13:48:42Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 1861 | 96.5% | 43 | +7.7126 |
| TRANSITOIRE (bruit retail) | 66 | 3.4% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 1 | 0.1% | 0 | +0.0000 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.0188 · σ=0.1192 · n=1928

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 1928 | 43 | 1867 | +7.7126 | `2026-08-21T13:48:53Z` → `2026-08-21T17:48:42Z` |
| ALPHA | 1713 | 28 | 1677 | +10.6060 | `2026-08-21T13:48:52Z` → `2026-08-21T17:48:43Z` |
| **TOTAL** | | 71 | | **+18.3186** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `gap_guard_pause` | 1532 | 82.1% |
| `regime_gate` | 255 | 13.7% |
| `wall_not_collapsed` | 46 | 2.5% |
| `radar_block` | 21 | 1.1% |
| `tactic_mismatch` | 8 | 0.4% |
| `stase_ecoute` | 5 | 0.3% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `gap_guard_pause` | 956 | 57.0% |
| `regime_gate` | 467 | 27.8% |
| `duo_wait` | 99 | 5.9% |
| `wall_not_collapsed` | 93 | 5.5% |
| `radar_block` | 30 | 1.8% |
| `tactic_mismatch` | 26 | 1.6% |
| `stase_ecoute` | 6 | 0.4% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

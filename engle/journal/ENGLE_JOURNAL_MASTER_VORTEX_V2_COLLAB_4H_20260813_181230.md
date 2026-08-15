# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-13T18:12:30Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-13T17:46:49Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 135 | 78.9% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 20 | 11.7% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 16 | 9.4% | 14 | +0.4746 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.3420 · σ=1.0525 · n=171

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 171 | 14 | 157 | +0.4746 | `2026-08-13T17:47:00Z` → `2026-08-13T18:12:22Z` |
| ALPHA | 147 | 4 | 143 | -12.5039 | `2026-08-13T17:47:02Z` → `2026-08-13T18:08:31Z` |
| **TOTAL** | | 18 | | **-12.0293** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 127 | 80.9% |
| `wall_not_collapsed` | 15 | 9.6% |
| `radar_block` | 15 | 9.6% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 103 | 72.0% |
| `duo_wait` | 16 | 11.2% |
| `radar_block` | 13 | 9.1% |
| `wall_not_collapsed` | 9 | 6.3% |
| `tactic_mismatch` | 2 | 1.4% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

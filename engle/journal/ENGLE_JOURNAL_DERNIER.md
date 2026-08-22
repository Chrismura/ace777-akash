# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-22T12:56:20Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-22T11:33:19Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 186 | 92.1% | 9 | -0.1959 |
| TRANSITOIRE (bruit retail) | 16 | 7.9% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 0 | 0.0% | 0 | +0.0000 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.0489 · σ=0.1792 · n=202

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 202 | 9 | 193 | -0.1959 | `2026-08-22T11:38:07Z` → `2026-08-22T12:56:02Z` |
| ALPHA | 158 | 7 | 151 | +4.6264 | `2026-08-22T11:34:06Z` → `2026-08-22T12:55:17Z` |
| **TOTAL** | | 16 | | **+4.4305** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `gap_guard_pause` | 141 | 73.1% |
| `regime_gate` | 33 | 17.1% |
| `wall_not_collapsed` | 14 | 7.3% |
| `stase_ecoute` | 3 | 1.6% |
| `radar_block` | 2 | 1.0% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `gap_guard_pause` | 117 | 77.5% |
| `regime_gate` | 22 | 14.6% |
| `wall_not_collapsed` | 6 | 4.0% |
| `radar_block` | 4 | 2.6% |
| `duo_wait` | 2 | 1.3% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

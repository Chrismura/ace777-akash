# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-17T11:40:19Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-17T07:40:11Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 789 | 66.0% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 269 | 22.5% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 138 | 11.5% | 138 | +0.2388 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.4084 · σ=1.1718 · n=1196

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 1196 | 138 | 1058 | +0.2388 | `2026-08-17T07:40:34Z` → `2026-08-17T11:40:12Z` |
| ALPHA | 1194 | 78 | 1116 | -3.0541 | `2026-08-17T07:40:25Z` → `2026-08-17T11:40:16Z` |
| **TOTAL** | | 216 | | **-2.8153** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 697 | 65.9% |
| `wall_not_collapsed` | 208 | 19.7% |
| `radar_block` | 93 | 8.8% |
| `gap_guard_pause` | 48 | 4.5% |
| `tactic_mismatch` | 9 | 0.9% |
| `stase_ecoute` | 3 | 0.3% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 737 | 66.0% |
| `wall_not_collapsed` | 186 | 16.7% |
| `radar_block` | 106 | 9.5% |
| `duo_wait` | 70 | 6.3% |
| `tactic_mismatch` | 12 | 1.1% |
| `stase_ecoute` | 5 | 0.4% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

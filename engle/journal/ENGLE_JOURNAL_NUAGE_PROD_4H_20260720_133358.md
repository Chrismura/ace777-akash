# JOURNAL ENGLE — NUAGE_PROD_4H

- Généré: `2026-07-20T13:33:58Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-20T10:27:48Z`
- CSV: `NUAGE_PROD_4H_BETA_X5.csv` · `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 481 | 67.0% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 113 | 15.7% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 124 | 17.3% | 120 | -3.2210 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.7379 · σ=1.9907 · n=718

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 718 | 120 | 598 | -3.2210 | `2026-07-20T10:28:08Z` → `2026-07-20T12:53:12Z` |
| ALPHA | 1087 | 2 | 1085 | -0.7233 | `2026-07-20T10:28:00Z` → `2026-07-20T13:33:43Z` |
| **TOTAL** | | 122 | | **-3.9443** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 441 | 73.7% |
| `wall_not_collapsed` | 83 | 13.9% |
| `radar_block` | 59 | 9.9% |
| `tactic_mismatch` | 12 | 2.0% |
| `stase_ecoute` | 3 | 0.5% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 600 | 55.3% |
| `radar_block` | 186 | 17.1% |
| `wall_not_collapsed` | 143 | 13.2% |
| `duo_wait` | 110 | 10.1% |
| `tension_stale` | 38 | 3.5% |
| `tactic_mismatch` | 8 | 0.7% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

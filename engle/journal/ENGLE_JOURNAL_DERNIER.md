# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-17T19:21:09Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-17T15:20:45Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 699 | 63.7% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 194 | 17.7% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 204 | 18.6% | 202 | +0.7720 |

- Courant (proxy): **CLUSTER (tension haute — proxy)** · μ=0.7349 · σ=1.7158 · n=1097

## Posture recommandée (conseil — pas appliquée)

- Code: `HUNT_WINDOW`
- Tension haute (proxy) — candidature future B3 gate/soft, pas encore appliqué.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 1097 | 202 | 895 | +0.7720 | `2026-08-17T15:20:56Z` → `2026-08-17T19:21:06Z` |
| ALPHA | 1171 | 102 | 1069 | -5.2797 | `2026-08-17T15:20:58Z` → `2026-08-17T19:20:52Z` |
| **TOTAL** | | 304 | | **-4.5077** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 632 | 70.6% |
| `wall_not_collapsed` | 159 | 17.8% |
| `radar_block` | 80 | 8.9% |
| `tactic_mismatch` | 14 | 1.6% |
| `stase_ecoute` | 10 | 1.1% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 651 | 60.9% |
| `wall_not_collapsed` | 167 | 15.6% |
| `duo_wait` | 116 | 10.9% |
| `radar_block` | 109 | 10.2% |
| `tactic_mismatch` | 19 | 1.8% |
| `stase_ecoute` | 7 | 0.7% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

# JOURNAL ENGLE — MASTER_VORTEX_V2_COLLAB_4H

- Généré: `2026-08-22T07:32:05Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-22T03:31:42Z`
- CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` · `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 562 | 90.6% | 23 | +5.9114 |
| TRANSITOIRE (bruit retail) | 45 | 7.3% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 13 | 2.1% | 0 | +0.0000 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.1801 · σ=1.1187 · n=620

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 620 | 23 | 597 | +5.9114 | `2026-08-22T03:32:20Z` → `2026-08-22T07:31:42Z` |
| ALPHA | 534 | 15 | 519 | -8.4095 | `2026-08-22T03:32:25Z` → `2026-08-22T07:31:56Z` |
| **TOTAL** | | 38 | | **-2.4981** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `gap_guard_pause` | 429 | 71.9% |
| `regime_gate` | 86 | 14.4% |
| `radar_block` | 33 | 5.5% |
| `wall_not_collapsed` | 25 | 4.2% |
| `tactic_mismatch` | 16 | 2.7% |
| `stase_ecoute` | 8 | 1.3% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `gap_guard_pause` | 282 | 54.3% |
| `regime_gate` | 108 | 20.8% |
| `radar_block` | 44 | 8.5% |
| `wall_not_collapsed` | 36 | 6.9% |
| `duo_wait` | 33 | 6.4% |
| `tactic_mismatch` | 9 | 1.7% |
| `stase_ecoute` | 7 | 1.3% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

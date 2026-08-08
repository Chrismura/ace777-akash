# JOURNAL ENGLE — VALIDATION_VOIE_A_PACK_A_P2

- Généré: `2026-07-30T15:56:07Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-30T06:22:17Z`
- CSV: `VALIDATION_VOIE_A_PACK_A_P2_BETA_X5.csv` · `VALIDATION_VOIE_A_PACK_A_P2_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 958 | 65.8% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 282 | 19.4% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 215 | 14.8% | 202 | +1.6224 |

- Courant (proxy): **TRANSITOIRE (bruit retail)** · μ=0.5267 · σ=1.3229 · n=1455

## Posture recommandée (conseil — pas appliquée)

- Code: `WATCH`
- Bruit retail — observer ; pas de knobs B3.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 1455 | 202 | 1253 | +1.6224 | `2026-07-30T06:22:26Z` → `2026-07-30T10:22:18Z` |
| ALPHA | 547 | 10 | 535 | -0.8128 | `2026-07-30T06:22:46Z` → `2026-07-30T10:22:24Z` |
| **TOTAL** | | 212 | | **+0.8096** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 893 | 71.3% |
| `wall_not_collapsed` | 190 | 15.2% |
| `radar_block` | 157 | 12.5% |
| `tactic_mismatch` | 13 | 1.0% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 334 | 62.4% |
| `duo_wait` | 71 | 13.3% |
| `wall_not_collapsed` | 69 | 12.9% |
| `radar_block` | 57 | 10.7% |
| `tactic_mismatch` | 4 | 0.7% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

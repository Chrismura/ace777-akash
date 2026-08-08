# JOURNAL ENGLE — VALIDATION_VOIE_A_PACK_A

- Généré: `2026-07-29T20:02:35Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-29T15:12:48Z`
- CSV: `VALIDATION_VOIE_A_PACK_A_BETA_X5.csv` · `VALIDATION_VOIE_A_PACK_A_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 830 | 61.0% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 218 | 16.0% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 313 | 23.0% | 253 | +1.5526 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.8973 · σ=1.9067 · n=1361

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 1361 | 253 | 1108 | +1.5526 | `2026-07-29T15:12:58Z` → `2026-07-29T20:02:33Z` |
| ALPHA | 534 | 28 | 506 | +18.2349 | `2026-07-29T15:13:18Z` → `2026-07-29T20:01:34Z` |
| **TOTAL** | | 281 | | **+19.7876** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 702 | 63.4% |
| `radar_block` | 248 | 22.4% |
| `wall_not_collapsed` | 141 | 12.7% |
| `tactic_mismatch` | 17 | 1.5% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 272 | 53.8% |
| `radar_block` | 101 | 20.0% |
| `duo_wait` | 80 | 15.8% |
| `wall_not_collapsed` | 50 | 9.9% |
| `tactic_mismatch` | 3 | 0.6% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

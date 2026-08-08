# JOURNAL ENGLE — VALIDATION_VOIE_A_PACK_B

- Généré: `2026-07-30T00:13:39Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-29T20:13:34Z`
- CSV: `VALIDATION_VOIE_A_PACK_B_BETA_X5.csv` · `VALIDATION_VOIE_A_PACK_B_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 1024 | 67.3% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 376 | 24.7% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 121 | 8.0% | 110 | +0.0122 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.2583 · σ=0.6206 · n=1521

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 1521 | 110 | 1411 | +0.0122 | `2026-07-29T20:13:44Z` → `2026-07-30T00:13:36Z` |
| ALPHA | 544 | 13 | 531 | -19.1938 | `2026-07-29T20:14:08Z` → `2026-07-30T00:13:16Z` |
| **TOTAL** | | 123 | | **-19.1817** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 956 | 67.8% |
| `wall_not_collapsed` | 253 | 17.9% |
| `radar_block` | 195 | 13.8% |
| `tactic_mismatch` | 7 | 0.5% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 345 | 65.0% |
| `wall_not_collapsed` | 80 | 15.1% |
| `radar_block` | 76 | 14.3% |
| `duo_wait` | 27 | 5.1% |
| `tactic_mismatch` | 3 | 0.6% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

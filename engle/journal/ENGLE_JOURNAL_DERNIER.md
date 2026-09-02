# JOURNAL ENGLE — ACE_RADAR_ALIGNED_V4_60M

- Généré: `2026-09-02T01:04:32Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-09-02T00:04:23Z`
- CSV: `ACE_RADAR_ALIGNED_V4_60M_BETA_X5.csv` · `ACE_RADAR_ALIGNED_V4_60M_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 261 | 75.0% | 9 | -5.8093 |
| TRANSITOIRE (bruit retail) | 50 | 14.4% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 37 | 10.6% | 0 | +0.0000 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.4222 · σ=1.2265 · n=348

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 348 | 9 | 339 | -5.8093 | `2026-09-02T00:04:30Z` → `2026-09-02T01:04:25Z` |
| ALPHA | 371 | 5 | 366 | -3.3131 | `2026-09-02T00:04:33Z` → `2026-09-02T01:04:28Z` |
| **TOTAL** | | 14 | | **-9.1224** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `regime_gate` | 252 | 74.3% |
| `radar_block` | 81 | 23.9% |
| `wall_not_collapsed` | 6 | 1.8% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `regime_gate` | 266 | 72.7% |
| `radar_block` | 85 | 23.2% |
| `duo_wait` | 9 | 2.5% |
| `wall_not_collapsed` | 5 | 1.4% |
| `tactic_mismatch` | 1 | 0.3% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

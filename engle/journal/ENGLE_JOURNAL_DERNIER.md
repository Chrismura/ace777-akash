# JOURNAL ENGLE — ACE_RADAR_ALIGNED_V1_15M

- Généré: `2026-09-01T19:56:24Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-09-01T19:41:19Z`
- CSV: `ACE_RADAR_ALIGNED_V1_15M_BETA_X5.csv` · `ACE_RADAR_ALIGNED_V1_15M_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 38 | 80.9% | 5 | -0.5983 |
| TRANSITOIRE (bruit retail) | 7 | 14.9% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 2 | 4.3% | 0 | +0.0000 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.1308 · σ=0.3381 · n=47

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 47 | 5 | 41 | -0.5983 | `2026-09-01T19:41:26Z` → `2026-09-01T19:56:21Z` |
| ALPHA | 56 | 4 | 52 | +2.4125 | `2026-09-01T19:41:28Z` → `2026-09-01T19:56:21Z` |
| **TOTAL** | | 9 | | **+1.8142** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `regime_gate` | 32 | 78.0% |
| `radar_block` | 8 | 19.5% |
| `wall_not_collapsed` | 1 | 2.4% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `regime_gate` | 38 | 73.1% |
| `wall_not_collapsed` | 5 | 9.6% |
| `radar_block` | 5 | 9.6% |
| `duo_wait` | 4 | 7.7% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

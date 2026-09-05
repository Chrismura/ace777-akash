# JOURNAL ENGLE — ACE_RADAR_ALIGNED_V3_15M

- Généré: `2026-09-01T23:09:06Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-09-01T22:59:57Z`
- CSV: `ACE_RADAR_ALIGNED_V3_15M_BETA_X5.csv` · `ACE_RADAR_ALIGNED_V3_15M_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 8 | 88.9% | 2 | -0.5472 |
| TRANSITOIRE (bruit retail) | 1 | 11.1% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 0 | 0.0% | 0 | +0.0000 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.0193 · σ=0.0580 · n=9

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 9 | 2 | 7 | -0.5472 | `2026-09-01T23:00:04Z` → `2026-09-01T23:07:44Z` |
| ALPHA | 22 | 1 | 21 | +0.4263 | `2026-09-01T23:00:10Z` → `2026-09-01T23:09:02Z` |
| **TOTAL** | | 3 | | **-0.1209** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `regime_gate` | 6 | 85.7% |
| `radar_block` | 1 | 14.3% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `regime_gate` | 13 | 61.9% |
| `duo_wait` | 5 | 23.8% |
| `wall_not_collapsed` | 2 | 9.5% |
| `radar_block` | 1 | 4.8% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

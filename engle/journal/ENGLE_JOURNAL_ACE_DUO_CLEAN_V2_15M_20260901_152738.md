# JOURNAL ENGLE — ACE_DUO_CLEAN_V2_15M

- Généré: `2026-09-01T15:27:38Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-09-01T15:12:33Z`
- CSV: `ACE_DUO_CLEAN_V2_15M_BETA_X5.csv` · `ACE_DUO_CLEAN_V2_15M_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 39 | 73.6% | 4 | -2.3104 |
| TRANSITOIRE (bruit retail) | 8 | 15.1% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 6 | 11.3% | 0 | +0.0000 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.3343 · σ=0.9292 · n=53

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 53 | 4 | 49 | -2.3104 | `2026-09-01T15:12:40Z` → `2026-09-01T15:27:32Z` |
| ALPHA | 88 | 3 | 85 | +3.0424 | `2026-09-01T15:12:42Z` → `2026-09-01T15:27:36Z` |
| **TOTAL** | | 7 | | **+0.7320** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `regime_gate` | 35 | 71.4% |
| `radar_block` | 14 | 28.6% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `regime_gate` | 55 | 64.7% |
| `radar_block` | 27 | 31.8% |
| `duo_wait` | 1 | 1.2% |
| `tactic_mismatch` | 1 | 1.2% |
| `wall_not_collapsed` | 1 | 1.2% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

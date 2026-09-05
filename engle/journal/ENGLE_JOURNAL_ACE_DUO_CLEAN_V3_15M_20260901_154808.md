# JOURNAL ENGLE — ACE_DUO_CLEAN_V3_15M

- Généré: `2026-09-01T15:48:08Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-09-01T15:33:00Z`
- CSV: `ACE_DUO_CLEAN_V3_15M_BETA_X5.csv` · `ACE_DUO_CLEAN_V3_15M_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 75 | 66.4% | 3 | -2.0627 |
| TRANSITOIRE (bruit retail) | 28 | 24.8% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 10 | 8.8% | 0 | +0.0000 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.3783 · σ=1.3215 · n=113

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 113 | 3 | 110 | -2.0627 | `2026-09-01T15:33:07Z` → `2026-09-01T15:48:03Z` |
| ALPHA | 98 | 3 | 95 | -1.8046 | `2026-09-01T15:33:10Z` → `2026-09-01T15:48:05Z` |
| **TOTAL** | | 6 | | **-3.8672** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `regime_gate` | 72 | 65.5% |
| `radar_block` | 34 | 30.9% |
| `wall_not_collapsed` | 4 | 3.6% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `regime_gate` | 54 | 56.8% |
| `radar_block` | 32 | 33.7% |
| `wall_not_collapsed` | 6 | 6.3% |
| `duo_wait` | 2 | 2.1% |
| `tactic_mismatch` | 1 | 1.1% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

# JOURNAL ENGLE — ACE_DUO_CLEAN_V4_15M

- Généré: `2026-09-01T16:17:19Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-09-01T16:02:10Z`
- CSV: `ACE_DUO_CLEAN_V4_15M_BETA_X5.csv` · `ACE_DUO_CLEAN_V4_15M_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 63 | 59.4% | 2 | -4.6029 |
| TRANSITOIRE (bruit retail) | 19 | 17.9% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 24 | 22.6% | 0 | +0.0000 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.6318 · σ=1.3688 · n=106

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 106 | 2 | 104 | -4.6029 | `2026-09-01T16:02:18Z` → `2026-09-01T16:17:17Z` |
| ALPHA | 125 | 1 | 124 | +0.6228 | `2026-09-01T16:02:19Z` → `2026-09-01T16:17:10Z` |
| **TOTAL** | | 3 | | **-3.9801** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `regime_gate` | 60 | 57.7% |
| `radar_block` | 42 | 40.4% |
| `tactic_mismatch` | 1 | 1.0% |
| `wall_not_collapsed` | 1 | 1.0% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `regime_gate` | 75 | 60.5% |
| `radar_block` | 41 | 33.1% |
| `wall_not_collapsed` | 5 | 4.0% |
| `duo_wait` | 2 | 1.6% |
| `tactic_mismatch` | 1 | 0.8% |

## Lecture courte (marché calme)

1. Régime mixte — journaliser encore 1–2 runs 4h avant B3.
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

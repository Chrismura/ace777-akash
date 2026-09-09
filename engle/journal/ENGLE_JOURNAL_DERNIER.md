# JOURNAL ENGLE — MASTER_BASE_V8_6_FORTRESS_8H20

- Généré: `2026-09-09T17:19:16Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-09-09T08:59:11Z`
- CSV: `MASTER_BASE_V8_6_FORTRESS_8H20_BETA_X5.csv` · `MASTER_BASE_V8_6_FORTRESS_8H20_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

*Pas assez de cycles BETA pour IRM.*

## Posture recommandée (conseil — pas appliquée)

- Code: `WATCH`
- Bruit retail — observer ; pas de knobs B3.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 0 | 0 | 0 | +0.0000 | — |
| ALPHA | 5612 | 0 | 5612 | +0.0000 | `2026-09-09T08:59:18Z` → `2026-09-09T17:19:14Z` |
| **TOTAL** | | 0 | | **+0.0000** | |

## SKIP BETA (top)

*Aucun SKIP classé.*

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `regime_gate` | 4242 | 75.6% |
| `duo_wait` | 539 | 9.6% |
| `wall_not_collapsed` | 415 | 7.4% |
| `radar_block` | 372 | 6.6% |
| `tactic_mismatch` | 44 | 0.8% |

## Lecture courte (marché calme)

1. Régime mixte — journaliser encore 1–2 runs 4h avant B3.
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

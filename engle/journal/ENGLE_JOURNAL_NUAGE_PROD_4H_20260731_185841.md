# JOURNAL ENGLE — NUAGE_PROD_4H

- Généré: `2026-07-31T18:58:41Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-31T18:38:18Z`
- CSV: `NUAGE_PROD_4H_BETA_X5.csv` · `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
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
| ALPHA | 44 | 0 | 44 | +0.0000 | `2026-07-31T18:38:31Z` → `2026-07-31T18:45:03Z` |
| **TOTAL** | | 0 | | **+0.0000** | |

## SKIP BETA (top)

*Aucun SKIP classé.*

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 31 | 70.5% |
| `radar_block` | 7 | 15.9% |
| `wall_not_collapsed` | 3 | 6.8% |
| `duo_wait` | 3 | 6.8% |

## Lecture courte (marché calme)

1. Régime mixte — journaliser encore 1–2 runs 4h avant B3.
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

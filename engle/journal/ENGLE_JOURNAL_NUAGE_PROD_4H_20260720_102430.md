# JOURNAL ENGLE — NUAGE_PROD_4H

- Généré: `2026-07-20T10:24:30Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-20T08:07:42Z`
- CSV: `NUAGE_PROD_4H_BETA_X5.csv` · `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 439 | 69.1% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 98 | 15.4% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 98 | 15.4% | 84 | +0.4063 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.6047 · σ=1.5819 · n=635

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 635 | 84 | 551 | +0.4063 | `2026-07-20T08:07:55Z` → `2026-07-20T10:09:17Z` |
| ALPHA | 753 | 4 | 749 | +8.2475 | `2026-07-20T08:07:56Z` → `2026-07-20T10:18:37Z` |
| **TOTAL** | | 88 | | **+8.6537** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 351 | 63.7% |
| `radar_block` | 111 | 20.1% |
| `wall_not_collapsed` | 78 | 14.2% |
| `tactic_mismatch` | 8 | 1.5% |
| `stase_ecoute` | 3 | 0.5% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 387 | 51.7% |
| `radar_block` | 196 | 26.2% |
| `wall_not_collapsed` | 78 | 10.4% |
| `duo_wait` | 54 | 7.2% |
| `tension_stale` | 28 | 3.7% |
| `tactic_mismatch` | 6 | 0.8% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

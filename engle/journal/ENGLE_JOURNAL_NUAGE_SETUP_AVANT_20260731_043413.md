# JOURNAL ENGLE — NUAGE_SETUP_AVANT

- Généré: `2026-07-31T04:34:13Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-30T22:13:19Z`
- CSV: `NUAGE_SETUP_AVANT_BETA_X5.csv` · `NUAGE_SETUP_AVANT_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 583 | 76.6% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 112 | 14.7% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 66 | 8.7% | 62 | +2.1944 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.3010 · σ=1.0063 · n=761

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 761 | 62 | 699 | +2.1944 | `2026-07-30T22:13:30Z` → `2026-07-31T00:13:17Z` |
| ALPHA | 799 | 1 | 798 | +0.0000 | `2026-07-30T22:13:32Z` → `2026-07-31T00:13:26Z` |
| **TOTAL** | | 63 | | **+2.1944** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 546 | 78.1% |
| `wall_not_collapsed` | 79 | 11.3% |
| `radar_block` | 67 | 9.6% |
| `tactic_mismatch` | 4 | 0.6% |
| `stase_ecoute` | 3 | 0.4% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 539 | 67.5% |
| `wall_not_collapsed` | 86 | 10.8% |
| `radar_block` | 77 | 9.6% |
| `duo_wait` | 76 | 9.5% |
| `tension_stale` | 17 | 2.1% |
| `tactic_mismatch` | 3 | 0.4% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

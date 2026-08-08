# JOURNAL ENGLE — NUAGE_SETUP_AVANT

- Généré: `2026-07-30T22:11:40Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-07-30T20:43:30Z`
- CSV: `NUAGE_SETUP_AVANT_BETA_X5.csv` · `NUAGE_SETUP_AVANT_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 149 | 61.8% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 44 | 18.3% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 48 | 19.9% | 48 | +1.4740 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.7629 · σ=2.0886 · n=241

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 241 | 48 | 193 | +1.4740 | `2026-07-30T20:43:39Z` → `2026-07-30T21:36:35Z` |
| ALPHA | 299 | 2 | 297 | -2.7554 | `2026-07-30T20:43:43Z` → `2026-07-30T21:36:35Z` |
| **TOTAL** | | 50 | | **-1.2814** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 142 | 73.6% |
| `wall_not_collapsed` | 34 | 17.6% |
| `radar_block` | 14 | 7.3% |
| `stase_ecoute` | 3 | 1.6% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 182 | 61.3% |
| `wall_not_collapsed` | 51 | 17.2% |
| `duo_wait` | 36 | 12.1% |
| `tension_stale` | 14 | 4.7% |
| `radar_block` | 10 | 3.4% |
| `tactic_mismatch` | 3 | 1.0% |
| `stase_ecoute` | 1 | 0.3% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

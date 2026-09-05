# JOURNAL ENGLE — ACE_DUO_CLEAN_V1_15M

- Généré: `2026-09-01T14:25:44Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-09-01T14:10:33Z`
- CSV: `ACE_DUO_CLEAN_V1_15M_BETA_X5.csv` · `ACE_DUO_CLEAN_V1_15M_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 65 | 61.3% | 2 | -2.9614 |
| TRANSITOIRE (bruit retail) | 23 | 21.7% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 18 | 17.0% | 0 | +0.0000 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=1.1291 · σ=2.9647 · n=106

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 106 | 2 | 104 | -2.9614 | `2026-09-01T14:10:40Z` → `2026-09-01T14:25:31Z` |
| ALPHA | 121 | 0 | 121 | +0.0000 | `2026-09-01T14:10:42Z` → `2026-09-01T14:25:42Z` |
| **TOTAL** | | 2 | | **-2.9614** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `regime_gate` | 61 | 58.7% |
| `radar_block` | 37 | 35.6% |
| `wall_not_collapsed` | 4 | 3.8% |
| `tactic_mismatch` | 2 | 1.9% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `regime_gate` | 74 | 61.2% |
| `radar_block` | 33 | 27.3% |
| `wall_not_collapsed` | 7 | 5.8% |
| `duo_wait` | 5 | 4.1% |
| `tactic_mismatch` | 2 | 1.7% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

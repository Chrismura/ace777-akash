# JOURNAL ENGLE — MASTER_BASE_V8_6_FORTRESS_6H00

- Généré: `2026-09-08T03:13:58Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-09-07T23:36:39Z`
- CSV: `MASTER_BASE_V8_6_FORTRESS_6H00_BETA_X5.csv` · `MASTER_BASE_V8_6_FORTRESS_6H00_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 955 | 89.1% | 46 | +0.2709 |
| TRANSITOIRE (bruit retail) | 112 | 10.4% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 5 | 0.5% | 0 | +0.0000 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.0697 · σ=0.3933 · n=1072

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 1072 | 46 | 986 | +0.2709 | `2026-09-07T23:36:47Z` → `2026-09-08T03:13:54Z` |
| ALPHA | 1920 | 17 | 1903 | -1.2512 | `2026-09-07T23:36:54Z` → `2026-09-08T03:13:56Z` |
| **TOTAL** | | 63 | | **-0.9802** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `regime_gate` | 865 | 87.7% |
| `wall_not_collapsed` | 79 | 8.0% |
| `radar_block` | 38 | 3.9% |
| `tactic_mismatch` | 4 | 0.4% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `regime_gate` | 1549 | 81.4% |
| `duo_wait` | 155 | 8.1% |
| `wall_not_collapsed` | 127 | 6.7% |
| `radar_block` | 64 | 3.4% |
| `tactic_mismatch` | 8 | 0.4% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

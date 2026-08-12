# JOURNAL ENGLE — NUAGE_TEST_8H_CMP3

- Généré: `2026-08-12T10:24:13Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-08-02T18:18:13Z`
- CSV: `NUAGE_TEST_8H_CMP3_BETA_X5.csv` · `NUAGE_TEST_8H_CMP3_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 563 | 96.2% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 15 | 2.6% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 7 | 1.2% | 1 | -0.0047 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.0392 · σ=0.4077 · n=585

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 585 | 1 | 584 | -0.0047 | `2026-08-02T18:18:24Z` → `2026-08-02T19:53:40Z` |
| ALPHA | 546 | 0 | 546 | +0.0000 | `2026-08-02T18:18:26Z` → `2026-08-02T19:54:01Z` |
| **TOTAL** | | 1 | | **-0.0047** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 546 | 93.5% |
| `radar_block` | 29 | 5.0% |
| `vacuum_filter` | 6 | 1.0% |
| `wall_not_collapsed` | 3 | 0.5% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `momentum_too_small` | 507 | 92.9% |
| `radar_block` | 32 | 5.9% |
| `vacuum_filter` | 4 | 0.7% |
| `wall_not_collapsed` | 3 | 0.5% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

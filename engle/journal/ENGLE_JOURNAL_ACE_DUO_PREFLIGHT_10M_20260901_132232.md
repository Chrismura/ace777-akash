# JOURNAL ENGLE — ACE_DUO_PREFLIGHT_10M

- Généré: `2026-09-01T13:22:32Z` (UTC)
- Couche: **B1** (lecture seule) · `ENGLE_ADAPT=0`
- Session start (filtre): `2026-09-01T13:12:21Z`
- CSV: `ACE_DUO_PREFLIGHT_10M_BETA_X5.csv` · `ACE_DUO_PREFLIGHT_10M_ALPHA_X13_BURST13.csv`
- Base: usine V2.2.1 + champion 37fca367 — **non modifié**

## Régime IRM (proxy)

| Régime | Cycles | % | Fills | PnL fills |
|--------|--------|---|-------|-----------|
| COMPRESSÉ (attente à froid) | 42 | 79.2% | 2 | +0.0691 |
| TRANSITOIRE (bruit retail) | 7 | 13.2% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 4 | 7.5% | 0 | +0.0000 |

- Courant (proxy): **COMPRESSÉ (attente à froid)** · μ=0.2749 · σ=1.0839 · n=53

## Posture recommandée (conseil — pas appliquée)

- Code: `WAIT_COLD`
- Marché calme — ne pas assouplir les seuils ; usine pure recommandée.
- Application moteur: **aucune** tant que B3 n’est pas GO + `ENGLE_ADAPT` dédié.

## Activité session

| Unité | Cycles | Fills | Skips | PnL fills (USDT) | Fenêtre |
|-------|--------|-------|-------|------------------|---------|
| BETA | 53 | 2 | 51 | +0.0691 | `2026-09-01T13:12:30Z` → `2026-09-01T13:22:26Z` |
| ALPHA | 60 | 1 | 59 | -0.1868 | `2026-09-01T13:12:30Z` → `2026-09-01T13:22:30Z` |
| **TOTAL** | | 3 | | **-0.1177** | |

## SKIP BETA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `regime_gate` | 40 | 78.4% |
| `radar_block` | 11 | 21.6% |

## SKIP ALPHA (top)

| Raison | Nb | % skips |
|--------|-----|---------|
| `regime_gate` | 44 | 74.6% |
| `radar_block` | 9 | 15.3% |
| `wall_not_collapsed` | 3 | 5.1% |
| `duo_wait` | 3 | 5.1% |

## Lecture courte (marché calme)

1. **COMPRESSÉ dominant** — normal que `momentum_too_small` / `wall_not_collapsed` mènent.
2. **Ne pas baisser les barrières** pour « forcer » des fills en calme.
3. Garder usine + B1/B2 log ; B3 seulement après runs contrastés (cluster réel).
4. Rollback always: coffre `29$/historique/ACE777_SAUVEGARDE_SETUP_JUILLET_20260718/`.

---

*B1 engle_journal.rb — zéro ordre, zéro genesis.*

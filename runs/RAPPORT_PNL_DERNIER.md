# RAPPORT PNL AUTO — MASTER_VORTEX_V2_COLLAB_4H

**Session:** `MASTER_VORTEX_V2_COLLAB_4H`
**Période:** 2026-08-14T07:41:10Z → 2026-08-14T07:56:26Z (0h15m)
**Setup:** `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt` | BETA `200` USDT | ALPHA `800` USDT | LLM gate `TRUE` fail_closed=`TRUE`
**Généré:** 2026-08-14T07:56:34Z UTC
**Filtre session:** `ts >= 2026-08-14T07:40:59Z` (lignes CSV antérieures exclues)

---

## BILAN GLOBAL

| Métrique | Valeur |
|----------|--------|
| **PNL BETA** | **+0.1240 USDT** |
| **PNL ALPHA** | **+2.9474 USDT** |
| **PNL SESSION TOTAL** | **+3.0714 USDT** |
| Statut | `POSITIF` |

---

## BETA — BETA (SCOUT x5)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 10 |
| Gagnants | 5 |
| Perdants | 5 |
| Flat (0) | 0 |
| Win rate | **50.0%** |
| Gains totaux | +0.1958 USDT |
| Pertes totales | -0.0718 USDT |
| **PNL net** | **+0.1240 USDT** |
| BPS moyen | 0.20 |

**Meilleur trade:** +0.1231 USDT
**Pire trade:** -0.0339 USDT

**Direction:** SELL (10)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| shock_inversion_stop | 6 |
| fluid_exit_inversion | 4 |

**Cycles SKIP:** 67
| Raison | Nb |
|--------|-----|
| radar_block | 49 |
| impulse_resonance_wait | 16 |
| tactic_mismatch | 2 |

---

## ALPHA — ALPHA (HUNTER x13)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 2 |
| Gagnants | 2 |
| Perdants | 0 |
| Flat (0) | 0 |
| Win rate | **100.0%** |
| Gains totaux | +2.9474 USDT |
| Pertes totales | +0.0000 USDT |
| **PNL net** | **+2.9474 USDT** |
| BPS moyen | 1.12 |

**Meilleur trade:** +2.6752 USDT
**Pire trade:** +0.2722 USDT

**Direction:** BUY (2)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| shock_inversion_stop | 1 |
| fluid_exit_brake | 1 |

**Cycles SKIP:** 41
| Raison | Nb |
|--------|-----|
| radar_block | 31 |
| impulse_resonance_wait | 10 |

---

## SYNTHÈSE

| Indicateur | BETA | ALPHA | TOTAL |
|------------|------|-------|-------|
| Trades | 10 | 2 | 12 |
| PnL | +0.1240 | +2.9474 | **+3.0714** |
| Win rate | 50.0% | 100.0% | 58.3% |

## IRM — régimes de tension (proxy, lecture seule)

> Pas un modèle ARCH Engle. Classification sur `tension=` des cycles BETA. N'influence pas le moteur. Seuils: COMPRESSÉ `< 0.05` · CLUSTER `≥ 1.0` · sinon TRANSITOIRE.

| Régime | Cycles | % temps | Fills | PnL fills (USDT) |
|--------|--------|---------|-------|------------------|
| COMPRESSÉ (attente à froid) | 39 | 50.6% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 28 | 36.4% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 10 | 13.0% | 10 | +0.1240 |

- Fenêtre: `2026-08-14T07:41:10Z` → `2026-08-14T07:56:26Z` (77 cycles) · μ(tension)=0.3280 · σ=0.5299 · courant(proxy)=**COMPRESSÉ (attente à froid)**
- Source: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`

## Engle — couches évolutives (hors moteur)

- Plan: `engle/PLAN_COUCHES_B1_B3.md`
- Journal B1: `engle/journal/ENGLE_JOURNAL_DERNIER.md` (généré via `engle_journal.rb` / `update_state_md.sh`)
- Adapt B2: `ENGLE_ADAPT=0` (défaut OFF = usine pure ; `log` = posture JSON only)
- Dernière posture log: `WAIT_COLD` · régime `COMPRESSE` · applied=`false`

## CONFIG ACTIVE (snapshot)

- ENTRY_25_75 BETA: `0.70` | ALPHA: `0.50`
- SHOCK_EXIT: `16` bps
- VOLATILITY_FILTER: `16`
- STASE: spread=`16` vol=`16`
- POLL_SEC: `0.064`

---

*Rapport auto — CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` | `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`*
*STATE: `runs/STATE.md`*

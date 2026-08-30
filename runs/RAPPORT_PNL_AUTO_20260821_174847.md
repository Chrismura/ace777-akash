# RAPPORT PNL AUTO — MASTER_VORTEX_V2_COLLAB_4H

**Session:** `MASTER_VORTEX_V2_COLLAB_4H`
**Période:** 2026-08-21T13:48:52Z → 2026-08-21T17:48:43Z (3h59m)
**Setup:** `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt` | BETA `200` USDT | ALPHA `800` USDT | LLM gate `TRUE` fail_closed=`TRUE`
**Généré:** 2026-08-21T17:48:47Z UTC
**Filtre session:** `ts >= 2026-08-21T13:48:42Z` (lignes CSV antérieures exclues)

---

## BILAN GLOBAL

| Métrique | Valeur |
|----------|--------|
| **PNL BETA** | **+7.7126 USDT** |
| **PNL ALPHA** | **+10.6060 USDT** |
| **PNL SESSION TOTAL** | **+18.3186 USDT** |
| Statut | `POSITIF` |

---

## BETA — BETA (SCOUT x5)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 43 |
| Gagnants | 25 |
| Perdants | 18 |
| Flat (0) | 0 |
| Win rate | **58.1%** |
| Gains totaux | +15.9892 USDT |
| Pertes totales | -8.2766 USDT |
| **PNL net** | **+7.7126 USDT** |
| BPS moyen | 3.46 |

**Meilleur trade:** +2.5722 USDT
**Pire trade:** -1.1341 USDT

**Direction:** SELL (43)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| 0.39424000 | 2 |
| 0.39776358 | 2 |
| 0.39566182 | 1 |
| 0.39464397 | 1 |
| 0.27684000 | 1 |

**Cycles SKIP:** 1867
| Raison | Nb |
|--------|-----|
| gap_guard_pause | 1532 |
| regime_gate | 255 |
| impulse_resonance_wait | 46 |
| radar_block | 21 |
| tactic_mismatch | 8 |

---

## ALPHA — ALPHA (HUNTER x13)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 28 |
| Gagnants | 16 |
| Perdants | 12 |
| Flat (0) | 0 |
| Win rate | **57.1%** |
| Gains totaux | +30.2505 USDT |
| Pertes totales | -19.6445 USDT |
| **PNL net** | **+10.6060 USDT** |
| BPS moyen | 0.71 |

**Meilleur trade:** +5.9712 USDT
**Pire trade:** -3.9700 USDT

**Direction:** BUY (28)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| 0.65050188 | 1 |
| 0.80435680 | 1 |
| 1.74315774 | 1 |
| 0.80677765 | 1 |
| 0.80523080 | 1 |

**Cycles SKIP:** 1677
| Raison | Nb |
|--------|-----|
| gap_guard_pause | 956 |
| regime_gate | 467 |
| duo_wait | 99 |
| impulse_resonance_wait | 93 |
| radar_block | 30 |

---

## SYNTHÈSE

| Indicateur | BETA | ALPHA | TOTAL |
|------------|------|-------|-------|
| Trades | 43 | 28 | 71 |
| PnL | +7.7126 | +10.6060 | **+18.3186** |
| Win rate | 58.1% | 57.1% | 57.7% |

## IRM — régimes de tension (proxy, lecture seule)

> Pas un modèle ARCH Engle. Classification sur `tension=` des cycles BETA. N'influence pas le moteur. Seuils: COMPRESSÉ `< 0.05` · CLUSTER `≥ 1.0` · sinon TRANSITOIRE.

| Régime | Cycles | % temps | Fills | PnL fills (USDT) |
|--------|--------|---------|-------|------------------|
| COMPRESSÉ (attente à froid) | 1861 | 96.5% | 43 | +7.7126 |
| TRANSITOIRE (bruit retail) | 66 | 3.4% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 1 | 0.1% | 0 | +0.0000 |

- Fenêtre: `2026-08-21T13:48:53Z` → `2026-08-21T17:48:42Z` (1928 cycles) · μ(tension)=0.0188 · σ=0.1192 · courant(proxy)=**COMPRESSÉ (attente à froid)**
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

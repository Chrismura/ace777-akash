# RAPPORT PNL AUTO — MASTER_VORTEX_V2_COLLAB_4H

**Session:** `MASTER_VORTEX_V2_COLLAB_4H`
**Période:** 2026-08-14T19:54:34Z → 2026-08-14T20:24:30Z (0h29m)
**Setup:** `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt` | BETA `200` USDT | ALPHA `800` USDT | LLM gate `TRUE` fail_closed=`TRUE`
**Généré:** 2026-08-14T20:24:33Z UTC
**Filtre session:** `ts >= 2026-08-14T19:54:23Z` (lignes CSV antérieures exclues)

---

## BILAN GLOBAL

| Métrique | Valeur |
|----------|--------|
| **PNL BETA** | **+0.2811 USDT** |
| **PNL ALPHA** | **+7.5524 USDT** |
| **PNL SESSION TOTAL** | **+7.8336 USDT** |
| Statut | `POSITIF` |

---

## BETA — BETA (SCOUT x5)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 22 |
| Gagnants | 8 |
| Perdants | 8 |
| Flat (0) | 6 |
| Win rate | **36.4%** |
| Gains totaux | +0.3490 USDT |
| Pertes totales | -0.0679 USDT |
| **PNL net** | **+0.2811 USDT** |
| BPS moyen | 0.30 |

**Meilleur trade:** +0.1137 USDT
**Pire trade:** -0.0216 USDT

**Direction:** SELL (22)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| shock_inversion_stop | 16 |
| fluid_exit_inversion | 5 |
| fluid_exit_brake | 1 |

**Cycles SKIP:** 147
| Raison | Nb |
|--------|-----|
| radar_block | 122 |
| impulse_resonance_wait | 22 |
| tactic_mismatch | 3 |

---

## ALPHA — ALPHA (HUNTER x13)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 11 |
| Gagnants | 7 |
| Perdants | 1 |
| Flat (0) | 3 |
| Win rate | **63.6%** |
| Gains totaux | +7.8991 USDT |
| Pertes totales | -0.3466 USDT |
| **PNL net** | **+7.5524 USDT** |
| BPS moyen | 0.71 |

**Meilleur trade:** +5.0386 USDT
**Pire trade:** -0.3466 USDT

**Direction:** BUY (11)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| shock_inversion_stop | 9 |
| fluid_exit_inversion | 1 |
| fluid_exit_brake | 1 |

**Cycles SKIP:** 166
| Raison | Nb |
|--------|-----|
| radar_block | 136 |
| impulse_resonance_wait | 16 |
| duo_wait | 11 |
| tactic_mismatch | 3 |

---

## SYNTHÈSE

| Indicateur | BETA | ALPHA | TOTAL |
|------------|------|-------|-------|
| Trades | 22 | 11 | 33 |
| PnL | +0.2811 | +7.5524 | **+7.8336** |
| Win rate | 36.4% | 63.6% | 45.5% |

## IRM — régimes de tension (proxy, lecture seule)

> Pas un modèle ARCH Engle. Classification sur `tension=` des cycles BETA. N'influence pas le moteur. Seuils: COMPRESSÉ `< 0.05` · CLUSTER `≥ 1.0` · sinon TRANSITOIRE.

| Régime | Cycles | % temps | Fills | PnL fills (USDT) |
|--------|--------|---------|-------|------------------|
| COMPRESSÉ (attente à froid) | 115 | 68.0% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 32 | 18.9% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 22 | 13.0% | 22 | +0.2811 |

- Fenêtre: `2026-08-14T19:54:34Z` → `2026-08-14T20:24:28Z` (169 cycles) · μ(tension)=0.3834 · σ=0.9828 · courant(proxy)=**COMPRESSÉ (attente à froid)**
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

# RAPPORT PNL AUTO — MASTER_VORTEX_V2_COLLAB_4H

**Session:** `MASTER_VORTEX_V2_COLLAB_4H`
**Période:** 2026-08-17T07:40:25Z → 2026-08-17T11:40:16Z (3h59m)
**Setup:** `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt` | BETA `200` USDT | ALPHA `800` USDT | LLM gate `TRUE` fail_closed=`TRUE`
**Généré:** 2026-08-17T11:40:19Z UTC
**Filtre session:** `ts >= 2026-08-17T07:40:11Z` (lignes CSV antérieures exclues)

---

## BILAN GLOBAL

| Métrique | Valeur |
|----------|--------|
| **PNL BETA** | **+0.2388 USDT** |
| **PNL ALPHA** | **-3.0541 USDT** |
| **PNL SESSION TOTAL** | **-2.8153 USDT** |
| Statut | `NEGATIF` |

---

## BETA — BETA (SCOUT x5)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 138 |
| Gagnants | 53 |
| Perdants | 45 |
| Flat (0) | 40 |
| Win rate | **38.4%** |
| Gains totaux | +2.5174 USDT |
| Pertes totales | -2.2786 USDT |
| **PNL net** | **+0.2388 USDT** |
| BPS moyen | -0.01 |

**Meilleur trade:** +0.4524 USDT
**Pire trade:** -0.3100 USDT

**Direction:** SELL (138)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| shock_inversion_stop | 96 |
| fluid_exit_inversion | 28 |
| fluid_exit_brake | 14 |

**Cycles SKIP:** 1058
| Raison | Nb |
|--------|-----|
| radar_block | 790 |
| impulse_resonance_wait | 208 |
| gap_guard_pause | 48 |
| tactic_mismatch | 9 |
| stase_ecoute | 3 |

---

## ALPHA — ALPHA (HUNTER x13)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 78 |
| Gagnants | 31 |
| Perdants | 30 |
| Flat (0) | 17 |
| Win rate | **39.7%** |
| Gains totaux | +7.3690 USDT |
| Pertes totales | -10.4231 USDT |
| **PNL net** | **-3.0541 USDT** |
| BPS moyen | -0.07 |

**Meilleur trade:** +1.2933 USDT
**Pire trade:** -2.7773 USDT

**Direction:** BUY (78)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| shock_inversion_stop | 48 |
| fluid_exit_inversion | 19 |
| fluid_exit_brake | 11 |

**Cycles SKIP:** 1116
| Raison | Nb |
|--------|-----|
| radar_block | 843 |
| impulse_resonance_wait | 186 |
| duo_wait | 70 |
| tactic_mismatch | 12 |
| stase_ecoute | 5 |

---

## SYNTHÈSE

| Indicateur | BETA | ALPHA | TOTAL |
|------------|------|-------|-------|
| Trades | 138 | 78 | 216 |
| PnL | +0.2388 | -3.0541 | **-2.8153** |
| Win rate | 38.4% | 39.7% | 38.9% |

## IRM — régimes de tension (proxy, lecture seule)

> Pas un modèle ARCH Engle. Classification sur `tension=` des cycles BETA. N'influence pas le moteur. Seuils: COMPRESSÉ `< 0.05` · CLUSTER `≥ 1.0` · sinon TRANSITOIRE.

| Régime | Cycles | % temps | Fills | PnL fills (USDT) |
|--------|--------|---------|-------|------------------|
| COMPRESSÉ (attente à froid) | 789 | 66.0% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 269 | 22.5% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 138 | 11.5% | 138 | +0.2388 |

- Fenêtre: `2026-08-17T07:40:34Z` → `2026-08-17T11:40:12Z` (1196 cycles) · μ(tension)=0.4084 · σ=1.1718 · courant(proxy)=**COMPRESSÉ (attente à froid)**
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

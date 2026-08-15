# RAPPORT PNL AUTO — MASTER_VORTEX_V2_COLLAB_4H

**Session:** `MASTER_VORTEX_V2_COLLAB_4H`
**Période:** 2026-08-13T18:12:49Z → 2026-08-13T20:37:07Z (2h24m)
**Setup:** `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt` | BETA `200` USDT | ALPHA `800` USDT | LLM gate `TRUE` fail_closed=`TRUE`
**Généré:** 2026-08-13T20:37:10Z UTC
**Filtre session:** `ts >= 2026-08-13T18:12:39Z` (lignes CSV antérieures exclues)

---

## BILAN GLOBAL

| Métrique | Valeur |
|----------|--------|
| **PNL BETA** | **+0.5452 USDT** |
| **PNL ALPHA** | **+0.8266 USDT** |
| **PNL SESSION TOTAL** | **+1.3718 USDT** |
| Statut | `POSITIF` |

---

## BETA — BETA (SCOUT x5)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 83 |
| Gagnants | 29 |
| Perdants | 30 |
| Flat (0) | 24 |
| Win rate | **34.9%** |
| Gains totaux | +2.0271 USDT |
| Pertes totales | -1.4818 USDT |
| **PNL net** | **+0.5452 USDT** |
| BPS moyen | 0.24 |

**Meilleur trade:** +0.3422 USDT
**Pire trade:** -0.2662 USDT

**Direction:** SELL (83)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| shock_inversion_stop | 61 |
| fluid_exit_inversion | 14 |
| fluid_exit_brake | 8 |

**Cycles SKIP:** 943
| Raison | Nb |
|--------|-----|
| radar_block | 859 |
| impulse_resonance_wait | 77 |
| tactic_mismatch | 5 |
| stase_ecoute | 2 |

---

## ALPHA — ALPHA (HUNTER x13)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 5 |
| Gagnants | 4 |
| Perdants | 0 |
| Flat (0) | 1 |
| Win rate | **80.0%** |
| Gains totaux | +0.8266 USDT |
| Pertes totales | +0.0000 USDT |
| **PNL net** | **+0.8266 USDT** |
| BPS moyen | 0.15 |

**Meilleur trade:** +0.6170 USDT
**Pire trade:** +0.0000 USDT

**Direction:** BUY (5)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| shock_inversion_stop | 3 |
| fluid_exit_brake | 1 |
| fluid_exit_inversion | 1 |

**Cycles SKIP:** 76
| Raison | Nb |
|--------|-----|
| radar_block | 68 |
| impulse_resonance_wait | 5 |
| duo_wait | 2 |
| tactic_mismatch | 1 |

---

## SYNTHÈSE

| Indicateur | BETA | ALPHA | TOTAL |
|------------|------|-------|-------|
| Trades | 83 | 5 | 88 |
| PnL | +0.5452 | +0.8266 | **+1.3718** |
| Win rate | 34.9% | 80.0% | 37.5% |

## IRM — régimes de tension (proxy, lecture seule)

> Pas un modèle ARCH Engle. Classification sur `tension=` des cycles BETA. N'influence pas le moteur. Seuils: COMPRESSÉ `< 0.05` · CLUSTER `≥ 1.0` · sinon TRANSITOIRE.

| Régime | Cycles | % temps | Fills | PnL fills (USDT) |
|--------|--------|---------|-------|------------------|
| COMPRESSÉ (attente à froid) | 811 | 79.0% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 131 | 12.8% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 84 | 8.2% | 83 | +0.5452 |

- Fenêtre: `2026-08-13T18:12:49Z` → `2026-08-13T20:37:07Z` (1026 cycles) · μ(tension)=0.2980 · σ=1.0334 · courant(proxy)=**COMPRESSÉ (attente à froid)**
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

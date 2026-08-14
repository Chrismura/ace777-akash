# RAPPORT PNL AUTO — MASTER_VORTEX_V2_COLLAB_4H

**Session:** `MASTER_VORTEX_V2_COLLAB_4H`
**Période:** 2026-08-14T12:51:14Z → 2026-08-14T15:57:03Z (3h05m)
**Setup:** `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt` | BETA `200` USDT | ALPHA `800` USDT | LLM gate `TRUE` fail_closed=`TRUE`
**Généré:** 2026-08-14T15:57:06Z UTC
**Filtre session:** `ts >= 2026-08-14T12:51:05Z` (lignes CSV antérieures exclues)

---

## BILAN GLOBAL

| Métrique | Valeur |
|----------|--------|
| **PNL BETA** | **+0.3956 USDT** |
| **PNL ALPHA** | **+28.2570 USDT** |
| **PNL SESSION TOTAL** | **+28.6526 USDT** |
| Statut | `POSITIF` |

---

## BETA — BETA (SCOUT x5)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 155 |
| Gagnants | 57 |
| Perdants | 65 |
| Flat (0) | 33 |
| Win rate | **36.8%** |
| Gains totaux | +3.5285 USDT |
| Pertes totales | -3.1329 USDT |
| **PNL net** | **+0.3956 USDT** |
| BPS moyen | -0.01 |

**Meilleur trade:** +0.5443 USDT
**Pire trade:** -0.3834 USDT

**Direction:** SELL (155)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| shock_inversion_stop | 123 |
| fluid_exit_inversion | 26 |
| fluid_exit_brake | 5 |
| shock_exit_10bps | 1 |

**Cycles SKIP:** 1089
| Raison | Nb |
|--------|-----|
| radar_block | 960 |
| impulse_resonance_wait | 113 |
| tactic_mismatch | 11 |
| stase_ecoute | 5 |

---

## ALPHA — ALPHA (HUNTER x13)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 65 |
| Gagnants | 30 |
| Perdants | 19 |
| Flat (0) | 16 |
| Win rate | **46.2%** |
| Gains totaux | +70.2873 USDT |
| Pertes totales | -42.0302 USDT |
| **PNL net** | **+28.2570 USDT** |
| BPS moyen | 0.25 |

**Meilleur trade:** +37.3299 USDT
**Pire trade:** -8.1873 USDT

**Direction:** BUY (65)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| shock_inversion_stop | 53 |
| fluid_exit_inversion | 10 |
| fluid_exit_brake | 2 |

**Cycles SKIP:** 1255
| Raison | Nb |
|--------|-----|
| radar_block | 997 |
| impulse_resonance_wait | 117 |
| duo_wait | 114 |
| tactic_mismatch | 21 |
| stase_ecoute | 6 |

---

## SYNTHÈSE

| Indicateur | BETA | ALPHA | TOTAL |
|------------|------|-------|-------|
| Trades | 155 | 65 | 220 |
| PnL | +0.3956 | +28.2570 | **+28.6526** |
| Win rate | 36.8% | 46.2% | 39.5% |

## IRM — régimes de tension (proxy, lecture seule)

> Pas un modèle ARCH Engle. Classification sur `tension=` des cycles BETA. N'influence pas le moteur. Seuils: COMPRESSÉ `< 0.05` · CLUSTER `≥ 1.0` · sinon TRANSITOIRE.

| Régime | Cycles | % temps | Fills | PnL fills (USDT) |
|--------|--------|---------|-------|------------------|
| COMPRESSÉ (attente à froid) | 918 | 73.8% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 167 | 13.4% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 159 | 12.8% | 155 | +0.3956 |

- Fenêtre: `2026-08-14T12:51:14Z` → `2026-08-14T15:57:03Z` (1244 cycles) · μ(tension)=0.4896 · σ=1.4285 · courant(proxy)=**COMPRESSÉ (attente à froid)**
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

# RAPPORT PNL AUTO — MASTER_VORTEX_V2_COLLAB_4H

**Session:** `MASTER_VORTEX_V2_COLLAB_4H`
**Période:** 2026-08-16T08:02:41Z → 2026-08-16T10:02:37Z (1h59m)
**Setup:** `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt` | BETA `200` USDT | ALPHA `800` USDT | LLM gate `TRUE` fail_closed=`TRUE`
**Généré:** 2026-08-16T10:02:40Z UTC
**Filtre session:** `ts >= 2026-08-16T08:02:31Z` (lignes CSV antérieures exclues)

---

## BILAN GLOBAL

| Métrique | Valeur |
|----------|--------|
| **PNL BETA** | **+0.0565 USDT** |
| **PNL ALPHA** | **-1.0421 USDT** |
| **PNL SESSION TOTAL** | **-0.9856 USDT** |
| Statut | `NEGATIF` |

---

## BETA — BETA (SCOUT x5)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 23 |
| Gagnants | 11 |
| Perdants | 7 |
| Flat (0) | 5 |
| Win rate | **47.8%** |
| Gains totaux | +0.5037 USDT |
| Pertes totales | -0.4472 USDT |
| **PNL net** | **+0.0565 USDT** |
| BPS moyen | 0.02 |

**Meilleur trade:** +0.2072 USDT
**Pire trade:** -0.1601 USDT

**Direction:** SELL (23)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| shock_inversion_stop | 20 |
| fluid_exit_inversion | 2 |
| fluid_exit_brake | 1 |

**Cycles SKIP:** 665
| Raison | Nb |
|--------|-----|
| radar_block | 562 |
| impulse_resonance_wait | 51 |
| price_stasis | 48 |
| stase_ecoute | 2 |
| tactic_mismatch | 2 |

---

## ALPHA — ALPHA (HUNTER x13)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 3 |
| Gagnants | 0 |
| Perdants | 2 |
| Flat (0) | 1 |
| Win rate | **0.0%** |
| Gains totaux | +0.0000 USDT |
| Pertes totales | -1.0421 USDT |
| **PNL net** | **-1.0421 USDT** |
| BPS moyen | -1.74 |

**Meilleur trade:** +0.0000 USDT
**Pire trade:** -1.0398 USDT

**Direction:** BUY (3)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| fluid_exit_brake | 2 |
| shock_inversion_stop | 1 |

**Cycles SKIP:** 672
| Raison | Nb |
|--------|-----|
| radar_block | 558 |
| duo_wait | 60 |
| impulse_resonance_wait | 47 |
| price_stasis | 4 |
| tactic_mismatch | 3 |

---

## SYNTHÈSE

| Indicateur | BETA | ALPHA | TOTAL |
|------------|------|-------|-------|
| Trades | 23 | 3 | 26 |
| PnL | +0.0565 | -1.0421 | **-0.9856** |
| Win rate | 47.8% | 0.0% | 42.3% |

## IRM — régimes de tension (proxy, lecture seule)

> Pas un modèle ARCH Engle. Classification sur `tension=` des cycles BETA. N'influence pas le moteur. Seuils: COMPRESSÉ `< 0.05` · CLUSTER `≥ 1.0` · sinon TRANSITOIRE.

| Régime | Cycles | % temps | Fills | PnL fills (USDT) |
|--------|--------|---------|-------|------------------|
| COMPRESSÉ (attente à froid) | 548 | 79.7% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 69 | 10.0% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 71 | 10.3% | 23 | +0.0565 |

- Fenêtre: `2026-08-16T08:02:41Z` → `2026-08-16T10:02:37Z` (688 cycles) · μ(tension)=0.4336 · σ=1.3709 · courant(proxy)=**COMPRESSÉ (attente à froid)**
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

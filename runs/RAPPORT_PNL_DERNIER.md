# RAPPORT PNL AUTO — MASTER_VORTEX_V2_COLLAB_4H

**Session:** `MASTER_VORTEX_V2_COLLAB_4H`
**Période:** 2026-08-20T14:06:39Z → 2026-08-20T14:32:47Z (0h26m)
**Setup:** `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt` | BETA `200` USDT | ALPHA `800` USDT | LLM gate `TRUE` fail_closed=`TRUE`
**Généré:** 2026-08-20T14:32:51Z UTC
**Filtre session:** `ts >= 2026-08-20T14:06:28Z` (lignes CSV antérieures exclues)

---

## BILAN GLOBAL

| Métrique | Valeur |
|----------|--------|
| **PNL BETA** | **+0.2532 USDT** |
| **PNL ALPHA** | **-3.8409 USDT** |
| **PNL SESSION TOTAL** | **-3.5877 USDT** |
| Statut | `NEGATIF` |

---

## BETA — BETA (SCOUT x5)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 18 |
| Gagnants | 9 |
| Perdants | 8 |
| Flat (0) | 1 |
| Win rate | **50.0%** |
| Gains totaux | +2.2104 USDT |
| Pertes totales | -1.9572 USDT |
| **PNL net** | **+0.2532 USDT** |
| BPS moyen | 0.49 |

**Meilleur trade:** +0.8915 USDT
**Pire trade:** -0.7854 USDT

**Direction:** SELL (18)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| 0.38901005 | 1 |
| 0.39030314 | 1 |
| 0.39046634 | 1 |
| 0.39048429 | 1 |
| 0.39045926 | 1 |

**Cycles SKIP:** 78
| Raison | Nb |
|--------|-----|
| radar_block | 63 |
| impulse_resonance_wait | 11 |
| stase_ecoute | 3 |
| tactic_mismatch | 1 |

---

## ALPHA — ALPHA (HUNTER x13)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 12 |
| Gagnants | 4 |
| Perdants | 6 |
| Flat (0) | 2 |
| Win rate | **33.3%** |
| Gains totaux | +0.6143 USDT |
| Pertes totales | -4.4552 USDT |
| **PNL net** | **-3.8409 USDT** |
| BPS moyen | -1.37 |

**Meilleur trade:** +0.2842 USDT
**Pire trade:** -1.5475 USDT

**Direction:** BUY (12)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| 2.59768994 | 1 |
| 4.78911490 | 1 |
| 3.19818260 | 1 |
| 3.88234371 | 1 |
| 3.88276013 | 1 |

**Cycles SKIP:** 121
| Raison | Nb |
|--------|-----|
| radar_block | 60 |
| gap_guard_pause | 42 |
| impulse_resonance_wait | 11 |
| tactic_mismatch | 5 |
| stase_ecoute | 2 |

---

## SYNTHÈSE

| Indicateur | BETA | ALPHA | TOTAL |
|------------|------|-------|-------|
| Trades | 18 | 12 | 30 |
| PnL | +0.2532 | -3.8409 | **-3.5877** |
| Win rate | 50.0% | 33.3% | 43.3% |

## IRM — régimes de tension (proxy, lecture seule)

> Pas un modèle ARCH Engle. Classification sur `tension=` des cycles BETA. N'influence pas le moteur. Seuils: COMPRESSÉ `< 0.05` · CLUSTER `≥ 1.0` · sinon TRANSITOIRE.

| Régime | Cycles | % temps | Fills | PnL fills (USDT) |
|--------|--------|---------|-------|------------------|
| COMPRESSÉ (attente à froid) | 81 | 84.4% | 18 | +0.2532 |
| TRANSITOIRE (bruit retail) | 15 | 15.6% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 0 | 0.0% | 0 | +0.0000 |

- Fenêtre: `2026-08-20T14:06:39Z` → `2026-08-20T14:32:47Z` (96 cycles) · μ(tension)=0.0837 · σ=0.2378 · courant(proxy)=**COMPRESSÉ (attente à froid)**
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

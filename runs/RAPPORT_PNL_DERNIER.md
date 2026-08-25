# RAPPORT PNL AUTO — MASTER_VORTEX_V2_COLLAB_4H

**Session:** `MASTER_VORTEX_V2_COLLAB_4H`
**Période:** 2026-08-22T15:44:53Z → 2026-08-22T19:12:57Z (3h28m)
**Setup:** `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt` | BETA `200` USDT | ALPHA `800` USDT | LLM gate `TRUE` fail_closed=`TRUE`
**Généré:** 2026-08-22T19:13:25Z UTC
**Filtre session:** `ts >= 2026-08-22T15:44:10Z` (lignes CSV antérieures exclues)

---

## BILAN GLOBAL

| Métrique | Valeur |
|----------|--------|
| **PNL BETA** | **-0.7378 USDT** |
| **PNL ALPHA** | **+2.0052 USDT** |
| **PNL SESSION TOTAL** | **+1.2674 USDT** |
| Statut | `POSITIF` |

---

## BETA — BETA (SCOUT x5)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 13 |
| Gagnants | 5 |
| Perdants | 8 |
| Flat (0) | 0 |
| Win rate | **38.5%** |
| Gains totaux | +2.6391 USDT |
| Pertes totales | -3.3769 USDT |
| **PNL net** | **-0.7378 USDT** |
| BPS moyen | -2.07 |

**Meilleur trade:** +0.8954 USDT
**Pire trade:** -0.7519 USDT

**Direction:** SELL (13)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| 0.39565568 | 1 |
| 0.39407258 | 1 |
| 0.39455488 | 1 |
| 0.39502541 | 1 |
| 0.39529830 | 1 |

**Cycles SKIP:** 257
| Raison | Nb |
|--------|-----|
| gap_guard_pause | 222 |
| regime_gate | 19 |
| impulse_resonance_wait | 9 |
| radar_block | 4 |
| tactic_mismatch | 3 |

---

## ALPHA — ALPHA (HUNTER x13)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 9 |
| Gagnants | 3 |
| Perdants | 4 |
| Flat (0) | 2 |
| Win rate | **33.3%** |
| Gains totaux | +5.4741 USDT |
| Pertes totales | -3.4689 USDT |
| **PNL net** | **+2.0052 USDT** |
| BPS moyen | 0.20 |

**Meilleur trade:** +3.5234 USDT
**Pire trade:** -1.3178 USDT

**Direction:** BUY (9)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| 0.53795789 | 1 |
| 2.61881395 | 1 |
| 0.80432560 | 1 |
| 0.53856898 | 1 |
| 1.74344357 | 1 |

**Cycles SKIP:** 249
| Raison | Nb |
|--------|-----|
| gap_guard_pause | 193 |
| regime_gate | 27 |
| duo_wait | 9 |
| impulse_resonance_wait | 9 |
| tactic_mismatch | 6 |

---

## SYNTHÈSE

| Indicateur | BETA | ALPHA | TOTAL |
|------------|------|-------|-------|
| Trades | 13 | 9 | 22 |
| PnL | -0.7378 | +2.0052 | **+1.2674** |
| Win rate | 38.5% | 33.3% | 36.4% |

## IRM — régimes de tension (proxy, lecture seule)

> Pas un modèle ARCH Engle. Classification sur `tension=` des cycles BETA. N'influence pas le moteur. Seuils: COMPRESSÉ `< 0.05` · CLUSTER `≥ 1.0` · sinon TRANSITOIRE.

| Régime | Cycles | % temps | Fills | PnL fills (USDT) |
|--------|--------|---------|-------|------------------|
| COMPRESSÉ (attente à froid) | 259 | 95.2% | 13 | -0.7378 |
| TRANSITOIRE (bruit retail) | 12 | 4.4% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 1 | 0.4% | 0 | +0.0000 |

- Fenêtre: `2026-08-22T15:44:53Z` → `2026-08-22T19:12:57Z` (272 cycles) · μ(tension)=0.0383 · σ=0.2200 · courant(proxy)=**COMPRESSÉ (attente à froid)**
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

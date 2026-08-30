# RAPPORT PNL AUTO — MASTER_VORTEX_V2_COLLAB_4H

**Session:** `MASTER_VORTEX_V2_COLLAB_4H`
**Période:** 2026-08-22T07:33:00Z → 2026-08-22T11:32:46Z (3h59m)
**Setup:** `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt` | BETA `200` USDT | ALPHA `800` USDT | LLM gate `TRUE` fail_closed=`TRUE`
**Généré:** 2026-08-22T11:32:56Z UTC
**Filtre session:** `ts >= 2026-08-22T07:32:28Z` (lignes CSV antérieures exclues)

---

## BILAN GLOBAL

| Métrique | Valeur |
|----------|--------|
| **PNL BETA** | **+0.0114 USDT** |
| **PNL ALPHA** | **-2.3637 USDT** |
| **PNL SESSION TOTAL** | **-2.3523 USDT** |
| Statut | `NEGATIF` |

---

## BETA — BETA (SCOUT x5)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 22 |
| Gagnants | 13 |
| Perdants | 9 |
| Flat (0) | 0 |
| Win rate | **59.1%** |
| Gains totaux | +6.0791 USDT |
| Pertes totales | -6.0677 USDT |
| **PNL net** | **+0.0114 USDT** |
| BPS moyen | 1.73 |

**Meilleur trade:** +1.1725 USDT
**Pire trade:** -2.5935 USDT

**Direction:** SELL (22)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| 0.39406797 | 1 |
| 0.79281766 | 1 |
| 0.39580416 | 1 |
| 0.39605658 | 1 |
| 0.39601715 | 1 |

**Cycles SKIP:** 467
| Raison | Nb |
|--------|-----|
| gap_guard_pause | 351 |
| regime_gate | 78 |
| impulse_resonance_wait | 19 |
| radar_block | 7 |
| tactic_mismatch | 7 |

---

## ALPHA — ALPHA (HUNTER x13)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 14 |
| Gagnants | 5 |
| Perdants | 9 |
| Flat (0) | 0 |
| Win rate | **35.7%** |
| Gains totaux | +6.9532 USDT |
| Pertes totales | -9.3170 USDT |
| **PNL net** | **-2.3637 USDT** |
| BPS moyen | -1.73 |

**Meilleur trade:** +2.6542 USDT
**Pire trade:** -2.9139 USDT

**Direction:** BUY (14)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| 0.53581699 | 1 |
| 0.80465216 | 1 |
| 0.53837270 | 1 |
| 1.30494722 | 1 |
| 1.74672581 | 1 |

**Cycles SKIP:** 512
| Raison | Nb |
|--------|-----|
| gap_guard_pause | 278 |
| regime_gate | 140 |
| impulse_resonance_wait | 36 |
| duo_wait | 25 |
| radar_block | 17 |

---

## SYNTHÈSE

| Indicateur | BETA | ALPHA | TOTAL |
|------------|------|-------|-------|
| Trades | 22 | 14 | 36 |
| PnL | +0.0114 | -2.3637 | **-2.3523** |
| Win rate | 59.1% | 35.7% | 50.0% |

## IRM — régimes de tension (proxy, lecture seule)

> Pas un modèle ARCH Engle. Classification sur `tension=` des cycles BETA. N'influence pas le moteur. Seuils: COMPRESSÉ `< 0.05` · CLUSTER `≥ 1.0` · sinon TRANSITOIRE.

| Régime | Cycles | % temps | Fills | PnL fills (USDT) |
|--------|--------|---------|-------|------------------|
| COMPRESSÉ (attente à froid) | 463 | 94.7% | 22 | +0.0114 |
| TRANSITOIRE (bruit retail) | 24 | 4.9% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 2 | 0.4% | 0 | +0.0000 |

- Fenêtre: `2026-08-22T07:33:00Z` → `2026-08-22T11:32:46Z` (489 cycles) · μ(tension)=0.0437 · σ=0.3991 · courant(proxy)=**COMPRESSÉ (attente à froid)**
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

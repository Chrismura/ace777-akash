# RAPPORT PNL AUTO — MASTER_VORTEX_V2_COLLAB_4H

**Session:** `MASTER_VORTEX_V2_COLLAB_4H`
**Période:** 2026-08-22T03:32:20Z → 2026-08-22T07:31:56Z (3h59m)
**Setup:** `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt` | BETA `200` USDT | ALPHA `800` USDT | LLM gate `TRUE` fail_closed=`TRUE`
**Généré:** 2026-08-22T07:32:05Z UTC
**Filtre session:** `ts >= 2026-08-22T03:31:42Z` (lignes CSV antérieures exclues)

---

## BILAN GLOBAL

| Métrique | Valeur |
|----------|--------|
| **PNL BETA** | **+5.9114 USDT** |
| **PNL ALPHA** | **-8.4095 USDT** |
| **PNL SESSION TOTAL** | **-2.4981 USDT** |
| Statut | `NEGATIF` |

---

## BETA — BETA (SCOUT x5)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 23 |
| Gagnants | 16 |
| Perdants | 7 |
| Flat (0) | 0 |
| Win rate | **69.6%** |
| Gains totaux | +9.9609 USDT |
| Pertes totales | -4.0495 USDT |
| **PNL net** | **+5.9114 USDT** |
| BPS moyen | 3.40 |

**Meilleur trade:** +1.7597 USDT
**Pire trade:** -1.3482 USDT

**Direction:** SELL (23)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| 0.39624806 | 1 |
| 0.39613190 | 1 |
| 0.39630629 | 1 |
| 0.64066200 | 1 |
| 0.39507955 | 1 |

**Cycles SKIP:** 597
| Raison | Nb |
|--------|-----|
| gap_guard_pause | 429 |
| regime_gate | 86 |
| radar_block | 33 |
| impulse_resonance_wait | 25 |
| tactic_mismatch | 16 |

---

## ALPHA — ALPHA (HUNTER x13)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 15 |
| Gagnants | 5 |
| Perdants | 10 |
| Flat (0) | 0 |
| Win rate | **33.3%** |
| Gains totaux | +7.9129 USDT |
| Pertes totales | -16.3224 USDT |
| **PNL net** | **-8.4095 USDT** |
| BPS moyen | -7.06 |

**Meilleur trade:** +2.1923 USDT
**Pire trade:** -3.4940 USDT

**Direction:** BUY (15)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| 2.61889790 | 1 |
| 0.80519373 | 1 |
| 1.61375029 | 1 |
| 0.80624640 | 1 |
| 1.61421700 | 1 |

**Cycles SKIP:** 519
| Raison | Nb |
|--------|-----|
| gap_guard_pause | 282 |
| regime_gate | 108 |
| radar_block | 44 |
| impulse_resonance_wait | 36 |
| duo_wait | 33 |

---

## SYNTHÈSE

| Indicateur | BETA | ALPHA | TOTAL |
|------------|------|-------|-------|
| Trades | 23 | 15 | 38 |
| PnL | +5.9114 | -8.4095 | **-2.4981** |
| Win rate | 69.6% | 33.3% | 55.3% |

## IRM — régimes de tension (proxy, lecture seule)

> Pas un modèle ARCH Engle. Classification sur `tension=` des cycles BETA. N'influence pas le moteur. Seuils: COMPRESSÉ `< 0.05` · CLUSTER `≥ 1.0` · sinon TRANSITOIRE.

| Régime | Cycles | % temps | Fills | PnL fills (USDT) |
|--------|--------|---------|-------|------------------|
| COMPRESSÉ (attente à froid) | 562 | 90.6% | 23 | +5.9114 |
| TRANSITOIRE (bruit retail) | 45 | 7.3% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 13 | 2.1% | 0 | +0.0000 |

- Fenêtre: `2026-08-22T03:32:20Z` → `2026-08-22T07:31:42Z` (620 cycles) · μ(tension)=0.1801 · σ=1.1187 · courant(proxy)=**COMPRESSÉ (attente à froid)**
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

# RAPPORT PNL AUTO — MASTER_VORTEX_V2_COLLAB_4H

**Session:** `MASTER_VORTEX_V2_COLLAB_4H`
**Période:** 2026-08-20T19:14:26Z → 2026-08-20T19:42:02Z (0h27m)
**Setup:** `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt` | BETA `200` USDT | ALPHA `800` USDT | LLM gate `TRUE` fail_closed=`TRUE`
**Généré:** 2026-08-20T19:42:05Z UTC
**Filtre session:** `ts >= 2026-08-20T19:14:14Z` (lignes CSV antérieures exclues)

---

## BILAN GLOBAL

| Métrique | Valeur |
|----------|--------|
| **PNL BETA** | **-0.9346 USDT** |
| **PNL ALPHA** | **+5.2772 USDT** |
| **PNL SESSION TOTAL** | **+4.3426 USDT** |
| Statut | `POSITIF` |

---

## BETA — BETA (SCOUT x5)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 21 |
| Gagnants | 3 |
| Perdants | 15 |
| Flat (0) | 3 |
| Win rate | **14.3%** |
| Gains totaux | +0.1702 USDT |
| Pertes totales | -1.1048 USDT |
| **PNL net** | **-0.9346 USDT** |
| BPS moyen | -0.76 |

**Meilleur trade:** +0.1628 USDT
**Pire trade:** -0.2343 USDT

**Direction:** SELL (21)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| 0.38953318 | 1 |
| 0.79386458 | 1 |
| 0.39415357 | 1 |
| 0.38858928 | 1 |
| 0.38872650 | 1 |

**Cycles SKIP:** 110
| Raison | Nb |
|--------|-----|
| radar_block | 82 |
| impulse_resonance_wait | 24 |
| stase_ecoute | 2 |
| tactic_mismatch | 2 |

---

## ALPHA — ALPHA (HUNTER x13)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 15 |
| Gagnants | 11 |
| Perdants | 2 |
| Flat (0) | 2 |
| Win rate | **73.3%** |
| Gains totaux | +5.6034 USDT |
| Pertes totales | -0.3263 USDT |
| **PNL net** | **+5.2772 USDT** |
| BPS moyen | 0.84 |

**Meilleur trade:** +1.9044 USDT
**Pire trade:** -0.2684 USDT

**Direction:** BUY (15)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| 2.39533834 | 1 |
| 3.87914030 | 1 |
| 2.39562137 | 1 |
| 2.39698592 | 1 |
| 2.39803329 | 1 |

**Cycles SKIP:** 117
| Raison | Nb |
|--------|-----|
| radar_block | 91 |
| impulse_resonance_wait | 20 |
| tactic_mismatch | 6 |

---

## SYNTHÈSE

| Indicateur | BETA | ALPHA | TOTAL |
|------------|------|-------|-------|
| Trades | 21 | 15 | 36 |
| PnL | -0.9346 | +5.2772 | **+4.3426** |
| Win rate | 14.3% | 73.3% | 38.9% |

## IRM — régimes de tension (proxy, lecture seule)

> Pas un modèle ARCH Engle. Classification sur `tension=` des cycles BETA. N'influence pas le moteur. Seuils: COMPRESSÉ `< 0.05` · CLUSTER `≥ 1.0` · sinon TRANSITOIRE.

| Régime | Cycles | % temps | Fills | PnL fills (USDT) |
|--------|--------|---------|-------|------------------|
| COMPRESSÉ (attente à froid) | 102 | 77.9% | 21 | -0.9346 |
| TRANSITOIRE (bruit retail) | 29 | 22.1% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 0 | 0.0% | 0 | +0.0000 |

- Fenêtre: `2026-08-20T19:14:26Z` → `2026-08-20T19:42:02Z` (131 cycles) · μ(tension)=0.1042 · σ=0.2287 · courant(proxy)=**COMPRESSÉ (attente à froid)**
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

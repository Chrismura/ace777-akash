# RAPPORT PNL AUTO — MASTER_VORTEX_V2_COLLAB_4H

**Session:** `MASTER_VORTEX_V2_COLLAB_4H`
**Période:** 2026-08-21T19:45:36Z → 2026-08-21T23:21:25Z (3h35m)
**Setup:** `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt` | BETA `200` USDT | ALPHA `800` USDT | LLM gate `TRUE` fail_closed=`TRUE`
**Généré:** 2026-08-21T23:21:36Z UTC
**Filtre session:** `ts >= 2026-08-21T19:44:48Z` (lignes CSV antérieures exclues)

---

## BILAN GLOBAL

| Métrique | Valeur |
|----------|--------|
| **PNL BETA** | **-16.4899 USDT** |
| **PNL ALPHA** | **+37.4136 USDT** |
| **PNL SESSION TOTAL** | **+20.9237 USDT** |
| Statut | `POSITIF` |

---

## BETA — BETA (SCOUT x5)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 64 |
| Gagnants | 25 |
| Perdants | 39 |
| Flat (0) | 0 |
| Win rate | **39.1%** |
| Gains totaux | +12.2388 USDT |
| Pertes totales | -28.7286 USDT |
| **PNL net** | **-16.4899 USDT** |
| BPS moyen | -4.26 |

**Meilleur trade:** +1.5194 USDT
**Pire trade:** -2.0859 USDT

**Direction:** SELL (64)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| 0.39661524 | 3 |
| 0.39451406 | 2 |
| 1.28966878 | 2 |
| 0.39472742 | 1 |
| 0.39454822 | 1 |

**Cycles SKIP:** 1149
| Raison | Nb |
|--------|-----|
| gap_guard_pause | 934 |
| regime_gate | 113 |
| impulse_resonance_wait | 46 |
| radar_block | 21 |
| stase_ecoute | 19 |

---

## ALPHA — ALPHA (HUNTER x13)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 39 |
| Gagnants | 27 |
| Perdants | 12 |
| Flat (0) | 0 |
| Win rate | **69.2%** |
| Gains totaux | +59.4501 USDT |
| Pertes totales | -22.0365 USDT |
| **PNL net** | **+37.4136 USDT** |
| BPS moyen | 8.53 |

**Meilleur trade:** +6.5480 USDT
**Pire trade:** -6.2272 USDT

**Direction:** BUY (39)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| 0.80640583 | 2 |
| 1.74602170 | 1 |
| 1.74631150 | 1 |
| 0.53685542 | 1 |
| 0.53658259 | 1 |

**Cycles SKIP:** 1132
| Raison | Nb |
|--------|-----|
| gap_guard_pause | 779 |
| regime_gate | 176 |
| impulse_resonance_wait | 66 |
| duo_wait | 39 |
| tactic_mismatch | 31 |

---

## SYNTHÈSE

| Indicateur | BETA | ALPHA | TOTAL |
|------------|------|-------|-------|
| Trades | 64 | 39 | 103 |
| PnL | -16.4899 | +37.4136 | **+20.9237** |
| Win rate | 39.1% | 69.2% | 50.5% |

## IRM — régimes de tension (proxy, lecture seule)

> Pas un modèle ARCH Engle. Classification sur `tension=` des cycles BETA. N'influence pas le moteur. Seuils: COMPRESSÉ `< 0.05` · CLUSTER `≥ 1.0` · sinon TRANSITOIRE.

| Régime | Cycles | % temps | Fills | PnL fills (USDT) |
|--------|--------|---------|-------|------------------|
| COMPRESSÉ (attente à froid) | 1150 | 94.5% | 64 | -16.4899 |
| TRANSITOIRE (bruit retail) | 60 | 4.9% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 7 | 0.6% | 0 | +0.0000 |

- Fenêtre: `2026-08-21T19:45:49Z` → `2026-08-21T23:21:25Z` (1217 cycles) · μ(tension)=0.0511 · σ=0.3749 · courant(proxy)=**COMPRESSÉ (attente à froid)**
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

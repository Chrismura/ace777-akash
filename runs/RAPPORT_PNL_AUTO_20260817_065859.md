# RAPPORT PNL AUTO — MASTER_VORTEX_V2_COLLAB_4H

**Session:** `MASTER_VORTEX_V2_COLLAB_4H`
**Période:** 2026-08-16T19:08:40Z → 2026-08-17T06:58:46Z (11h50m)
**Setup:** `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt` | BETA `200` USDT | ALPHA `800` USDT | LLM gate `TRUE` fail_closed=`TRUE`
**Généré:** 2026-08-17T06:58:59Z UTC
**Filtre session:** `ts >= 2026-08-16T19:08:26Z` (lignes CSV antérieures exclues)

---

## BILAN GLOBAL

| Métrique | Valeur |
|----------|--------|
| **PNL BETA** | **+0.4979 USDT** |
| **PNL ALPHA** | **+0.0000 USDT** |
| **PNL SESSION TOTAL** | **+0.4979 USDT** |
| Statut | `POSITIF` |

---

## BETA — BETA (SCOUT x5)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 303 |
| Gagnants | 130 |
| Perdants | 130 |
| Flat (0) | 43 |
| Win rate | **42.9%** |
| Gains totaux | +12.3116 USDT |
| Pertes totales | -11.8137 USDT |
| **PNL net** | **+0.4979 USDT** |
| BPS moyen | -0.16 |

**Meilleur trade:** +0.9290 USDT
**Pire trade:** -1.0109 USDT

**Direction:** SELL (303)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| shock_inversion_stop | 167 |
| fluid_exit_inversion | 87 |
| fluid_exit_brake | 47 |
| shock_exit_10bps | 2 |

**Cycles SKIP:** 2775
| Raison | Nb |
|--------|-----|
| radar_block | 2130 |
| impulse_resonance_wait | 382 |
| price_stasis | 150 |
| gap_guard_pause | 64 |
| tactic_mismatch | 33 |

---

## ALPHA — ALPHA (HUNTER x13)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 0 |
| **PNL net** | **0.0000 USDT** |

*ALPHA n'a pas exécuté de trade — vérifier duo_wait, radar, stase, llm_gate dans les SKIP.*

**Cycles SKIP:** 3118
| Raison | Nb |
|--------|-----|
| radar_block | 2181 |
| impulse_resonance_wait | 501 |
| duo_wait | 359 |
| tactic_mismatch | 40 |
| price_stasis | 37 |

---

## SYNTHÈSE

| Indicateur | BETA | ALPHA | TOTAL |
|------------|------|-------|-------|
| Trades | 303 | 0 | 303 |
| PnL | +0.4979 | +0.0000 | **+0.4979** |
| Win rate | 42.9% | — | 42.9% |

## IRM — régimes de tension (proxy, lecture seule)

> Pas un modèle ARCH Engle. Classification sur `tension=` des cycles BETA. N'influence pas le moteur. Seuils: COMPRESSÉ `< 0.05` · CLUSTER `≥ 1.0` · sinon TRANSITOIRE.

| Régime | Cycles | % temps | Fills | PnL fills (USDT) |
|--------|--------|---------|-------|------------------|
| COMPRESSÉ (attente à froid) | 2066 | 67.1% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 549 | 17.8% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 465 | 15.1% | 303 | +0.4979 |

- Fenêtre: `2026-08-16T19:08:40Z` → `2026-08-17T06:58:46Z` (3080 cycles) · μ(tension)=0.5987 · σ=1.5977 · courant(proxy)=**COMPRESSÉ (attente à froid)**
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

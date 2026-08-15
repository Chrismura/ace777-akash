# RAPPORT PNL AUTO — MASTER_VORTEX_V2_COLLAB_4H

**Session:** `MASTER_VORTEX_V2_COLLAB_4H`
**Période:** 2026-08-14T10:32:47Z → 2026-08-14T10:52:20Z (0h19m)
**Setup:** `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt` | BETA `200` USDT | ALPHA `800` USDT | LLM gate `TRUE` fail_closed=`TRUE`
**Généré:** 2026-08-14T10:52:22Z UTC
**Filtre session:** `ts >= 2026-08-14T10:32:38Z` (lignes CSV antérieures exclues)

---

## BILAN GLOBAL

| Métrique | Valeur |
|----------|--------|
| **PNL BETA** | **+0.5630 USDT** |
| **PNL ALPHA** | **+0.0000 USDT** |
| **PNL SESSION TOTAL** | **+0.5630 USDT** |
| Statut | `POSITIF` |

---

## BETA — BETA (SCOUT x5)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 15 |
| Gagnants | 6 |
| Perdants | 1 |
| Flat (0) | 8 |
| Win rate | **40.0%** |
| Gains totaux | +0.5661 USDT |
| Pertes totales | -0.0031 USDT |
| **PNL net** | **+0.5630 USDT** |
| BPS moyen | 0.26 |

**Meilleur trade:** +0.2586 USDT
**Pire trade:** -0.0031 USDT

**Direction:** SELL (15)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| shock_inversion_stop | 14 |
| fluid_exit_inversion | 1 |

**Cycles SKIP:** 118
| Raison | Nb |
|--------|-----|
| radar_block | 107 |
| impulse_resonance_wait | 10 |
| stase_ecoute | 1 |

---

## ALPHA — ALPHA (HUNTER x13)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 0 |
| **PNL net** | **0.0000 USDT** |

*ALPHA n'a pas exécuté de trade — vérifier duo_wait, radar, stase, llm_gate dans les SKIP.*

**Cycles SKIP:** 147
| Raison | Nb |
|--------|-----|
| radar_block | 111 |
| impulse_resonance_wait | 19 |
| duo_wait | 16 |
| tactic_mismatch | 1 |

---

## SYNTHÈSE

| Indicateur | BETA | ALPHA | TOTAL |
|------------|------|-------|-------|
| Trades | 15 | 0 | 15 |
| PnL | +0.5630 | +0.0000 | **+0.5630** |
| Win rate | 40.0% | — | 40.0% |

## IRM — régimes de tension (proxy, lecture seule)

> Pas un modèle ARCH Engle. Classification sur `tension=` des cycles BETA. N'influence pas le moteur. Seuils: COMPRESSÉ `< 0.05` · CLUSTER `≥ 1.0` · sinon TRANSITOIRE.

| Régime | Cycles | % temps | Fills | PnL fills (USDT) |
|--------|--------|---------|-------|------------------|
| COMPRESSÉ (attente à froid) | 97 | 72.9% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 21 | 15.8% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 15 | 11.3% | 15 | +0.5630 |

- Fenêtre: `2026-08-14T10:32:47Z` → `2026-08-14T10:52:16Z` (133 cycles) · μ(tension)=0.5434 · σ=1.6915 · courant(proxy)=**COMPRESSÉ (attente à froid)**
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

# RAPPORT PNL AUTO — MASTER_VORTEX_V2_COLLAB_4H

**Session:** `MASTER_VORTEX_V2_COLLAB_4H`
**Période:** 2026-08-16T15:02:37Z → 2026-08-16T15:04:05Z (0h01m)
**Setup:** `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt` | BETA `200` USDT | ALPHA `800` USDT | LLM gate `TRUE` fail_closed=`TRUE`
**Généré:** 2026-08-16T15:04:10Z UTC
**Filtre session:** `ts >= 2026-08-16T15:02:00Z` (lignes CSV antérieures exclues)

---

## BILAN GLOBAL

| Métrique | Valeur |
|----------|--------|
| **PNL BETA** | **+0.0000 USDT** |
| **PNL ALPHA** | **+0.0000 USDT** |
| **PNL SESSION TOTAL** | **+0.0000 USDT** |
| Statut | `NEUTRE` |

---

## BETA — BETA (SCOUT x5)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 0 |
| Gagnants | 0 |
| Perdants | 0 |
| Flat (0) | 0 |
| Win rate | **—** |
| Gains totaux | +0.0000 USDT |
| Pertes totales | +0.0000 USDT |
| **PNL net** | **+0.0000 USDT** |
| BPS moyen | — |

**Direction:** —

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| _aucun trade_ | 0 |

**Cycles SKIP:** 5
| Raison | Nb |
|--------|-----|
| gap_guard_pause | 3 |
| radar_block | 2 |

---

## ALPHA — ALPHA (HUNTER x13)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 0 |
| **PNL net** | **0.0000 USDT** |

*ALPHA n'a pas exécuté de trade — vérifier duo_wait, radar, stase, llm_gate dans les SKIP.*

**Cycles SKIP:** 2
| Raison | Nb |
|--------|-----|
| duo_wait | 1 |
| radar_block | 1 |

---

## SYNTHÈSE

| Indicateur | BETA | ALPHA | TOTAL |
|------------|------|-------|-------|
| Trades | 0 | 0 | 0 |
| PnL | +0.0000 | +0.0000 | **+0.0000** |
| Win rate | — | — | — |

## IRM — régimes de tension (proxy, lecture seule)

> Pas un modèle ARCH Engle. Classification sur `tension=` des cycles BETA. N'influence pas le moteur. Seuils: COMPRESSÉ `< 0.05` · CLUSTER `≥ 1.0` · sinon TRANSITOIRE.

| Régime | Cycles | % temps | Fills | PnL fills (USDT) |
|--------|--------|---------|-------|------------------|
| COMPRESSÉ (attente à froid) | 5 | 100.0% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 0 | 0.0% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 0 | 0.0% | 0 | +0.0000 |

- Fenêtre: `2026-08-16T15:02:37Z` → `2026-08-16T15:04:01Z` (5 cycles) · μ(tension)=0.0000 · σ=0.0000 · courant(proxy)=**COMPRESSÉ (attente à froid)**
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

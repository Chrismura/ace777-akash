# RAPPORT PNL AUTO — MASTER_VORTEX_V2_COLLAB_4H

**Session:** `MASTER_VORTEX_V2_COLLAB_4H`
**Période:** 2026-08-21T07:39:21Z → 2026-08-21T07:40:18Z (0h00m)
**Setup:** `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt` | BETA `200` USDT | ALPHA `800` USDT | LLM gate `TRUE` fail_closed=`TRUE`
**Généré:** 2026-08-21T07:40:20Z UTC
**Filtre session:** `ts >= 2026-08-21T07:39:10Z` (lignes CSV antérieures exclues)

---

## BILAN GLOBAL

| Métrique | Valeur |
|----------|--------|
| **PNL BETA** | **-1.3847 USDT** |
| **PNL ALPHA** | **+4.2415 USDT** |
| **PNL SESSION TOTAL** | **+2.8568 USDT** |
| Statut | `POSITIF` |

---

## BETA — BETA (SCOUT x5)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 2 |
| Gagnants | 0 |
| Perdants | 2 |
| Flat (0) | 0 |
| Win rate | **0.0%** |
| Gains totaux | +0.0000 USDT |
| Pertes totales | -1.3847 USDT |
| **PNL net** | **-1.3847 USDT** |
| BPS moyen | -4.61 |

**Meilleur trade:** -0.1018 USDT
**Pire trade:** -1.2829 USDT

**Direction:** SELL (2)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| 1.28994597 | 1 |
| 0.64242696 | 1 |

**Cycles SKIP:** 1
| Raison | Nb |
|--------|-----|
| radar_block | 1 |

---

## ALPHA — ALPHA (HUNTER x13)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 1 |
| Gagnants | 1 |
| Perdants | 0 |
| Flat (0) | 0 |
| Win rate | **100.0%** |
| Gains totaux | +4.2415 USDT |
| Pertes totales | +0.0000 USDT |
| **PNL net** | **+4.2415 USDT** |
| BPS moyen | 10.62 |

**Meilleur trade:** +4.2415 USDT
**Pire trade:** +4.2415 USDT

**Direction:** BUY (1)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| 3.19650487 | 1 |

**Cycles SKIP:** 3
| Raison | Nb |
|--------|-----|
| radar_block | 2 |
| duo_wait | 1 |

---

## SYNTHÈSE

| Indicateur | BETA | ALPHA | TOTAL |
|------------|------|-------|-------|
| Trades | 2 | 1 | 3 |
| PnL | -1.3847 | +4.2415 | **+2.8568** |
| Win rate | 0.0% | 100.0% | 33.3% |

## IRM — régimes de tension (proxy, lecture seule)

> Pas un modèle ARCH Engle. Classification sur `tension=` des cycles BETA. N'influence pas le moteur. Seuils: COMPRESSÉ `< 0.05` · CLUSTER `≥ 1.0` · sinon TRANSITOIRE.

| Régime | Cycles | % temps | Fills | PnL fills (USDT) |
|--------|--------|---------|-------|------------------|
| COMPRESSÉ (attente à froid) | 3 | 100.0% | 2 | -1.3847 |
| TRANSITOIRE (bruit retail) | 0 | 0.0% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 0 | 0.0% | 0 | +0.0000 |

- Fenêtre: `2026-08-21T07:39:21Z` → `2026-08-21T07:40:15Z` (3 cycles) · μ(tension)=0.0000 · σ=0.0000 · courant(proxy)=**COMPRESSÉ (attente à froid)**
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

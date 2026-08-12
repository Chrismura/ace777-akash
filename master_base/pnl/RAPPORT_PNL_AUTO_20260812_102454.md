# RAPPORT PNL AUTO — NUAGE_TEST_8H_CMP3

**Session:** `NUAGE_TEST_8H_CMP3`
**Période:** 2026-08-02T18:18:24Z → 2026-08-02T19:54:01Z (1h35m)
**Setup:** `vide_froid_binance` v`V2.2.1_NO_SUICIDE` | BETA `200` USDT | ALPHA `800` USDT | LLM gate `TRUE` fail_closed=`TRUE`
**Généré:** 2026-08-12T10:24:54Z UTC
**Filtre session:** `ts >= 2026-08-02T18:18:13Z` (lignes CSV antérieures exclues)

---

## BILAN GLOBAL

| Métrique | Valeur |
|----------|--------|
| **PNL BETA** | **-0.0047 USDT** |
| **PNL ALPHA** | **+0.0000 USDT** |
| **PNL SESSION TOTAL** | **-0.0047 USDT** |
| Statut | `NEGATIF` |

---

## BETA — BETA (SCOUT x5)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 1 |
| Gagnants | 0 |
| Perdants | 1 |
| Flat (0) | 0 |
| Win rate | **0.0%** |
| Gains totaux | +0.0000 USDT |
| Pertes totales | -0.0047 USDT |
| **PNL net** | **-0.0047 USDT** |
| BPS moyen | -0.05 |

**Meilleur trade:** -0.0047 USDT
**Pire trade:** -0.0047 USDT

**Direction:** SELL (1)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| fluid_exit_inversion | 1 |

**Cycles SKIP:** 584
| Raison | Nb |
|--------|-----|
| radar_block | 575 |
| vacuum_filter | 6 |
| impulse_resonance_wait | 3 |

---

## ALPHA — ALPHA (HUNTER x13)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 0 |
| **PNL net** | **0.0000 USDT** |

*ALPHA n'a pas exécuté de trade — vérifier duo_wait, radar, stase, llm_gate dans les SKIP.*

**Cycles SKIP:** 546
| Raison | Nb |
|--------|-----|
| radar_block | 539 |
| vacuum_filter | 4 |
| impulse_resonance_wait | 3 |

---

## SYNTHÈSE

| Indicateur | BETA | ALPHA | TOTAL |
|------------|------|-------|-------|
| Trades | 1 | 0 | 1 |
| PnL | -0.0047 | +0.0000 | **-0.0047** |
| Win rate | 0.0% | — | 0.0% |

## IRM — régimes de tension (proxy, lecture seule)

> Pas un modèle ARCH Engle. Classification sur `tension=` des cycles BETA. N'influence pas le moteur. Seuils: COMPRESSÉ `< 0.05` · CLUSTER `≥ 1.0` · sinon TRANSITOIRE.

| Régime | Cycles | % temps | Fills | PnL fills (USDT) |
|--------|--------|---------|-------|------------------|
| COMPRESSÉ (attente à froid) | 563 | 96.2% | 0 | +0.0000 |
| TRANSITOIRE (bruit retail) | 15 | 2.6% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 7 | 1.2% | 1 | -0.0047 |

- Fenêtre: `2026-08-02T18:18:24Z` → `2026-08-02T19:53:40Z` (585 cycles) · μ(tension)=0.0392 · σ=0.4077 · courant(proxy)=**COMPRESSÉ (attente à froid)**
- Source: `NUAGE_TEST_8H_CMP3_BETA_X5.csv`

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

*Rapport auto — CSV: `NUAGE_TEST_8H_CMP3_BETA_X5.csv` | `NUAGE_TEST_8H_CMP3_ALPHA_X13_BURST13.csv`*
*STATE: `runs/STATE.md`*

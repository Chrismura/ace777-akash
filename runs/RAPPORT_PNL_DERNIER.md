# RAPPORT PNL AUTO — MASTER_VORTEX_V2_COLLAB_4H

**Session:** `MASTER_VORTEX_V2_COLLAB_4H`
**Période:** 2026-08-20T18:50:45Z → 2026-08-20T19:13:10Z (0h22m)
**Setup:** `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt` | BETA `200` USDT | ALPHA `800` USDT | LLM gate `TRUE` fail_closed=`TRUE`
**Généré:** 2026-08-20T19:13:14Z UTC
**Filtre session:** `ts >= 2026-08-20T18:50:34Z` (lignes CSV antérieures exclues)

---

## BILAN GLOBAL

| Métrique | Valeur |
|----------|--------|
| **PNL BETA** | **+2.2137 USDT** |
| **PNL ALPHA** | **-1.1247 USDT** |
| **PNL SESSION TOTAL** | **+1.0889 USDT** |
| Statut | `POSITIF` |

---

## BETA — BETA (SCOUT x5)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 17 |
| Gagnants | 9 |
| Perdants | 7 |
| Flat (0) | 1 |
| Win rate | **52.9%** |
| Gains totaux | +2.4237 USDT |
| Pertes totales | -0.2100 USDT |
| **PNL net** | **+2.2137 USDT** |
| BPS moyen | 1.49 |

**Meilleur trade:** +1.4406 USDT
**Pire trade:** -0.1027 USDT

**Direction:** SELL (17)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| 0.39381030 | 1 |
| 1.29410468 | 1 |
| 0.38849977 | 1 |
| 0.38841883 | 1 |
| 0.39416934 | 1 |

**Cycles SKIP:** 72
| Raison | Nb |
|--------|-----|
| radar_block | 56 |
| impulse_resonance_wait | 13 |
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
| Gains totaux | +0.8707 USDT |
| Pertes totales | -1.9955 USDT |
| **PNL net** | **-1.1247 USDT** |
| BPS moyen | -0.33 |

**Meilleur trade:** +0.5106 USDT
**Pire trade:** -1.3372 USDT

**Direction:** BUY (9)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| 2.39915318 | 2 |
| 2.39943139 | 1 |
| 1.19427758 | 1 |
| 1.59829613 | 1 |
| 2.39650358 | 1 |

**Cycles SKIP:** 89
| Raison | Nb |
|--------|-----|
| radar_block | 68 |
| impulse_resonance_wait | 13 |
| tactic_mismatch | 4 |
| duo_wait | 3 |
| stase_ecoute | 1 |

---

## SYNTHÈSE

| Indicateur | BETA | ALPHA | TOTAL |
|------------|------|-------|-------|
| Trades | 17 | 9 | 26 |
| PnL | +2.2137 | -1.1247 | **+1.0889** |
| Win rate | 52.9% | 33.3% | 46.2% |

## IRM — régimes de tension (proxy, lecture seule)

> Pas un modèle ARCH Engle. Classification sur `tension=` des cycles BETA. N'influence pas le moteur. Seuils: COMPRESSÉ `< 0.05` · CLUSTER `≥ 1.0` · sinon TRANSITOIRE.

| Régime | Cycles | % temps | Fills | PnL fills (USDT) |
|--------|--------|---------|-------|------------------|
| COMPRESSÉ (attente à froid) | 73 | 82.0% | 17 | +2.2137 |
| TRANSITOIRE (bruit retail) | 16 | 18.0% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 0 | 0.0% | 0 | +0.0000 |

- Fenêtre: `2026-08-20T18:50:45Z` → `2026-08-20T19:13:10Z` (89 cycles) · μ(tension)=0.0972 · σ=0.2275 · courant(proxy)=**COMPRESSÉ (attente à froid)**
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

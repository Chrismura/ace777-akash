# RAPPORT PNL AUTO — MASTER_VORTEX_V2_COLLAB_4H

**Session:** `MASTER_VORTEX_V2_COLLAB_4H`
**Période:** 2026-08-22T11:34:06Z → 2026-08-22T12:56:02Z (1h21m)
**Setup:** `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt` | BETA `200` USDT | ALPHA `800` USDT | LLM gate `TRUE` fail_closed=`TRUE`
**Généré:** 2026-08-22T12:56:18Z UTC
**Filtre session:** `ts >= 2026-08-22T11:33:19Z` (lignes CSV antérieures exclues)

---

## BILAN GLOBAL

| Métrique | Valeur |
|----------|--------|
| **PNL BETA** | **-0.1959 USDT** |
| **PNL ALPHA** | **+4.6264 USDT** |
| **PNL SESSION TOTAL** | **+4.4305 USDT** |
| Statut | `POSITIF` |

---

## BETA — BETA (SCOUT x5)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 9 |
| Gagnants | 3 |
| Perdants | 5 |
| Flat (0) | 1 |
| Win rate | **33.3%** |
| Gains totaux | +0.9319 USDT |
| Pertes totales | -1.1278 USDT |
| **PNL net** | **-0.1959 USDT** |
| BPS moyen | -0.42 |

**Meilleur trade:** +0.5689 USDT
**Pire trade:** -0.6594 USDT

**Direction:** SELL (9)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| 0.64345965 | 1 |
| 0.39489485 | 1 |
| 0.39493478 | 1 |
| 0.39535974 | 1 |
| 0.64270918 | 1 |

**Cycles SKIP:** 193
| Raison | Nb |
|--------|-----|
| gap_guard_pause | 141 |
| regime_gate | 33 |
| impulse_resonance_wait | 14 |
| stase_ecoute | 3 |
| radar_block | 2 |

---

## ALPHA — ALPHA (HUNTER x13)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 7 |
| Gagnants | 6 |
| Perdants | 0 |
| Flat (0) | 1 |
| Win rate | **85.7%** |
| Gains totaux | +4.6264 USDT |
| Pertes totales | +0.0000 USDT |
| **PNL net** | **+4.6264 USDT** |
| BPS moyen | 5.37 |

**Meilleur trade:** +2.4232 USDT
**Pire trade:** +0.0000 USDT

**Direction:** BUY (7)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| 1.61707029 | 1 |
| 0.40106508 | 1 |
| 0.80890928 | 1 |
| 0.80937145 | 1 |
| 0.80382952 | 1 |

**Cycles SKIP:** 151
| Raison | Nb |
|--------|-----|
| gap_guard_pause | 117 |
| regime_gate | 22 |
| impulse_resonance_wait | 6 |
| radar_block | 4 |
| duo_wait | 2 |

---

## SYNTHÈSE

| Indicateur | BETA | ALPHA | TOTAL |
|------------|------|-------|-------|
| Trades | 9 | 7 | 16 |
| PnL | -0.1959 | +4.6264 | **+4.4305** |
| Win rate | 33.3% | 85.7% | 56.2% |

## IRM — régimes de tension (proxy, lecture seule)

> Pas un modèle ARCH Engle. Classification sur `tension=` des cycles BETA. N'influence pas le moteur. Seuils: COMPRESSÉ `< 0.05` · CLUSTER `≥ 1.0` · sinon TRANSITOIRE.

| Régime | Cycles | % temps | Fills | PnL fills (USDT) |
|--------|--------|---------|-------|------------------|
| COMPRESSÉ (attente à froid) | 186 | 92.1% | 9 | -0.1959 |
| TRANSITOIRE (bruit retail) | 16 | 7.9% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 0 | 0.0% | 0 | +0.0000 |

- Fenêtre: `2026-08-22T11:38:07Z` → `2026-08-22T12:56:02Z` (202 cycles) · μ(tension)=0.0489 · σ=0.1792 · courant(proxy)=**COMPRESSÉ (attente à froid)**
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

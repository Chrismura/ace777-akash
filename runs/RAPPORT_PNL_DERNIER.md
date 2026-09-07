# RAPPORT PNL AUTO — MASTER_BASE_V8_6_FORTRESS_1H30

**Session:** `MASTER_BASE_V8_6_FORTRESS_1H30`
**run_id:** `MASTER_BASE_V8_6_FORTRESS_1H30_20260907T210011Z_9797`
**Frais Binance:** `UNMATCHED_BINANCE_FEES` (aucune commission/funding externe n'est ajoutée sans correspondance explicite)
**Période:** 2026-09-07T21:00:23Z → 2026-09-07T22:30:16Z (1h29m)
**Setup:** `?` v`?` | BETA `200` USDT | ALPHA `800` USDT | LLM gate `?` fail_closed=`?`
**Généré:** 2026-09-07T22:30:18Z UTC
**Filtre session:** `ts >= 2026-09-07T21:00:13Z` (lignes CSV antérieures exclues)

---

## BILAN GLOBAL

| Métrique | Valeur |
|----------|--------|
| PNL brut BETA | +2.1619 USDT |
| Frais BETA | +9.5209 USDT |
| **PNL net BETA** | **-7.3590 USDT** |
| PNL brut ALPHA | -3.0685 USDT |
| Frais ALPHA | +6.4615 USDT |
| **PNL net ALPHA** | **-9.5300 USDT** |
| **PNL SESSION TOTAL** | **-16.8890 USDT** |
| Statut | `NEGATIF` |

---

## BETA — BETA (SCOUT x5)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 18 |
| Gagnants | 2 |
| Perdants | 16 |
| Flat (0) | 0 |
| Win rate | **11.1%** |
| Gains totaux | +0.3694 USDT |
| Pertes totales | -7.7284 USDT |
| PNL brut | +2.1619 USDT |
| Frais | +9.5209 USDT |
| **PNL net** | **-7.3590 USDT** |
| BPS moyen | 1.59 |

**Meilleur trade:** +0.2278 USDT
**Pire trade:** -1.0139 USDT

**Direction:** SELL (18)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| timeout | 9 |
| exit_fatigue | 8 |
| kill_switch | 1 |

**Cycles SKIP:** 499
| Raison | Nb |
|--------|-----|
| reason=COMPRESSE tension=0.00000000 threshold=0.05 | 170 |
| reason=COMPRESSE tension=0.00001169 threshold=0.05 | 4 |
| reason=COMPRESSE tension=0.00001998 threshold=0.05 | 4 |
| reason=COMPRESSE tension=0.00001608 threshold=0.05 | 3 |
| reason=COMPRESSE tension=0.00002095 threshold=0.05 | 3 |

---

## ALPHA — ALPHA (HUNTER x13)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 6 |
| Gagnants | 0 |
| Perdants | 6 |
| Flat (0) | 0 |
| Win rate | **0.0%** |
| Gains totaux | +0.0000 USDT |
| Pertes totales | -9.5300 USDT |
| PNL brut | -3.0685 USDT |
| Frais | +6.4615 USDT |
| **PNL net** | **-9.5300 USDT** |
| BPS moyen | -3.80 |

**Meilleur trade:** -0.8297 USDT
**Pire trade:** -2.4688 USDT

**Direction:** BUY (6)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| exit_fatigue | 3 |
| timeout | 3 |

**Cycles SKIP:** 831
| Raison | Nb |
|--------|-----|
| reason=COMPRESSE tension=0.00000000 threshold=0.05 | 309 |
| reason=no_trigger mode=none | 38 |
| reason=COMPRESSE tension=0.00001608 threshold=0.05 | 3 |
| reason=COMPRESSE tension=0.00001391 threshold=0.05 | 2 |
| reason=COMPRESSE tension=0.00002143 threshold=0.05 | 2 |

---

## SYNTHÈSE

| Indicateur | BETA | ALPHA | TOTAL |
|------------|------|-------|-------|
| Trades | 18 | 6 | 24 |
| PnL | -7.3590 | -9.5300 | **-16.8890** |
| Win rate | 11.1% | 0.0% | 8.3% |

## IRM — régimes de tension (proxy, lecture seule)

> Pas un modèle ARCH Engle. Classification sur `tension=` des cycles BETA. N'influence pas le moteur. Seuils: COMPRESSÉ `< 0.05` · CLUSTER `≥ 1.0` · sinon TRANSITOIRE.

| Régime | Cycles | % temps | Fills | PnL fills (USDT) |
|--------|--------|---------|-------|------------------|
| COMPRESSÉ (attente à froid) | 457 | 87.2% | 18 | +2.1619 |
| TRANSITOIRE (bruit retail) | 64 | 12.2% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 3 | 0.6% | 0 | +0.0000 |

- Fenêtre: `2026-09-07T21:00:23Z` → `2026-09-07T22:30:16Z` (524 cycles) · μ(tension)=0.0616 · σ=0.2301 · courant(proxy)=**COMPRESSÉ (attente à froid)**
- Source: `MASTER_BASE_V8_6_FORTRESS_1H30_BETA_X5.csv`

## Engle — couches évolutives (hors moteur)

- Plan: `engle/PLAN_COUCHES_B1_B3.md`
- Journal B1: `engle/journal/ENGLE_JOURNAL_DERNIER.md` (généré via `engle_journal.rb` / `update_state_md.sh`)
- Adapt B2: `ENGLE_ADAPT=0` (défaut OFF = usine pure ; `log` = posture JSON only)
- Dernière posture log: `WAIT_COLD` · régime `COMPRESSE` · applied=`false`

## CONFIG ACTIVE (snapshot)

- ENTRY_25_75 BETA: `?` | ALPHA: `?`
- SHOCK_EXIT: `?` bps
- VOLATILITY_FILTER: `—`
- STASE: spread=`?` vol=`?`
- POLL_SEC: `?`

---

*Rapport auto — CSV: `MASTER_BASE_V8_6_FORTRESS_1H30_BETA_X5.csv` | `MASTER_BASE_V8_6_FORTRESS_1H30_ALPHA_X13_BURST13.csv`*
*STATE: `runs/STATE.md`*

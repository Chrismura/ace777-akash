# RAPPORT PNL AUTO — ACE_RADAR_ALIGNED_V4_60M

**Session:** `ACE_RADAR_ALIGNED_V4_60M`
**run_id:** `ACE_RADAR_ALIGNED_V4_60M_20260902T000420Z_41201`
**Frais Binance:** `UNMATCHED_BINANCE_FEES` (aucune commission/funding externe n'est ajoutée sans correspondance explicite)
**Période:** 2026-09-02T00:04:30Z → 2026-09-02T01:04:28Z (0h59m)
**Setup:** `?` v`?` | BETA `?` USDT | ALPHA `?` USDT | LLM gate `?` fail_closed=`?`
**Généré:** 2026-09-02T01:04:32Z UTC
**Filtre session:** `ts >= 2026-09-02T00:04:23Z` (lignes CSV antérieures exclues)

---

## BILAN GLOBAL

| Métrique | Valeur |
|----------|--------|
| PNL brut BETA | -5.8093 USDT |
| Frais BETA | +4.7056 USDT |
| **PNL net BETA** | **-10.5149 USDT** |
| PNL brut ALPHA | -3.3131 USDT |
| Frais ALPHA | +4.9776 USDT |
| **PNL net ALPHA** | **-8.2907 USDT** |
| **PNL SESSION TOTAL** | **-18.8056 USDT** |
| Statut | `NEGATIF` |

---

## BETA — BETA (SCOUT x5)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 9 |
| Gagnants | 2 |
| Perdants | 7 |
| Flat (0) | 0 |
| Win rate | **22.2%** |
| Gains totaux | +0.5980 USDT |
| Pertes totales | -11.1129 USDT |
| PNL brut | -5.8093 USDT |
| Frais | +4.7056 USDT |
| **PNL net** | **-10.5149 USDT** |
| BPS moyen | -6.89 |

**Meilleur trade:** +0.5161 USDT
**Pire trade:** -4.4158 USDT

**Direction:** SELL (9)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| stop_loss | 5 |
| timeout | 3 |
| trailing_stop | 1 |

**Cycles SKIP:** 339
| Raison | Nb |
|--------|-----|
| reason=COMPRESSE tension=0.00000000 threshold=0.05 | 152 |
| reason=COMPRESSE tension=0.00000613 threshold=0.05 | 2 |
| reason=COMPRESSE tension=0.01680238 threshold=0.05 | 1 |
| reason=COMPRESSE tension=0.00101623 threshold=0.05 | 1 |
| reason=COMPRESSE tension=0.00001931 threshold=0.05 | 1 |

---

## ALPHA — ALPHA (HUNTER x13)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 5 |
| Gagnants | 0 |
| Perdants | 5 |
| Flat (0) | 0 |
| Win rate | **0.0%** |
| Gains totaux | +0.0000 USDT |
| Pertes totales | -8.2907 USDT |
| PNL brut | -3.3131 USDT |
| Frais | +4.9776 USDT |
| **PNL net** | **-8.2907 USDT** |
| BPS moyen | -5.93 |

**Meilleur trade:** -0.7743 USDT
**Pire trade:** -2.6799 USDT

**Direction:** BUY (5)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| timeout | 2 |
| trailing_stop | 1 |
| stop_loss | 1 |
| kill_switch | 1 |

**Cycles SKIP:** 366
| Raison | Nb |
|--------|-----|
| reason=COMPRESSE tension=0.00000000 threshold=0.05 | 176 |
| reason=no_trigger mode=none | 5 |
| reason=no_state mode=none | 4 |
| reason=COMPRESSE tension=0.00057525 threshold=0.05 | 1 |
| reason=COMPRESSE tension=0.00000855 threshold=0.05 | 1 |

---

## SYNTHÈSE

| Indicateur | BETA | ALPHA | TOTAL |
|------------|------|-------|-------|
| Trades | 9 | 5 | 14 |
| PnL | -10.5149 | -8.2907 | **-18.8056** |
| Win rate | 22.2% | 0.0% | 14.3% |

## IRM — régimes de tension (proxy, lecture seule)

> Pas un modèle ARCH Engle. Classification sur `tension=` des cycles BETA. N'influence pas le moteur. Seuils: COMPRESSÉ `< 0.05` · CLUSTER `≥ 1.0` · sinon TRANSITOIRE.

| Régime | Cycles | % temps | Fills | PnL fills (USDT) |
|--------|--------|---------|-------|------------------|
| COMPRESSÉ (attente à froid) | 261 | 75.0% | 9 | -5.8093 |
| TRANSITOIRE (bruit retail) | 50 | 14.4% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 37 | 10.6% | 0 | +0.0000 |

- Fenêtre: `2026-09-02T00:04:30Z` → `2026-09-02T01:04:25Z` (348 cycles) · μ(tension)=0.4222 · σ=1.2265 · courant(proxy)=**COMPRESSÉ (attente à froid)**
- Source: `ACE_RADAR_ALIGNED_V4_60M_BETA_X5.csv`

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

*Rapport auto — CSV: `ACE_RADAR_ALIGNED_V4_60M_BETA_X5.csv` | `ACE_RADAR_ALIGNED_V4_60M_ALPHA_X13_BURST13.csv`*
*STATE: `runs/STATE.md`*

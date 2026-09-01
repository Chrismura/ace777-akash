# RAPPORT PNL AUTO — ACE_DUO_CLEAN_V4_15M

**Session:** `ACE_DUO_CLEAN_V4_15M`
**run_id:** `ACE_DUO_CLEAN_V4_15M_20260901T160208Z_34195`
**Frais Binance:** `UNMATCHED_BINANCE_FEES` (aucune commission/funding externe n'est ajoutée sans correspondance explicite)
**Période:** 2026-09-01T16:02:18Z → 2026-09-01T16:17:17Z (0h14m)
**Setup:** `?` v`?` | BETA `?` USDT | ALPHA `?` USDT | LLM gate `?` fail_closed=`?`
**Généré:** 2026-09-01T16:17:19Z UTC
**Filtre session:** `ts >= 2026-09-01T16:02:10Z` (lignes CSV antérieures exclues)

---

## BILAN GLOBAL

| Métrique | Valeur |
|----------|--------|
| PNL brut BETA | -4.6029 USDT |
| Frais BETA | +1.1962 USDT |
| **PNL net BETA** | **-5.7991 USDT** |
| PNL brut ALPHA | +0.6228 USDT |
| Frais ALPHA | +1.0772 USDT |
| **PNL net ALPHA** | **-0.4544 USDT** |
| **PNL SESSION TOTAL** | **-6.2535 USDT** |
| Statut | `NEGATIF` |

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
| Pertes totales | -5.7991 USDT |
| PNL brut | -4.6029 USDT |
| Frais | +1.1962 USDT |
| **PNL net** | **-5.7991 USDT** |
| BPS moyen | -28.22 |

**Meilleur trade:** -1.4232 USDT
**Pire trade:** -4.3758 USDT

**Direction:** SELL (2)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| stop_loss | 2 |

**Cycles SKIP:** 104
| Raison | Nb |
|--------|-----|
| reason=COMPRESSE tension=0.00000000 threshold=0.05 | 34 |
| reason=spread_too_wide conf=0.5 mom_sig=1.06849918 raw_mom_bps=0.00000000 spread_bps=41.50140000 tension=1.06849918 bid_drop=6.94524466 ask_drop=0.26761617 swarm=0 | 1 |
| mom=long structure=short | 1 |
| reason=spread_too_wide conf=0.5 mom_sig=2.84403454 raw_mom_bps=0.00000000 spread_bps=10.40030000 tension=2.84403454 bid_drop=18.48622452 ask_drop=0.16780662 swarm=0 | 1 |
| reason=spread_too_wide conf=0.5 mom_sig=2.13510629 raw_mom_bps=0.00000000 spread_bps=40.96460000 tension=2.13510629 bid_drop=13.87819090 ask_drop=0.00000000 swarm=0 | 1 |

---

## ALPHA — ALPHA (HUNTER x13)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 1 |
| Gagnants | 0 |
| Perdants | 1 |
| Flat (0) | 0 |
| Win rate | **0.0%** |
| Gains totaux | +0.0000 USDT |
| Pertes totales | -0.4544 USDT |
| PNL brut | +0.6228 USDT |
| Frais | +1.0772 USDT |
| **PNL net** | **-0.4544 USDT** |
| BPS moyen | 4.63 |

**Meilleur trade:** -0.4544 USDT
**Pire trade:** -0.4544 USDT

**Direction:** BUY (1)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| trailing_stop | 1 |

**Cycles SKIP:** 124
| Raison | Nb |
|--------|-----|
| reason=COMPRESSE tension=0.00000000 threshold=0.05 | 40 |
| reason=no_state mode=none | 2 |
| reason=COMPRESSE tension=0.00092633 threshold=0.05 | 1 |
| reason=COMPRESSE tension=0.00000083 threshold=0.05 | 1 |
| reason=COMPRESSE tension=0.01041051 threshold=0.05 | 1 |

---

## SYNTHÈSE

| Indicateur | BETA | ALPHA | TOTAL |
|------------|------|-------|-------|
| Trades | 2 | 1 | 3 |
| PnL | -5.7991 | -0.4544 | **-6.2535** |
| Win rate | 0.0% | 0.0% | 0.0% |

## IRM — régimes de tension (proxy, lecture seule)

> Pas un modèle ARCH Engle. Classification sur `tension=` des cycles BETA. N'influence pas le moteur. Seuils: COMPRESSÉ `< 0.05` · CLUSTER `≥ 1.0` · sinon TRANSITOIRE.

| Régime | Cycles | % temps | Fills | PnL fills (USDT) |
|--------|--------|---------|-------|------------------|
| COMPRESSÉ (attente à froid) | 63 | 59.4% | 2 | -4.6029 |
| TRANSITOIRE (bruit retail) | 19 | 17.9% | 0 | +0.0000 |
| CLUSTER (tension haute — proxy) | 24 | 22.6% | 0 | +0.0000 |

- Fenêtre: `2026-09-01T16:02:18Z` → `2026-09-01T16:17:17Z` (106 cycles) · μ(tension)=0.6318 · σ=1.3688 · courant(proxy)=**COMPRESSÉ (attente à froid)**
- Source: `ACE_DUO_CLEAN_V4_15M_BETA_X5.csv`

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

*Rapport auto — CSV: `ACE_DUO_CLEAN_V4_15M_BETA_X5.csv` | `ACE_DUO_CLEAN_V4_15M_ALPHA_X13_BURST13.csv`*
*STATE: `runs/STATE.md`*

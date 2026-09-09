# RAPPORT PNL AUTO — MASTER_BASE_V8_6_FORTRESS_8H20

**Session:** `MASTER_BASE_V8_6_FORTRESS_8H20`
**run_id:** `MASTER_BASE_V8_6_FORTRESS_8H20_20260909T085909Z_25898`
**Frais Binance:** `UNMATCHED_BINANCE_FEES` (aucune commission/funding externe n'est ajoutée sans correspondance explicite)
**Période:** 2026-09-09T08:59:18Z → 2026-09-09T17:19:14Z (8h19m)
**Setup:** `?` v`?` | BETA `200` USDT | ALPHA `800` USDT | LLM gate `?` fail_closed=`?`
**Généré:** 2026-09-09T17:19:16Z UTC
**Filtre session:** `ts >= 2026-09-09T08:59:11Z` (lignes CSV antérieures exclues)

---

## BILAN GLOBAL

| Métrique | Valeur |
|----------|--------|
| PNL brut BETA | +0.0000 USDT |
| Frais BETA | +0.0000 USDT |
| **PNL net BETA** | **+0.0000 USDT** |
| PNL brut ALPHA | +0.0000 USDT |
| Frais ALPHA | +0.0000 USDT |
| **PNL net ALPHA** | **+0.0000 USDT** |
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
| PNL brut | +0.0000 USDT |
| Frais | +0.0000 USDT |
| **PNL net** | **+0.0000 USDT** |
| BPS moyen | — |

**Direction:** —

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| _aucun trade_ | 0 |

**Cycles SKIP:** 0
| Raison | Nb |
|--------|-----|
| _aucun_ | 0 |

---

## ALPHA — ALPHA (HUNTER x13)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 0 |
| **PNL net** | **0.0000 USDT** |

*ALPHA n'a pas exécuté de trade — vérifier duo_wait, radar, stase, llm_gate dans les SKIP.*

**Cycles SKIP:** 5612
| Raison | Nb |
|--------|-----|
| reason=COMPRESSE tension=0.00000000 threshold=0.05 | 1444 |
| reason=no_state mode=none | 539 |
| mom=long structure=short | 25 |
| mom=short structure=long | 19 |
| reason=COMPRESSE tension=0.00001454 threshold=0.05 | 4 |

---

## SYNTHÈSE

| Indicateur | BETA | ALPHA | TOTAL |
|------------|------|-------|-------|
| Trades | 0 | 0 | 0 |
| PnL | +0.0000 | +0.0000 | **+0.0000** |
| Win rate | — | — | — |

## IRM — régimes de tension (proxy, lecture seule)

> Pas un modèle ARCH Engle. Classification sur `tension=` des cycles BETA. N'influence pas le moteur. Seuils: COMPRESSÉ `< 0.05` · CLUSTER `≥ 1.0` · sinon TRANSITOIRE.

*Aucun cycle dans la fenêtre session — IRM indisponible.*

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

*Rapport auto — CSV: `MASTER_BASE_V8_6_FORTRESS_8H20_BETA_X5.csv` | `MASTER_BASE_V8_6_FORTRESS_8H20_ALPHA_X13_BURST13.csv`*
*STATE: `runs/STATE.md`*

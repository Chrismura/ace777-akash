# Éval #15 — Kimi · revue architecture Risk / WARM / DR

**Source :** réponse Kimi sur `tech.html` / C1–C6  
**Date :** 2026-07-30  
**Verdict reviewer :** KEEP-WITH-FIXES (« digne d’un hedge fund early-stage »)  
**Action Index :** intégrée dans `architecture/tech.html` §7–9 · C7/C8 · `BUDGET_API.md`

## Tableau gaps

| # | Manque | Où | Prio | Statut ACE777 |
|---|--------|----|------|---------------|
| 1 | Risk Guardian | entre HOT et BOARD | Haute | Spec + lane GUARD · prototype existant · **pas en vol** (GO futur) |
| 2 | Circuit breaker DD combiné ACE+Hulk | C7 | Haute | Constraint ajoutée · seuil X% = décision humaine |
| 3 | Couche WARM | HOT↔COLD | Moyenne | Labelé (Hulk gates, veille_status, Cortana horaire, Guardian) |
| 4 | Backup / DR | C8 | Moyenne | Spec §8 · `/tmp` volatile OK |
| 5 | Budget API | C5 / BUDGET_API.md | Basse | Stub créé |

## Règles gardées

- Kill switch only · **no order** · **no genesis touch**
- Risk Guardian ≠ silent GO
- WARM lit le HOT, n’écrit pas les fills

## Suite (GO humain)

| Fix | Statut 2026-07-30 |
|-----|-------------------|
| P1 atomic write | ✅ CLOSED — note + writers OK |
| P2 `MAX_GLOBAL_DD_PCT=8` | ✅ `config_risk_warm.env` · [[RISK_C7]] |
| P3 Cortana URGENT | ✅ alert/poll + launchd 60s |

Encore ouvert : brancher Risk Guardian WARM sur C7 (kill soft + `cortana_thermo.py alert`).

[[ARCHITECTURE_TECH]] · [[BUDGET_API]] · [[01_TABLEAU_VIVANT]]

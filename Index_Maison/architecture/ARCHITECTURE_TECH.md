# ACE777 — Architecture TECH (revue IA)

**Statut :** 🟢 canon technique · twin de `architecture/tech.html`  
**Date :** 2026-07-31 (Δ après 30 juil.)  
**Public :** IA / expert externe qui doit **évaluer** (pas seulement s’orienter)  
**Vue humaine :** `architecture/index.html` · [[ARCHITECTURE_AGORA]]

Ouvrir la page :
```bash
open ~/ace777-test-day1/Index_Maison/architecture/tech.html
```

---

## 0. Constraints (non-négociables)

| ID | Constraint | Implication reviewer |
|----|------------|----------------------|
| C1 | Champion genesis `37fca367…` intangible | Wrappers / molettes only — never patch genesis |
| C2 | 0 LLM in hot trading path | Reject Ollama/Claude inside ACE fill loop |
| C3 | 1 GO = 1 flight · trading never implicit | Obsidian/Index must not auto-fire orders |
| C4 | Fills CSV = ground truth | Score vs CSV, not narrative |
| C5 | Mac Air M1 **8 Go** · no paid APIs default | Penalize heavy multiplex / RAG+9 agents during ACE |
| C6 | Anti-overdose · 1 place / info | Route into canons — don’t invent file piles |
| C7 | Combined drawdown ACE+Hulk · **défaut 8%** | `Index_Maison/config_risk_warm.env` · [[RISK_C7]] · Guardian pas en vol |
| C8 | Backup / DR `runs/` + Hulk state | `/tmp/ace777_ram_exchange` volatile → CSV |

---

## 1. Components

| Component | Path / entry | Stack | Lane | Maturity | Contracts |
|-----------|--------------|-------|------|----------|-----------|
| **ACE777** | `~/ace777-test-day1/` · `./GO_USINE_NUAGE.sh [DUR] [TAG]` | Bash + Ruby + HMAC Binance Futures | HOT | lab-prod testnet | `runs/*fills*.csv` · LIVE · STATE · WHY_ARRET · BETA↔ALPHA |
| **Hulk** | `hulk-mexc/scripts/paper_diprip.py` · `digest_watch.py --live` | Python 3.9 stdlib · MEXC public | HOT paper | early paper | seed **20$ / 2 pairs** · universe **15** · soft RED · veille JSON |
| **Cockpit** | `Index_Maison/cockpit/` · `open_cockpit_app.sh` · `:17777` / `:17800` | HTML+JS · bridge · LaunchAgents | WARM ops | zone test | Read-only + STOP · bubbles TOTAL/α/β/Hulk · **no entry** · sync Obsidian ≠ UI |
| **Cortana** | `~/crypto-voice-assistant-core/` · `launch_cortana.sh open` | Rust egui · whisper · Gemini/Ollama | VOICE | app OK · **not** orchestrator | Reads Attention — must not silent-GO |
| **Punk** | `veille-punk/` + COMPTES | scripts / filter X | COLD | semi-auto | Attention · BRIEF |
| **Cursor** | IDE ACTIF/PASSIF | human+agent | COLD | active | Évals · Tableau · MEMOIRE · **speak-simple default** |
| **Index_Maison** | `Index_Maison/` | Markdown + HTML UIs | BOARD | living | Single decision source pre-sync |
| **Obsidian** | `Documents/Obsidian_ACE777/` via `_sync_now.sh` | Markdown · TCC | COFFRE | human memory | **no hot auto** · Cursor cannot write Documents |

**No single `main.py`.**

### Changelog (anti stale review)

| When | Landed | Reviewer note |
|------|--------|---------------|
| **2026-07-31** | `session_debut`/`session_fin` · cockpit app · portfolio HUD · Hulk seed 2×10$ · speak-simple rule · bridge anti-double-bind · thermo last-good | Do **not** review as 30-juil. only |
| 2026-07-30 | tech.html + Kimi KEEP-WITH-FIXES · C7/C8 · veille atomic | Constraints still bind |

---

## 2. Allowed / forbidden edges

**Allowed:** Human GO → ACE/Hulk · fills → post-mortem · validation → éval/tableau/Attention/MEMOIRE → OUTBOX → Obsidian · Punk → Attention · Cortana read bus · Hulk deterministic RED skip · Cockpit read + panic STOP.

**Forbidden:** Obsidian/LLM → order · mutate genesis · LLM in ACE radar/fill · paid APIs as default · 9 cold agents during ACE · Desktop as second truth · Cockpit entry orders.

---

## 3. Data flow

```
[GO] → ACE (testnet) → CSV fills → score
         └─ BETA ↔ ALPHA (intra swarm REAL)
     → Hulk paper → ledger + veille JSON

[ops UI] → Cockpit ← bridge :17777 ← mission.json (CSV/thermo/Hulk state)

[idea] → Cursor → Éval#N → TABLEAU → Attention/MEMOIRE → OUTBOX → Obsidian
                                                              ⇣ cold lessons only
```

---

## 4. Swarm status

| Layer | Status | Mechanism |
|-------|--------|-----------|
| Intra-ACE duo | **REAL** | BETA↔ALPHA |
| Inter-leg | **EMBRYO** | Markdown handoffs / OUTBOX / Swarm_Bus |
| Orchestrator | **ABSENT** | Human + Cursor ; Cortana ≠ chef · Cockpit ≠ GO |

---

## 5. Rubric for external AI

Score:

1. Boundary integrity (HOT/COLD/LLM)  
2. Single source of truth (CSV / Index)  
3. Human-in-loop (GO only)  
4. Resource fit (8 Go)  
5. Handoff quality (Markdown contracts)  
6. Maturity honesty (claimed vs embryonic)  
7. Migration safety (champion intangible)  
8. **Spec freshness** (read Changelog — reject reviews that ignore 31 juil. Δ)

**Output format:**

```
VERDICT: KEEP | KEEP-WITH-FIXES | REWORK
FORCES: …
FAIBLESSES: …
RISQUES: …
PROPOSITIONS (ranked, GO-sized): …
ANTI-PATTERNS REJECTED: …
```

---

## 6. Related canons

- [[ARCHITECTURE_AGORA]] · [[OSSATURE_INDEX]] · [[01_TABLEAU_VIVANT]] · [[AUTO_PROCESSUS]] · [[PREFS_STACK]] · [[JOURNAL_COCKPIT]]
- Root audit: `AUDIT_TROIS_JAMBES_SWARM_20260726.md`
- [[BUDGET_API]] · [[Evaluations/15_kimi_archi_risk_warm]]

---

## 7. Risk & Guardians (Kimi review)

| Guardian | Lane | Trigger | Action |
|----------|------|---------|--------|
| ACE internal | HOT | timer, max loss, STOP | Self stop |
| Hulk stops | HOT | rules paper | Self stop |
| Cockpit STOP | WARM | human confirm | Panic path / stop scripts |
| **Risk Guardian** | **WARM** | DD global, 3 err/10min, Mac orphan | Kill ACE + alert · no order · no genesis |
| Human | BOARD | Any | GO/STOP |

**WARM** = live hors fill loop (gates Hulk, `.veille_status`, scoreur, Cortana horaire, Risk Guardian, Cockpit).

## 8. Backup & DR (spec)

| Asset | Freq | Target |
|-------|------|--------|
| `runs/*.csv` + Hulk state | Daily (spec) | Git sélectif + disque externe |
| `/tmp/ace777_ram_exchange/` | Never | Reconstruct from CSV |
| Obsidian vault | User / iCloud | OUTBOX bridge |

## 9. External review — Kimi 2026-07-30

VERDICT: **KEEP-WITH-FIXES**. Gaps intégrés.

| Fix | Statut |
|-----|--------|
| P1 atomic `.veille_status` | ✅ **CLOSED** — `_safe_write` · writers OK |
| P2 `MAX_GLOBAL_DD_PCT=8` | ✅ constante · [[RISK_C7]] · Guardian pas en vol |
| P3 Cortana URGENT | ✅ `.urgent_alert.json` + poll 60s |

Risk Guardian **pas encore en vol** (WARM kill = GO futur).

**Re-review after 31 juil. Δ** recommended if scoring cockpit / session cadence / Hulk seed.

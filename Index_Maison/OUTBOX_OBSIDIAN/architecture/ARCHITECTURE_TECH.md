# ACE777 — Architecture TECH (revue IA)

**Statut :** 🟢 canon technique · twin de `architecture/tech.html`  
**Date :** 2026-08-12 (Δ 12 août : hub cloud + pont gate + radar + ADA + Cortana V2)  
**Public :** IA / expert externe qui doit **évaluer** (pas seulement s'orienter)  
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
| C6 | Anti-overdose · 1 place / info | Route into canons — don't invent file piles |
| C7 | Combined drawdown ACE+Hulk · **défaut 8%** | `Index_Maison/config_risk_warm.env` · [[RISK_C7]] · Guardian pas en vol |
| C8 | Backup / DR `runs/` + Hulk state | `/tmp/ace777_ram_exchange` volatile → CSV |
| C9 | **0 IA locale nulle part** (depuis 11/08) | Hub cloud = seule passerelle LLM · pont `11439` pour le gate · fail-closed vers règles, jamais qwen-local |
| C10 | Budget cloud quotidien (plafond réglable) | `hub_prise_ia.py` compteur jour · dépassement → bascule gemini (cloud) · jamais local |

---

## 1. Components

| Component | Path / entry | Stack | Lane | Maturity | Contracts |
|-----------|--------------|-------|------|----------|-----------|
| **ACE777** | `~/ace777-test-day1/` · `./GO_USINE_NUAGE.sh [DUR] [TAG]` | Bash + Ruby + HMAC Binance Futures | HOT | lab-prod testnet | `runs/*fills*.csv` · LIVE · STATE · WHY_ARRET · BETA↔ALPHA |
| **Hulk** | `hulk-mexc/scripts/paper_diprip.py` · `digest_watch.py --live` | Python 3.9 stdlib · MEXC public | HOT paper | early paper | seed **20$ / 2 pairs** · universe **15** · soft RED · veille JSON |
| **HUB CLOUD (prise-ia)** | `~/prise-ia/hub_prise_ia.py` · `:11435` | Python stdlib HTTP · routing.json · providers.json | WARM/COLD | prod quotidien | Tâches : `supervise.decision`, `analyste.strategie`, `code.ia`, `cortana.yeux`, `signets.*`, `veille.youtube`, `audit.protocol`… · contexte vivant injecté (6000 car) · compteur budget/jour |
| **PONT GATE (llm_gate_hub_bridge)** | `Index_Maison/scripts/llm_gate_hub_bridge.py` · `:11439` · LaunchAgent `com.ace777.llm-gate-hub` | Python stdlib · cache 90s (réglable `LLM_GATE_PONT_CACHE_SEC`) | WARM | prod (preuve `llm_wind` 12/08) | Gate trades → hub (grok→gemini) · fail-closed 503 → règles, jamais local · redémarrage auto |
| **BUFFY (superviseur)** | session chat (Freebuff) · `MEMOIRE_COLLAB.md` · `POINT_REPRISE_DERNIER.md` | IA superviseur / chef d'orchestre | ORCHESTRATION | toutes sessions | Pilote la flotille (codeur · famille · juge) · specs · run tests · valide avant action · **session — renaît à chaque ouverture, mémoires dans le coffre** · jamais dans le hot path |
| **Vigie temps réel** | `Index_Maison/scripts/vigie_live.py` | WebSocket Binance brut RFC 6455 (BTC/ETH) + RSS news · journal radar | WARM | brique 1 | Seuils : 0,5 %/60s · 2 %/5min · volume ×3 · journal_radar.log → ADA |
| **Analyste** | `Index_Maison/scripts/analyste.py` · `analyste_cadence.sh` | Hub `analyste.strategie` (gemini) · journal des analyses | WARM | brique 2 | `strategie/derniere_analyse.md` · `MEMOIRE_ANALYSTE.md` · `REGISTRE_PREDICTIONS.md` |
| **ADA gardienne + saison** | `Index_Maison/scripts/ada_gardienne.py` · `ada_saison.py` | Python · voilure continue 0–100 (lissée, jamais de saut IF) · zones VERT/JAUNE/ROUGE/PRENDS_LA_PERTE | WARM | brique 3 (live cockpit thermo) | `strategie/ada_gardienne_live.json` · alarme sonore + voix progressive (veilleuse→sirène) |
| **Journal d'intention** | `Index_Maison/scripts/journal_intention.py` | Python · écrit l'intention des bots (pourquoi) | WARM | brique 4 | `strategie/journal_intention_live.json` + `.jsonl` · affiché cockpit |
| **Fiches offres IA** | `Index_Maison/scripts/fiches_offres.py` | Hub `analyste.strategie` · cache atomique · quota 8/jour | COLD/WARM | prod | `strategie/FICHES_OFFRES.json` · cockpit onglet offres |
| **Signets X (lecture IA)** | `Index_Maison/scripts/signets_lecture.py` | Hub `analyste.strategie` · quota 15/jour | COLD | prod | `strategie/SIGNETS_RESUMES.json` · push X → cockpit |
| **Cortana V2** | `Index_Maison/scripts/cortana_brief.py` · `cortana_cockpit_bridge.py` (`:17777`) · `cortana_thermo.py` | Python · edge-tts (voix Vivienne) · oral_fr (nombres en mots) · barge_in (micro coupe la voix) · yeux (vision à la demande) | VOICE | V2 prod | Brief matin (offres + signets) · consultation famille/juge (`/chat`) · `/ecoute` toggle · `.urgent_alert.json` |
| **Cortana yeux** | `Index_Maison/scripts/cortana_yeux.py` | screencapture + sips + hub `cortana.yeux` (gemini vision) | VOICE (à la demande) | prototype | `--speak` / `--image` · jamais en continu, que sur demande |
| **Veille YouTube** | `Index_Maison/scripts/veille_yt.py` | yt-dlp sous-titres + hub `veille.youtube` | COLD | brique | analyse vidéos à la demande, résumé + avis |
| **MiroFish** | `~/mirofis/` · backend `:5001` · front `:3000` · plists `DESACTIVES_2026-08-10/` | Flask Python 3.12 · Vue/Vite · hub NVIDIA NIM (clé ZEP posée ✅) | COLD recherche | **PAUSE budgétaire 10/08** (tournait à vide) | Simulation sociale multi-agents (foule, biais) · **jamais d'exécution** · rapport → `MIROFISH_DONNEES_2026-08-10/` · réactivation = décision collective + `launchctl load` |
| **Cockpit** | `Index_Maison/cockpit/` · `open_cockpit_app.sh` · `:17777` / `:17800` | HTML+JS · bridge · LaunchAgents | WARM ops | zone test → v2 | Read-only + STOP · onglets : graph, stratégie (résumé + offres + exploration), thermo (ADA + voilure), offres (fiches IA), signets, hub · architecture servie `:17800/architecture/` |
| **Obsidian** | `Documents/Obsidian_ACE777/` via `_sync_now.sh` | Markdown · TCC | COFFRE | human memory | **no hot auto** · Cursor cannot write Documents |

**No single `main.py`.**

---

## 1b. Utiliser les personnages IA (famille · juge · codeur · Cortana) — guide pratique

> ⚠️ Règle d'or (16/08, gravée) : **tout passe par le hub `:11435` via le `task` officiel** — jamais de modèles en dur, jamais de LLM local (C9). Le hub route par personnage, injecte le contexte vivant, applique le budget et l'anti-tempête.

### Les personnages et leur canal (`task`)

| Personnage | Task (canal hub) | Prompt system (gravé) | Rôle |
|---|---|---|---|
| **GEMINI** | `gemini.analyse` | « Auditeur en chef — angles morts, structure » | L'analyste qui voit ce qui manque |
| **DEEPSEEK** | `deepseek.analyse` | « Critique factuel — preuves, contre-exemples » | Refuse les conclusions non étayées |
| **JUGE** | `juge.tranche` | « Tranche formellement : GO / GO AVEC RESERVES / NON » | Le verdict formel |
| **ULTRA** | `inferx.analyse` | « Robustesse à l'échelle — prod, tempête, charge » | Ce qui casse en réel |
| **INFERX** | `inferx.analyse` | « Logique interne — flux, garde-fous, pièges » | Le code au microscope |
| **GROK** | `puter-grok.analyse` | « Pragmatique — ce qui casse en conditions réelles » | Le démon 24/7 |
| **CODEUR** | `code.ia` | « Écrit et vérifie le code — factuel, refuse la fiction » | Produit le code (chaîne provider/fallback/secondary) |
| **CORTANA** | `cortana.analyse` | « ADVISORY — propose, n'applique jamais rien » | L'analyste-maîtresse, voix |

### La CLAUSE PERMANENTE (gravée 16/08, dans TOUS les prompts)

> « Ne te contente PAS de corriger ou de valider : si tu proposes AUTRE CHOSE (approche différente, autre architecture, autre unité) ou une AMÉLIORATION qui a du sens, dis-le explicitement. Corriger n'est pas suffisant : proposer est attendu. »

Elle est injectée dans le `system` de chaque appel par les scripts de consultation (`scripts/consulter_*.py`, `scripts/checkup_*.py`) — plus besoin de la répéter manuellement.

### Le pattern d'une consultation (protocole maison)

```python
# 1. Le payload : task = personnage officiel (JAMAIS model en dur)
payload = {
    "task": "juge.tranche",            # ou gemini.analyse / code.ia / cortana.analyse…
    "messages": [
        {"role": "system", "content": SYSTEM_PERSONNAGE + "\n\n" + CLAUSE},
        {"role": "user", "content": CONTEXTE},   # le brief : faits, code exact, questions
    ],
    "max_tokens": 1400,
    "temperature": 0.3,
}
# 2. POST http://127.0.0.1:11435/v1/chat/completions
# 3. Réponse → OUT = scripts/AVIS_<NOM>.md (ou CONSULTATION_*/)
```

### Le circuit famille (exemple réel : sonde aspiration, 16/08)

```
Buffy (superviseur) construit le brief (faits + code + questions)
    → consulter_famille_*.py : 6 membres (GEMINI, DEEPSEEK, JUGE, ULTRA, INFERX, GROK)
    → consulter_codeur : task code.ia (le codeur écrit/vérifie le code)
    → consulter_cortana : task cortana.analyse (ADVISORY)
    → synthèse Buffy → GO/GO-RÉSERVES/NON consolidé → décision avec Christophe
```

**Règles** :
- Le JUGE tranche formellement, la famille trouve les angles morts, le codeur vérifie le code réel (jamais la fiction).
- Consulter AUX BESOINS, jamais en spam (anti-double : 5 min minimum entre 2 consultations).
- Une consultation = des AVIS dans un dossier `CONSULTATION_*/` + une synthèse écrite.
- **maker ≠ checker** : le JUGE vérifie ce que le codeur produit.

### Scripts de référence (copier le pattern)

| Script | Ce qu'il fait |
|---|---|
| `Index_Maison/scripts/consulter_famille_*.py` | 6 personnages famille via tasks officiels |
| `hulk-mexc/scripts/consulter_codeur_*.py` | Codeur via `task: code.ia` |
| `hulk-mexc/scripts/consulter_cortana_*.py` | Cortana via `task: cortana.analyse` |
| `hulk-mexc/scripts/checkup_codeur_*.py` | Check-up post-implémentation (code réel envoyé) |

**No single `main.py`.**

### Changelog (anti stale review)

| When | Landed | Reviewer note |
|------|--------|---------------|
| **2026-08-16** | **Guide personnages IA §1b** (tasks officiels hub, clause permanente, circuit famille, scripts de référence) · sonde aspiration Hulk (observation 48h, corrélation BTC) · boucle baleines complétée (plist pont-onchain) · carte ONCHAIN cockpit · chantier schéma des index · check-up codeur+famille 7/7 GO-RÉSERVES | C9/C10 appliqués · clause permanente dans tous les prompts |
| **2026-08-12** | **Hub cloud seule passerelle LLM** (pont `11439` pour gate trades, preuve `llm_wind` 12/08, run 4h comparaison hub vs Ollama) · vigie temps réel · analyste · ADA gardienne (voilure + alarme progressive) · journal d'intention · fiches offres IA (quota 8/j) · signets lecture IA (quota 15/j) · Cortana V2 (oral_fr, barge_in, yeux, consultation famille) · onglet stratégie cockpit · point de reprise `POINT_REPRISE_DERNIER.md` | Do **not** review as 31-juil. only — C9/C10 + lane WARM élargie |
| 2026-07-31 | `session_debut`/`session_fin` · cockpit app · portfolio HUD · Hulk seed 2×10$ · speak-simple rule · bridge anti-double-bind · thermo last-good | Do not review as 30-juil. only |
| 2026-07-30 | tech.html + Kimi KEEP-WITH-FIXES · C7/C8 · veille atomic | Constraints still bind |

---

## 2. Allowed / forbidden edges

**Allowed:** Human GO → ACE/Hulk · fills → post-mortem · validation → éval/tableau/Attention/MEMOIRE → OUTBOX → Obsidian · Punk → Attention · Cortana read bus + consult famille/juge (lecture seule) · Hub cloud pour gate/analyste/signets/yeux (pas le fill loop) · Hulk deterministic RED skip · Cockpit read + panic STOP · ADA lit le radar et alerte (ne trade pas).

**Forbidden:** Obsidian/LLM → order · mutate genesis · LLM in ACE radar/fill · paid APIs as default (plafond budget) · **IA locale nulle part** (C9) · 9 cold agents during ACE · Desktop as second truth · Cockpit entry orders · yeux en continu (que sur demande) · **MiroFish en continu** (simulation à la demande seulement, budget).

---

## 3. Data flow

```
[GO] → ACE (testnet) → CSV fills → score
         └─ BETA ↔ ALPHA (intra swarm REAL)
     → Hulk paper → ledger + veille JSON

[RADAR] vigie_live (WebSocket Binance + RSS) → journal_radar.log
     → ADA gardienne → voilure + alarme (son/voix progressive) → cockpit thermo
     → journal d'intention (pourquoi des bots)

[HUB cloud :11435] ← toutes demandes LLM (gate via pont :11439, cache 90s)
     ├─ supervise.decision → gate trades (mode, cohésion) — preuve llm_wind
     ├─ analyste.strategie → analyses + fiches offres + résumés signets
     ├─ code.ia → codeur (SPE/CODE produits par le hub)
     ├─ cortana.yeux → vision (sur demande)
     └─ contexte vivant ARCHITECTURE_VIVANTE.md injecté à chaque appel

[ops UI] → Cockpit ← bridge :17777 ← mission.json / live.json / ada / journal

[idea] → Cursor → Éval#N → TABLEAU → Attention/MEMOIRE → OUTBOX → Obsidian
                                                              ⇣ cold lessons only
```

---

## 4. Swarm status

| Layer | Status | Mechanism |
|-------|--------|-----------|
| Intra-ACE duo | **REAL** | BETA↔ALPHA |
| Hub cloud | **REAL** | prisé tous services LLM · routing.json · providers.json · contexte vivant |
| Radar→ADA→Cockpit | **REAL** | événementiel (changement déclenche, pas l'inverse) |
| MiroFish (simulation foule) | **PAUSE** | à la demande · décision collective requise · clé ZEP OK |
| Inter-leg | **EMBRYO** | Markdown handoffs / OUTBOX / Swarm_Bus |
| Orchestrator | **SESSION** | **BUFFY** (superviseur/chief scientist, pilote codeur+famille+juge) · Human GO · Cortana ≠ chef · Cockpit ≠ GO |

---

## 5. Rubric for external AI

Score:

1. Boundary integrity (HOT/COLD/LLM/WARM)  — le hub ne touche jamais le fill loop
2. Single source of truth (CSV / Index)  — les JSON vivants ne remplacent pas le CSV
3. Human-in-loop (GO only)  — ADA alerte, ne trade pas
4. Resource fit (8 Go)  — hub = réseau, zéro RAM local
5. Handoff quality (Markdown contracts)  — journal d'intention = le "pourquoi"
6. Maturity honesty (claimed vs embryonic)  — C9/C10 réellement appliqués ?
7. Migration safety (champion intangible)  — genesis jamais patchée
8. **Spec freshness** (read Changelog — reject reviews that ignore 12 août Δ)

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
- `SYNTHESE_24H_CHANTIER_HUB_2026-08-12.md` · `POINT_REPRISE_DERNIER.md` (départ de session) · `SPEC_pont_llm_gate_hub.md` · `CODE_pont_llm_gate_hub.md`
- [[BUDGET_API]] · [[Evaluations/15_kimi_archi_risk_warm]]

---

## 7. Risk & Guardians (Kimi review + hub)

| Guardian | Lane | Trigger | Action |
|----------|------|---------|--------|
| ACE internal | HOT | timer, max loss, STOP | Self stop |
| Hulk stops | HOT | rules paper | Self stop |
| ADA gardienne | WARM | voilure ROUGE / PRENDS_LA_PERTE | Alarme sonore + voix progressive · reflète, ne trade pas |
| Pont gate | WARM | hub down | 503 → fail-closed règles (jamais local) · redémarrage auto |
| Budget hub | WARM | plafond cloud/jour | Bascule gemini (cloud) · jamais local |
| Cockpit STOP | WARM | human confirm | Panic path / stop scripts |
| **Risk Guardian** | **WARM** | DD global, 3 err/10min, Mac orphan | Kill ACE + alert · no order · no genesis |
| Human | BOARD | Any | GO/STOP |

**WARM** = live hors fill loop (gates Hulk, `.veille_status`, scoreur, pont gate, ADA, Vigie, Analyste, hub, Cortana, Cockpit).

---

## 8. Backup & DR (spec)

| Asset | Freq | Target |
|-------|------|--------|
| `runs/*.csv` + Hulk state | Daily (spec) | Git sélectif + disque externe |
| `/tmp/ace777_ram_exchange/` | Never | Reconstruct from CSV |
| Obsidian vault | User / iCloud | OUTBOX bridge |
| `strategie/*.json` vivants | Continu (live) | Git auto-sync horaire |

---

## 9. External review — Kimi 2026-07-30

VERDICT: **KEEP-WITH-FIXES**. Gaps intégrés.

| Fix | Statut |
|-----|--------|
| P1 atomic `.veille_status` | ✅ **CLOSED** — `_safe_write` · writers OK |
| P2 `MAX_GLOBAL_DD_PCT=8` | ✅ constante · [[RISK_C7]] · Guardian pas en vol |
| P3 Cortana URGENT | ✅ `.urgent_alert.json` + poll 60s |

Risk Guardian **pas encore en vol** (WARM kill = GO futur).

**Re-review après Δ 12 août recommandée** : hub cloud, pont gate, ADA, journal d'intention, fiches offres, Cortana V2.

---

## 10. NOTE STRICTE & SINCÈRE (pour la famille — 2026-08-12)

> Destinataire : famille (gemini / deepseek / juge) avant toute évaluation. Lire aussi `POINT_REPRISE_DERNIER.md` + `SYNTHESE_24H_CHANTIER_HUB_2026-08-12.md`.

**Ce qui est vrai et solide :**
- Le hub cloud est devenu **la seule passerelle LLM** (C9 respectée, zéro local). Preuve en vol : `llm_wind` écouté en continu sur le gate trades (12/08).
- Le contexte vivant (`ARCHITECTURE_VIVANTE.md`) est injecté à chaque appel → une IA qui change ne casse rien.
- La chaîne événementielle RADAR → ADA → Cockpit est réelle (pas de polling, le changement déclenche).

**Ce qui est encore fragile / à ne pas surévaluer :**
- **Le run 4h de comparaison (12/08 soir)** décidera si le hub améliore réellement la sélection vs Ollama (référence −12,26 USDT le 11/08). **Un seul run ne prouve rien** — il faudra répéter.
- ADA est un **reflet** (elle lit et alerte, elle ne trade pas) — ne pas la confondre avec un Risk Guardian en vol.
- Le Risk Guardian lui-même **n'est toujours pas en vol** (kill switch = GO futur).
- `journal_intention` et les fiches offres sont jeunes : formats à stabiliser.
- Le budget cloud peut être dépassé (les compteurs ont montré 522/480) — la bascule gemini tient, mais c'est un signal de cadence à surveiller.
- Les JSON vivants (`strategie/*.json`) bougent en continu et peuvent créer des impressions de "toujours pareil" dans le cockpit si les feeds ne sont pas rafraîchis.

**Demande à la famille :** évaluer la Δ 12 août avec les yeux neufs, signaler toute contradiction entre ce que cette spec affirme et ce que les fichiers disent vraiment, et proposer les 3 corrections GO-sized les plus urgentes.

---

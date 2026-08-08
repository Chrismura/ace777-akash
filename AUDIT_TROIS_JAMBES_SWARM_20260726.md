# AUDIT — ACE777 / Hulk / Cortana  
**Date :** 2026-07-26  
**Auteur :** Agent Cursor (Christophe)  
**Objectif :** permettre à un expert externe (IA) de comprendre l’architecture, forces/faiblesses, et une migration vers swarm + handoffs Markdown (Obsidian).

---

## 0. Résumé exécutif (30 secondes)

Trois **jambes semi-indépendantes** sur un MacBook Air M1 8 Go :

| Jambe | Rôle réel | Venue | Maturité |
|-------|-----------|-------|----------|
| **ACE777** | Moteur futures microstructurel (duo SCOUT/HUNTER) | Binance **testnet** | Production-lab (champion figé + molettes) |
| **Hulk** | Paper dip/rip + veille digest | **MEXC** spot (public) | Early paper |
| **Cortana** | Assistant vocal crypto | Local + Gemini/Ollama | App native utilisable ; pas encore orchestrateur |

**Philosophie déclarée :** swarm intelligence.  
**Réalité :** swarm **intra-ACE** (BETA↔ALPHA via JSON RAM) existe ; swarm **inter-jambes** (Hulk↔ACE↔Cortana↔Qwen↔Obsidian) est **embryonnaire**.

Pas de `main.py` unique. Pas de LangChain/CCXT au cœur d’ACE.

---

## 1. Structure du projet

### 1.1 Emplacements racines

```
/Users/christophe/ace777-test-day1/          # ACE777 + engle + hulk-mexc/
/Users/christophe/crypto-voice-assistant-core/  # Cortana (Rust)
/Users/christophe/Documents/Obsidian_ACE777/    # Vault Obsidian (cahier)
```

### 1.2 Arborescence utile (simplifiée)

```
ace777-test-day1/
├── genesis_manifest.txt          # CHAMPION (bash monolithique, md5 37fca367…)
├── GO_USINE_NUAGE.sh             # Point d’entrée ops ACE (patches runtime)
├── launch_vide_froid_* / launch_test_master_*  # lanceurs historiques
├── config_active.env / config_profiles/
├── scripts/                      # preflight, hygiene, rapports, flatten testnet…
├── runs/                         # CSV ALPHA/BETA, LIVE_COLOR, STATE, WHY_ARRET…
├── engle/                        # docs science + journal erreurs E01–E17…
├── hulk-mexc/                    # jambe Hulk (séparée)
│   ├── scripts/{paper_diprip,digest_watch,ace_sense_mexc,watchdog_hulk_ghost}.py|.sh
│   ├── config/defaults.env
│   ├── docs/{TRACKS_SEPARES,VEILLE_QWEN,PROTOCOLE_GHOST,CONFRONTATION}.md
│   └── runs/
├── master_qwen_* / Modelfile*    # modèles Ollama historiques (peu branchés ops)
└── PLAN_AMELIORATIONS_PRO.md

crypto-voice-assistant-core/
├── launch_cortana.sh
├── Cargo.toml / src/main.rs
├── src/live/{app,mic,stt,tts,conversation}.rs
├── src/tools/{detect,market,trading,ace777,...}.rs
├── src/{gemini,ollama,vault}.rs
├── config/app.toml
└── .env (secrets — ne pas commit)

Obsidian_ACE777/
├── Cahier/*.md                   # mémoire humaine/agent (18 notes)
└── Veille_secteur/*.md           # ingest news (amorcé)
```

**Non trouvé comme monolithe unique :** `main.py` / `index.js` global du « projet ACE ».

### 1.3 Points d’entrée

| Composant | Entrée |
|-----------|--------|
| ACE | `./GO_USINE_NUAGE.sh [durée] [TAG]` → copie snapshot usine → patch → `preflight_total_365j.sh` → lance BETA+ALPHA |
| Hulk paper | `python3 hulk-mexc/scripts/paper_diprip.py` |
| Hulk veille | `python3 hulk-mexc/scripts/digest_watch.py --live` |
| Ghost Hulk | `hulk-mexc/scripts/watchdog_hulk_ghost.sh` (toutes les 30 min) |
| Cortana | `./launch_cortana.sh open` → binaire Rust egui |

### 1.4 Extrait GO (structure)

```bash
# GO_USINE_NUAGE.sh — lignes 1–33 (esprit)
# Champion disque 37fca367 — JAMAIS modifié.
# Molettes: BIDIR, STORM_LATCH, STORM_HOLD, STORM_HUNTER, MIN_ENTRY_TENSION
# Usage: NUAGE_MIN_ENTRY_TENSION=2.5 ./GO_USINE_NUAGE.sh 04:00:00 NUAGE_PROD_4H
```

### 1.5 Extrait genesis (moteur)

```bash
#!/usr/bin/env bash
set -euo pipefail
# === V8.6 FORTRESS ===
# Correctif 4061 + Masse 1.618->2.5 + Reset PnL
duration_input="${RUN_DURATION:-07:30:00}"
# … ~2500+ lignes : radar, tension, duo scout/hunter, fills Binance …
```

---

## 2. Stack technique

### 2.1 Langages

| Zone | Langage |
|------|---------|
| ACE moteur | **Bash** (genesis + lanceurs) + Ruby (timer, rapports, IRM) + Python (preflight helpers, rapports erreurs) |
| Hulk | **Python 3.9** (stdlib `urllib`, pas CCXT) |
| Cortana | **Rust** (tokio, egui, whisper-rs, reqwest) |
| Obsidian | Markdown (édition manuelle / agent Cursor) |

### 2.2 Librairies notables

- **ACE :** pas pandas/CCXT ; curl + signing HMAC Binance Futures ; JSON files.
- **Hulk :** Python stdlib + module local `ace_sense_mexc.py` (carnet/tension).
- **Cortana :** `eframe/egui`, `whisper-rs` (Metal), `cpal`/`coreaudio`, `reqwest`, `hmac/sha2`.

**Absent du cœur :** LangChain, LlamaIndex, CCXT, yfinance (sauf outils périphériques éventuels).

### 2.3 API externes

| API | Qui |
|-----|-----|
| Binance Futures **testnet** | ACE (trading), Cortana (trading vocal optionnel), preflight solde |
| MEXC public | Hulk paper + digest |
| DefiLlama | Hulk digest (best-effort TVL) |
| Gemini | Cortana LLM online |
| Ollama local | Cortana offline + modèles Qwen/ACE historiques |
| CoinGecko, mempool, Fear&Greed, Nansen | Cortana market tools |

### 2.4 Modèles LLM

| Usage | Modèle |
|-------|--------|
| Cortana online | Gemini Flash Lite (+ rotation quota) |
| Cortana offline | `qwen2.5:3b` |
| Vision Cortana | `moondream` |
| ACE LLM gate (historique) | Ollama (`QWEEN_V9`, Trinity, etc.) — fail-closed si down |
| Hulk Qwen « yeux » | **Principalement manuel** (prompt dans `VEILLE_QWEN.md`) — pas de boucle Ollama auto stable |

---

## 3. Architecture & logique métier

### 3.1 Schéma de communication actuel

```
                    ┌─────────────────────┐
                    │ Obsidian (Markdown) │  ← écrit surtout par humain/Cursor
                    │ Cahier + Veille     │  ← bots: presque jamais (sauf ingest collage)
                    └──────────▲──────────┘
                               │ (faible)
     ┌─────────────────────────┼─────────────────────────┐
     │                         │                         │
┌────┴────┐            ┌───────┴────────┐         ┌──────┴──────┐
│  Hulk   │            │    ACE777      │         │  Cortana    │
│ MEXC    │            │  Binance TN    │         │  Voix       │
│ paper   │            │  BETA+ALPHA    │         │  Gemini     │
└────┬────┘            └───────┬────────┘         └──────┬──────┘
     │ runs/*.md/json          │ /tmp/ace777_ram_exchange │ lit runs/ ACE
     │ VEILLE_*                │ duo_state, swarm_telemetry│ (ace777.rs)
     └─────────────────────────┴─────────────────────────┘
                    Pas de bus unique inter-jambes
```

### 3.2 Qui décide le trading ?

| Jambe | Décideur |
|-------|----------|
| ACE | **Moteur déterministe** (genesis) : radar → tension/vacuum → tactic → duo → qty → (LLM gate optionnel) → execute. BETA = SCOUT, ALPHA = HUNTER. « Vote » = **pas** un comité LLM ; c’est un **duo mécanique** + shockwaves. |
| Hulk paper | Heuristiques dip/rip dans `paper_diprip.py` (plein stake, 2× → sell 50%). |
| Hulk veille | Digest calcule hints ; **Qwen ne trade pas**. |
| Cortana | Peut proposer un ordre vocal → `vault.rs` (plafonds) → confirmation → Binance testnet. **Ne pilote pas** ACE/Hulk en production. |

### 3.3 Portefeuille

- ACE : masses `BUY_USDT_BETA` (défaut 200) + `BUY_USDT_ALPHA` (800) ; preflight exige somme ≤ solde disponible.
- Hulk : paper notional (ex. 20 USDT/paire), bags, state JSON.
- Pas de portfolio manager unifié multi-venues.

### 3.4 Mémoire / logs

| Artefact | Contenu |
|----------|---------|
| `runs/NUAGE_PROD_*_{ALPHA,BETA}.csv` | Cycles SKIP/FILLED |
| `runs/*_LIVE_COLOR.log` | Trace colorée live |
| `/tmp/ace777_ram_exchange/{duo_state,swarm_telemetry}.json` | Bus essaim ACE (volatil) |
| `runs/LAST_STOP_REASON.txt` / `WHY_ARRET=` | Cause d’arrêt (E18, récent) |
| `engle/JOURNAL_ERREURS.md` | Taxonomie E01–E17… |
| `hulk-mexc/runs/PAPER_*` / `DIGEST_*` / `VEILLE_*` | Paper + veille |
| Obsidian `Cahier/` | Décisions / leçons (humain+Cursor) |

---

## 4. Vault Obsidian

**Chemin :** `/Users/christophe/Documents/Obsidian_ACE777`

### 4.1 Structure

```
Cahier/
  00_Accueil.md
  01_Etat_du_projet.md
  02_Hulk_journal.md
  03_ACE_lecons_molettes.md
  04_Cortana_bot_vocal.md (+ 04b)
  05_Idees_a_tester.md
  06_Qwen_vision_analyse.md
  07_Concepts_physique_et_swarm.md
  08_Cours_setup_pour_Qwen.md
  09_Plan_agent_Twitter_Obsidian.md
  10–13_ACE_*.md
  Journal_2026-07-23.md
  Comment_nourrir_ce_cahier.md
Veille_secteur/
  INDEX.md
  2026-07-23_modele.md
Projet_2_Assistant_Vocal/   # sous-coffre, peu nourri (pointeur LIRE_ICI)
```

### 4.2 Handoffs bots ↔ Obsidian

| Direction | État |
|-----------|------|
| Bots → Obsidian | **Quasi absent** en automatique. Exception : script `veille_secteur_ingest.py` (collage manuel → note). |
| Obsidian → bots | **Non câblé**. Qwen/Cortana ne lisent pas encore le Cahier en prod. |
| Format | Markdown simple, liens `[[wikilinks]]`, **pas** de frontmatter YAML standardisé pour l’instant. |

**Note UX :** Obsidian sur ce Mac a montré des écrans noirs (GPU) ; le contenu reste lisible via Finder/TextEdit.

---

## 5. Points de friction & bugs

### 5.1 Bugs / incidents documentés (échantillon)

| ID | Symptôme | Statut |
|----|----------|--------|
| E11 | ALPHA mort `set -e` sur test faux `post_delta` | Fix runtime GO |
| E16 | Watchdog tue process **vivant** (heartbeat stale pendant NET_RETRY) | Fix E16 skip-kill si ALIVE |
| E17 | Boot purge cassé si `pgrep` match Hulk/Ghost | Fix E17 |
| E18 | STOP anticipé sans writer tracé | `STOP_REASON.txt` + `WHY_ARRET` |
| Ops | Orphelins caffeinate/timer après STOP | Hygiène manuelle fragile |
| Ops | Preflight solde 200+800=1000 vs ~975 dispo | Masse/faucet |
| Hulk | Bags paper ouverts, PnL réalisé faible | Méthode non encore prouvée |
| ACE | PnL souvent porté par **1 gros trade ALPHA** | Fragile |
| ACE | `tension_stale` bloque hunter malgré `STORM_HUNTER arm` (alpage/latence) | Signal terrain |
| Cortana | Quota Gemini, barge-in, écho — largement corrigés juil. 2026 | OK relatif |
| Nuit | Script `nuit_ghost_et_relance_ace` : log court (9 lignes) — relance auto **non garantie** si Mac sleep | Fragile |

### 5.2 Fragilité / spaghetti

- `genesis_manifest.txt` = **monolithe bash** géant (ordre des gates critique).
- `GO_USINE_NUAGE.sh` = patcher string-replace sur snapshot (puissant mais fragile aux drifts de snapshot).
- Dossier ACE très chargé (CSV historiques, sauvegardes, `.1437`, plaintes) → bruit pour un nouvel arrivant.
- Compteurs de cycle BETA≠ALPHA : **normal**, mais trompeur sans doc.

### 5.3 Hardcodé → devrait être config

- Seuils vacuum/radar/impulse dans genesis (vision Engle = les rendre adaptatifs — **pas fait**).
- `nuage_max_age_ms=800` (gate fraîcheur).
- Masses 200/800.
- Chemins absolus Mac dans Cortana (`ACE777_RUNS_DIR` défaut).
- Univers Hulk dans CSV + `defaults.env`.

---

## 6. Sécurité & risques

| Contrôle | État |
|----------|------|
| Clés Binance | `~/.binance_testnet.env` (hors repo) |
| Clés Cortana | `.env` gitignoré + `.env.example` |
| Clés MEXC live | Optionnel `~/.mexc.env` ; paper sans clé |
| Champion ACE | MD5 `37fca367…` — règle « ne pas modifier » |
| Circuit breakers ACE | STOP_ALPHA/BETA, timer, watchdog max_relaunch, LLM fail-closed |
| Circuit Hulk | STOP_PAPER / STOP_DIGEST ; Ghost relance si mort |
| Cortana vault | Plafond ordre, whitelist paires, confirm |
| Rate-limit LLM | Timeouts courts ACE gate ; Gemini rotation 429 ; pas de budget $ LLM unifié |
| Live mainnet ACE | Fichier live env **absent** sur cette machine (testnet only observé) |

**Risque principal :** confusion testnet/live + orphelins process + latence alpage mal interprétée comme « bot cassé ».

---

## 7. Forces / faiblesses

### Forces
- Séparation claire **champion intact** vs molettes GO.
- Duo SCOUT/HUNTER + telemetry swarm réelle (`swarm_cohesion`, shockwaves).
- Observabilité en progrès (PROCESS_EXIT, WHY_ARRET, journal Engle).
- Hulk isolé (ne pollue pas genesis).
- Cortana : stack vocale sérieuse (AEC, barge-in).
- Cahier Obsidian déjà structuré pour un expert.

### Faiblesses
- Pas d’orchestrateur unique ; « swarm » inter-jambes = slogan > code.
- Edge ACE non stable (dépendance jackpot ALPHA).
- Hulk paper non conclu (confrontation Qwen incomplète).
- Obsidian non branché en handoff automatique.
- Ops nuit/Mac sleep/RAM 8 Go = points de rupture.
- Dette de fichiers historiques dans `ace777-test-day1`.

---

## 8. Proposition de migration — Swarm + handoffs Obsidian

### Principe
Ne **pas** fusionner les moteurs. Ajouter une **couche de coordination** Markdown + un seul agent « Chef » (Cursor/Cortana) qui lit/écrit des handoffs.

### Contrat handoff (proposé)

Dossier Obsidian `Handoffs/` :

| Fichier | Producteur | Consommateur | Contenu |
|---------|------------|--------------|---------|
| `ETAT_TROIS.md` | script cron 5–15 min | tous | PIDs, stérile?, Ghost?, solde, âge paper |
| `ACE_SESSION.md` | post-run ACE | Qwen/Cursor/Cortana | WHY_ARRET, fills, molettes, leçons ≤5 |
| `HULK_DIGEST.md` | digest_watch (symlink/copie DIGEST_LATEST) | Qwen | hints |
| `HULK_CALLS.md` | scoreur (à écrire) | confrontation | hit/miss |
| `VEILLE_SECTEUR.md` | ingest Twitter/Hermes | Qwen | 3 signaux/jour |
| `ORDRES_PROPOSES.md` | Qwen/Cortana | **humain seulement** | jamais auto-exécuté sans confirm |
| `LECONS.md` | juge déterministe + LLM | prochains prompts | append-only |

**Format minimal :**

```markdown
---
ts: 2026-07-26T12:00:00Z
from: ace_post_run
to: [qwen, cursor, cortana]
status: ready
---
# ACE_SESSION
WHY_ARRET: ...
PnL: ...
Leçons:
- ...
```

### Phases

1. **P0 (1 semaine)** — Scripts qui **écrivent** `ETAT_TROIS` + `ACE_SESSION` depuis `runs/` (zéro changement genesis).  
2. **P1** — Qwen auto lit `HULK_DIGEST` + `Cours_setup` + écrit notes structurées (toujours no-trade).  
3. **P2** — Cortana lit `ETAT_TROIS` / `ACE_SESSION` (étendre `ace777.rs`).  
4. **P3** — Scoreur Hulk calls→outcomes ; confrontation auto.  
5. **P4** — Agent veille (Hermes-like) → `Veille_secteur` uniquement.  
6. **Ne pas faire** : unifier ACE+Hulk en un process ; laisser un LLM modifier `genesis_manifest.txt`.

### Critères de succès migration
- Un expert ouvre Obsidian et comprend l’état en &lt; 5 min.  
- Chaque fin de run ACE produit un handoff sans intervention.  
- Aucun ordre live sans confirm humaine.  
- Champion md5 inchangé.

---

## 9. Fichiers « à lire en premier » pour un expert

1. `GO_USINE_NUAGE.sh` (ops ACE)  
2. `genesis_manifest.txt` (moteur — lecture seule)  
3. `engle/JOURNAL_ERREURS.md` + `PLAN_STORM_WICK.md`  
4. `hulk-mexc/docs/TRACKS_SEPARES.md` + `paper_diprip.py` / `digest_watch.py`  
5. `crypto-voice-assistant-core/EXPORT_SETUP_IA.md` + `src/tools/ace777.rs`  
6. Obsidian `Cahier/00_Accueil.md` + `08_Cours_setup_pour_Qwen.md`  
7. `PLAN_AMELIORATIONS_PRO.md`

---

## 10. État opérationnel au moment de l’audit (2026-07-26)

- Vault Obsidian : notes présentes ; app parfois **écran noir** (GPU) — contenu OK sur disque.  
- Log nuit `NUIT_GHOST_RELANCE.log` : démarré 2026-07-23 21:24Z, **pas de preuve** de relance ACE dans ce fichier (9 lignes) — vérifier manuellement process/runs.  
- Champion certifié : md5 préfixe `37fca367`.

---

*Fin du rapport. Copier-coller tel quel vers un expert IA externe.*

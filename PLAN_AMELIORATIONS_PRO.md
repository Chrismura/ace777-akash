# Plan d'améliorations professionnelles — ACE777 + Cortana

> Référence loop engineering (Roan) + portfolio pro (CyrilXBT)  
> Dernière mise à jour : 2026-07-08  
> Statut : en cours

---

## Principes directeurs

1. **Fail-closed** — si un composant critique (LLM, API, verifier) échoue → SKIP, jamais TRADE par défaut
2. **Déterministe d'abord** — vérifications en code, pas en LLM (Sharpe, drawdown, qty min)
3. **Config unique** — un seul `config_active.env` sourcé par tous les lanceurs
4. **Boucle fermée** — PnL → leçons → règles → prochain cycle (sans overfit réactif)
5. **Ne pas toucher** sans ordre explicite : `BUY_USDT_BETA`, timeouts Binance (0.2–0.3s)

---

## Phase 1 — Fiabilité critique (semaine 1–2)

### #1 LLM gate fail-closed ✅ FAIT
**Fichier :** `genesis_manifest.txt`, `launch_test_master_base_v8_6_fortress.sh`

| Avant | Après |
|-------|-------|
| Ollama down / vide → TRADE | Ollama down / vide / ambigu → SKIP |
| Timeout 15s | Timeout 3s (configurable) |
| Log `reason=ollama_skip` seulement | Log `reason=... status=OK\|FAIL\|SKIP` |

**Variables ajoutées :**
- `LLM_GATE_FAIL_CLOSED=TRUE` (défaut)
- `LLM_GATE_CONNECT_TIMEOUT=2`
- `LLM_GATE_MAX_TIME=3`

**Raisons de SKIP :**
- `ollama_unreachable` — curl échoue
- `ollama_empty` — réponse JSON sans contenu
- `ollama_skip` — LLM dit non
- `ollama_ambiguous` — réponse sans TRADE/SKIP clair (fail-closed)

**Test manuel :**
```bash
# Ollama arrêté → tous les signaux doivent SKIP llm_gate ollama_unreachable (FAIL)
LLM_GATE_ENABLED=TRUE ollama stop
./launch_vide_froid_4h_binance.sh

# Ollama actif → TRADE seulement si réponse contient trade/oui/yes/go/ok
ollama serve &
```

---

### #2 Config unifiée ✅ FAIT
**Fichiers :** `config_active.env`, `config_profiles/`, `scripts/load_config.sh`

- `config_active.env` — source unique (profil vide_froid_binance canonique)
- `config_profiles/masse_250.env` — override masses 250/250 (explicite)
- `config_profiles/vide_froid_classic.env` — ancien profil stase 5bps
- `scripts/load_config.sh` — chargeur avec garde `ACE777_CONFIG_LOADED`
- Lanceurs simplifiés : `launch_vide_froid_*_binance.sh`, `launch_250_4h.sh`, `launch_vide_froid_4h/8h.sh`

**Test :**
```bash
source ./scripts/load_config.sh && echo $BUY_USDT_BETA  # → 200
source ./scripts/load_config.sh masse_250 && echo $BUY_USDT_BETA  # → 250
```

---

### #3 STATE.md canonique ✅ FAIT
**Fichiers :** `scripts/generate_state_md.rb`, `scripts/update_state_md.sh`, `runs/STATE.md`

- Génération auto : début run (`running`), fin run (`ended`), arrêt (`stopped`)
- Contenu : config, PnL BETA/ALPHA, duo_state, top SKIP, vortex, processus, ERREURS_AI
- Auto-détection du dernier tag CSV si `STATE_TAG` absent

**Usage manuel :**
```bash
STATE_TAG=MASTER_BASE_V8_5_IMPACT_8H00 STATE_PHASE=snapshot ./scripts/update_state_md.sh
cat runs/STATE.md
```

---

### #4 Post-run auto PnL ✅ FAIT
**Fichiers :** `scripts/generate_pnl_report.rb`, `scripts/post_run_report.sh`

- Génère `runs/RAPPORT_PNL_AUTO_YYYYMMDD_HHMMSS.md`
- Copie dans `master_base/pnl/`
- Lien latest : `runs/RAPPORT_PNL_DERNIER.md`
- Append `master_base/pnl/INDEX_MASTER_BASE.csv`
- Append `RUN_INDEX.md`
- Déclenché en fin de cycle + `stop_ace777.sh`

**Usage manuel :**
```bash
STATE_TAG=MASTER_BASE_V8_5_IMPACT_8H00 ./scripts/post_run_report.sh
cat runs/RAPPORT_PNL_DERNIER.md
```

---

### #5 Diagnostic ALPHA dormante ✅ FAIT
**Fichiers :** `scripts/generate_diag_alpha.rb`, `scripts/diagnostic_alpha.sh`, `runs/DIAG_ALPHA_DERNIER.md`

- Cause racine identifiée : `DUO_HUNTER_REQUIRE_STOP_LOSS=TRUE` + sorties BETA en `shock_inversion_stop`
- secondaire : `DUO_EVENT_TTL_SEC=20` → `stale_state` (80% des duo_wait)
- Recommandations documentées, **aucune constante modifiée**
- Auto en post-run via `post_run_report.sh`

**Fix appliqué 2026-07-08 (config_active.env + genesis) :**
- P0 : `DUO_HUNTER_REQUIRE_STOP_LOSS=FALSE`
- P1 : `DUO_EVENT_TTL_SEC=60`
- P2 : `duo_touch_heartbeat()` chaque cycle SCOUT
- Code : revenge accepte aussi `shock_inversion_stop`, `fluid_exit_*`, `beta_sentinel_cut`

### #13 Bridge Cortana ↔ ACE777 ✅ FAIT
**Fichiers :** `src/tools/ace777.rs`, `src/tools/detect.rs`, `src/live/app.rs`, `.env.example`

- Lit `STATE.md`, `duo_state.json`, `RAPPORT_PNL_DERNIER.md`, `DIAG_ALPHA_DERNIER.md`
- Phrases : « statut beta », « pnl session », « diagnostic alpha », « stop le bot »
- Variable `ACE777_RUNS_DIR` dans `.env`

---

## Phase 2 — Loop engineering (semaine 3–4)

### #6 Verifier JSON structuré
**Fichier :** `scripts/llm_gate_verify.py` (nouveau)

- Remplace grep bash par JSON `{decision, confidence, reason}`
- Timeout 0.3s max, fail-closed
- Appelé depuis genesis via `python3 scripts/llm_gate_verify.py`

### #7 SKILL.md Cursor
**Fichier :** `.cursor/skills/ace777-trading/SKILL.md`

Procédures : lancer run, arrêter, lire PnL, promouvoir setup plus-value, checklist preflight

### #8 Hooks automation
**Fichiers :** `.cursor/hooks.json`

- `pre-run` : ping Binance, ping Ollama, vérif clés API
- `post-run` : rapport PnL auto, mise à jour STATE.md

### #9 Réparer supervisor V9
**Fichier :** `tendance/supervisor_v9.sh`

- Corriger parsing JSON Ollama 8B (`invalid_v9_json`)
- Fallback CHOP explicite loggé

### #10 Bridge conseil_phase → live
**Fichier :** `conseil_phase_ace777.py`

- Lire `runs/duo_state.json`, `duo_session.json`, dernières lignes CSV
- Mode advisory read-only (pas d'ordres)

---

## Phase 3 — Cortana vocal (semaine 3–5)

### #11 Métriques latence
**Fichier :** `crypto-voice-assistant-core/src/live/metrics.rs` (nouveau)

- Timestamps : `listen_ms`, `stt_ms`, `llm_ms`, `tts_ms`, `total_ms`
- Affichage UI + log `runs/cortana_metrics.log`

### #12 Cache marché TTL
**Fichier :** `crypto-voice-assistant-core/src/tools/cache.rs` (nouveau)

- Prix 10s, dérivés 30s, pulse 60s
- Réduit latence et risque 429

### #13 Bridge Cortana ↔ ACE777
**Fichiers :** `crypto-voice-assistant-core/src/tools/ace777.rs` (nouveau)

- Lire `~/ace777-test-day1/runs/duo_state.json`
- Commandes vocales : « status BETA », « PnL session », « phase actuelle »
- Variable `ACE777_RUNS_DIR` dans `.env`

### #14 Journal d'ordres vocal
**Fichier :** `crypto-voice-assistant-core/data/trade_journal.jsonl`

- Chaque ordre vocal : timestamp, intent, vault check, réponse Binance

### #15 Streaming LLM → TTS
**Fichiers :** `gemini.rs`, `tts.rs`, `app.rs`

- SSE Gemini → TTS dès première phrase complète
- Réduit latence perçue de 5–15s à ~2s

### #16 Découpage app.rs
**Modules :** `state.rs`, `barge_in.rs`, `trade_flow.rs`, `llm_worker.rs`

---

## Phase 4 — Niveau desk (mois 2–3)

| # | Action | Projet |
|---|--------|--------|
| 17 | Extraire modules testables (radar, duo, sizing) | ACE777 |
| 18 | Shadow → calibration seuils | ACE777 |
| 19 | Connecteur Exchange abstrait | ACE777 |
| 20 | Function calling Gemini (tools structurés) | Cortana |
| 21 | WebSocket Binance alertes vocales | Cortana |
| 22 | Tests E2E audio PCM synthétique | Cortana |

---

## Ordre d'exécution (ce que l'IA suit)

```
✅ #1  LLM gate fail-closed
✅ #2  Config unifiée
✅ #3  STATE.md
✅ #4  Post-run auto PnL
✅ #5  Diagnostic ALPHA
✅ #13 Bridge Cortana ↔ ACE777
✅ A1  V9 supervisor réparé
✅ A2  P3 radar ALPHA (conf 0.25 / mom 0.008)
✅ A3  Preflight script
✅ Run validation 4H (#1) — session ~+17 USDT, ALPHA 57 trades
⬜ Run validation #2 (~3h30)
⬜ #11 Métriques latence Cortana
⬜ #6–#10 Phase 2 trading
⬜ #12–#16 Phase 3 vocal
⬜ #17–#22 Phase 4
```

---

## Critères « niveau pro »

| Critère | Cible |
|---------|-------|
| LLM gate fail-closed | ✅ |
| Config reproductible | 1 source unique |
| Rapport PnL auto | Chaque cycle |
| Latence vocale perçue | < 3s première syllabe |
| Supervision vocale bot | Status + PnL + stop |
| Tests automatisés | radar, vault, trade_intent |
| Audit trail | CSV + JSONL + STATE.md |

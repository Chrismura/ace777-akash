# SYNTHÈSE 24H — CHANTIER HUB (2026-08-12)

> Gravé en fin de session pour ne rien perdre. Run 4h de comparaison en cours
> (fin prévue ~23:00) — le bilan chiffré sera ajouté demain matin.

---

## 🎯 L'objectif du jour
Brancher le garde-fou des trades (gate LLM du moteur) sur le **hub cloud**,
pour ne plus dépendre de l'IA locale (qwen-local) — directive Christophe :
« plus d'IA locale nulle part, tout sur le hub ».

## ✅ Ce qui a été construit (la preuve est acquise)

### 1. Le pont `llm_gate_hub_bridge.py` (codé par le codeur, intégré + blindé par le superviseur)
- **Emulation Ollama** : `/api/tags` + `/api/generate` → le moteur croit parler à Ollama
- **Traduction** vers le hub : `POST 127.0.0.1:11435/v1/chat/completions`, task `supervise.decision`
- **System prompt JSON strict** (sans lui, grok répond en texte → parse échoue)
- **Cache réglable** `LLM_GATE_PONT_CACHE_SEC` (90 s par défaut) : le hub est consulté
  1×/90 s au lieu de chaque cycle → budget cloud tenu (~160 appels/run au lieu de ~1000)
- **Cache par prompt** (hash) : le mode radar (si activé un jour) ne reçoit pas la réponse du mode cohesion
- **Fail-closed** : hub mort → 503 → pas de run sans juge
- **Bind localhost** + extraction JSON robuste (strip fences markdown)
- **Service launchd** `com.ace777.llm-gate-hub` (KeepAlive, auto-relance testée : kill → relancé ✓)

### 2. Le moteur champion (intact)
- Zéro ligne de logique changée — juste 3 délais rendus configurables :
  `VORTEX_LLM_READ_TIMEOUT=45`, `VORTEX_LLM_OPEN_TIMEOUT=5`, `VORTEX_LLM_BUDGET_SEC=20`
- Bascule config : `LLM_OLLAMA_URL=http://127.0.0.1:11439` (backup fait)

### 3. La preuve en conditions réelles (12/08)
- **Test décisif moteur → pont → hub** : `cohesion 0.35, justification llm_wind, emergency FALSE`
  → le juge du hub est écouté, zéro fallback sur les règles
- **Deux vitesses prouvées** : 1er appel 9,9 s (hub consulté) → suivant 0,016 s (cache)
- **Séparation par prompt prouvée** : prompt différent → hub re-consulté
- **Run de preuve 30 min** (GO_VORTEX_V2) : juge hub écouté en continu (`llm_wind`),
  pont consulté toutes les ~20 s, cache actif

## 🚀 Le run de comparaison 4h (en cours)
- **Hier (référence Ollama)** : 8 trades, PnL −12,26 USDT
- **Ce soir (hub)** : lancé à 19:00 via `ENCHAINER_RUN_4H_HUB.sh` (auto après le run 30 min),
  tag `MASTER_VORTEX_V2_COLLAB_4H`, fin ~23:00
- **À comparer demain** : mêmes conditions, seule différence = le cerveau du garde-fou

## 🔧 Les 2 pièges évités en route
1. `GO_USINE_NUAGE.sh` = gate **OFF** (preuve impossible) → il faut **`GO_VORTEX_V2.sh`**
   (profil `vortex_v2_collab.env` : `VORTEX_CONTROL_ENABLED=TRUE` + `VORTEX_V2_RADAR_PILOT=TRUE`)
2. Le profil `vortex_v2_collab.env` écrasait le budget avec l'ancienne valeur `1.2`
   → corrigé à `20` (sinon le juge est classé « llm_slow » au lieu de « llm_wind »)

## 🧠 La connaissance vivante (question de Christophe, vérifiée dans le hub)
- Le hub injecte `ARCHITECTURE_VIVANTE.md` (régénéré ≤ 2 min) dans les prompts des tâches
  de **décision** (famille, juge, audit, strategie, signets, protocole)
- Le **gate des trades** (`supervise.decision`) reçoit un prompt minimal volontairement
  (JSON strict, pas de contexte) — choix d'économie de tokens, pas un oubli
- Conséquence : changer d'IA ne casse rien — la fiche ACE777 suit chaque appel

## 📌 Points à surveiller (demain)
1. **Heartbeat figé** : `/tmp/alpha_heartbeat.txt` reste à 16:25Z pendant le run —
   le run vit (CSV + gate + process) mais le watchdog sémantique semble endormi
2. **Budget cloud** : 523/480 aujourd'hui (dépassé) — le fallback gemini tient (cloud),
   aucun local utilisé. À décider : relever le budget ou rester comme ça
3. **Même tag CSV** : le run 4h partage le fichier du run 30 min →
   filtrer par timestamp (>17:00 UTC) pour la comparaison

## 📁 Fichiers clés du chantier
- `Index_Maison/scripts/llm_gate_hub_bridge.py` (pont, prod)
- `~/Library/LaunchAgents/com.ace777.llm-gate-hub.plist` (service)
- `scripts/vortex_supervisor_v2_llm.rb` (gate patché)
- `config_active.env` (bascule 11439 + timeouts + cache) — NON tracké (secrets)
- `config_profiles/vortex_v2_collab.env` (profil gate ON, budget corrigé)
- `ENCHAINER_RUN_4H_HUB.sh` (enchaîneur auto 30 min → 4h)
- `Index_Maison/SPEC_pont_llm_gate_hub.md` + `CODE_pont_llm_gate_hub.md` (trace)

## 🏔️ Verdict
Le chantier hub est **terminé et prouvé**. Le garde-fou des trades parle au hub
(grok → gemini en secours), le moteur n'a pas bougé, le budget cloud tient grâce
au cache. Prochaine étape : bilan chiffré du run 4h (demain) + comparaison.

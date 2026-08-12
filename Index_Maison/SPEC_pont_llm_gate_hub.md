# SPEC — PONT LLM GATE → HUB (remplacement Ollama, Voie A)

**Orchestrateur :** Ada (Buffy) — loi 1quinquies : Ada spécifie, le CODEUR code.
**Date :** 12 août 2026. **Statut :** GO Christophe (Voie A — adaptateur pont).

---

## 1. OBJECTIF

Remplacer la passerelle IA locale Ollama du garde-fou des trades (LLM gate)
par le HUB ACE777 (`http://127.0.0.1:11435`), sans toucher au moteur champion.

Directive Christophe : « zéro IA locale, tout passe par le hub ». Le vieux moteur
(Alpha/Beta via Binance testnet) exige un garde-fou fail-closed avant chaque
trade. Aujourd'hui ce garde-fou appelle Ollama (`qwen2.5-coder:1.5b`). On
installe un **pont** qui émule l'API Ollama mais appelle le hub derrière.

## 2. PRINCIPE (à comprendre avant de coder)

```
MOTEUR (vortex_supervisor_v2_llm.rb)
   │  POST http://127.0.0.1:11439/api/generate   ← LLM_OLLAMA_URL pointe vers le pont
   ▼
PONT Python (llm_gate_hub_bridge.py) — émule Ollama
   │  POST http://127.0.0.1:11435/v1/chat/completions  task=supervise.decision
   ▼
HUB → puter-grok (fallback gemini) → réponse JSON
   │
   ▼ (le pont traduit la réponse en format Ollama {"response": "..."})
MOTEUR (inchangé) → continue
```

**Règle d'or : le moteur ne change PAS de comportement.** Il croit parler à
Ollama. Le pont traduit. Si le hub est muet → le pont répond 503 → le moteur
fait son fallback règles (fail-closed conservé, idem aujourd'hui).

## 3. LE PONT — `llm_gate_hub_bridge.py` (Python 3.9, stdlib uniquement)

Serveur HTTP local (http.server stdlib) qui émule **2 endpoints Ollama** :

### 3.1 `GET /api/tags`
Réponse attendue par le preflight (qui grep le nom du modèle) :
```json
{"models": [{"name": "<LLM_MODEL demandé>"}]}
```
Le nom du modèle vient de la variable d'env `LLM_MODEL` (ex: qwen2.5-coder:1.5b).
Le pont retourne TOUJOURS ce nom (peu importe le vrai modèle derrière — c'est le hub).

### 3.2 `POST /api/generate`
Body reçu (format Ollama) :
```json
{
  "model": "qwen2.5-coder:1.5b",
  "prompt": "{\"swarm_cohesion\":0.5,\"mode\":\"CHOP\"}",
  "stream": false,
  "format": "json",
  "options": {"num_predict": 45, "temperature": 0.0, "top_p": 1.0}
}
```
Actions du pont :
1. Construire l'appel hub (OpenAI format) :
   - URL : `HUB_URL` (défaut `http://127.0.0.1:11435/v1/chat/completions`)
   - Body : `{"task": "supervise.decision", "messages": [{"role": "user", "content": <prompt reçu>}], "temperature": 0.0, "max_tokens": <options.num_predict>}`
   - Timeout pont→hub : connect 2 s, read **45 s** (le cloud est lent, le pont attend patiemment)
2. Réponse hub → extraire `choices[0].message.content`
3. Traduire en réponse Ollama : `{"response": "<contenu>"}`
4. **Si hub injoignable / timeout / erreur** → répondre `503` (le moteur fera son fallback règles, comme avec Ollama mort)

### 3.3 Config (variables d'env)
| Var | Défaut | Rôle |
|---|---|---|
| `LLM_GATE_PONT_PORT` | `11439` | Port d'écoute du pont |
| `HUB_URL` | `http://127.0.0.1:11435/v1/chat/completions` | Endpoint hub |
| `LLM_MODEL` | `qwen2.5-coder:1.5b` | Nom renvoyé par /api/tags |
| `LLM_GATE_HUB_TIMEOUT_READ` | `45` | Timeout pont→hub (s) |

### 3.4 Contraintes
- Python 3.9 stdlib uniquement (http.server, json, urllib) — macOS, non fatal
- Commentaires en français
- Log : `/tmp/llm_gate_hub.log` (chaque requête : reçue / traduite / erreur)
- `--test` mode : vérifie le hub, répond 0 si OK
- Ne jamais afficher de secret

## 4. PATCH ADDITIF DU MOTEUR (2 lignes, comportement inchangé par défaut)

**Point critique (honnêteté) :** `vortex_supervisor_v2_llm.rb` attend la réponse
du juge en **2 s max** (`open_timeout=1, read_timeout=2.0`). Ollama local répondait
en <1 s. Le hub cloud met 2-8 s. Si on ne change rien, le moteur timeout → le
juge hub ne sera **jamais écouté**.

Patch MINIMAL et ADDITIF dans `vortex_supervisor_v2_llm.rb` (les 2 seuls endroits) :
```ruby
http.open_timeout = (ENV["VORTEX_LLM_OPEN_TIMEOUT"] || "1").to_f
http.read_timeout = (ENV["VORTEX_LLM_READ_TIMEOUT"] || "2.0").to_f
```
Défauts = valeurs actuelles → **zéro changement de comportement** si les ENV
ne sont pas posées. Quand on basculera vers le hub, on posera
`VORTEX_LLM_READ_TIMEOUT=45` dans config_active.env.

⚠️ Ce patch est ADDITIF : il ne change pas la logique, il rend 2 constantes
configurables. Le moteur reste fonctionnel à l'identique sans les ENV.

## 5. DÉPLOIEMENT (fait par Ada après revue, pas par le codeur)

1. Copier `llm_gate_hub_bridge.py` → `~/ace777-test-day1/Index_Maison/scripts/`
2. Tester `--test` → hub répond
3. Lancer détaché (start_new_session) → vérifier /api/tags et /api/generate au curl
4. Plist launchd `com.ace777.llm-gate-hub` (KeepAlive) — relance auto si mort
5. Basculer `LLM_OLLAMA_URL=http://127.0.0.1:11439` dans config_active.env
   + `VORTEX_LLM_READ_TIMEOUT=45` → effet au PROCHAIN run (pas celui en cours)
6. Test réel : lancer vortex une fois en CLI avec le pont → la justification
   dans vortex_control.json doit montrer le hub (`llm_wind_*` + pas d'emergency)

## 6. CONTRAT DE SORTIE DU CODEUR

Le code complet de `llm_gate_hub_bridge.py` (prêt à copier, non fatal,
commenté en français) + le patch exact des 2 lignes pour `vortex_supervisor_v2_llm.rb`.
Une seule mission : LE PONT. Rien d'autre.

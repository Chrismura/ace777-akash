# 🔀 ROUTAGE IA — structure des dépenses et des tâches

> Le hub Prise IA (127.0.0.1:11435) route chaque appel vers la bonne IA selon la TÂCHE.
> Philosophie : **local d'abord** (gratuit + privé), **cloud quand la qualité l'exige** (et dans le budget).

## Comment ça marche
- Tout appel POST /v1/chat/completions peut porter un champ `task` (ex: `"task": "ada.sanity"`).
- Sans `task` : comportement historique (ordre de providers.json) — **rien ne casse**.
- Avec `task` : le hub lit `routing.json`, applique [provider préféré → fallback], logge dans `usage.jsonl`, et respecte le budget cloud global.

## Table des tâches (routing.json)
| Tâche | Préféré | Repli | Quota cloud/j | Usage |
|---|---|---|---|---|
| `ada.sanity` | Qwen local | Gemini | 5 | tuyauterie de démarrage (ada.command étape 2) |
| `cortana.brief` | Qwen local | Gemini | 20 | briefs vocaux — **local par défaut (confidentialité de la voix)** |
| `audit.protocol` | **Gemini** | Qwen local | 5 | audit de protocole — qualité maximale |
| `signets.synthese` | Qwen local | Gemini | 10 | synthèse des bookmarks X |
| `chat.local` | Qwen local | Gemini | 30 | usage interactif libre |

## Budget global — DYNAMIQUE (08/08)
- `cloud_daily_budget` = nombre max d'appels CLOUD par jour, toutes tâches confondues.
- **Le budget n'est plus figé** : il se recalcule automatiquement via `budget_hub.py` depuis les **providers actifs** (capacité théorique × 15 %, borné 40–800). Ajouter un provider → le budget suit.
  - `python3 ~/prise-ia/budget_hub.py` (affiche) · `--apply` (écrit dans routing.json + backup)
- Au-delà : repli automatique sur le local + événement `quota` dans hub_events.jsonl.
- Visible en direct : `GET /routing` (table + compteurs du jour) et `GET /usage` (journal).
- **Jauge de capacité** : `python3 ~/prise-ia/capacite_hub.py` (limites vs consommation, marge restante).

## Étalement des appels (08/08 — règle des limites par minute)
- Le vrai facteur limitant n'est PAS le budget quotidien mais les **limites par minute** :
  OpenRouter `:free` ~20 req/min · NVIDIA NIM ~40 req/min · Gemini ~15-30 req/min · Groq ~30 req/min.
- **Règle** : tout batch d'appels cloud doit **espacer** ses requêtes (≥ 5 s entre deux appels) et **étaler** sur la journée. Les cadences (`*_cadence.sh`) sont déjà séquentielles — c'est le bon pattern.
- Le hub bascule automatiquement en failover sur 429/échec (jamais de crash) — les erreurs sont loggées dans hub_events.jsonl.

## Ajouter / modifier une tâche
1. Éditer `routing.json` (effet immédiat — le hub le relit à chaque requête).
2. Envoyer l'appel avec `"task": "mon.nouvelle.tache"`.

## Principe énergétique (à affiner ensemble)
- Le quotidien (tuyauterie, briefs, synthèses) : **local** → 0 €, 0 export.
- Le pointu (audits, tâches de raisonnement) : **cloud** → qualité, coût maîtrisé par quota.
- `usage.jsonl` permet de mesurer la répartition réelle (local vs cloud) par jour et par tâche.

## Routage par complexité (inspiré LLMRouter — @tom_doerr, ajouté 07/08)

- Option par tâche `route_by_complexity: true` + `complexity_threshold` (caractères, défaut 600).
- Logique : requête **courte** (< seuil, messages `user` uniquement) → **local** ; requête **longue/analytique** (≥ seuil) → **cloud** si budget global dispo, sinon local.
- Activée sur : `chat.local` + `signets.synthese`.
- Événements `routing` dans hub_events.jsonl · backups `*.bak-2026-08-07` · à l'essai — seuil ajustable.

## Fournisseurs gratuits branchés (07/08 — vérifiés)

| id | Provider | Tier gratuit | Clé à créer (.env) |
|---|---|---|---|
| `qwen-local` | Ollama local | — | aucune (local) |
| `gemini` | Google AI Studio | ~1000 req/j (flash-lite) | GEMINI_API_KEY ✅ |
| `openrouter-free` | OpenRouter `:free` | $0/token · 14 modèles gratuits · ~20 req/min | OPENROUTER_API_KEY ✅ (gratuite, sans carte) |
| `groq` | Groq LPU | 30 RPM / 1000 req/j (70b) | GROQ_API_KEY (à activer si besoin) |
| `nvidia` | build.nvidia.com | 100+ modèles (DeepSeek V4, GLM 5.2, Kimi K2.6), ~40 req/min, ~1000 crédits | NVIDIA_NIM_API_KEY ✅ (nvapi-, sans carte, ACTIF 08/08) |
| `mistral` | La Plateforme | essai ~1 req/s | MISTRAL_API_KEY (désactivé) |
| `cloudflare-workers-ai` | Workers AI | 10k Neurons/j | CF_API_TOKEN + account_id (désactivé) |

Clés dans `~/.env` (une par ligne) : GEMINI_API_KEY · OPENROUTER_API_KEY · NVIDIA_NIM_API_KEY · GROQ_API_KEY · MISTRAL_API_KEY.
Sans clé → le provider est appelé SANS en-tête Authorization → échec 401 rapide → le hub bascule automatiquement sur le suivant (rien ne casse, mais prévoir les clés pour que le fallback soit utile).
Cerebras (tier gratuit fermé 17/08) et GitHub Models (retiré 30/07) → NE PAS ajouter.

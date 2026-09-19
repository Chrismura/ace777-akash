# ⚡ Prise IA — Hub léger local

> Hub universel d'IA, version légère (zéro dépendance, stdlib Python).  
> Créé par Buffy le 05/08/2026 · testé OK : Qwen locale + Gemini + bascule auto.

## Ce que c'est

Un serveur local compatible **API OpenAI** qui essaie vos IA dans l'ordre de priorité et **bascule automatiquement** si l'une échoue (quota, panne…).

- **Port** : `127.0.0.1:11435` (local uniquement)
- **Endpoints** : `POST /v1/chat/completions` · `GET /v1/models` · `GET /health` · `GET /events`

## Prises branchées (providers.json)

| Ordre | Prise | Modèle |
|-------|-------|--------|
| 1 | Qwen locale (Ollama) | `qwen2.5:3b` (rapide) |
| 2 | Google Gemini | `gemini-flash-lite-latest` |
| 3 | OpenRouter (gratuits) | `:free` — désactivé par défaut (clé requise) |

## Lancer / arrêter

Le hub est un **LaunchAgent** macOS (survit aux terminaux, relance auto) :

```bash
launchctl load   ~/Library/LaunchAgents/com.ace777.prise-ia.plist   # démarrer
launchctl unload ~/Library/LaunchAgents/com.ace777.prise-ia.plist   # arrêter
```

Logs : `~/prise-ia/hub.log` · événements : `GET /events` ou `hub_events.jsonl`

## Utiliser (compatible OpenAI)

```bash
curl http://127.0.0.1:11435/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"messages": [{"role": "user", "content": "Bonjour"}]}'
```

→ Réponse de Qwen locale. Si Qwen tombe → bascule Gemini automatiquement.  
→ `"model": "gemini-flash-lite-latest"` force une prise précise.  
→ Tout autre client compatible OpenAI (Cortana, cockpit, scripts) peut pointer vers `http://127.0.0.1:11435/v1`.

## Ajouter une prise

Éditer `providers.json` : `base_url` (compatible OpenAI), `model`, `api_key_env` (variable d'env ou clé dans `~/prise-ia/.env`), `order`.  
Le hub relit la config à chaque requête — pas de redémarrage nécessaire.

## Prochaines étapes (fiche complète : FICHE-PRISE-IA.md)

- Radar OpenRouter (modèles gratuits) — à activer avec clé
- UI (React + Convex) quand le hub prouve son utilité
- Brancher Cortana / cockpit sur le hub

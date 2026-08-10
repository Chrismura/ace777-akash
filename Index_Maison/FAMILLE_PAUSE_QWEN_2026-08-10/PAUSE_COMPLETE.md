# PAUSE QWEN — COMPLÈTE (10/08, soir)

La pause réversible de Qwen-Ollama (validée famille GO, GEMINI + JUGE) est
désormais **entièrement appliquée**.

## Ce qui restait (3 tâches) et a été fait

| Tâche | Avant | Après |
|---|---|---|
| `ada.sanity` (tuyauterie démarrage) | qwen-local (fb gemini) | **gemini** (fb nvidia) |
| `signets.synthese` (bookmarks X) | qwen-local (fb gemini) | **gemini** (fb nvidia) |
| `chat.local` (interactif libre) | qwen-local (fb gemini) | **gemini** (fb nvidia) |

→ `route_by_complexity` supprimé sur signets.synthese + chat.local (le routage
local n'a plus de sens : plus aucune cible locale dans ces tâches).

## Preuve réelle (testé)

- Appel `ada.sanity` via le hub → **provider = Google Gemini**, réponse OK
- `ollama ps` : **vide** — le modèle ne se recharge plus
- RAM : **3,4 Go libres** (avant : 97 Mo, RAM=CRITIQUE)
- Hub (9 providers), pont, gardien : intacts

## Réversibilité (rien n'est supprimé)

- Modèle `qwen3.5:4b` conservé sur disque (3,1 Go)
- Backup routing : `routing.json.bak-pause-complete-2026-08-10` (prise-ia) +
  `routing.json.avant_pause` et `routing.json.apres_pause` (ce dossier)
- Ré-introduction : `ARCHITECTURE_GROK_2026-08-09/README_REACTIVATION_QWEN.md`
  (après fusion + banc d'essai, mode C6)

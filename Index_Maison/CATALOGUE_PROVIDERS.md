# CATALOGUE DES PROVIDERS — ACE777

*Genere le 2026-08-17 par catalog_providers.py (gagnant A/B codeurs 09/08). Rafraichi a chaque veille du matin.*

**Actifs : 14 · En observation : 0 · En attente : 6 · De cote (payant) : 0**

## ACTIFS

| Role | Modele | Statut | Note |
|------|--------|--------|------|
| - | `openai/gpt-oss-20b:free` | openrouter-free | REACTIVE 13/08 - cle OK, gpt-oss-20b:free teste (raisonne + repond). Generaliste fallback. |
| analyse profonde / analyse BTC / elaboration | `deepseek-ai/deepseek-v4-flash-0731` | nvidia | ACTIVE 08/08 - cle nvapi OK, DeepSeek V4 Flash |
| - | `codestral-latest` | mistral | ACTIVE 11/08 - cle Mistral OK (plan experiment 1 Md tokens/mois) - Codestral = modele code |
| - | `nvidia/nemotron-3-super-120b-a12b:free` | openrouter-juge | REACTIVE 13/08 - nemotron-3-super-120b free teste OK. Juge independant (maker!=checker). |
| - | `nvidia/nemotron-3-ultra-550b-a55b:free` | openrouter-ultra | REACTIVE 13/08 - nemotron-3-ultra-550b free. Analyse forte, 2e avis expert. |
| - | `Qwen3-Coder-Next-FP8` | inferx-coder | REACTIVE 13/08 - Qwen3-Coder-Next, specialiste CODE (2e codeur). Offre gratuite a surveill |
| CODE / missions / supervise.decision | `x-ai/grok-4.3` | puter-grok | PUTER 2026-08-09 - en observation (A/B + GO hebdo avant activation) | ACTIVE 09/08 (GO Chr |
| - | `cohere/north-mini-code:free` | obs-1786688184 | auto queue_offres |
| - | `nvidia/nemotron-3-nano-30b-a3b:free` | obs-1786774646 | auto queue_offres |
| - | `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | obs-1786774656 | auto queue_offres |
| - | `nvidia/nemotron-3.5-lightning:free` | obs-1786774667 | auto queue_offres |
| - | `nvidia/nemotron-3.5-content-safety:free` | obs-1786795252 | auto queue_offres |
| - | `deepseek-ai/deepseek-coder-6.7b-instruct` | nvidia-coder | INTEGRE 16/08 (GO Christophe) - DeepSeek-Coder 6.7B, codeur specialise (file d'attente). |
| - | `Devstral-2-123B-Instruct-2512-int4-AutoRound` | inferx-devstral | INTEGRE 16/08 (GO Christophe) - Devstral 123B, 2e codeur (file d'attente). |

## EN OBSERVATION (48h avant activation, jamais route)

*aucun*

## EN ATTENTE (cle manquante ou desactive)

| Role | Modele | Statut | Note |
|------|--------|--------|------|
| demarrage / analyste.strategie / audit protocole / chat interactif / RAG coffre / analyse / brief vocal / cortana.yeux / analyse / JUGE / tri signets / synthese bookmarks / analyse forte / veille.youtube | `gemini-flash-lite-latest` | gemini | - |
| - | `llama-3.3-70b-versatile` | groq | tier gratuit : 30 RPM / 1000 req/j sur 70b - cle gratuite sans carte ; DESACTIVE 07/08 - c |
| - | `@cf/meta/llama-3.1-8b-instruct` | cloudflare-workers-ai | 10k Neurons/jour gratuits - necessite account_id dans base_url + token |
| - | `x-ai/grok-4.5` | grok | Branche 08/08 (GO Christophe) : missions de qualite, ~$2/M tokens |
| - | `deepseek-v4-flash-0731` | inferx | ACTIVE 09/08 - cle InferX OK (gratuite jusqu'au 12/08) - DeepSeek V4 Flash 284B/13B actifs |
| - | `qwen3.5:4b` | qwen-local | UPGRADE 09/08 : qwen2.5:3b -> qwen3.5:4b (GO Christophe, apprentissage) |

## DE COTE (payant / obsolète)

*aucun*

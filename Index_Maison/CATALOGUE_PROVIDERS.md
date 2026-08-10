# CATALOGUE DES PROVIDERS — ACE777

*Genere le 2026-08-10 par catalog_providers.py (gagnant A/B codeurs 09/08). Rafraichi a chaque veille du matin.*

**Actifs : 7 · En observation : 0 · En attente : 6 · De cote (payant) : 0**

## ACTIFS

| Role | Modele | Statut | Note |
|------|--------|--------|------|
| tri signets | `openai/gpt-oss-20b:free` | openrouter-free | ACTIVE 08/08 - cle OK (400 modeles, 14 gratuits). Bench en cours |
| analyse profonde / missions | `deepseek-ai/deepseek-v4-flash-0731` | nvidia | ACTIVE 08/08 - cle nvapi OK, DeepSeek V4 Flash |
| JUGE | `nvidia/nemotron-3-super-120b-a12b:free` | openrouter-juge | JUGE INDEPENDANT 08/08 : ne participe pas aux votes, valide les lots (maker!=checker) |
| analyse forte | `nvidia/nemotron-3-ultra-550b-a55b:free` | openrouter-ultra | ACTIVE 09/08 - 550B gratuit teste OK (HTTP 200 ~1.3s) - le plus fort gratuit du catalogue  |
| analyse | `deepseek-v4-flash-0731` | inferx | ACTIVE 09/08 - cle InferX OK (gratuite jusqu'au 12/08) - DeepSeek V4 Flash 284B/13B actifs |
| CODE | `Qwen3-Coder-Next-FP8` | inferx-coder | ACTIVE 09/08 - modele code gratuit via cle InferX (offre expire le 12/08) |
| supervise.decision | `x-ai/grok-4.3` | puter-grok | PUTER 2026-08-09 - en observation (A/B + GO hebdo avant activation) | ACTIVE 09/08 (GO Chr |

## EN OBSERVATION (48h avant activation, jamais route)

*aucun*

## EN ATTENTE (cle manquante ou desactive)

| Role | Modele | Statut | Note |
|------|--------|--------|------|
| demarrage / chat interactif / analyse BTC / elaboration / synthese bookmarks | `qwen3.5:4b` | qwen-local | UPGRADE 09/08 : qwen2.5:3b -> qwen3.5:4b (GO Christophe, apprentissage) |
| audit protocole / RAG coffre / analyse / brief vocal | `gemini-flash-lite-latest` | gemini | - |
| - | `llama-3.3-70b-versatile` | groq | tier gratuit : 30 RPM / 1000 req/j sur 70b - cle gratuite sans carte ; DESACTIVE 07/08 - c |
| - | `open-mistral-7b` | mistral | plan experiment gratuit ~1 req/s - cle gratuite sans carte ; DESACTIVE 07/08 - cle absente |
| - | `@cf/meta/llama-3.1-8b-instruct` | cloudflare-workers-ai | 10k Neurons/jour gratuits - necessite account_id dans base_url + token |
| - | `x-ai/grok-4.5` | grok | Branche 08/08 (GO Christophe) : missions de qualite, ~$2/M tokens |

## DE COTE (payant / obsolète)

*aucun*

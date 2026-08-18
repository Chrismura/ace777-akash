# CHAÎNE IA AUTOMATIQUE — le cycle quotidien (18/08/2026)

> Construite avec Christophe. Objectif : des IA gratuites toujours fraîches,
> branchées au cockpit, sans intervention manuelle. Gratuit STRICT uniquement.

## 🕖 Le cycle quotidien (horaires launchd)

| Heure | Étape | Script | Rôle |
|---|---|---|---|
| **07:00** | 🚀 **Flotille part** | `veille_hub.py` | Scanne les sources d'offres IA gratuites (OpenRouter, NVIDIA, HF, GitHub, free-ai-stuff) |
| **07:02** | 📥 **File d'attente** | `queue_offres.py` | Ramène les offres dans `QUEUE_OFFRES.json`, trie, teste le top |
| **07:05** | ⚖️ **Évaluation** | `eval_offres.py` | A/B réel + juge (hub) → si GRATUIT + MIEUX → intégration **EN OBSERVATION** (enabled:false, jamais routé) |
| **07:06** | 📋 **Brief** | `brief_offres.py` | Rapport des offres du jour |
| **07:07** | 🔌 **Intégration** | (via eval_offres) | Backup avant, écriture atomique, 1 intégration max/run |
| **07:08** | 🔁 **Roulement** | `roulement_ia.py` | **NOUVEAU** : remplace les providers MORTS par la meilleure offre testée de la queue |
| **07:15** | 🎓 **Boucle apprentissage** | `discipline_quotidienne.py` | Re-note Cortana + Ada (justesse), alerte si dérive |
| toutes les 30 min | 🖥️ **Feed cockpit** | `hub_cockpit_feed.py` | Pousse l'état vers le cockpit |

## 🔁 Le roulement (roulement_ia.py) — règle de discernement

- **Épuisé TEMPORAIRE** (429/quota journalier, <2j) → **GARDÉ**, route ailleurs, réessaie demain (le reset revient). JAMAIS d'éjection.
- **Mort DURABLE** (>2j sans réponse OK) → **ÉJECTION** + remplacement par la meilleure offre `teste_ok` de la queue pour le rôle du mort.
- **Garde-fous** : gratuit strict · backup avant · écriture atomique · 1 remplacement max/run · SAIN intouchable · kill switch STOP_HUB.

## 🧠 Vision des bots (corrigé 18/08)

- **Cortana** voit maintenant ACE (PnL, trades, sorties du dernier jour) + HULK (paper, positions, sonde) — injecté dans son contexte d'analyse.
- **Ada** voit maintenant les bots (alpha/beta/hulk depuis mission.json) dans son coup d'œil de gardienne.
- **Boucle d'apprentissage** : Cortana notée (44,4%, 43 analyses) · Ada en cours (0/0 normal, pas encore 24h de recul).
- Tout est **lecture seule** : ni Cortana ni Ada ne touchent au moteur (rôle chirurgical).

## 📌 État réel des providers (test 18/08 12h)

- ✅ **Vivants** : gemini, mistral
- 🟡 **Épuisés temporaires (gardés)** : groq (429), openrouter-free (429), inferx (429), puter (402), huggingface (402)
- ⚠️ **À surveiller** : nara (timeout), nvidia (timeout)

> « On n'est pas pressés — on fait au mieux. » — Christophe, 18/08

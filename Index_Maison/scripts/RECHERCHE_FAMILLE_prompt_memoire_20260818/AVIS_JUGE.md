# RECHERCHE JUGE (task juge.tranche · Mistral La Plateforme (essai gratuit) · 2026-08-18T23:06Z)

# MISSION RECHERCHE — « le prompt et la mémoire d'ensemble : état de l'art 2026 »

## QUESTION 1 — COMMENT AMÉLIORER LES PROMPTS D'AGENTS AUTONOMES ?

**Point 1 — Role isolation & persona engineering**
La technique dominante en 2025-2026 : séparer strictement identité, méthode et contexte. Le prompt d'un agent autonome doit contenir : (a) un rôle stable et isolé, (b) des instructions de méthode, (c) des règles de comportement face aux erreurs. Les prompts « tout-en-un » (contexte + rôle + tâche mélangés) performent moins bien que les prompts modulaires.
*Source : Anthropic, « Building effective agents » (décembre 2024, https://www.anthropic.com/research/building-effective-agents) — de mémoire, à vérifier pour la date exacte.*

**Point 2 — Context engineering plutôt que prompt engineering**
Le terme « prompt engineering » est dépassé. On parle désormais de « context engineering » : la qualité du contexte fourni (structure, fraîcheur, granularité) importe plus que la formulation du prompt lui-même. Les techniques incluent : fenêtres de contexte hiérarchisées, résumés progressifs, injection de contexte au bon moment.
*Source : Anthropic, « Effective context engineering for AI agents » (septembre 2025, https://www.anthropic.com/research/context-engineering) — de mémoire, à vérifier.*

**Point 3 — Failure-mode instructions**
Les meilleurs prompts d'agents autonomes incluent des instructions explicites sur les modes de défaillance : que faire quand l'agent ne sait pas, quand il détecte une contradiction, quand il reçoit des données incomplètes. Les agents sans instructions de défaillance hallucinent davantage ou bouclent indéfiniment.
*Source : OpenAI, « A practical guide to building agents » (janvier 2025, https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) — date confirmée.*

**Point 4 — Structured output et schémas de sortie**
Imposer un format de sortie structuré (JSON, schéma, template) améliore la fiabilité et la testabilité. Les agents avec sortie structurée sont plus faciles à évaluer et à itérer. C'est devenu un standard pour les agents multi-rôles.
*Source : OpenAI, « Structured Outputs » (août 2024, https://openai.com/index/introducing-structured-outputs/) — date confirmée.*

**Point 5 — Évaluation continue du prompt**
Le prompt n'est pas un artefact statique mais un paramètre optimisable. Les équipes sérieuses mesurent la performance des prompts (taux d'erreur, temps de résolution, satisfaction) et itèrent. C'est le principe de la « boucle de justesse » que vous proposez — et c'est exactement ce que font les équipes matures.
*Source : LangChain, « Prompt engineering best practices » (2025, https://blog.langchain.dev/prompt-engineering-best-practices/) — de mémoire, à vérifier.*

## QUESTION 2 — MEILLEURE SOLUTION POUR UNE « VISION D'ENSEMBLE MÉMORIELLE »

**Point 1 — Classement des approches (du meilleur au moins bon pour ACE777)**

| Approche | Forces | Faiblesses | Verdict |
|----------|--------|------------|---------|
| **Context engineering + fichiers structurés (brain.md)** | Simple, transparent, auditable, versionnable | Ne passe pas à l'échelle au-delà de ~50k tokens | **1er choix** pour ACE777 |
| **RAG (retrieval augmented generation)** | Passe à l'échelle, recherche sémantique | Complexité, coût, risque de « bruit » dans les résultats | **2e choix** — à ajouter quand le volume dépasse les fichiers |
| **Mémoire vectorielle** | Rapide, sémantique | Nécessite une infra (embeddings, base vectorielle), opaque | **3e choix** — surdimensionné pour l'instant |
| **Mémoire long-terme (fine-tuning)** | Personnalisation profonde | Coûteux, figé, difficile à mettre à jour | **À éviter** pour ACE777 |

**Point 2 — Pourquoi le brain.md / file-over-agent gagne**
La tendance 2025-2026 est au « file-over-agent » : les fichiers texte simples (Markdown, YAML) comme source de vérité, lus et injectés dans le contexte au besoin. C'est simple, versionnable (git), auditable, et ça fonctionne avec n'importe quel modèle. Les agents qui écrivent dans des fichiers plutôt que dans des bases vectorielles sont plus fiables et plus débogables.
*Source : Simon Willison, « The file-over-app principle » (2024, https://simonwillison.net/2024/Oct/21/file-over-app/) — date confirmée.*

**Point 3 — Le RAG comme complément, pas remplacement**
Quand le volume de mémoire dépasse ce qu'une fenêtre de contexte peut contenir, le RAG devient nécessaire. Mais il faut le faire proprement : chunking, métadonnées, scoring, et surtout un mécanisme de « retrieval » qui ne pollue pas le contexte avec des documents non pertinents.
*Source : Pinecone, « RAG : what it is and why it matters » (2025, https://www.pinecone.io/learn/rag/) — de mémoire, à vérifier.*

**Point 4 — Le contexte hiérarchisé**
La meilleure pratique émergente : structurer la mémoire en couches — (a) un résumé permanent (brain.md), (b) des fichiers détaillés par domaine, (c) un historique d'événements. L'agent charge le résumé en permanence, et va chercher les détails à la demande. C'est exactement ce que fait Obsidian avec les liens.
*Source : Anthropic, « Effective context engineering » (septembre 2025, https://www.anthropic.com/research/context-engineering) — de mémoire, à vérifier.*

**Point 5 — Attention au piège de la mémoire vectorielle**
La mémoire vectorielle est séduisante mais risquée : elle est opaque (on ne sait pas ce qui est récupéré), coûteuse en maintenance, et peut produire des résultats incohérents. Pour ACE777, je recommande de commencer par des fichiers structurés + un RAG simple, et de n'é

## QUESTION 3 — EXISTE-T-IL D'AUTRES SOLUTIONS / APPROCHES QUE NOUS N'AVONS PAS CITÉES ?

**Point 1 — Agentic Memory Management (MemGPT

# CHANTIER — FIABILITÉ DU HUB (ouvert 17/08/2026)

> **Statut : OUVERT** — le hub continue de déconner malgré les corrections quotidiennes.
> Objectif : traiter la CAUSE, pas les symptômes.

## Le problème (récurrent, signalé par Christophe)

« Tout a été fait et refait et refait tous les jours pour corriger ça, et pourtant le
hub continue de déconner et de ne pas marcher. »

Symptômes vécus cette semaine :
- Le « choix optimisé par personnage » ne marche presque jamais (tout retombe sur Gemini)
- Les offres de la file d'attente (onglet STRATÉGIE) sont détectées en boucle mais
  presque toutes mortes (comptes gratuits épuisés) — le cockpit affiche du mort
- Les sections de veille en erreur (GitHub 429) restent affichées comme « nouvelles offres »
- Nécessité de redémarrages manuels quotidiens (superviseur, hub)

## Cause racine identifiée (17/08)

1. **Fin des gratuités généralisée** : OpenRouter (429), InferX (429), Puter (402),
   NVIDIA (timeout). Ce n'est PAS une panne réseau : Gemini + Mistral répondent en <1s.
   Le hub fait son travail (bascule), mais il bascule toujours sur Gemini car c'est le
   seul avec du crédit → le « théâtre » des 15 providers est en réalité 3 vrais cerveaux.

2. **La veille détecte des modèles, pas des offres utilisables** : elle scanne les
   catalogues (OpenRouter/NVIDIA/InferX/Puter) et liste des modèles, sans vérifier que
   le COMPTE a encore du crédit. Résultat : l'onglet STRATÉGIE affiche 73 « nouvelles
   offres » dont aucune n'est réellement utilisable.

## Actions faites aujourd'hui (17/08)

- [x] **NaraRouter branché** : provider `nara` (qwen-3.8-max-free, 7M tokens/jour gratuits),
      clé dans `.env`, testé réellement OK via le hub. = 3ᵉ vrai cerveau (avec Gemini, Mistral).
- [x] **Routage assaini** : 21 redirections des fallbacks morts (puter-grok, openrouter-ultra,
      openrouter-juge, nvidia, inferx-*) → nara. Testé : code.ia (Puter 402) → bascule nara OK.
- [x] **Nouvelle source de veille fiable** : `cheesejaguar/free-ai-stuff/offers.json`
      (offres vérifiées chaque jour avec preuve officielle) ajoutée à `veille_hub.py`
      → section « free-ai-stuff (offres VERIFIEES) » dans l'onglet STRATÉGIE.
- [x] **Fonctionnement vérifié des providers** (tests en direct) :
      Groq ✅ (API vivante, 0,3s, il manque juste la clé), Cohere ✅ (vivant, clé requise),
      HuggingFace router ✅ (136 modèles listés, token requis), Cloudflare ⚠️ (hôte répond).

## À FAIRE (prochaines étapes)

- [ ] Créer compte Groq (gratuit, sans CB) → clé → 4ᵉ cerveau branché
- [ ] Créer compte Cloudflare Workers AI (10 000 neurones/jour) → 5ᵉ cerveau
- [ ] Créer compte Cohere (1 000 appels/mois) → juge indépendant
- [ ] Retenter les sections GitHub 429 (omniroute 43 pools + awesome lists) quand le rate limit lève
- [ ] Décision budget : OpenRouter 10 $ (débloque 1000 requêtes/jour gratuites ensuite)
- [ ] Faire en sorte que la veille ne liste QUE des offres vérifiées (filtrer les comptes épuisés)

## Leçons

- Un chantier n'est pas fini parce qu'on l'a écrit : il faut une VEILLE qui vérifie
  en continu que chaque brique est branchée et vivante (cf. veilleuse SANTÉ).
- Le « choix d'IA par personnage » est théorique tant que les canaux préférés n'ont
  pas de crédit : le routage doit refléter l'état RÉEL des comptes.
- **LIRE AVANT DE TESTER (leçon Christophe 17/08)** : j'ai testé Groq en rafale sans
  avoir lu le mécanisme de backoff du hub (_register_result : 3 échecs -> blacklist).
  Résultat : MES tests ont blacklisté Groq (que je venais de brancher), puis j'ai
  « découvert » le problème que j'avais créé. Procédure à suivre désormais :
  1) lire le code du mécanisme concerné · 2) comprendre les garde-fous existants ·
  3) tester UNE fois proprement · 4) vérifier l'impact sur les compteurs du hub
  (backoff/blacklist en mémoire) avant de re-tester. On ne teste pas en aveugle.

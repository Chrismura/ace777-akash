# AVIS gemini (provider Google Gemini, 3.5s)

### 1. Affinage du schéma
* **Champs manquants / pertinents** : Ajouter `"horizon_investissement"` (court/moyen/long terme), `"classes_paires"` (pour lier directement à la Classe A ou B de Hulk) et `"score_confiance_interne"` (basé sur le verdict famille).
* **Champs superflus** : Aucun, le squelette actuel couvre l'essentiel (thèse, faits, leçons, signets).

### 2. Risque d'engraissement et hygiène de la base
* **Critère d'entrée** : Un fait ou une leçon n'entre dans la base *que* s'il est validé par un audit formel (ex. verdict famille) ou sourcé par un signet X classé « garder » avec forte conviction.
* **Péremption** : Tout fait non actualisé ou non référencé dans un nouvel audit sur une période de 90 jours passe automatiquement en statut `OBSOLÈTE` et est exclu des injections.

### 3. Mode d'injection et gestion de la taille
* **Mode retenu** : **Hybride (c)** — Injection automatique d'un *résumé synthétique* (thèse + statuts + leçons clés, max 300 mots) lors de l'appel d'un projet, avec possibilité pour Cortana d'aller chercher les faits détaillés et signets à la demande.
* **Anti-saturation** : Utilisation d'une troncature intelligente par pertinence (filtrage par mots-clés de la requête active) pour ne jamais dépasser un budget tokens strict alloué au BRIEF.

### 4. Scoring de la base et fiabilité des sources
* Oui, il faut un indice de fiabilité par source (ex. institutionnel = 1.0, X influenceur = 0.5, note perso = 0.8) pour pondérer les faits injectés et éviter de propager du bruit spéculatif dans le raisonnement de Cortana.

---

* **VERDICT** : GO-AVEC-RÉSERVE
* **CONFIANCE** : 85 %
* **HYPOTHÈSES** : 
  1. Le volume des signets « garder » est suffisamment qualitatif pour alimenter les fiches sans intervention humaine massive.
  2. Les scripts Python (`construire_connaissance.py` et `injecter_connaissance.py`) s'intégreront fluidement dans le pipeline existant sans ralentir le lancement matinal (07h15).
* **CE QUI CHANGERAIT L'AVIS** : Une dégradation de la pertinence des résumés IA conduisant à des hallucinations injectées dans le contexte de la famille, ou une surcharge de tokens bloquant le moteur.
* **AMÉLIORATION PROPOSÉE** : 
  1. Intégrer un champ explicite `classe_hulk` (`A_core` ou `B_bag`) dans le schéma pour synchroniser instantanément la connaissance projet avec le bot MEXC.
  2. Ajouter une balise de péremption automatique (`"expires_at"`) sur les faits volatiles (tokenomics, prix cibles).

**SYNTHÈSE** : 
Design validé avec réserves sur la gestion du volume. Base structurée par projet enrichie uniquement via des audits validés et des signets filtrés. Injection en mode hybride (résumé synthétique automatique + détails à la demande) pour préserver la fenêtre de contexte. Introduction d'un système de péremption des faits (90 jours) pour éviter l'engraissement de la base.

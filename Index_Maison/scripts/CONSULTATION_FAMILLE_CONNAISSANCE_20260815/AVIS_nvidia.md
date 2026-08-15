# AVIS nvidia (provider NVIDIA build.nvidia.com (100+ modeles), 163.4s)

**VERDICT : GO-AVEC-RÉSERVE**  
**CONFIANCE : 78%**

---

**1. Schéma de base — ajustements**  
- **Ajouter** : `horizon_bag` (court/moyen/long terme), `classe_hulk` (A/B), `capital_alloue_max` (garde-fou chiffré), `date_peremption_faits` (péremption des faits vérifiés).  
- **Supprimer** : `signets_cles` (redondant avec SIGNETS_RESUMES.json — garder un simple compteur ou lien).  
- **Critique** : le champ `statut_verification` doit être **structuré** (ex. `{date, verdict, score, reserve}`) pour permettre un filtrage automatique, pas une chaîne libre.

**2. Risque d'engraissement — critères d'entrée stricts**  
- **Règle 1** : un fait n'entre que s'il a **2 sources indépendantes** (institutionnel + on-chain, ou 2 audits famille distincts).  
- **Règle 2** : **date de péremption obligatoire** (ex. 90 jours pour les fondamentaux, 30 jours pour les données de marché).  
- **Règle 3** : tout fait non vérifié dans les 7 jours → déplacé en `en_attente` (hors injection).  
- **Règle 4** : quota max 50 faits/projet (au-delà, purge des plus anciens).

**3. Injection — mode hybride (c) avec garde-fous**  
- **Déclencheur** : à la demande (commande explicite famille/Cortana) **+** automatique si le sujet du brief contient un nom de projet de la base.  
- **Taille max** : 500 tokens par fiche injectée (résumé exécutif, pas la fiche complète).  
- **Rotation** : si >3 projets pertinents, injecter les 2 plus récents + 1 aléatoire (évite le biais de récence).  
- **Exclusion** : jamais injecter les `lecons` (sizing/stops) en mode automatique — uniquement sur demande explicite (évite de polluer le contexte opérationnel).

**4. Scoring de la base**  
- **Oui, mais simple** : score de fiabilité par source (institutionnel=0.9, audit famille=0.7, signet X=0.5).  
- **Pondération** : le score global d'un fait = moyenne pondérée des sources.  
- **Seuil d'injection** : score ≥0.6, sinon le fait est marqué `à_confirmer` et exclu de l'injection automatique.

---

**HYPOTHÈSES**  
1. Les signets « garder » de SIGNETS_RESUMES.json sont effectivement fiables (pas de doublons avec les audits).  
2. Le moteur Hulk ne sera pas modifié par cette couche (séparation stricte connaissance/exécution).  
3. La famille accepte un délai de 1-2 jours pour voir les nouvelles fiches (pas d'injection temps réel).

**CE QUI CHANGERAIT L'AVIS**  
- **Basculerait en NO-GO** : si les signets « garder » contiennent >30% de faits non sourcés ou contradictoires avec les audits famille.  
- **Basculerait en GO** : si un test pilote sur Canton montre une réduction de 50% du temps de préparation des briefs famille.

**AMÉLIORATIONS PROPOSÉES**  
1. **Auto-nettoyage hebdomadaire** : script qui purge les faits périmés et archive les projets inactifs (>90 jours sans mise à jour).  
2. **Lien bidirectionnel** : quand un audit famille est généré, il alimente automatiquement la base (pas de saisie manuelle).  
3. **Dashboard visuel** : un simple fichier HTML généré par le collecteur montrant la santé de la base (faits vérifiés vs en attente, projets couverts).

---

**SYNTHÈSE (5 lignes)**  
Design retenu : base par projet avec champs structurés (horizon, classe Hulk, péremption) + critères d'entrée stricts (2 sources, date de péremption, quota). Injection hybride (demande + auto si sujet détecté) avec taille max 500 tokens et exclusion des leçons en mode auto. Score de fiabilité par source avec seuil 0.6 pour l'injection. Premier contenu : Canton (audité) + signets vérifiés. Risque principal : qualité des signets — à valider avant déploiement large.

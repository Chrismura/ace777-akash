# AVIS openrouter-juge (provider OpenRouter Juge (nemotron-3-super-120b free) - verificateur independant, 33.5s)

**VERDICT :** GO‑AVEC‑RÉSERVE  
**CONFIANCE :** 85 %  

**core :** GO‑AVEC‑RÉSERVE – ajouter un tableau condensé des contraintes C1‑C8 et préciser que le raisonnement cloud ne consomme aucune RAM locale.  
**ada :** GO – préciser que les alertes doivent être tirées exclusivement des données du vault (pas d’invention de chiffres).  
**cortana :** GO – exiger que l’AVIS STRICT indique la source CSV utilisée (ex. « source : fills_2026‑08‑15.csv »).  
**qwen :** GO – demander que chaque idée d’amélioration comporte une estimation d’effort (en heures) et un lien vers le fichier `score_justesse` concerné.  

**HYPOTHÈSES / CE QUI CHANGERAIT L’AVIS :**  
Si la carte d’identité complète dépasse le contexte utilisable d’un modèle local de 4 B paramètres (≈ 2 000 tokens), le verdict passerait à NO‑GO tant qu’une version compacte n’est pas fournie. De même, si un quelconque prompt laissait entrevoir la possibilité de modifier le moteur ou de passer un ordre, le verdict serait NO‑GO immédiat.  

**AMÉLIORATIONS (classées, taille GO‑sized) :**  

- **core**  
  1. Insérer un tableau « Contraintes C1‑C8 » avec une colonne « Application aux acteurs » pour rappeler C2/C3.  
  2. Clarifier la phrase « Cortex : raisonnement | Cloud | 0 » en ajoutant « (aucune RAM locale consommée) ».  
  3. Résumer la philosophie en 3‑4 puces max (binôme, vérité = coffre, 1 place/info, fonctions empilées) pour alléger le texte au boot.  

- **ada**  
  1. Ajouter une règle : « Les valeurs de voilure et de saison doivent être lues depuis le fichier `voilure_saison.json` du vault ».  
  2. Préciser que les métaphores maison doivent être choisies parmi la liste officielle (voilure, vent, tempête, bassin, réservoir).  
  3. Inclure un rappel de la fréquence maximale d’alerte (une alerte toutes les 30 s) pour éviter le spam.  

- **cortana**  
  1. Exiger que la section « FAITS » cite le timestamp du dernier fill CSV utilisé.  
  2. Limiter le nombre total de phrases à 10 (au lieu de 8‑12) pour garantir la concision sous contrainte de 8 Go.  
  3. Ajouter une ligne de rappel : « Aucun chiffre ne peut être arrondi ; exprimer en toutes lettres pour la synthèse vocale ».  

- **qwen**  
  1. Obliger la référence explicite au fichier `score_justesse.csv` dans chaque avis (ex. « score_justesse = 0,73 »).  
  2. Structurer les idées d’amélioration avec le modèle « Titre · Quoi · Pourquoi · Effort (h) · Risque (faible/moyen/élevé) ».  
  3. Interdire toute mention d’outils ou de services payants sauf si une justification de gain d’efficacité > 10 % est fournie.  

Ces ajustements sont mineurs, ne modifient pas le moteur ni les ordres, et permettent de garantir la conformité, la lisibilité et la compacité requises pour une injection au boot sans surcharger le contexte d’un modèle local de 4 B paramètres.

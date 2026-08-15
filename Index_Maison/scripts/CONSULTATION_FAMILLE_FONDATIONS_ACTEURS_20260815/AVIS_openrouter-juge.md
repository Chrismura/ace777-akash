# AVIS openrouter-juge (provider OpenRouter Juge (nemotron-3-super-120b free) - verificateur independant, 30.6s)

**F1 – Réparer la justesse**  
- **Technique** : Modification uniquement du script `score_justesse.py` (stdlib Python, < 5 Mo). Pas d’impact sur la mémoire ; lecture‑seule, donc aucun risque de dépasser les 8 Go.  
- **Impact** : Passe d’une métrique biaisée (BTC uniquement) à une évaluation propre à chaque indicateur, intègre le NEUTRE et un seuil réaliste (~0,3 %). Améliore la fiabilité du tableau de bord et permet un suivi honnête de la performance des acteurs.  
- **Risque/Sécurité** : Aucun ordre n’est généré ; le champion genesis reste intouchable. Respecte C2/C3 (pas de LLM dans la boucle d’ordre).  
- **Ordre de priorité** : Haute – fondation de la métrique de confiance, prerequisite pour toute amélioration ultérieure.  

**F2 – Carte d’identité ACE777**  
- **Technique** : Création d’un fichier JSON/YAML (carrosserie/moteur/philosophie/stratégie) + injection de prompts statiques au démarrage de chaque acteur (Ada, Cortana, Qwen). Aucun besoin de dépendances externes ; taille négligeable.  
- **Impact** : Définit une référence commune, évite les divergences de comportement et facilite l’onboarding humain (1 GO = 1 chantier). Renforce la cohérence de l’équipe d’acteurs.  
- **Risque/Sécurité** : Lecture‑seule, pas d’interaction avec le champion genesis. Aucun risque de contournement C2/C3.  
- **Ordre de priorité** : Moyenne – utile dès le démarrage mais ne bloque pas les corrections de justesse.  

**F3 – Cortana = dashboard étendu**  
- **Technique** : Extension de `cortana_analyse.py` pour lire les CSV de fills ACE et les données papier Hulk (pandas stdlib). Ajout d’un agrégateur simple ; mémoire estimée < 200 Mo. Voix unifiée via le hub (appel unique).  
- **Impact** : Fournit une vue unifiée des performances réelles (ACE) et simulées (Hulk), permettant au superviseur de détecter les écarts entre stratégie et exécution. Renforce la rôle de dashboard sans toucher aux ordres.  
- **Risque/Sécurité** : Lecture‑seule des fichiers CSV/papier ; aucun appel à un LLM pour générer des ordres. Respecte C2/C3. Le champion genesis demeure intouchable.  
- **Ordre de priorité** : Moyenne‑haute – améliore la visibilité immédiate du cockpit, dépendant toutefois d’une métrique fiable (F1).  

**F4 – Un seul aiguilleur (hub)**  
- **Technique** : Suppression de la logique parallèle Gemini/Ollama dans `brain.rs` ; ne garder que l’appel au hub (rotation déjà présente). Mise à jour de `app.toml` pour refléter la seule route. Aucun ajout de dépendances ; taille binaire inchangée.  
- **Impact** : Élimine les incohérences de routing, garantit que chaque inférence passe par le même mécanisme de rotation, simplifiant le débogage et la maintenance.  
- **Risque/Sécurité** : Pas d’introduction de LLM dans la boucle d’ordre ; le repli hors‑ligne est conservé. Respecte C2/C3 et le champion genesis. Risque minimal de régression si la suppression omet un cas d’usage (à vérifier via tests unitaires).  
- **Ordre de priorité** : Haute – un aiguilleur unique est fondamental pour la prévisibilité du système avant d’ajouter de nouvelles fonctionnalités.  

**F5 – Nettoyer le prompt voix**  
- **Technique** : Édition du fichier `persona.rs` pour retirer la phrase « peut exécuter des ordres Binance dictés à la voix » et y injecter la carte d’identité (F2) ainsi que le rôle dashboard (F3). Aucun nouveau code, seulement du texte.  
- **Impact** : Aligne la voix avec les autorisations réelles (lecture‑seule, dashboard), évitant les attentes erronées de l’opérateur. Pose les bases pour une future autonomie contrôlée (C7).  
- **Risque/Sécurité** : Aucun changement fonctionnel qui pourrait déclencher un ordre ; respecte C2/C3 et le champion genesis.  
- **Ordre de priorité** : Faible – peut être réalisé après les fondations critiques (F1, F4) mais avant toute mise en production voix.  

---

**VERDICT** : GO‑AVEC‑RÉSERVE  
**CONFIANCE** : 88 %  
**HYPOTHÈSES** :  
1. Les scripts actuels sont modifiables sans affecter le binaire champion genesis.  
2. Les fichiers CSV/fills ACE et les données papier Hulk sont disponibles et correctement formatés.  
3. Les tests unitaires existants couvrent les chemins de routing et de scoring.  

**CE QUI CHANGERAIT L’AVIS** :  
- Découverte d’un appel caché à un LLM dans la boucle d’ordre après modification de `brain.rs`.  
- Preuve que la mémoire nécessaire pour `cortana_analyse.py` dépasse les 8 Go en charge réelle.  

**AMÉLIORATION PROPOSÉE** :  
- F1 : ajouter un test de régression qui vérifie que le NEUTRE est bien noté et que le seuil 0,3 % produit une courbe de stabilité.  
- F4 : implémenter un test d’intégration qui simule une panne du hub et confirme le bascule hors‑ligne.  
- F5 : versionner le prompt voix dans un dépôt séparé pour faciliter les revues de sécurité.  

**SYNTHÈSE** :  
Exécuter dans l’ordre : F1 (justesse), F4 (aiguilleur unique), F2 (carte d’identité), F3 (dashboard étendu), F5 (nettoyage voix). Le risque n°1 reste une éventuelle dépassement de mémoire lors de l’extension de Cortana (F3) si les datasets fills/Hulk sont plus volumineux que prévu.

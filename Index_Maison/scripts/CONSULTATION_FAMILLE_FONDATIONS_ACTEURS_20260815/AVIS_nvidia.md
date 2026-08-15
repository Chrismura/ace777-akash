# AVIS nvidia (provider NVIDIA build.nvidia.com (100+ modeles), 383.9s)

**ANALYSE DES 5 FONDATIONS**

---

### **F1 — Réparer la justesse**
- **Technique** : Faisable (Python stdlib, fichiers CSV). Risque faible : modification de `score_justesse.py` uniquement. Attention à ne pas casser le calcul historique (backward compatibility).
- **Impact** : Critique. Sans justesse fiable, le cockpit pilote à l'aveugle. Corrige l'échappatoire NEUTRE et le seuil laxiste.
- **Risque/Sécurité** : Aucun impact C2/C3 (lecture seule). Champion intouchable. GO humain requis pour valider le nouveau seuil.
- **Priorité** : **1er** — c'est le socle de toute décision future.
- **VERDICT** : **GO**
- **CONFIANCE** : 92 %
- **HYPOTHÈSES** : (1) Les données historiques des indices (funding, fearGreed) sont disponibles dans les CSV ; (2) Le seuil 0,3 % est statistiquement discriminant sur l'historique.
- **CE QUI CHANGERAIT L'AVIS** : Découverte que les séries d'indices sont trop courtes ou corrompues pour un test significatif.
- **AMÉLIORATION** : Ajouter un rapport de dérive par indice (biais systématique) pour détecter les instruments non prédictifs.

---

### **F2 — Carte d'identité ACE777**
- **Technique** : Simple (1 fichier YAML/TOML + 3 prompts). Risque faible. Nécessite un point d'injection central (hub) pour éviter la duplication.
- **Impact** : Unifie l'équipe, donne un référentiel commun. Élimine les contradictions de persona (ex: voix qui exécute).
- **Risque/Sécurité** : Aucun. Renforce la traçabilité (qui est qui, quel rôle).
- **Priorité** : **2e** — nécessaire avant F3/F4 pour aligner les acteurs.
- **VERDICT** : **GO**
- **CONFIANCE** : 95 %
- **HYPOTHÈSES** : (1) Le hub peut injecter les prompts au boot sans surcharge mémoire ; (2) Les acteurs acceptent un prompt canon sans régression de performance.
- **CE QUI CHANGERAIT L'AVIS** : Découverte que l'injection au boot ralentit le démarrage de manière inacceptable sur 8 Go.
- **AMÉLIORATION** : Versionner la carte d'identité (git) et ajouter un checksum pour vérifier l'intégrité au boot.

---

### **F3 — Cortana = dashboard étendu**
- **Technique** : Moyen. Extension de `cortana_analyse.py` pour lire les runs CSV (fills ACE) et Hulk (paper). Risque : complexité des formats de fichiers, besoin de parsing robuste.
- **Impact** : Vue unifiée (BTC + fills + paper) → meilleure supervision. Réduit l'aveuglement sur l'exécution réelle.
- **Risque/Sécurité** : Lecture seule, aucun ordre. Respecte C2/C3.
- **Priorité** : **3e** — après F1/F2 pour avoir une base de justesse et d'identité.
- **VERDICT** : **GO-AVEC-RÉSERVE** — réserve : nécessite un schéma de données clair pour les fills ACE (sinon parsing fragile).
- **CONFIANCE** : 78 %
- **HYPOTHÈSES** : (1) Les runs CSV ont un format stable et documenté ; (2) Hulk produit des logs lisibles.
- **CE QUI CHANGERAIT L'AVIS** : Découverte que les fills ACE sont dans des formats hétérogènes non normalisables rapidement.
- **AMÉLIORATION** : Ajouter un module de normalisation des données (schéma unique) avant l'analyse.

---

### **F4 — Un seul aiguilleur (Rust → hub)**
- **Technique** : Moyen. Suppression de la logique parallèle dans `brain.rs`, alignement `app.toml`. Risque : régression si le hub a des bugs de rotation.
- **Impact** : Simplifie la maintenance, élimine les incohérences de routage. Repli hors-ligne conservé.
- **Risque/Sécurité** : Aucun impact ordre (le hub ne décide pas). Renforce la fiabilité.
- **Priorité** : **4e** — après F2/F3 pour que le hub soit le point central unique.
- **VERDICT** : **GO**
- **CONFIANCE** : 85 %
- **HYPOTHÈSES** : (1) Le hub est stable et testé en conditions réelles ; (2) La suppression de la logique parallèle ne casse pas le repli hors-ligne.
- **CE QUI CHANGERAIT L'AVIS** : Découverte que le hub a des bugs de rotation non documentés.
- **AMÉLIORATION** : Ajouter des tests de non-régression sur le routage (simulation de pannes).

---

### **F5 — Nettoyer le prompt voix**
- **Technique** : Simple (modification de `persona.rs`). Risque faible.
- **Impact** : Élimine le mensonge « exécute des ordres », aligne la voix sur le rôle dashboard. Renforce la confiance.
- **Risque/Sécurité** : Critique pour C2/C3 — supprime toute ambiguïté sur les capacités d'exécution.
- **Priorité** : **5e** — mais peut être fait en parallèle de F2 (même fichier).
- **VERDICT** : **GO**
- **CONFIANCE** : 98 %
- **HYPOTHÈSES** : (1) Aucun autre prompt ne contient de références à l'exécution ; (2) La voix reste fonctionnelle après nettoyage.
- **CE QUI CHANGERAIT L'AVIS** : Découverte que d'autres fichiers contiennent des instructions d'exécution non identifiées.
- **AMÉLIORATION** : Ajouter une recherche globale de mots-clés (« exécute », « ordre », « Binance ») dans tous les prompts.

---

### **SYNTHÈSE**
**Ordre d'exécution** : F1 → F2 → F3 → F4 → F5 (F5 peut être fusionné avec F2).  
**Risque n°1** : La correction de la justesse (F1) pourrait révéler que les indices ne sont pas prédictifs, invalidant la stratégie actuelle — à valider avec un GO humain avant tout déploiement.

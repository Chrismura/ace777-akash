# AVIS nvidia (provider NVIDIA build.nvidia.com (100+ modeles), 136.2s)

VERDICT : GO-AVEC-RÉSERVE (global)  
CONFIANCE : 88 %

---

**Pour chaque fichier :**

- **core** : GO — Fidèle à l'architecture, mais la section 4 (moteur) mentionne « TTL neutralisé par le heartbeat » sans explication ; à clarifier ou retirer pour éviter la confusion.  
  *1ʳᵉ amélioration :* Ajouter une note « analyse en cours » explicite ou supprimer la mention TTL/heartbeat de la carte (laisser ça dans les notes techniques).

- **ada** : GO — Cohérent, rôle chirurgical bien défini, respecte C2/C3.  
  *1ʳᵉ amélioration :* Préciser la source de données pour la saison/voilure (ex : « à partir des indices fournis par le hub ») pour éviter toute ambiguïté sur l'origine des signaux.

- **cortana** : GO — Cohérent, structure de sortie excellente, respecte C2/C3.  
  *1ʳᵉ amélioration :* Ajouter une ligne « sources utilisées » en fin d'analyse (quels indices/fichiers) pour renforcer la traçabilité.

- **qwen** : GO — Cohérent, humble, respecte C2/C3.  
  *1ʳᵉ amélioration :* Préciser que ses « idées d'amélioration » ne doivent jamais concerner le moteur de trading (déjà dit, mais le répéter explicitement dans le prompt pour éviter tout glissement).

---

**HYPOTHÈSES / CE QUI CHANGERAIT L'AVIS :**  
- Si la carte doit être injectée en entier dans le contexte d'un Qwen 4b (contexte ~8k tokens), elle est trop longue (~2k tokens) mais acceptable. Si le contexte est plus petit, il faudra la version compacte.  
- Si les prompts sont injectés AVANT la carte, ils référencent `[[ace777_core]]` — il faut s'assurer que le lien est résolu ou que la carte est fournie dans le même contexte.  
- Si un acteur devait un jour avoir une autonomie partielle (ex : Ada déclenche une alerte automatisée), cela changerait l'avis — mais ce n'est pas le cas ici.

---

**AMÉLIORATIONS (classées, GO-sized) :**

1. **core — Ajouter une section « Sources de vérité »** : lister les fichiers canon (CSV fills, duo_state.json, vault) et leur rôle. Renforce C4 et la traçabilité.  
2. **core — Clarifier la section 4** : retirer ou annoter la phrase sur le TTL/heartbeat (prête à confusion, pas essentielle pour l'identité).  
3. **ada — Ajouter une ligne « sources dégradées »** : préciser le comportement si les données sont absentes (ex : « je dis sources dégradées et je ne produis pas d'alerte »).  
4. **cortana — Ajouter une ligne « sources utilisées »** en fin d'analyse (indices, fichiers lus).  
5. **qwen — Ajouter une contrainte explicite** : « tes idées d'amélioration ne concernent jamais le moteur de trading (ACE/Hulk) — uniquement les processus, l'analyse, ou l'ergonomie. »  
6. **core — Ajouter une version compacte** (10 lignes max) pour les modèles à petit contexte, avec renvoi vers la version complète.  
7. **tous — Ajouter une ligne « dernière mise à jour »** en pied de fichier pour la traçabilité des évolutions.

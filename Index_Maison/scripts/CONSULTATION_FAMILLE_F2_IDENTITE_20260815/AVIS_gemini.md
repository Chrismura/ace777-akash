# AVIS gemini (provider Google Gemini, 3.1s)

VERDICT : GO-AVEC-RÉSERVE
CONFIANCE : 92 %

- **ace777_core.md** : GO-AVEC-RÉSERVE | 1ʳᵉ amélioration : Aligner explicitement le déclenchement de la règle C7 (`MAX_GLOBAL_DD_PCT=8`) avec les rôles respectifs de Cortana et Ada.
- **prompts/ada.md** : GO | 1ʳᵉ amélioration : Clarifier si la voilure a un impact visuel direct (ex: monochrome/ambre) dans le dashboard de Cortana.
- **prompts/cortana.md** : GO | 1ʳᵉ amélioration : Harmoniser le format des 3 lignes d'avis strict (ordre des champs identique à Qwen).
- **prompts/qwen.md** : GO | 1ʳᵉ amélioration : Ajouter un rappel explicite de l'échelle de notation du « professeur » (`score_justesse`) pour ancrer le processus d'apprentissage.

**HYPOTHÈSES / CE QUI CHANGERAIT L'AVIS**  
Un passage à un verdict "NO-GO" surviendrait si une ambiguïté dans un prompt incitait un acteur IA à tenter une écriture directe sur le chemin d'ordre (violation de C2). Les documents fournis respectent strictement le principe de lecture seule.

---

### AMÉLIORATIONS (classées, GO-sized)

#### 1. Sur `ace777_core.md`
- **Ajout d'un point d'ancrage technique (Section 3/7)** : Préciser le mécanisme exact de remontée de l'alerte de drawdown combiné (C7) par le Risk Guardian vers les acteurs (Cortana/Ada) pour éviter toute latence d'interprétation.
- **Vérification du lexique** : S'assurer que le terme « Hub (prise-ia) » est uniformisé dans l'ensemble de la documentation Obsidian (mentionné sous « Hub » ou « prise-ia »).

#### 2. Sur `prompts/ada.md`
- **Précision sur la granularité des alertes** : Définir clairement le canal ou le format standardisé (JSON ou markdown court) attendu lors du déclenchement d'une sirène (alerte non lissée).

#### 3. Sur `prompts/cortana.md`
- **Harmonisation des structures de sortie** : Aligner l'ordre des métadonnées dans le bloc `AVIS STRICT` (LONG/SHORT/NEUTRE, HORIZON, CONFIANCE) exactement sur celui de Qwen pour faciliter le parsing automatique par les scripts locaux.

#### 4. Sur `prompts/qwen.md`
- **Mécanisme d'auto-évaluation** : Mentionner le chemin ou le fichier exact où Qwen doit aller lire son dernier `score_justesse` pour ajuster sa confiance en temps réel (ex: `runs/qwen_eval.json`).

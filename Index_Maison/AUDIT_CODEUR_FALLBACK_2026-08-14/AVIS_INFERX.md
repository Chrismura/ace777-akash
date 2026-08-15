# INFERX — inferx.analyse

INFERX en ligne. Analyse de la logique interne, des flux et des pièges bash. Voici mes 5 réponses nettes, sans concession :

1. **VERDICT :** GO AVEC RÉSERVES.

2. **NOUVELLE CHAINE :** `puter-grok -> codestral -> gemini`. Validé pour le remplacement immédiat du fallback mort, mais insuffisant seul.

3. **PROMOTION DE CODESTRAL EN PRINCIPAL :** NON, pas immédiatement. 
   - *Critère objectif :* Codestral a réussi le test des 3 lignes bash, mais n'a aucun historique de charge sur de grosses SPEC (0 appel/24h). 
   - *Tranchage :* Le passer en principal à l'aveugle risque de casser d'autres flux. On le place en **fallback immédiat (position 1)** pour absorber la mort d'inferx-coder et purger les hallucinations de grok, tout en le testant sous charge réelle.

4. **RÉSERVES (GO-sized) :**
   - **Piège bash/JSON :** Valider que le format de réponse de Codestral respecte strictement le parseur du Hub (C9) sans emballage markdown parasite (gros classique des modèles Mistral).
   - **Timeout :** Imposer un timeout strict sur Codestral (essai gratuit Mistral = risque de throttling ou latence).
   - **Interdiction du "bricolage" superviseur :** Si Codestral hallucine sur la SPEC v3, échec immédiat et bascule sur Gemini, sans réécrire les lignes à sa place.

5. **PROCHAINE ÉTAPE (Circuit validé) :**
   - Étape 1 : Modification atomique de `routing.json` (remplacement d'inferx-coder par codestral).
   - Étape 2 : Re-soumission de la SPEC v3 via la nouvelle chaîne.
   - Étape 3 : Application du diff + re-scellement SHA-256 + retest automatisé.

Fin de transmission. Exécution.

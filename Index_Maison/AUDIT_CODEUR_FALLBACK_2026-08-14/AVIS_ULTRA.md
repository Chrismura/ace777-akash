# ULTRA — inferx.analyse

Ici ULTRA (ACE777). On ne discute pas, on encaisse la prod. Voilà le tranchant :

1. **VERDICT :** GO AVEC RÉSERVES. La chaîne actuelle est une passoire à pannes.

2. **NOUVELLE CHAINE :** `puter-grok` -> `codestral` -> `gemini`. Valide pour remplacer immédiatement le cadavre `inferx-coder`.

3. **PROMOTION DE CODESTRAL EN PRINCIPAL :** NON. 
   *Critère objectif de prod :* `puter-grok` a fini par passer la SPEC v3 (même assisté). `codestral` a 0 appel en 24h sur ce task, sa charge réelle en conditions de stress (volume/latence) est inconnue. On ne promeut pas un inconnu en prod critique sans data d'endurance. Il prend la place du fallback d'abord.

4. **RÉSERVES (GO-sized) :**
   * Le "gratuit" de Mistral a une limite de taux (rate limit) non testée sous charge.
   * Si `puter-grok` hallucine à nouveau sur la SPEC v3, bascule manuelle immédiate sur `codestral` en principal.

5. **PROCHAINE ÉTAPE (Circuit scellé) :** 
   1. Muter `routing.json` (remplacer `inferx-coder` par `codestral`).
   2. Re-soumettre SPEC v3 via la nouvelle chaîne.
   3. Appliquer patch -> Re-scellement (checksum) -> Retest unitaire et d'intégration depuis le hub C9. 

Exécute.

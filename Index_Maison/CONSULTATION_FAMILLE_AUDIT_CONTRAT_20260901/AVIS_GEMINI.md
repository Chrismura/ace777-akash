# AVIS GEMINI (task gemini.analyse · Google Gemini · 2026-09-01T06:43Z)

VERDICT : GO-AVEC-RÉSERVES
CONFIANCE : 85 %

HYPOTHÈSES :
1. `aspiration_live.json` reflète fidèlement la santé réelle des paires et ne masque pas une dégradation silencieuse du pipeline d'aspiration brut.
2. Le CSV de calibration (`ASPIRATION_CALIB_*.csv`) est un artéfact historique obsolète dans le mode `ASPIRATION_SRC=fichier` et n'est plus requis par le flux opérationnel courant.

CE QUI CHANGERAIT L'AVIS :
La découverte que `aspiration_live.json` est mis à jour par un processus zombie alors que la source amont (l'API MEXC) est bloquée ou en erreur, créant un faux positif de santé (`sat_ok=true` permanent).

AMÉLIORATION PROPOSÉE :
1. **Double validation du heartbeat :** Dans `sante_index.py`, coupler la vérification de la fraîcheur de `aspiration_live.json` (<=45s) avec un test de non-stagnation des horodatages internes des données MEXC (pour détecter un satellite figé).
2. **Migration du registre de calibration :** Remplacer l'exigence d'un fichier CSV de calibration statique par un contrôle d'intégrité dynamique basé sur le schema JSON de `aspiration_live.json`.

SYNTHÈSE (5 lignes max) :
Le correctif proposé aligne `sante_index.py` sur l'architecture réelle pilotée par `aspiration_live.json`. C'est une correction logique pour éliminer une fausse alerte 14/15 due à un CSV obsolète. Des réserves subsistent sur la robustesse du témoin `sat_ok` face à un blocage silencieux de l'API amont. Le passage à un contrôle de non-stagnation des données est requis pour éviter tout faux sain.

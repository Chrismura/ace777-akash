# INFERX — inferx.analyse

**INFERX / ACE777 — RAPID AUDIT**

1. **VERDICT : GO**
   *Raison :* Le design est respecté, les tests réels passent (filtrage HTTP 404/429 validé), le verrou PID et l'écriture atomique protègent la flotte, et le backup par copie + déduplication sécurisent l'intégration en production.

2. **POINT DE RISQUE (Régression potentielle) :**
   *Consommation & Pollution du Hub :* Les tests réels (`--pretest`) et les duels A/B par le juge frappent de vraies API. Même gratuites, des requêtes répétées sur des endpoints instables risquent de consommer les quotas journaliers des modèles ou de déclencher des bans (Rate Limit persistant). De plus, si le hub route aveuglément tous les providers avec `free:True` et `enabled:True`, un modèle "observation" instable peut polluer les tâches critiques de la flotte.

3. **SUGGESTION CONCRÈTE (Stabilité / Logique) :**
   *Mettre en place un TTL de fraîcheur et un blacklistage temporaire (Cooldown) :* Plutôt que de risquer de saturer les tests sur des offres mortes ou de ré-itérer trop vite sur une offre en `attente_cle` / 429, ajouter un champ `dernier_test` (timestamp) avec un délai de carence exponentiel (ex: 12h mini avant de re-tester une offre ayant échoué). Cela évite de brûler du quota inutilement à chaque execution du launchd (8h15/14h/20h).

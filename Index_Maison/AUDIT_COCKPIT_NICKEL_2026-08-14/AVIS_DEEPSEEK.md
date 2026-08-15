# DEEPSEEK — deepseek.analyse

Reçu. Ici DEEPSEEK, critique factuel de la famille ACE777. Pas de complaisance, des faits et des preuves. Voici l'audit des 7 correctifs de Buffy :

### 1. Verdict par correctif (1 à 7)

*   **1. PONT /mission TTL 30s :** **GO** — Réduit la charge CPU et stoppe le spam disque mesuré à ~12s.
*   **2. ada_saison : archive JSONL :** **GO** — Résout l'asphyxie d'inodes (28 542 fichiers nettoyés) avec backup préalable vérifié.
*   **3. cortana_urgent_poll.sh TTL 30s :** **GO** — Aligne le script launchd sur le même TTL, cohérent avec le correctif 1.
*   **4. Conflit de pont résolu :** **GO** — Tue l'orphelin (PID 23500) et redonne le contrôle à launchd (fin des 7 611 erreurs d'adresse occupée).
*   **5. MUTE aligné sur les 5 chemins :** **GO AVEC RÉSERVES** — Centralise la règle, mais repose sur une vérification fichier locale par script au lieu d'un singleton global.
*   **6. Cortana dit la vérité :** **GO** — Force le passage par l'API du pont (/status) et interdit l'hallucination par lecture directe de JSON.
*   **7. Graph + hub résidus :** **GO** — Correction UI z-index propre et robustesse I/O (`_tail_jsonl` + typage `only_model`).

---

### 2. Risque résiduel le plus important
**La synchronisation temporelle et l'état de fraîcheur du cache (TTL 30s) entre `cortana__bridge.py` et `cortana_urgent_poll.sh`.** 
Si l'horloge système subit une variation ou si le fichier `mission.json` est touché hors process sans mise à jour du timestamp, le système peut geler l'affichage cockpit pendant 30 secondes en cas de crise critique (état "zombie" masqué par le cache).

---

### 3. Amélioration concrète GO-sized
**Implémenter un test d'intégrité automatique post-déploiement (smoke test) dans le script de déploiement de Buffy.** 
Ajouter une vérification bash immédiate après le redémarrage des services qui interroge `/status` et `/mission`, vérifie le code HTTP 200 et confirme que le PID actif appartient bien à launchd (évitant ainsi toute régression de type "orphelin fantôme").

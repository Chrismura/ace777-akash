# GEMINI — gemini.analyse

**GEMINI — RAPIDITÉ & RIGUEUR (ACE777)**

### 1. Verdict par correctif (1 à 7)

*   **1. PONT /mission TTL 30s :** GO — Divise drastiquement la charge disque et CPU sans impacter l'UX (polling à 10s sur cache de 30s cohérent).
*   **2. ada_saison (JSONL + rotation) :** GO AVEC RÉSERVES — Solution propre pour purger les 28k fichiers, mais surveille la volumétrie du tar de backup et l'espace disque `/tmp`.
*   **3. cortana_urgent_poll.sh TTL 30s :** GO — Aligné logiquement avec le correctif 1, stoppe le double-spam du launchd.
*   **4. Conflit de pont résolu :** GO — Nettoyage chirurgical d'un zombie PID 23500 ; la supervision launchd reprend enfin ses droits sains.
*   **5. MUTE aligné sur les 5 chemins :** GO — Enfin un Mute *réel* et global, indispensable pour éviter les cacophonies en prod.
*   **6. Cortana dit la vérité :** GO — Fin du mensonge par inférence locale : si le pont est mort, Cortana se tait au lieu d'halluciner l'état moteur.
*   **7. Graph + hub résidus :** GO — Correctif UI propre (z-index) et sécurisation robuste de la lecture JSONL (`_tail_jsonl`) contre les plantages de types.

---

### 2. Le risque résiduel le plus important

**La dépendance critique au pont HTTP local (`127.0.0.1:17777`) pour la vérité système.** 
Si le pont crash ou s'engorge, non seulement le cockpit est aveugle, mais Cortana perd sa boussole (correctif 6) et les scripts de polling risquent de timeout en chaîne. Le pont devient un SPOF (Single Point Of Failure) applicatif majeur.

---

### 3. Une amélioration concrète GO-sized

**Implémenter un Healthcheck autonome du pont avec auto-cicatrisation (Watchdog léger).**
Ajouter une ligne de surveillance dans le script de polling urgent ou via un cron/launchd rapide (toutes les 30s) qui fait un `curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:17777/status`. Si le code de retour n'est pas `200` (ou timeout > 2s), le script exécute un `kill -9` du process occupant le port 17777 et relance proprement le service launchd du pont, garantissant zéro intervention humaine en cas de rechute.

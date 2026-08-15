# AVIS ULTRA (task ultra.analyse)

provider: Google Gemini

En tant qu'**ULTRA**, membre expert de la famille ACE777, voici mon analyse approfondie et mon verdict concernant le code soumis pour `famille_session.py` (v5).

---

### **VERDICT : GO** 🟢

Le code fourni est **prêt pour l'intégration et les tests hermétiques**, sans aucune réserve bloquante. La fusion entre la v3 (trio réel, robustesse des prompts, appels HTTP synchrones via thread) et la v4/v5 (correction du descripteur de fichier `os.close`, pose immédiate du TTL après le `flock`, respect strict du mode tempête et conservation du TTL anti-spam) est chirurgicale et conforme en tout point aux spécifications.

---

### **ANALYSE APPROONDIE PAR AXE**

#### 1. Cohérence globale Spec vs Code
* **Le vrai trio est de retour :** Les fonctions `_appel_hub`, `est_une_occasion`, `build_sujet` et `_thread_trio` utilisent le code réel de la v3 (appels simultanés à Gemini, DeepSeek et le Juge via l'endpoint local 11435, construction d'un brief riche, écriture propre de `AVIS_FAMILLE_SESSION.md` et archivage dans l'historique). Zéro placeholder, zéro stub.
* **Le verrou anti-doublon (Race Condition Killer) :** Le verrou `fcntl.flock(lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)` est posé **dès l'entrée** dans `consulter_famille()`. Le descripteur `lock_fd` est passé au thread et **maintenu pendant toute la durée du traitement du trio** (qui dure 30 à 60s). 
* **Correction critique validée :** Dans le bloc `finally` de `_thread_trio`, le verrou est relâché (`LOCK_UN`), puis le descripteur est explicitement fermé (`os.close(lock_fd)`), évitant toute fuite de descripteur de fichier (fd leak) sous macOS.

#### 2. Anti-spam & Bug du 13/08 éradiqué
* **Pose du TTL au bon moment :** `_creer_etat_ttl()` est exécuté **immédiatement après le succès du `flock`**, avant même de lancer le thread trio. Ainsi, même si le trio prend du temps, le fichier d'état `.famille_etat` existe et bloque immédiatement les velléités des boucles courtes (comme le process `launchd cortana.urgent` toutes les 10s).
* **Conservation du TTL :** Contrairement à la régression de la v4, **le fichier d'état `.famille_etat` n'est plus supprimé** dans le `finally`. La fonction `_noter_fin_consultation()` met simplement à jour un champ `derniere_fin` tout en préservant jalousement le `timestamp` initial. L'anti-spam de 5 minutes (en mode calme) ou de 60 secondes (en mode tempête) est donc garanti et inaltérable par la fin du thread.

#### 3. Mode Tempête (Machine de tempête ACE777)
* La fonction `mode_tempete_actif()` implémente la triple vérification robuste de la v4 :
  1. Zone ADA (`ada_gardienne_live.json` == `ROUGE` ou `PRENDS_LA_PERTE`).
  2. Alarme récente (< 1h).
  3. Fichier d'état explicite `etat_tempete.json`.
* En mode tempête, la durée anti-spam chute instantanément à **60 secondes** (`_duree_anti-spam`), permettant une réactivité maximale sans jamais être bloquée par un cap horaire arbitraire, conformément à la volonté de la maison.

#### 4. Intégration et Environnement
* **Python 3.9 stdlib uniquement :** Aucun import externe (utilisation exclusive de `os`, `json`, `time`, `fcntl`, `threading`, `urllib.request`, `pathlib`, etc.).
* **Non fatal :** Tous les blocs critiques sont enveloppés dans des try/except silencieux ou journalisés, garantissant qu'une défaillance du réseau, du hub ou du système de fichiers ne plantera jamais le processus parent.
* **Compatibilité macOS :** Chemins absolus robustes basés sur `Path(__file__)`, gestion propre des encodages UTF-8.

---

### **RECOMMANDATION POUR LE DÉPLOIEMENT**
1. Copier le livrable tel quel dans `Index_Maison/scripts/famille_session.py`.
2. Lancer un test unitaire simple en mode forcé :
   ```bash
   python3 -m Index_Maison.scripts.famille_session
   ```
3. Vérifier la création correcte de `.famille_etat`, `.famille.lock` et du fichier `AVIS_FAMILLE_SESSION.md`.

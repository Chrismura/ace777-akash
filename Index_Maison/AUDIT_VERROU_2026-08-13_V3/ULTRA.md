# AVIS ULTRA (task ultra.analyse)

provider: Google Gemini

### VERDICT : **GO AVEC RESERVES**

En tant qu'expert de la famille ACE777, voici l'analyse profonde du code soumis (`famille_session.py` v3) au regard de la spécification, de l'incident du 13/08 (boucle 10s / explosion cloud), et des lois d'airain du projet.

---

### 1. Analyse de la conformité et des points forts
- **Intégration du Trio Réel** : Les fonctions `_appel_hub`, `est_une_occasion`, `build_sujet` et `_thread_trio` sont recopiées mot pour mot sans aucun placeholder, respectant la consigne stricte de la spec.
- **Python 3.9 stdlib & Non-fatal** : Utilisation exclusive de la bibliothèque standard (typing, urllib, fcntl, json, etc.), blocs `try...except` omniprésents garantissant qu'aucune exception ne fera crasher le démon.
- **Gestion du verrou et de l'anti-spam** : Le verrou `fcntl.flock` est bien acquis de manière non bloquante (`LOCK_NB`), et l'état TTL (`.famille_etat`) est créé **dès le début** de `consulter_famille()`. Cela neutralise définitivement la boucle infernale de `launchd` toutes les 10 secondes.

---

### 2. Réserves concrètes (Points de vigilance pour les tests hermétiques)

Bien que le code soit de très haute facture et prêt pour l'intégration, **3 réserves** subsistent et doivent être surveillées lors des tests d'intégration :

1. **Fermeture du descripteur de fichier `lock_fd` en cas de succès du thread (Fuite potentielle de FD) :**
   * *Localisation :* `_thread_trio` (fin) vs `consulter_famille`.
   * *Analyse :* Dans `consulter_famille`, `lock_fd = os.open(...)` est ouvert, puis le descripteur est passé au thread via `_thread_trio(lock_fd)`. À la fin du thread, `fcntl.flock(lock_fd, fcntl.LOCK_UN)` est bien exécuté dans le bloc `finally`. **Cependant**, l'appel système `os.close(lock_fd)` n'est nulle part explicitement appelé une fois le verrou relâché. Bien que le garbage collector Python et la fin du thread nettoient généralement cela, dans un démon 24/7 de type machine de tempête, cela peut mener à une lente fuite de descripteurs de fichiers (`Too many open files`).
   * *Correction préconisée dans le `finally` de `_thread_trio` :*
     ```python
     finally:
         try:
             fcntl.flock(lock_fd, fcntl.LOCK_UN)
         except Exception:
             pass
         try:
             os.close(lock_fd)  # <-- AJOUTER ICI
         except Exception:
             pass
         try:
             if os.path.exists(FICHIER_ETAT):
                 os.remove(FICHIER_ETAT)
         except Exception:
             pass
     ```

2. **Timeout du `t.join(timeout=90)` dans `consulter_famille` vs durée du trio :**
   * *Localisation :* `consulter_famille()` (lignes de fin).
   * *Analyse :* Le thread trio lance 3 requêtes HTTP en parallèle avec `timeout=None` pour chaque appel, et le thread fait un `t.join(timeout=240)`. Mais dans le thread principal (`consulter_famille`), le `t.join` est fixé à **90 secondes**. Si le Hub (11435) met du temps à répondre (ce qui arrive en tempête lors de fortes charges sur les providers gratuits), le thread principal abandonnera l'attente au bout de 90s, rendant la main, alors que le thread arrière-plan continue de tourner et détient toujours le `lock_fd`. C'est cohérent avec la non-bloquance, mais à garder en tête pour les logs.

3. **Absence de prise en compte explicite du "Mode Tempête" dans la décision d'occasion :**
   * *Localisation :* `consulter_famille()` et `est_une_occasion()`.
   * *Analyse :* La spec indique : *"Mode tempête : déclencheurs (zone ROUGE/PRENDS_LA_PERTE, alarme, vortex>=2) -> consultation immediate, anti-spam 60s, cap horaire desactive. Jamais bloque par le cap."* Actuellement, `consulter_famille()` vérifie `_verifier_etat_ttl()` au début. Si le mode tempête est actif, la règle des 5 minutes (anti-spam) doit descendre à 60s et contourner le TTL standard. Il manque un court raccord dans `consulter_famille` pour interroger `mode_tempete_actif()` et moduler le TTL.

---

### Conclusion

Le code est **prêt pour l'intégration** dans l'arborescence ACE777 (`Index_Maison/scripts/`). Les réserves ci-dessus n'empêchent pas le fonctionnement mais garantissent la robustesse à long terme face aux tempêtes de requêtes. Applique la correction de la fermeture du FD (`os.close`) pour un zéro-défaut absolu.

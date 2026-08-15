# AVIS DEEPSEEK (task mission)

provider: Puter Grok (gratuit)

**Verdict : GO AVEC RESERVES**

Le code livré est globalement conforme à la SPEC v3 et corrige le bug principal de la v2 (verrou relâché trop tôt). Le trio réel est présent (aucun placeholder `pass` dans `_appel_hub`, `est_une_occasion` ou `build_sujet`), le verrou flock est bien détenu par le thread jusqu’à la fin des appels, et l’anti-spam est positionné au début. Le code est intégrable tel quel sur Python 3.9 stdlib.

### Réserves concrètes (à corriger avant intégration finale)

**1. Verrou flock – fuite de descripteur (famille_session.py, lignes 168-170 et 212-215)**
- Le `lock_fd` est passé au thread mais **jamais fermé** (`os.close(lock_fd)` manquant) ni dans `_thread_trio` ni dans `consulter_famille`.
- Risque : descripteurs qui s’accumulent sur les Mac 8 Go si plusieurs consultations se déclenchent. Ajouter `os.close(lock_fd)` dans le `finally` de `_thread_trio` après le `LOCK_UN`.

**2. Mode tempête incomplet (famille_session.py)**
- `mode_tempete_actif()` existe mais n’est **jamais appelé** dans `consulter_famille()`.
- Pas de bypass de l’anti-spam 5 min ni passage à 60 s quand `mode_tempete_actif()` ou alarme/vortex détecté.
- `est_une_occasion` gère l’alarme mais pas le cas « tempête active → consultation immédiate + cap horaire désactivé ».
- Réserve bloquante pour le principe « machine de tempête ».

**3. Anti-spam en cas d’échec du trio – correct mais fragile**
- Le TTL est bien créé **avant** le lancement du thread (ligne ~165), donc même si le trio plante, l’anti-spam tient.
- Cependant, si une exception survient entre l’acquisition du lock et `_creer_etat_ttl()`, le verrou est relâché sans TTL → risque de double appel. Il faut créer le TTL **immédiatement après** le `flock` réussi, avant tout autre chose.

**4. Budget et providers gratuits**
- Absents de ce fichier (conforme au périmètre famille_session.py).
- Vérifier que `budget_hub.py` implémente bien le recalcul quotidien dynamique + 20 % réserve storm + gratuits jamais coupés. Ce n’est pas dans le livrable soumis.

**5. Petits points de robustesse**
- `mode_tempete_actif()` lit `etat_tempete.json` sans vérifier que le fichier existe (peut lever une exception silencieuse mais correcte via le try/except).
- Le `join(timeout=90)` dans `consulter_famille` peut laisser le thread tourner seul après timeout ; c’est acceptable mais documenter que le verrou reste détenu par le thread.

### Synthèse
Le verrou anti-doublon et l’anti-spam au début sont corrects (le bug original de la v2 est résolu). Le trio est réel et le code est propre. Les réserves portent principalement sur l’intégration incomplète du mode tempête et la fuite du descripteur de verrou.

**GO** une fois les points 1, 2 et 3 corrigés. Le reste est acceptable pour intégration.

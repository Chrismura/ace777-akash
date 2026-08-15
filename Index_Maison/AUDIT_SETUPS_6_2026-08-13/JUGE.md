# AVIS JUGE (task signets.juge)

provider: Google Gemini

En tant que **JUGE, vérificateur indépendant ACE777**, j'ai procédé à l'audit strict, selon la loi du brut, des éléments soumis.

---

### RAPPORT D'AUDIT ACE777

1. **Correction de la cause racine du 13/08 (Boucle famille / 900 appels/h)** :
   * *Constat :* Dans `famille_session.py`, le verrou `flock` (`LOCK_EX | LOCK_NB`) est désormais acquis **au début** de `consulter_famille()` et est tenu par le thread du trio (`_thread_trio`) **pendant toute la durée des appels API** (jusqu'au `finally:`). 
   * *Vérification du scénario (appel 10s plus tard pendant que le trio tourne) :* Si un nouvel appel arrive 10 secondes plus tard alors que le trio tourne encore, `fcntl.flock` lève une exception `BlockingIOError`, ferme immédiatement le descripteur et **quitte instantanément** sans lancer de nouveau thread ni solliciter le hub. Le TTL n'est écrit qu'au moment d'une occasion réelle dans le thread, évitant l'écriture en fin de thread (anti-spam thread détaché corrigé).
   * **Statut : VALIDÉ.**

2. **Principe tempête respecté** :
   * *Constat :* Le mode tempête (`mode_tempete_actif`) s'active correctement sur des déclencheurs réels et robustes : zone ADA (`ROUGE` / `PRENDS_LA_PERTE`), vortex de saison `>= 2`, alarme fraîche de moins d'1h, ou fichier d'état explicite. En tempête, l'anti-spam passe à 60s et l'appel bypass le cap horaire classique (`_verifier_etat_ttl()` est ignoré). La réserve storm (20%) et les options gratuites sont préservées sans brider la machine.
   * **Statut : VALIDÉ.**

3. **Budget dynamique & Gratuits dynamiques** :
   * *Constat :* Dans `budget_hub.py`, le budget n'est **jamais une valeur fixe**. Il est calculé dynamiquement à partir des capacités des providers actifs, pondéré par le facteur de sécurité (`FACTEUR_SECURITE = 0.15`), encadré entre `MIN_BUDGET` (40) et `MAX_BUDGET` (800). La réserve storm est calculée proprement à 20% (`cloud_daily_reserve: 156` pour un total de 780 dont 624 calme). 
   * *Gratuits dynamiques :* `gratuits_actifs()` lit directement le champ `"free": true` dans `providers.json`, sans aucune liste figée en dur dans le code.
   * **Statut : VALIDÉ.**

4. **Robustesse et intégrabilité (démons 24/7, préflight, fuites)** :
   * *Constat :* `famille_session.py` gère proprement la fermeture des descripteurs de fichiers (`os.close(lock_fd)`) dans les blocs `finally`. Les chemins sont absolus (`Path(__file__).resolve().parent`). Le script de préchauffage (`prechauffage_reserve.py`) valide les points C1 à C4 avec tests hermétiques, et l'architecture intègre un retour syntaxique valide.
   * **Statut : VALIDÉ.**

---

### VERDICT FINAL

# **GO**

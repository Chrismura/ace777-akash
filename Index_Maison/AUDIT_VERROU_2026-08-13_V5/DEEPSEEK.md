# AVIS DEEPSEEK (task mission)

provider: Puter Grok (gratuit)

**Verdict : GO AVEC RÉSERVES**

Le code v5 livré est globalement conforme à la fusion demandée (v3 trio réel + corrections v4 + conservation TTL). Il est intégrable tel quel dans `Index_Maison/scripts/famille_session.py`, Python 3.9 stdlib, non fatal, avec le vrai trio hub (_appel_hub + urllib, est_une_occasion, build_sujet) et sans placeholder ni `pass` dans les fonctions métier.

### Points validés
- Verrou flock posé au début de `consulter_famille` et **tenu pendant toute la durée** du trio dans `_thread_trio` (finally avec `LOCK_UN` + `os.close(lock_fd)`). Un appel 10 s plus tard est bien bloqué tant que le thread n’a pas terminé.
- Anti-spam au tout début (`_verifier_etat_ttl` avant toute chose), même en cas d’échec du trio.
- Mode tempête branché correctement (`mode_tempete_actif` + bypass TTL + `_duree_anti_spam` = 60 s).
- TTL créé **juste après** le flock réussi (`_creer_etat_ttl`) et **jamais supprimé** (remplacé par `_noter_fin_consultation` qui n’altère pas le timestamp initial).
- Trio réel présent et fonctionnel (3 appels hub via threads, écriture AVIS_FAMILLE_SESSION.md + historique).

### Réserves concrètes (à corriger avant mise en prod)
1. **Fichier `famille_session.py` – ligne ~280-285 (`mode_tempete_actif`)**  
   Le déclencheur `vortex>=2` n’est pas implémenté. Seuls ROUGE/PRENDS_LA_PERTE, alarme < 1 h et `etat_tempete.json` sont testés. Ajouter explicitement la vérification du vortex (ou confirmer qu’il alimente `etat_tempete.json`).

2. **Fichier `famille_session.py` – ligne ~140 (`_thread_trio`)**  
   Quand `est_une_occasion` retourne False, la fonction `return` tôt mais le TTL a déjà été créé dans `consulter_famille`. Cela crée un anti-spam inutile de 5 min (ou 60 s) pour rien. Déplacer la création du TTL **après** la vérification d’occasion dans le thread, ou ne créer le TTL que si occasion = True.

3. **Fichier `famille_session.py` – ligne ~320 (`consulter_famille`)**  
   Le `t.join(timeout=90)` est trop court par rapport aux `t.join(timeout=240)` internes du trio. En cas de latence hub, le thread principal lâche la main alors que le verrou est encore détenu (comportement acceptable mais à documenter ou aligner sur 240 s).

4. **Budget / providers gratuits**  
   Absents de ce fichier (normal, c’est dans `budget_hub.py`). Vérifier séparément que les providers gratuits (dont Puter-Grok) ne sont jamais coupés et que la réserve storm 20 % + recalcul quotidien sont bien implémentés.

**Conclusion** : le verrou famille + mode tempête est maintenant correct et corrige le bug du 13/08. Les 4 réserves ci-dessus sont mineures et faciles à traiter. GO une fois ces points ajustés.

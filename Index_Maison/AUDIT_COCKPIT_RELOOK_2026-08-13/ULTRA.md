# ULTRA — verdict famille

Provider: Google Gemini

**FAMILLE ACE777 — Rapport d'Audit Qualité (Hedge Fund Suisse)**  
*Date : 13/08*

---

### 1. VERDICT : **GO AVEC RÉSERVES**
Le cahier des charges de Christophe est rigoureusement respecté :
- **Heure locale unifiée** : Suppression totale d'UTC, horloge et rafraîchissement ancrés en `fr-FR` avec libellé discret « locale ».
- **UX Visuelle (Synapse & Cosmos)** : Petits somas ($r=4..6$), orbites aérées à 2 anneaux si $>8$ providers, et système de leader lines avec anti-chevauchement.
- **Layout** : Passage réussi des panneaux de droite en grille 2 colonnes, événements en pleine largeur.
- **LIVE** : Polling `hub.json` (10s, `no-store`) validé par l'incrément budgétaire (1602 $\to$ 1613). Fenêtres d'info préservées.

*Réserve mineure* : La garde de l'anti-chevauchement (`while guard < 10`) peut saturer sur des datasets aberrants, mais reste acceptable pour la volumétrie actuelle.

---

### 2. AMÉLIORATIONS LOGIQUE, PERF & STABILITÉ
Pour hisser ce cockpit au standard absolu de notre desk de trading :

1. **Robustesse du Polling (`hub.json`)** : 
   - Ajouter un bloc `try/catch` avec gestion explicite des erreurs réseau. Si le serveur sur 17800 décroche, le polling actuel risque de planter silencieusement ou de geler le rendu. Afficher un indicateur discret « LIVE (dégradé) » en cas d'échec consécutif.
2. **Anti-chevauchement des labels** :
   - L'algorithme actuel repose sur un décalage vertical simple. Pour une robustesse "Hedge Fund", implémenter une relaxation de force (type *force-directed label placement*) ou un tri préalable par ordonnée $Y$ pour éliminer définitivement les collisions croisées.
3. **Cohérence temporelle totale** :
   - Vérifier les tooltips et les timestamps internes des graphiques (ex: onglet Graph) pour traquer la moindre trace résiduelle d'UTC ou de `Date.now()` brut.
4. **Performance DOM** :
   - Le polling toutes les 10s déclenche `buildNodes()` et `renderCosmos()`. S'assurer que les écouteurs d'événements (clics sur les nœuds) ne sont pas réattachés en boucle à chaque tick, évitant ainsi toute fuite mémoire (*memory leak*).

---
*Signé : Validation ACE777, Genève.*

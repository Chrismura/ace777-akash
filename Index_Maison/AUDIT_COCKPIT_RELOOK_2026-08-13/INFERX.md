# INFERX — verdict famille

Provider: Google Gemini

### 1. Verdict : GO AVEC RÉSERVES

Le cahier des charges de Christophe (13/08) est respecté avec rigueur et les extraits de code témoignent d'une implémentation propre :
* **Heure locale unifiée** : Suppression du suffixe `Z` et bascule systématique sur `fr-FR` (`toLocaleTimeString`).
* **UI/UX Synapse & Cosmos** : Petits somas ($r=4..6$), orbites étagées si $>8$ providers, et système de *leader lines* avec anti-chevauchement itératif (gardien à 10 tours).
* **Agencement** : Passage en grille 2 colonnes (`grid-template-columns: repeat(2, 1fr)`) préservant l'ergonomie, avec événements en *full-width*.
* **LIVE** : Polling effectif à 10 s sans perte des fenêtres d'info interactives adorées par Christophe.

---

### 2. Améliorations Logique / Perf / Stabilité (Recommandations ACE777)

* **Anti-chevauchement des labels** : Le mécanisme actuel (`while guard < 10`) fonctionne mais reste local. Pour une robustesse "hedge fund", il est conseillé d'implémenter un tri initial des nœuds par angle (`Math.atan2`) avant le calcul des décalages verticaux, afin de garantir un espacement régulier sans effet d'amas.
* **Résilience du Polling (`fetch`)** : Un simple `fetch('/hub.json')` sans bloc `try/catch` ni gestion du statut HTTP (ex: `if (!res.ok) throw...`) risque de planter silencieusement ou de saturer la console si le serveur micro-service (`:17800`) décroche. Ajouter un compteur d'erreurs consécutives pour basculer le widget en mode "DEGRADED / STALE" après 3 échecs.
* **Consommation CPU / Rafraîchissement** : Le polling à 10 s est très léger et n'impacte pas le rendu 60 FPS des graphes. Toutefois, veiller à utiliser l'API `requestAnimationFrame` pour les animations de canvas et stopper le polling si l'onglet du navigateur est en arrière-plan (`document.hidden`).
* **Audit horaire exhaustif** : Vérifier que les timestamps bruts dans les tableaux (`queue`, `events`) proviennent bien d'une normalisation côté serveur ou sont convertis explicitement via `new Date()` local pour éviter tout décalage d'affichage dans les tooltips.

---

### 3. Conclusion

**GO** pour le déploiement en production, sous réserve d'encapsuler le `fetch` dans un bloc `try/catch` robuste pour parer aux micro-coupures réseau du port `:17800`.

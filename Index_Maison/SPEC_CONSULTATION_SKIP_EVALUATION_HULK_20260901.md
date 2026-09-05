# CONSULTATION STRICTE — SKIP / VITESSE D’ÉVALUATION HULK — 2026-09-01

## Question
Les SKIP ralentissent-ils l’évaluation Hulk, et quelle amélioration est sûre sans modifier la stratégie ? Produire un avis strict, contester les hypothèses, proposer des améliorations classées et coordonner un GO/NO-GO.

## Faits mesurés
- Run récent : `PAPER_V1_20260901_052301.csv`.
- SKIP comptés : 18 997.
- Motifs principaux : VOL 16 358 (~86 %), MUR-CASSE 741, SPREAD 643, SKIP_VEILLE_RED 330, CB 324, MUR-FAIBLE 241, MUR-SPOOF 178, SKIP_COOLDOWN 144, SENSE 38.
- `POLL_SEC=20`.
- `SCORE_EVERY=3` : refresh scores environ toutes les 60 secondes.
- La boucle parcourt les paires et appelle `fetch_all_prices` à chaque cycle ; les scores et sondes ont des cadences distinctes.
- Les SKIP sont journalisés dans le CSV et peuvent être répétés à chaque cycle.
- Les sorties et la gestion des positions doivent rester exécutées à chaque cycle.
- Aucun changement de seuil n’est autorisé dans ce chantier.
- Aucun mode live, Kelly ou Cortana automatique.

## Hypothèse à examiner
Le volume de lignes SKIP semble surtout être un bruit d’observabilité. Il peut aussi cacher un coût CPU/IO ou des évaluations réseau répétées. Il faut distinguer :
1. coût d’écriture/logging ;
2. coût des appels API ;
3. coût du calcul local ;
4. refus légitimes dus aux seuils ;
5. refus obsolètes dus à un cache de score trop long.

## Proposition à évaluer
- Instrumenter la durée par phase sans changer le comportement.
- Dédupliquer les SKIP identiques par paire et motif avec TTL court, tout en conservant des compteurs agrégés et un résumé périodique.
- Ne jamais dédupliquer les événements de sortie, erreurs, changements de régime, changements de données ou transitions de gate.
- Ne pas introduire une nouvelle boucle ni une nouvelle source de vérité.
- Ne pas modifier `VOL_SPIKE_MIN_SMALL`, `POLL_SEC`, `SCORE_EVERY` ou les autres seuils sans campagne dédiée.

## Questions obligatoires
1. Les SKIP ralentissent-ils réellement la boucle, ou seulement le fichier ? Quelles mesures faut-il ajouter ?
2. Quelle déduplication est sûre et où doit-elle vivre pour éviter les doublons ?
3. Faut-il instrumenter avant de dédupliquer ?
4. Le refresh des scores toutes les 60 secondes crée-t-il un risque de décision obsolète ?
5. Quelles paires/motifs doivent être analysés séparément avant toute modification ?
6. Donner une coordination : fichiers autorisés/interdits, tests hermétiques, rollback, critères d’arrêt.

## Contraintes d’architecture
- Remonter à la source avant chaque modification.
- Réutiliser les fonctions existantes ; ne pas créer une troisième couche de gate.
- Préserver `maybe_enter`, `buy`, `manage_open`, `manage_bag` et les circuits de risque.
- Préserver la traçabilité : un compteur ne doit pas remplacer la preuve d’un changement d’état.
- Le cockpit doit continuer à distinguer les motifs de refus, même si les lignes brutes sont échantillonnées.

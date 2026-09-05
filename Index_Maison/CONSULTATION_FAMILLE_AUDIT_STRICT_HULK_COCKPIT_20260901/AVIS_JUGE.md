# AVIS JUGE (task juge.tranche · Google Gemini · 2026-09-01T07:32Z)

VERDICT : GO-AVEC-RÉSERVES
CONFIANCE : 88 %
HYPOTHÈSES : 
1. Le satellite d'aspiration écrit de manière atomique sur un volume disque partagé, garantissant l'accès du moteur sans latence réseau.
2. Le cockpit se contente d'une lecture passive des états persistés (JSON/CSV) sans interférer avec la boucle d'exécution du moteur.

CE QUI CHANGERAIT L'AVIS : Une divergence avérée entre les soldes affichés par le cockpit et l'état réel persisté par le moteur lors d'un test de redémarrage (crash recovery).

AMÉLIORATION PROPOSÉE : 
1. **Contrat de fraîcheur et schéma unique (`ace_schema.py`)** : Centraliser le typage des positions (`trade`, `bag`, `seed`) et le seuil de fraîcheur (>45s) dans un module partagé pour que le moteur et le cockpit s'alignent sur une source de vérité unique, évitant les recalculs UI.
2. **Politique Fail-Safe explicite** : Remplacer le fallback inline par un mode strict `DEGRADED_NO_NEW_ENTRIES` dans le moteur en cas de rupture satellite, autorisant uniquement la gestion des positions existantes sans surcharger l'API.
3. **Plafond de perte DCA (R6)** : Fixer un stop technique absolu et inaliénable (ex: -50%) pour les états `bag` afin d'empêcher tout enlisement infini du capital.

SYNTHÈSE (5 lignes max)
L'audit confirme la robustesse générale du moteur Hulk Paper et de son cockpit, sous réserve de verrouiller la gestion du fallback et d'harmoniser la sémantique des "bags". Le LIVE demeure strictement interdit et le mode PAPER est validé avec des réserves sur la centralisation du contrat de fraîcheur. Toute modification doit respecter les frontières étanches entre supervision, moteur et affichage.

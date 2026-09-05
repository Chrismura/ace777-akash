# AVIS GEMINI (task gemini.analyse · Google Gemini · 2026-09-01T07:32Z)

VERDICT : GO-AVEC-RÉSERVES
CONFIANCE : 82 %
HYPOTHÈSES : 
1. Le satellite d'aspiration et le moteur partagent le même volume monté (`runs/`) sur l'hôte, garantissant l'intégrité des écritures atomiques sans latence réseau inter-conteneurs.
2. Le cockpit lit les états de manière purement passive (lecture seule de `mission.json` ou équivalent), sans jamais injecter de commande de contrôle direct dans le moteur.

CE QUI CHANGERAIT L'AVIS : Une divergence constatée entre les soldes affichés dans le cockpit et les états persistés en JSON/CSV lors d'un test de redémarrage (crash recovery), prouvant une corruption de la sémantique `pos`/`bags`.

AMÉLIORATION PROPOSÉE : 
1. **Module de contrat de schéma partagé (`ace_schema.py`)** : Centraliser les types et structures de données (positions, bags, cash) pour que le moteur les sérialise et que le cockpit les consomme sans recalculer de logique financière en JS.
2. **Politique Fail-Safe explicite** : Remplacer le fallback inline muet par un état d'exception `DEGRADED_NO_NEW_ENTRIES` dans le moteur, bloquant les nouvelles entrées si le JSON d'aspiration est stale >45s tout en autorisant la gestion des positions existantes.
3. **Double comptabilité PnL Paper** : Ajouter un calcul de frais théoriques et de slippage simulé directement dans le journal de sortie du moteur pour que le cockpit affiche un PnL net comparable au benchmark HOLD.

SYNTHÈSE (5 lignes max) :
Le moteur Hulk Paper et son cockpit fonctionnent globalement de manière cohérente mais souffrent d'ambiguïtés sur le fallback d'aspiration et la sémantique des "bags". Le LIVE demeure strictement interdit et le mode PAPER est validé sous réserve d'isoler la logique de dégradé. Aucune nouvelle boucle ni modification simultanée satellite/moteur ne doit être initiée sans ce contrat de schéma. Le système de persistance est sain mais exige un test d'atomicité de reprise strict.

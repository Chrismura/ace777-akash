# Consultation famille — source cockpit persistante

## Question stricte
Le cockpit visible continue d'afficher l'ancienne présentation malgré les corrections. Identifier la cause racine et recommander une seule correction minimale, sans modifier Hulk ni ses états.

## Faits vérifiés
- Le fichier Bureau exécuté est `~/Desktop/Cockpit.command`.
- Son feed est `/Users/christophe/ace777-test-day1/Index_Maison/scripts/cockpit_mission_feed.py`.
- Le feed exécuté affiche désormais : `HULK trades=6 seeds=9 house_bags=0 cash=5 pnl=-6.2422`.
- `Index_Maison/cockpit/mission.json` contient `PAPER_V1_20260901_080116_state.json`, `categoryCounts` et `pnlNetEstimated=-6.6167`.
- `Index_Maison/cockpit/mission.js` servi par `127.0.0.1:17800` est identique au fichier disque et contient `PAPER_V1`, `categoryCounts` et `pnlNetEstimated`.
- La page HTML contient les nouveaux identifiants `h-net-est`, `h-bags-note` et le rendu `renderHulk()`.
- Le terminal Brave affiche `Opening in existing browser session.`
- La capture utilisateur montre encore l'ancienne ligne visuelle `SCORE HULK vs HOLD` et la présentation `bags=15`.
- Il existe deux lanceurs Bureau : `Cockpit.command` et `ACE777 Cockpit.app`.
- Le serveur HTTP persistant écoute sur `127.0.0.1:17800`.

## Contraintes
1. Ne pas redémarrer Hulk.
2. Ne pas modifier positions, stratégie, seuils, états ni LaunchAgents trading.
3. Ne pas ajouter une nouvelle couche sans preuve.
4. Distinguer données servies, code de rendu, fenêtre visible et éventuelle autre application.
5. Avis strict : si les faits sont insuffisants, le dire.

## Réponse attendue
A. Cause racine la plus probable et preuves manquantes.
B. Tests non destructifs à faire.
C. Une correction minimale recommandée.
D. Corrections à ne surtout pas faire.



**VERDICT FINAL : GO-AVEC-RÉSERVE**

1. **Goulot n°1 global : EXÉCUTION / sizing.**  
La ruine Monte Carlo à 32,5 % est le risque le plus bloquant aujourd’hui, car elle menace directement le PnL positif de +29,11 $. Je tranche EXÉCUTION avant MÉMOIRE, HUB ou veille.

2. **Secteur retenu et pépite : EXÉCUTION, sizing fixe.**  
Le goulot est l’absence de sizing dynamique prudent. La pépite à installer est **Kelly (43+105)**, mais en mode bridé/dry-run pour ne pas fausser le run `MASTER_VORTEX_V2_COLLAB_4H`.

3. **Une pépite par goulot : OUI, discipline séquentielle.**  
NON à deux pépites simultanées, sauf si la seconde est strictement indispensable à la sécurité ou à la réversibilité de la première. Ici, Kelly seule suffit à traiter le goulot n°1.

4. **Risque d’installation pendant le run : GO-AVEC-RÉSERVE.**  
On peut préparer/poser Kelly maintenant si tout reste en lecture seule ou dry-run. Aucune activation live sur les fills sans validation après runtests, sauf si l’installation est strictement réversible et sans impact hot.

**Conditions non négociables :** sauvegarde immédiate, installation en dry-run/lecture seule, rollback en une commande. Ne pas toucher hub, pont cockpit, radar, ni aux paramètres live ALPHA/BETA hors sizing. Activation seulement si la simulation montre une baisse de la ruine sans dégrader la PnL.
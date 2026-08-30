# AVIS ULTRA (provider Google Gemini)

Ici ULTRA (famille ACE777). On regarde la prod, la tempête, le long terme. Pas de théorie, du chiffré.

### 1. VERDICT
**GO AVEC RÉSERVES SÉVÈRES.**
*Raison :* Le pattern horaire (creux 15h / pic 01h) est statistiquement marqué sur 3 jours, mais exploiter un actif à $44M de market cap avec des variations 15 min de 22% (dd15) sans kill-switch de liquidité va décimer le portefeuille Hulk en cas de décrochage macro.

---

### 2. LES ANGLES MORTS (Ce qui va casser en prod)
* **L'illusion du mur à 45 240 $ :** Sur un token à faible capitalisation, un mur de cette taille s'évapore en une seule seconde si le carnet global se vide. Ce n'est pas un coussin de sécurité, c'est un mirage en cas de stress de marché.
* **Le biais des 3 jours (Overfitting) :** Valider un cycle intraday sur 72 heures, c'est trader le hasard d'une semaine calme. Si le Bitcoin tousse entre 15h et 16h UTC, le « creux d'accumulation » se transforme en chute libre sans plancher.
* **Le coût du slippage nocturne :** Viser 01h-05h UTC expose aux heures de liquidité mince sur les DEX/CEX secondaires où RED est tradé. Le spread va dévorer la marge de 2,4%.

---

### 3. AMÉLIORATION PROPOSÉE (Ce que je rajoute au set-up)
*Je ne corrige pas, je pose une brique d'infrastructure indispensable :*

**Mise en place d'un « Circuit Breaker de Volatilité » basé sur le order book depth, combiné à un DCA asymétrique en 3 paliers.**

* **En pratique :** Interdiction d'exécuter l'entrée de 15h-16h si le volume de transactions des 15 minutes précédentes dépasse 3 fois la moyenne mobile 24h (signal de panique, pas de creux sain). 
* **Côté exécution :** Au lieu d'un bloc unique dans la zone creux, on fragmente l'entrée en 3 tranches (à -1%, -2% et -3% sous le prix médian de 15h) pour absorber les mèches violentes du *dd15 moyen (22,86%)*, couplé à un stop-loss dur fixé dynamiquement à 1,5× le range de la bougie 15 min précédente.

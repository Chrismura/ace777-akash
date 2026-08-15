# AVIS gemini (provider Google Gemini, 4.2s)

1. **Le design du pont est-il le bon (injecter dans live.json) ? Risques de confusion avec whaleN/whaleUsd ?**
   Oui, injecter dans `live.json` est le choix le plus pragmatique pour éviter de multiplier les sources à parser pour Cortana et Ada. Cependant, le risque de confusion est élevé avec les clés existantes `whaleN`/`whaleUsd` (qui mesurent les gros trades dérivés). Il faut impérativement préfixer clairement les nouvelles clés (ex: `onchain_` au lieu de juste `whale_`) pour cloisonner les données onchain (mempool brut) des données de carnet/dérivés.

2. **Les clés proposées sont-elles les bonnes ? Manque-t-il quelque chose ?**
   Les clés proposées (`whaleBlocsN`, `whaleFragN`, etc.) sont correctes mais incomplètes. Il manque une clé temporelle cruciale pour le contexte tactique : `onchain_dernier_evt_min` (l'âge en minutes de la dernière alerte baleine) pour permettre à Cortana de pondérer la fraîcheur de l'information.

3. **ADA : comment intégrer l'onchain SANS casser sa philosophie (voilure continue, pondération) ?**
   L'onchain ne doit pas modifier directement le sens de la pression (bleed/storm), mais agir comme un *facteur de friction* (un multiplicateur compris entre 0.8 et 1.2) appliqué au calcul de la voilure. Une sortie massive d'exchange (outflow) réduit la voilure (prudence face à un risque de vente spot), une entrée (inflow) l'augmente légèrement. Pondération maximale recommandée : 10% du score global d'Ada pour éviter de sur-répondre au bruit onchain.

4. **CORTANA : à 44% de justesse, l'ajout d'un indice onchain améliore-t-il ou brouille-t-il son signal ?**
   À 44% de justesse, Cortana souffre déjà d'infobésité (bruit de fond funding/fearGreed). Ajouter des données onchain brutes va *brouiller* davantage son signal LLM, sauf si le pont fournit une synthèse textuelle pré-mâchée (ex: `"Tendance onchain: 2 gros blocs sortants vers Binance, pression vendeuse modérée"`) plutôt que des chiffres bruts qu'elle interprète mal.

---

* **VERDICT :** GO-AVEC-RÉSERVE
* **CONFIANCE :** 75%
* **HYPOTHÈSES :** 
  1. Le format `live.json` accepte l'ajout de clés sans saturer la fenêtre de contexte de Cortana.
  2. Le mapping des adresses dans `whales.json` est suffisamment stable pour qualifier la direction (inflow/outflow).
  3. Ada peut intégrer un multiplicateur exogène sans réécrire sa boucle de calcul historique.
* **CE QUI CHANGERAIT L'AVIS :** Une baisse de la justesse de Cortana en dessous de 40% après intégration, ou une instabilité du daemon `mempool.space` saturant les I/O du disque.
* **AMÉLIORATION PROPOSÉE :** 
  1. Renommer toutes les nouvelles clés avec le préfixe explicite `onchain_` pour éviter toute collision avec `whaleUsd`.
  2. Fournir à Cortana une phrase de synthèse pré-calculée par le pont plutôt que des métriques brutes.

**SYNTHÈSE :** 
Design validé via `live.json` à condition de préfixer strictement les clés onchain (`onchain_`). Ada intègre ces flux via un multiplicateur de voilure continu et borné (poids max 10%). Cortana reçoit une synthèse textuelle pré-analysée pour ne pas dégrader sa justesse (44%). Pérennisation impérative via launchd.

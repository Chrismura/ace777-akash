Confrontation avec la TERRAIN — j'ai testé l'API en direct avant d'appliquer ton design, et il y a un problème sur le point (c) volume :

**Ce que j'ai mesuré en direct (aujourd'hui, bloc réel 963837, 5719 tx) :**
- `GET /api/block/{hash}` (mempool.space ET blockstream.info) → renvoie le HEADER du bloc (height, size, tx_count…) mais **PAS la liste des transactions**. Aucun champ `txs`.
- `GET /api/block/{hash}/txids` → renvoie la liste complète des txids (1 appel, ~1 Mo).
- `GET /api/block/{hash}/txs/{index}` → renvoie 25 transactions légères par page (avec txid, mais je dois vérifier si la valeur y est). Pour 5719 tx = **229 appels** pour tout le bloc.
- `GET /api/tx/{txid}` → renvoie la transaction complète avec ses outputs (la valeur en satoshis), 1 appel par tx.
- Historique ACE : le 22/08, ~50 appels / 2 min a fait BANNIR notre IP (rate-limit) → 8 h de silence.

Donc « le résumé du bloc porte la valeur de chaque tx » est FAUX sur l'API gratuite réelle. Ta correction (c) n'est pas implémentable telle quelle.

Question — avec cette réalité, quelle est la MEILLEURE stratégie de volume ? Évalue ces options et donne-moi TA recommandation chiffrée :
1. Garder l'échantillonnage actuel : creuser `/api/tx/{id}` pour les tx fantômes SEULEMENT si taux ≥ 10 %, plafonné à 50 tx (0,2 s entre chaque).
2. Monter le plafond (à combien ?) avec un backoff anti-429.
3. Utiliser la pagination `/txs/{index}` pour les fantômes uniquement (pages qui contiennent les txids fantômes, repérables par leur index dans la liste txids) — combien de pages max ?
4. Estimée par la taille du bloc / poids moyen (aucun appel supplémentaire) — mais imprécise.
5. Autre chose que tu juges meilleure.

Donne la stratégie optimale : méthode + valeurs (plafond, cadence, seuil de déclenchement) + le compromis précision/API. Maximum 400 mots.
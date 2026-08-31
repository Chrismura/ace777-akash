# AVIS nvidia (provider Google Gemini)

Analyse critique et sans complaisance du plan « Moteur Léger et Costaud » de Buffy (31/08/2026).

---

### A) PRIORITÉ 1 (Batch prix) : Bonne idée, mais risque de désynchronisation critique

**Est-ce la bonne première étape ?**
**Oui, absolument.** C’est le « *low-hanging fruit* » absolu. Passer de 21 appels séquentiels (ou mal parallélisés) à 1 seul appel `/api/v3/ticker/price` réduit immédiatement la charge réseau de ~90% et libère la bande passante pour absorber les retries.

**Les RISQUES réels et ce qui pourrait casser :**
1. **Désynchronisation temporelle inter-paires (Le risque majeur) :** 
   * *Actuel :* Le bot fait 21 appels successifs. La paire n°21 a un prix vieux de 1 à 2 secondes par rapport à la paire n°1. 
   * *Avec le batch :* Les 21 prix proviennent *exactement* du même cliché instantané (snapshot) pris à $T_0$. C'est en réalité **mieux** pour la cohérence globale du portefeuille, mais attention au cache de 15-20 s.
2. **Le piège du cache de 15-20 s pour un bot à boucle de 20 s :**
   * Si la boucle tourne toutes les 20 secondes et que le cache dure 20 secondes, vous risquez de lire *exactement deux fois de suite la même réponse* si le timing dérive légèrement, ou pire, d'avoir des prix périmés de 39 secondes dans un cycle lent.
   * *Règle d'or :* Le TTL (Time To Live) du cache doit être strictement inférieur à la période de la boucle (ex: cache de 8 à 10 s max pour une boucle de 20 s), ou mieux : **le cache doit être invalidé et rafraîchi par le début de chaque nouveau cycle**, et non basé sur un timer arbitraire.
3. **Paires manquantes ou renommées :**
   * L'endpoint global `/ticker/price` renvoie un tableau de dictionnaires `[{'symbol': 'BTCUSDT', 'price': '...'}, ...]`. Si le format de la réponse MEXC diffère légèrement de l'appel unitaire (ce qui arrive parfois sur les exchanges tier-1/tier-2), le bot va lever un `KeyError` généralisé et crasher au premier cycle.
   * *Comment le faire sans casser :* Faire un *fallback* (si la paire n'est pas trouvée dans le dictionnaire du batch, loguer une erreur et faire un appel unitaire de secours pour cette paire uniquement, au lieu de tout faire planter).

---

### B) AUTRES CAUSES DE LOURDEUR / FRAGILITÉ (Angles morts de Buffy)

1. **L'I/O Bloquante sur le disque (Le vrai tueur de performance caché) :**
   * Le moteur écrit *à chaque cycle* dans `croisement_contexte.jsonl` (1 point/paire/minute, ou pire, à chaque boucle de 20s). Si les outils satellites lisent ce même fichier en même temps sans verrouillage propre (locks `fcntl` ou répertoires atomiques), ou si l'écriture synchrone bloque la boucle principale, le bot subit des micro-gels (« *lag spikes* »).
2. **Gestion synchrone des requêtes HTTP :**
   * Si le code utilise `requests` (synchrone bloquant) au lieu de `httpx` ou `aiohttp` (asynchrone), la moindre micro-coupure réseau bloque *toute* la boucle pendant les secondes de timeout, décalant le timing global.
3. **Fuite mémoire lente (Memory Leak) sur les structures de données Python :**
   * Les historiques de klines (360 bougies), les scores et les dataframes/listes accumulés en mémoire sans purge agressive (fenêtre glissante stricte) finissent par faire saturer le Garbage Collector, provoquant des pauses imprévisibles de la machine virtuelle Python.

---

### C) COSTAUD STRUCTUREL : L'architecture Cœur / Satellites est-elle la bonne ?

**Oui, c'est la seule architecture viable à terme.** 
Le trading algorithmique repose sur une règle absolue : **Le Cœur (Execution/Decision) doit être aveuglément rapide et aveugle au bruit extérieur.** 

* **Pourquoi c'est la bonne voie :** 
  Séparer la *collecte de données* (les sondes, les carnets, les murs, les flux WebSocket) de la *prise de décision* (le moteur Hulk) élimine les risques de blocage en cascade. Si un satellite plante (rate-limit sur l'API des murs, timeout sur l'aspiration), Hulk continue de tourner sur sa dernière valeur connue lue dans un fichier JSON local ou un socket UNIX/Redis.
* **Le meilleur découpage (Recommandation) :**
  1. **Satellites (Producteurs d'état) :** Des scripts indépendants (ou des threads robustes) tournent en arrière-plan et écrivent des fichiers JSON **atomiques** (écriture dans un fichier `.tmp` puis renommage `os.replace()`, ce qui garantit qu'on ne lit jamais un fichier partiellement écrit).
  2. **Cœur (Hulk - Consommateur pur) :** N'effectue **aucun appel réseau externe lourd**, il lit uniquement les fichiers locaux en mémoire (opération < 1 ms) et passe ses ordres d'achat/vente.

---

### D) AMÉLIORATION CONCRÈTE & AVIS STRICT SUR LE PLAN

#### 1. Ce qui est bon dans le plan de Buffy :
* Le constat chiffré est rigoureux (diagnostic précis des 200-270 req/min).
* L'étape 1 (Batch) et l'étape 5 (Circuit-breaker 429) sont indispensables et urgentes.

#### 2. Ce qui est risqué ou mal priorisé :
* **L'étape 2 (Timeout agressif 10s x 2) est dangereuse si mal implémentée :** Si MEXC subit une micro-latence, baisser le timeout à 10s sans un mécanisme de repli propre va multiplier les faux positifs et annuler des ordres ou sauter des cycles de manière erratique. Il vaut mieux un timeout de 15s avec *un seul retry immédiat*, puis abandon du cycle en cours si l'exchange ne répond pas.

#### 3. L'amélioration concrète et prouvée de mon cru : **Le Pattern d'Écriture Atomique et la Transition vers les WebSockets**
Puisque le moteur tourne en continu sur un MacBook, l'appel HTTP REST pour le prix est un anachronisme en 2026. 

* **La solution définitive (Remplace l'étape 1 à terme) :** 
  Lancer un unique script satellite léger qui se connecte au **Flux WebSocket public de MEXC** (`wss://wbs.mexc.com/ws`) pour écouter le flux global des prix (`miniTicker`). 
  * *Résultat :* **Zéro appel HTTP REST pour les prix.** Les prix sont rafraîchis en temps réel (millisecondes) dans un dictionnaire en mémoire partagé ou un fichier JSON local mis à jour en continu. Hulk n'a plus qu'à lire ce dictionnaire local à chaque cycle de 20 s. 
  * *Gain :* Suppression de 95% des problèmes de rate-limit, fin des timeouts sur les prix, et fraîcheur maximale des données.

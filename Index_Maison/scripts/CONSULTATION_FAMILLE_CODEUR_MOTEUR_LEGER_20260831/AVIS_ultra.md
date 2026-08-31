# AVIS ultra (provider Google Gemini)

### A) PRIORITÉ 1 (Batch prix) : Analyse critique

#### Est-ce la bonne première étape ?
**Oui, absolument.** C’est chirurgical, à haut ratio effort/bénéfice. En passant de 21 appels unitaires à 1 seul appel global (`/api/v3/ticker/price`), on élimine instantanément 70 % à 90 % de la charge réseau et on s'éloigne de la zone rouge des rate-limits (200 req/min). 

#### Risques et points de rupture potentiels :
1. **Désynchronisation temporelle (Race conditions / Fraîcheur) :** 
   * *Risque :* Un cache de 15-20 secondes signifie que les paires en fin de tableau ou lues 19 secondes après l'appel API manipulent des prix périmés par rapport au début du cycle. Pour du trading à cycle de 20 s, c'est critique si la volatilité est forte.
   * *Solution :* Ne pas stocker un cache temporel aveugle, mais faire **un unique appel par cycle** au tout début de la boucle (`fetch_all_prices()`), stocker le dictionnaire en mémoire locale pour la durée exacte du cycle (qui dure quelques millisecondes), puis vider. Pas besoin de persister 15-20 s : l'appel se fait au début du tick de 20 s.
2. **Paires non renvoyées ou format de réponse :**
   * *Risque :* Le endpoint global de MEXC renvoie un tableau d'objets (`[{symbol: "BTCUSDT", price: "..."}]`). Si une paire suivie est delistée, renommée, ou absente du payload, le bot risque de lever un `KeyError` et de crasher.
   * *Solution :* Transformer la réponse brute en un dictionnaire indexé (`{pair: price}`) au démarrage du cycle et ajouter un garde-fou : si la paire n'est pas dans le dictionnaire du batch, ignorer proprement le tick pour cette paire au lieu de planter la boucle.

---

### B) AUTRES CAUSES DE LOURDEUR / FRAGILITÉ (Angle Architecture)

Au-delà des rate-limits bruts, le profil de Hulk souffre de tares architecturales classiques des bots "monolithiques scriptés" :

1. **L'I/O synchrone bloquante (The Bottleneck Trap) :**
   Si le moteur fait ses 60 à 90 appels de manière **synchrone** (boucle `for` séquentielle), un seul appel lent (timeout à 10 s ou 40 s) bloque *toute* la machine. Même avec un meilleur timeout, la séquentialité tue la réactivité.
2. **L'écriture disque frénétique (`croisement_contexte.jsonl`) :**
   Écrire à chaque cycle (toutes les 20 s) dans un fichier texte (append) depuis le processus principal génère des micro-bloquages du système de fichiers (I/O wait), surtout sur les SSD des MacBooks soumis à Spotlight ou Time Machine.
3. **Absence de gestion d'état transactionnel :**
   Si le bot plante au milieu d'un cycle (ex: après avoir vendu mais avant d'avoir enregistré l'achat de rééquilibrage), le fichier d'état local et la réalité de l'exchange divergent.

---

### C) COSTAUD STRUCTUREL : Cœur vs Satellites (Étape 4)

**C'est LA meilleure décision du plan.** L'architecture "Cœur / Satellites" est la seule voie viable pour un bot robuste. 

* **Pourquoi c'est bon :** Le Cœur de trading ne doit faire *qu'une seule chose* : lire son état local en mémoire/JSON, appliquer sa logique mathématique/de risque, et envoyer des ordres d'exécution. Il ne doit **jamais** faire de requêtes d'analyse exploratoire (murs, carnets profonds, GEX, klines lourdes).
* **Le découpage idéal :**
  * **Le Cœur (Hulk) :** Boucle rapide (ex: 5 à 10 s), 100% synchrone ou asynchrone léger, lit des fichiers JSON locaux mis à jour en arrière-plan par les satellites.
  * **Les Démons Satellites (Workers indépendants) :** 
    * `sat_market_data.py` (Met à jour le prix global et le carnet des paires actives).
    * `sat_analytics.py` (Gère les klines 360 bougies toutes les 3 minutes).
    * `sat_sentiments.py` (Murs, aspiration).
  * **Le Mécanisme de partage :** Utiliser des fichiers JSON atomiques (écrire dans un fichier `.tmp` puis renommer (`os.replace()`) pour éviter les lectures de fichiers partiellement écrits). Encore mieux pour un MacBook : un mini-serveur Redis local en mémoire, ou simplement des fichiers JSON sur `/tmp` (RAM disk sur macOS si configuré, ce qui évite l'usure et les latences du disque).

---

### D) AMÉLIORATION CONCRÈTE ET AVIS STRICT SUR L'ENSEMBLE

#### Avis strict sur le plan de Buffy :
* **Étape 1 (Batch) :** Excellent, indispensable.
* **Étape 2 (Timeout 10s x2) :** Très bon. 40 secondes en crypto, c'est l'éternité ; le prix a changé 3 fois.
* **Étape 3 (Espacer les coûteux) :** Logique. Les klines à 360 bougies n'ont indeed pas besoin d'être rafraîchies à la seconde.
* **Étape 4 (Cœur/Satellites) :** Vision d'architecte correcte, c'est la structure cible.
* **Étape 5 (Circuit-breaker 429) :** **CRITIQUE.** C'est la brique de survie. Sans ça, le moindre pic de trafic de MEXC couche le bot.

#### L'amélioration concrète de mon cru : **Le Pattern "Atomic RAM-Swap" (Double buffer JSON)**

Pour éliminer définitivement les risques de corruption de fichiers JSON et les conflits de lecture/écriture entre le Cœur et ses Satellites sur macOS, implémentez un pattern d'écriture atomique via un dossier en RAM (`/tmp/hulk_ram/`) :

1. **Le satellite écrit** ses données dans `/tmp/hulk_ram/contexte.tmp`.
2. **Le satellite bascule** instantanément le fichier via un appel système atomique : `os.replace('/tmp/hulk_ram/contexte.tmp', '/tmp/hulk_ram/contexte.json')`.
3. **Le Cœur lit** uniquement `/tmp/hulk_ram/contexte.json`. 

*Pourquoi c'est supérieur ?* 
Sur un MacBook, `/tmp` est souvent mappé sur un tmpfs (RAM disk) par défaut ou géré de manière très fluide par le kernel. Cela réduit à **zéro** l'usure du SSD, supprime les latences d'I/O disque, et garantit que le Cœur ne lira **jamais** un JSON tronqué ou en cours d'écriture (l'opération `rename` étant atomique sous Unix).

#### Conclusion :
Le plan de Buffy est **très bon, pragmatique et lucide**. Il attaque la racine du mal (l'asphyxie par l'API). En combinant le batching des prix (Étape 1), le découpage par satellites (Étape 4) et des écritures atomiques en RAM, Hulk passera d'un prototype fragile sur le point de disjoncter à un moteur robuste capable de tourner des semaines sans intervention. **Validation accordée, à coder sans attendre.**

# AVIS juge (provider Google Gemini)

Analyse sans complaisance du plan « Moteur Léger et Costaud » (superviseur Buffy, 31/08/2026).

---

### A) PRIORITÉ 1 (Batch prix) : Bonne idée et risques

**Est-ce la bonne première étape ?**
**Oui, absolument.** C'est chirurgical et le ROI est immédiat. Passer de 21 appels à 1 seul appel pour récupérer les prix supprime instantanément la plus grosse source de saturation réseau.

**Les RISQUES réels et ce qui pourrait casser :**
1. **Désynchronisation interne (race condition sur le cycle) :** Si le batch prend un instantané à $T_0$, mais que le traitement de la 21e paire se termine à $T_0 + 5\text{ s}$, cette dernière paire prend des décisions sur un prix qui a 5 secondes de retard par rapport à la première. *Atténuation :* Le batch doit être assigné à une variable unique au début exacte du cycle (`prices = fetch_all_prices()`), figée pour tout le tour de boucle.
2. **Structure de données inattendue :** L'API `GET /api/v3/ticker/price` sans symbole renvoie généralement une *liste* d'objets JSON (`[{symbol: "BTCUSDT", price: "..."}, ...]`) au lieu d'un dictionnaire direct. Si le code actuel s'attend à un objet unique par appel, itérer sur une liste sans la transformer en index `dict` (ex: `{item['symbol']: item['price'] for item in data}`) va lever un `KeyError` généralisé et crasher le bot.
3. **Paires manquantes oudelistées :** Si MEXC retire une paire ou renvoie une erreur partielle, le dictionnaire global n'aura pas la clé. *Atténuation :* Prévoir un `try/except` strict avec fallback (ignorer la paire pour ce cycle ou garder l'ancienne valeur du cache, mais jamais crasher le cœur).
4. **Fraîcheur du cache (15-20 s) vs trading :** Vu que la boucle tourne déjà toutes les 20 secondes, un cache de 15-20 s ne change fondamentalement pas la fraîcheur globale par rapport à l'état actuel (où les appels s'empilaient séquentiellement sur plusieurs secondes), mais il garantit un prix *homogène* pour tout le marché au même instant $T$.

---

### B) AUTRES CAUSES DE LOURDEUR / FRAGILITÉ (Angles morts de Buffy)

1. **L'I/O bloquante synchrone (Disque) :** 
   Le texte mentionne l'écriture dans `croisement_contexte.jsonl` (1 point/paire/minute). Si cette écriture est synchrone et se fait au milieu de la boucle principale sans gestion des descripteurs de fichiers ou avec des verrouillages (`flock`), chaque écriture disque est un point de blocage potentiel ($I/O$ wait). Sur un MacBook (souvent sur SSD, mais avec Spotlight ou des processus de fond), cela peut étirer un cycle de 20s à 35s.
2. **L'effet « Boule de Neige » des retries (Le vrai poison) :**
   Un timeout de 40 s avec 4 tentatives signifie qu'en cas de micro-coupure réseau, un thread/processus peut bloquer pendant **160 secondes**. Si la boucle est à 20 s, les cycles se saturent, s'empilent en mémoire, s'entrechoquent et finissent par saturer l'API à la reprise.
3. **Absence de gestion de la dérive temporelle (Drift) :**
   Si la boucle est codée avec un simple `time.sleep(20)` à la fin, le temps d'exécution du cycle s'ajoute au délai (ex: 20s de sommeil + 5s de calcul = 25s par cycle). Sur 24h, le timing dérive complètement, ce qui fausse les indicateurs temporels.

---

### C) COSTAUD STRUCTUREL : L'architecture Cœur / Satellites

**Est-ce la bonne voie ? Oui, à 100 %.**
C'est la seule architecture viable pour un bot de trading sérieux qui doit scaler sans imploser. 

**Pourquoi c'est vital :**
Le cœur de trading doit faire une seule chose, et la faire ultra-vite : **Lire l'état $\rightarrow$ Décider $\rightarrow$ Exécuter**. 
Il ne doit *jamais* faire de calculs lourds (Klines sur 360 bougies), de scraping de carnets d'ordres profonds, ou d'appels tiers non critiques. 

**Le découpage idéal (recommandé) :**
* **Les Satellites (Producteurs d'État, asynchrones, tolérants à la panne) :**
  * `satellite_prices.py` (écrit le gros JSON des prix toutes les 5s).
  * `satellite_orderbook.py` (surveille les murs et l'aspiration, écrit dans `murs.json`).
  * `satellite_klines.py` (calcule les régimes et scores toutes les 2-3 min, écrit dans `scores.json`).
* **Le Cœur (Consommateur pur, synchrone, ultra-rapide) :**
  * Lit uniquement des fichiers locaux en mémoire (`/dev/shm` sur Linux, ou un dossier temporaire en RAM sur Mac si possible, ou simple cache RAM local).
  * Ne fait des appels réseau *que* pour passer des ordres (BUY/SELL).

---

### D) AMÉLIORATION CONCRÈTE & AVIS STRICT SUR L'ENSEMBLE

#### 1. Ce qui est TRÈS BON dans le plan :
* Passer au batch global (`/api/v3/ticker/price`) : **Génie simple, gain immédiat.**
* Sortir les sondes lourdes du cœur (Étape 4) : **C'est l'architecture standard des fonds quantitatifs (Event-driven / State-driven).**
* Le circuit-breaker 429 (Étape 5) : **Indispensable.** Face à une API centralisée comme MEXC, insister quand on se fait rejetter est suicidaire.

#### 2. Ce qui est RISQUÉ ou mal priorisé :
* **L'étape 2 (Timeout agressif à 10s) est dangereuse si elle est faite isolément.** Si le réseau flanche 12 secondes, couper brutalement sans un mécanisme de repli propre (ex: utiliser la dernière valeur connue en cache forcé) va provoquer des faux signaux de vente/achat par manque de données. Le timeout doit être court, *mais* s'il échoue, le bot doit utiliser le dernier prix valide du cache en affichant un warning, au lieu de sauter la paire.

#### 3. LA CONTRIBUTION CONCRÈTE DE NOTRE CRU : **L'utilisation d'un stockage en RAM (Tmpfs / RAMDisk)**
Puisque le MacBook tourne en continu et que le cœur lit des fichiers JSON écrits par les satellites, **interdire les écritures sur disque dur (SSD)** pour ces fichiers temporaires. 

* **La solution :** Forcer tous les fichiers de communication inter-processus (le contexte, les prix, les scores) dans un dossier monté en mémoire vive (RAMDisk sur macOS via `hdiutil`, ou `/tmp` qui est souvent géré en mémoire virtuelle par macOS).
* **Pourquoi ?** Cela réduit le temps d'écriture/lecture à $0\text{ ms}$ (fini les I/O wait), élimine l'usure prématurée du SSD du Mac à cause des écritures frénétiques (toutes les minutes), et garantit que le cœur lit toujours une donnée ultra-fraîche instantanément.

**Verdict final :** Le plan de Buffy est remarquablement lucide et pragmatique. Validez-le, en exécutant l'étape 1 immédiatement, mais complétez l'étape 4 par une isolation stricte des fichiers en RAM (RAMDisk) pour rendre le cœur littéralement "invulnérable" aux latences matérielles.

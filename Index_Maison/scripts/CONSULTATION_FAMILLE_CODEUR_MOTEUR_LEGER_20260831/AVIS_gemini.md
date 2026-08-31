# AVIS gemini (provider Google Gemini)

*Avis technique strict, factuel et sans complaisance pour le superviseur Buffy.*

---

### A) PRIORITÉ 1 (Batch prix) : Bonne étape et risques

**Est-ce la bonne première étape ?**  
Oui, c'est la **seule** mesure d'urgence viable. Réduire l'empreinte réseau de 95% sur la brique critique de prix est une évidence absolue. Rester à 200+ req/min sur une limite IP de 200 frôle l'aberration architecturale.

**Risques et ce qui pourrait casser :**
1. **Désynchronisation temporelle (Race condition intra-cycle) :**  
   *Le problème :* Faire 21 appels unitaires garantit (en théorie) des prix prélevés séquentiellement. Un batch unique donne une **photographie globale** à un instant $T$. Pour une stratégie de market making haute fréquence, c'est mortel. Pour un bot papier tournant sur une boucle de 20 secondes, c'est un non-problème, voire un avantage (vision cohérente de tout le marché au même $T$).
2. **Paires manquantes / Format de réponse :**  
   *Le risque :* L'endpoint `/api/v3/ticker/price` sans symbole renvoie un tableau d'objets `[{symbol: "BTCUSDT", price: "..."}]`. Si le format change ou si une paire suivie est delistée/suspendue, le parsing direct crashe la boucle.
   *La parade :* Transformer le résultat en dictionnaire `prices_cache = {item['symbol']: float(item['price']) for item in response}` avec une validation stricte : si une paire surveillée est absente du batch, on déclenche un fallback ou on ignore proprement la paire pour ce cycle, sans tuer le bot.
3. **Le cache de 15-20 secondes :**  
   Trop long pour du trading. Si la boucle tourne toutes les 20 secondes, un cache de 15-20 s signifie que vous lisez parfois des prix vieux d'un cycle complet. 
   *Correction :* Pas de cache temporel arbitraire. Le batch **est** l'appel unique fait au *début* de chaque cycle de 20 s. Un cycle = un appel batch global. Le cache inter-cycle est inutile si l'appel se fait une fois par tour de boucle.

---

### B) AUTRES CAUSES DE LOURDEUR / FRAGILITÉ (Angle Architecture)

Buffy a ciblé les symptômes volumétriques, mais oublie des tares structurelles majeures :

1. **L'IO synchrone bloquant (Le poison silencieux) :**  
   Si le code utilise `requests` (synchrone) au lieu de `httpx` (asynchrone) ou `aiohttp`, le moindre ralentissement réseau de MEXC gèle l'intégralité du thread principal. À 20 secondes la boucle, un appel réseau qui traîne à 15 s décale tout le timing.
2. **L'écriture disque frénétique :**  
   Écrire dans `croisement_contexte.jsonl` à chaque cycle (toutes les 20 s) depuis le cœur, combiné aux satellites qui lisent/écrivent, crée des risques de *race conditions* sur les fichiers (fichiers partiellement écrits lus à la volée, erreurs I/O sous macOS).
3. **L'absence de gestion fine des exceptions d'API :**  
   Les bots de trading plantent souvent non pas à cause des 429 (Rate Limit), mais à cause des erreurs 5xx de l'échangeur ou des timeouts de socket mal interceptés qui laissent le bot dans un état "zombie" (positions ouvertes non suivies).

---

### C) COSTAUD STRUCTUREL : Cœur / Satellites (Étape 4)

**Est-ce la bonne voie ?**  
**Oui, à 100%.** C'est le pattern standard de l'industrie (séparation Producer/Consumer ou Séparation of Concerns). 

* **Le Cœur** ne doit faire qu'une seule chose : **Gérer l'état du portefeuille, appliquer la logique de décision, et passer les ordres.** Il doit être aveugle au carnet d'ordres profond, aux murs et aux analyses macro.
* **Les Satellites** (des scripts démons indépendants) calculent les indicateurs lourds (GEX, aspiration, carnets) en tâche de fond et cracheent des fichiers JSON atomiques (écriture via fichier temporaire + `os.replace` pour éviter les lectures de fichiers tronqués).

*Un meilleur découpage ?*  
Utiliser un **broker interne léger (type Redis en mémoire locale sur le Mac, ou de simples sockets Unix / fichiers JSON atomiques avec verrou)** plutôt que multiplier les écritures de fichiers bruts qui s'entassent. Mais les fichiers JSON restent acceptables si la fréquence est basse (> 10-30s).

---

### D) AMÉLIORATION CONCRÈTE & AVIS STRICT SUR LE PLAN

#### L'amélioration concrète de mon cru : **L'écriture atomique anti-corruption**
Pour fiabiliser l'architecture Cœur/Satellites (Étape 4) et l'écriture du contexte, interdisez l'écriture directe dans les fichiers JSON/JSONL. Utilisez toujours le pattern **Atomic Write** :
```python
import json
import os


def atomic_write(filepath, data):
  temp_path = f"{filepath}.tmp"
  with open(temp_path, "w") as f:
    json.dump(data, f)
    f.flush()
    os.fsync(f.fileno())  # Force l'écriture sur le disque du Mac
  os.replace(temp_path, filepath)  # Atomique sur UNIX
```
Cela élimine 100% des bugs de lecture de JSON corrompus (« *Expecting value: line 1 column 1 (char 0)* ») qui plantent les satellites en silence.

---

#### Mon avis strict sur l'ensemble du plan de Buffy :

* **Étape 1 (Batch prix) :** **BON.** Indispensable. (Attention toutefois au format du payload MEXC).
* **Étape 2 (Timeout agressif 10s x2) :** **EXCELLENT.** 40 secondes de timeout en trading, c'est du suicide. Si l'exchange ne répond pas en 5-10 secondes, le marché a déjà bougé. Couper court évite l'accumulation des threads pendants.
* **Étape 3 (Espacer les coûteux) :** **BON, mais insuffisant.** Les klines 360 bougies n'ont pas besoin d'être recalculées toutes les 60 secondes. Passez-les à 5 minutes minimum. Le régime de marché change rarement à la seconde près.
* **Étape 4 (Cœur / Satellites) :** **FONDAMENTAL.** C'est la seule façon de pérenniser le bot sur un MacBook sans qu'il s'asphyxie.
* **Étape 5 (Circuit-breaker 429) :** **CRITIQUE.** Un 429 sur MEXC doit déclencher un backoff exponentiel immédiat de toute l'application, pas seulement un "pause 30s" naïf. Si MEXC vous ban l'IP 5 minutes, le bot doit se mettre en mode "Safe/Sleep" sans spammer.

**Ce que je ferais différemment :**  
Ne touchez plus au code temps-réel du cœur tant que l'Étape 4 (Sortie des sondes lourdes) n'est pas faite. **Attaquez par l'Étape 4 et l'Étape 1 en même temps.** Le batch prix nettoie l'API, et sortir les sondes nettoie la logique. Le reste (timeouts, circuit-breaker) découlera naturellement de cette cure d'amaigrissement.

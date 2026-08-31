# CODEUR (provider Google Gemini)

### A) PRIORITÉ 1 (Batch prix) : Analyse critique et risques

#### 1. Est-ce la bonne première étape ?
**Oui, absolument.** C'est la seule et unique mesure d'urgence qui peut stabiliser le système immédiatement. Réduire la voilure réseau de 200–270 req/min à moins de 30 req/min fait sortir le bot de la zone rouge des rate-limits MEXC (souvent évalués sur une fenêtre glissante stricte de 60 secondes).

#### 2. Risques techniques et sémantiques
Passer d'appels individuels `GET /api/v3/ticker/price?symbol=XXX` à un appel global `GET /api/v3/ticker/price` (sans symbole) comporte plusieurs risques majeurs pour un bot de trading :

*   **Désynchronisation temporelle (Race Condition / Skew) :** 
    *   *Risque :* L'API globale renvoie un snapshot sérialisé par l'exchange à l'instant $T$. Si le traitement des 21 paires dans la boucle prend du temps (logs, calculs, écritures disque), la dernière paire évaluée du tableau utilise un prix qui a déjà 10 à 20 secondes de décalage par rapport à la première paire du même cycle.
    *   *Impact :* Faussement positif/négatif sur les signaux multi-paires ou les arbitrages/corrélations internes.
*   **Atomicité et Cohérence du Tick :**
    *   *Risque :* Dans l'ancienne méthode, chaque `last_price` était quasi-synchrone de la décision de la paire. Avec un cache de 15-20 secondes, le moteur prend des décisions d'exécution (Market/Limit) sur des prix figés. Si un flash crash ou un pump a lieu à $T+5$s, le bot continue de trader sur la photo de $T0$.
*   **Structure de données et Résilience (Ce qui peut casser) :**
    *   *Risque :* Le dictionnaire global retourné par MEXC est une liste d'objets `[{"symbol": "BTCUSDT", "price": "60000.0"}, ...]`. Si le format change, ou si une paire de la liste des 21 (ex: `EDEL`, souvent des paires exotiques/obscures) est absente du payload global (délestage, maintenance de paire, format de nommage exotique), le code plantera par `KeyError` ou `NoneType` exception si le parsing n'est pas blindé.

#### 3. Comment le faire sans tout casser (Implémentation robuste)
1. **Parser une seule fois par cycle (Map O(1)) :** Au tout début du cycle de 20s, effectuer l'appel global et le transformer immédiatement en un dictionnaire Python en mémoire : `prices_cache = {item['symbol']: float(item['price']) for item in response['data']}`.
2. **Injecter un TTL strict et un fallback :** Si l'appel global échoue, ne pas trader sur un cache périmé de plus d'un cycle ; lever une exception contrôlée pour sauter le cycle (circuit-breaker soft).
3. **Valider l'existence des paires :** Pour chaque paire suivie, vérifier `if symbol not in prices_cache:` avant de lire la valeur, avec log d'alerte immédiat au lieu d'un crash du thread principal.

---

### B) AUTRES CAUSES DE LOURDEUR / FRAGILITÉ (Vision Architecture)

Au-delà du nombre d'appels, le moteur souffre de tares architecturales classiques des bots "monolithiques bricolés" :

1. **L'I/O Bloquant Synchrone (Le goulot d'étranglement caché) :**
   Le bot fait du traitement séquentiel (boucle `for pair in pairs:`). Si l'écriture de `croisement_contexte.jsonl` sur le disque du MacBook (ou pire, un stockage géré par iCloud/Dropbox si le dossier est synchronisé) prend 50ms, multiplié par 21 paires, le cycle prend du retard. Les appels réseaux bloquants (`requests.get` sans pool de connexions optimisé ou sans asynchronisme) paralysent le thread principal.
2. **La gestion naïve de l'état (State Management) :**
   Écrire un fichier `.jsonl` à chaque minute et le faire relire par des satellites crée des conditions de concurrence (*race conditions* sur les fichiers) et des corruptions de données potentielles (`JSONDecodeError` si un satellite lit pendant que le cœur écrit).
3. **Le monolithe synchrone face à la complexité :**
   Mélanger la logique de décision (trading), la collecte de données (profondeur, carnets) et la télémétrie (écriture de contexte) dans une seule boucle synchrone de 20 secondes est une aberration architecturale. Le moindre hoquet réseau sur la profondeur d'une paire bloque l'évaluation des 20 autres.

---

### C) COSTAUD STRUCTUREL : Cœur / Satellites

#### Est-ce la bonne voie ?
**Oui, c'est la seule voie viable à moyen terme.** 
Séparer le **Plan de Données (Data Plane)** du **Plan de Contrôle / Exécution (Control/Execution Plane)** est le standard de l'industrie.

#### Le meilleur découpage (Validation & Ajustement de l'Étape 4) :
*   **Le Cœur (Le Bot Hulk) :** 
    *   *Rôle unique :* Gérer le portefeuille, calculer les signaux finaux basés sur des données *en mémoire*, et exécuter les ordres (Buy/Sell) sur l'API MEXC.
    *   *Règles d'or :* **Zéro appel réseau vers des endpoints de diagnostic/analyse.** Il consomme uniquement de la mémoire vive ou des structures locales ultra-légères.
*   **Les Satellites (Processeurs autonomes ou Daemons) :**
    *   Des scripts indépendants (ex: `sentinel_murs.py`, `sentinel_depth.py`) qui tournent à leurs propres fréquences (ex: carnet toutes les 5s, klines toutes les 2 min) et écrivent dans des **bases de données en mémoire partagée (ex: Redis local, ou fichiers atomiques avec double-buffering / `rename` atomique)**.

> ⚠️ **Attention au piège des fichiers JSON :** Ne faites pas écrire les satellites directement dans un fichier que le cœur lit en mode append/read direct sans verrouillage. Utilisez la technique du fichier temporaire + écriture complète + `os.replace()` (opération atomique au niveau du système de fichiers) pour que le cœur lise toujours une version intacte.

---

### D) AMÉLIORATION CONCRÈTE & AVIS STRICT SUR LE PLAN

#### 1. Avis global : Le plan est bon, mais l'Étape 2 est dangereuse en l'état
*   **Ce qui est très bon :** Le passage au batch prix (Étape 1) et la sortie des sondes de la boucle principale (Étape 4). Ce sont des évidences architecturales.
*   **Ce qui est risqué :** L'Étape 2 (`TIMEOUT 10s × 2 retries`). Réduire le timeout à 10s sur une connexion domestique ou un MacBook en Wi-Fi qui subit des micro-coupures ou du throttling DNS de l'ISP/MEXC va provoquer des faux positifs d'erreurs réseau constants. 
    *   *Alternative proposée :* Garder un timeout raisonnable (ex: 5s à 7s) mais faire **1 seul retry immédiat**, et surtout, implémenter un **backoff exponentiel** uniquement en cas de code HTTP 429 ou 5xx.

#### 2. L'amélioration concrète et prouvée (Le "Bonus Codeur") :
**L'Atomicité des Fichiers via Double-Buffering et l'abandon du `.jsonl` brut au profit d'un cache mémoire inter-processus léger (SQLite en mode WAL ou fichiers atomiques `.tmp` -> `.json`).**

Le problème récurrent des bots basés sur des fichiers JSON/JSONL sur un MacBook, c'est la corruption lors des lectures/écritures simultanées. 

Voici le pattern exact à implémenter pour les satellites et le cœur pour éliminer 100% des bugs d'I/O :

```python
import json
import os
import tempfile


def atomic_write_json(filepath: str, data: dict):
  """Écrit un fichier JSON de manière atomique pour

  garantir qu'aucun lecteur ne lit un fichier partiellement écrit.
  """
  dir_name = os.path.dirname(filepath)
  # Créer un fichier temporaire dans le même dossier (nécessaire pour os.replace atomique)
  with tempfile.NamedTemporaryFile(
      'w', dir=dir_name, delete=False, suffix='.tmp'
  ) as tf:
    json.dump(data, tf)
    temp_name = tf.name

  # Remplacement atomique au niveau du système d'exploitation
  os.replace(temp_name, filepath)
```

#### Synthèse des priorités d'exécution pour le codeur :
1. **Immédiat (Aujourd'hui) :** Batch `/ticker/price` + dictionnaire mémoire global + écriture atomique.
2. **Court terme (Demain) :** Sortir `book_sense` et `probe_aspiration` du cœur pour en faire des satellites asynchrones écrivant via `atomic_write_json

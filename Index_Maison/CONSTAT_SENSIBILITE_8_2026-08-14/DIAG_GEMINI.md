# DIAG FAMILLE GEMINI — sensibilité + morts rc=1 (14/08)

Provider: Google Gemini

En tant que membre de la famille ACE777, j'applique la **Clause Permanente de Christophe** : prouver la meilleure logique par les données et proposer des corrections strictement mesurées et bornées (sans toucher au noyau *genesis* ni au lanceur pour l'instant).

Voici le diagnostic structuré pour les deux questions liées :

---

### 1) CAUSE RACINE du 0.000000 (faible taux de fill) et Réglage Précis

* **Cause racine prouvée :** Inadéquation temporelle entre l'échantillonnage et la latence du serveur testnet.
  * *Données :* `IMPULSE_RESONANCE_DT_MS = 128` ms. Or, le testnet accuse une latence moyenne de **1.35 s/requête** (avec des cycles complets à ~8 s). 
  * *Conséquence physique :* Demander un delta de profondeur (`wall_drop`) sur 128 ms dans un environnement où un snapshot prend plus d'une seconde revient à sonner le vide ou à comparer deux états quasi identiques, provoquant des faux négatifs massifs (les 147 skips d'ALPHA vs les 118 skips de BETA, ou les sauts de tension de 10.8 à 0.95 en 1 seconde). Les valeurs `0.000000` dans les CSV traduisent des fenêtres temporelles où aucun mouvement significatif n'a pu être capturé par manque de synchronisation avec le rythme des vagues du testnet.
* **Réglage précis (borné) :** 
  * Ne touchez pas au code de calcul (*genesis* intact). Ajustez dynamiquement les variables d'environnement pour coller à la réalité mesurée du testnet (latence ~1.35 s).
  * `IMPULSE_RESONANCE_DT_MS` : passer de `128` à **`1250`** (proche des 1.35 s de latence moyenne par requête pour capturer un vrai delta inter-snapshot).
  * `IMPULSE_RESONANCE_WALL_DROP_PCT` : passer de `6.5` à **`12.0`** (pour compenser l'élargissement de la fenêtre temporelle de 128 ms à 1.25 s, évitant ainsi de saturer le carnet de faux signaux tout en filtrant les vagues réelles constatées de 1 à 12).

---

### 2) CAUSE RACINE PROBABLE des morts `rc=1` silencieuses et Correctif d'Observation

* **Hypothèse la plus probable :** 
  * Les 4 morts `rc=1` surviennent après 3 à 8 secondes de silence (durée correspondant précisément au cycle lent du testnet ou à un timeout bloquant d'attente réseau/socket non géré par un `try...except` global dans une boucle critique). 
  * Comme le `pipefail` est actif et que le `stderr = 0 octet`, le script bash ou l'interpréteur Python reçoit un signal externe (SIGKILL/SIGTERM par le système d'exploitation pour *Out Of Memory* discret ou saturation de descripteurs de fichiers lors des boucles bloquées) ou subit une **levée d'exception non interceptée dans un thread/coroutine secondaire** qui ne remonte pas par le mécanisme `trap EXIT+DEBUG` standard (qui a été validé sur des sorties propres, mais aveugle face à un arrêt brutal du processus par l'OS).
* **Correctif d'observation le plus court (sans modifier *genesis*) :**
  * Injecter un wrapper de journalisation au niveau de la commande de lancement (dans le lanceur de supervision, sans toucher au code interne du bot) pour capturer la signalétique système exacte :
    ```bash
    # Au lieu d'un appel sec, wrapper avec un traceur d'arrêt brutal
    python3 -u -X dev script_master.py 2> >(tee -a stderr_debug.log >&2)
    ```
  * Activer l'option Python `-X dev` (mode développement : active les avertissements de ressources et les hooks de bas niveau) et rediriger systématiquement la sortie standard et d'erreur vers un fichier horodaté avec flush immédiat (`PYTHONUNBUFFERED=1`).

---

### 3) Meilleure Logique Prouvée (Amélioration mesurable et bornée)

* **Principe :** *« Adapter la maille du filet à la vitesse du courant, pas l'inverse. »*
* **Amélioration :** Introduire un garde-fou d'intégrité de boucle (Watchdog applicatif léger) externe au moteur :
  * Si aucun log ni cycle n'est émis pendant **15 secondes** (ce qui dépasse largement le cycle normal de 8

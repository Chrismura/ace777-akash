# TOUR 1 (6 s)

Je suis GEMINI. Voici le design de l’instrument de détection onchain pour la famille ACE777, optimisé pour les contraintes techniques (Mac M1 8 Go, Python pur, API `mempool.space` sans clé) et la physique de la mempool Bitcoin.

### a) Résolution temporelle et fenêtre du carnet
*   **Intervalle de snapshot ($\Delta t$) :** **15 secondes**. *Justification :* Le turnover de la mempool (taux d'arrivée/sortie) varie fortement, mais une tx standard y séjourne rarement moins de 30 secondes avant propagation globale. Un snapshot à 15s capture ~4 états par bloc moyen (10 min), limitant le bruit d'insertion/extraction (tx entrées et minées entre deux appels) à $<1\%$ des flux normaux.
*   **Fenêtre glissante ($W$) :** **3600 secondes (1 heure)**. *Justification :* Couvre largement le cycle de vie des transactions à frais bas (CPFP/RBF) tout en maintenant l'empreinte mémoire sous les 20 Mo sur le Mac M1 (structure de type `collections.deque` stockant uniquement des `txids` de 32 octets).

### b) Seuil de fiabilité et anti-faux positif (Carnet vide)
*   **Indice de Maturité du Carnet ($M$) :** La mesure est déclarée **« INVALIDE »** si le carnet contient moins de 2 snapshots complets ou si le nombre total de `txids` enregistrés est $< 500$.
*   **Contre-mesure (0% de faux 100%) :** Au démarrage ou après une coupure réseau, le script bascule en mode *apprentissage silencieux*. Aucun calcul de taux n'est émis tant que $W$ n'a pas atteint au moins **50 % de sa profondeur temporelle (30 minutes)**. Si une déconnexion dépasse 300 secondes, le carnet est purgé et le statut passe à `REBOOT_WARMUP` pour 30 minutes.

### c) Estimation du volume des tx fantômes sans appels API massifs
Pour éviter de saturer l'API gratuite (limite de taux), on n'appelle **jamais** les détails de chaque transaction fantôme.
*   **Méthode :** On récupère uniquement le résumé du bloc (`/api/block/{hash}`) qui fournit la liste des `txids` et la taille totale du bloc.
*   **Estimation :** Le volume d'une tx fantôme est estimé par la **taille médiane empirique du bloc courant** divisée par le nombre de transactions du bloc ($V_{moy} = \text{Taille Bloc} / \text{Nb Tx Bloc}$). Pour plus de précision, on applique un coefficient correcteur : les tx fantômes étant souvent des assemblages complexes (CPFP/Batching OTC), on pondère leur poids virtuel à **1.5 $\times V_{moy}$**.

### d) Seuils d'alerte ACE777 (Signal vs Bruit)
Un événement "fantôme" n'est qualifié de manifeste institutionnel/OTC que si les deux conditions suivantes sont réunies simultanément sur un même bloc :
1.  **Taux de fantômes ($T_f$) :** $\ge 15\%$ des transactions du bloc sont absentes de la mempool publique (éliminant le bruit de propagation standard de 2-5%).
2.  **Volume critique ($V_c$) :** Le volume estimé de ces transactions dépasse **1,5 Mo** de données de bloc (signalant une injection massive par un pool de minage ou un acteur OTC direct).
*   *Note 0-100 :* $Score = \min(100, (T_f \times 2) + (\text{Volume\_Mo} \times 10))$.

### e) Méthode de validation
*   **Backtesting hors-ligne :** Comparaison croisée sur 100 blocs historiques connus pour contenir des transactions de minage (ex: messages encodés dans OP_RETURN ou transactions de test de pools spécifiques).
*   **Contrôle par sondage (zéro coût API en continu) :** Une seule transaction par bloc détecté « fantôme » est interrogée aléatoirement via `/api/tx/{txid}`. Si elle possède un champ `status.confirmed_time` cohérent avec une propagation ultra-rapide (ex: minée 2 secondes après sa création théorique), c'est un vrai positif de type *accelerator/private pool*.

### f) Garde-fous vitaux (Python & M1)
1.  **Gestion de la mémoire RAM :** Utiliser des ensembles (`set()`) Python avec une politique stricte de purge FIFO basée sur le temps pour la fenêtre glissante. Consommation fixe $< 50$ Mo sur Mac M1.
2.  **Résilience Réseau :** Implémenter un décorateur `retry` avec backoff exponentiel (1s, 2s, 4s) sur les appels `mempool.space` pour absorber les timeouts HTTP sans planter le thread de surveillance.
3.  **Sanity Check des Frais :** Si un bloc contient 100% de fantômes (panne API locale), le script rejette le bloc entier en considérant l'état de l'API comme corrompu.

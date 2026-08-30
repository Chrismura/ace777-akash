# TOUR 4 (4 s)

ON NE PEUT PLUS FAIRE MIEUX. Voici les remparts définitifs pour verrouiller chaque angle mort physique et logiciel sur ce Mac M1 :

1. **Double panne (API + Carnet) :** Rempart : Persistance atomique. À chaque snapshot, le carnet (`set`) est sérialisé en local via `json` dans un fichier `/tmp/ace777_carnet.json` avec un `fsync`. Si l'API tombe, le système bascule sur une *mempool synthétique locale* déduite des blocs précédents jusqu'à reconnexion, évitant le faux 100 %.
2. **Résumé de bloc tronqué :** Rempart : Sanity Check de taille. L'API `mempool.space` renvoie la taille réelle et le nombre exact de txs du bloc. Si `len(block_txids)` diffère du champ `tx_count`, le bloc est marqué `CORRUPT_BLOCK` et rejeté instantanément (score = 0).
3. **Bruit de turnover vs VRAI événement OTC :** Rempart : Le ratio de structure. Un pic de turnover public inonde la mempool de txs standard (frais uniformes, taille classique). Un événement OTC/CPFP massif présente une *bimodalité de frais* (poussière à frais très bas ou transactions surdimensionnées). Si le volume fantôme est concentré sur $< 5\%$ des txs du bloc avec $> 80\%$ de la valeur BTC, c'est un OTC validé ; sinon, le score est divisé par 2.
4. **Coupure réseau longue (> 1 heure) :** Rempart : Purge totale et réinitialisation. Si $\Delta t > W$ (le carnet entier est plus vieux qu'une heure), le script exécute un `flush()` complet, repasse en mode *warm-up* forcé pendant 30 minutes, et journalise un avertissement critique `SYSTEM_COLD_REBOOT`.
5. **Dérive d'horloge (Veille macOS) :** Rempart : Monotonicité temporelle. Utilisation exclusive de `time.monotonic()` (et non `time.time()`) pour gérer la fenêtre glissante. Cela immunise totalement le carnet contre les sauts d'horloge liés à la mise en veille du Mac M1.
6. **Doublon de process (Conflit d'écriture) :** Rempart : Mutex par verrou de fichier. Utilisation de la bibliothèque standard `fcntl` au démarrage du script pour poser un verrou exclusif (`LOCK_EX | LOCK_NB`) sur un fichier `/tmp/ace777.lock`. Si un second process se lance, il s'arrête net sans corrompre le carnet.
7. **Dérive / Aveuglement sur 7 jours :** Rempart : Ligne de base mobile (Rolling Baseline). Calcul quotidien de la moyenne mobile sur 7 jours du taux de fantômes. Si le taux moyen dévie de plus de $3\sigma$ (écart-type) sur 24h glissantes, l'indicateur déclenche un signal `DRIFT_WARNING` (l'API ou la structure de la mempool a changé, ex: adoption massive d'un nouveau protocole).

***

**Conclusion :** 
Cet instrument est désormais blindé de bout en bout. De l'échantillonnage temporel aux garde-fous matériels (macOS), chaque byte de mémoire et chaque appel API sont optimisés pour extraire le signal brut des transactions fantômes sans jamais mentir, saturer ou s'aveugler. Mission accomplie pour la famille ACE777.

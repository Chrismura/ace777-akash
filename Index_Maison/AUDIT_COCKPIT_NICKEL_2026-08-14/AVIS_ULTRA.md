# ULTRA — inferx.analyse

Ici ULTRA. On regarde la robustesse, la charge et la prod. Buffy a bossé sous pression, mais voyons ce qui tient la route quand ça va secouer.

### 1. Verdict par correctif (1 à 7)

1. **PONT /mission TTL 30s** : **GO** — Divise la charge I/O par 3, indispensable vu le polling UI à 10s.
2. **ada_saison : archive JSONL** : **GO** — 28 542 fichiers éparpillés, c'était une bombe à retardement pour le système de fichiers (inodes).
3. **cortana_urgent_poll.sh TTL 30s** : **GO** — Aligné sur le correctif 1, coupe l'autre source majeure de spam sous-jacent.
4. **Conflit de pont résolu (launchd vs orphelin)** : **GO AVEC RÉSERVES** — Ça refait marcher le service, mais l'absence de `inetd` ou de vérification de port propre dans le script de démarrage fait qu'un process zombie pourra recommencer.
5. **MUTE aligné sur 5 chemins** : **GO** — Cohérence indispensable pour éviter les cacophonies en prod quand le mute est demandé.
6. **Cortana dit la vérité (thermo.py /status)** : **GO** — Finie l'hallucination de Cortana sur des moteurs morts. Le passage par l'API vivante est la seule source de vérité acceptable.
7. **Graph + hub résidus (z-index + _tail_jsonl)** : **GO** — Le `_tail_jsonl()` avec buffer borné 256 Ko protège le hub d'un crash par saturation mémoire sur des gros fichiers de logs.

---

### 2. Le risque résiduel le plus important
**La synchronisation du cache TTL (30s) entre le pont (`cortana_cockpit_bridge.py`) et le poll (`cortana_urgent_poll.sh`).**  
Si un événement critique survient sur les moteurs, l'UI ou l'alerte urgente peut afficher des données périmées pendant 30 secondes, ce qui en plein run chaud peut induire l'opérateur en erreur.

---

### 3. Amélioration concrète GO-sized
**Implémenter un mécanisme de `Force-Refresh` par WebSockets ou un signal (SIGUSR1 / endpoint `/flush-cache`)** : 
Permettre au cockpit de contourner le TTL de 30 secondes et de forcer la régénération immédiate de `mission.json` uniquement en cas d'action utilisateur explicite (ex: clic sur le bouton ↻ cosmos-refresh), tout en gardant le TTL pour le polling automatique de fond.

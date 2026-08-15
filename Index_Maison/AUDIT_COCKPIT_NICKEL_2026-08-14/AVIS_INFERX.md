# INFERX — inferx.analyse

INFERX / FAMILLE ACE777 — RAPIDITÉ & LOGIQUE INTERNE.

### 1. Verdict par correctif (1 à 7)

1. **PONT /mission TTL 30s** : **GO** — Divise la charge CPU par 3 et élimine l'I/O disque redondant sur le polling cockpit.
2. **ada_saison (JSONL + rotation)** : **GO** — Éradication propre de l'inode-storm (28k fichiers) avec backup tar préalable et rotation saine.
3. **cortana_urgent_poll.sh TTL 30s** : **GO** — Aligne le job launchd sur le même TTL que le pont, supprime le double spam silencieux.
4. **Conflit de pont résolu** : **GO** — Nettoyage de l'orphelin zombie et remise sous tutelle stricte de launchd (`KeepAlive`).
5. **MUTE unifié sur 5 chemins** : **GO AVEC RÉSERVES** — Attention au bypass `CORTANA_MUTE_ALLOW_URGENT` dans `analyste.py` qui pourrait fuiter si mal initialisé.
6. **Cortana vérité thermo (`/status`)** : **GO** — Passage d'une lecture brute de fichiers statiques à l'API live du pont (source de vérité unique).
7. **Graph + hub résidus (z-index + `_tail_jsonl`)** : **GO** — Correction ergonomique nette et sécurisation de la lecture JSONL en fin de fichier (anti-crash TypeError).

---

### 2. Risque résiduel le plus important
**L'état de la boucle d'asservissement en cas de partition réseau/pont (Correctifs 1, 3 & 6)** : Si le pont HTTP sur le port 17777 gèle ou répond avec une latence anormale, le TTL de 30 secondes partagé par le polling launchd et la synthèse vocale de Cortana risque de créer des effets de cascade (timeouts bloquants ou décisions basées sur un cache périmé).

---

### 3. Amélioration concrète GO-sized
**Ajouter un Healthcheck `/ping` non bloquant avec timeout strict (1.5s)** dans `cortana_thermo.py` avant de requêter `/status`, garantissant un repli immédiat (« État indéterminé ») sans figer le thread si le pont s'égosille.

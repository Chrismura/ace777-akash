# AVIS GROK (task puter-grok.analyse · Google Gemini · 2026-08-27T19:19Z)

VERDICT : GO-AVEC-RÉSERVES
CONFIANCE : 90 %
HYPOTHÈSES : 
1. `atomic_write.py` gère correctement un verrou d'exclusion mutuelle (filet inter-processus via `fcntl.flock` ou équivalent) pour éviter la corruption en écriture concurrente.
2. Les 36 scripts lecteurs lisent en mode lecture seule non bloquante ou tolèrent un fichier temporaire pendant l'écriture atomique (renommage atomique `os.replace`).

CE QUI CHANGERAIT L'AVIS : 
Si les injecteurs partiels (comme `pont_onchain.py`) doivent impérativement persister leur état immédiatement sans attendre le prochain run complet du thermo (1h) et qu'une architecture en bus centralisé (Redis/SQLite) est rejetée par contrainte de stack.

AMÉLIORATION PROPOSÉE : 
1. **Patron "Read-Modify-Write" universel et centralisé** : Interdire aux scripts partiels d'écrire directement dans `live.json`. Ils doivent utiliser une fonction helper unique (`update_live_section(section_name, data)`) qui lit le JSON actuel, fusionne la sous-section sous verrou exclusif, et réécrit.
2. **Architecture Redis en façade (Optionnelle mais robuste)** : Remplacer à terme `live.json` sur disque par un stockage Redis local (ou SQLite en mode WAL) pour les écritures fréquentes de 5 min, le thermo complet ne faisant qu'un `HSET` massif, éliminant les risques de race condition sur un fichier plat.

SYNTHÈSE (5 lignes max)
Laisser 3 scripts écrire librement dans `live.json` est une aberration architecturale corrigée par un point d'entrée unique. 
Le fix impose que les sous-écrivains (onchain, 11 clés) passent par une fonction de fusion atomique centralisée.
Aucun script partiel ne doit plus jamais remplacer le payload global par une version tronquée.
Risque résiduel : un blocage de verrou si un processus plante en écriture (nécessite un timeout/filet `fcntl`).
Solution viable immédiatement sans casser les 36 lecteurs.

# AVIS ULTRA (task inferx.analyse · Google Gemini · 2026-08-27T19:19Z)

VERDICT : GO-AVEC-RÉSERVES
CONFIANCE : 92 %
HYPOTHÈSES : 
1. `SafeLiveWriter` utilise déjà un pattern `open(..., 'w')` avec renommage atomique (`os.replace`) mais sans verrou inter-processus (`fcntl.flock`).
2. Les 36 lecteurs gèrent correctement une lecture non bloquante pendant une écriture atomique (grâce au fichier temporaire + rename).
CE QUI CHANGERAIT L'AVIS : Si les scripts partiels continuent d'écrire directement dans `live.json` sans passer par le bus d'événements ou une API centralisée en ignorant le verrou.
AMÉLIORATION PROPOSÉE : 
1. **Bus d'événements/State Store en mémoire partagée (Redis ou fichier Lock-based)** : Remplacer l'écriture directe par un daemon central (ou pattern IPC par sockets/files d'attente) où les injecteurs envoient des *patches* JSON (ex: `PATCH /onchain`) au lieu de modifier le fichier global.
2. **Validation par Schéma (Pydantic / JSON Schema)** : Bloquer systématiquement toute écriture si le payload final fait moins de 60 clés ou manque des champs critiques (`geopol`, `mark`), avec rollback automatique immédiat.
SYNTHÈSE : 
Laisser des scripts partiels écraser un fichier global est une hérésie en prod. Le fix structurel exige d'interdire l'écriture directe du JSON complet aux injecteurs partiels au profit d'un pattern *Merge & Patch* atomique. L'écrivain principal ou un daemon central doit fusionner les deltas dans une structure en mémoire avant l'écriture disque finale sous verrou `fcntl`. Les 36 lecteurs restent intouchés.

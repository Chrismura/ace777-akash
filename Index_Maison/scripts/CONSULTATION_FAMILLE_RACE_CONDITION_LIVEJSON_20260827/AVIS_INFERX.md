# AVIS INFERX (task inferx.analyse · Google Gemini · 2026-08-27T19:19Z)

**VERDICT :** GO-AVEC-RÉSERVES  
**CONFIANCE :** 92 %  

**HYPOTHÈSES :**  
1. `SafeLiveWriter` (ou un mécanisme équivalent basé sur un fichier temporaire + `os.replace`) est déjà disponible et thread-safe/process-safe au niveau OS (atomicité POSIX).  
2. Le système de fichiers hébergeant `thermo/live.json` réside sur un stockage local (pas de NFS/réseau distant avec des verrous POSIX foireux).  

**CE QUI CHANGERAIT L'AVIS :**  
La découverte que certains injecteurs partiels tournent en concurrence directe synchrone et intensive sans file d'attente, provoquant des `OSError: Resource temporarily unavailable` en cas de contention prolongée du verrou.  

**AMÉLIORATION PROPOSÉE :**  
1. **Architecture Publisher/Subscriber interne :** Au lieu d'autoriser des scripts tiers à modifier directement un fichier JSON partagé, basculer vers un modèle où les injecteurs partiels écrivent leurs deltas dans un répertoire dédié `thermo/inbox/*.json` (nommé par source). Le processus principal `thermo_quotidien_free.py` (ou un daemon dédié) fusionne ces deltas lors de son cycle de construction du payload global.  
2. **Schéma de validation Pydantic / JSON Schema strict :** Imposer un garde-fou bloquant dans le writer atomique : si un payload entrant possède un nombre de clés inférieur au seuil critique (ex: < 50 clés au lieu de 64), le rejet est immédiat avec alerte critique, interdisant mathématiquement l'écrasement silencieux par un sous-ensemble.  

**SYNTHÈSE :**  
La source de vérité `live.json` subit une corruption chronique due à une architecture multi-écrivains non synchronisée. Le fix structurel exige la centralisation de l'écriture finale via un unique daemon ou un verrouillage strict (Mutex/Flock) combiné à une validation de schéma (garde-fou anti-régression de taille). Les injecteurs partiels ne doivent plus écrire directement dans `live.json`, mais déposer des deltas isolés.

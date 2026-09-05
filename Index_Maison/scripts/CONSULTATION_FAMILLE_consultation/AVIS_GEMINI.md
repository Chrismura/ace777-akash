# AVIS GEMINI (task gemini.analyse · Google Gemini · 2026-09-01T09:21Z)

VERDICT : GO-AVEC-RÉSERVES
CONFIANCE : 90 %

HYPOTHÈSES :
1. **Cache persistant du navigateur (Brave/Chromium) :** Brave utilise une session existante (`Opening in existing browser session`) et met en cache agressivement les fichiers statiques (`mission.js`, `index.html`) ou stocke un état en LocalStorage/SessionStorage, ignorant la version fraîche servie par le port 17800.
2. **Conflit de lanceurs / Contexte d'exécution :** L'utilisateur interagit potentiellement avec une instance lancée via l'ancien raccourci (`ACE777 Cockpit.app`) pointant vers une autre racine ou un autre port/contexte, alors que le diagnostic valide `~/Desktop/Cockpit.command`.

CE QUI CHANGERAIT L'AVIS :
- La confirmation formelle par capture réseau (DevTools) que le navigateur charge bien le nouveau `mission.js` du disque et non une version en cache.
- La preuve que l'UI visible ne pointe pas vers un autre port ou un autre serveur résiduel en arrière-plan.

AMÉLIORATION PROPOSÉE :
1. **Ajout d'un paramètre de versioning (Cache-Busting) dans le HTML :** Forcer le rechargement des scripts côté client via query string dynamique (`mission.js?v=TIMESTAMP`) pour invalider définitivement le cache navigateur sans intervention utilisateur.
2. **Implémentation d'un Health-Check visuel :** Afficher un hash de commit ou un horodatage de build directement dans le coin du cockpit pour identifier instantanément quelle version de l'UI est réellement affichée.

SYNTHÈSE (5 lignes max) :
Le serveur sert le bon code et le bon feed, mais le navigateur Brave (via une session existante) ou une confusion de lanceur maintient l'affichage obsolète. 
La cause racine réside dans la persistance du cache client ou l'utilisation de l'ancien raccourci `.app`. 
Aucune modification de Hulk n'est requise. 
La correction minimale consiste à purger le cache du navigateur ou à forcer l'ouverture d'une fenêtre de navigation privée.

---

### A. Cause racine la plus probable et preuves manquantes
* **Cause racine :** Cache persistant du navigateur (Brave s'attachant à une session existante sans revalider les scripts JS/HTML) ou confusion d'interface entre `Cockpit.command` et `ACE777 Cockpit.app`.
* **Preuves manquantes :** L'état exact du cache du navigateur et l'URL exacte (port compris) affichée dans la barre d'adresse de la fenêtre visuelle de l'utilisateur.

### B. Tests non destructifs à faire
1. Ouvrir le cockpit dans une **fenêtre de navigation privée** (Incognito) pointant sur `http://127.0.0.1:17800`.
2. Forcer un rechargement complet dans Brave (`Cmd + Shift + R` ou vider le cache pour `127.0.0.1`).
3. Vérifier via `lsof -i :17800` qu'un seul processus HTTP sert le dossier correct.

### C. Une correction minimale recommandée
Tuer le processus du navigateur en cours et lancer le cockpit en mode forcé sans cache, ou utiliser explicitement une nouvelle instance de navigateur pointant vers le serveur actif, sans toucher aux scripts de trading.

### D. Corrections à ne surtout pas faire
* Ne pas modifier les scripts Python de Hulk (`hulk.py`, états, seeds, trades).
* Ne pas modifier les fichiers JSON de persistance du bot.
* Ne pas réécrire le serveur HTTP ou changer le port 17800 sans cartographie préalable.

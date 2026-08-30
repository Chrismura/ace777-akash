# AVIS GEMINI (task gemini.analyse · Google Gemini · 2026-08-21T19:33Z)

VERDICT : GO-AVEC-RÉSERVES  
CONFIANCE : 82 %  

HYPOTHÈSES :  
1. Le plist a été déchargé par `launchctl bootout` suite à une mise à jour d'OS, une déconnexion de session (GUI vs SSH), ou une corruption de l'index de launchd.  
2. Le `watchdog_superviseur` (ou `superviseur.sh`) est lui-même un processus dépendant du contexte utilisateur ou d'un autre plist mort, créant une angle mort en cascade.  
3. `launchctl load` a été exécuté sans l'option de persistance moderne (`bootstrap` via domaine de session GUI), provoquant sa perte au premier redémarrage ou changement de contexte utilisateur.  

CE QUI CHANGERAIT L'AVIS :  
L'accès aux logs bruts (`com.apple.launchd` via `log show`) de la fenêtre temporelle exacte du déchargement et l'état exact du domaine utilisateur (`launchctl print gui/501`).  

AMÉLIORATION PROPOSÉE :  
1. **Migration vers `launchctl bootstrap` et domaine de service système/GUI** : Abandonner définitivement `launchctl load` (obsolète) au profit de `launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/...` pour garantir l'ancrage dans la session graphique persistante.  
2. **Dédoublement du DMS hors de la machine** : Ne pas confier la surveillance des plists uniquement à des processus tournant sur le même MacBook Air. Un heartbeat externe (type healthchecks.io ou cron distant) doit valider que le superviseur pousse son signal de vie, sinon alerte immédiate.  
3. **Implantation d'un Daemon racine (LaunchDaemons)** pour les fonctions critiques au lieu de LaunchAgents, afin de s'affranchir des contraintes de verrouillage de session utilisateur macOS.  

SYNTHÈSE :  
Un plist ne meurt jamais "seul" : macOS le décharge suite à une rupture de session, un reboot, ou un appel `bootout` implicite. `launchctl load` n'est pas fiable sur les OS récents et perd sa persistance hors contexte GUI. Le vrai problème est structurel : reposer sur des LaunchAgents et des scripts locaux pour s'auto-surveiller crée un angle mort fatal. Il faut externaliser le Dead Man's Switch et moderniser les appels `launchctl`.

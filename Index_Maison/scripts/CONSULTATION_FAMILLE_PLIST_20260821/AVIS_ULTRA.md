# AVIS ULTRA (task inferx.analyse · Google Gemini · 2026-08-21T19:33Z)

VERDICT : NON
CONFIANCE : 95 %

HYPOTHÈSES : 
1. Le plist a planté avec un code de sortie non-zéro répété, provoquant sa mise en quarantaine ou son déchargement automatique par `launchd` (mécanisme de protection contre les boucles de crash).
2. Le `watchdog_superviseur` (ou `superviseur.sh`) tourne lui-même dans un contexte utilisateur ou un autre plist qui a échoué ou dont le chemin absolu était invalide lors d'une rotation de session.
3. Une mise à jour ou un redémarrage a réinitialisé l'état des sessions graphiques (`Aqua`), empêchant le chargement des `LaunchAgents` utilisateur sans intervention d'une session interactive (`launchctl bootstrap`).

CE QUI CHANGERAIT L'AVIS : 
- Un log `launchd` prouvant un déchargement manuel (`launchctl bootout`).
- La preuve que `KeepAlive` était correctement configuré avec un `SuccessfulExit` explicite.

AMÉLIORATION PROPOSÉE : 
1. **Sortir de `~/Library/LaunchAgents` :** Migrer le service critique vers `/Library/Daemons/` pour qu'il tourne au niveau système (root) et survive aux fermetures de session utilisateur (`Aqua`).
2. **Implémenter un Heartbeat externe (Dead Man's Switch cloud ou distant) :** Ne pas compter sur la machine locale pour surveiller sa propre santé si la stack s'effondre.
3. **Forcer la résilience `KeepAlive` :** Configurer le plist avec `KeepAlive: { SuccessfulExit: false, Crashed: true }` et ajouter `ThrottleInterval` pour éviter le spam CPU en cas de boucle de crash.

SYNTHÈSE :
Un `LaunchAgent` utilisateur meurt silencieusement lors des ruptures de session ou de plantages répétés que `launchd` finit par blacklister. Compter sur `~/Library/LaunchAgents` pour de la prod critique est une hérésie d'architecture. Il faut basculer en Daemon système (`/Library/Daemons`) et découpler totalement la surveillance du processus local en panne.

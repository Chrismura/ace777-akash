# AVIS JUGE (task juge.tranche · Google Gemini · 2026-08-21T19:33Z)

VERDICT : GO AVEC RESERVES
CONFIANCE : 88 %

HYPOTHÈSES :
1. Le plist a été déchargé par `launchd` en raison d'une boucle de plantages consécutifs (crash loop) sans la clé `<key>KeepAlive</key>` configurée proprement.
2. `launchctl load` (méthode legacy) a été utilisé sans l'ancrage robuste du domaine GUI, provoquant son éviction lors d'une micro-coupure de session.
3. Le watchdog local est aveugle au registre `launchd` et ne surveillait que la présence volatile du PID en mémoire.

CE QUI CHANGERAIT L'AVIS :
La sortie brute de `log show --predicate 'subsystem == "com.apple.launchd"' --last 1h` confirmant s'il s'agit d'un `bootout` explicite ou d'un abandon sur crash.

AMÉLIORATION PROPOSÉE :
1. **Migration obligatoire vers `launchctl bootstrap gui/$(id -u)`** combiné aux clés XML `<key>KeepAlive</key><true/>` et `<key>RunAtLoad</key><true/>` dans tous les plists de `~/Library/LaunchAgents/`.
2. **Ajout d'une sonde de registre `launchctl` dans `superviseur.sh`** : le script ne doit pas seulement checker le PID mais exécuter `launchctl list com.ace777.superviseur-core` pour détecter un déchargement instantanément.
3. **Mise en place d'un Heartbeat externe minimaliste** (ex: un simple cron ou script distant) qui crie au loup si le superviseur local ne valide pas son état toutes les 5 minutes, s'affranchissant ainsi de la cécité d'un watchdog local potentiellement mort.

SYNTHÈSE :
Le plist a disparu de `launchd` suite à un crash loop ou une perte de session, et le watchdog local n'a rien vu car il ne vérifiait pas le registre système. Conformément à la clause permanente, il ne suffit pas de recharger le plist : il faut impérativement moderniser son injection via `bootstrap`, forcer `KeepAlive`, et coupler le contrôle à une vérification directe de `launchctl`.

# AVIS GROK (task puter-grok.analyse · Google Gemini · 2026-08-21T19:33Z)

VERDICT : NON
CONFIANCE : 90 %

HYPOTHÈSES :
1. Le plist a planté à répétition (crash loop), poussant `launchd` à le placer en quarantaine ("KeepAlive" mal configuré ou exit code non-zéro répété).
2. Une mise à jour ou un nettoyage a supprimé/déchargé le service, et `launchctl load` n'a pas été exécuté avec l'option `-w` (nécessaire pour persister à travers les reboots/sessions).
3. Le `watchdog_superviseur` surveillait les processus en vain car le binaire lui-même était orphelin ou le script de supervision était bloqué.

CE QUI CHANGERAIT L'AVIS :
Les logs exacts de `launchd` (`log show --predicate 'process == "launchd"' --info`) pour l'heure de la mort du plist, prouvant s'il s'agit d'un crash, d'une décharge manuelle ou d'un nettoyage OS.

AMÉLIORATION PROPOSÉE :
1. **Option `-w` et mode Bootstrap :** Remplacer les vieux `launchctl load` par `launchctl bootstrap gui/$(id -u)` combiné avec l'écriture du plist dans `~/Library/LaunchAgents/` avec `KeepAlive = true` et des limites de backoff pour éviter la quarantaine.
2. **Délégation Watchdog hors-macOS/launchd :** Ne pas compter uniquement sur `launchd` pour relancer le superviseur core. Mettre en place un vrai *daemon* externe ou une supervision croisée via cron/system-timer (ou un second script minimaliste) qui fait un `launchctl print` et force un `bootstrap` si l'état est absent.
3. **Heartbeat externe :** Déporter l'alerte du DMS sur un canal indépendant (ex: webhook externe type curl direct) qui hurle dès que le heartbeat s'arrête 2 minutes, sans attendre que le Mac réalise qu'il est aveugle.

SYNTHÈSE :
Un plist disparaît de `launchd` soit suite à un crash répété (quarantaine), soit par un `unload` non persistant. `launchctl load` simple ne garantit pas la survie après un incident lourd ou un redémarrage si l'état est corrompu. Le watchdog local était aveugle car le superviseur lui-même était mort. Il faut passer à un bootstrap moderne avec relance croisée externe.

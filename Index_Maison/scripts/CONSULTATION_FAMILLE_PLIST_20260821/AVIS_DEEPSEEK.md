# AVIS DEEPSEEK (task deepseek.analyse · Google Gemini · 2026-08-21T19:33Z)

VERDICT : NON
CONFIANCE : 95 %

HYPOTHÈSES :
1. Le plist `com.ace777.superviseur-core` a planté avec un code de sortie non-zéro répété, provoquant sa mise en quarantaine ou son déchargement par `launchd` (mécanisme de protection contre les boucles de crash).
2. Le script `watchdog_superviseur` surveillait des processus en mémoire mais ne vérifiait pas l'état réel de `launchd` via `launchctl list`, créant un angle mort.
3. Le flag `-w` n'a pas été utilisé lors du chargement initial (`launchctl bootstrap` ou `load`), empêchant la persistance après un redémarrage ou une modification du système.

CE QUI CHANGERAIT L'AVIS :
Fournir les logs de `launchd` pour le domaine utilisateur (`log show --predicate 'subsystem == "com.apple.launchd"' --info`) prouvant qu'aucun crash n'a eu lieu, ainsi que le code source exact de `watchdog_superviseur`.

AMÉLIORATION PROPOSÉE :
1. **Remplacement par des daemons natifs et `KeepAlive` strict :** Configurer les plists avec la clé `<key>KeepAlive</key><true/>` et `<key>RunAtLoad</key><true/>` combinée à un `StandardErrorPath` pour logger les plantages.
2. **Supervision externe par `launchctl` :** Modifier le superviseur pour qu'il interroge directement `launchctl list com.ace777.superviseur-core` plutôt que de se fier uniquement à la présence du processus en mémoire.
3. **Migration vers un gestionnaire robuste (ex: `daemon` ou systemd-like sous macOS si applicable, ou script Python gérant un `pidfile` avec auto-reboot via cron ou daemondo) :** `launchd` est trop opaque sur macOS pour des architectures critiques ACE777 sans supervision de son état de santé.

SYNTHÈSE :
Le déchargement silencieux d'un plist sous macOS découle généralement d'un crash récurrent provoquant un abandon par `launchd` ou d'une absence de persistance explicite (`KeepAlive`). Le watchdog actuel souffre d'un angle mort en ne vérifiant pas l'état du démon dans le registre du système. Il est impératif d'imposer un monitoring direct de `launchctl` et d'abandonner les scripts de supervision aveugles.

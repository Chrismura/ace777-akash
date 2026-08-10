# AVIS ULTRA (task ultra.analyse)

provider: OpenRouter Nemotron 3 Ultra 550B (free) - analyse forte

**VERDICT : GO AVEC RESERVES**

**RESERVES CONCRETES :**

1. **superviseur_core.sh (boucle while)** : Absence de gestion `--force` (FORCE=1) — ajouter en tout début de boucle `if [ "${FORCE:-0}" -eq 1 ]; then FORCE=0; ... forcer check_due=0 ... fi` pour exécuter un cycle immédiat puis continuer.
2. **watchdog_superviseur.sh (ligne 4)** : `set -o pipefail` **incompatible Bash 3.2 macOS** — supprimer `pipefail` (garder `set -u` seulement).
3. **watchdog_superviseur.sh (ligne 28)** : `launchctl load` chemin durci `~/Library/LaunchAgents/` — utiliser `launchctl bootstrap gui/$(id -u) <plist>` (moderne) ou variable `$PLIST_PATH` pour robustesse multi-env.
4. **watchdog_superviseur.sh (ligne 15)** : `pgrep -f 'superviseur_core.sh'` match large — risquer faux positif si éditeur/autre processus contient la chaîne ; préférer `pgrep -f 'bash.*superviseur_core\.sh'` ou stocker PID launchd via `launchctl print`.

# AVIS INFERX (task inferx.analyse · Google Gemini · 2026-08-21T19:33Z)

**VERDICT :** GO-AVEC-RÉSERVES
**CONFIANCE :** 82 %

**HYPOTHÈSES :**
1. Le plist a planté avec un code de sortie non-zéro répété, poussant `launchd` à abandonner les tentatives de redémarrage (comportement standard si `KeepAlive` est mal configuré).
2. Le `watchdog_superviseur` vérifie l'existence du processus en mémoire mais ne vérifie pas l'état du job dans `launchctl`, créant un angle mort.
3. Le fichier plist a été modifié ou écrasé par un script de déploiement/mise à jour, provoquant un déchargement implicite.

**CE QUI CHANGERAIT L'AVIS :**
L'accès aux logs de `launchd` pour le domaine utilisateur (`/var/log/system.log` ou `log show --predicate 'process == "launchd"'`) prouvant une suppression manuelle via `launchctl unload`.

**AMÉLIORATION PROPOSÉE :**
1. **Implémenter un Healthcheck Bidirectionnel :** Ne pas se contenter de vérifier si le processus tourne via `ps`, mais interroger `launchctl list | grep com.ace777` depuis le watchdog pour forcer un `launchctl bootstrap` immédiat si le job est absent du registre.
2. **Durcir la clé `KeepAlive` :** Ajouter explicitement `<key>KeepAlive</key><dict><key>SuccessfulExit</key><false/></dict>` pour garantir que `launchd` relance le service même après un crash brutal.
3. **Migration vers une supervision externe (Heartbeat) :** Puisque le superviseur local peut mourir avec son plist, déporter l'alerte DMS sur un démon indépendant ou un cron système (root) qui valide l'activité du fichier de log du superviseur (ex: `find ... -mmin +5`).

**SYNTHÈSE :**
Un plist ne disparaît jamais de `launchd` par magie : soit il a crashé en boucle menant à son abandon, soit il a été déchargé par une action externe. Le watchdog actuel est aveugle aux états de `launchd`. Pour stabiliser la chaîne ACE777, il faut lier la surveillance au registre du système et non plus seulement aux processus actifs.

# SPEC — Plists qui meurent sans alerte (21/08 20:50)

## Constat
Le plist `com.ace777.superviseur-core` n'était PAS chargé dans launchd.
Conséquence : la chaine 9/9 est passée en ALERTE.
Le DMS (Dead Man's Switch) l'a détecté mais trop tard.

## Questions
1. Pourquoi un plist se décharge-t-il sans qu'on le sache ?
2. Est-ce que `launchctl load` est persistant après un reboot ?
3. Le watchdog_superviseur aurait dû le relancer — pourquoi il ne l'a pas fait ?
4. Est-ce un problème structurel (plist pas persistant) ou un accident ?
5. Quel est le mécanisme fiable pour qu'un plist reste chargé en permanence ?

## Contexte
- OS: macOS (MacBook Air)
- plists dans ~/Library/LaunchAgents/
- launchd gère les plists
- superviseur.sh vérifie les processus chaque minute
- auto_reparer.py est en mode actif depuis aujourd'hui

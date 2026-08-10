# Commande d'arrêt ACE777

## 🎯 LA commande officielle (fait TOUT)

**Ouvre un NOUVEAU terminal** (pas celui où le cycle tourne), puis :

```bash
cd /Users/christophe/ace777-test-day1 && ./stop_ace777.sh
```

Cette commande fait TOUT, dans le bon ordre :
1. **Arrêt des 4 services 3 étages** (watchdog EN PREMIER — sinon il relance tout — puis superviseur-core, cockpit-pont, cockpit-http) via `launchctl bootout`
2. **Arrêt de tous les anciens processus** (vortex, genesis, master, radar, watchdog Ruby...)
3. **Vérifications de sécurité** (filet kill -9 + alertes si un processus résiste)

## 🛟 One-liner de secours (si on ne peut pas lancer le script)

```bash
# 1. Services 3 étages (ordre CRITIQUE : watchdog en premier, sinon il relance tout)
launchctl bootout gui/$(id -u)/com.ace777.watchdog 2>/dev/null
launchctl bootout gui/$(id -u)/com.ace777.superviseur-core 2>/dev/null
launchctl bootout gui/$(id -u)/com.ace777.cockpit-pont 2>/dev/null
launchctl bootout gui/$(id -u)/com.ace777.cockpit-http 2>/dev/null

# 2. Anciens processus (liste complète)
cd /Users/christophe/ace777-test-day1 && touch STOP STOP_ALPHA STOP_BETA 2>/dev/null
kill -9 -$(cat runs/master.pid 2>/dev/null) 2>/dev/null; kill -9 $(cat runs/master.pid runs/alpha.pid runs/beta.pid 2>/dev/null) 2>/dev/null
pkill -9 -f launch_vortex_v2_collab; pkill -9 -f watchdog_ace777; pkill -9 -f "caffeinate -is -w"
pkill -9 -f genesis_manifest; pkill -9 -f "tail -n +85"; pkill -9 -f "tail.*genesis"
pkill -9 -f "bash -s"; pkill -9 -f launch_test_master_base; pkill -9 -f launch_test_master
pkill -9 -f radar_gate; pkill -9 -f "ruby.*sleep"; pkill -9 -f "vortex_supervisor_v2_llm.rb"
echo "Arrêté"
```

## 🔍 Vérifier que tout est éteint

```bash
# Les 4 services 3 étages doivent avoir disparu de launchd :
launchctl list | grep -E 'superviseur-core|watchdog|cockpit-pont|cockpit-http'
#   → rien ne doit s'afficher

# Aucun processus critique résiduel :
pgrep -f 'superviseur_core\.sh'     # → rien
pgrep -f 'watchdog_superviseur'     # → rien
```

## 🔄 Redémarrer SANS reboot

```bash
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.ace777.superviseur-core.plist
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.ace777.watchdog.plist
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.ace777.cockpit-pont.plist
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.ace777.cockpit-http.plist
```

Note : après un REBOOT complet, ces services se rechargent automatiquement au
login — rien à faire. La relance manuelle ne sert que pour un stop/start dans la
même session.

**Si ça ne marche pas :** Ctrl+C dans le terminal où le cycle tourne.

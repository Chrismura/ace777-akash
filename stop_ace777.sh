#!/usr/bin/env bash
# Arrêt ACE777 — À lancer dans un NOUVEAU terminal

cd /Users/christophe/ace777-test-day1

# === ARRET SERVICES 3 ETAGES (codeur hub, 10/08) =============
# Ordre CRITIQUE : superviseur + watchdog EN PREMIER (sinon ils relancent tout).
# KeepAlive=true -> seul launchctl bootout arrete vraiment.
echo "=== [3ETAGES] Arret des services launchd (KeepAlive=true) ==="

# 0. superviseur + vigie-live — les respawneurs de la maison (relancent les process
#    PENDANT le stop si on ne les bootout pas). FIX PANIC 12/08.
#    NOTE : com.ace777.prise-ia (hub IA) n'est PAS arrêté — il doit survivre (cerveau).
launchctl bootout gui/$(id -u)/com.ace777.superviseur 2>/dev/null
launchctl bootout gui/$(id -u)/com.ace777.superviseur-process 2>/dev/null
launchctl bootout gui/$(id -u)/com.ace777.vigie-live 2>/dev/null
pkill -9 -f 'superviseur\.sh' 2>/dev/null

# 1. watchdog — doit etre arrete en premier (garde-fou R5, famille 10/08)
if launchctl bootout gui/$(id -u)/com.ace777.watchdog 2>/dev/null; then
    echo "[3ETAGES] com.ace777.watchdog arrete"
else
    if ! launchctl list | grep -q "com.ace777.watchdog"; then
        echo "[3ETAGES] com.ace777.watchdog absent (deja arrete)"
    else
        # Garde-fou : le bootout a echoue et le service est encore enregistre
        echo "[3ETAGES] bootout echoue — tentative de kill -9..."
        pkill -9 -f 'watchdog_superviseur' 2>/dev/null
        sleep 1
        if pgrep -f 'watchdog_superviseur' > /dev/null; then
            echo ""
            echo "!!! ALERTE : LE WATCHDOG EST ENCORE ACTIF — arret interrompu, verifier manuellement !!!"
            echo ""
            exit 1
        else
            echo "[3ETAGES] com.ace777.watchdog arrete EN FORCE (bootout echoue, kill -9)"
        fi
    fi
fi

# 2. superviseur-core — gardien principal
if launchctl bootout gui/$(id -u)/com.ace777.superviseur-core 2>/dev/null; then
    echo "[3ETAGES] com.ace777.superviseur-core arrete"
else
    if launchctl list | grep -q "com.ace777.superviseur-core"; then
        echo "[3ETAGES] com.ace777.superviseur-core WARN bootout echoue"
    else
        echo "[3ETAGES] com.ace777.superviseur-core absent (deja arrete)"
    fi
fi

# Filet de securite superviseur-core (recherche elargie R4, famille 10/08)
if pgrep -f 'superviseur_core\.sh' > /dev/null; then
    echo "[3ETAGES] Processus superviseur_core.sh residuel detecte — kill -9"
    pkill -9 -f 'superviseur_core\.sh' 2>/dev/null
    sleep 1
    if pgrep -f 'superviseur_core\.sh' > /dev/null; then
        echo ""
        echo "!!! ALERTE : superviseur_core.sh encore actif apres kill -9 !!!"
        echo ""
        exit 1
    fi
else
    echo "[3ETAGES] Aucun processus superviseur_core.sh residuel"
fi

# 3. cockpit-pont — pont vocal/chat
if launchctl bootout gui/$(id -u)/com.ace777.cockpit-pont 2>/dev/null; then
    echo "[3ETAGES] com.ace777.cockpit-pont arrete"
else
    if launchctl list | grep -q "com.ace777.cockpit-pont"; then
        echo "[3ETAGES] com.ace777.cockpit-pont WARN bootout echoue"
    else
        echo "[3ETAGES] com.ace777.cockpit-pont absent (deja arrete)"
    fi
fi

# 4. cockpit-http — tableau de bord
if launchctl bootout gui/$(id -u)/com.ace777.cockpit-http 2>/dev/null; then
    echo "[3ETAGES] com.ace777.cockpit-http arrete"
else
    if launchctl list | grep -q "com.ace777.cockpit-http"; then
        echo "[3ETAGES] com.ace777.cockpit-http WARN bootout echoue"
    else
        echo "[3ETAGES] com.ace777.cockpit-http absent (deja arrete)"
    fi
fi

echo "=== [3ETAGES] Services 3 etages arretes ==="
# Fin section 3 etages

touch STOP STOP_ALPHA STOP_BETA 2>/dev/null

# 1. Groupe process (priorité)
mp=$(cat runs/master.pid 2>/dev/null)
[ -n "$mp" ] && kill -9 -"$mp" 2>/dev/null
[ -n "$mp" ] && kill -9 "$mp" 2>/dev/null

# 2. Alpha, Beta
for p in $(cat runs/alpha.pid runs/beta.pid 2>/dev/null); do
  kill -9 -"$p" 2>/dev/null
  kill -9 "$p" 2>/dev/null
done

# 3. pkill
pkill -9 -f "launch_vortex_v2_collab" 2>/dev/null
pkill -9 -f "watchdog_ace777" 2>/dev/null
pkill -9 -f "caffeinate -is -w" 2>/dev/null
pkill -9 -f "genesis_manifest" 2>/dev/null
pkill -9 -f "tail -n +85" 2>/dev/null
pkill -9 -f "tail.*genesis" 2>/dev/null
pkill -9 -f "bash -s" 2>/dev/null
pkill -9 -f "launch_test_master_base" 2>/dev/null
pkill -9 -f "launch_test_master" 2>/dev/null
pkill -9 -f "tail.*genesis" 2>/dev/null
pkill -9 -f "radar_gate" 2>/dev/null
pkill -9 -f "ruby.*sleep" 2>/dev/null
pkill -9 -f "vortex_supervisor_v2_llm.rb" 2>/dev/null
if [ -f runs/timer.pid ]; then
  kill -9 "$(cat runs/timer.pid)" 2>/dev/null || true
  rm -f runs/timer.pid
fi
if [ -f runs/supervisor_v9_v2.pid ]; then
  ./scripts/stop_supervisor_v9_v2.sh 2>/dev/null || \
    kill -9 "$(cat runs/supervisor_v9_v2.pid)" 2>/dev/null || true
fi

# 4. Tout ce qui reste
# FIX PANIC 12/08 : on exclut CE script lui-même ($$) et les scripts d'arrêt,
# sinon le pkill se tue lui-même en plein milieu et le radar / cockpit-http
# (qui viennent après dans la liste) survivent au PANIC.
SELF=$$
for pid in $(ps -e -o pid= -o args= 2>/dev/null | grep -E "ace777-test-day1|genesis_manifest|launch_test_master" | grep -v grep | grep -vE "stop_ace777" | awk '{print $1}'); do
  [ "$pid" = "$SELF" ] && continue
  kill -9 "$pid" 2>/dev/null
done

echo "Arrêté."

export STATE_PHASE="stopped"
./scripts/update_state_md.sh 2>/dev/null || true
./scripts/post_run_report.sh 2>/dev/null || true

if [ -x ./scripts/post_stop_cleanup.sh ]; then
  ./scripts/post_stop_cleanup.sh
fi

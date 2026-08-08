# ACE777 — MANIFESTE DE SAUVEGARDE ULTIME V3.5 (MONOLITHIQUE)
**Assemblé:** 2026-07-15T06:38:53Z
**Champion:** genesis md5 37fca367 | Enveloppe V2.2.1_NO_SUICIDE

# [PARTIE 1] — PROTOCOLE DE STÉRILITÉ ET NETTOYAGE APPLIQUÉ (ANTI-SABOTAGE)

**Statut:** ✅ Compilé  
**Réf:** ACE777_SAUVEGARDE_ULTIME_V3.5  
**Date:** 2026-07-15

---

## 1.1. Diagnostic de la Faille d'Accumulation (Zombies `tail -F`)

### Mécanisme V2.1 (bug)

Dans NUAGE V2.1_STROBOSCOPE, chaque unité (BETA/ALPHA) lance un pipeline asynchrone :

```bash
tail -n 0 -F "$raw_log" | while read line; do
  printf '[%s] %s\n' "$unit" "$line" >>"$live_log"
  printf '[%s] %s\n' "$unit" "$line"   # stdout terminal
done &
```

**Problème:** à chaque relance watchdog ALPHA ou redémarrage de session :
- le processus `tail -F` devient **orphelin** (PPID=1 ou parent tué sans kill du tail)
- les relances empilent **2, 4, 8… tails** par oiseau
- chaque tail maintient un descripteur ouvert sur `.NUAGE_*.raw.log` + pipe actif

### Impact matériel constaté (session 14/07/2026)

| Symptôme | Mesure / observation |
|---|---|
| Swapouts macOS | **39 872** swapouts cumulés (~1/s sur run long pollué) |
| RAM MacBook Air M1 8 Go | Saturation — 12+ processus bash/tail actifs |
| Thermal | `machdep.xcpm.cpu_thermal_level` monte malgré **26°C ambiant** |
| SSD | Écritures logs + swap → usure cellules NAND |

### Correctif V2.2 / V2.2.1 — fichiers `*_tail.pid`

Enregistrement PID du subshell tail → kill ciblé avant relance :

```bash
nuage_kill_tail_for_unit() {
  local unit="$1"
  local raw_log="${RUN_DIR}/.${tag}_${unit}.raw.log"
  local tpf="${RUN_DIR}/${unit}_tail.pid"
  local tp=""

  [ -f "$tpf" ] && tp="$(tr -d ' \n\r' <"$tpf" 2>/dev/null || true)"
  if [ -n "$tp" ]; then
    pkill -P "$tp" 2>/dev/null || true
    kill -TERM "$tp" 2>/dev/null || true
    sleep 0.5
    pkill -KILL -P "$tp" 2>/dev/null || true
    kill -KILL "$tp" 2>/dev/null || true
  fi
  pkill -f "tail -n 0 -F ${raw_log}" 2>/dev/null || true
  pkill -f "tail -F ${raw_log}" 2>/dev/null || true
  rm -f "$tpf"
}
```

Dans `run_unit()` — écriture du PID + kill à la fin :

```bash
run_unit() {
  local unit="$1"
  local raw_log="${RUN_DIR}/.${tag}_${unit}.raw.log"
  local live_log="${RUN_DIR}/${tag}_LIVE_COLOR.log"
  local wrapper_pid=0
  local genesis_pid=0
  local tee_pid=0

  : >"$raw_log"

  (
    trap '' PIPE
    _linebuf tail -n 0 -F "$raw_log" 2>/dev/null | while IFS= read -r line || [ -n "$line" ]; do
      [ -z "${line//[[:space:]]/}" ] && continue
      printf '[%s] %s\n' "$unit" "$line" >>"$live_log" 2>/dev/null || true
      printf '[%s] %s\n' "$unit" "$line"
    done
  ) &
  tee_pid=$!
  echo "$tee_pid" >"${RUN_DIR}/${unit}_tail.pid"

  set +e
  _linebuf ace777_stream_genesis >>"$raw_log" 2>&1 &
  wrapper_pid=$!
  genesis_pid="$(nuage_resolve_bash_s_pid "$wrapper_pid")"
  set -e

  echo "$genesis_pid" >"${RUN_DIR}/${unit}_genesis.pid"
  echo "$wrapper_pid" >"${RUN_DIR}/${unit}_wrapper.pid"

  wait "$wrapper_pid" 2>/dev/null || true
  local rc=$?

  nuage_kill_tail_for_unit "$unit"
  kill "$tee_pid" 2>/dev/null || true
  wait "$tee_pid" 2>/dev/null || true
  rm -f "$raw_log" "${RUN_DIR}/${unit}_tail.pid"

  return "$rc"
}
```

### Règle d'or N°1 (Christophe — 15/07/2026)

**Avant tout run : tuer/éliminer sans demander.**

```bash
cd /Users/christophe/ace777-test-day1
kill -9 $(cat runs/timer.pid 2>/dev/null) 2>/dev/null
./stop_ace777_hard.sh
rm -f runs/timer.pid runs/master.pid runs/alpha.pid runs/beta.pid
rm -f STOP STOP_ALPHA STOP_BETA
rm -rf /tmp/ace777_ram_exchange && mkdir -p /tmp/ace777_ram_exchange
rm -f /tmp/alpha_heartbeat.txt
./scripts/verif_sterilite.sh   # STERILE=OK obligatoire
```

**Ne pas utiliser** `rm -f runs/*.pid` sous zsh (erreur « no matches found » si vide).

---

## 1.2. Code Source et Logique de la Purge Validée (V2.2.1 / V3.1)

### `nuage_purge_totale()` — enveloppe NUAGE (extrait)

```bash
nuage_purge_totale() {
  echo "=== NUAGE PURGE TOTALE — début ==="

  rm -f STOP STOP_ALPHA STOP_BETA

  nuage_pgrep_kill "tail -f.*NUAGE"
  nuage_pgrep_kill "tail -n 0 -F.*NUAGE"
  nuage_pgrep_kill "tail -F.*NUAGE"
  nuage_pgrep_kill "ace777_launch_v85_nuage"
  nuage_pgrep_kill "genesis_manifest"
  nuage_pgrep_kill "bash -s"
  nuage_pgrep_kill "watchdog_ace777"
  nuage_pgrep_kill "launch_test_master_base_v8_6_fortress"
  nuage_pgrep_kill "caffeinate -is.*ace777"
  nuage_pgrep_kill "launch_test_master_base"

  RUN_DIR="${RUN_DIR:-runs}"
  rm -f "$RUN_DIR"/master.pid "$RUN_DIR"/alpha.pid "$RUN_DIR"/beta.pid
  rm -f "$RUN_DIR"/alpha_wrapper.pid "$RUN_DIR"/beta_wrapper.pid
  rm -f "$RUN_DIR"/ALPHA_X13_BURST13_genesis.pid "$RUN_DIR"/ALPHA_X13_BURST13_wrapper.pid
  rm -f "$RUN_DIR"/BETA_X5_genesis.pid "$RUN_DIR"/BETA_X5_wrapper.pid
  rm -f "$RUN_DIR"/timer.pid "$RUN_DIR"/supervisor_v9_v2.pid
  rm -f "$RUN_DIR"/duo_state.json "$RUN_DIR"/duo_session.json "$RUN_DIR"/swarm_telemetry.json
  rm -f "$RUN_DIR"/.NUAGE*.raw.log 2>/dev/null || true

  rm -f /tmp/alpha_heartbeat.txt
  rm -rf /tmp/ace777_ram_exchange 2>/dev/null || true
  mkdir -p /tmp/ace777_ram_exchange

  rm -f /tmp/ace777_launch_v85_nuage_*.sh 2>/dev/null || true

  sleep 1

  _left=""
  _left="$(pgrep -fl "ace777-test-day1|genesis_manifest|bash -s|watchdog_ace777|ace777_launch_v85|launch_test_master" 2>/dev/null | grep -vi ollama || true)"
  if [ -n "$_left" ]; then
    _left="$(echo "$_left" | while IFS= read -r line; do
      pid="${line%% *}"
      case "$(nuage_self_pids | tr '\n' ' ')" in *" $pid "*|"$pid "*) continue ;; esac
      echo "$line"
    done)"
  fi
  if [ -n "$_left" ]; then
    echo "PURGE_WARN: résidus détectés — 2e passe"
    echo "$_left"
    nuage_pgrep_kill "ace777_launch_v85_nuage"
    nuage_pgrep_kill "bash -s"
    nuage_pgrep_kill "watchdog_ace777"
    sleep 1
  else
    echo "PURGE_OK: zéro process ACE777"
  fi

  echo "PURGE_OK: STOP supprimés | pid/genesis/wrapper/raw/RAM/heartbeat nettoyés"
  echo "=== NUAGE PURGE TOTALE — fin ==="
  echo ""
}
```

### `nuage_kill_genesis_tree()` — enveloppe NUAGE (extrait)

```bash
nuage_kill_genesis_tree() {
  local unit="$1"
  local gpf="${RUN_DIR}/${unit}_genesis.pid"
  local wpf="${RUN_DIR}/${unit}_wrapper.pid"
  local gp="" wp=""

  nuage_kill_tail_for_unit "$unit"

  [ -f "$gpf" ] && gp="$(tr -d ' \n\r' <"$gpf" 2>/dev/null || true)"
  [ -f "$wpf" ] && wp="$(tr -d ' \n\r' <"$wpf" 2>/dev/null || true)"

  if [ -n "$gp" ]; then
    pkill -P "$gp" 2>/dev/null || true
    kill -TERM "$gp" 2>/dev/null || true
    sleep 2
    pkill -KILL -P "$gp" 2>/dev/null || true
    kill -KILL "$gp" 2>/dev/null || true
  fi

  if [ -n "$wp" ] && [ "$wp" != "$gp" ]; then
    pkill -P "$wp" 2>/dev/null || true
    kill -TERM "$wp" 2>/dev/null || true
    sleep 1
    pkill -KILL -P "$wp" 2>/dev/null || true
    kill -KILL "$wp" 2>/dev/null || true
  fi

  rm -f "$gpf" "$wpf"
}
```

### `scripts/preflight_total_365j.sh` — INTÉGRAL (V3.1)

```bash
#!/usr/bin/env bash
# ==============================================================================
# ACE777 — PROTOCOLE DE PRÉ-VOL TOTAL INDUSTRIEL (V3.1)
# Objectif : Certification stérile 365j avant lancement de l'essaim NUAGE.
# Zéro écriture sur le modèle champion disque.
# ==============================================================================
set -euo pipefail

_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$_root"

C_N="\033[0m"
C_R="\033[0;31m"
C_G="\033[0;32m"
C_Y="\033[0;33m"
C_C="\033[0;36m"

fail() {
  echo -e "${C_R}FAIL: $1${C_N}" >&2
  exit 1
}

sign_query() {
  printf '%s' "$1" | openssl dgst -sha256 -hmac "$BINANCE_API_SECRET" -binary | xxd -p -c 256
}

echo -e "${C_C}=== INITIALISATION CHECK-UP PREFLIGHT TOTAL V3.1 ===${C_N}"

# 0. Config & champion (lecture seule)
echo -n "0. Audit config & champion... "
if [ ! -f "./config_active.env" ]; then
  fail "config_active.env introuvable"
fi
# shellcheck source=scripts/load_config.sh
source ./scripts/load_config.sh 2>/dev/null || fail "config_active.env illisible"
for f in genesis_manifest.txt radar_gate.rb; do
  [ -f "$_root/$f" ] || fail "fichier manquant: $f"
done
_min_usdt=$(( ${BUY_USDT_BETA:-200} + ${BUY_USDT_ALPHA:-800} ))
echo -e "${C_G}OK (${ACE777_CONFIG_NAME:-?} BETA=${BUY_USDT_BETA:-?} ALPHA=${BUY_USDT_ALPHA:-?} min=${_min_usdt})${C_N}"

# 1. EXTERMINATION DES TIMERS ET ZOMBIES ORPHELINS
echo -n "1. Purge des fantômes Unix... "
if [ -f "runs/timer.pid" ]; then
  _tp="$(tr -d ' \n\r' < runs/timer.pid 2>/dev/null || true)"
  if [ -n "$_tp" ]; then
    kill -9 "$_tp" 2>/dev/null || true
  fi
  rm -f runs/timer.pid
fi

if pgrep -fl 'ace777|NUAGE|genesis_manifest|watchdog_ace777|ace777_launch_v85|launch_vide_froid_4h_binance|tail -n 0 -F runs/|tail -F runs/\.NUAGE|caffeinate -is.*ace777' 2>/dev/null | grep -vi ollama | grep -q .; then
  ./stop_ace777_hard.sh >/dev/null 2>&1 || true
fi

pkill -9 -f "File.write\('STOP_ALPHA'" 2>/dev/null || true
pkill -9 -f 'ace777_launch_v85_nuage' 2>/dev/null || true
pkill -9 -f 'launch_vide_froid_4h_binance_NUAGE' 2>/dev/null || true
pkill -9 -f 'watchdog_ace777' 2>/dev/null || true
pkill -9 -f 'genesis_manifest' 2>/dev/null || true
pkill -9 -f 'tail -n 0 -F runs/' 2>/dev/null || true
pkill -9 -f 'tail -F runs/\.NUAGE' 2>/dev/null || true
pkill -9 -f 'caffeinate -is.*ace777' 2>/dev/null || true

rm -f runs/master.pid runs/alpha.pid runs/beta.pid runs/timer.pid
rm -f runs/*wrapper*.pid runs/*genesis*.pid 2>/dev/null || true
rm -f STOP STOP_ALPHA STOP_BETA
rm -rf /tmp/ace777_ram_exchange
mkdir -p /tmp/ace777_ram_exchange
rm -f /tmp/alpha_heartbeat.txt

if ! ./scripts/verif_sterilite.sh >/dev/null 2>&1; then
  fail "processus ACE777 encore actifs après purge (voir verif_sterilite.sh)"
fi
touch STOP STOP_ALPHA STOP_BETA
echo -e "${C_G}STERILE=OK${C_N}"

# 2. VÉRIFICATION THERMIQUE
echo -n "2. Diagnostic thermique MacBook Air... "
_local_temp="$(sysctl -n machdep.xcpm.cpu_thermal_level 2>/dev/null || echo "0")"
if [ "$_local_temp" -gt 5 ]; then
  echo -e "${C_Y}WARN: CPU sous contrainte thermique (${_local_temp}). Laissez refroidir.${C_N}"
else
  echo -e "${C_G}TEMP_NORMAL=OK (level=${_local_temp})${C_N}"
fi

# 3. AUDIT LIGNE SURF (curl fapi ping — pas ICMP)
echo -n "3. Interrogation ligne Surf (fapi ping)... "
_binance_mode="${BINANCE_MODE:-testnet}"
if [ "$_binance_mode" = "live" ]; then
  _ping_url="${WATCHDOG_PING_URL:-https://fapi.binance.com/fapi/v1/ping}"
else
  _ping_url="${WATCHDOG_PING_URL:-https://testnet.binancefuture.com/fapi/v1/ping}"
fi

_ping_resp=""
_ping_ms=""
for _attempt in 1 2 3; do
  _curl_out="$(curl -sS -o /tmp/ace777_preflight_ping.json -w '%{time_total}' \
    --connect-timeout 2 --max-time 5 "$_ping_url" 2>/dev/null || true)"
  _ping_resp="$(cat /tmp/ace777_preflight_ping.json 2>/dev/null || true)"
  _ping_ms="$(ruby -e 'ms=(Float(ARGV[0]) rescue 0.0)*1000.0; printf("%.0f", ms)' "$_curl_out" 2>/dev/null || echo "?")"
  [ "$_ping_resp" = "{}" ] && break
  sleep 0.3
done
rm -f /tmp/ace777_preflight_ping.json

if [ "$_ping_resp" != "{}" ]; then
  fail "Binance inaccessible (3 tentatives) url=${_ping_url}"
fi
echo -e "${C_G}PING=${_ping_ms}ms OK${C_N}"

# 4. AUDIT COMPTE & WALLET (API signée)
echo -n "4. Connexion API & vérification solde USDT... "
if [ "$_binance_mode" = "live" ]; then
  [ -f "${HOME}/.binance_live.env" ] || fail "~/.binance_live.env manquant (BINANCE_MODE=live)"
  set -a
  # shellcheck source=/dev/null
  source "${HOME}/.binance_live.env"
  set +a
  export BASE_URL="${BASE_URL:-https://fapi.binance.com}"
else
  [ -f "${HOME}/.binance_testnet.env" ] || fail "~/.binance_testnet.env manquant"
  set -a
  # shellcheck source=/dev/null
  source "${HOME}/.binance_testnet.env"
  set +a
  export BASE_URL="${BASE_URL:-https://testnet.binancefuture.com}"
fi

[ -n "${BINANCE_API_KEY:-}" ] || fail "BINANCE_API_KEY manquante"
[ -n "${BINANCE_API_SECRET:-}" ] || fail "BINANCE_API_SECRET manquante"

_ts="$(ruby -e 'puts (Time.now.to_f * 1000).to_i')"
_q="timestamp=${_ts}&recvWindow=60000"
_sig="$(sign_query "$_q")"
_balance_json="$(curl -sS --connect-timeout 5 --max-time 15 \
  -H "X-MBX-APIKEY: ${BINANCE_API_KEY}" \
  "${BASE_URL}/fapi/v2/balance?${_q}&signature=${_sig}" 2>/dev/null || true)"

_solde_usdt="$(ruby -rjson -e '
  begin
    j = JSON.parse(STDIN.read)
    if j.is_a?(Hash) && j["code"]
      print "ERR"
    else
      b = j.find { |x| x["asset"] == "USDT" }
      print((b["availableBalance"] || b["balance"] || "0").to_f.round(2))
    end
  rescue
    print "ERR"
  end
' <<< "$_balance_json" 2>/dev/null || echo "ERR")"

if [ "$_solde_usdt" = "ERR" ] || [ -z "$_solde_usdt" ]; then
  _api_msg="$(ruby -rjson -e 'j=JSON.parse(STDIN.read) rescue {}; puts j["msg"] || j["code"] || "?"' <<< "$_balance_json" 2>/dev/null || echo "?")"
  fail "API balance rejetée (${_api_msg})"
fi

if ruby -e 'exit((Float(ARGV[0]) < Float(ARGV[1])) ? 0 : 1)' "$_solde_usdt" "$_min_usdt" 2>/dev/null; then
  fail "Solde insuffisant (${_solde_usdt} USDT < ${_min_usdt} requis). Risque -2028."
fi
echo -e "${C_G}SOLDE=${_solde_usdt} USDT NOMINAL OK (min=${_min_usdt})${C_N}"

# 5. Certification finale pre-run
echo -n "5. Certification stérilité pre-run... "
if ! ./scripts/verif_sterilite.sh --pre-run >/dev/null 2>&1; then
  fail "verif_sterilite --pre-run NOK"
fi
echo -e "${C_G}CERTIFIED=OK${C_N}"

echo -e "${C_G}=== FEU VERT : LE COCKPIT EST CERTIFIÉ STÉRILE ET PRÊT ===${C_N}"
exit 0
```

### `scripts/verif_sterilite.sh` — INTÉGRAL

```bash
#!/usr/bin/env bash
# Vérification binaire stérilité ACE777/NUAGE — exit 0 = GO | exit 1 = STOP
set -uo pipefail
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

PATTERN='ace777|NUAGE|genesis_manifest|bash -s|watchdog_ace777|ace777_launch_v85|launch_vide_froid_4h_binance|launch_test_master_base_v8_6|tail -n 0 -F runs/|tail -F runs/\.NUAGE|caffeinate -is.*ace777'

_left="$(pgrep -fl "$PATTERN" 2>/dev/null | grep -vi ollama || true)"

if [ -n "$_left" ]; then
  echo "STERILE=NOK"
  echo "$_left"
  exit 1
fi

# Fichiers STOP doivent exister avant un run (pas après purge pré-run)
if [ "${1:-}" = "--pre-run" ]; then
  for f in STOP STOP_ALPHA STOP_BETA; do
    if [ ! -f "$f" ]; then
      echo "STERILE=NOK — manquant: $f (pose STOP avant run)"
      exit 1
    fi
  done
  if [ -f runs/master.pid ]; then
    echo "STERILE=NOK — runs/master.pid existe encore"
    exit 1
  fi
fi

echo "STERILE=OK"
exit 0
```

### Commande prod avec preflight

```bash
cd /Users/christophe/ace777-test-day1 && \
./scripts/preflight_total_365j.sh && \
rm -f STOP STOP_ALPHA STOP_BETA && \
unset ALPHA_RAMP_MODE && \
export RUN_DURATION="04:00:00" && \
export TEST_TAG_OVERRIDE="NUAGE_PROD_4H" && \
/tmp/launch_vide_froid_4h_binance_NUAGE.sh --duration 04:00:00
```

**Mesures preflight typiques (session certifiée):**
- Thermique: `level=0` (TEMP_NORMAL=OK)
- Ping Surf fapi: ~**444 ms** RTT (testnet/live selon config)
- Solde HMAC SHA256: ex. **1785.9 USDT** (variable au moment du check)
- Stérilité: `STERILE=OK` + `CERTIFIED=OK`

---

# [PARTIE 2] — BILAN SÉMANTIQUE ET PARAMÈTRES DU SETUP DE BASE (SHORT/LONG)

**Statut:** ✅ Compilé  
**Réf:** ACE777_SAUVEGARDE_ULTIME_V3.5  
**ADN:** genesis md5 `37fca367`

---

## 2.1. Code d'Usine et Cloisonnement Directionnel

### Exports BETA — SCOUT strictement SHORT x5 (200 USDT)

```bash
launch_beta() {
  (
    trap '' PIPE
    set +o pipefail
    export LOG_FILE="$LOG_BETA"
    export STOP_FILE="STOP_BETA"
    export DUO_STATE_FILE DUO_SESSION_FILE VORTEX_CONTROL_FILE SWARM_TELEMETRY_FILE
    export DUO_V6_BURST_FILE DUO_V63_ALARM_FILE
    export SWARM_COUPLING_ENABLED=TRUE
    export LEVERAGE="${BETA_LEVERAGE_OVERRIDE:-5}"
    export BUY_USDT="${BUY_USDT_BETA:-200}"
    export ENTRY_25_75_INITIAL_FRACTION="${ENTRY_25_75_INITIAL_FRACTION_BETA:-0.70}"
    export FORCE_ENTRY_SIDE="SELL"
    export POSITION_SIDE="SHORT"
    export DUO_MODE="TRUE"
    export DUO_ROLE="SCOUT"
    export V8_RESONANCE_MODE="TRUE"
    export V8_TENSION_MODE="TRUE"
    export VOLATILITY_IMPULSE_THRESHOLD="${MOMENTUM_THRESHOLD:-0.96}"
    export IMPULSE_RESONANCE_WALL_DROP_PCT="6.5"
    export VACUUM_TENSION_THRESHOLD="${VACUUM_TENSION_THRESHOLD_BETA:-0.85}"
    export V8_VOID_LOCK_ENABLED="TRUE"
    export V8_SHOCK_EXIT_ENABLED="TRUE"
    export FLUID_EXIT_ENABLED="TRUE"
    export DUO_GLOBAL_STOP_SESSION_USDT="${GLOBAL_STOP_USDT:--45.00}"
    export DUO_GLOBAL_STOP_HALT_RUN="TRUE"
    export DUO_V63_PHASE_SHIFT_ENABLED="TRUE"
    export DUO_V63_ALARM_BPS="-3"
    run_unit "BETA_X5"
  ) &
  PID_BETA_WRAPPER=$!
  echo "$PID_BETA_WRAPPER" > "${RUN_DIR}/beta_wrapper.pid"
}
```

### Exports ALPHA — HUNTER strictement LONG x13 fixe (800 USDT)

```bash
launch_alpha() {
  NUAGE_ALPHA_BOOT_EPOCH="$(date +%s)"
  date -u +%Y-%m-%dT%H:%M:%SZ > "${ALPHA_HEARTBEAT_FILE}"

  (
    export LOG_FILE="$LOG_ALPHA"
    export STOP_FILE="STOP_ALPHA"
    export DUO_STATE_FILE DUO_SESSION_FILE SWARM_TELEMETRY_FILE
    export DUO_V6_BURST_FILE DUO_V63_ALARM_FILE
    export SWARM_COUPLING_ENABLED=TRUE
    export NUAGE_TENSION_MAX_AGE_MS="${NUAGE_TENSION_MAX_AGE_MS:-800}"
    export ALPHA_HEARTBEAT_FILE="${ALPHA_HEARTBEAT_FILE:-/tmp/alpha_heartbeat.txt}"
    export LEVERAGE="13"
    export LEVERAGE_RAMP_ENABLED="TRUE"
    export LEVERAGE_RAMP_START="13"
    export LEVERAGE_RAMP_END="13"
    export LEVERAGE_RAMP_CYCLES="180"
    export BUY_USDT="${BUY_USDT_ALPHA:-800}"
    export ENTRY_25_75_INITIAL_FRACTION="${ENTRY_25_75_INITIAL_FRACTION_ALPHA:-0.50}"
    export FORCE_ENTRY_SIDE="BUY"
    export POSITION_SIDE="LONG"
    export DUO_MODE="TRUE"
    export DUO_ROLE="HUNTER"
    export DUO_V6_BURST_X13="TRUE"
    export V8_RESONANCE_MODE="TRUE"
    export V8_TENSION_MODE="TRUE"
    export VOLATILITY_IMPULSE_THRESHOLD="${MOMENTUM_THRESHOLD:-0.96}"
    export IMPULSE_RESONANCE_WALL_DROP_PCT="6.5"
    export VACUUM_TENSION_THRESHOLD="${VACUUM_TENSION_THRESHOLD_ALPHA:-0.85}"
    export V8_VOID_LOCK_ENABLED="TRUE"
    export V8_SHOCK_EXIT_ENABLED="TRUE"
    export FLUID_EXIT_ENABLED="TRUE"
    export DUO_GLOBAL_STOP_SESSION_USDT="${GLOBAL_STOP_USDT:--45.00}"
    export DUO_GLOBAL_STOP_HALT_RUN="TRUE"
    export DUO_V63_PHASE_SHIFT_ENABLED="TRUE"
    export RUN_STATE_ENABLED="TRUE"
    export RUN_STATE_LINK_TOTAL_PNL="TRUE"
    run_unit "ALPHA_X13_BURST13"
  ) &
  PID_ALPHA_WRAPPER=$!
  echo "$PID_ALPHA_WRAPPER" > "${RUN_DIR}/alpha_wrapper.pid"
}
```

### Règle mathématique anti-cannibalisation

| Agent | `FORCE_ENTRY_SIDE` | `POSITION_SIDE` | `DUO_ROLE` | Masse × Levier | Effet |
|---|---|---|---|---|---|
| BETA | SELL | SHORT | SCOUT | 200 × x5 | Éclaireur vendeur — publie `duo_state.json` |
| ALPHA | BUY | LONG | HUNTER | 800 × x13 | Chasseur acheteur — lit duo, ne vend jamais en scout |

**Conflit éradiqué:** BETA SHORT + ALPHA LONG → jamais deux ordres même sens sur même jambe hedge.  
ALPHA ne peut pas « manger » la position BETA ; elle **réagit** au signal duo après publication RAM.

**Formule gate:** `allow_revenge ⟺ (status=CLOSED ∧ pnl < 0 ∧ reason ∈ revenge_reasons)`  
**Formule blocage flat:** `pnl = 0 → closed_loss = false → allow = false, reason = no_trigger`

---

## 2.2. La Physique du Transfert d'Énergie (The Shockwave)

### Séquence d'armement

```
1. BETA entre SELL @ tension élevée
2. BETA sort avec pnl < 0 (closed_loss) + reason ∈ revenge_reasons
3. duo_publish_state() → /tmp/ace777_ram_exchange/duo_state.json
4. swarm_broadcast_shockwave() → swarm_telemetry.json
5. ALPHA lit duo_hunter_signal() → mode=revenge, mult=1.5x
6. nuage_cloud_tension_gate() → age duo_state < 800ms
7. ALPHA BUY hunter_revenge au prix de marché post-choc
```

### `nuage_cloud_tension_gate()` — preamble NUAGE

```bash
nuage_cloud_tension_gate() {
  local cycle="$1"
  local max_age="${NUAGE_TENSION_MAX_AGE_MS:-800}"
  local age_ms path
  duo_is_hunter || return 0
  path="${DUO_STATE_FILE:-runs/duo_state.json}"
  age_ms="$(ruby -rjson -e '
    path = ARGV[0]
    begin
      j = JSON.parse(File.read(path))
      ts = (j["ts_ms"].to_i rescue 0)
      age = ((Time.now.to_f * 1000).to_i - ts)
      age = 0 if age < 0
      print(age)
    rescue
      print(999999)
    end
  ' -- "$path" 2>/dev/null || echo 999999)"
  if [ "$age_ms" -gt "$max_age" ]; then
    echo "$(date -u +%FT%TZ),${cycle},SKIP,SKIPPED,,,,,0,tension_stale,reason=nuage_age_ms=${age_ms} thresh=${max_age}" >> "$LOG_FILE"
    sk_lev="$C_C"; num_ge "$current_leverage" "13" && sk_lev="$C_G"; num_le "$current_leverage" "5" && sk_lev="$C_Y"
    echo "${C_C}$(date -u +%H:%M:%S)${C_N} ${sk_lev}x$current_leverage${C_N} ${C_C}#${cycle}${C_N} SKIP ${C_Y}| tension_stale age=${age_ms}ms>${max_age}ms (NUAGE)${C_N}"
    alpha_touch_heartbeat
    return 1
  fi
  return 0
}
```

### `swarm_broadcast_shockwave()` — genesis_manifest.txt

```bash
swarm_broadcast_shockwave() {
  local cycle="$1" reason="$2"
  [ "$SWARM_COUPLING_ENABLED" = "TRUE" ] || return 0
  local key
  key="$(swarm_agent_key)"
  [ "$key" = "solo" ] && return 0
  SWARM_TELEMETRY_FILE="$SWARM_TELEMETRY_FILE" SWARM_SHOCKWAVE_CYCLES="$SWARM_SHOCKWAVE_CYCLES" \
    ruby "./scripts/swarm_telemetry.rb" shockwave \
      --from "$key" --cycle "$cycle" --duration "$SWARM_SHOCKWAVE_CYCLES" 2>/dev/null || true
  echo "${C_Y}SWARM shockwave${C_N} ${C_N}| $key -> neighbor (${reason})${C_N}"
}
```

### `duo_hunter_signal()` — genesis_manifest.txt (INTÉGRAL)

```bash
duo_hunter_signal() {
  duo_is_hunter || {
    echo "allow=true mode=disabled forced=AUTO mult=1.0 reason=duo_off"
    return 0
  }
  ruby -rjson -e '
    path=ARGV[0]
    ttl=(Integer(ARGV[1]) rescue 20)
    suffer_bps=(Float(ARGV[2]) rescue -5.0)
    suffer_usdt=(Float(ARGV[3]) rescue -0.5)
    require_sl=(ARGV[4] == "TRUE")
    revenge_mult=ARGV[5]
    force_opp=(ARGV[6] == "TRUE")
    sens_boost=(ARGV[7] == "TRUE")
    fast_death_sec=(Integer(ARGV[8]) rescue 30)
    boost_mult=(Float(ARGV[9]) rescue 0.5)
    boost_ttl_sec=(Integer(ARGV[10]) rescue 40)
    burst_on=(ARGV[11] == "TRUE")
    burst_mult=ARGV[12]
    burst_min_loss=(Float(ARGV[13]) rescue 15.0)
    burst_min_speed=(Float(ARGV[14]) rescue 0.5)
    burst_cooldown=(Integer(ARGV[15]) rescue 188)
    burst_file=ARGV[16]
    require_true_vacuum=(ARGV[17] == "TRUE")
    begin
      j=JSON.parse(File.read(path))
    rescue
      puts "allow=false mode=none forced=AUTO mult=1.0 reason=no_state boost=1.0 scout_bps=0 scout_hold=0"
      exit 0
    end
    age=((Time.now.to_f*1000).to_i - (j["ts_ms"].to_i rescue 0))
    if age > ttl*1000
      puts "allow=false mode=none forced=AUTO mult=1.0 reason=stale_state boost=1.0 scout_bps=0 scout_hold=0"
      exit 0
    end
    side=j["side"].to_s
    forced="AUTO"
    if force_opp
      forced = (side == "BUY" ? "SELL" : (side == "SELL" ? "BUY" : "AUTO"))
    end
    status=j["status"].to_s
    bps=(Float(j["bps"]) rescue 0.0)
    pnl=(Float(j["pnl_usdt"]) rescue 0.0)
    reason=j["reason"].to_s
    hold_sec=(Integer(j["hold_sec"]) rescue 0)
    suffer = (status == "OPEN") && (bps <= suffer_bps || pnl <= suffer_usdt)
    closed_loss = (status == "CLOSED") && pnl < 0.0
    revenge_reasons = %w[stop_loss shock_inversion_stop shock_exit_10bps fluid_exit_inversion fluid_exit_brake beta_sentinel_cut]
    revenge = closed_loss && (!require_sl || revenge_reasons.include?(reason))
    fast_death = closed_loss && hold_sec > 0 && hold_sec <= fast_death_sec
    speed_bps_s = hold_sec > 0 ? (bps.abs / hold_sec.to_f) : 0.0
    out_mode="none"
    out_mult="1.0"
    out_reason="no_trigger"
    out_allow=false
    out_boost=1.0
    vacuum_strike = (status == "OPEN" && reason == "true_vacuum")
    if require_true_vacuum && !vacuum_strike
      puts "allow=false mode=none forced=AUTO mult=1.0 reason=no_true_vacuum boost=1.0 scout_bps=#{bps} scout_hold=#{hold_sec}"
      exit 0
    end
    if vacuum_strike
      out_allow=true
      out_mode="vacuum_strike"
      out_mult="1.0"
      out_reason=reason
      puts "allow=#{out_allow} mode=#{out_mode} forced=#{forced} mult=#{out_mult} reason=#{out_reason} boost=#{out_boost} scout_bps=#{bps} scout_hold=#{hold_sec}"
      exit 0
    end
    if revenge
      out_allow=true
      out_mode="revenge"
      out_mult=revenge_mult
      out_reason=reason
      if burst_on && bps <= -burst_min_loss && speed_bps_s >= burst_min_speed
        cooldown_ok=true
        begin
          bj=JSON.parse(File.read(burst_file))
          last_ms=(bj["last_burst_ms"].to_i rescue 0)
          now_ms=(Time.now.to_f*1000).to_i
          cooldown_ok = ((now_ms - last_ms) >= burst_cooldown*1000)
        rescue
          cooldown_ok=true
        end
        if cooldown_ok
          out_mode="burst"
          out_mult=burst_mult
          out_reason="burst_x13"
          begin
            File.write(burst_file, JSON.generate({"last_burst_ms"=>(Time.now.to_f*1000).to_i}))
          rescue
          end
        else
          out_reason="cooldown_revenge"
        end
      end
      if sens_boost && fast_death && age <= boost_ttl_sec*1000
        out_boost=boost_mult
      end
    elsif suffer
      out_allow=true
      out_mode="suffer"
      out_mult="1.0"
      out_reason=reason
    end
    puts "allow=#{out_allow} mode=#{out_mode} forced=#{forced} mult=#{out_mult} reason=#{out_reason} boost=#{out_boost} scout_bps=#{bps} scout_hold=#{hold_sec}"
  ' -- "$DUO_STATE_FILE" "$DUO_EVENT_TTL_SEC" "$DUO_SCOUT_SUFFER_BPS" "$DUO_SCOUT_SUFFER_USDT" "$DUO_HUNTER_REQUIRE_STOP_LOSS" "$DUO_HUNTER_REVENGE_MULT" "$DUO_FORCE_OPPOSITE" "$DUO_V6_SENSITIVITY_BOOST" "$DUO_V6_FAST_DEATH_SEC" "$DUO_V6_BOOST_MULT" "$DUO_V6_BOOST_TTL_SEC" "$DUO_V6_BURST_X13" "$DUO_V6_BURST_MULT" "$DUO_V6_BURST_MIN_LOSS_BPS" "$DUO_V6_BURST_MIN_SPEED_BPS_PER_SEC" "$DUO_V6_BURST_COOLDOWN_SEC" "$DUO_V6_BURST_FILE" "$DUO_HUNTER_REQUIRE_TRUE_VACUUM"
}
```

### Trade du 14 juillet 2026 — 12:47 UTC (+32,07 USDT en 7 s)

**LIVE log** (`logs_meches/trade_20260714_1247_LIVE.log`):

```
[ALPHA_X13_BURST13] [1;36m12:47:10[0m [1;32mx13[0m [1;36m#218[0m SKIP tension=[1;31m6.03930286[0m [0m| spread_too_wide [1;33mconf=0.5[0m
[ALPHA_X13_BURST13] [1;36m12:47:10[0m [1;32mx13[0m [1;36m#218[0m SKIP tension=[1;31m6.03930286[0m [0m| spread_too_wide [1;33mconf=0.5[0m
[ALPHA_X13_BURST13] [1;36m12:47:10[0m [1;32mx13[0m [1;36m#218[0m SKIP tension=[1;31m6.03930286[0m [0m| spread_too_wide [1;33mconf=0.5[0m
[BETA_X5] [1;36mentry=12:47:05@63553.30000000[0m [1;33mx5[0m [1;36m#490[0m [1;31mSELL[0m tension=[1;31m6.38500207[0m hold=[1;36m10[0ms sec=[1;36m10[0m [0m| exit=63566.90000000 [1;32mconf=0.9862[0m [1;36mexit_time=12:47:15[0m [1;31mpnl=-0.10472000 bps=-2.13993609 pct=-0.02139936% total=2.0492600000000003[0m
[BETA_X5] [1;36m12:47:24[0m [1;33mx5[0m [1;36m#491[0m SKIP tension=[1;36m0.33455436[0m [0m| wall_not_collapsed
[ALPHA_X13_BURST13] [1;36mentry=12:47:22@63582.60000000[0m [1;32mx13[0m [1;36m#219[0m [1;32mBUY[0m tension=[1;31m7.87418878[0m hold=[1;36m7[0ms sec=[1;36m7[0m [0m| exit=63663.40000000 [1;33mconf=0.6324[0m [1;36mexit_time=12:47:29[0m [1;32mpnl=32.06952000 bps=12.70787920 pct=0.12707879% total=34.11878[0m
```

**CSV BETA (déclencheur):**

```
/Users/christophe/ace777-test-day1/runs/NUAGE_PROD_4H_BETA_X5.csv:2026-07-14T12:47:16Z,490,SELL,FILLED,63553.30000000,63566.90000000,0.00770000,-2.13993609,-0.10472000,shock_inversion_stop,radar=long conf=0.9862 size_note=strong_conf_full+entry_25_75_full soft=1 pct=-0.02139936 tension=6.38500207 bid_drop=0.00049106 ask_drop=41.50251347
/Users/christophe/ace777-test-day1/runs/NUAGE_PROD_4H_BETA_X5.csv:2026-07-14T12:47:24Z,491,SKIP,SKIPPED,,,,,0,impulse_resonance_wait,reason=wall_not_collapsed tension=0.33455436 bid_drop=0.20909809 ask_drop=2.17460332
/Users/christophe/ace777-test-day1/runs/NUAGE_PROD_4H_BETA_X5.csv:2026-07-14T12:47:32Z,492,SKIP,SKIPPED,,,,,0,radar_block,reason=spread_too_wide conf=0.3032 mom_sig=0.36379311 raw_mom_bps=0.00000000 spread_bps=17.22790000 tension=0.36379311 bid_drop=0.08512811 ask_drop=2.36465524 swarm=1
/Users/christophe/ace777-test-day1/runs/NUAGE_PROD_4H_BETA_X5.csv:2026-07-14T12:47:40Z,493,SKIP,SKIPPED,,,,,0,radar_block,reason=spread_too_wide conf=0.0009 mom_sig=0.00106305 raw_mom_bps=0.00000000 spread_bps=30.80390000 tension=0.00106305 bid_drop=0.00690980 ask_drop=0.00000000 swarm=0
/Users/christophe/ace777-test-day1/runs/NUAGE_PROD_4H_BETA_X5.csv:2026-07-14T12:47:47Z,494,SKIP,SKIPPED,,,,,0,radar_block,reason=spread_too_wide conf=0.5 mom_sig=1.00264671 raw_mom_bps=-29.51828734 spread_bps=15.15780000 tension=1.00264671 bid_drop=0.00003553 ask_drop=6.51720359 swarm=0
```

**CSV ALPHA (percussion):**

```
/Users/christophe/ace777-test-day1/runs/NUAGE_PROD_4H_ALPHA_X13_BURST13.csv:2026-07-14T12:47:00Z,217,SKIP,SKIPPED,,,,,0,radar_block,reason=direction_unclear conf=0.0121 mom_sig=0.08388063 raw_mom_bps=0.62943258 spread_bps=1.48020000 tension=0.08388063 bid_drop=0.54522409 ask_drop=0.00000000 swarm=0
/Users/christophe/ace777-test-day1/runs/NUAGE_PROD_4H_ALPHA_X13_BURST13.csv:2026-07-14T12:47:09Z,218,SKIP,SKIPPED,,,,,0,radar_block,reason=spread_too_wide conf=0.5 mom_sig=6.03930286 raw_mom_bps=0.00000000 spread_bps=11.04170000 tension=6.03930286 bid_drop=0.00000000 ask_drop=39.25546858 swarm=1
/Users/christophe/ace777-test-day1/runs/NUAGE_PROD_4H_ALPHA_X13_BURST13.csv:2026-07-14T12:47:29Z,219,BUY,FILLED,63582.60000000,63663.40000000,0.39690000,12.70787920,32.06952000,shock_inversion_stop,radar=long conf=0.6324 size_note=hunter_revenge_1.5x+entry_25_75_full soft=0 pct=0.12707879 tension=7.87418878 bid_drop=0.00000000 ask_drop=51.18222707
/Users/christophe/ace777-test-day1/runs/NUAGE_PROD_4H_ALPHA_X13_BURST13.csv:2026-07-14T12:47:38Z,220,SKIP,SKIPPED,,,,,0,radar_block,reason=direction_unclear conf=0.2383 mom_sig=0.19511999 raw_mom_bps=0.00000000 spread_bps=2.13740000 tension=0.19511999 bid_drop=0.00000000 ask_drop=1.26827996 swarm=0
/Users/christophe/ace777-test-day1/runs/NUAGE_PROD_4H_ALPHA_X13_BURST13.csv:2026-07-14T12:47:46Z,221,SKIP,SKIPPED,,,,,0,radar_block,reason=spread_too_wide conf=0.5 mom_sig=0.92707116 raw_mom_bps=0.00000000 spread_bps=15.37780000 tension=0.92707116 bid_drop=0.00222078 ask_drop=6.02596256 swarm=0
/Users/christophe/ace777-test-day1/runs/NUAGE_PROD_4H_ALPHA_X13_BURST13.csv:2026-07-14T12:47:55Z,222,SKIP,SKIPPED,,,,,0,radar_block,reason=spread_too_wide conf=0.5 mom_sig=1.24979589 raw_mom_bps=0.00000000 spread_bps=29.68630000 tension=1.24979589 bid_drop=0.07786069 ask_drop=8.12367326 swarm=0
```

**Chronologie:** BETA perte 12:47:15 → SWARM shockwave → ALPHA entry 12:47:22 → exit +32,07 12:47:29 (hold 7s, hunter_revenge_1.5x).

---

## 2.3. L'Impact des Sorties à l'Équilibre (Flat pnl=0)

### Condition code (`duo_hunter_signal`)

```ruby
closed_loss = (status == "CLOSED") && pnl < 0.0
revenge = closed_loss && (!require_sl || revenge_reasons.include?(reason))
```

**Si BETA sort flat (pnl=0.0):** `closed_loss = false` → `revenge = false` → `allow=false reason=no_trigger`.

### Observation soir 14/07 (tension 6+ mais duo bloqué)

```
[ALPHA_X13_BURST13] tension=7.15369223 | duo no_trigger
[ALPHA_X13_BURST13] tension=2.10859007 | duo no_trigger
```

**Explication:** la tension locale V8 (mur carnet) ≠ signal duo. ALPHA lit **`duo_state.json`** (état BETA post-trade), pas la tension instantanée. BETA peut afficher tension 6+ en SKIP radar tout en ayant dernier `duo_state` avec `pnl=0` ou sortie flat → **protection capital** : pas de chasse sans « cadavre » scout.

Exemple BETA flat même session (05:21 UTC 15/07):

```
2026-07-15T05:21:11Z,189,SELL,FILLED,64651.80000000,64651.80000000,...,-0.00000000,shock_inversion_stop,...
```

→ ALPHA reste en `duo no_trigger` malgré SWARM si pnl=0.

---

# [PARTIE 3] — JALON HISTORIQUE SOUVERAIN — RUN +29 USDT

**Statut:** ✅ Compilé  
**Réf:** ACE777_SAUVEGARDE_ULTIME_V3.5  

> **Correction date:** jalon certifié = **2026-07-10** (pas juin). Session **204206**, 20:27 UTC.

---

## 3.1. Analyse Forensique du Gain de +29,41 USDT

### Identité session

| Champ | Valeur |
|---|---|
| Session | **204206** |
| Horodatage | **2026-07-10T20:27:00Z → 20:41:52Z** (14 min) |
| Tag CSV | `MASTER_VORTEX_V2_COLLAB_4H` |
| Genesis md5 | **37fca367** (barrière duo OUI, PHI NON) |
| BETA | SCOUT x5 — 200 USDT — 15 FILLED SELL |
| ALPHA | HUNTER x13 fixe — 800 USDT — 14 FILLED BUY |
| PnL certifié | **+29,4095 USDT** (BETA +1,16 / ALPHA +28,25) |
| Meilleur trade ALPHA | **+22,8643 USDT** @ 20:29:56 UTC |

### Chronologie chaîne soir 10/07

| Rapport | PnL | Rôle |
|---------|-----|------|
| 163716 | -0,33 $ | Premier de la chaîne soir |
| 193940 | +13,23 $ | Premier boot x13 identique |
| 202645 | +0,88 $ | Continuation |
| **204206** | **+29,41 $** | **Jalon souverain** |

### Rapport PnL intégral session 204206

# RAPPORT PNL AUTO — MASTER_VORTEX_V2_COLLAB_4H

**Session:** `MASTER_VORTEX_V2_COLLAB_4H`
**Période:** 2026-07-10T20:27:00Z → 2026-07-10T20:41:52Z (0h14m)
**Setup:** `vide_froid_vortex_v2_collab` v`2026-07-10-v2.2.2-no-partner-halt` | BETA `200` USDT | ALPHA `800` USDT | LLM gate `TRUE` fail_closed=`TRUE`
**Généré:** 2026-07-10T20:42:06Z UTC
**Filtre session:** `ts >= 2026-07-10T20:26:47Z` (lignes CSV antérieures exclues)

---

## BILAN GLOBAL

| Métrique | Valeur |
|----------|--------|
| **PNL BETA** | **+1.1616 USDT** |
| **PNL ALPHA** | **+28.2480 USDT** |
| **PNL SESSION TOTAL** | **+29.4095 USDT** |
| Statut | `POSITIF` |

---

## BETA — BETA (SCOUT x5)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 15 |
| Gagnants | 4 |
| Perdants | 10 |
| Flat (0) | 1 |
| Win rate | **26.7%** |
| Gains totaux | +1.5846 USDT |
| Pertes totales | -0.4230 USDT |
| **PNL net** | **+1.1616 USDT** |
| BPS moyen | 2.53 |

**Meilleur trade:** +0.7618 USDT
**Pire trade:** -0.1617 USDT

**Direction:** SELL (15)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| shock_inversion_stop | 9 |
| fluid_exit_inversion | 6 |

**Cycles SKIP:** 36
| Raison | Nb |
|--------|-----|
| radar_block | 32 |
| impulse_resonance_wait | 3 |
| tactic_mismatch | 1 |

---

## ALPHA — ALPHA (HUNTER x13)

| Métrique | Valeur |
|----------|--------|
| Trades FILLED | 14 |
| Gagnants | 12 |
| Perdants | 1 |
| Flat (0) | 1 |
| Win rate | **85.7%** |
| Gains totaux | +29.9640 USDT |
| Pertes totales | -1.7160 USDT |
| **PNL net** | **+28.2480 USDT** |
| BPS moyen | 2.23 |

**Meilleur trade:** +22.8643 USDT
**Pire trade:** -1.7160 USDT

**Direction:** BUY (14)

**Raisons de sortie (exitReason):**
| Raison | Nb |
|--------|-----|
| shock_inversion_stop | 13 |
| fluid_exit_inversion | 1 |

**Cycles SKIP:** 63
| Raison | Nb |
|--------|-----|
| radar_block | 48 |
| impulse_resonance_wait | 9 |
| duo_wait | 5 |
| tactic_mismatch | 1 |

---

## SYNTHÈSE

| Indicateur | BETA | ALPHA | TOTAL |
|------------|------|-------|-------|
| Trades | 15 | 14 | 29 |
| PnL | +1.1616 | +28.2480 | **+29.4095** |
| Win rate | 26.7% | 85.7% | 55.2% |

## CONFIG ACTIVE (snapshot)

- ENTRY_25_75 BETA: `0.70` | ALPHA: `0.50`
- SHOCK_EXIT: `16` bps
- VOLATILITY_FILTER: `16`
- STASE: spread=`16` vol=`16`
- POLL_SEC: `0.064`

---

*Rapport auto — CSV: `MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv` | `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`*
*STATE: `runs/STATE.md`*

### Meilleur trade ALPHA — log CSV d'origine

```
2026-07-10T20:29:05Z,15,SKIP,SKIPPED,,,,,0,radar_block,reason=spread_too_wide conf=0.5 mom_sig=0.96978754 raw_mom_bps=0.00000000 spread_bps=10.20630000 tension=0.96978754 bid_drop=6.30361899 ask_drop=0.00000000 swarm=0
2026-07-10T20:29:14Z,16,SKIP,SKIPPED,,,,,0,radar_block,reason=spread_too_wide conf=0.0002 mom_sig=0.00021429 raw_mom_bps=0.00000000 spread_bps=11.11460000 tension=0.00021429 bid_drop=0.00000000 ask_drop=0.00139289 swarm=0
2026-07-10T20:29:22Z,17,SKIP,SKIPPED,,,,,0,radar_block,reason=spread_too_wide conf=0.0003 mom_sig=0.00040318 raw_mom_bps=-10.20633734 spread_bps=10.36080000 tension=0.00040318 bid_drop=0.00000000 ask_drop=0.00262070 swarm=0
2026-07-10T20:29:31Z,18,SKIP,SKIPPED,,,,,0,radar_block,reason=spread_too_wide conf=0.0 mom_sig=0.00000760 raw_mom_bps=0.00000000 spread_bps=10.59610000 tension=0.00000760 bid_drop=0.00000000 ask_drop=0.00004940 swarm=0
2026-07-10T20:29:56Z,19,BUY,FILLED,63718.80000000,63858.90000000,0.16320000,21.98723140,22.86432000,shock_inversion_stop,radar=short conf=0.719 size_note=strong_conf_full+entry_25_75_full soft=0 pct=0.21987231 tension=2.31057925 bid_drop=15.01876511 ask_drop=0.00000000
```

**Paramètres carnet au moment de la frappe (extrait CSV):**
- Entry: **63718.80** → Exit: **63858.90** (+140.10 $ BTC, ~22 bps)
- Tension: **2.31** | conf radar: **0.719** | size: strong_conf_full
- Exit: `shock_inversion_stop` | hold ~cycle court post-revenge BETA

### Alignement couple asynchrone (preuve logique)

1. BETA publie pertes `shock_inversion_stop` (9×) → `duo_state.json` + SWARM
2. ALPHA lit `duo_hunter_signal mode=revenge` → 14 BUY FILLED
3. Win rate ALPHA **85,7%** vs BETA **26,7%** = transfert d'énergie scout→hunter
4. 5 cycles ALPHA `duo_wait` = gate barrière / fraîcheur duo (pas cannibalisation)
5. Meilleur trade **+22,86 USDT** = choc directionnel majeur capturé par HUNTER x13

### Restauration setup identique 204206

```bash
cd /Users/christophe/ace777-test-day1
./LANCER_IDENTIQUE_204206.sh        # vérif
./LANCER_IDENTIQUE_204206.sh lancer # run (utilisateur seul)
```

---

# [PARTIE 4] — EXPLICATIONS THÉORIQUES DES PHÉNOMÈNES DE MARCHÉ (HORS CONFIG)

**Statut:** ✅ Compilé  
**Réf:** ACE777_SAUVEGARDE_ULTIME_V3.5  

---

## 4.1. Le Principe du Temps de Réponse (Tuning Concept)

L'éclaireur BETA cycle ~8–12 s ; le chasseur ALPHA ~8–15 s avec gate NUAGE **800 ms** sur `duo_state.ts_ms`. Le décalage stroboscopique vise **~2 s** entre publication tension BETA et frappe ALPHA.

**Tension ≠ trigger:** ALPHA lit l'état duo post-trade (RAM), pas la tension V8 instantanée. Un tuning efficace ne synchronise pas les numéros de cycle mais la **fraîcheur RAM** (`age_ms < 800`).

Si BETA freeze (pause pacing) ou meurt (SIGTERM), `duo_state` vieillit → `tension_stale` / `stale_state` → ALPHA dormante. Le watchdog sémantique relance ALPHA mais **ts_ms BETA reste la vérité**.

**Écart de sensibilité:** BETA réagit aux micro-mouvements en scout (levier x5, hold court). ALPHA en hunter x13 a une fenêtre d'entrée plus étroite : elle doit arriver dans les 800 ms post-publication du cadavre scout, sinon le choc s'est dissipé.

---

## 4.2. Le Phénomène de Hachage Microstructurel (Whipsaw ~4$ — 15/07 05:25)

**Observation matin 15/07 ~05:25 UTC:**

```
BETA #189: SELL flat pnl=0.00000000 @ 64651.80 (05:21:11)
BETA #190: SELL perte -0.00760000 @ 64654.80→64655.80 (05:21:33)
ALPHA #94: BUY hunter_revenge perte -0.96480000 @ 64655.80→64651.80 (05:25:14, hold ~7s)
```

Amplitude BTC ~**4 $** — micro-oscillation symétrique.

**Théorie (aucun code):**

1. **Détection adversaire < 10 ms:** les makers HFT testnet/mainnet détectent la signature répétitive (levier × masse × hold 6–7 s × hunter_revenge_1.5x) quasi instantanément.

2. **Transit Surf 400–600 ms:** la ligne fapi (ping preflight ~444 ms typique) ajoute un RTT aller-retour. ALPHA entre **après** que le carnet ait inversé la microstructure locale.

3. **Whipsaw symétrique:** BETA vend sur choc → carnet absorbe → prix remonte légèrement → ALPHA achète au sommet local → prix retombe de ~4$ → sortie `shock_inversion_stop` en perte.

4. **Conséquence systémique:** le coupling logique (revenge valide) peut produire un PnL négatif sur micro-amplitude quand la latence Surf dépasse la fenêtre de cohérence du carnet.

---

## 4.3. Le Concept de Double Standard (Principe de Retournement)

En phase **baissière lourde**, le setup canonique SHORT/LONG peut sous-performer :
- BETA SHORT grattte les rebonds techniques
- ALPHA LONG chasse contre la tendance dominante → drawdowns cumulés

**Concept inverse (non implémenté dans 37fca367):**

| Rôle | Setup canonique | Double standard |
|---|---|---|
| BETA (scout) | SHORT / SELL | **LONG / BUY** |
| ALPHA (hunter) | LONG / BUY | **SHORT / SELL** |

L'inversion adapterait les rôles à la dérive baissière : l'éclaireur achète les squeezes, le chasseur vend les rechutes post-perte scout.

**Statut:** documenté pour recherche future — le champion actuel force `FORCE_ENTRY_SIDE=SELL` (BETA) et `BUY` (ALPHA) dans l'enveloppe NUAGE.

---

# [PARTIE 5] — ARCHITECTURE DE MÉMOIRE LOCALE (OBSIDIAN)

**Statut:** ✅ Compilé  
**Réf:** ACE777_SAUVEGARDE_ULTIME_V3.5  

---

## 5.1. Structuration du Coffre-Fort de Fichiers Markdown (.md)

### Principe

Tout artefact ACE777 est stocké en **texte pur UTF-8** (.md, .csv, .sh, .json) — zéro format propriétaire. Compatible MacBook Air M1 offline, grep, Obsidian, Khoj, git.

### Arborescence coffre V3.5 (implémentation)

```
ace777-test-day1/
├── 29$/historique/ACE777_SAUVEGARDE_ULTIME_V3.5/   ← COFFRE ACTIF
│   ├── INDEX.md
│   ├── parties/PARTIE_01..05_*.md
│   ├── scripts/preflight_total_365j.sh
│   ├── scripts/verif_sterilite.sh
│   ├── snapshots/launch_vide_froid_4h_binance_NUAGE_V2.2.1.sh
│   ├── genesis/genesis_manifest.txt_ACTIF_37fca367
│   ├── rapports/RAPPORT_PNL_AUTO_20260710_*.md
│   ├── logs_meches/trade_*.log|csv|txt
│   └── conversation/README.md → liens transcripts
├── runs/
│   ├── NUAGE_PROD_4H_*.csv              ← fills bruts prod
│   ├── NUAGE_PROD_4H_LIVE_COLOR.log      ← duo intercalé terminal
│   └── RAPPORT_PNL_AUTO_*.md             ← bilans auto post-run
├── master_base/pnl/                      ← archive rapports datés
└── genesis_manifest.txt                  ← CHAMPION INTACT md5 37fca367
```

### Standards de nommage

| Type | Pattern | Exemple |
|---|---|---|
| Rapport PnL | `RAPPORT_PNL_AUTO_YYYYMMDD_HHMMSS.md` | `RAPPORT_PNL_AUTO_20260710_204206.md` |
| CSV fills | `{TAG}_{UNIT}.csv` | `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv` |
| LIVE intercalé | `{TAG}_LIVE_COLOR.log` | `NUAGE_PROD_4H_LIVE_COLOR.log` |
| Snapshot moteur | `genesis_manifest.txt_{LABEL}_{md5prefix}` | `genesis_manifest.txt_ACTIF_37fca367` |
| Trade clé | `trade_YYYYMMDD_HHMM_desc.*` | `trade_20260714_1247_LIVE.log` |

### Bilans sessions NUAGE_PROD_4H certifiés (14–15/07/2026)

| Session | UTC | Durée | BETA | ALPHA | Total |
|---|---|---|---|---|---|
| Matin champion | 11:26→~15:00 | ~3h | -0,25 | +35,49 | **~+35,24** |
| Soir #1 | 20:50→22:04 | 1h14 | +0,57 | +1,39 | **+1,95** |
| Nuit #2 (timer OK) | 22:22→02:22 | **4h00** | -2,44 | +9,95 | **+7,51** |
| Matin 15/07 | 04:49→05:25 | 36m | +0,35 | -0,96 | **-0,61** (Ctrl+C) |

---

## 5.2. Indexation Vectorielle (Khoj & Smart Connections sur GitHub)

### Fonctionnement technique

1. **Corpus indexé:** tous les `.md` du coffre + en-têtes CSV + rapports PnL + transcripts conversation
2. **Embeddings locaux:** modèle sentence-transformers exécuté en batch (pas pendant run trading)
3. **Charge CPU:** **0% constante** en run — indexation nocturne ou post-session uniquement
4. **Smart Connections (Obsidian):** graphe de liens entre concepts (`duo_hunter_signal`, `NUAGE gate 800ms`, `204206`, etc.)

### Requêtes types (retrieval instantané)

| Question naturelle | Fichier retrouvé |
|---|---|
| « bilan session nuit 22:22 timer » | `RAPPORT_PNL_AUTO_20260714_221939.md` |
| « trade +32 juillet 12h47 » | `logs_meches/trade_20260714_1247_*` |
| « jalon +29 dollars » | `rapports/RAPPORT_PNL_AUTO_20260710_204206.md` |
| « preflight ping solde » | `scripts/preflight_total_365j.sh` |
| « zombies tail pid » | `snapshots/launch_vide_froid_4h_binance_NUAGE_V2.2.1.sh` |

### Workflow assistant + coffre

```
User question → Khoj embedding search → top-3 chunks .md
           → Agent lit fichier source intégral (pas résumé)
           → Réponse citant path + ligne
```

### GitHub = remote coffre

- Push du dossier `29$/historique/` = backup off-machine
- Obsidian = vue humaine locale (graph, backlinks)
- Khoj = retrieval agent (semantic search)

### Assemblage monolithe final

```bash
cd "/Users/christophe/ace777-test-day1/29$/historique/ACE777_SAUVEGARDE_ULTIME_V3.5"
{
  echo "# ACE777 — MANIFESTE DE SAUVEGARDE ULTIME V3.5 (MONOLITHIQUE)"
  echo "**Assemblé:** $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo ""
  cat parties/PARTIE_01_STERILITE.md
  echo ""
  cat parties/PARTIE_02_SEMANTIQUE.md
  echo ""
  cat parties/PARTIE_03_JALON_29USD.md
  echo ""
  cat parties/PARTIE_04_THEORIE.md
  echo ""
  cat parties/PARTIE_05_OBSIDIAN.md
  echo ""
  echo "---"
  echo "## ANNEXE — Enveloppe NUAGE V2.2.1 INTÉGRALE"
  echo '```bash'
  cat snapshots/launch_vide_froid_4h_binance_NUAGE_V2.2.1.sh
  echo '```'
} > ../ACE777_SAUVEGARDE_ULTIME_V3.5.md
```

---

## ANNEXE — Enveloppe NUAGE V2.2.1 INTÉGRALE (663 lignes)
```bash
#!/usr/bin/env bash
# === ESSAIM NUAGE V2.2 — Stroboscope + kill tail/genesis ===
# Enveloppe éphémère /tmp — champion disque INTACT
# Réf: NUAGE_V2.1_STROBOSCOPE_ROBUSTE

set -euo pipefail

ACE777_ROOT="${ACE777_ROOT:-/Users/christophe/ace777-test-day1}"
cd "$ACE777_ROOT"

# ═══ PURGE TOTALE AUTOMATIQUE — à CHAQUE départ (obligatoire) ═══
# NE PAS appeler stop_ace777_hard ici : il tue launch_vide_froid (auto-suicide).
nuage_self_pids() {
  local p="$$" pp=""
  while [ -n "$p" ] && [ "$p" -gt 1 ]; do
    echo "$p"
    pp="$(ps -p "$p" -o ppid= 2>/dev/null | tr -d ' ' || true)"
    [ -z "$pp" ] || [ "$pp" = "$p" ] && break
    p="$pp"
  done
}

nuage_pgrep_kill() {
  local pattern="$1"
  local keep pid args
  keep="$(nuage_self_pids | tr '\n' '|' | sed 's/|$//')"
  while IFS= read -r line; do
    [ -z "$line" ] && continue
    pid="${line%% *}"
    args="${line#* }"
    case "|${keep}|" in *"|${pid}|"*) continue ;; esac
    case "$args" in *launch_vide_froid_4h_binance_NUAGE*) continue ;; esac
    kill -9 "$pid" 2>/dev/null || true
  done < <(pgrep -fl "$pattern" 2>/dev/null || true)
}

nuage_purge_totale() {
  echo "=== NUAGE PURGE TOTALE — début ==="

  rm -f STOP STOP_ALPHA STOP_BETA

  nuage_pgrep_kill "tail -f.*NUAGE"
  nuage_pgrep_kill "tail -n 0 -F.*NUAGE"
  nuage_pgrep_kill "tail -F.*NUAGE"
  nuage_pgrep_kill "ace777_launch_v85_nuage"
  nuage_pgrep_kill "genesis_manifest"
  nuage_pgrep_kill "bash -s"
  nuage_pgrep_kill "watchdog_ace777"
  nuage_pgrep_kill "launch_test_master_base_v8_6_fortress"
  nuage_pgrep_kill "caffeinate -is.*ace777"
  nuage_pgrep_kill "launch_test_master_base"

  RUN_DIR="${RUN_DIR:-runs}"
  rm -f "$RUN_DIR"/master.pid "$RUN_DIR"/alpha.pid "$RUN_DIR"/beta.pid
  rm -f "$RUN_DIR"/alpha_wrapper.pid "$RUN_DIR"/beta_wrapper.pid
  rm -f "$RUN_DIR"/ALPHA_X13_BURST13_genesis.pid "$RUN_DIR"/ALPHA_X13_BURST13_wrapper.pid
  rm -f "$RUN_DIR"/BETA_X5_genesis.pid "$RUN_DIR"/BETA_X5_wrapper.pid
  rm -f "$RUN_DIR"/timer.pid "$RUN_DIR"/supervisor_v9_v2.pid
  rm -f "$RUN_DIR"/duo_state.json "$RUN_DIR"/duo_session.json "$RUN_DIR"/swarm_telemetry.json
  rm -f "$RUN_DIR"/.NUAGE*.raw.log 2>/dev/null || true

  rm -f /tmp/alpha_heartbeat.txt
  rm -rf /tmp/ace777_ram_exchange 2>/dev/null || true
  mkdir -p /tmp/ace777_ram_exchange

  rm -f /tmp/ace777_launch_v85_nuage_*.sh 2>/dev/null || true

  sleep 1

  _left=""
  _left="$(pgrep -fl "ace777-test-day1|genesis_manifest|bash -s|watchdog_ace777|ace777_launch_v85|launch_test_master" 2>/dev/null | grep -vi ollama || true)"
  if [ -n "$_left" ]; then
    _left="$(echo "$_left" | while IFS= read -r line; do
      pid="${line%% *}"
      case "$(nuage_self_pids | tr '\n' ' ')" in *" $pid "*|"$pid "*) continue ;; esac
      echo "$line"
    done)"
  fi
  if [ -n "$_left" ]; then
    echo "PURGE_WARN: résidus détectés — 2e passe"
    echo "$_left"
    nuage_pgrep_kill "ace777_launch_v85_nuage"
    nuage_pgrep_kill "bash -s"
    nuage_pgrep_kill "watchdog_ace777"
    sleep 1
  else
    echo "PURGE_OK: zéro process ACE777"
  fi

  echo "PURGE_OK: STOP supprimés | pid/genesis/wrapper/raw/RAM/heartbeat nettoyés"
  echo "=== NUAGE PURGE TOTALE — fin ==="
  echo ""
}

nuage_purge_totale

_args=("$@")
set --
# shellcheck source=scripts/load_config.sh
source ./scripts/load_config.sh
set -- "${_args[@]}"

export RUN_DURATION="${RUN_DURATION:-00:15:00}"
export CAFFEINATE_RUN="${CAFFEINATE_RUN:-TRUE}"

while [ "$#" -gt 0 ]; do
  case "$1" in
    --duration)
      shift
      export RUN_DURATION="${1:-00:15:00}"
      ;;
    *)
      echo "Usage: $0 [--duration HH:MM:SS]"
      exit 1
      ;;
  esac
  shift || true
done

export SWARM_COUPLING_ENABLED=TRUE
export SWARM_TELEMETRY_HEARTBEAT_SEC="${SWARM_TELEMETRY_HEARTBEAT_SEC:-2}"
export ACE777_RAM_EXCHANGE="${ACE777_RAM_EXCHANGE:-/tmp/ace777_ram_exchange}"
mkdir -p "${ACE777_RAM_EXCHANGE}"

export DUO_STATE_FILE="${ACE777_RAM_EXCHANGE}/duo_state.json"
export DUO_SESSION_FILE="${ACE777_RAM_EXCHANGE}/duo_session.json"
export SWARM_TELEMETRY_FILE="${ACE777_RAM_EXCHANGE}/swarm_telemetry.json"
export DUO_V6_BURST_FILE="${ACE777_RAM_EXCHANGE}/duo_burst.json"
export DUO_V63_ALARM_FILE="${ACE777_RAM_EXCHANGE}/duo_v63_alarm.json"

export BETA_LEVERAGE_OVERRIDE=5
export NUAGE_TENSION_MAX_AGE_MS="${NUAGE_TENSION_MAX_AGE_MS:-800}"
export TEST_TAG_OVERRIDE="${TEST_TAG_OVERRIDE:-NUAGE_SMOKE_15M}"
export ACE777_NUAGE_MODE=TRUE
export ACE777_NUAGE_VERSION="V2.2.1_NO_SUICIDE"

export ALPHA_HEARTBEAT_FILE="/tmp/alpha_heartbeat.txt"

export NUAGE_WATCHDOG_INTERVAL_SEC="${NUAGE_WATCHDOG_INTERVAL_SEC:-30}"
export NUAGE_WATCHDOG_STALE_SEC="${NUAGE_WATCHDOG_STALE_SEC:-60}"
export NUAGE_WATCHDOG_MAX_RELAUNCH="${NUAGE_WATCHDOG_MAX_RELAUNCH:-5}"
export NUAGE_WATCHDOG_INIT_TIMEOUT_SEC="${NUAGE_WATCHDOG_INIT_TIMEOUT_SEC:-120}"
export NUAGE_WATCHDOG_RELAUNCH_GRACE_SEC="${NUAGE_WATCHDOG_RELAUNCH_GRACE_SEC:-60}"

NUAGE_V85="/tmp/ace777_launch_v85_nuage_$$.sh"
export LAUNCH_V85_SCRIPT="${NUAGE_V85}"
export ACE777_GENESIS_SOURCE="${ACE777_ROOT}/genesis_manifest.txt"

cat > "${NUAGE_V85}" <<'NUAGE_V85_EOF'
#!/usr/bin/env bash
set -euo pipefail

if [ -d /app ]; then
  cd /app
else
  cd "${ACE777_ROOT:-/Users/christophe/ace777-test-day1}"
fi

_binance_mode="${BINANCE_MODE:-testnet}"
if [ "$_binance_mode" = "live" ]; then
  if [ -f "${HOME}/.binance_live.env" ]; then
    set -a
    # shellcheck source=/dev/null
    source "${HOME}/.binance_live.env"
    set +a
    export BASE_URL="${BASE_URL:-https://fapi.binance.com}"
    export BINANCE_ALLOW_MAINNET="${BINANCE_ALLOW_MAINNET:-TRUE}"
    export WATCHDOG_PING_URL="${WATCHDOG_PING_URL:-https://fapi.binance.com/fapi/v1/ping}"
    echo "INFO_CLES: LIVE mainnet depuis ${HOME}/.binance_live.env"
  else
    echo "PREFLIGHT_ERR: BINANCE_MODE=live mais ~/.binance_live.env introuvable" >&2
    exit 1
  fi
elif [ -f "${HOME}/.binance_testnet.env" ]; then
  set -a
  # shellcheck source=/dev/null
  source "${HOME}/.binance_testnet.env"
  set +a
  export BASE_URL="${BASE_URL:-https://testnet.binancefuture.com}"
  export WATCHDOG_PING_URL="${WATCHDOG_PING_URL:-https://testnet.binancefuture.com/fapi/v1/ping}"
  echo "INFO_CLES: testnet depuis ${HOME}/.binance_testnet.env"
fi

RUN_DIR="${RUN_DIR:-runs}"
duration_sec="${RUN_SEC_OVERRIDE:-900}"
tag="${TEST_TAG_OVERRIDE:-NUAGE_SMOKE_15M}"
mkdir -p "$RUN_DIR"

RAM="${ACE777_RAM_EXCHANGE:-/tmp/ace777_ram_exchange}"
mkdir -p "$RAM"
export DUO_STATE_FILE="${DUO_STATE_FILE:-${RAM}/duo_state.json}"
export DUO_SESSION_FILE="${DUO_SESSION_FILE:-${RAM}/duo_session.json}"
export SWARM_TELEMETRY_FILE="${SWARM_TELEMETRY_FILE:-${RAM}/swarm_telemetry.json}"
export DUO_V6_BURST_FILE="${DUO_V6_BURST_FILE:-${RAM}/duo_burst.json}"
export DUO_V63_ALARM_FILE="${DUO_V63_ALARM_FILE:-${RAM}/duo_v63_alarm.json}"
export SWARM_COUPLING_ENABLED=TRUE
export ALPHA_HEARTBEAT_FILE="${ALPHA_HEARTBEAT_FILE:-/tmp/alpha_heartbeat.txt}"
export LOG_BETA="${RUN_DIR}/${tag}_BETA_X5.csv"
export LOG_ALPHA="${RUN_DIR}/${tag}_ALPHA_X13_BURST13.csv"

if [ "${VORTEX_V2_RADAR_PILOT:-FALSE}" = "TRUE" ]; then
  chmod +x ./scripts/stop_supervisor_v9_v2.sh 2>/dev/null || true
  ./scripts/stop_supervisor_v9_v2.sh 2>/dev/null || true
fi

rm -f STOP STOP_ALPHA STOP_BETA
rm -f "$RUN_DIR"/alpha_wrapper.pid "$RUN_DIR"/beta_wrapper.pid "$RUN_DIR"/master.pid
rm -f "$RUN_DIR"/ALPHA_X13_BURST13_genesis.pid "$RUN_DIR"/ALPHA_X13_BURST13_wrapper.pid
rm -f "$RUN_DIR"/BETA_X5_genesis.pid "$RUN_DIR"/BETA_X5_wrapper.pid
rm -f "$DUO_SESSION_FILE" "$DUO_STATE_FILE" "$SWARM_TELEMETRY_FILE"
rm -f "${ALPHA_HEARTBEAT_FILE}"
if [ -f "$RUN_DIR/timer.pid" ]; then
  kill "$(cat "$RUN_DIR/timer.pid")" 2>/dev/null || true
fi
pkill -f "File.write('STOP_ALPHA'" 2>/dev/null || true
rm -f "$RUN_DIR/timer.pid"

./scripts/preflight_ace777.sh

echo $$ > "${RUN_DIR}/master.pid"
echo "NUAGE_V2.1: kill -9 -$$ pour arrêter"

start_utc="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
end_utc="$(ruby -e 'puts (Time.now + ARGV[0].to_i).utc.strftime("%Y-%m-%dT%H:%M:%SZ")' -- "$duration_sec" 2>/dev/null || echo N/A)"
export RUN_START_UTC="$start_utc" RUN_END_UTC="$end_utc"

ruby -rjson -e '
  require "fileutils"
  rd = ENV.fetch("RUN_DIR", "runs")
  FileUtils.mkdir_p(rd)
  meta = {
    "start_utc" => ENV["RUN_START_UTC"],
    "planned_end_utc" => ENV.fetch("RUN_END_UTC", ""),
    "tag" => ENV.fetch("TEST_TAG_OVERRIDE", ""),
    "launcher" => "NUAGE_V2.1_STROBOSCOPE",
    "version" => ENV.fetch("ACE777_NUAGE_VERSION", "V2.1"),
    "swarm" => ENV.fetch("SWARM_COUPLING_ENABLED", "?"),
    "nuage_max_age_ms" => ENV.fetch("NUAGE_TENSION_MAX_AGE_MS", "?"),
    "beta_leverage" => ENV.fetch("BETA_LEVERAGE_OVERRIDE", "5"),
    "ram_exchange" => ENV.fetch("ACE777_RAM_EXCHANGE", "?"),
    "alpha_heartbeat" => ENV.fetch("ALPHA_HEARTBEAT_FILE", "?"),
    "watchdog_stale_sec" => ENV.fetch("NUAGE_WATCHDOG_STALE_SEC", "60"),
    "watchdog_init_timeout_sec" => ENV.fetch("NUAGE_WATCHDOG_INIT_TIMEOUT_SEC", "120"),
    "watchdog_max_relaunch" => ENV.fetch("NUAGE_WATCHDOG_MAX_RELAUNCH", "5"),
    "index_sync" => "DISABLED_THESIS_3"
  }
  File.write(File.join(rd, "#{meta["tag"]}_run_meta.json"), JSON.pretty_generate(meta))
' 2>/dev/null || true

echo "=== ${tag} — ESSAIM NUAGE V2.1 Stroboscope Robuste ==="
echo "Start UTC: $start_utc | End UTC: $end_utc"
echo "SWARM=ON | BETA x${BETA_LEVERAGE_OVERRIDE:-5} | GATE=${NUAGE_TENSION_MAX_AGE_MS:-800}ms"
echo "Heartbeat: ${ALPHA_HEARTBEAT_FILE} | Stale=${NUAGE_WATCHDOG_STALE_SEC:-60}s"
echo "MaxRelaunch=${NUAGE_WATCHDOG_MAX_RELAUNCH:-5} | INDEX SYNC: OFF"

NUAGE_RELAUNCH_COUNT=0
NUAGE_WATCHDOG_GRACE_UNTIL=0
NUAGE_ALPHA_BOOT_EPOCH=0
PID_ALPHA_WRAPPER=0
PID_BETA_WRAPPER=0
PID_SEMANTIC_WATCHDOG=0
PID_WATCHDOG=0
PID_TIMER=0

_linebuf() {
  if command -v stdbuf >/dev/null 2>&1; then
    stdbuf -oL -eL "$@"
  else
    "$@"
  fi
}

nuage_resolve_bash_s_pid() {
  local parent="$1"
  local pid="" gpid="" args="" i=0

  [ -n "$parent" ] || return 1

  while [ "$i" -lt 100 ]; do
    for pid in $(pgrep -P "$parent" 2>/dev/null || true); do
      args="$(ps -p "$pid" -o args= 2>/dev/null || true)"
      case "$args" in
        *"bash -s"*|*"bash -s "*) echo "$pid"; return 0 ;;
      esac
      for gpid in $(pgrep -P "$pid" 2>/dev/null || true); do
        args="$(ps -p "$gpid" -o args= 2>/dev/null || true)"
        case "$args" in
          *"bash -s"*|*"bash -s "*) echo "$gpid"; return 0 ;;
        esac
      done
    done
    sleep 0.1
    i=$((i + 1))
  done

  echo "$parent"
  return 0
}

nuage_kill_tail_for_unit() {
  local unit="$1"
  local raw_log="${RUN_DIR}/.${tag}_${unit}.raw.log"
  local tpf="${RUN_DIR}/${unit}_tail.pid"
  local tp=""

  [ -f "$tpf" ] && tp="$(tr -d ' \n\r' <"$tpf" 2>/dev/null || true)"
  if [ -n "$tp" ]; then
    pkill -P "$tp" 2>/dev/null || true
    kill -TERM "$tp" 2>/dev/null || true
    sleep 0.5
    pkill -KILL -P "$tp" 2>/dev/null || true
    kill -KILL "$tp" 2>/dev/null || true
  fi
  pkill -f "tail -n 0 -F ${raw_log}" 2>/dev/null || true
  pkill -f "tail -F ${raw_log}" 2>/dev/null || true
  rm -f "$tpf"
}

nuage_kill_genesis_tree() {
  local unit="$1"
  local gpf="${RUN_DIR}/${unit}_genesis.pid"
  local wpf="${RUN_DIR}/${unit}_wrapper.pid"
  local gp="" wp=""

  nuage_kill_tail_for_unit "$unit"

  [ -f "$gpf" ] && gp="$(tr -d ' \n\r' <"$gpf" 2>/dev/null || true)"
  [ -f "$wpf" ] && wp="$(tr -d ' \n\r' <"$wpf" 2>/dev/null || true)"

  if [ -n "$gp" ]; then
    pkill -P "$gp" 2>/dev/null || true
    kill -TERM "$gp" 2>/dev/null || true
    sleep 2
    pkill -KILL -P "$gp" 2>/dev/null || true
    kill -KILL "$gp" 2>/dev/null || true
  fi

  if [ -n "$wp" ] && [ "$wp" != "$gp" ]; then
    pkill -P "$wp" 2>/dev/null || true
    kill -TERM "$wp" 2>/dev/null || true
    sleep 1
    pkill -KILL -P "$wp" 2>/dev/null || true
    kill -KILL "$wp" 2>/dev/null || true
  fi

  rm -f "$gpf" "$wpf"
}

cleanup() {
  kill "${PID_WATCHDOG:-}" "${PID_SEMANTIC_WATCHDOG:-}" 2>/dev/null || true
  touch STOP_ALPHA STOP_BETA 2>/dev/null || true
  nuage_kill_genesis_tree "ALPHA_X13_BURST13"
  nuage_kill_genesis_tree "BETA_X5"
  kill "${PID_ALPHA_WRAPPER:-}" "${PID_BETA_WRAPPER:-}" "${PID_TIMER:-}" 2>/dev/null || true
  echo "NUAGE_V2.1 arrêt global."
}
trap cleanup SIGINT SIGTERM

ruby -e "sleep ${duration_sec}; File.write('STOP_ALPHA',''); File.write('STOP_BETA','')" &
PID_TIMER=$!
echo "$PID_TIMER" > "${RUN_DIR}/timer.pid"

chmod +x ./scripts/watchdog_ace777.sh 2>/dev/null || true
./scripts/watchdog_ace777.sh &
PID_WATCHDOG=$!

ace777_stream_genesis() {
  local genesis="${ACE777_GENESIS_SOURCE:-./genesis_manifest.txt}"
  {
    cat <<'NUAGE_PREAMBLE'

NUAGE_TENSION_MAX_AGE_MS="${NUAGE_TENSION_MAX_AGE_MS:-800}"
ALPHA_HEARTBEAT_FILE="${ALPHA_HEARTBEAT_FILE:-/tmp/alpha_heartbeat.txt}"

duo_hunter_phase_barrier() { :; }

alpha_touch_heartbeat() {
  duo_is_hunter || return 0
  date -u +%Y-%m-%dT%H:%M:%SZ > "${ALPHA_HEARTBEAT_FILE}" 2>/dev/null || true
}

nuage_cloud_tension_gate() {
  local cycle="$1"
  local max_age="${NUAGE_TENSION_MAX_AGE_MS:-800}"
  local age_ms path
  duo_is_hunter || return 0
  path="${DUO_STATE_FILE:-runs/duo_state.json}"
  age_ms="$(ruby -rjson -e '
    path = ARGV[0]
    begin
      j = JSON.parse(File.read(path))
      ts = (j["ts_ms"].to_i rescue 0)
      age = ((Time.now.to_f * 1000).to_i - ts)
      age = 0 if age < 0
      print(age)
    rescue
      print(999999)
    end
  ' -- "$path" 2>/dev/null || echo 999999)"
  if [ "$age_ms" -gt "$max_age" ]; then
    echo "$(date -u +%FT%TZ),${cycle},SKIP,SKIPPED,,,,,0,tension_stale,reason=nuage_age_ms=${age_ms} thresh=${max_age}" >> "$LOG_FILE"
    sk_lev="$C_C"; num_ge "$current_leverage" "13" && sk_lev="$C_G"; num_le "$current_leverage" "5" && sk_lev="$C_Y"
    echo "${C_C}$(date -u +%H:%M:%S)${C_N} ${sk_lev}x$current_leverage${C_N} ${C_C}#${cycle}${C_N} SKIP ${C_Y}| tension_stale age=${age_ms}ms>${max_age}ms (NUAGE)${C_N}"
    alpha_touch_heartbeat
    return 1
  fi
  return 0
}

NUAGE_PREAMBLE
    tail -n +85 "$genesis" | awk '
      /^duo_hunter_phase_barrier\(\) \{/ {
        print "duo_hunter_phase_barrier() { :; }"
        skip=1; next
      }
      skip { if (/^\}$/) skip=0; next }
      /^[[:space:]]*duo_hunter_phase_barrier "\$i"/ {
        print "  : # NUAGE bypass barrier (index ignored)"
        next
      }
      /^[[:space:]]*duo_touch_heartbeat$/ && !hb_done {
        print "  duo_touch_heartbeat"
        print "  alpha_touch_heartbeat"
        hb_done=1; next
      }
      /^[[:space:]]*raw_qty="\$\(num_div/ && !gate_done {
        print "  if duo_is_hunter; then"
        print "    nuage_cloud_tension_gate \"$i\" || { alpha_touch_heartbeat; sleep \"$SLEEP_SEC\"; continue; }"
        print "  fi"
        gate_done=1
      }
      { print }
    '
  } | bash -s
}

run_unit() {
  local unit="$1"
  local raw_log="${RUN_DIR}/.${tag}_${unit}.raw.log"
  local live_log="${RUN_DIR}/${tag}_LIVE_COLOR.log"
  local wrapper_pid=0
  local genesis_pid=0
  local tee_pid=0

  : >"$raw_log"

  (
    trap '' PIPE
    _linebuf tail -n 0 -F "$raw_log" 2>/dev/null | while IFS= read -r line || [ -n "$line" ]; do
      [ -z "${line//[[:space:]]/}" ] && continue
      printf '[%s] %s\n' "$unit" "$line" >>"$live_log" 2>/dev/null || true
      printf '[%s] %s\n' "$unit" "$line"
    done
  ) &
  tee_pid=$!
  echo "$tee_pid" >"${RUN_DIR}/${unit}_tail.pid"

  set +e
  _linebuf ace777_stream_genesis >>"$raw_log" 2>&1 &
  wrapper_pid=$!
  genesis_pid="$(nuage_resolve_bash_s_pid "$wrapper_pid")"
  set -e

  echo "$genesis_pid" >"${RUN_DIR}/${unit}_genesis.pid"
  echo "$wrapper_pid" >"${RUN_DIR}/${unit}_wrapper.pid"

  wait "$wrapper_pid" 2>/dev/null || true
  local rc=$?

  nuage_kill_tail_for_unit "$unit"
  kill "$tee_pid" 2>/dev/null || true
  wait "$tee_pid" 2>/dev/null || true
  rm -f "$raw_log" "${RUN_DIR}/${unit}_tail.pid"

  return "$rc"
}

launch_beta() {
  (
    trap '' PIPE
    set +o pipefail
    export LOG_FILE="$LOG_BETA"
    export STOP_FILE="STOP_BETA"
    export DUO_STATE_FILE DUO_SESSION_FILE VORTEX_CONTROL_FILE SWARM_TELEMETRY_FILE
    export DUO_V6_BURST_FILE DUO_V63_ALARM_FILE
    export SWARM_COUPLING_ENABLED=TRUE
    export LEVERAGE="${BETA_LEVERAGE_OVERRIDE:-5}"
    export BUY_USDT="${BUY_USDT_BETA:-200}"
    export ENTRY_25_75_INITIAL_FRACTION="${ENTRY_25_75_INITIAL_FRACTION_BETA:-0.70}"
    export FORCE_ENTRY_SIDE="SELL"
    export POSITION_SIDE="SHORT"
    export DUO_MODE="TRUE"
    export DUO_ROLE="SCOUT"
    export V8_RESONANCE_MODE="TRUE"
    export V8_TENSION_MODE="TRUE"
    export VOLATILITY_IMPULSE_THRESHOLD="${MOMENTUM_THRESHOLD:-0.96}"
    export IMPULSE_RESONANCE_WALL_DROP_PCT="6.5"
    export VACUUM_TENSION_THRESHOLD="${VACUUM_TENSION_THRESHOLD_BETA:-0.85}"
    export V8_VOID_LOCK_ENABLED="TRUE"
    export V8_SHOCK_EXIT_ENABLED="TRUE"
    export FLUID_EXIT_ENABLED="TRUE"
    export DUO_GLOBAL_STOP_SESSION_USDT="${GLOBAL_STOP_USDT:--45.00}"
    export DUO_GLOBAL_STOP_HALT_RUN="TRUE"
    export DUO_V63_PHASE_SHIFT_ENABLED="TRUE"
    export DUO_V63_ALARM_BPS="-3"
    run_unit "BETA_X5"
  ) &
  PID_BETA_WRAPPER=$!
  echo "$PID_BETA_WRAPPER" > "${RUN_DIR}/beta_wrapper.pid"
}

launch_alpha() {
  NUAGE_ALPHA_BOOT_EPOCH="$(date +%s)"
  date -u +%Y-%m-%dT%H:%M:%SZ > "${ALPHA_HEARTBEAT_FILE}"

  (
    export LOG_FILE="$LOG_ALPHA"
    export STOP_FILE="STOP_ALPHA"
    export DUO_STATE_FILE DUO_SESSION_FILE SWARM_TELEMETRY_FILE
    export DUO_V6_BURST_FILE DUO_V63_ALARM_FILE
    export SWARM_COUPLING_ENABLED=TRUE
    export NUAGE_TENSION_MAX_AGE_MS="${NUAGE_TENSION_MAX_AGE_MS:-800}"
    export ALPHA_HEARTBEAT_FILE="${ALPHA_HEARTBEAT_FILE:-/tmp/alpha_heartbeat.txt}"
    export LEVERAGE="13"
    export LEVERAGE_RAMP_ENABLED="TRUE"
    export LEVERAGE_RAMP_START="13"
    export LEVERAGE_RAMP_END="13"
    export LEVERAGE_RAMP_CYCLES="180"
    export BUY_USDT="${BUY_USDT_ALPHA:-800}"
    export ENTRY_25_75_INITIAL_FRACTION="${ENTRY_25_75_INITIAL_FRACTION_ALPHA:-0.50}"
    export FORCE_ENTRY_SIDE="BUY"
    export POSITION_SIDE="LONG"
    export DUO_MODE="TRUE"
    export DUO_ROLE="HUNTER"
    export DUO_V6_BURST_X13="TRUE"
    export V8_RESONANCE_MODE="TRUE"
    export V8_TENSION_MODE="TRUE"
    export VOLATILITY_IMPULSE_THRESHOLD="${MOMENTUM_THRESHOLD:-0.96}"
    export IMPULSE_RESONANCE_WALL_DROP_PCT="6.5"
    export VACUUM_TENSION_THRESHOLD="${VACUUM_TENSION_THRESHOLD_ALPHA:-0.85}"
    export V8_VOID_LOCK_ENABLED="TRUE"
    export V8_SHOCK_EXIT_ENABLED="TRUE"
    export FLUID_EXIT_ENABLED="TRUE"
    export DUO_GLOBAL_STOP_SESSION_USDT="${GLOBAL_STOP_USDT:--45.00}"
    export DUO_GLOBAL_STOP_HALT_RUN="TRUE"
    export DUO_V63_PHASE_SHIFT_ENABLED="TRUE"
    export RUN_STATE_ENABLED="TRUE"
    export RUN_STATE_LINK_TOTAL_PNL="TRUE"
    run_unit "ALPHA_X13_BURST13"
  ) &
  PID_ALPHA_WRAPPER=$!
  echo "$PID_ALPHA_WRAPPER" > "${RUN_DIR}/alpha_wrapper.pid"
}

nuage_semantic_watchdog() {
  local hb="${ALPHA_HEARTBEAT_FILE:-/tmp/alpha_heartbeat.txt}"
  local stale_limit="${NUAGE_WATCHDOG_STALE_SEC:-60}"
  local check_interval="${NUAGE_WATCHDOG_INTERVAL_SEC:-30}"
  local max_relaunch="${NUAGE_WATCHDOG_MAX_RELAUNCH:-5}"
  local init_timeout="${NUAGE_WATCHDOG_INIT_TIMEOUT_SEC:-120}"
  local grace_sec="${NUAGE_WATCHDOG_RELAUNCH_GRACE_SEC:-60}"
  local now age_sec boot_age

  while [ -f "${RUN_DIR}/master.pid" ] && kill -0 "$(cat "${RUN_DIR}/master.pid")" 2>/dev/null; do
    sleep "$check_interval"

    now="$(date +%s)"

    if [ ! -f "$hb" ]; then
      if [ "${NUAGE_ALPHA_BOOT_EPOCH:-0}" -gt 0 ]; then
        boot_age=$((now - NUAGE_ALPHA_BOOT_EPOCH))
        if [ "$boot_age" -gt "$init_timeout" ]; then
          echo "CRITICAL: ALPHA init timeout > ${init_timeout}s. Emergency halt."
          touch STOP_ALPHA STOP_BETA
          break
        fi
      fi
      continue
    fi

    if [ "${NUAGE_WATCHDOG_GRACE_UNTIL:-0}" -gt "$now" ]; then
      continue
    fi

    age_sec="$(ruby -e '
      require "time"
      begin
        t = Time.parse(File.read(ARGV[0]).strip).utc
        puts((Time.now.utc - t).to_i)
      rescue
        puts 999999
      end
    ' "$hb" 2>/dev/null || echo 999999)"

    if [ "$age_sec" -le "$stale_limit" ]; then
      continue
    fi

    NUAGE_RELAUNCH_COUNT=$((NUAGE_RELAUNCH_COUNT + 1))
    echo "WATCHDOG_SEMANTIC: ALPHA stale ${age_sec}s (seuil=${stale_limit}s) — relance #${NUAGE_RELAUNCH_COUNT}/${max_relaunch}"

    if [ "$NUAGE_RELAUNCH_COUNT" -gt "$max_relaunch" ]; then
      echo "WATCHDOG_SEMANTIC: max_relaunch=${max_relaunch} atteint → STOP session"
      touch STOP_ALPHA STOP_BETA
      break
    fi

    nuage_kill_genesis_tree "ALPHA_X13_BURST13"
    kill "${PID_ALPHA_WRAPPER:-}" 2>/dev/null || true
    wait "${PID_ALPHA_WRAPPER:-}" 2>/dev/null || true

    date -u +%Y-%m-%dT%H:%M:%SZ > "${ALPHA_HEARTBEAT_FILE}"
    NUAGE_WATCHDOG_GRACE_UNTIL=$((now + grace_sec))

    launch_alpha
    echo "WATCHDOG_SEMANTIC: ALPHA relancée — grace ${grace_sec}s — ts_ms BETA = vérité"
  done
}

launch_beta
sleep 2
launch_alpha
nuage_semantic_watchdog &
PID_SEMANTIC_WATCHDOG=$!

echo "NUAGE_V2.1 duo en marche."
echo "Logs: ${LOG_BETA} | ${LOG_ALPHA} | LIVE: ${RUN_DIR}/${tag}_LIVE_COLOR.log"
echo "Watchdog sémantique PID=${PID_SEMANTIC_WATCHDOG} → ${ALPHA_HEARTBEAT_FILE}"

wait "$PID_BETA_WRAPPER" 2>/dev/null || true
wait "$PID_ALPHA_WRAPPER" 2>/dev/null || true

kill "${PID_SEMANTIC_WATCHDOG:-}" 2>/dev/null || true
nuage_kill_genesis_tree "BETA_X5"
nuage_kill_genesis_tree "ALPHA_X13_BURST13"
kill "${PID_ALPHA_WRAPPER:-}" "${PID_BETA_WRAPPER:-}" 2>/dev/null || true
pkill -f "tail -n 0 -F ${RUN_DIR}/\.${tag}_" 2>/dev/null || true
pkill -f "tail -F ${RUN_DIR}/\.${tag}_" 2>/dev/null || true
echo "NUAGE_V2.2 mission terminée."
rm -f "${RUN_DIR}/master.pid" "${RUN_DIR}/alpha_wrapper.pid" "${RUN_DIR}/beta_wrapper.pid"
rm -f "${RUN_DIR}/ALPHA_X13_BURST13_genesis.pid" "${RUN_DIR}/ALPHA_X13_BURST13_wrapper.pid"
rm -f "${RUN_DIR}/ALPHA_X13_BURST13_tail.pid"
rm -f "${RUN_DIR}/BETA_X5_genesis.pid" "${RUN_DIR}/BETA_X5_wrapper.pid"
rm -f "${RUN_DIR}/BETA_X5_tail.pid"
NUAGE_V85_EOF

chmod +x "${NUAGE_V85}"

echo ""
echo "=== ESSAIM NUAGE V2.1 — Stroboscope Robuste ==="
echo "Version: ${ACE777_NUAGE_VERSION}"
echo "SWARM=ON | BETA x5 | GATE=${NUAGE_TENSION_MAX_AGE_MS}ms"
echo "Heartbeat: ${ALPHA_HEARTBEAT_FILE}"
echo "Durée: ${RUN_DURATION} | Tag: ${TEST_TAG_OVERRIDE}"
echo "Lanceur V8.5: ${NUAGE_V85}"
echo "Champion disque: NON MODIFIÉ"
echo ""

if [ "${CAFFEINATE_RUN}" = "TRUE" ] && command -v caffeinate >/dev/null 2>&1; then
  exec caffeinate -is env ACE777_ROOT="$ACE777_ROOT" ./launch_test_master_base_v8_6_fortress.sh --duration "${RUN_DURATION}"
else
  exec env ACE777_ROOT="$ACE777_ROOT" ./launch_test_master_base_v8_6_fortress.sh --duration "${RUN_DURATION}"
fi
```

---

## CRITÈRE DE CERTIFICATION ET SCELLÉ BINAIRE

**Réf:** ACE777_SAUVEGARDE_ULTIME_V3.5 — **STATUT: CERTIFIÉ**  
**Date scellement:** 2026-07-15T06:52:00Z  
**Source calcul:** fichiers disque vivants (`scripts/preflight_total_365j.sh`, `snapshots/launch_vide_froid_4h_binance_NUAGE_V2.2.1.sh` L437–476, `genesis_manifest.txt` L1041)

```
SCEAU_1 [COMPTEUR_LIGNES] : 173
SCEAU_2 [MD5_THEORIQUE]  : 7436d4584082c02ac63397dfe0e3b679
SCEAU_3 [VERROU_GENESIS]   :     suffer = (status == "OPEN") && (bps <= suffer_bps || pnl <= suffer_usdt)
```

### Détail SCEAU_2 — bloc `run_unit()` hashé (V2.2_TAIL_KILL intégré)

Fichier: `snapshots/launch_vide_froid_4h_binance_NUAGE_V2.2.1.sh` lignes 437–476.

```bash
run_unit() {
  local unit="$1"
  local raw_log="${RUN_DIR}/.${tag}_${unit}.raw.log"
  local live_log="${RUN_DIR}/${tag}_LIVE_COLOR.log"
  local wrapper_pid=0
  local genesis_pid=0
  local tee_pid=0

  : >"$raw_log"

  (
    trap '' PIPE
    _linebuf tail -n 0 -F "$raw_log" 2>/dev/null | while IFS= read -r line || [ -n "$line" ]; do
      [ -z "${line//[[:space:]]/}" ] && continue
      printf '[%s] %s\n' "$unit" "$line" >>"$live_log" 2>/dev/null || true
      printf '[%s] %s\n' "$unit" "$line"
    done
  ) &
  tee_pid=$!
  echo "$tee_pid" >"${RUN_DIR}/${unit}_tail.pid"

  set +e
  _linebuf ace777_stream_genesis >>"$raw_log" 2>&1 &
  wrapper_pid=$!
  genesis_pid="$(nuage_resolve_bash_s_pid "$wrapper_pid")"
  set -e

  echo "$genesis_pid" >"${RUN_DIR}/${unit}_genesis.pid"
  echo "$wrapper_pid" >"${RUN_DIR}/${unit}_wrapper.pid"

  wait "$wrapper_pid" 2>/dev/null || true
  local rc=$?

  nuage_kill_tail_for_unit "$unit"
  kill "$tee_pid" 2>/dev/null || true
  wait "$tee_pid" 2>/dev/null || true
  rm -f "$raw_log" "${RUN_DIR}/${unit}_tail.pid"

  return "$rc"
}
```

**Commande de re-vérification:**

```bash
wc -l < /Users/christophe/ace777-test-day1/scripts/preflight_total_365j.sh
sed -n '437,476p' /Users/christophe/ace777-test-day1/29$/historique/ACE777_SAUVEGARDE_ULTIME_V3.5/snapshots/launch_vide_froid_4h_binance_NUAGE_V2.2.1.sh | md5
sed -n '1041p' /Users/christophe/ace777-test-day1/genesis_manifest.txt
```

**FIN DU MANIFESTE ACE777_SAUVEGARDE_ULTIME_V3.5 — SCELLÉ**

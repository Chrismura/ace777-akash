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

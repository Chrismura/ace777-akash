#!/usr/bin/env bash
# =============================================================================
# ACE777 — LANCEMENT USINE + PATCHS RÉVERSIBLES (hors genesis)
#
# 1) Restaure snapshot V2.2.1 (INDEX SYNC: OFF) — cksum usine 812033996 22672
# 2) Patch wait-timer: wait "$PID_TIMER" (pas fin précoce wrappers)
# 3) Patch duo PID watchdog: relance BETA et/ou ALPHA si process mort
#      (NUAGE_DUO_PID_WATCHDOG=1 défaut ; =0 pour OFF — voir engle/DUO_PID_WATCHDOG.md)
# 3c) Patch côtés bi-dir (optionnel): BETA+ALPHA AUTO/BOTH, revenge opposite
#      (NUAGE_BIDIR_SIDES=0 défaut = usine SELL/BUY ; =1 pour essai — engle/BIDIR_SIDES.md)
# 3d) STORM_LATCH (optionnel): bypass Mode Écoute si tension haute
#      (NUAGE_STORM_LATCH=0 défaut ; =1 — engle/PLAN_STORM_WICK.md)
# 3d-bis) STORM_SCOUT_HOLD (K3v3): min hold avant shock/fluid — latch à l'entrée
#      (NUAGE_STORM_SCOUT_HOLD=0 ; =1 + NUAGE_STORM_MIN_HOLD_SEC=20)
# 3d-ter) STORM_HUNTER (K2): ALPHA entre sans perte scout (anti duo no_trigger)
#      (NUAGE_STORM_HUNTER=0 ; =1 + TTL/spread — engle/PLAN_STORM_WICK.md)
# 3d-0) FIX set -e post_delta (toujours): évite mort ALPHA sur test faux
# 3e) PROCESS_EXIT / PROCESS_DIE — log raison mort BETA/ALPHA (toujours ON)
#      voir engle/PROCESS_EXIT_LOG.md — champion disque intact
# 3f) MIN_ENTRY_TENSION (optionnel): relève VACUUM scout → moins de micros
#      (NUAGE_MIN_ENTRY_TENSION=0 défaut=0.85 usine ; ex. =2.5 — engle/MIN_ENTRY_TENSION.md)
# 4) A2 IRM lecture seule + B2 Engle adapt log-only
# Champion disque 37fca367 — JAMAIS modifié.
#
# Usage:
#   ./GO_USINE_NUAGE.sh
#   NUAGE_DUO_PID_WATCHDOG=0 ./GO_USINE_NUAGE.sh   # sans garde-fou duo
#   NUAGE_BIDIR_SIDES=1 ./GO_USINE_NUAGE.sh         # côtés dynamiques (A/B)
#   NUAGE_STORM_LATCH=1 ./GO_USINE_NUAGE.sh         # bypass Mode Écoute (A/B mèche)
#   NUAGE_STORM_SCOUT_HOLD=1 ./GO_USINE_NUAGE.sh    # hold min 20s en tempête (K3)
#   NUAGE_STORM_HUNTER=1 ./GO_USINE_NUAGE.sh        # ALPHA percute sans revenge (K2)
#   NUAGE_MIN_ENTRY_TENSION=2.5 ./GO_USINE_NUAGE.sh  # filtre entrée (bps / frais)
#   caffeinate -dims ./GO_USINE_NUAGE.sh
#
# Boot attendu:
#   INDEX SYNC: OFF
#   Watchdog duo PID=… (si duo ON)
#   BIDIR_SIDES=… / STORM_LATCH=… / STORM_HOLD=… / STORM_HUNTER=… / MIN_ENTRY_TENSION=…
#   PROCESS_EXIT/DIE actifs (log mort process)
#   NUAGE_V2.2: attente timer …
# =============================================================================
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

SNAP="$ROOT/29\$/historique/ACE777_SAUVEGARDE_ULTIME_V3.5/snapshots/launch_vide_froid_4h_binance_NUAGE_V2.2.1.sh"
LAUNCHER="/tmp/launch_vide_froid_4h_binance_NUAGE.sh"
EXPECT_CKSUM_USINE="812033996 22672"
EXPECT_MD5_PREFIX="01c38510"   # 20/08 re-scellé S-10 NET+algoOrder V4 (commit 1e318498, 19/08) — voir ENQUETE_SCELLE_CHAMPION_2026-08-20.md
DURATION="${1:-04:00:00}"
TAG="${2:-NUAGE_PROD_4H}"

fail() { echo "FAIL: $*" >&2; exit 1; }

export NUAGE_DUO_PID_WATCHDOG="${NUAGE_DUO_PID_WATCHDOG:-1}"
export NUAGE_BIDIR_SIDES="${NUAGE_BIDIR_SIDES:-0}"
export NUAGE_STORM_LATCH="${NUAGE_STORM_LATCH:-0}"
export NUAGE_STORM_TENSION="${NUAGE_STORM_TENSION:-2.5}"
export NUAGE_STORM_SCOUT_HOLD="${NUAGE_STORM_SCOUT_HOLD:-0}"
export NUAGE_STORM_MIN_HOLD_SEC="${NUAGE_STORM_MIN_HOLD_SEC:-20}"
export NUAGE_STORM_HUNTER="${NUAGE_STORM_HUNTER:-0}"
export NUAGE_STORM_TTL_SEC="${NUAGE_STORM_TTL_SEC:-20}"
export NUAGE_STORM_MAX_SPREAD_BPS="${NUAGE_STORM_MAX_SPREAD_BPS:-14}"
export NUAGE_MIN_ENTRY_TENSION="${NUAGE_MIN_ENTRY_TENSION:-0}"

# 3f) Filtre entrée : relève vacuum BETA (et ALPHA aligné) via env déjà lu par usine
#     Défaut 0 = usine 0.85. Ex. 2.5 → skip tension froide (moins de micros < frais).
if [ -n "${NUAGE_MIN_ENTRY_TENSION}" ] && [ "${NUAGE_MIN_ENTRY_TENSION}" != "0" ] && [ "${NUAGE_MIN_ENTRY_TENSION}" != "off" ]; then
  export VACUUM_TENSION_THRESHOLD_BETA="${VACUUM_TENSION_THRESHOLD_BETA:-$NUAGE_MIN_ENTRY_TENSION}"
  export VACUUM_TENSION_THRESHOLD_ALPHA="${VACUUM_TENSION_THRESHOLD_ALPHA:-$NUAGE_MIN_ENTRY_TENSION}"
  echo "MIN_ENTRY_TENSION: ON → VACUUM BETA/ALPHA=${VACUUM_TENSION_THRESHOLD_BETA} (usine était 0.85)"
else
  echo "MIN_ENTRY_TENSION: OFF — vacuum usine 0.85"
fi

echo "=== GO_USINE_NUAGE — usine + wait-timer + duo PID=${NUAGE_DUO_PID_WATCHDOG} + BIDIR=${NUAGE_BIDIR_SIDES} + STORM_LATCH=${NUAGE_STORM_LATCH} + STORM_HOLD=${NUAGE_STORM_SCOUT_HOLD} + STORM_HUNTER=${NUAGE_STORM_HUNTER} + MIN_ENTRY=${NUAGE_MIN_ENTRY_TENSION} ==="
echo "ROOT=$ROOT DURATION=$DURATION TAG=$TAG"

case "$DURATION" in
  *720*|*168:*) fail "durée type mois/720h refusée — blocs 4h/8h seulement." ;;
esac

# 1) Champion
[ -e "$ROOT/genesis_manifest.txt" ] || fail "genesis_manifest.txt manquant"
_md5="$(md5 -q "$ROOT/genesis_manifest.txt")"
echo "genesis md5=$_md5"
[[ "$_md5" == "$EXPECT_MD5_PREFIX"* ]] || fail "champion ≠ $EXPECT_MD5_PREFIX…"

# 2) Snapshot usine
[ -f "$SNAP" ] || fail "snapshot manquant: $SNAP"
_ck="$(cksum "$SNAP" | awk '{print $1" "$2}')"
echo "snapshot usine cksum=$_ck"
[ "$_ck" = "$EXPECT_CKSUM_USINE" ] || fail "snapshot ≠ usine $EXPECT_CKSUM_USINE"

# 3) Copier usine → /tmp puis patch wait-timer UNIQUEMENT
cp -f "$SNAP" "$LAUNCHER"
chmod +x "$LAUNCHER"

python3 - "$LAUNCHER" <<'PY'
import pathlib, sys
path = pathlib.Path(sys.argv[1])
text = path.read_text()
old = """echo \"NUAGE_V2.1 duo en marche.\"
echo \"Logs: ${LOG_BETA} | ${LOG_ALPHA} | LIVE: ${RUN_DIR}/${tag}_LIVE_COLOR.log\"
echo \"Watchdog sémantique PID=${PID_SEMANTIC_WATCHDOG} → ${ALPHA_HEARTBEAT_FILE}\"

wait \"$PID_BETA_WRAPPER\" 2>/dev/null || true
wait \"$PID_ALPHA_WRAPPER\" 2>/dev/null || true

kill \"${PID_SEMANTIC_WATCHDOG:-}\" 2>/dev/null || true
nuage_kill_genesis_tree \"BETA_X5\"
nuage_kill_genesis_tree \"ALPHA_X13_BURST13\"
kill \"${PID_ALPHA_WRAPPER:-}\" \"${PID_BETA_WRAPPER:-}\" 2>/dev/null || true
pkill -f \"tail -n 0 -F ${RUN_DIR}/\\.${tag}_\" 2>/dev/null || true
pkill -f \"tail -F ${RUN_DIR}/\\.${tag}_\" 2>/dev/null || true
echo \"NUAGE_V2.2 mission terminée.\"
rm -f \"${RUN_DIR}/master.pid\" \"${RUN_DIR}/alpha_wrapper.pid\" \"${RUN_DIR}/beta_wrapper.pid\"
rm -f \"${RUN_DIR}/ALPHA_X13_BURST13_genesis.pid\" \"${RUN_DIR}/ALPHA_X13_BURST13_wrapper.pid\"
rm -f \"${RUN_DIR}/ALPHA_X13_BURST13_tail.pid\"
rm -f \"${RUN_DIR}/BETA_X5_genesis.pid\" \"${RUN_DIR}/BETA_X5_wrapper.pid\"
rm -f \"${RUN_DIR}/BETA_X5_tail.pid\"
"""
new = """echo \"NUAGE_V2.1 duo en marche.\"
echo \"Logs: ${LOG_BETA} | ${LOG_ALPHA} | LIVE: ${RUN_DIR}/${tag}_LIVE_COLOR.log\"
echo \"Watchdog sémantique PID=${PID_SEMANTIC_WATCHDOG} → ${ALPHA_HEARTBEAT_FILE}\"

# Attendre le TIMER (durée nominale), pas la mort d'un wrapper.
# Sinon: après relance ALPHA, wait ALPHA est déjà mort → dès que BETA sort
# le master affiche \"mission terminée\" au bout d'1h au lieu de 4h.
echo \"NUAGE_V2.2: attente timer ${duration_sec}s (pid=${PID_TIMER}) — pas de fin précoce wrapper\"
wait \"$PID_TIMER\" 2>/dev/null || true
# Si STOP déjà posés sans raison (manuel / externe) → tracer
if [ ! -f runs/STOP_REASON.txt ]; then
  echo \"\$(date -u +%Y-%m-%dT%H:%M:%SZ) reason=stop_present_or_post_timer_touch note=unknown_writer\" > runs/STOP_REASON.txt
fi
touch STOP_ALPHA STOP_BETA 2>/dev/null || true
sleep 2
# Hygiène #3 — toujours une ligne WHY après arrêt
STATE_TAG=\"\${tag}\" ./scripts/rapport_erreurs_session.sh >/dev/null 2>&1 || true
if [ -f runs/LAST_STOP_REASON.txt ]; then
  echo \"WHY_ARRET: \$(cat runs/LAST_STOP_REASON.txt)\"
fi

kill \"${PID_SEMANTIC_WATCHDOG:-}\" \"${PID_WATCHDOG:-}\" \"${PID_DUO_PID_WATCHDOG:-}\" 2>/dev/null || true
nuage_kill_genesis_tree \"BETA_X5\"
nuage_kill_genesis_tree \"ALPHA_X13_BURST13\"
# PIDs disque = vérité (relances watchdog)
[ -f \"${RUN_DIR}/alpha_wrapper.pid\" ] && kill \"$(tr -d ' \\n\\r' <\"${RUN_DIR}/alpha_wrapper.pid\")\" 2>/dev/null || true
[ -f \"${RUN_DIR}/beta_wrapper.pid\" ] && kill \"$(tr -d ' \\n\\r' <\"${RUN_DIR}/beta_wrapper.pid\")\" 2>/dev/null || true
kill \"${PID_ALPHA_WRAPPER:-}\" \"${PID_BETA_WRAPPER:-}\" 2>/dev/null || true
pkill -f \"tail -n 0 -F ${RUN_DIR}/\\.${tag}_\" 2>/dev/null || true
pkill -f \"tail -F ${RUN_DIR}/\\.${tag}_\" 2>/dev/null || true
echo \"NUAGE_V2.2 mission terminée.\"
rm -f \"${RUN_DIR}/master.pid\" \"${RUN_DIR}/alpha_wrapper.pid\" \"${RUN_DIR}/beta_wrapper.pid\" \"${RUN_DIR}/timer.pid\"
rm -f \"${RUN_DIR}/ALPHA_X13_BURST13_genesis.pid\" \"${RUN_DIR}/ALPHA_X13_BURST13_wrapper.pid\"
rm -f \"${RUN_DIR}/ALPHA_X13_BURST13_tail.pid\"
rm -f \"${RUN_DIR}/BETA_X5_genesis.pid\" \"${RUN_DIR}/BETA_X5_wrapper.pid\"
rm -f \"${RUN_DIR}/BETA_X5_tail.pid\"
"""
if old not in text:
    sys.exit("FAIL: bloc wait wrappers introuvable dans le snapshot (patch non appliqué)")
if text.count(old) != 1:
    sys.exit("FAIL: occurrences wait wrappers ≠ 1")
path.write_text(text.replace(old, new, 1))
print("patch wait-timer: OK (1 bloc remplacé)")
PY

# 3a-0) STOP_REASON — timer ruby écrit pourquoi les STOP sont posés (hygiène E18)
python3 - "$LAUNCHER" <<'PY'
import pathlib, sys
path = pathlib.Path(sys.argv[1])
text = path.read_text()
old = '''ruby -e "sleep ${duration_sec}; File.write('STOP_ALPHA',''); File.write('STOP_BETA','')" &'''
new = '''ruby -e "sleep ${duration_sec}; File.write('runs/STOP_REASON.txt', %(#{Time.now.utc.strftime('%Y-%m-%dT%H:%M:%SZ')} reason=timer_nominal duration_sec=${duration_sec}\\n)); File.write('STOP_ALPHA',''); File.write('STOP_BETA','')" &'''
if "reason=timer_nominal" in text:
    print("patch STOP_REASON timer: already present")
elif old not in text:
    sys.exit("FAIL: ligne timer ruby STOP introuvable (STOP_REASON)")
else:
    if text.count(old) != 1:
        sys.exit("FAIL: occurrences timer ruby ≠ 1 (STOP_REASON)")
    path.write_text(text.replace(old, new, 1))
    print("patch STOP_REASON timer: OK")
PY
grep -q 'reason=timer_nominal' "$LAUNCHER" || fail "STOP_REASON timer absent"

# 3a-bis) E17 — purge filter: `*)` dans `"$(...)"` ferme le $() trop tôt
#         (crash si résidus pgrep, ex. Ghost/Hulk mentionnant ace777-test-day1)
python3 - "$LAUNCHER" <<'PY'
import pathlib, sys
path = pathlib.Path(sys.argv[1])
text = path.read_text()
old = """  if [ -n \"$_left\" ]; then
    _left=\"$(echo \"$_left\" | while IFS= read -r line; do
      pid=\"${line%% *}\"
      case \"$(nuage_self_pids | tr '\\n' ' ')\" in *\" $pid \"*|\"$pid \"*) continue ;; esac
      echo \"$line\"
    done)\"
  fi
"""
new = """  if [ -n \"$_left\" ]; then
    # E17: ne pas mettre case *) dans \"$(...)\" — le ) ferme le $() (syntax error)
    _filt=\"\"
    while IFS= read -r _line; do
      [ -z \"$_line\" ] && continue
      _pid=\"${_line%% *}\"
      _keep=\" $(nuage_self_pids | tr '\\n' ' ') \"
      case \"$_keep\" in *\" ${_pid} \"*) continue ;; esac
      _filt=\"${_filt}${_line}\"$'\\n'
    done <<< \"$_left\"
    _left=\"$_filt\"
  fi
"""
marker = "E17: ne pas mettre case"
if marker in text:
    print("patch E17 purge-filter: already present")
elif old not in text:
    sys.exit("FAIL: bloc purge _left filter introuvable (E17)")
else:
    if text.count(old) != 1:
        sys.exit("FAIL: occurrences purge _left filter ≠ 1 (E17)")
    path.write_text(text.replace(old, new, 1))
    print("patch E17 purge-filter: OK")
PY
grep -q 'E17: ne pas mettre case' "$LAUNCHER" || fail "E17 purge-filter absent"

# 3b) Patch garde-fou duo PID (BETA+ALPHA) — réversible via NUAGE_DUO_PID_WATCHDOG
python3 - "$LAUNCHER" <<'PY'
import pathlib, sys, os
path = pathlib.Path(sys.argv[1])
text = path.read_text()
duo_on = os.environ.get("NUAGE_DUO_PID_WATCHDOG", "1").strip() not in ("0", "off", "OFF", "false", "FALSE")

old = """launch_beta
sleep 2
launch_alpha
nuage_semantic_watchdog &
PID_SEMANTIC_WATCHDOG=$!

echo \"NUAGE_V2.1 duo en marche.\"
echo \"Logs: ${LOG_BETA} | ${LOG_ALPHA} | LIVE: ${RUN_DIR}/${tag}_LIVE_COLOR.log\"
echo \"Watchdog sémantique PID=${PID_SEMANTIC_WATCHDOG} → ${ALPHA_HEARTBEAT_FILE}\"
"""

func = r'''
# --- Garde-fou duo PID (couche GO_USINE) : relance process mort BETA et/ou ALPHA ---
# Désactiver: NUAGE_DUO_PID_WATCHDOG=0
nuage_duo_pid_watchdog() {
  local check_interval="${NUAGE_DUO_WATCHDOG_INTERVAL_SEC:-15}"
  local max_relaunch="${NUAGE_DUO_WATCHDOG_MAX_RELAUNCH:-8}"
  local grace_sec="${NUAGE_DUO_WATCHDOG_GRACE_SEC:-45}"
  local diag="${RUN_DIR}/DUO_PID_WATCHDOG.log"
  NUAGE_DUO_RELAUNCH_BETA="${NUAGE_DUO_RELAUNCH_BETA:-0}"
  NUAGE_DUO_RELAUNCH_ALPHA="${NUAGE_DUO_RELAUNCH_ALPHA:-0}"
  NUAGE_DUO_GRACE_UNTIL="${NUAGE_DUO_GRACE_UNTIL:-0}"
  echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) WATCHDOG_DUO: start interval=${check_interval}s max=${max_relaunch}" >>"$diag"

  while [ -f "${RUN_DIR}/master.pid" ]; do
    _mp="$(tr -d ' \n\r' <"${RUN_DIR}/master.pid" 2>/dev/null || true)"
    [ -n "$_mp" ] && kill -0 "$_mp" 2>/dev/null || break
    sleep "$check_interval"

    if [ -f STOP ]; then
      echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) WATCHDOG_DUO: STOP — exit" >>"$diag"
      break
    fi
    # Fin normale timer: les deux STOP posés → ne pas relancer
    if [ -f STOP_BETA ] && [ -f STOP_ALPHA ]; then
      echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) WATCHDOG_DUO: STOP_BETA+STOP_ALPHA — exit" >>"$diag"
      break
    fi

    now="$(date +%s)"
    if [ "${NUAGE_DUO_GRACE_UNTIL:-0}" -gt "$now" ]; then
      continue
    fi

    if [ ! -f STOP_BETA ]; then
      bp=""
      [ -f "${RUN_DIR}/beta_wrapper.pid" ] && bp="$(tr -d ' \n\r' <"${RUN_DIR}/beta_wrapper.pid")"
      if [ -z "$bp" ] || ! kill -0 "$bp" 2>/dev/null; then
        NUAGE_DUO_RELAUNCH_BETA=$((NUAGE_DUO_RELAUNCH_BETA + 1))
        echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) WATCHDOG_DUO: BETA mort — relance #${NUAGE_DUO_RELAUNCH_BETA}/${max_relaunch}" | tee -a "$diag"
        if [ "$NUAGE_DUO_RELAUNCH_BETA" -gt "$max_relaunch" ]; then
          echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) WATCHDOG_DUO: max BETA → STOP session" | tee -a "$diag"
          echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) reason=duo_max_relaunch_beta count=${NUAGE_DUO_RELAUNCH_BETA}" > runs/STOP_REASON.txt
          touch STOP_ALPHA STOP_BETA
          break
        fi
        nuage_kill_genesis_tree "BETA_X5" 2>/dev/null || true
        kill "${PID_BETA_WRAPPER:-}" 2>/dev/null || true
        wait "${PID_BETA_WRAPPER:-}" 2>/dev/null || true
        launch_beta
        PID_BETA_WRAPPER="$(tr -d ' \n\r' <"${RUN_DIR}/beta_wrapper.pid" 2>/dev/null || true)"
        NUAGE_DUO_GRACE_UNTIL=$((now + grace_sec))
        echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) WATCHDOG_DUO: BETA relancé pid=${PID_BETA_WRAPPER}" | tee -a "$diag"
      fi
    fi

    if [ ! -f STOP_ALPHA ]; then
      ap=""
      [ -f "${RUN_DIR}/alpha_wrapper.pid" ] && ap="$(tr -d ' \n\r' <"${RUN_DIR}/alpha_wrapper.pid")"
      if [ -z "$ap" ] || ! kill -0 "$ap" 2>/dev/null; then
        NUAGE_DUO_RELAUNCH_ALPHA=$((NUAGE_DUO_RELAUNCH_ALPHA + 1))
        echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) WATCHDOG_DUO: ALPHA mort — relance #${NUAGE_DUO_RELAUNCH_ALPHA}/${max_relaunch}" | tee -a "$diag"
        if [ "$NUAGE_DUO_RELAUNCH_ALPHA" -gt "$max_relaunch" ]; then
          echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) WATCHDOG_DUO: max ALPHA → STOP session" | tee -a "$diag"
          echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) reason=duo_max_relaunch_alpha count=${NUAGE_DUO_RELAUNCH_ALPHA}" > runs/STOP_REASON.txt
          touch STOP_ALPHA STOP_BETA
          break
        fi
        nuage_kill_genesis_tree "ALPHA_X13_BURST13" 2>/dev/null || true
        kill "${PID_ALPHA_WRAPPER:-}" 2>/dev/null || true
        wait "${PID_ALPHA_WRAPPER:-}" 2>/dev/null || true
        launch_alpha
        PID_ALPHA_WRAPPER="$(tr -d ' \n\r' <"${RUN_DIR}/alpha_wrapper.pid" 2>/dev/null || true)"
        NUAGE_DUO_GRACE_UNTIL=$((now + grace_sec))
        echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) WATCHDOG_DUO: ALPHA relancé pid=${PID_ALPHA_WRAPPER}" | tee -a "$diag"
      fi
    fi
  done
}

'''

if duo_on:
    new = func + """launch_beta
sleep 2
launch_alpha
nuage_semantic_watchdog &
PID_SEMANTIC_WATCHDOG=$!
nuage_duo_pid_watchdog &
PID_DUO_PID_WATCHDOG=$!

echo \"NUAGE_V2.1 duo en marche.\"
echo \"Logs: ${LOG_BETA} | ${LOG_ALPHA} | LIVE: ${RUN_DIR}/${tag}_LIVE_COLOR.log\"
echo \"Watchdog sémantique PID=${PID_SEMANTIC_WATCHDOG} → ${ALPHA_HEARTBEAT_FILE}\"
echo \"Watchdog duo PID=${PID_DUO_PID_WATCHDOG} (relance BETA+ALPHA si process mort)\"
"""
else:
    new = """launch_beta
sleep 2
launch_alpha
nuage_semantic_watchdog &
PID_SEMANTIC_WATCHDOG=$!
PID_DUO_PID_WATCHDOG=""

echo \"NUAGE_V2.1 duo en marche.\"
echo \"Logs: ${LOG_BETA} | ${LOG_ALPHA} | LIVE: ${RUN_DIR}/${tag}_LIVE_COLOR.log\"
echo \"Watchdog sémantique PID=${PID_SEMANTIC_WATCHDOG} → ${ALPHA_HEARTBEAT_FILE}\"
echo \"Watchdog duo PID: OFF (NUAGE_DUO_PID_WATCHDOG=0)\"
"""

if old not in text:
    sys.exit("FAIL: bloc launch_beta/semantic introuvable (patch duo)")
if text.count(old) != 1:
    sys.exit("FAIL: occurrences launch_beta/semantic ≠ 1")
path.write_text(text.replace(old, new, 1))
print("patch duo-pid-watchdog: OK (ON)" if duo_on else "patch duo-pid-watchdog: OK (OFF stub)")
PY

# 3c) Patch côtés bi-dir (BETA AUTO + ALPHA AUTO/BOTH) — défaut OFF = usine intacte
#     NUAGE_BIDIR_SIDES=1 → scout choisit le sens, hunter revenge = opposé (DUO_FORCE_OPPOSITE)
#     Leviers/masses inchangés (x5/200 · x13/800). Ne touche pas genesis.
# 3d) STORM_LATCH — copie runtime genesis + bypass Mode Écoute si tension haute (champion disque intact)
python3 - "$LAUNCHER" <<'PY'
import pathlib, sys, os
path = pathlib.Path(sys.argv[1])
text = path.read_text()
bidir = os.environ.get("NUAGE_BIDIR_SIDES", "0").strip() in ("1", "on", "ON", "true", "TRUE")

old_beta = '''    export FORCE_ENTRY_SIDE="SELL"
    export POSITION_SIDE="SHORT"
    export DUO_MODE="TRUE"
    export DUO_ROLE="SCOUT"'''
new_beta = '''    export FORCE_ENTRY_SIDE="AUTO"
    export POSITION_SIDE="BOTH"
    export DUO_FORCE_OPPOSITE="${DUO_FORCE_OPPOSITE:-TRUE}"
    export DUO_MODE="TRUE"
    export DUO_ROLE="SCOUT"'''

old_alpha = '''    export FORCE_ENTRY_SIDE="BUY"
    export POSITION_SIDE="LONG"
    export DUO_MODE="TRUE"
    export DUO_ROLE="HUNTER"'''
new_alpha = '''    export FORCE_ENTRY_SIDE="AUTO"
    export POSITION_SIDE="BOTH"
    export DUO_FORCE_OPPOSITE="${DUO_FORCE_OPPOSITE:-TRUE}"
    export DUO_MODE="TRUE"
    export DUO_ROLE="HUNTER"'''

# Bannière boot (après SWARM=ON | BETA…)
old_boot = 'echo "SWARM=ON | BETA x${BETA_LEVERAGE_OVERRIDE:-5} | GATE=${NUAGE_TENSION_MAX_AGE_MS:-800}ms"'
# Il peut y avoir 2 occurrences (début + fin) — on annote les deux de façon idempotente
if bidir:
    if old_beta not in text:
        sys.exit("FAIL: bloc FORCE_ENTRY_SIDE BETA introuvable (patch bidir)")
    if old_alpha not in text:
        sys.exit("FAIL: bloc FORCE_ENTRY_SIDE ALPHA introuvable (patch bidir)")
    if text.count(old_beta) != 1 or text.count(old_alpha) != 1:
        sys.exit("FAIL: occurrences FORCE_ENTRY_SIDE ≠ 1 (patch bidir)")
    text = text.replace(old_beta, new_beta, 1).replace(old_alpha, new_alpha, 1)
    boot_note = 'echo "SWARM=ON | BETA x${BETA_LEVERAGE_OVERRIDE:-5} | GATE=${NUAGE_TENSION_MAX_AGE_MS:-800}ms | BIDIR_SIDES=ON (AUTO/BOTH + opposite)"'
    if old_boot not in text:
        sys.exit("FAIL: ligne boot SWARM=ON introuvable (patch bidir)")
    text = text.replace(old_boot, boot_note)
    path.write_text(text)
    print("patch bidir-sides: OK (ON — FORCE_ENTRY_SIDE=AUTO POSITION_SIDE=BOTH)")
else:
    # Usine: laisser SELL/SHORT + BUY/LONG ; annoter boot OFF si présent
    boot_note = 'echo "SWARM=ON | BETA x${BETA_LEVERAGE_OVERRIDE:-5} | GATE=${NUAGE_TENSION_MAX_AGE_MS:-800}ms | BIDIR_SIDES=OFF (usine SELL/BUY)"'
    if old_boot in text:
        text = text.replace(old_boot, boot_note)
        path.write_text(text)
    print("patch bidir-sides: OK (OFF — usine SELL/BUY intacte)")
PY

# 3d-0) Genesis runtime TOUJOURS (champion disque intact) + fix set -e post_delta
#     PROCESS_DIE a capturé: rc=1 sur `[ "$post_delta" -le "$post_grace_i" ]` (test faux + set -e)
GENESIS_DISK="$ROOT/genesis_manifest.txt"
GENESIS_RUNTIME="/tmp/ace777_genesis_runtime.txt"
cp -f "$GENESIS_DISK" "$GENESIS_RUNTIME"
python3 - "$GENESIS_RUNTIME" <<'PY'
import pathlib, sys
path = pathlib.Path(sys.argv[1])
text = path.read_text()
old = '''      post_delta=$((cycle_i - shock_until_i))
      post_grace_i="$(to_int "$SWARM_HUNTER_POST_SHOCKWAVE_SOLO_CYCLES")"
      [ "$post_delta" -le "$post_grace_i" ] && swarm_shockwave_post_solo=1'''
new = '''      post_delta=$((cycle_i - shock_until_i))
      post_grace_i="$(to_int "$SWARM_HUNTER_POST_SHOCKWAVE_SOLO_CYCLES")"
      # FIX set -e: un test faux ne doit PAS tuer le process (E-PROC ALPHA)
      if [ "$post_delta" -le "$post_grace_i" ]; then
        swarm_shockwave_post_solo=1
      fi'''
if old not in text:
    if "FIX set -e: un test faux" in text:
        print("patch set-e post_delta: already present")
    else:
        sys.exit("FAIL: bloc post_delta introuvable (set -e fix)")
else:
    if text.count(old) != 1:
        sys.exit("FAIL: occurrences post_delta ≠ 1")
    path.write_text(text.replace(old, new, 1))
    print("patch set-e post_delta: OK")
PY
python3 - "$LAUNCHER" <<'PY'
import pathlib, sys
path = pathlib.Path(sys.argv[1])
text = path.read_text()
old = 'export ACE777_GENESIS_SOURCE="${ACE777_ROOT}/genesis_manifest.txt"'
new = 'export ACE777_GENESIS_SOURCE="${ACE777_GENESIS_SOURCE:-${ACE777_ROOT}/genesis_manifest.txt}"'
if old in text:
    path.write_text(text.replace(old, new, 1))
    print("patch launcher GENESIS_SOURCE override: OK")
else:
    print("patch launcher GENESIS_SOURCE override: already soft")
PY
export ACE777_GENESIS_SOURCE="$GENESIS_RUNTIME"
echo "GENESIS_RUNTIME: $GENESIS_RUNTIME (disk md5=$(md5 -q "$GENESIS_DISK") — intact)"

# 3d) STORM_LATCH — bypass Mode Écoute si tension >= NUAGE_STORM_TENSION et direction claire
#     + écrit storm_latch.ts pour fenêtre K2 (TTL)
if [ "${NUAGE_STORM_LATCH}" = "1" ] || [ "${NUAGE_STORM_LATCH}" = "TRUE" ] || [ "${NUAGE_STORM_LATCH}" = "on" ]; then
  python3 - "$GENESIS_RUNTIME" <<'PY'
import pathlib, sys
path = pathlib.Path(sys.argv[1])
text = path.read_text()
start = text.find('  detect_soft_anomaly "$tick_bps_abs"')
if start < 0:
    sys.exit("FAIL: detect_soft_anomaly introuvable (STORM)")
end = text.find('  apply_dynamic_sizing', start)
if end < 0:
    sys.exit("FAIL: apply_dynamic_sizing après stase introuvable (STORM)")
old = text[start:end]
if "Mode Écoute" not in old and "Mode Ecoute" not in old:
    sys.exit("FAIL: bloc stase sans Mode Écoute (STORM)")
if "storm_bypass=1" in old:
    print("patch storm-latch: already present")
else:
    new = '''  detect_soft_anomaly "$tick_bps_abs"
  if [ "$STASE_DYNAMIQUE_ENABLED" = "TRUE" ] && [ "$soft_cooldown_remaining" -gt 0 ]; then
    # --- NUAGE_STORM_LATCH (runtime GO) : bypass Mode Écoute en tempête directionnelle ---
    storm_bypass=0
    if [ "${NUAGE_STORM_LATCH:-0}" = "1" ] || [ "${NUAGE_STORM_LATCH:-0}" = "TRUE" ] || [ "${NUAGE_STORM_LATCH:-0}" = "on" ]; then
      _storm_th="${NUAGE_STORM_TENSION:-2.5}"
      if num_ge "${tension_score:-0}" "$_storm_th"; then
        if [ "${mom_direction:-neutral}" != "neutral" ] && [ -n "${mom_direction:-}" ]; then
          storm_bypass=1
          _storm_ram="${ACE777_RAM_EXCHANGE:-/tmp/ace777_ram_exchange}"
          mkdir -p "$_storm_ram" 2>/dev/null || true
          echo "$(date +%s) ${mom_direction} ${tension_score}" > "${_storm_ram}/storm_latch.ts" 2>/dev/null || true
          echo "${C_Y}$(date -u +%H:%M:%S)${C_N} ${C_Y}STORM_LATCH${C_N} bypass Mode Écoute | tension=${tension_score} th=${_storm_th} dir=${mom_direction}"
        fi
      fi
    fi
    if [ "$storm_bypass" -eq 0 ]; then
    spread_cold=0
    volat_cold=0
    num_lt "$spread_bps" "$STASE_DYNAMIQUE_MAX_SPREAD_BPS" && spread_cold=1
    num_lt "$impulse_abs_bps_s" "$STASE_DYNAMIQUE_MAX_VOLATILITY" && volat_cold=1
    if [ "$spread_cold" -eq 0 ] || [ "$volat_cold" -eq 0 ]; then
      echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,0,stase_ecoute,reason=spread_or_volat_not_cold spread_bps=$spread_bps volat=$impulse_abs_bps_s" >> "$LOG_FILE"
      sk_lev="$C_C"; num_ge "$current_leverage" "13" && sk_lev="$C_G"; num_le "$current_leverage" "5" && sk_lev="$C_Y"
      echo "${C_C}$(date -u +%H:%M:%S)${C_N} ${sk_lev}x$current_leverage${C_N} ${C_C}#$i${C_N} SKIP ${C_N}| Mode Écoute: spread=$spread_bps volat=$impulse_abs_bps_s (attente froid)"
      sleep "$SLEEP_SEC"
      continue
    fi
    fi
  fi
'''
    path.write_text(text[:start] + new + text[end:])
_chk = path.read_text()
if "storm_bypass=1" not in _chk or "NUAGE_STORM_LATCH" not in _chk:
    sys.exit("FAIL: patch STORM non appliqué")
print("patch storm-latch genesis runtime: OK")
PY
  python3 - "$LAUNCHER" <<'PY'
import pathlib, sys
path = pathlib.Path(sys.argv[1])
text = path.read_text()
needle = 'GATE=${NUAGE_TENSION_MAX_AGE_MS:-800}ms'
if "STORM_LATCH=" not in text:
    text = text.replace(
        needle,
        needle + ' | STORM_LATCH=${NUAGE_STORM_LATCH:-OFF}',
        1,
    )
    path.write_text(text)
print("patch boot STORM banner: OK")
PY
  echo "STORM_LATCH: ON (runtime + storm_latch.ts)"
else
  echo "STORM_LATCH: OFF"
fi

# 3d-bis) STORM_HOLD (K3v3) — min hold avant shock/fluid
#         E14: latch à l'ENTRÉE — en fin de mèche tension live retombe < th
#         et K3v2 laissait passer shock à 6–7s (run 2026-07-22 −10.5$ ALPHA).
#         Flag historique: NUAGE_STORM_SCOUT_HOLD=1
if [ "${NUAGE_STORM_SCOUT_HOLD}" = "1" ] || [ "${NUAGE_STORM_SCOUT_HOLD}" = "TRUE" ] || [ "${NUAGE_STORM_SCOUT_HOLD}" = "on" ]; then
  python3 - "$GENESIS_RUNTIME" <<'PY'
import pathlib, sys
path = pathlib.Path(sys.argv[1])
text = path.read_text()

if "STORM_HOLD_K3v3" in text and "storm_hold_latched" in text:
    print("patch storm-hold (K3v3 entry-latch): already present")
    raise SystemExit(0)

latch_anchor = '''  fatigue_count=0
  slow_velocity_count=0
  current_bps="0"
  current_pnl_live="0"
  while true; do'''

latch_block = '''  fatigue_count=0
  slow_velocity_count=0
  current_bps="0"
  current_pnl_live="0"
  # STORM_HOLD_K3v3: latch hold si entrée en tempête (scout|hunter)
  storm_hold_latched=0
  if [ "${NUAGE_STORM_SCOUT_HOLD:-0}" = "1" ] || [ "${NUAGE_STORM_SCOUT_HOLD:-0}" = "TRUE" ] || [ "${NUAGE_STORM_SCOUT_HOLD:-0}" = "on" ]; then
    if duo_is_scout || duo_is_hunter; then
      if num_ge "${tension_score:-0}" "${NUAGE_STORM_TENSION:-2.5}"; then
        storm_hold_latched=1
      fi
    fi
  fi
  while true; do'''

new_shock = '''      if num_le "$vel_abs_bps_s" "$V8_SHOCK_SPEED_EPS_BPS_S"; then
        # STORM_HOLD_K3v3: min hold — latch entrée OU tension live
        storm_hold_arm=0
        if [ "${NUAGE_STORM_SCOUT_HOLD:-0}" = "1" ] || [ "${NUAGE_STORM_SCOUT_HOLD:-0}" = "TRUE" ] || [ "${NUAGE_STORM_SCOUT_HOLD:-0}" = "on" ]; then
          if duo_is_scout || duo_is_hunter; then
            if [ "${storm_hold_latched:-0}" = "1" ] || num_ge "${tension_score:-0}" "${NUAGE_STORM_TENSION:-2.5}"; then
              if [ "$hold_sec" -lt "${NUAGE_STORM_MIN_HOLD_SEC:-20}" ]; then
                storm_hold_arm=1
              fi
            fi
          fi
        fi
        if [ "$storm_hold_arm" -eq 0 ]; then
          reason="shock_inversion_stop"; break
        fi
      fi'''

new_fluid = '''      # STORM_HOLD_K3v3: min hold scout+hunter (latch entrée OU tension live)
      storm_hold_arm=0
      if [ "${NUAGE_STORM_SCOUT_HOLD:-0}" = "1" ] || [ "${NUAGE_STORM_SCOUT_HOLD:-0}" = "TRUE" ] || [ "${NUAGE_STORM_SCOUT_HOLD:-0}" = "on" ]; then
        if duo_is_scout || duo_is_hunter; then
          if [ "${storm_hold_latched:-0}" = "1" ] || num_ge "${tension_score:-0}" "${NUAGE_STORM_TENSION:-2.5}"; then
            if [ "$hold_sec" -lt "${NUAGE_STORM_MIN_HOLD_SEC:-20}" ]; then
              storm_hold_arm=1
            fi
          fi
        fi
      fi
      if [ "$storm_hold_arm" -eq 0 ] && num_le "$vel_signed_bps_s" "$FLUID_EXIT_INVERT_BPS_S"; then
        reason="fluid_exit_inversion"; break
      fi
      if [ "$storm_hold_arm" -eq 0 ] && num_le "$vel_abs_bps_s" "$FLUID_EXIT_BRAKE_BPS_S"; then
        reason="fluid_exit_brake"; break
      fi'''

# Remplace tout bloc shock déjà patché (K3v1/v2) ou usine
import re
shock_pat = re.compile(
    r'      if num_le "\$vel_abs_bps_s" "\$V8_SHOCK_SPEED_EPS_BPS_S"; then\n'
    r'(?:        .*\n)*?'
    r'      fi',
    re.M,
)
fluid_pat = re.compile(
    r'(?:      # STORM_HOLD_K3v2:.*\n|      storm_hold_arm=0\n|      if num_le "\$vel_signed_bps_s" "\$FLUID_EXIT_INVERT_BPS_S"; then\n)'
    r'(?:.*\n)*?'
    r'      if (?:\[ "\$storm_hold_arm" -eq 0 \] && )?num_le "\$vel_abs_bps_s" "\$FLUID_EXIT_BRAKE_BPS_S"; then\n'
    r'        reason="fluid_exit_brake"; break\n'
    r'      fi',
    re.M,
)

old_shock_usine = '''      if num_le "$vel_abs_bps_s" "$V8_SHOCK_SPEED_EPS_BPS_S"; then
        reason="shock_inversion_stop"; break
      fi'''

old_fluid_usine = '''      if num_le "$vel_signed_bps_s" "$FLUID_EXIT_INVERT_BPS_S"; then
        reason="fluid_exit_inversion"; break
      fi
      if num_le "$vel_abs_bps_s" "$FLUID_EXIT_BRAKE_BPS_S"; then
        reason="fluid_exit_brake"; break
      fi'''

# 1) latch init
if "storm_hold_latched=" not in text:
    if latch_anchor not in text:
        sys.exit("FAIL: ancre hold loop introuvable (K3v3 latch)")
    text = text.replace(latch_anchor, latch_block, 1)

# 2) shock
if "STORM_HOLD_K3v3: min hold — latch" in text:
    pass
elif old_shock_usine in text and text.count(old_shock_usine) == 1:
    text = text.replace(old_shock_usine, new_shock, 1)
else:
    m = shock_pat.search(text)
    if not m or "V8_SHOCK_SPEED_EPS_BPS_S" not in m.group(0):
        sys.exit("FAIL: bloc shock_inversion introuvable (K3v3)")
    text = shock_pat.sub(new_shock, text, count=1)

# 3) fluid
if "STORM_HOLD_K3v3: min hold scout+hunter (latch" in text:
    pass
elif old_fluid_usine in text and text.count(old_fluid_usine) == 1:
    text = text.replace(old_fluid_usine, new_fluid, 1)
else:
    # remplacer bloc K3v2 fluid si présent
    old_fluid_v2 = '''      # STORM_HOLD_K3v2: min hold scout+hunter avant fluid exit
      storm_hold_arm=0
      if [ "${NUAGE_STORM_SCOUT_HOLD:-0}" = "1" ] || [ "${NUAGE_STORM_SCOUT_HOLD:-0}" = "TRUE" ] || [ "${NUAGE_STORM_SCOUT_HOLD:-0}" = "on" ]; then
        if num_ge "${tension_score:-0}" "${NUAGE_STORM_TENSION:-2.5}"; then
          if duo_is_scout || duo_is_hunter; then
            if [ "$hold_sec" -lt "${NUAGE_STORM_MIN_HOLD_SEC:-20}" ]; then
              storm_hold_arm=1
            fi
          fi
        fi
      fi
      if [ "$storm_hold_arm" -eq 0 ] && num_le "$vel_signed_bps_s" "$FLUID_EXIT_INVERT_BPS_S"; then
        reason="fluid_exit_inversion"; break
      fi
      if [ "$storm_hold_arm" -eq 0 ] && num_le "$vel_abs_bps_s" "$FLUID_EXIT_BRAKE_BPS_S"; then
        reason="fluid_exit_brake"; break
      fi'''
    if old_fluid_v2 in text:
        text = text.replace(old_fluid_v2, new_fluid, 1)
    else:
        m = fluid_pat.search(text)
        if not m:
            sys.exit("FAIL: bloc fluid_exit introuvable (K3v3)")
        text = fluid_pat.sub(new_fluid, text, count=1)

path.write_text(text)
_chk = path.read_text()
if "STORM_HOLD_K3v3" not in _chk or "storm_hold_latched" not in _chk:
    sys.exit("FAIL: patch STORM_HOLD K3v3 non appliqué")
print("patch storm-hold (K3v3 entry-latch): OK")
PY
  python3 - "$LAUNCHER" <<'PY'
import pathlib, sys
path = pathlib.Path(sys.argv[1])
text = path.read_text()
if "STORM_HOLD=" not in text:
    needle = 'GATE=${NUAGE_TENSION_MAX_AGE_MS:-800}ms'
    if needle in text:
        text = text.replace(needle, needle + ' | STORM_HOLD=${NUAGE_STORM_SCOUT_HOLD:-OFF}/${NUAGE_STORM_MIN_HOLD_SEC:-20}s', 1)
path.write_text(text)
print("patch launcher STORM_HOLD banner: OK")
PY
  echo "STORM_HOLD: ON (K3v3 entry-latch) min_hold=${NUAGE_STORM_MIN_HOLD_SEC}s th=${NUAGE_STORM_TENSION}"
else
  echo "STORM_SCOUT_HOLD: OFF"
fi

# 3d-ter) STORM_HUNTER (K2v2) — ALPHA entre sans closed_loss scout (anti duo no_trigger)
#         E13 fix: armé sur tension live ≥ th (latch TTL n'est plus un mur)
#         Sens: mom_direction, sinon dir dans storm_latch.ts, sinon radar_direction
#         Spread: floor dès tension haute (même si dir encore floue)
if [ "${NUAGE_STORM_HUNTER}" = "1" ] || [ "${NUAGE_STORM_HUNTER}" = "TRUE" ] || [ "${NUAGE_STORM_HUNTER}" = "on" ]; then
  python3 - "$GENESIS_RUNTIME" <<'PY'
import pathlib, sys
path = pathlib.Path(sys.argv[1])
text = path.read_text()

# Si K2v1 déjà là → on remplace les blocs ; si K2v2 → skip
if "STORM_HUNTER_K2v2" in text:
    print("patch storm-hunter (K2v2): already present")
    raise SystemExit(0)

# --- Blocs cibles : usine pure OU K2v1 déjà patché ---
old_radar_usine = '''  swarm_telemetry_publish "$i" "$tension_score" "$last_swarm_conf" "$mom_direction" "$mom_bps" "active"
  swarm_apply_coupling "$i"

  if ! check_radar "$momentum_signal" "$spread_bps"; then'''

old_radar_v1 = '''  swarm_telemetry_publish "$i" "$tension_score" "$last_swarm_conf" "$mom_direction" "$mom_bps" "active"
  swarm_apply_coupling "$i"

  # NUAGE_STORM_HUNTER (K2): élargit spread ALPHA pendant fenêtre tempête
  if duo_is_hunter; then
    if [ "${NUAGE_STORM_HUNTER:-0}" = "1" ] || [ "${NUAGE_STORM_HUNTER:-0}" = "TRUE" ] || [ "${NUAGE_STORM_HUNTER:-0}" = "on" ]; then
      if num_ge "${tension_score:-0}" "${NUAGE_STORM_TENSION:-2.5}"; then
        if [ "${mom_direction:-neutral}" != "neutral" ] && [ -n "${mom_direction:-}" ]; then
          cycle_swarm_spread_floor="${NUAGE_STORM_MAX_SPREAD_BPS:-14}"
        fi
      fi
    fi
  fi

  if ! check_radar "$momentum_signal" "$spread_bps"; then'''

new_radar = '''  swarm_telemetry_publish "$i" "$tension_score" "$last_swarm_conf" "$mom_direction" "$mom_bps" "active"
  swarm_apply_coupling "$i"

  # STORM_HUNTER_K2v2: spread floor ALPHA dès tension haute (dir optionnelle)
  if duo_is_hunter; then
    if [ "${NUAGE_STORM_HUNTER:-0}" = "1" ] || [ "${NUAGE_STORM_HUNTER:-0}" = "TRUE" ] || [ "${NUAGE_STORM_HUNTER:-0}" = "on" ]; then
      if num_ge "${tension_score:-0}" "${NUAGE_STORM_TENSION:-2.5}"; then
        cycle_swarm_spread_floor="${NUAGE_STORM_MAX_SPREAD_BPS:-14}"
      fi
    fi
  fi

  if ! check_radar "$momentum_signal" "$spread_bps"; then'''

old_duo_usine = '''    if [ "$duo_allow" != "true" ] && [ "$SWARM_HUNTER_POST_SHOCKWAVE_SOLO" = "TRUE" ]; then
      if [ "$swarm_shockwave_post_solo" = "1" ] && num_gt "$tension_score" "$SWARM_HUNTER_POST_SHOCKWAVE_TENSION"; then
        duo_allow="true"
        duo_mode_note="post_shockwave_solo"
        duo_reason="tension_fly"
      fi
    fi
    if [ "$duo_allow" != "true" ]; then'''

# K2v1 bloc (entre post_shockwave et if duo_allow) — matcher début v1 pour strip
old_duo_v1_marker = "    # NUAGE_STORM_HUNTER (K2): entrée sans closed_loss scout (anti no_trigger)"

new_duo = '''    if [ "$duo_allow" != "true" ] && [ "$SWARM_HUNTER_POST_SHOCKWAVE_SOLO" = "TRUE" ]; then
      if [ "$swarm_shockwave_post_solo" = "1" ] && num_gt "$tension_score" "$SWARM_HUNTER_POST_SHOCKWAVE_TENSION"; then
        duo_allow="true"
        duo_mode_note="post_shockwave_solo"
        duo_reason="tension_fly"
      fi
    fi
    # STORM_HUNTER_K2v2: anti no_trigger — tension live ≥ th (latch = bonus dir, pas un mur TTL)
    if [ "$duo_allow" != "true" ]; then
      if [ "${NUAGE_STORM_HUNTER:-0}" = "1" ] || [ "${NUAGE_STORM_HUNTER:-0}" = "TRUE" ] || [ "${NUAGE_STORM_HUNTER:-0}" = "on" ]; then
        _storm_ram="${ACE777_RAM_EXCHANGE:-/tmp/ace777_ram_exchange}"
        _storm_file="${_storm_ram}/storm_latch.ts"
        _storm_th="${NUAGE_STORM_TENSION:-2.5}"
        _storm_age="-"
        _storm_dir="${mom_direction:-neutral}"
        if [ -f "$_storm_file" ]; then
          _storm_ts="$(awk '{print $1}' "$_storm_file" 2>/dev/null || echo 0)"
          _storm_latch_dir="$(awk '{print $2}' "$_storm_file" 2>/dev/null || true)"
          _storm_age=$(( $(date +%s) - ${_storm_ts:-0} ))
          if [ "$_storm_dir" = "neutral" ] || [ -z "$_storm_dir" ]; then
            case "${_storm_latch_dir}" in long|short) _storm_dir="${_storm_latch_dir}" ;; esac
          fi
        fi
        if [ "$_storm_dir" = "neutral" ] || [ -z "$_storm_dir" ]; then
          case "${radar_direction:-neutral}" in long|short) _storm_dir="${radar_direction}" ;; esac
        fi
        _storm_ok=0
        if num_ge "${tension_score:-0}" "$_storm_th"; then
          case "${_storm_dir}" in
            long|short) _storm_ok=1 ;;
          esac
        fi
        if [ "$_storm_ok" -eq 1 ]; then
          duo_allow="true"
          duo_mode_note="storm"
          duo_reason="storm_live"
          duo_forced="AUTO"
          echo "${C_Y}$(date -u +%H:%M:%S)${C_N} ${C_Y}STORM_HUNTER${C_N} arm | tension=${tension_score} th=${_storm_th} dir=${_storm_dir} age=${_storm_age}"
        fi
      fi
    fi
    if [ "$duo_allow" != "true" ]; then'''

old_side_usine = '''    if [ "$duo_forced" = "BUY" ]; then
      side="BUY"; close_side="SELL"; signed_dir="1"
    elif [ "$duo_forced" = "SELL" ]; then
      side="SELL"; close_side="BUY"; signed_dir="-1"
    fi
    if [ "$duo_mode_note" = "revenge" ] || [ "$duo_mode_note" = "burst" ]; then'''

old_side_v1 = '''    if [ "$duo_forced" = "BUY" ]; then
      side="BUY"; close_side="SELL"; signed_dir="1"
    elif [ "$duo_forced" = "SELL" ]; then
      side="SELL"; close_side="BUY"; signed_dir="-1"
    fi
    # STORM_HUNTER: même sens que le flux (pas revenge inverse)
    if [ "$duo_mode_note" = "storm" ]; then
      if [ "$mom_direction" = "long" ]; then
        side="BUY"; close_side="SELL"; signed_dir="1"
      elif [ "$mom_direction" = "short" ]; then
        side="SELL"; close_side="BUY"; signed_dir="-1"
      fi
    fi
    if [ "$duo_mode_note" = "revenge" ] || [ "$duo_mode_note" = "burst" ]; then'''

new_side = '''    if [ "$duo_forced" = "BUY" ]; then
      side="BUY"; close_side="SELL"; signed_dir="1"
    elif [ "$duo_forced" = "SELL" ]; then
      side="SELL"; close_side="BUY"; signed_dir="-1"
    fi
    # STORM_HUNTER_K2v2: sens = flux résolu (_storm_dir ou mom)
    if [ "$duo_mode_note" = "storm" ]; then
      _side_dir="${_storm_dir:-${mom_direction:-neutral}}"
      if [ "$_side_dir" = "long" ]; then
        side="BUY"; close_side="SELL"; signed_dir="1"
      elif [ "$_side_dir" = "short" ]; then
        side="SELL"; close_side="BUY"; signed_dir="-1"
      fi
    fi
    if [ "$duo_mode_note" = "revenge" ] || [ "$duo_mode_note" = "burst" ]; then'''

# Radar
if old_radar_v1 in text:
    text = text.replace(old_radar_v1, new_radar, 1)
elif old_radar_usine in text:
    if text.count(old_radar_usine) != 1:
        sys.exit("FAIL: radar usine occurrences ≠ 1 (K2v2)")
    text = text.replace(old_radar_usine, new_radar, 1)
else:
    sys.exit("FAIL: bloc radar introuvable (K2v2)")

# Duo: si v1 présent, retirer v1 puis injecter v2 après post_shockwave
if old_duo_v1_marker in text:
    # Strip from v1 comment through the closing before "if [ \"$duo_allow\" != \"true\" ]; then" that follows storm block
    start = text.find(old_duo_v1_marker)
    if start < 0:
        sys.exit("FAIL: marker K2v1 introuvable")
    # Find post_shockwave block start to rebuild from there
    ps = text.rfind("    if [ \"$duo_allow\" != \"true\" ] && [ \"$SWARM_HUNTER_POST_SHOCKWAVE_SOLO\" = \"TRUE\" ]; then", 0, start)
    if ps < 0:
        sys.exit("FAIL: post_shockwave avant K2v1 introuvable")
    # End: the duo_wait "if [ \"$duo_allow\" != \"true\" ]; then" AFTER the v1 storm block
    end = text.find('    if [ "$duo_allow" != "true" ]; then\n      echo "$(date -u +%FT%TZ),$i,SKIP,SKIPPED,,,,,0,duo_wait', start)
    if end < 0:
        sys.exit("FAIL: duo_wait après K2v1 introuvable")
    text = text[:ps] + new_duo + text[end:]
elif old_duo_usine in text:
    if text.count(old_duo_usine) != 1:
        sys.exit("FAIL: duo usine occurrences ≠ 1 (K2v2)")
    text = text.replace(old_duo_usine, new_duo, 1)
else:
    sys.exit("FAIL: bloc duo introuvable (K2v2)")

# Side
if old_side_v1 in text:
    text = text.replace(old_side_v1, new_side, 1)
elif old_side_usine in text:
    if text.count(old_side_usine) != 1:
        sys.exit("FAIL: side usine occurrences ≠ 1 (K2v2)")
    text = text.replace(old_side_usine, new_side, 1)
else:
    sys.exit("FAIL: bloc side introuvable (K2v2)")

path.write_text(text)
_chk = path.read_text()
if "STORM_HUNTER_K2v2" not in _chk or 'duo_reason="storm_live"' not in _chk:
    sys.exit("FAIL: patch STORM_HUNTER K2v2 non appliqué")
print("patch storm-hunter (K2v2): OK")
PY
  # Export explicite NUAGE_STORM_* dans les subshells BETA/ALPHA (E13: env peut ne pas suivre)
  python3 - "$LAUNCHER" <<'PY'
import pathlib, sys
path = pathlib.Path(sys.argv[1])
text = path.read_text()
storm_exports = '''    export NUAGE_STORM_HUNTER="${NUAGE_STORM_HUNTER:-0}"
    export NUAGE_STORM_LATCH="${NUAGE_STORM_LATCH:-0}"
    export NUAGE_STORM_SCOUT_HOLD="${NUAGE_STORM_SCOUT_HOLD:-0}"
    export NUAGE_STORM_TENSION="${NUAGE_STORM_TENSION:-2.5}"
    export NUAGE_STORM_TTL_SEC="${NUAGE_STORM_TTL_SEC:-20}"
    export NUAGE_STORM_MAX_SPREAD_BPS="${NUAGE_STORM_MAX_SPREAD_BPS:-14}"
    export NUAGE_STORM_MIN_HOLD_SEC="${NUAGE_STORM_MIN_HOLD_SEC:-20}"
    export ACE777_RAM_EXCHANGE="${ACE777_RAM_EXCHANGE:-/tmp/ace777_ram_exchange}"
'''
if "export NUAGE_STORM_HUNTER=" in text:
    print("patch launcher STORM env export: already present")
else:
    needle_a = '    export NUAGE_TENSION_MAX_AGE_MS="${NUAGE_TENSION_MAX_AGE_MS:-800}"\n'
    needle_b = '    export SWARM_COUPLING_ENABLED=TRUE\n'
    if needle_a not in text:
        sys.exit("FAIL: needle ALPHA NUAGE_TENSION introuvable (storm env)")
    # ALPHA: après NUAGE_TENSION
    text = text.replace(needle_a, needle_a + storm_exports, 1)
    # BETA: première occurrence SWARM_COUPLING dans launch_beta (avant ALPHA)
    idx = text.find("launch_beta()")
    idx2 = text.find(needle_b, idx)
    if idx2 < 0:
        sys.exit("FAIL: SWARM_COUPLING dans launch_beta introuvable")
    text = text[:idx2] + needle_b + storm_exports + text[idx2 + len(needle_b):]
    path.write_text(text)
    print("patch launcher STORM env export: OK (BETA+ALPHA)")
PY
  python3 - "$LAUNCHER" <<'PY'
import pathlib, sys
path = pathlib.Path(sys.argv[1])
text = path.read_text()
if "STORM_HUNTER=" not in text:
    needle = 'GATE=${NUAGE_TENSION_MAX_AGE_MS:-800}ms'
    if needle in text:
        text = text.replace(
            needle,
            needle + ' | STORM_HUNTER=${NUAGE_STORM_HUNTER:-OFF}/ttl=${NUAGE_STORM_TTL_SEC:-20}s',
            1,
        )
        path.write_text(text)
print("patch launcher STORM_HUNTER banner: OK")
PY
  echo "STORM_HUNTER: ON (K2v2 live) ttl=${NUAGE_STORM_TTL_SEC}s spread_max=${NUAGE_STORM_MAX_SPREAD_BPS} th=${NUAGE_STORM_TENSION}"
else
  echo "STORM_HUNTER: OFF"
fi

# 3e) PROCESS_EXIT — raison de mort process (run_unit + trap dans preamble)
#     Corrige aussi: `wait || true` masquait rc (toujours 0) → E10 impossible à diagnostiquer
python3 - "$LAUNCHER" <<'PY'
import pathlib, sys
path = pathlib.Path(sys.argv[1])
text = path.read_text()

old_wait = '''  wait "$wrapper_pid" 2>/dev/null || true
  local rc=$?

  nuage_kill_tail_for_unit "$unit"
  kill "$tee_pid" 2>/dev/null || true
  wait "$tee_pid" 2>/dev/null || true
  rm -f "$raw_log" "${RUN_DIR}/${unit}_tail.pid"

  return "$rc"
}'''

new_wait = '''  set +e
  wait "$wrapper_pid" 2>/dev/null
  local rc=$?
  set -e

  # PROCESS_EXIT (E10) — ne plus perdre le code/signal de mort
  local how="exit" sig="" why=""
  if [ "$rc" -eq 0 ]; then
    how="exit0"
    why="clean_end_or_self_exit_0"
  elif [ "$rc" -gt 128 ]; then
    how="signal"
    sig=$((rc - 128))
    why="killed_by_signal_${sig}"
  else
    why="nonzero_rc_${rc}"
  fi
  local exit_line
  exit_line="$(date -u +%Y-%m-%dT%H:%M:%SZ) PROCESS_EXIT unit=${unit} wrapper=${wrapper_pid} genesis=${genesis_pid:-?} how=${how} why=${why} rc=${rc}"
  mkdir -p "${RUN_DIR}"
  echo "$exit_line" >> "${RUN_DIR}/PROCESS_EXIT.log" 2>/dev/null || true
  echo "$exit_line" >> "$live_log" 2>/dev/null || true
  echo "[$unit] ${C_Y:-}${exit_line}${C_N:-}"
  if [ "$rc" -ne 0 ] && [ -f "$raw_log" ]; then
    cp -f "$raw_log" "${RUN_DIR}/.${tag}_${unit}.raw.EXIT.rc${rc}.log" 2>/dev/null || true
  fi

  nuage_kill_tail_for_unit "$unit"
  kill "$tee_pid" 2>/dev/null || true
  wait "$tee_pid" 2>/dev/null || true
  rm -f "$raw_log" "${RUN_DIR}/${unit}_tail.pid"

  return "$rc"
}'''

if old_wait not in text:
    sys.exit("FAIL: bloc wait wrapper_pid introuvable (patch PROCESS_EXIT)")
if text.count(old_wait) != 1:
    sys.exit("FAIL: occurrences wait wrapper ≠ 1")
text = text.replace(old_wait, new_wait, 1)

old_pre = '''NUAGE_TENSION_MAX_AGE_MS="${NUAGE_TENSION_MAX_AGE_MS:-800}"
ALPHA_HEARTBEAT_FILE="${ALPHA_HEARTBEAT_FILE:-/tmp/alpha_heartbeat.txt}"

duo_hunter_phase_barrier() { :; }'''

q = chr(39)  # quote simple pour trap bash
new_pre = (
    'NUAGE_TENSION_MAX_AGE_MS="${NUAGE_TENSION_MAX_AGE_MS:-800}"\n'
    'ALPHA_HEARTBEAT_FILE="${ALPHA_HEARTBEAT_FILE:-/tmp/alpha_heartbeat.txt}"\n'
    '\n'
    '# PROCESS_DIE — dernière commande si set -e / signal tue bash -s (E10)\n'
    '_ACE777_DIE_LOGGED=0\n'
    'ace777_process_die_log() {\n'
    '  local ec=${1:-$?}\n'
    '  [ "${_ACE777_DIE_LOGGED:-0}" = "1" ] && return 0\n'
    '  _ACE777_DIE_LOGGED=1\n'
    '  echo "PROCESS_DIE | ts=$(date -u +%Y-%m-%dT%H:%M:%SZ) role=${DUO_ROLE:-?} stop=${STOP_FILE:-?} ec=${ec} last_cmd=${BASH_COMMAND:-?} line=${BASH_LINENO[0]:-?}"\n'
    '}\n'
    f'trap {q}ace777_process_die_log $?{q} ERR\n'
    f'trap {q}ace777_process_die_log $?{q} EXIT\n'
    '\n'
    'duo_hunter_phase_barrier() { :; }'
)

if old_pre not in text:
    sys.exit("FAIL: NUAGE_PREAMBLE introuvable (patch PROCESS_DIE)")
if text.count(old_pre) != 1:
    sys.exit("FAIL: occurrences preamble ≠ 1")
text = text.replace(old_pre, new_pre, 1)

path.write_text(text)
print("patch PROCESS_EXIT/DIE: OK (run_unit rc + trap ERR/EXIT)")
PY

# 3g) E16 — watchdog sémantique: stale ≠ mort (skip kill si process ALIVE)
python3 - "$LAUNCHER" <<'PY'
import pathlib, sys
path = pathlib.Path(sys.argv[1])
text = path.read_text()
if "skip kill (E16)" in text:
    print("patch E16 semantic-alive: already present")
    raise SystemExit(0)

old = '''    if [ "$age_sec" -le "$stale_limit" ]; then
      continue
    fi

    NUAGE_RELAUNCH_COUNT=$((NUAGE_RELAUNCH_COUNT + 1))
    echo "WATCHDOG_SEMANTIC: ALPHA stale ${age_sec}s (seuil=${stale_limit}s) — relance #${NUAGE_RELAUNCH_COUNT}/${max_relaunch}"
'''

# Variante déjà hygiénisée (_wd_echo) — TIMER_WAIT / runs antérieurs
old_wd = '''    if [ "$age_sec" -le "$stale_limit" ]; then
      continue
    fi

    NUAGE_RELAUNCH_COUNT=$((NUAGE_RELAUNCH_COUNT + 1))
    _wd_echo "WATCHDOG_SEMANTIC: ALPHA stale ${age_sec}s (seuil=${stale_limit}s) — relance #${NUAGE_RELAUNCH_COUNT}/${max_relaunch}"
'''

new = '''    if [ "$age_sec" -le "$stale_limit" ]; then
      continue
    fi

    # E16: heartbeat stale ≠ process mort (NET_RETRY peut geler le HB >60s).
    if [ -f STOP_ALPHA ]; then
      echo "WATCHDOG_SEMANTIC: ALPHA stale ${age_sec}s mais STOP_ALPHA présent — pas de relance"
      break
    fi
    _alive=0
    _gp=""
    [ -f "${RUN_DIR}/ALPHA_X13_BURST13_genesis.pid" ] && _gp="$(tr -d ' \\n\\r' <"${RUN_DIR}/ALPHA_X13_BURST13_genesis.pid" 2>/dev/null || true)"
    [ -z "$_gp" ] && [ -f "${RUN_DIR}/alpha_wrapper.pid" ] && _gp="$(tr -d ' \\n\\r' <"${RUN_DIR}/alpha_wrapper.pid" 2>/dev/null || true)"
    [ -z "$_gp" ] && _gp="${PID_ALPHA_WRAPPER:-}"
    if [ -n "$_gp" ] && kill -0 "$_gp" 2>/dev/null; then
      _alive=1
    fi
    if [ "$_alive" = "1" ]; then
      echo "WATCHDOG_SEMANTIC: ALPHA stale ${age_sec}s (seuil=${stale_limit}s) mais process ALIVE (pid=${_gp}) — skip kill (E16)"
      continue
    fi

    NUAGE_RELAUNCH_COUNT=$((NUAGE_RELAUNCH_COUNT + 1))
    echo "WATCHDOG_SEMANTIC: ALPHA stale ${age_sec}s (seuil=${stale_limit}s) process MORT — relance #${NUAGE_RELAUNCH_COUNT}/${max_relaunch}"
'''

new_wd = new.replace('echo "WATCHDOG_SEMANTIC:', '_wd_echo "WATCHDOG_SEMANTIC:')

if old in text:
    if text.count(old) != 1:
        sys.exit("FAIL: occurrences stale-relaunch ≠ 1 (E16)")
    path.write_text(text.replace(old, new, 1))
    print("patch E16 semantic-alive: OK")
elif old_wd in text:
    if text.count(old_wd) != 1:
        sys.exit("FAIL: occurrences stale-relaunch _wd ≠ 1 (E16)")
    path.write_text(text.replace(old_wd, new_wd, 1))
    print("patch E16 semantic-alive: OK (_wd_echo)")
else:
    sys.exit("FAIL: bloc stale-relaunch introuvable (patch E16)")
PY

# 4) Vérifs post-patch
grep -q 'INDEX SYNC: OFF' "$LAUNCHER" || fail "INDEX SYNC OFF perdu"
grep -q 'PROCESS_EXIT unit=' "$LAUNCHER" || fail "PROCESS_EXIT absent"
grep -q 'PROCESS_DIE' "$LAUNCHER" || fail "PROCESS_DIE trap absent"
grep -q 'skip kill (E16)' "$LAUNCHER" || fail "E16 semantic-alive absent"
grep -q 'attente timer' "$LAUNCHER" || fail "ligne attente timer absente"
grep -q 'wait "$PID_TIMER"' "$LAUNCHER" || fail "wait PID_TIMER absent"
grep -q 'wait "$PID_BETA_WRAPPER"' "$LAUNCHER" && fail "wait BETA wrapper encore présent"
grep -q 'wait "$PID_ALPHA_WRAPPER"' "$LAUNCHER" && fail "wait ALPHA wrapper encore présent"
if [ "${NUAGE_DUO_PID_WATCHDOG}" != "0" ]; then
  grep -q 'nuage_duo_pid_watchdog' "$LAUNCHER" || fail "duo watchdog absent"
  grep -q 'Watchdog duo PID=' "$LAUNCHER" || fail "ligne boot duo absente"
fi
if [ "${NUAGE_BIDIR_SIDES}" = "1" ]; then
  grep -q 'FORCE_ENTRY_SIDE="AUTO"' "$LAUNCHER" || fail "bidir AUTO absent"
  grep -q 'POSITION_SIDE="BOTH"' "$LAUNCHER" || fail "bidir BOTH absent"
  grep -q 'BIDIR_SIDES=ON' "$LAUNCHER" || fail "bannière BIDIR ON absente"
  # Usine stricte ne doit plus forcer SELL/BUY dans launch_*
  grep -q 'FORCE_ENTRY_SIDE="SELL"' "$LAUNCHER" && fail "bidir: SELL forcé encore présent"
  grep -q 'FORCE_ENTRY_SIDE="BUY"' "$LAUNCHER" && fail "bidir: BUY forcé encore présent"
else
  grep -q 'FORCE_ENTRY_SIDE="SELL"' "$LAUNCHER" || fail "usine BETA SELL perdu"
  grep -q 'FORCE_ENTRY_SIDE="BUY"' "$LAUNCHER" || fail "usine ALPHA BUY perdu"
fi
if [ "${NUAGE_STORM_LATCH}" = "1" ] || [ "${NUAGE_STORM_LATCH}" = "TRUE" ]; then
  [ -f /tmp/ace777_genesis_runtime.txt ] || fail "genesis runtime STORM absent"
  grep -q 'NUAGE_STORM_LATCH' /tmp/ace777_genesis_runtime.txt || fail "STORM_LATCH non patché dans runtime"
  grep -q 'storm_bypass=1' /tmp/ace777_genesis_runtime.txt || fail "bypass storm_bypass absent"
  grep -q 'storm_latch.ts' /tmp/ace777_genesis_runtime.txt || fail "storm_latch.ts writer absent"
  # Champion disque intact
  _md5_disk="$(md5 -q "$ROOT/genesis_manifest.txt")"
  [[ "$_md5_disk" == 01c38510* ]] || fail "champion disque altéré"
  grep -q 'NUAGE_STORM_LATCH' "$ROOT/genesis_manifest.txt" && fail "STORM ne doit PAS être dans genesis disque"
fi
if [ "${NUAGE_STORM_SCOUT_HOLD}" = "1" ] || [ "${NUAGE_STORM_SCOUT_HOLD}" = "TRUE" ]; then
  [ -f /tmp/ace777_genesis_runtime.txt ] || fail "genesis runtime STORM_HOLD absent"
  grep -q 'STORM_HOLD_K3v3' /tmp/ace777_genesis_runtime.txt || fail "STORM_HOLD K3v3 marker absent"
  grep -q 'storm_hold_latched' /tmp/ace777_genesis_runtime.txt || fail "STORM_HOLD K3v3 latch absent"
  grep -q 'duo_is_scout || duo_is_hunter' /tmp/ace777_genesis_runtime.txt || fail "STORM_HOLD hunter non inclus"
  _md5_disk="$(md5 -q "$ROOT/genesis_manifest.txt")"
  [[ "$_md5_disk" == 01c38510* ]] || fail "champion disque altéré"
  grep -q 'storm_hold_arm' "$ROOT/genesis_manifest.txt" && fail "STORM_HOLD ne doit PAS être dans genesis disque"
fi
# set -e fix toujours présent dans runtime
[ -f /tmp/ace777_genesis_runtime.txt ] || fail "genesis runtime absent"
grep -q 'FIX set -e: un test faux' /tmp/ace777_genesis_runtime.txt || fail "fix set -e post_delta absent"
grep -q 'FIX set -e: un test faux' "$ROOT/genesis_manifest.txt" && fail "fix set -e ne doit PAS être dans genesis disque"
if [ "${NUAGE_STORM_HUNTER}" = "1" ] || [ "${NUAGE_STORM_HUNTER}" = "TRUE" ]; then
  grep -q 'STORM_HUNTER_K2v2' /tmp/ace777_genesis_runtime.txt || fail "STORM_HUNTER K2v2 marker absent"
  grep -q 'duo_mode_note="storm"' /tmp/ace777_genesis_runtime.txt || fail "STORM_HUNTER mode storm absent"
  grep -q 'duo_reason="storm_live"' /tmp/ace777_genesis_runtime.txt || fail "STORM_HUNTER storm_live absent"
  grep -q 'STORM_HUNTER' /tmp/ace777_genesis_runtime.txt || fail "STORM_HUNTER log tag absent"
  grep -q 'export NUAGE_STORM_HUNTER=' "$LAUNCHER" || fail "STORM env export absent launcher"
  _md5_disk="$(md5 -q "$ROOT/genesis_manifest.txt")"
  [[ "$_md5_disk" == 01c38510* ]] || fail "champion disque altéré"
  grep -q 'duo_mode_note="storm"' "$ROOT/genesis_manifest.txt" && fail "STORM_HUNTER ne doit PAS être dans genesis disque"
fi
echo "launcher /tmp = USINE + wait-timer + duo + bidir + storm OK (cksum=$(cksum "$LAUNCHER" | awk '{print $1" "$2}'))"

# Copie durable projet (même contenu)
cp -f "$LAUNCHER" "$ROOT/launch_vide_froid_4h_binance_NUAGE_TIMER_WAIT.sh"
chmod +x "$ROOT/launch_vide_froid_4h_binance_NUAGE_TIMER_WAIT.sh"

# 5) Fortress mince
_fline="$(wc -l < "$ROOT/launch_test_master_base_v8_6_fortress.sh" | tr -d ' ')"
[ "$_fline" -lt 200 ] || fail "fortress anormalement gros ($_fline lignes)"
grep -q 'LAUNCH_V85_SCRIPT' "$ROOT/launch_test_master_base_v8_6_fortress.sh" || fail "fortress sans LAUNCH_V85_SCRIPT"

# 6) Sterile soft
if [ -f runs/timer.pid ]; then
  kill "$(tr -d ' \n\r' < runs/timer.pid)" 2>/dev/null || true
fi
rm -f STOP STOP_ALPHA STOP_BETA runs/STOP_REASON.txt runs/LAST_STOP_REASON.txt
unset ALPHA_RAMP_MODE || true

# 7) Preflight
./scripts/preflight_total_365j.sh

# 7b) A2 — météo IRM (lecture CSV only, n'altère rien)
export RUN_DURATION="$DURATION"
export TEST_TAG_OVERRIDE="$TAG"
_irm_csv="$ROOT/runs/${TAG}_BETA_X5.csv"
echo "=== IRM (proxy tension — lecture seule, hors moteur) ==="
if [ -x "$ROOT/scripts/irm_tension.rb" ] || [ -f "$ROOT/scripts/irm_tension.rb" ]; then
  ruby "$ROOT/scripts/irm_tension.rb" boot "$_irm_csv" 50 || echo "IRM météo: indisponible (non bloquant)"
else
  echo "IRM météo: script absent — skip"
fi

# 7c) B2 Engle adapt — LOG ONLY (ENGLE_ADAPT=0 défaut = usine pure)
#     ENGLE_ADAPT=log → écrit runs/engle_adapt_posture.json, applied=false toujours
export ENGLE_ADAPT="${ENGLE_ADAPT:-0}"
echo "=== ENGLE_ADAPT (B2 log-only, hors moteur) ENGLE_ADAPT=${ENGLE_ADAPT} ==="
if [ -f "$ROOT/scripts/engle_adapt.rb" ]; then
  ruby "$ROOT/scripts/engle_adapt.rb" boot "$_irm_csv" 50 || echo "ENGLE_ADAPT: indisponible (non bloquant)"
else
  echo "ENGLE_ADAPT: script absent — skip"
fi

# 8) Launch
echo "=== BOOT — vérifie: INDEX SYNC: OFF + attente timer ==="
exec "$LAUNCHER" --duration "$DURATION"

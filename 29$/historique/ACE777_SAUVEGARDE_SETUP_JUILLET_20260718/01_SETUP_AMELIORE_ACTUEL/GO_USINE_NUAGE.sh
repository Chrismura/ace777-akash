#!/usr/bin/env bash
# =============================================================================
# ACE777 — LANCEMENT USINE + PATCH MINIMAL wait-timer
#
# 1) Restaure snapshot V2.2.1 (INDEX SYNC: OFF) — cksum usine 812033996 22672
# 2) Applique UNIQUEMENT le correctif:
#      wait wrappers → wait "$PID_TIMER"
#    (évite fin précoce après relance watchdog ALPHA)
# 3) A2 léger: affiche IRM météo (scripts/irm_tension.rb) — LECTURE SEULE,
#    zéro impact moteur / pas de SKIP live.
# Champion disque 37fca367 — JAMAIS modifié.
#
# Usage:
#   ./GO_USINE_NUAGE.sh              # 4h
#   ./GO_USINE_NUAGE.sh 08:00:00     # 8h
#
# Au boot tu dois voir:
#   INDEX SYNC: OFF
#   IRM météo (proxy tension, …)
#   NUAGE_V2.2: attente timer … — pas de fin précoce wrapper
# =============================================================================
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

SNAP="$ROOT/29\$/historique/ACE777_SAUVEGARDE_ULTIME_V3.5/snapshots/launch_vide_froid_4h_binance_NUAGE_V2.2.1.sh"
LAUNCHER="/tmp/launch_vide_froid_4h_binance_NUAGE.sh"
EXPECT_CKSUM_USINE="812033996 22672"
EXPECT_MD5_PREFIX="37fca367"
DURATION="${1:-04:00:00}"
TAG="${2:-NUAGE_PROD_4H}"

fail() { echo "FAIL: $*" >&2; exit 1; }

echo "=== GO_USINE_NUAGE — usine + wait-timer only ==="
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
touch STOP_ALPHA STOP_BETA 2>/dev/null || true
sleep 2

kill \"${PID_SEMANTIC_WATCHDOG:-}\" \"${PID_WATCHDOG:-}\" 2>/dev/null || true
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

# 4) Vérifs post-patch
grep -q 'INDEX SYNC: OFF' "$LAUNCHER" || fail "INDEX SYNC OFF perdu"
grep -q 'attente timer' "$LAUNCHER" || fail "ligne attente timer absente"
grep -q 'wait "$PID_TIMER"' "$LAUNCHER" || fail "wait PID_TIMER absent"
grep -q 'wait "$PID_BETA_WRAPPER"' "$LAUNCHER" && fail "wait BETA wrapper encore présent"
grep -q 'wait "$PID_ALPHA_WRAPPER"' "$LAUNCHER" && fail "wait ALPHA wrapper encore présent"
echo "launcher /tmp = USINE + wait-timer OK (cksum=$(cksum "$LAUNCHER" | awk '{print $1" "$2}'))"

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
rm -f STOP STOP_ALPHA STOP_BETA
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

# 8) Launch
echo "=== BOOT — vérifie: INDEX SYNC: OFF + attente timer ==="
exec "$LAUNCHER" --duration "$DURATION"

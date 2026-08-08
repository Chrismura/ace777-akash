#!/usr/bin/env bash
# Test BOOT 35s — vérifie que le lanceur NUAGE ne se suicide pas
# Usage: ./scripts/verif_boot_nuage.sh
# Tue le run après test. Ne pas lancer si un run est déjà actif.
set -uo pipefail
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

BOOT_SEC="${NUAGE_BOOT_TEST_SEC:-35}"
TAG="NUAGE_BOOTTEST_$(date -u +%H%M)Z"
LOG="/tmp/nuage_boottest_$$.log"
FAIL=0

echo "=== VERIF BOOT NUAGE (${BOOT_SEC}s) — début ==="

if ! ./scripts/verif_sterilite.sh --pre-run; then
  echo "FAIL: pas stérile avant boot test"
  exit 1
fi

rm -f STOP STOP_ALPHA STOP_BETA
rm -rf /tmp/ace777_ram_exchange && mkdir -p /tmp/ace777_ram_exchange
rm -f /tmp/alpha_heartbeat.txt

unset ALPHA_RAMP_MODE
export RUN_DURATION="00:15:00"
export TEST_TAG_OVERRIDE="$TAG"

echo "TAG=$TAG — lancement boot test..."
/tmp/launch_vide_froid_4h_binance_NUAGE.sh --duration 00:15:00 >"$LOG" 2>&1 &
_launcher=$!
echo "launcher_pid=$_launcher"

sleep 5
if ! kill -0 "$_launcher" 2>/dev/null; then
  echo "FAIL: lanceur mort avant 5s (auto-suicide?)"
  echo "--- log ---"
  tail -30 "$LOG" 2>/dev/null || true
  FAIL=1
else
  echo "OK: lanceur vivant à t+5s"
fi

sleep $((BOOT_SEC - 5))

if ! kill -0 "$_launcher" 2>/dev/null; then
  echo "FAIL: lanceur mort avant t+${BOOT_SEC}s"
  tail -40 "$LOG" 2>/dev/null || true
  FAIL=1
else
  echo "OK: lanceur vivant à t+${BOOT_SEC}s"
fi

if [ ! -f runs/master.pid ]; then
  echo "FAIL: runs/master.pid absent à t+${BOOT_SEC}s"
  FAIL=1
else
  echo "OK: master.pid=$(cat runs/master.pid 2>/dev/null)"
fi

_cnt="$(pgrep -fl 'ace777|NUAGE|bash -s|tail.*NUAGE' 2>/dev/null | wc -l | tr -d ' ')"
_tail="$(pgrep -fl 'tail -n 0 -F.*NUAGE' 2>/dev/null | wc -l | tr -d ' ')"
_bashs="$(pgrep -fl 'bash -s' 2>/dev/null | grep -Ei 'ace777|genesis|NUAGE|/tmp/ace777_launch' | wc -l | tr -d ' ')"
# Subshells macOS peuvent apparaître comme bash -s — seuil boot: max 3 (2 oiseaux + marge démarrage)
_bashs_max="${NUAGE_BOOT_BASH_S_MAX:-3}"
echo "PROCESS: total=${_cnt} tail=${_tail} bash_s=${_bashs}"
if [ "${_tail:-0}" -gt 2 ]; then
  echo "FAIL: trop de tail (${_tail} > 2)"
  pgrep -fl 'tail.*NUAGE' 2>/dev/null || true
  FAIL=1
fi
if [ "${_bashs:-0}" -gt "${_bashs_max}" ]; then
  echo "FAIL: trop de bash -s ACE777 (${_bashs} > ${_bashs_max})"
  pgrep -fl 'bash -s' 2>/dev/null | grep -Ei 'ace777|genesis|NUAGE|/tmp/ace777_launch' || true
  FAIL=1
fi
_proc_max="${NUAGE_BOOT_PROC_MAX:-25}"
if [ "${_cnt:-0}" -gt "${_proc_max}" ]; then
  echo "FAIL: trop de process ACE777 (${_cnt} > ${_proc_max})"
  pgrep -fl 'ace777|NUAGE' 2>/dev/null || true
  FAIL=1
fi

echo "--- fin log boot (dernières lignes) ---"
tail -15 "$LOG" 2>/dev/null || true

echo "=== arrêt boot test ==="
./scripts/purge_vierge_usine.sh >/tmp/nuage_boottest_purge_$$.log 2>&1 || true
kill -9 "$_launcher" 2>/dev/null || true
pkill -9 -P "$_launcher" 2>/dev/null || true
sleep 2

for i in 1 2 3; do
  echo "--- post-stérilité $i/3 ---"
  ./scripts/verif_sterilite.sh --pre-run || FAIL=1
done

rm -f "$LOG"
echo "=== VERIF BOOT NUAGE — fin ==="
if [ "$FAIL" -eq 0 ]; then
  echo "BOOT=OK"
  exit 0
fi
echo "BOOT=NOK"
exit 1

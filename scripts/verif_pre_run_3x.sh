#!/usr/bin/env bash
# Pre-run triple vérification — exit 0 = GO | exit 1 = STOP
# Phase PRE uniquement (pas de lancement). BOOT test séparé: verif_boot_nuage.sh
set -uo pipefail
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Champion scellé : 98c80b5c (9fe9f105 sans barrière + FIX-SCOUT) + trap ERR
# diagnostic (14/08, famille 6/6 Q2=a) + safe_call anti-mort (14/08 SPEC v3) = d6977337… Re-scellé 14/08.
CHAMPION_MD5="d6977337a13e14c7867df6a832467d36"
FAIL=0

echo "=== VERIF PRE-RUN 3× — début ==="

for i in 1 2 3; do
  echo "--- stérilité $i/3 ---"
  if ! ./scripts/verif_sterilite.sh --pre-run; then
    echo "FAIL: stérilité $i/3"
    FAIL=1
  fi
done

echo "--- champion md5 ---"
_actual="$(md5 -q genesis_manifest.txt 2>/dev/null || md5sum genesis_manifest.txt 2>/dev/null | awk '{print $1}')"
if [ "$_actual" != "$CHAMPION_MD5" ]; then
  echo "FAIL: genesis md5=$_actual attendu=$CHAMPION_MD5"
  FAIL=1
else
  echo "OK: genesis md5=$CHAMPION_MD5"
fi

echo "--- STOP files ---"
for f in STOP STOP_ALPHA STOP_BETA; do
  if [ ! -f "$f" ]; then
    echo "FAIL: manquant $f"
    FAIL=1
  fi
done
[ "$FAIL" -eq 0 ] && echo "OK: STOP STOP_ALPHA STOP_BETA"

echo "--- master.pid ---"
if [ -f runs/master.pid ]; then
  echo "FAIL: runs/master.pid existe ($(cat runs/master.pid))"
  FAIL=1
else
  echo "OK: pas de master.pid"
fi

echo "--- RAM vierge ---"
if [ -f /tmp/alpha_heartbeat.txt ]; then
  echo "FAIL: /tmp/alpha_heartbeat.txt existe"
  FAIL=1
fi
_ram_left="$(find /tmp/ace777_ram_exchange -type f 2>/dev/null | wc -l | tr -d ' ')"
if [ "${_ram_left:-0}" -gt 0 ]; then
  echo "WARN: RAM exchange contient ${_ram_left} fichier(s) — stale possible"
  find /tmp/ace777_ram_exchange -type f 2>/dev/null || true
fi
[ "$FAIL" -eq 0 ] && [ "${_ram_left:-0}" -eq 0 ] && echo "OK: RAM vide"

echo "--- enveloppe NUAGE ---"
if [ ! -x /tmp/launch_vide_froid_4h_binance_NUAGE.sh ]; then
  echo "FAIL: /tmp/launch_vide_froid_4h_binance_NUAGE.sh absent ou non exécutable"
  FAIL=1
elif grep -q 'stop_ace777_hard' /tmp/launch_vide_froid_4h_binance_NUAGE.sh && \
     grep -A2 'nuage_purge_totale' /tmp/launch_vide_froid_4h_binance_NUAGE.sh | grep -q 'stop_ace777_hard'; then
  echo "FAIL: enveloppe contient stop_ace777_hard dans purge (auto-suicide)"
  FAIL=1
else
  _ver="$(grep 'ACE777_NUAGE_VERSION=' /tmp/launch_vide_froid_4h_binance_NUAGE.sh | head -1 || true)"
  echo "OK: enveloppe présente ${_ver}"
fi

echo "=== VERIF PRE-RUN 3× — fin ==="
if [ "$FAIL" -eq 0 ]; then
  echo "PREFLIGHT=OK"
  exit 0
fi
echo "PREFLIGHT=NOK"
exit 1

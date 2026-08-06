#!/usr/bin/env bash
# Check indicateurs cockpit — fait partie de l’hygiène (zone test).
# Ne lance PAS ACE/Hulk. Refresh thermo + mission feed (lecture).
set -uo pipefail
ROOT="/Users/christophe/ace777-test-day1"
WS="$ROOT/Index_Maison"
PY=/usr/bin/python3
FAIL=0

echo "=== COCKPIT HYGIÈNE (indicateurs) ==="

echo
echo "1) Thermo free (Binance public)"
if ! "$PY" "$WS/scripts/thermo_quotidien_free.py"; then
  echo "THERMO=NOK"
  FAIL=1
else
  echo "THERMO=OK"
fi

echo
echo "2) Mission feed (CSV / Hulk / thermo → mission.json)"
if ! "$PY" "$WS/scripts/cockpit_mission_feed.py"; then
  echo "MISSION_FEED=NOK"
  FAIL=1
else
  echo "MISSION_FEED=OK"
fi

echo
echo "3) Pont Cortana :17777"
BRIDGE_OK=0
if curl -sS --max-time 2 "http://127.0.0.1:17777/status" >/tmp/ace777_cockpit_bridge_status.json 2>/dev/null; then
  BRIDGE_OK=1
  echo "BRIDGE=OK"
  cat /tmp/ace777_cockpit_bridge_status.json
  echo
else
  echo "BRIDGE=OFF — à lancer pour feed live + voix :"
  echo "  python3 $WS/scripts/cortana_cockpit_bridge.py"
  FAIL=1
fi

echo
echo "4) Indicateurs clés (mission.json + live.json)"
"$PY" - <<'PY'
import json, sys
from pathlib import Path
ws = Path("/Users/christophe/ace777-test-day1/Index_Maison")
live = json.loads((ws / "thermo/live.json").read_text())
miss = json.loads((ws / "cockpit/mission.json").read_text())
th = miss.get("thermo") or {}
fail = 0

def need(label, ok):
    global fail
    print(f"  {'OK' if ok else 'NOK'}  {label}")
    if not ok:
        fail = 1

need(f"live.funding={live.get('funding')}", live.get("funding") is not None)
need(f"live.oi={live.get('oi')}", live.get("oi") is not None)
need(f"live.fearGreed={live.get('fearGreed')}", live.get("fearGreed") is not None)
need(f"live.score={live.get('score')} climate={live.get('climate')}", live.get("score") is not None)
need(f"mission.run={miss.get('run')}", bool(miss.get("run")))
need(f"mission.comboPnl={miss.get('comboPnl')}", miss.get("comboPnl") is not None)
inds = th.get("indicators") or live.get("indicators") or {}
need(f"thermo.indicators n={len(inds)}", len(inds) >= 5)
# LIQ/ETF souvent n/d en free — WARN seulement
liq = th.get("liq24Usd", live.get("liq24Usd"))
etf = (th.get("etf") or live.get("etf") or {})
print(f"  WARN  LIQ/ETF free flaky — liq={liq} etf_btc={etf.get('btc')}")
sys.exit(fail)
PY
IND_RC=$?
if [[ "$IND_RC" -ne 0 ]]; then
  FAIL=1
  echo "INDICATEURS=NOK"
else
  echo "INDICATEURS=OK"
fi

echo
if [[ "$FAIL" -eq 0 ]]; then
  echo "COCKPIT_HYGIENE=OK"
else
  echo "COCKPIT_HYGIENE=NOK (bridge OFF ou indicateurs manquants — corriger avant lecture run)"
fi
exit "$FAIL"

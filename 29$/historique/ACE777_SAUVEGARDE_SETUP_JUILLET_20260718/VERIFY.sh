#!/usr/bin/env bash
# Vérifie intégrité du coffre + cohérence avec fichiers live critiques
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/../../.." && pwd)"
# ROOT = ace777-test-day1 (HERE=.../29$/historique/COFFRE → ../../.. = projet)
# From COFFRE: .. = historique, ../.. = 29$, ../../.. = ROOT — yes

ok=0
fail=0
check() {
  local label="$1" expect="$2" file="$3"
  if [ ! -f "$file" ]; then
    echo "FAIL missing: $file ($label)"
    fail=$((fail+1))
    return
  fi
  local got
  got="$(cksum "$file" | awk '{print $1" "$2}')"
  if [ "$got" = "$expect" ]; then
    echo "OK  $label  $got"
    ok=$((ok+1))
  else
    echo "FAIL $label  got=$got expect=$expect  file=$file"
    fail=$((fail+1))
  fi
}
check_md5() {
  local label="$1" expect="$2" file="$3"
  if [ ! -f "$file" ] && [ ! -e "$file" ]; then
    echo "FAIL missing: $file ($label)"
    fail=$((fail+1))
    return
  fi
  local got
  got="$(md5 -q "$file")"
  if [ "$got" = "$expect" ]; then
    echo "OK  $label  $got"
    ok=$((ok+1))
  else
    echo "FAIL $label  got=$got expect=$expect"
    fail=$((fail+1))
  fi
}

echo "=== VERIFY coffre SETUP JUILLET 20260718 ==="
echo "HERE=$HERE"
echo "ROOT=$ROOT"

USINE_EXPECT="812033996 22672"
CHAMP="37fca36712d49aa8b97890c5cad5f2e6"

check "original_coffre" "$USINE_EXPECT" "$HERE/00_ORIGINAL_USINE/launch_vide_froid_4h_binance_NUAGE_V2.2.1.sh"
check "original_live_V3.5" "$USINE_EXPECT" "$ROOT/29\$/historique/ACE777_SAUVEGARDE_ULTIME_V3.5/snapshots/launch_vide_froid_4h_binance_NUAGE_V2.2.1.sh"
check_md5 "champion_live" "$CHAMP" "$ROOT/genesis_manifest.txt"
check_md5 "champion_coffre" "$CHAMP" "$HERE/03_CHAMPION_CERTIFIE/LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt"

# coffre vs live (doivent matcher pour fichiers setup)
echo "--- coffre vs live (byte) ---"
while IFS= read -r rel; do
  a="$HERE/01_SETUP_AMELIORE_ACTUEL/$rel"
  # map cursor_rules → .cursor/rules
  if [[ "$rel" == cursor_rules/* ]]; then
    b="$ROOT/.cursor/rules/$(basename "$rel")"
  else
    b="$ROOT/$rel"
  fi
  if [ ! -f "$a" ]; then
    echo "FAIL coffre missing $rel"; fail=$((fail+1)); continue
  fi
  if [ ! -f "$b" ]; then
    echo "WARN live missing $rel (coffre OK — restaurer depuis coffre si besoin)"
    continue
  fi
  ca=$(cksum "$a" | awk '{print $1" "$2}')
  cb=$(cksum "$b" | awk '{print $1" "$2}')
  if [ "$ca" = "$cb" ]; then
    echo "OK  match $rel"
    ok=$((ok+1))
  else
    echo "DIFF $rel  coffre=$ca live=$cb"
    fail=$((fail+1))
  fi
done <<'RELS'
GO_USINE_NUAGE.sh
launch_vide_froid_4h_binance_NUAGE_TIMER_WAIT.sh
scripts/hygiene_mac_ram.sh
scripts/irm_tension.rb
scripts/swarm_telemetry.rb
scripts/verif_sterilite.sh
scripts/generate_pnl_report.rb
scripts/update_state_md.sh
cursor_rules/ace777-run-test-protocol.mdc
RELS

echo "=== RESULT ok=$ok fail=$fail ==="
[ "$fail" -eq 0 ] && echo "INTEGRITE=OK" && exit 0
echo "INTEGRITE=NOK"
exit 1

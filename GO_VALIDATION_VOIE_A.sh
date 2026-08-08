#!/usr/bin/env bash
# =============================================================================
# GO VALIDATION VOIE A — Pack A (pattern strict) puis Pack B (témoin)
# Paper/testnet via V8.5 IMPACT. Champion genesis intact.
#
# Usage:
#   ./GO_VALIDATION_VOIE_A.sh A          # 4h pack pattern
#   ./GO_VALIDATION_VOIE_A.sh B          # 4h témoin (après A)
#   ./GO_VALIDATION_VOIE_A.sh A 02:00:00 # durée custom
#   ./GO_VALIDATION_VOIE_A.sh A 04:00:00 P2  # 2e passe (tag …_P2)
# =============================================================================
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

PACK="${1:-A}"
DURATION="${2:-04:00:00}"
PASS_LABEL="${3:-}"
case "$DURATION" in
  *:*:*) ;;
  *) echo "Durée attendue HH:MM:SS (ex. 04:00:00)"; exit 1 ;;
esac
# secondes
DUR_SEC="$(ruby -e 'h,m,s=ARGV[0].split(":").map(&:to_i); puts h*3600+m*60+s' -- "$DURATION")"

mkdir -p runs Index_Maison/logs
SCORE="Index_Maison/logs/validation_pattern_voie_A.csv"
if [ ! -f "$SCORE" ]; then
  echo "ts_utc,pack,tag,n_fills_beta,n_fills_alpha,n_fills,pnl_beta,pnl_alpha,pnl_total,max_dd_note,bruit_pct_note,skip_note,verdict" > "$SCORE"
fi

export BINANCE_MODE="${BINANCE_MODE:-testnet}"
export RUN_SEC_OVERRIDE="$DUR_SEC"
export ACE777_CONFIG_NAME="VALIDATION_VOIE_A"
export ACE777_CONFIG_VERSION="pack_${PACK}${PASS_LABEL:+_$PASS_LABEL}"

if [ "$PACK" = "A" ] || [ "$PACK" = "a" ]; then
  TAG="VALIDATION_VOIE_A_PACK_A"
  [ -n "$PASS_LABEL" ] && TAG="${TAG}_${PASS_LABEL}"
  export TEST_TAG_OVERRIDE="$TAG"
  # Pack PATTERN (protocole)
  export MOMENTUM_THRESHOLD="0.96"
  export VACUUM_TENSION_THRESHOLD_BETA="0.85"
  export VACUUM_TENSION_THRESHOLD_ALPHA="0.85"
  export VAL_WALL_DROP="6.5"
  export VAL_VOID_LOCK="TRUE"
  export VAL_MASS_NOTE="1.618"
  echo "=== PACK A (PATTERN) radar=0.85 MOM=0.96 wall=6.5% void=ON tag=$TAG ==="
elif [ "$PACK" = "B" ] || [ "$PACK" = "b" ]; then
  TAG="VALIDATION_VOIE_A_PACK_B"
  [ -n "$PASS_LABEL" ] && TAG="${TAG}_${PASS_LABEL}"
  export TEST_TAG_OVERRIDE="$TAG"
  # Pack TÉMOIN (lâche)
  export MOMENTUM_THRESHOLD="0.70"
  export VACUUM_TENSION_THRESHOLD_BETA="0.70"
  export VACUUM_TENSION_THRESHOLD_ALPHA="0.70"
  export VAL_WALL_DROP="16"
  export VAL_VOID_LOCK="FALSE"
  export VAL_MASS_NOTE="1.0"
  echo "=== PACK B (TÉMOIN) radar=0.70 MOM=0.70 wall=16% void=OFF ==="
else
  echo "Pack doit être A ou B"; exit 1
fi

# Lanceur temp à la RACINE (dirname = ROOT → scripts/ OK). Champion non touché.
LAUNCH_TMP="$ROOT/_launch_validation_voie_a_${PACK}.sh"
cp "$ROOT/launch_test_master_base_v8_5_impact.sh" "$LAUNCH_TMP"
# Injecter wall + void (Pack A = 6.5/TRUE · Pack B = 16/FALSE)
perl -i -pe "s/IMPULSE_RESONANCE_WALL_DROP_PCT=\"6\\.5\"/IMPULSE_RESONANCE_WALL_DROP_PCT=\"${VAL_WALL_DROP}\"/g" "$LAUNCH_TMP"
perl -i -pe "s/V8_VOID_LOCK_ENABLED=\"TRUE\"/V8_VOID_LOCK_ENABLED=\"${VAL_VOID_LOCK}\"/g" "$LAUNCH_TMP"
chmod +x "$LAUNCH_TMP"
# contrôle
grep -E 'WALL_DROP|VOID_LOCK' "$LAUNCH_TMP" | head -6


META="runs/${TAG}_pack_meta.json"
ruby -rjson -e '
  meta = {
    "pack" => ENV["ACE777_CONFIG_VERSION"],
    "tag" => ENV["TEST_TAG_OVERRIDE"],
    "wall_drop_pct" => ENV["VAL_WALL_DROP"],
    "void_lock" => ENV["VAL_VOID_LOCK"],
    "momentum" => ENV["MOMENTUM_THRESHOLD"],
    "vacuum_beta" => ENV["VACUUM_TENSION_THRESHOLD_BETA"],
    "vacuum_alpha" => ENV["VACUUM_TENSION_THRESHOLD_ALPHA"],
    "mass_note" => ENV["VAL_MASS_NOTE"],
    "duration_sec" => ENV["RUN_SEC_OVERRIDE"],
    "protocol" => "PROTOCOLE_VALIDATION_PATTERN_V8",
    "start_utc" => Time.now.utc.strftime("%Y-%m-%dT%H:%M:%SZ")
  }
  File.write(ARGV[0], JSON.pretty_generate(meta))
' "$META"
echo "META=$META"
echo "SCORE=$SCORE (remplir après run)"
echo "Lancement $TAG durée=$DURATION ($DUR_SEC s)…"

exec bash "$LAUNCH_TMP"

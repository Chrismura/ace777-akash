#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   bash ./VALIDATION_ACE777_BASE/TEST_MASTER/finalize_test.sh /path/to/run.csv
#
# Actions:
# 1) Copy CSV to TEST_MASTER/inbox_runs with timestamp suffix
# 2) Generate PnL report in TEST_MASTER/reports

if [ "${1:-}" = "" ]; then
  echo "Usage: bash ./VALIDATION_ACE777_BASE/TEST_MASTER/finalize_test.sh /path/to/run.csv"
  exit 1
fi

SRC_CSV="$1"
if [ ! -f "$SRC_CSV" ]; then
  echo "Erreur: fichier introuvable: $SRC_CSV"
  exit 1
fi

ROOT="/Users/christophe/ace777-test-day1/VALIDATION_ACE777_BASE/TEST_MASTER"
INBOX="$ROOT/inbox_runs"
REPORTS="$ROOT/reports"
mkdir -p "$INBOX" "$REPORTS"

TS_UTC="$(date -u +%Y%m%dT%H%M%SZ)"
SRC_NAME="$(basename "$SRC_CSV")"
BASE_NAME="${SRC_NAME%.csv}"

DEST_CSV="$INBOX/${BASE_NAME}_${TS_UTC}.csv"
REPORT_FILE="$REPORTS/${BASE_NAME}_${TS_UTC}_REPORT.txt"

cp "$SRC_CSV" "$DEST_CSV"

TIME_INFO="$(
  ruby -rtime -e '
    f = ARGV[0]
    lines = File.readlines(f).map(&:strip).reject(&:empty?)
    ts = (lines[1..] || []).map { |l| l.split(",", 2).first }.select { |t| t =~ /^\d{4}-\d{2}-\d{2}T/ }
    if ts.empty?
      puts "na na na"
      exit 0
    end
    t0 = Time.iso8601(ts.first)
    t1 = Time.iso8601(ts.last)
    d = (t1 - t0).to_i
    h = d / 3600
    m = (d % 3600) / 60
    s = d % 60
    puts "#{t0.utc.iso8601} #{t1.utc.iso8601} #{h}h#{m}m#{s}s"
  ' "$DEST_CSV"
)"
set -- $TIME_INFO
START_UTC="${1:-na}"
END_UTC="${2:-na}"
DURATION_HMS="${3:-na}"

METRICS="$(
  awk -F',' '
    FNR==1 { next }
    $4=="FILLED" && $9 ~ /^-?[0-9.]+$/ {
      n++;
      pnl += $9;
      if ($9 > 0) { w++; gp += $9 }
      else if ($9 < 0) { l++; gl += $9 }
    }
    $3=="EXIT_ERROR" { exit_err++ }
    $3=="ENTRY_ERROR" { entry_err++ }
    END {
      pf = (gl < 0) ? gp/(-gl) : 0;
      printf "%.8f %d %d %d %.4f %d %d", pnl, n, w, l, pf, exit_err, entry_err
    }
  ' "$DEST_CSV"
)"
set -- $METRICS
PNL_NET="${1:-0.00000000}"
TRADES="${2:-0}"
WINS="${3:-0}"
LOSSES="${4:-0}"
PROFIT_FACTOR="${5:-0.0000}"
EXIT_ERRORS="${6:-0}"
ENTRY_ERRORS="${7:-0}"

cat > "$REPORT_FILE" <<EOF
ACE777 TEST_MASTER - Rapport fin de run
======================================

Timestamp UTC: $(date -u +%Y-%m-%dT%H:%M:%SZ)
Source originale: $SRC_CSV
Snapshot inbox: $DEST_CSV
Debut run (UTC): $START_UTC
Fin run (UTC): $END_UTC
Duree: $DURATION_HMS

Resultats:
- trades FILLED: $TRADES
- wins: $WINS
- losses: $LOSSES
- pnl_net: $PNL_NET USDT
- profit_factor: $PROFIT_FACTOR
- exit_errors: $EXIT_ERRORS
- entry_errors: $ENTRY_ERRORS
EOF

echo "OK: CSV archive -> $DEST_CSV"
echo "OK: Rapport PnL -> $REPORT_FILE"

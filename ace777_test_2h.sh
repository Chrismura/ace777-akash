#!/bin/zsh
set -u

DURATION=7200
INTERVAL=10
OUT_DIR="${HOME}/ace777_test_outputs"
CSV="${OUT_DIR}/samples.csv"
REPORT="${OUT_DIR}/report.txt"

mkdir -p "$OUT_DIR"

# === Remplace ces commandes par tes vraies sources métriques ===
cmd_p95='echo 320'
cmd_p99='echo 780'
cmd_quorum='echo 7'
cmd_slippage='echo 0.09'
cmd_impact='echo 0.6'
cmd_entropy='echo 0.17'
cmd_mode='echo TURBO'
cmd_lev='echo 8'
cmd_one='echo OK'
# ===============================================================

echo "timestamp,elapsed_s,phase,p95_ms,p99_ms,quorum,slippage_pct,impact_pct,entropy,mode,leverage,one_to_one_ok" > "$CSV"

start=$(date +%s)
end=$((start + DURATION))

phase_of() {
  local e=$1
  if   (( e < 900 )); then echo "warmup"
  elif (( e < 3600 )); then echo "normal"
  elif (( e < 6300 )); then echo "volatility"
  else echo "incident"
  fi
}

echo "Start 2h test..."
while (( $(date +%s) < end )); do
  now=$(date +%s)
  elapsed=$((now - start))
  phase=$(phase_of $elapsed)

  p95=$(eval "$cmd_p95")
  p99=$(eval "$cmd_p99")
  quorum=$(eval "$cmd_quorum")
  slippage=$(eval "$cmd_slippage")
  impact=$(eval "$cmd_impact")
  entropy=$(eval "$cmd_entropy")
  mode=$(eval "$cmd_mode")
  lev=$(eval "$cmd_lev")
  one=$(eval "$cmd_one")

  ts=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
  echo "$ts,$elapsed,$phase,$p95,$p99,$quorum,$slippage,$impact,$entropy,$mode,$lev,$one" >> "$CSV"

  echo "[$elapsed s][$phase] p95=$p95 p99=$p99 q=$quorum slip=$slippage impact=$impact E=$entropy mode=$mode lev=$lev 1:1=$one"
  sleep $INTERVAL
done

# Résumé rapide (awk)
p95_med=$(awk -F, 'NR>1{a[++n]=$4} END{if(n==0){print "NA"; exit} asort(a); if(n%2) print a[(n+1)/2]; else print (a[n/2]+a[n/2+1])/2}' "$CSV")
p99_med=$(awk -F, 'NR>1{a[++n]=$5} END{if(n==0){print "NA"; exit} asort(a); if(n%2) print a[(n+1)/2]; else print (a[n/2]+a[n/2+1])/2}' "$CSV")
q_min=$(awk -F, 'NR>1{if(min=="" || $6<min) min=$6} END{print (min==""?"NA":min)}' "$CSV")
slip_max=$(awk -F, 'NR>1{if(max=="" || $7>max) max=$7} END{print (max==""?"NA":max)}' "$CSV")
impact_max=$(awk -F, 'NR>1{if(max=="" || $8>max) max=$8} END{print (max==""?"NA":max)}' "$CSV")
one_bad=$(awk -F, 'NR>1{v=tolower($12); if(v=="ko"||v=="false"||v=="0"||v=="no") c++} END{print c+0}' "$CSV")

{
  echo "ACE777 2h report"
  echo "p95_median=$p95_med"
  echo "p99_median=$p99_med"
  echo "quorum_min=$q_min"
  echo "slippage_max=$slip_max"
  echo "impact_max=$impact_max"
  echo "one_to_one_violations=$one_bad"
  echo ""
  echo "GO criteria:"
  echo "- p95_median < 400"
  echo "- p99_median < 1000"
  echo "- quorum_min >= 5"
  echo "- slippage_max < 0.1437"
  echo "- impact_max < 1.0"
  echo "- one_to_one_violations = 0"
} > "$REPORT"

echo ""
echo "Done."
echo "CSV: $CSV"
echo "Report: $REPORT"

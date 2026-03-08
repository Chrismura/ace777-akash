#!/bin/zsh
set -u

# ACE777 FINAL 2H PAPER TEST
# - Recalibrage strict toutes les 60s (Lagrange-60)
# - Side LONG/SHORT
# - Filtres risque (slippage/impact/quorum/1:1)

DURATION="${DURATION:-7200}"         # 2h (900 for quick test)
INTERVAL="${INTERVAL:-10}"          # tick logging
OUT_DIR="${OUT_DIR:-${HOME}/ace777_test_outputs_final}"
CSV="${OUT_DIR}/samples.csv"
REPORT="${OUT_DIR}/report.txt"

mkdir -p "$OUT_DIR"

echo "timestamp,elapsed_s,phase,btc_price,entropy,mode,leverage,side,recalibrated,p95_ms,p99_ms,quorum,slippage_pct,impact_pct,one_to_one_ok,trade,pnl_step,cum_pnl" > "$CSV"

start=$(date +%s)
end=$((start + DURATION))

randf() { # randf min max
  awk -v min="$1" -v max="$2" 'BEGIN{srand(); print min+rand()*(max-min)}'
}

phase_of() {
  local e=$1
  if   (( e < 900 )); then echo "warmup"
  elif (( e < 3600 )); then echo "normal"
  elif (( e < 6300 )); then echo "volatility"
  else echo "incident"
  fi
}

mode_from_entropy() {
  local e="$1"
  awk -v E="$e" 'BEGIN{
    if (E <= 0.15) print "NORMAL";
    else if (E <= 0.20) print "TURBO";
    else if (E <= 0.25) print "VENTURI";
    else print "SAFE";
  }'
}

lev_from_mode() {
  case "$1" in
    NORMAL) echo "5" ;;
    TURBO) echo "8" ;;
    VENTURI) echo "3" ;;
    SAFE) echo "1" ;;
    *) echo "1" ;;
  esac
}

btc_price="100000.00"
recal_price_ref="$btc_price"
last_minute_idx="-1"
f_mode="NORMAL"
f_lev="5"
f_side="FLAT"
cum_pnl="0.00"

echo "Start ACE777 FINAL 2h test..."
while (( $(date +%s) < end )); do
  now=$(date +%s)
  elapsed=$((now - start))
  phase=$(phase_of "$elapsed")

  # ---- synthetic market metrics by phase ----
  case "$phase" in
    warmup)
      entropy=$(randf 0.08 0.14)
      p95=$(randf 260 340)
      p99=$(randf 600 900)
      quorum=7
      slippage=$(randf 0.05 0.11)
      impact=$(randf 0.30 0.70)
      px_delta=$(randf -20 20)
      ;;
    normal)
      entropy=$(randf 0.10 0.17)
      p95=$(randf 280 360)
      p99=$(randf 650 950)
      quorum=7
      slippage=$(randf 0.06 0.13)
      impact=$(randf 0.35 0.85)
      px_delta=$(randf -60 60)
      ;;
    volatility)
      entropy=$(randf 0.16 0.23)
      p95=$(randf 300 430)
      p99=$(randf 750 1200)
      quorum=6
      slippage=$(randf 0.08 0.16)
      impact=$(randf 0.50 1.10)
      px_delta=$(randf -180 180)
      ;;
    incident)
      entropy=$(randf 0.22 0.29)
      p95=$(randf 350 520)
      p99=$(randf 900 1600)
      quorum=5
      slippage=$(randf 0.10 0.25)
      impact=$(randf 0.70 1.40)
      px_delta=$(randf -250 250)
      ;;
  esac

  # price walk
  btc_price=$(awk -v p="$btc_price" -v d="$px_delta" 'BEGIN{printf "%.2f", p+d}')

  # 1:1 invariant (rare KO in incident only)
  one="OK"
  if [[ "$phase" == "incident" ]]; then
    r=$((RANDOM % 25))
    if (( r == 0 )); then one="KO"; fi
  fi

  # ---- Lagrange-60 recalibration ----
  minute_idx=$((elapsed / 60))
  recalibrated="NO"
  if (( minute_idx != last_minute_idx )); then
    recalibrated="YES"
    last_minute_idx=$minute_idx

    f_mode=$(mode_from_entropy "$entropy")
    f_lev=$(lev_from_mode "$f_mode")

    momentum=$(awk -v p="$btc_price" -v r="$recal_price_ref" 'BEGIN{print p-r}')
    if awk -v m="$momentum" 'BEGIN{exit !(m>0)}'; then
      f_side="LONG"
    elif awk -v m="$momentum" 'BEGIN{exit !(m<0)}'; then
      f_side="SHORT"
    else
      f_side="FLAT"
    fi

    recal_price_ref="$btc_price"
  fi

  # ---- Paper execution ----
  trade="NO_TRADE"
  pnl_step="0.00"

  ok_slip=$(awk -v s="$slippage" 'BEGIN{print (s < 0.1437) ? 1 : 0}')
  ok_imp=$(awk -v i="$impact" 'BEGIN{print (i < 1.0) ? 1 : 0}')
  ok_quorum=$(awk -v q="$quorum" 'BEGIN{print (q >= 5) ? 1 : 0}')

  if [[ "$f_mode" == "TURBO" || "$f_mode" == "VENTURI" ]]; then
    if [[ "$ok_slip" == "1" && "$ok_imp" == "1" && "$ok_quorum" == "1" && "$one" == "OK" && "$f_side" != "FLAT" ]]; then
      trade="PAPER_TRADE"
      if [[ "$f_mode" == "TURBO" ]]; then
        # better expectancy in TURBO, includes losing trades
        pnl_step=$(awk 'BEGIN{srand(); print sprintf("%.2f", (rand()*6)-2)}')     # -2.00 .. +4.00
      else
        # constrained in VENTURI
        pnl_step=$(awk 'BEGIN{srand(); print sprintf("%.2f", (rand()*3)-1.5)}')   # -1.50 .. +1.50
      fi
    else
      trade="BLOCKED_RISK"
    fi
  fi

  cum_pnl=$(awk -v a="$cum_pnl" -v b="$pnl_step" 'BEGIN{print sprintf("%.2f", a+b)}')

  ts=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
  echo "$ts,$elapsed,$phase,$btc_price,$entropy,$f_mode,$f_lev,$f_side,$recalibrated,$p95,$p99,$quorum,$slippage,$impact,$one,$trade,$pnl_step,$cum_pnl" >> "$CSV"

  printf "[%4ss][%s] px=%s E=%.4f mode=%s lev=%s side=%s recal=%s p95=%.0f p99=%.0f q=%s slip=%.4f impact=%.4f 1:1=%s trade=%s pnl=%s cum=%s\n" \
    "$elapsed" "$phase" "$btc_price" "$entropy" "$f_mode" "$f_lev" "$f_side" "$recalibrated" "$p95" "$p99" "$quorum" "$slippage" "$impact" "$one" "$trade" "$pnl_step" "$cum_pnl"

  sleep "$INTERVAL"
done

# ---- Summary ----
p95_med=$(awk -F, 'NR>1{a[++n]=$10} END{if(n==0){print "NA"; exit} asort(a); if(n%2) print a[(n+1)/2]; else print (a[n/2]+a[n/2+1])/2}' "$CSV")
p99_med=$(awk -F, 'NR>1{a[++n]=$11} END{if(n==0){print "NA"; exit} asort(a); if(n%2) print a[(n+1)/2]; else print (a[n/2]+a[n/2+1])/2}' "$CSV")
q_min=$(awk -F, 'NR>1{if(min=="" || $12<min) min=$12} END{print (min==""?"NA":min)}' "$CSV")
slip_max=$(awk -F, 'NR>1{if(max=="" || $13>max) max=$13} END{print (max==""?"NA":max)}' "$CSV")
impact_max=$(awk -F, 'NR>1{if(max=="" || $14>max) max=$14} END{print (max==""?"NA":max)}' "$CSV")
one_bad=$(awk -F, 'NR>1{v=tolower($15); if(v=="ko"||v=="false"||v=="0"||v=="no") c++} END{print c+0}' "$CSV")
trade_count=$(awk -F, 'NR>1{if($16=="PAPER_TRADE") c++} END{print c+0}' "$CSV")
long_count=$(awk -F, 'NR>1{if($8=="LONG") c++} END{print c+0}' "$CSV")
short_count=$(awk -F, 'NR>1{if($8=="SHORT") c++} END{print c+0}' "$CSV")
final_cum_pnl=$(awk -F, 'NR>1{v=$18} END{print (v==""?"0.00":v)}' "$CSV")

go="YES"
reasons=""
if awk -v v="$p95_med" 'BEGIN{exit !(v!="NA" && v>=400)}'; then go="NO"; reasons="${reasons}\n- p95_median >= 400"; fi
if awk -v v="$p99_med" 'BEGIN{exit !(v!="NA" && v>=1000)}'; then go="NO"; reasons="${reasons}\n- p99_median >= 1000"; fi
if awk -v v="$q_min" 'BEGIN{exit !(v!="NA" && v<5)}'; then go="NO"; reasons="${reasons}\n- quorum_min < 5"; fi
if awk -v v="$slip_max" 'BEGIN{exit !(v!="NA" && v>=0.1437)}'; then go="NO"; reasons="${reasons}\n- slippage_max >= 0.1437"; fi
if awk -v v="$impact_max" 'BEGIN{exit !(v!="NA" && v>=1.0)}'; then go="NO"; reasons="${reasons}\n- impact_max >= 1.0"; fi
if (( one_bad > 0 )); then go="NO"; reasons="${reasons}\n- one_to_one_violations > 0"; fi

{
  echo "ACE777 FINAL 2h report"
  echo "p95_median=$p95_med"
  echo "p99_median=$p99_med"
  echo "quorum_min=$q_min"
  echo "slippage_max=$slip_max"
  echo "impact_max=$impact_max"
  echo "one_to_one_violations=$one_bad"
  echo "paper_trade_count=$trade_count"
  echo "long_count=$long_count"
  echo "short_count=$short_count"
  echo "paper_cum_pnl=$final_cum_pnl"
  echo ""
  echo "GO=$go"
  if [[ "$go" == "NO" ]]; then
    echo "Reasons:${reasons}"
  fi
} > "$REPORT"

echo ""
echo "Done."
echo "CSV: $CSV"
echo "Report: $REPORT"
echo "GO=$go"


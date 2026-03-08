#!/bin/zsh
set -u

# ACE777 TEST - RESONANCE.1437 + MEMOIRE HOLOGRAPHIQUE.1437
# - Recalibrage strict Lagrange-60 (1 decision/minute)
# - Vibration marche Vm sur fenetre glissante 10 min
# - Phase-lock ACE<->BTC
# - Coeur lent (macro bias) + coeur rapide (micro)
# - Garde-fous execution

# ------------------ Config ------------------
DURATION="${DURATION:-7200}"                # 2h default
INTERVAL="${INTERVAL:-10}"                  # tick logging
OUT_DIR="${OUT_DIR:-${HOME}/ace777_test_outputs_res_holo}"
CSV="${OUT_DIR}/samples.csv"
REPORT="${OUT_DIR}/report.txt"
SYMBOL="${SYMBOL:-BTCUSDT}"
REST_BASE_URL="${REST_BASE_URL:-https://testnet.binance.vision}"
WS_BASE_URL="${WS_BASE_URL:-wss://stream.testnet.binance.vision}"
WS_TIMEOUT_SEC="${WS_TIMEOUT_SEC:-8}"
ORDER_NOTIONAL_USDT="${ORDER_NOTIONAL_USDT:-100}"
PROXY_BYPASS_BINANCE="${PROXY_BYPASS_BINANCE:-1}"

MACRO_BIAS="${MACRO_BIAS:-NEUTRAL}"         # BULL | BEAR | NEUTRAL
HOLO_STRICT="${HOLO_STRICT:-1}"             # 1 => blocage direction opposee
FAST_BPS="${FAST_BPS:-25}"                  # short-circuit recalibration threshold
PANIC_BPS="${PANIC_BPS:-60}"                # force SAFE threshold

# Resonance constants
V_ACE_HZ="${V_ACE_HZ:-7.2}"                 # vibration interne ACE
RANGE_USD="${RANGE_USD:-200}"               # reference range calm
SPIKE_USD="${SPIKE_USD:-1500}"              # reference spike
TICK_BASE_USD="${TICK_BASE_USD:-5}"         # baseline tick abs move / 10s
TICK_SPIKE_USD="${TICK_SPIKE_USD:-60}"      # spike tick abs move / 10s

mkdir -p "$OUT_DIR"
if [[ "$PROXY_BYPASS_BINANCE" == "1" ]]; then
  NO_PROXY="localhost,127.0.0.1,::1,testnet.binance.vision,stream.testnet.binance.vision,api.binance.com,api1.binance.com"
  export NO_PROXY no_proxy
  unset HTTP_PROXY HTTPS_PROXY http_proxy https_proxy ALL_PROXY all_proxy
fi
echo "timestamp,elapsed_s,phase,btc_price,entropy,atr_10m,tickvel_10m,vm,mkt_hz,v_ace_hz,phase_lock,macro_bias,mode,lev,quorum_target,t_base_s,k_factor,side,tick_bps,fast_path,recalibrated,p95_ms,p99_ms,quorum_obs,slippage_pct,impact_pct,one_to_one_ok,holo_gate,trade,pnl_step,cum_pnl" > "$CSV"

# ------------------ Helpers ------------------

clip01() { awk -v x="$1" 'BEGIN{if(x<0)x=0; if(x>1)x=1; print x}'; }

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

json_get() {
  local json="$1"
  local key="$2"
  ruby -rjson -e 'j=JSON.parse(STDIN.read) rescue {}; v=j[ARGV[0]]; print(v.nil? ? "" : v)' "$key" <<< "$json"
}

ws_trade_once() {
  local ws_url="$1"
  ruby - "$ws_url" "$WS_TIMEOUT_SEC" <<'RUBY'
require "socket"
require "openssl"
require "securerandom"
require "base64"
require "uri"
require "timeout"

def read_exact(io, n)
  out = +""
  while out.bytesize < n
    out << io.readpartial(n - out.bytesize)
  end
  out
end

url = ARGV[0]
timeout_sec = (ARGV[1] || "8").to_i
u = URI(url)
path = u.path.to_s.empty? ? "/" : u.path
path = "#{path}?#{u.query}" if u.query

Timeout.timeout(timeout_sec) do
  tcp = TCPSocket.new(u.host, u.port || 443)
  ssl = OpenSSL::SSL::SSLSocket.new(tcp, OpenSSL::SSL::SSLContext.new)
  ssl.hostname = u.host if ssl.respond_to?(:hostname=)
  ssl.sync_close = true
  ssl.connect

  key = Base64.strict_encode64(SecureRandom.random_bytes(16))
  req = +"GET #{path} HTTP/1.1\r\n"
  req << "Host: #{u.host}\r\n"
  req << "Upgrade: websocket\r\n"
  req << "Connection: Upgrade\r\n"
  req << "Sec-WebSocket-Key: #{key}\r\n"
  req << "Sec-WebSocket-Version: 13\r\n\r\n"
  ssl.write(req)

  header = +""
  until header.include?("\r\n\r\n")
    header << ssl.readpartial(1024)
    raise "handshake too large" if header.bytesize > 16384
  end
  first = header.lines.first.to_s
  raise "handshake failed: #{first}" unless first.include?("101")

  loop do
    b = read_exact(ssl, 2).bytes
    opcode = b[0] & 0x0f
    masked = (b[1] & 0x80) != 0
    len = b[1] & 0x7f
    len = read_exact(ssl, 2).unpack1("n") if len == 126
    len = read_exact(ssl, 8).unpack1("Q>") if len == 127
    mask = masked ? read_exact(ssl, 4).bytes : nil
    payload = read_exact(ssl, len).bytes
    if masked && mask
      payload = payload.each_with_index.map { |x, i| x ^ mask[i % 4] }
    end
    data = payload.pack("C*")
    if opcode == 1
      puts data
      break
    elsif opcode == 8
      break
    elsif opcode == 9
      # pong
      out = [0x8A]
      if data.bytesize < 126
        out << data.bytesize
        ssl.write(out.pack("C*") + data)
      else
        ssl.write([0x8A, 126].pack("CC") + [data.bytesize].pack("n") + data)
      end
    end
  end
rescue => e
  warn "ws_error=#{e.message}"
  exit 1
end
RUBY
}

# ------------------ Runtime state ------------------
start=$(date +%s)
end=$((start + DURATION))

init_ticker="$(curl -sS "${REST_BASE_URL}/api/v3/ticker/price?symbol=${SYMBOL}" || true)"
btc_price="$(json_get "$init_ticker" "price")"
if [[ -z "$btc_price" ]]; then
  echo "Init error: impossible de lire le prix initial ${SYMBOL} sur ${REST_BASE_URL}" >&2
  exit 1
fi
last_minute_idx="-1"
price_ref_60="$btc_price"
cum_pnl="0.00"

# rolling buffers for 10m @10s = 60 samples
typeset -a dabs_buf
dabs_buf=()

# decision state (frozen for each Lagrange-60 cycle)
f_mode="NORMAL"
f_lev="5"
f_side="FLAT"
f_q_target="7"
f_tbase="60"
f_k="0.70"
f_holo_gate="PASS"
f_phase_lock="0.50"
f_mkt_hz="0.10"
f_vm="0.00"
f_atr="0.00"
f_tickvel="0.00"

echo "Start ACE777 RESONANCE+HOLO test (real WS feed: ${SYMBOL})..."

while (( $(date +%s) < end )); do
  now=$(date +%s)
  elapsed=$((now - start))
  phase=$(phase_of "$elapsed")

  # Real market profile from Binance Testnet WS + REST bookTicker.
  ws_json="$(ws_trade_once "${WS_BASE_URL}/ws/${SYMBOL:l}@trade" || true)"
  px_ws="$(json_get "$ws_json" "p")"
  if [[ -z "$px_ws" ]]; then
    px_ws="$(json_get "$ws_json" "c")"
  fi
  if [[ -z "$px_ws" ]]; then
    # If a tick is missed, keep run alive but mark degraded quality.
    px_ws="$btc_price"
    ws_ok=0
  else
    ws_ok=1
  fi
  prev_price="$btc_price"
  btc_price="$px_ws"
  dabs=$(awk -v a="$btc_price" -v b="$prev_price" 'BEGIN{d=a-b; if(d<0)d=-d; print d}')
  tick_bps=$(awk -v a="$btc_price" -v b="$prev_price" 'BEGIN{if(b==0){print 0}else{d=(a-b); if(d<0)d=-d; print (d/b)*10000}}')
  tick_bps_signed=$(awk -v a="$btc_price" -v b="$prev_price" 'BEGIN{if(b==0){print 0}else{d=(a-b); print (d/b)*10000}}')

  # Latency placeholders from polling cadence and ws health.
  if (( ws_ok == 1 )); then
    p95=$(awk -v i="$INTERVAL" 'BEGIN{print 120 + (i*8)}')
    p99=$(awk -v i="$INTERVAL" 'BEGIN{print 250 + (i*15)}')
  else
    p95="900"
    p99="1500"
  fi

  # Orderbook-based slippage/impact proxies.
  book_json="$(curl -sS "${REST_BASE_URL}/api/v3/ticker/bookTicker?symbol=${SYMBOL}" || true)"
  bid_price="$(json_get "$book_json" "bidPrice")"
  ask_price="$(json_get "$book_json" "askPrice")"
  bid_qty="$(json_get "$book_json" "bidQty")"
  ask_qty="$(json_get "$book_json" "askQty")"
  if [[ -z "$bid_price" || -z "$ask_price" || -z "$bid_qty" || -z "$ask_qty" ]]; then
    slippage="9.9999"
    impact="9.9999"
    quorum_obs=5
  else
    slippage=$(awk -v a="$ask_price" -v b="$bid_price" 'BEGIN{if(a==0){print 9.9999}else{print ((a-b)/a)*100.0}}')
    impact=$(awk -v n="$ORDER_NOTIONAL_USDT" -v a="$ask_price" -v aq="$ask_qty" -v bq="$bid_qty" 'BEGIN{
      if(a<=0 || aq<=0 || bq<=0){print 9.9999; exit}
      q=n/a
      top=aq+bq
      print (q/top)*100.0
    }')
    quorum_obs=7
  fi

  # update 10m rolling abs-delta buffer
  dabs_buf+=("$dabs")
  if (( ${#dabs_buf[@]} > 60 )); then
    dabs_buf=("${dabs_buf[@]:1}")
  fi

  # Entropy proxy from real tick amplitude.
  entropy=$(awk -v b="$tick_bps" 'BEGIN{
    e=0.08 + ((b/80.0) * 0.22)
    if(e<0.08)e=0.08
    if(e>0.30)e=0.30
    print e
  }')

  # 1:1 invariant placeholder (kept explicit for report compatibility).
  one="OK"
  if (( ws_ok == 0 )); then one="KO"; fi

  # ---------- Lagrange-60 recalibration ----------
  minute_idx=$((elapsed / 60))
  fast_path="NO"
  panic_path="NO"
  if awk -v b="$tick_bps" -v p="$PANIC_BPS" 'BEGIN{exit !(b >= p)}'; then
    fast_path="YES"
    panic_path="YES"
  elif awk -v b="$tick_bps" -v f="$FAST_BPS" 'BEGIN{exit !(b >= f)}'; then
    fast_path="YES"
  fi
  recalibrated="NO"
  if (( minute_idx != last_minute_idx )) || [[ "$fast_path" == "YES" ]]; then
    recalibrated="YES"
    if (( minute_idx != last_minute_idx )); then
      last_minute_idx=$minute_idx
    fi

    # ATR_10m approx = avg(abs(delta))
    f_atr=$(printf "%s\n" "${dabs_buf[@]}" | awk '{s+=$1; n++} END{if(n==0) print 0; else print s/n}')
    # Tick velocity approx = ATR_10m / 10s
    f_tickvel=$(awk -v a="$f_atr" 'BEGIN{print a/10.0}')

    # normalize 0..1
    atr_norm=$(awk -v a="$f_atr" -v r="$RANGE_USD" -v s="$SPIKE_USD" 'BEGIN{x=(a-r)/(s-r); if(x<0)x=0; if(x>1)x=1; print x}')
    tv_norm=$(awk -v t="$f_tickvel" -v b="$TICK_BASE_USD" -v sp="$TICK_SPIKE_USD" 'BEGIN{x=(t-b)/(sp-b); if(x<0)x=0; if(x>1)x=1; print x}')

    # Vm and market hz
    f_vm=$(awk -v a="$atr_norm" -v t="$tv_norm" 'BEGIN{print a*t}')
    f_mkt_hz=$(awk -v vm="$f_vm" 'BEGIN{hz=0.1 + (vm*19.9); if(hz<0.1)hz=0.1; if(hz>20)hz=20; print hz}')

    # phase-lock score: 1 - distance/20
    f_phase_lock=$(awk -v mhz="$f_mkt_hz" -v ahz="$V_ACE_HZ" 'BEGIN{d=mhz-ahz; if(d<0)d=-d; s=1-(d/20.0); if(s<0)s=0; if(s>1)s=1; print s}')

    # Base mode from entropy (can be overridden by panic path)
    f_mode=$(mode_from_entropy "$entropy")
    f_lev=$(lev_from_mode "$f_mode")

    # Dynamic resonance tuning (bounded)
    if awk -v hz="$f_mkt_hz" 'BEGIN{exit !(hz <= 6)}'; then
      # Calm/range
      f_tbase="60"
      f_k="0.70"
      f_q_target="7"
    elif awk -v hz="$f_mkt_hz" 'BEGIN{exit !(hz <= 14)}'; then
      # Transitional
      f_tbase="30"
      f_k="0.90"
      f_q_target="6"
    else
      # Spike/action
      f_tbase="15"
      f_k="1.10"
      f_q_target="5"
    fi

    # Rapid heart side from 60s momentum
    mom60=$(awk -v p="$btc_price" -v r="$price_ref_60" 'BEGIN{print p-r}')
    if awk -v m="$mom60" 'BEGIN{exit !(m>0)}'; then
      f_side="LONG"
    elif awk -v m="$mom60" 'BEGIN{exit !(m<0)}'; then
      f_side="SHORT"
    else
      f_side="FLAT"
    fi
    price_ref_60="$btc_price"

    # Holographic memory gate (long-term bias)
    f_holo_gate="PASS"
    if [[ "$HOLO_STRICT" == "1" ]]; then
      if [[ "$MACRO_BIAS" == "BEAR" && "$f_side" == "LONG" ]]; then
        f_holo_gate="BLOCK_LONG_HOLO"
      elif [[ "$MACRO_BIAS" == "BULL" && "$f_side" == "SHORT" ]]; then
        f_holo_gate="BLOCK_SHORT_HOLO"
      fi
    else
      # Soft mode: no hard block, only leverage cap
      if [[ "$MACRO_BIAS" == "BEAR" && "$f_side" == "LONG" ]]; then
        if (( f_lev > 3 )); then f_lev="3"; fi
        f_holo_gate="SOFT_CAP_LONG"
      elif [[ "$MACRO_BIAS" == "BULL" && "$f_side" == "SHORT" ]]; then
        if (( f_lev > 3 )); then f_lev="3"; fi
        f_holo_gate="SOFT_CAP_SHORT"
      fi
    fi

    # Fast interrupt override: lightning -> VENTURI immediately
    if [[ "$fast_path" == "YES" && "$panic_path" == "NO" ]]; then
      f_mode="VENTURI"
      f_lev="3"
      f_q_target="5"
      f_tbase="15"
      f_k="1.00"
      if [[ "$f_holo_gate" == "PASS" ]]; then
        f_holo_gate="FAST_VENTURI"
      fi
    fi

    # Panic override: extreme move -> SAFE immediately
    if [[ "$panic_path" == "YES" ]]; then
      f_mode="SAFE"
      f_lev="1"
      f_side="FLAT"
      f_q_target="7"
      f_tbase="60"
      f_k="0.50"
      f_holo_gate="FAST_PANIC_SAFE"
    fi
  fi

  # ---------- Trade decision ----------
  trade="NO_TRADE"
  pnl_step="0.00"

  ok_slip=$(awk -v s="$slippage" 'BEGIN{print (s < 0.1437) ? 1 : 0}')
  ok_imp=$(awk -v i="$impact" 'BEGIN{print (i < 1.0) ? 1 : 0}')
  ok_quorum=$(awk -v q="$quorum_obs" -v qt="$f_q_target" 'BEGIN{print (q >= qt) ? 1 : 0}')
  ok_phase=$(awk -v p="$f_phase_lock" 'BEGIN{print (p >= 0.45) ? 1 : 0}')
  ok_holo=1
  if [[ "$f_holo_gate" == BLOCK_* ]]; then ok_holo=0; fi

  if [[ "$f_mode" == "TURBO" || "$f_mode" == "VENTURI" ]]; then
    if [[ "$f_side" != "FLAT" && "$ok_slip" == "1" && "$ok_imp" == "1" && "$ok_quorum" == "1" && "$ok_phase" == "1" && "$ok_holo" == "1" && "$one" == "OK" ]]; then
      trade="PAPER_TRADE"
      # Side-aware paper PnL from real signed move between two WS ticks.
      pnl_step=$(awk -v b="$tick_bps_signed" -v n="$ORDER_NOTIONAL_USDT" -v side="$f_side" -v ph="$f_phase_lock" 'BEGIN{
        dir=(side=="LONG") ? 1 : -1
        gross=(b/10000.0)*n*dir
        quality=(ph-0.5)*0.4
        print sprintf("%.2f", gross + quality)
      }')
    else
      trade="BLOCKED_RISK"
    fi
  fi

  cum_pnl=$(awk -v a="$cum_pnl" -v b="$pnl_step" 'BEGIN{print sprintf("%.2f", a+b)}')

  ts=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
  echo "$ts,$elapsed,$phase,$btc_price,$entropy,$f_atr,$f_tickvel,$f_vm,$f_mkt_hz,$V_ACE_HZ,$f_phase_lock,$MACRO_BIAS,$f_mode,$f_lev,$f_q_target,$f_tbase,$f_k,$f_side,$tick_bps,$fast_path,$recalibrated,$p95,$p99,$quorum_obs,$slippage,$impact,$one,$f_holo_gate,$trade,$pnl_step,$cum_pnl" >> "$CSV"

  printf "[%4ss][%s] px=%s E=%.4f Vm=%.4f mHz=%.2f lock=%.2f mode=%s lev=%s side=%s qT=%s tBase=%ss bps=%.1f fast=%s holo=%s recal=%s p95=%.0f p99=%.0f q=%s slip=%.4f impact=%.4f 1:1=%s trade=%s pnl=%s cum=%s\n" \
    "$elapsed" "$phase" "$btc_price" "$entropy" "$f_vm" "$f_mkt_hz" "$f_phase_lock" "$f_mode" "$f_lev" "$f_side" "$f_q_target" "$f_tbase" "$tick_bps" "$fast_path" "$f_holo_gate" "$recalibrated" "$p95" "$p99" "$quorum_obs" "$slippage" "$impact" "$one" "$trade" "$pnl_step" "$cum_pnl"

  sleep "$INTERVAL"
done

# ------------------ Summary ------------------
median_col() {
  local col="$1"
  local n
  n=$(awk -F, -v c="$col" 'NR>1 && $c!="" {n++} END{print n+0}' "$CSV")
  if (( n == 0 )); then
    echo "NA"
    return
  fi
  awk -F, -v c="$col" 'NR>1 && $c!="" {print $c}' "$CSV" | sort -n | awk -v n="$n" '
    {a[NR]=$1}
    END{
      if(n%2==1){print a[(n+1)/2]}
      else{print (a[n/2]+a[n/2+1])/2}
    }'
}

p95_med=$(median_col 22)
p99_med=$(median_col 23)
q_min=$(awk -F, 'NR>1{if(min=="" || $24<min) min=$24} END{print (min==""?"NA":min)}' "$CSV")
slip_max=$(awk -F, 'NR>1{if(max=="" || $25>max) max=$25} END{print (max==""?"NA":max)}' "$CSV")
impact_max=$(awk -F, 'NR>1{if(max=="" || $26>max) max=$26} END{print (max==""?"NA":max)}' "$CSV")
one_bad=$(awk -F, 'NR>1{v=tolower($27); if(v=="ko"||v=="false"||v=="0"||v=="no") c++} END{print c+0}' "$CSV")
trade_count=$(awk -F, 'NR>1{if($29=="PAPER_TRADE") c++} END{print c+0}' "$CSV")
long_count=$(awk -F, 'NR>1{if($18=="LONG") c++} END{print c+0}' "$CSV")
short_count=$(awk -F, 'NR>1{if($18=="SHORT") c++} END{print c+0}' "$CSV")
blocked_count=$(awk -F, 'NR>1{if($29=="BLOCKED_RISK") c++} END{print c+0}' "$CSV")
final_cum_pnl=$(awk -F, 'NR>1{v=$31} END{print (v==""?"0.00":v)}' "$CSV")
avg_lock=$(awk -F, 'NR>1{s+=$11;n++} END{if(n==0) print "0"; else printf "%.4f", s/n}' "$CSV")
fast_count=$(awk -F, 'NR>1{if($20=="YES") c++} END{print c+0}' "$CSV")

go="YES"
reasons=""
if awk -v v="$p95_med" 'BEGIN{exit !(v!="NA" && v>=400)}'; then go="NO"; reasons="${reasons}\n- p95_median >= 400"; fi
if awk -v v="$p99_med" 'BEGIN{exit !(v!="NA" && v>=1000)}'; then go="NO"; reasons="${reasons}\n- p99_median >= 1000"; fi
if awk -v v="$q_min" 'BEGIN{exit !(v!="NA" && v<5)}'; then go="NO"; reasons="${reasons}\n- quorum_min < 5"; fi
if awk -v v="$slip_max" 'BEGIN{exit !(v!="NA" && v>=0.1437)}'; then go="NO"; reasons="${reasons}\n- slippage_max >= 0.1437"; fi
if awk -v v="$impact_max" 'BEGIN{exit !(v!="NA" && v>=1.0)}'; then go="NO"; reasons="${reasons}\n- impact_max >= 1.0"; fi
if (( one_bad > 0 )); then go="NO"; reasons="${reasons}\n- one_to_one_violations > 0"; fi

{
  echo "ACE777 RESONANCE+HOLO report"
  echo "macro_bias=$MACRO_BIAS"
  echo "holo_strict=$HOLO_STRICT"
  echo "p95_median=$p95_med"
  echo "p99_median=$p99_med"
  echo "quorum_min=$q_min"
  echo "slippage_max=$slip_max"
  echo "impact_max=$impact_max"
  echo "one_to_one_violations=$one_bad"
  echo "paper_trade_count=$trade_count"
  echo "blocked_risk_count=$blocked_count"
  echo "fast_path_count=$fast_count"
  echo "long_count=$long_count"
  echo "short_count=$short_count"
  echo "avg_phase_lock=$avg_lock"
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


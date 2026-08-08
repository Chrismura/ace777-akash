#!/usr/bin/env bash
# === SUPERVISEUR ACE777 V9 — régime TREND/CHOP via vortex_control.json ===
set -euo pipefail

cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Auto-détecte le dernier CSV BETA si LOG_BETA absent
if [ -z "${LOG_BETA:-}" ] || [ ! -f "${LOG_BETA}" ]; then
  latest="$(ls -t runs/*_BETA_X5.csv 2>/dev/null | head -1 || true)"
  LOG_BETA="${latest:-runs/MASTER_BASE_V8_5_IMPACT_4H_BETA_X5.csv}"
fi

CONTROL_FILE="${CONTROL_FILE:-runs/vortex_control.json}"
# Fallback modèles : SUPERVISOR_MODEL → LLM_MODEL → qwen2.5-coder:1.5b
MODEL="${SUPERVISOR_MODEL:-${LLM_MODEL:-qwen2.5-coder:1.5b}}"
INTERVAL_SEC="${SUPERVISOR_INTERVAL_SEC:-60}"
TAIL_LINES="${SUPERVISOR_TAIL_LINES:-40}"
OLLAMA_URL="${LLM_OLLAMA_URL:-http://127.0.0.1:11434}"

case "$INTERVAL_SEC" in
  ''|*[!0-9]*) INTERVAL_SEC=60 ;;
esac
[ "$INTERVAL_SEC" -lt 60 ] && INTERVAL_SEC=60

mkdir -p "$(dirname "$CONTROL_FILE")"

echo "=== SUPERVISEUR V9 === model=${MODEL} interval=${INTERVAL_SEC}s"
echo "Log: ${LOG_BETA}"
echo "Control: ${CONTROL_FILE}"

write_control() {
  local json="$1"
  printf '%s\n' "$json" > "${CONTROL_FILE}.tmp"
  mv "${CONTROL_FILE}.tmp" "$CONTROL_FILE"
}

write_fallback() {
  local reason="${1:-fallback}"
  local ts
  ts="$(date -u +%FT%TZ)"
  write_control "{\"mode\":\"CHOP\",\"radar_adj\":0.05,\"mom\":0.95,\"confiance_structure\":0.10,\"message\":\"${reason}\",\"ts\":\"${ts}\"}"
}

# Régime déterministe depuis le CSV (si LLM échoue)
rule_based_regime() {
  local log="$1"
  [ -f "$log" ] || { write_fallback "no_log"; return; }
  ruby -rjson -e '
    path=ARGV[0]
    lines=File.readlines(path).last(40)
    pnls=[]
    lines.each do |ln|
      cols=ln.strip.split(",")
      next if cols.size < 10
      next unless cols[3] == "FILLED"
      pnls << cols[8].to_f
    end
  if pnls.empty?
    mode="CHOP"; adj=0.05; mom=0.95; conf=0.10; msg="rule_no_trades"
  else
    net=pnls.sum
    mode = net > 0 ? "TREND" : "CHOP"
    adj = net > 0 ? -0.05 : 0.05
    mom = mode == "TREND" ? 0.85 : 0.95
    conf = [[pnls.size / 20.0, 1.0].min, 0.1].max
    msg = "rule_pnl_" + format("%.2f", net)
  end
  ts=Time.now.utc.strftime("%Y-%m-%dT%H:%M:%SZ")
  puts JSON.generate({"mode"=>mode,"radar_adj"=>adj,"mom"=>mom,"confiance_structure"=>conf.round(4),"message"=>msg,"ts"=>ts})
  ' "$log"
}

ollama_json_regime() {
  local data="$1"
  local prompt
  prompt="Analyse ces cycles ACE777. Reponds UNIQUEMENT avec un objet JSON valide, sans texte autour.
Format exact: {\"mode\":\"TREND\" ou \"CHOP\",\"radar_adj\":-0.05 ou 0 ou 0.05,\"mom\":0.85 ou 0.90 ou 0.95,\"confiance_structure\":0.0 a 1.0,\"message\":\"court\"}
Data:
${data}"

  local models="${MODEL} ${LLM_MODEL:-} qwen2.5-coder:1.5b qwen2.5:3b"
  for m in $models; do
    [ -z "$m" ] && continue
    local raw
    raw="$(curl -sS --connect-timeout 3 --max-time 25 -X POST "${OLLAMA_URL}/api/generate" \
      -H "Content-Type: application/json" \
      -d "$(ruby -rjson -e 'print JSON.generate(model: ARGV[0], prompt: ARGV[1], stream: false, format: "json")' "$m" "$prompt")" 2>/dev/null || true)"
    [ -z "$raw" ] && continue
    local out
    out="$(printf '%s' "$raw" | ruby -rjson -e '
      begin
        j=JSON.parse(STDIN.read)
        txt=j["response"].to_s
        c=JSON.parse(txt)
        mode=(c["mode"]||"CHOP").to_s.upcase
        mode="CHOP" unless %w[TREND CHOP].include?(mode)
        adj=(Float(c["radar_adj"]) rescue 0.05).clamp(-0.20, 0.20)
        mom=(Float(c["mom"]) rescue (mode=="TREND" ? 0.85 : 0.95))
        conf=(Float(c["confiance_structure"]) rescue 0.5).clamp(0.0, 1.0)
        msg=(c["message"]||"ok").to_s[0,80]
        puts JSON.generate({"mode"=>mode,"radar_adj"=>adj.round(4),"mom"=>mom.round(4),"confiance_structure"=>conf.round(4),"message"=>msg,"ts"=>Time.now.utc.strftime("%Y-%m-%dT%H:%M:%SZ")})
      rescue
      end
    ' 2>/dev/null || true)"
    if [ -n "$out" ]; then
      printf '%s' "$out"
      return 0
    fi
  done
  return 1
}

while true; do
  if [ ! -f "$LOG_BETA" ]; then
    echo "[$(date +%H:%M:%S)] attente log BETA..."
    write_fallback "waiting_log"
    sleep "$INTERVAL_SEC"
    continue
  fi

  DATA="$(tail -n "$TAIL_LINES" "$LOG_BETA" | awk -F',' 'NF>=9 {print "t="$1" pnl="$9" msg="$12}')"
  [ -n "$DATA" ] || DATA="no_data"

  RESP_JSON="$(ollama_json_regime "$DATA" || true)"
  if [ -z "$RESP_JSON" ]; then
    RESP_JSON="$(rule_based_regime "$LOG_BETA")"
    echo "[$(date +%H:%M:%S)] LLM fail -> rule-based $(echo "$RESP_JSON" | ruby -rjson -e 'j=JSON.parse(STDIN.read); print j["message"]')"
  else
    echo "[$(date +%H:%M:%S)] LLM ok $(echo "$RESP_JSON" | ruby -rjson -e 'j=JSON.parse(STDIN.read); print "mode=#{j["mode"]} adj=#{j["radar_adj"]}"' 2>/dev/null || echo ok)"
  fi

  write_control "$RESP_JSON"
  sleep "$INTERVAL_SEC"
done

#!/usr/bin/env bash
# Preflight ACE777 — vérifie config, Binance, Ollama avant un cycle
# Usage: ./scripts/preflight_ace777.sh
# Exit 0 = OK | Exit 1 = bloquant

set -euo pipefail

_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$_root"
errors=0
warnings=0

fail() { echo "PREFLIGHT_ERR: $1" >&2; errors=$((errors + 1)); }
warn() { echo "PREFLIGHT_WARN: $1" >&2; warnings=$((warnings + 1)); }
ok()   { echo "PREFLIGHT_OK: $1"; }

# --- Config ---
if [ -f "./config_active.env" ]; then
  # shellcheck source=scripts/load_config.sh
  source ./scripts/load_config.sh 2>/dev/null || fail "config_active.env illisible"
  ok "config ${ACE777_CONFIG_NAME} v${ACE777_CONFIG_VERSION} BETA=${BUY_USDT_BETA} ALPHA=${BUY_USDT_ALPHA}"
else
  fail "config_active.env introuvable"
fi

# --- Fichiers moteur ---
for f in genesis_manifest.txt radar_gate.rb launch_test_master_base_v8_5_impact.sh; do
  [ -f "$_root/$f" ] || fail "fichier manquant: $f"
done
ok "fichiers moteur présents"

# --- Champion : INTÉGRITÉ CRYPTOGRAPHIQUE (C1 mécanique) ---
# Champion scellé 12/08 = 9fe9f105 (sans barrière) + FIX-SCOUT = md5 98c80b5c...
# + trap ERR diagnostic (14/08) + safe_call anti-mort (14/08 SPEC v3 famille 6/6) = d6977337...
# Re-scellé 14/08 par la famille (6/6 GO AVEC RÉSERVES, Q2=a) — diff vérifié :
# seul ajout = le trap, zéro altération métier.
_champion_attendu="d6977337a13e14c7867df6a832467d36"
_champion_actuel="$(md5 -q genesis_manifest.txt 2>/dev/null || md5sum genesis_manifest.txt 2>/dev/null | awk '{print $1}')"
if [ "$_champion_actuel" != "$_champion_attendu" ]; then
  fail "genesis md5=$_champion_actuel attendu=$_champion_attendu — CHAMPION MODIFIÉ, ne pas lancer"
else
  ok "champion intègre (md5 $_champion_attendu)"
fi

# --- Binance clés ---
_binance_mode="${BINANCE_MODE:-testnet}"
if [ "$_binance_mode" = "live" ]; then
  if [ -f "${HOME}/.binance_live.env" ]; then
    set -a
    # shellcheck source=/dev/null
    source "${HOME}/.binance_live.env"
    set +a
    export BASE_URL="${BASE_URL:-https://fapi.binance.com}"
    ok "clés Binance LIVE chargées"
  else
    fail "~/.binance_live.env introuvable (BINANCE_MODE=live)"
  fi
elif [ -f "${HOME}/.binance_testnet.env" ]; then
  set -a
  # shellcheck source=/dev/null
  source "${HOME}/.binance_testnet.env"
  set +a
  ok "clés Binance testnet chargées"
fi
if [ -z "${BINANCE_API_KEY:-}" ] || [ -z "${BINANCE_API_SECRET:-}" ]; then
  fail "BINANCE_API_KEY ou BINANCE_API_SECRET manquant"
fi

# Ping Binance (preflight uniquement — le moteur live garde timeout 0.2–0.3s)
_ping_url="${WATCHDOG_PING_URL:-}"
if [ -z "$_ping_url" ]; then
  if [ "$_binance_mode" = "live" ]; then
    _ping_url="https://fapi.binance.com/fapi/v1/ping"
  else
    _ping_url="https://testnet.binancefuture.com/fapi/v1/ping"
  fi
fi
ping_resp=""
for _attempt in 1 2 3; do
  ping_resp="$(curl -sS --connect-timeout 1 --max-time 2 "$_ping_url" 2>/dev/null || true)"
  [ "$ping_resp" = "{}" ] && break
  sleep 0.3
done
if [ "$ping_resp" != "{}" ]; then
  fail "Binance unreachable (3 tentatives) mode=${_binance_mode}"
else
  ok "Binance ping (${_binance_mode})"
fi

# --- Positions orphelines (C8 / coupure batterie) ---
# Après une coupure ou un kill -9, une position peut rester ouverte sur le compte.
# Elle bloque la marge -> les entrées échouent (code -2019) -> les unités meurent en
# boucle (Abort leverage error). On refuse de lancer tant que le compte n'est pas à plat.
_ts_ms="$(ruby -e 'puts (Time.now.to_f * 1000).to_i')"
_q_sig="timestamp=${_ts_ms}&recvWindow=5000"
_sig="$(printf '%s' "$_q_sig" | openssl dgst -sha256 -hmac "$BINANCE_API_SECRET" -binary | od -A n -t x1 | tr -d ' \n')"
_pos_base="https://testnet.binancefuture.com"
[ "$_binance_mode" = "live" ] && _pos_base="https://fapi.binance.com"
_pos_resp="$(curl -sS --connect-timeout 2 --max-time 5 -H "X-MBX-APIKEY: $BINANCE_API_KEY" \
  "${_pos_base}/fapi/v2/positionRisk?$_q_sig&signature=$_sig" 2>/dev/null || true)"
_pos_open="$(printf '%s' "$_pos_resp" | ruby -rjson -e '
  begin
    j = JSON.parse(STDIN.read)
    open = j.select { |p| (p["positionAmt"].to_f).abs > 1e-9 }
    open.each { |p| puts "#{p["symbol"]} #{p["positionAmt"]} @ #{p["entryPrice"]} (unPnl #{p["unRealizedProfit"]})" }
    puts "COUNT=#{open.size}"
  rescue
    puts "COUNT=ERR"
  end
')"
_pos_count="$(printf '%s' "$_pos_open" | grep -c '^COUNT=' >/dev/null; printf '%s' "$_pos_open" | sed -n 's/^COUNT=//p')"
if [ "$_pos_count" = "ERR" ] || [ -z "$_pos_count" ]; then
  fail "impossible de lire les positions ($_pos_resp) — vérifier le compte avant de lancer"
elif [ "$_pos_count" -gt 0 ] 2>/dev/null; then
  fail "$_pos_count position(s) orpheline(s) ouverte(s) sur le compte — fermer avant de lancer :"
  printf '%s\n' "$_pos_open" | grep -v '^COUNT=' | sed 's/^/  PREFLIGHT_WARN: /' || true
else
  ok "compte à plat (0 position ouverte)"
fi

# --- Ollama (si LLM gate actif) ---
if [ "${LLM_GATE_ENABLED:-FALSE}" = "TRUE" ]; then
  ollama_url="${LLM_OLLAMA_URL:-http://127.0.0.1:11434}"
  if ! curl -sS --connect-timeout 2 --max-time 3 "${ollama_url}/api/tags" >/dev/null 2>&1; then
    fail "Ollama unreachable (${ollama_url}) — LLM gate fail-closed bloquera tous les trades"
  else
    model="${LLM_MODEL:-qwen2.5-coder:1.5b}"
    has_model="$(curl -sS --connect-timeout 2 --max-time 5 "${ollama_url}/api/tags" 2>/dev/null | \
      ruby -rjson -e 'm=ARGV[0]; j=JSON.parse(STDIN.read) rescue {}; puts((j["models"]||[]).any?{|x| x["name"].to_s.start_with?(m) } ? "yes" : "no")' "$model" 2>/dev/null || echo "no")"
    if [ "$has_model" != "yes" ]; then
      fail "modèle Ollama absent: ${model} (ollama pull requis)"
    else
      ok "Ollama + modèle ${model}"
    fi
  fi
else
  warn "LLM_GATE_ENABLED=FALSE — gate désactivé"
fi

# --- Vortex supervisor (si activé) ---
if [ "${VORTEX_CONTROL_ENABLED:-FALSE}" = "TRUE" ]; then
  sup_pid=""
  if [ "${VORTEX_V2_RADAR_PILOT:-FALSE}" = "TRUE" ]; then
    [ -f runs/supervisor_v9_v2.pid ] && sup_pid="$(cat runs/supervisor_v9_v2.pid 2>/dev/null || true)"
    if [ -n "$sup_pid" ] && kill -0 "$sup_pid" 2>/dev/null; then
      ok "supervisor Vortex v2 running (pid ${sup_pid})"
    elif [ "${VORTEX_SUPERVISOR_AUTO:-FALSE}" = "TRUE" ]; then
      ok "supervisor Vortex v2 auto-attache (démarrage master)"
    else
      warn "VORTEX_V2=ON mais supervisor v2 absent — lancer ./scripts/start_supervisor_v9_v2.sh"
    fi
  else
    [ -f runs/supervisor_v9.pid ] && sup_pid="$(cat runs/supervisor_v9.pid 2>/dev/null || true)"
    if [ -n "$sup_pid" ] && kill -0 "$sup_pid" 2>/dev/null; then
      ok "supervisor V9 running (pid ${sup_pid})"
    else
      warn "VORTEX_CONTROL_ENABLED=TRUE mais supervisor_v9 non détecté — lancer ./scripts/start_supervisor_v9.sh"
    fi
  fi
  if [ -f runs/vortex_control.json ]; then
    msg="$(ruby -rjson -e 'j=JSON.parse(File.read(ARGV[0])) rescue {}; puts j["message"]' runs/vortex_control.json 2>/dev/null || echo "?")"
    if [ "$msg" = "invalid_v9_json" ]; then
      warn "vortex_control.json en fallback invalid_v9_json — relancer supervisor"
    fi
  fi
else
  ok "VORTEX_CONTROL=OFF (vide froid canonique)"
fi

# --- Réserve storm (préchauffage 13/08) ---
# R1 — Budget et réserve présents dans routing.json
if [ -f ~/prise-ia/routing.json ]; then
  vals=$(python3 -c '
import json, sys
try:
    with open(sys.argv[1]) as f:
        j = json.load(f)
    print(j.get("cloud_daily_budget", 0) or 0)
    print(j.get("cloud_daily_reserve", 0) or 0)
except Exception:
    print(0)
    print(0)
' ~/prise-ia/routing.json 2>/dev/null)
  budget=$(printf '%s\n' "$vals" | head -n1)
  reserve=$(printf '%s\n' "$vals" | tail -n1)
  if [ "$budget" != "0" ] && [ -n "$budget" ]; then
    ok "budget calme=$budget"
  else
    warn "budget calme absent ou nul"
  fi
  if [ "$reserve" != "0" ] && [ -n "$reserve" ]; then
    ok "réserve storm=$reserve"
  else
    warn "réserve storm absente — lancer : cd ~/prise-ia && python3 budget_hub.py --apply"
  fi
else
  warn "routing.json absent — impossible de vérifier budget/réserve"
fi

# R2 — Gratuits dynamiques détectés dans providers.json
if [ -f ~/prise-ia/providers.json ]; then
  count=$(python3 -c '
import json, sys
try:
    with open(sys.argv[1]) as f:
        data = json.load(f)
    providers = data if isinstance(data, list) else data.get("providers", [])
    # Coherence avec budget_hub/prechauffage (13/08) : on compte les gratuits
    # ACTIFS (enabled) — qwen-local est free=True mais en pause (enabled=False)
    free_count = sum(1 for p in providers
                     if isinstance(p, dict) and p.get("free") is True
                     and p.get("enabled", True) is not False)
    print(free_count)
except Exception:
    print(0)
' ~/prise-ia/providers.json 2>/dev/null)
  if [ -n "$count" ] && [ "$count" -gt 0 ] 2>/dev/null; then
    ok "gratuits dynamiques détectés ($count)"
  else
    warn "aucun provider gratuit détecté — la bascule tempête serait sans filet"
  fi
else
  warn "providers.json absent — impossible de vérifier les gratuits dynamiques"
fi

# R3 — Rapport de préchauffage récent
if [ -f ~/prise-ia/prechauffage_reserve.json ]; then
  now=$(date +%s)
  mtime=$(stat -f %m ~/prise-ia/prechauffage_reserve.json 2>/dev/null || stat -c %Y ~/prise-ia/prechauffage_reserve.json 2>/dev/null || echo 0)
  if [ "$mtime" -gt 0 ] 2>/dev/null; then
    date_str=$(date -r "$mtime" "+%Y-%m-%d %H:%M" 2>/dev/null || echo "récemment")
  else
    date_str="date inconnue"
  fi
  verdict=$(python3 -c '
import json, sys
try:
    with open(sys.argv[1]) as f:
        j = json.load(f)
    print(j.get("verdict", ""))
except Exception:
    print("")
' ~/prise-ia/prechauffage_reserve.json 2>/dev/null)
  age=$((now - mtime))
  if [ "$verdict" = "OK" ] && [ "$age" -lt 86400 ]; then
    ok "préchauffage réserve OK ($date_str)"
  elif [ "$verdict" = "OK" ]; then
    warn "préchauffage réserve trop ancien (>24h) — lancer : cd ~/prise-ia && python3 prechauffage_reserve.py"
  else
    warn "préchauffage réserve verdict=$verdict — lancer : cd ~/prise-ia && python3 prechauffage_reserve.py"
  fi
else
  warn "préchauffage réserve pas OK/récent — lancer : cd ~/prise-ia && python3 prechauffage_reserve.py"
fi

# R4 — Préchauffage exécutable
if [ -x ~/prise-ia/prechauffage_reserve.py ]; then
  ok "préchauffage prêt"
else
  warn "prechauffage_reserve.py absent"
fi

# --- Ruby ---
if ! command -v ruby >/dev/null 2>&1; then
  fail "ruby absent"
else
  ok "ruby $(ruby -e 'print RUBY_VERSION')"
fi

echo ""
if [ "$errors" -gt 0 ]; then
  echo "=== PREFLIGHT ÉCHEC === ${errors} erreur(s), ${warnings} avertissement(s)"
  exit 1
fi
echo "=== PREFLIGHT OK === ${warnings} avertissement(s)"
exit 0

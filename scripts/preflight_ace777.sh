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
# Toute modif du genesis (même bien intentionnée) DOIT passer par un re-scelle + re-scellage doc.
_champion_attendu="98c80b5cf71db06697533aa48c5fd335"
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

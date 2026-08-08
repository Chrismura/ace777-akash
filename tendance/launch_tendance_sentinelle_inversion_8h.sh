#!/bin/bash
# === TENDANCE 8H - SENTINELLE & INVERSION ===
# BETA: MOM=0.85 (sentinelle, lecture de boite)
# ALPHA: inversion SHORT avec shock inversion actif
# Logique cible: si contexte se retourne apres tension forte, ALPHA frappe en opposite

cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

export LLM_GATE_ENABLED=TRUE
export LLM_MODEL="${LLM_MODEL:-qwen2.5-coder:1.5b}"
export LLM_OLLAMA_URL="${LLM_OLLAMA_URL:-http://127.0.0.1:11434}"

# Base execution
export POLL_SEC=0.032
export VOLATILITY_IMPULSE_DT_MS=32
export IMPULSE_RESONANCE_DT_MS=32
export STASE_DYNAMIQUE_ENABLED=TRUE
export STASE_DYNAMIQUE_MAX_SPREAD_BPS=5
export STASE_DYNAMIQUE_MAX_VOLATILITY=0.5

# Parametres setup Tendance
# BETA : sentinelle (temps long)
export VOLATILITY_DT_MS_BETA=500
export MOM_BETA=0.85
export MOMENTUM_THRESHOLD_BETA="${MOM_BETA}"
export MOMENTUM_THRESHOLD_ALPHA=0.85

# ALPHA : chasseur de vide (temps court)
export VOLATILITY_DT_MS_ALPHA=32
export SHOCK_INVERSION_ENABLED=TRUE
export LEVERAGE_ALPHA=13
export VACUUM_TENSION_THRESHOLD_BETA=0.618
export VACUUM_TENSION_THRESHOLD_ALPHA=0.618
export SHOCK_INVERSION_ALPHA="${SHOCK_INVERSION_ENABLED}"
export BUY_USDT_BETA=400
export BUY_USDT_ALPHA=400
export SHOCK_EXIT_10_BPS=18.0
export V8_SHOCK_SPEED_EPS_BPS_S=0.0
export DUO_HUNTER_AGGR_TRAIL_ARM_BPS=12
export DUO_HUNTER_AGGR_TRAIL_GIVEBACK_BPS=9
export DUO_V6_BURST_COOLDOWN_SEC=240
export SOFT_COOLDOWN_CYCLES=5

# Isolement symbole: tendance ETH only (sauf override explicite)
export SYMBOL="${SYMBOL:-ETHUSDT}"

# ALPHA fixe a 13 pour ce setup
export LEVERAGE_ALPHA_START="${LEVERAGE_ALPHA}"
export LEVERAGE_ALPHA_END="${LEVERAGE_ALPHA}"
export LEVERAGE_ALPHA_RAMP_CYCLES=1

# Le lien (symbiose)
export DUO_SYNC_MODE=AGGRESSIVE_HEDGE

# Securite session: reset PnL inter-runs
rm -f runs/duo_session.json STOP_*
export RUN_STATE_ENABLED=FALSE
export RUN_STATE_LINK_TOTAL_PNL=FALSE
export RUN_SEC_OVERRIDE=28800
export TEST_TAG_OVERRIDE="MASTER_TENDANCE_SENTINELLE_INVERSION_8H00"

# Pilotage lent par Superviseur V9 (vortex_control.json)
export VORTEX_CONTROL_ENABLED=TRUE
export VORTEX_CONTROL_FILE="runs/vortex_control.json"
export VORTEX_CHOP_RADAR=0.85
export VORTEX_TREND_RADAR=0.618
export VORTEX_CHOP_MOM=0.95
export VORTEX_TREND_MOM=0.85

echo "=== TENDANCE SENTINELLE&INVERSION 8H ==="
echo "BETA LONG dt=500ms mom=0.85 | ALPHA SHORT dt=32ms mom=0.85 lev=13 inversion=TRUE"
echo "Symbiose: DUO_SYNC_MODE=AGGRESSIVE_HEDGE | ETHUSDT | Radar=0.618 | Masse 400/400"
echo "Trailing hunter=12/9 | Shock=-18bps | RunState=OFF"
echo "Vortex control: ON (${VORTEX_CONTROL_FILE}) via supervisor_v9.sh"

exec ./tendance/launch_test_master_tendance_sentinelle_inversion.sh

#!/bin/bash
# === VIDE FROID 8H - Protocole ACE777 ===
# L'ENTRÉE 25/75% | ÉJECTION -10 bps | STASE DYNAMIQUE | Base 16 @ 64ms

cd "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

export LLM_GATE_ENABLED=TRUE

# Vide Froid - Entrée progressive
export ENTRY_25_75_ENABLED=TRUE
export ENTRY_25_75_CONFIRM_MS=500
export ENTRY_25_75_FLUX_MIN_BPS=-5

# Vide Froid - Shock-Exit instantané -10 bps
export SHOCK_EXIT_10_BPS_ENABLED=TRUE
export SHOCK_EXIT_10_BPS=10

# Vide Froid - Stase Dynamique (Mode Écoute après anomaly)
export STASE_DYNAMIQUE_ENABLED=TRUE
export STASE_DYNAMIQUE_MAX_SPREAD_BPS=5
export STASE_DYNAMIQUE_MAX_VOLATILITY=0.5

# Base 16 - Latence 64ms M1
export POLL_SEC=0.064
export VOLATILITY_IMPULSE_DT_MS=64
export IMPULSE_RESONANCE_DT_MS=64

echo "=== VIDE FROID 8H ==="
echo "Entrée 25/75% | Shock-Exit -10bps | Stase Dynamique | Latence 64ms"
exec ./launch_test_master_base_v8_6_fortress.sh --duration 08:00:00

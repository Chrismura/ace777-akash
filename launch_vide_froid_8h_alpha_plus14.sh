#!/bin/bash
# === VIDE FROID 8H - ALPHA +14 PROFILE ===
# Base robuste identique au setup en cours.
# Objectif: figer le profil HUNTER observé sur les trades +14
# SANS modifier la masse.

cd "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

export LLM_GATE_ENABLED=TRUE

# Vide Froid - Entrée progressive (inchangé)
export ENTRY_25_75_ENABLED=TRUE
export ENTRY_25_75_CONFIRM_MS=500
export ENTRY_25_75_FLUX_MIN_BPS=-5

# Vide Froid - Shock-Exit ajuste
export SHOCK_EXIT_10_BPS_ENABLED=TRUE
export SHOCK_EXIT_10_BPS=9.68

# Vide Froid - Stase Dynamique (inchangé)
export STASE_DYNAMIQUE_ENABLED=TRUE
export STASE_DYNAMIQUE_MAX_SPREAD_BPS=5
export STASE_DYNAMIQUE_MAX_VOLATILITY=0.5

# Base 16 - Latence 32ms (priorite trailing ALPHA)
export POLL_SEC=0.032
export VOLATILITY_IMPULSE_DT_MS=32
export IMPULSE_RESONANCE_DT_MS=32

# Radar plus permissif (applique explicitement BETA et ALPHA)
export VACUUM_TENSION_THRESHOLD=0.75
export VACUUM_TENSION_THRESHOLD_BETA=0.75
export VACUUM_TENSION_THRESHOLD_ALPHA=0.75

# Masse: strictement identique au setup robuste actuel (pas de changement)
export BUY_USDT_BETA=400
export BUY_USDT_ALPHA=400

# Profil ALPHA/HUNTER observé sur les +14 (explicité, sans changer la masse)
export DUO_HUNTER_REVENGE_MULT=1.5
export DUO_HUNTER_REQUIRE_STOP_LOSS=TRUE
export DUO_HUNTER_AGGR_TRAIL_ARM_BPS=2
export DUO_HUNTER_AGGR_TRAIL_GIVEBACK_BPS=1

# Shock inversion detendu (moins nerveux)
export V8_SHOCK_SPEED_EPS_BPS_S=0.0

echo "=== VIDE FROID 8H - ALPHA +14 PROFILE ==="
echo "Entrée 25/75% | Shock-Exit -9.68bps | Stase Dynamique | Latence 32ms"
echo "Radar=0.75 | Shock inversion detendu"
echo "Masse conservee: BETA=400 | ALPHA=400"
echo "Alpha profile: hunter_revenge_1.5x + trailing agressif (2/1 bps)"
exec ./launch_test_master_base_v8_6_fortress.sh --duration 08:00:00

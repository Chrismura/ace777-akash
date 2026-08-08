#!/usr/bin/env bash
# Vérif setup champion 10/07 20:27 session 204206 (+29,41 USDT) — SANS lancer
# Usage: ./scripts/verif_setup_champion.sh
# Exit 0 = OK pour lancer | Exit 1 = ne pas lancer

set -uo pipefail
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

GENESIS_MD5="37fca36712d49aa8b97890c5cad5f2e6"
VORTEX_MD5="6ce82f6bb0819faff94b954c43f3f336"
GEMINI_MD5="35bd09c9ec2611a1a9cbcbe81727bf72"

errors=0
ok()   { echo "OK: $1"; }
fail() { echo "FAIL: $1"; errors=$((errors + 1)); }

echo "=== VERIF SETUP CHAMPION 204206 (sans run) ==="
echo "Référence: +29,41 USDT | genesis 37fca367 | BETA x3 | ALPHA x13 fixe | barrière OUI | PHI NON"
echo ""

# Processus
if pgrep -fl "ace777-test-day1|launch_vortex|GEMINI_TEST|bash -s|watchdog_ace777" 2>/dev/null | grep -v watchdogd >/dev/null; then
  fail "process actif — ./stop_ace777_hard.sh d'abord"
  pgrep -fl "ace777|launch_vortex|GEMINI|bash -s|watchdog_ace777" 2>/dev/null | grep -v watchdogd || true
else
  ok "0 process ACE777"
fi

# md5 moteur + lanceurs
g="$(md5 -q genesis_manifest.txt 2>/dev/null || true)"
v="$(md5 -q launch_vortex_v2_collab_4h_binance.sh 2>/dev/null || true)"
m="$(md5 -q launch_test_master_base_v8_5_impact_GEMINI_TEST.sh 2>/dev/null || true)"

[ "$g" = "$GENESIS_MD5" ] && ok "genesis md5 $g" || fail "genesis md5=$g attendu $GENESIS_MD5"
[ "$v" = "$VORTEX_MD5" ] && ok "vortex md5 $v" || fail "vortex md5=$v attendu $VORTEX_MD5"
[ "$m" = "$GEMINI_MD5" ] && ok "GEMINI md5 $m (BETA x3)" || fail "GEMINI md5=$m attendu $GEMINI_MD5"

# Sémantique genesis
if grep -q "duo_hunter_phase_barrier" genesis_manifest.txt && ! grep -q "calculate_quantum_flux" genesis_manifest.txt; then
  ok "genesis: barrière duo OUI, PHI NON (37fca367 / 204206)"
else
  fail "genesis sémantique — attendu barrière OUI et PHI NON (37fca367)"
fi

# BETA levier boot 204206 = x3 dans GEMINI_TEST (log: Leverage=3)
if grep -q 'export LEVERAGE="3"' launch_test_master_base_v8_5_impact_GEMINI_TEST.sh; then
  ok "GEMINI BETA LEVERAGE=3 (identique boot 20:27)"
else
  fail "GEMINI BETA LEVERAGE — attendu export LEVERAGE=\"3\" (pas x5)"
fi

# ALPHA rampe gemini = x13 fixe dès cycle 1
if grep -q 'export LEVERAGE_RAMP_START="13"' launch_test_master_base_v8_5_impact_GEMINI_TEST.sh \
   && grep -q 'export LEVERAGE_RAMP_END="13"' launch_test_master_base_v8_5_impact_GEMINI_TEST.sh; then
  ok "ALPHA rampe start=13 end=13"
else
  fail "ALPHA rampe — attendu start=13 end=13 dans GEMINI_TEST"
fi

# Syntaxe
bash -n genesis_manifest.txt 2>/dev/null && ok "bash -n genesis" || fail "bash -n genesis"
bash -n launch_vortex_v2_collab_4h_binance.sh 2>/dev/null && ok "bash -n vortex" || fail "bash -n vortex"
bash -n launch_test_master_base_v8_5_impact_GEMINI_TEST.sh 2>/dev/null && ok "bash -n GEMINI" || fail "bash -n GEMINI"

# STOP
if [ -f STOP ] || [ -f STOP_ALPHA ] || [ -f STOP_BETA ]; then
  fail "fichiers STOP présents — rm -f STOP STOP_ALPHA STOP_BETA avant lancement"
else
  ok "pas de STOP"
fi

# ALPHA_RAMP_MODE=model => rampe 5->13 (PAS le champion)
if [ "${ALPHA_RAMP_MODE:-}" = "model" ]; then
  fail "ALPHA_RAMP_MODE=model — faire: unset ALPHA_RAMP_MODE"
else
  ok "ALPHA_RAMP_MODE absent ou != model (ramp=gemini)"
fi

echo ""
if [ "$errors" -gt 0 ]; then
  echo "=== VERIF ÉCHEC ($errors) — NE PAS LANCER ==="
  exit 1
fi

echo "=== VERIF OK — setup identique 204206 prêt ==="
echo ""
echo "cd /Users/christophe/ace777-test-day1"
echo "unset ALPHA_RAMP_MODE"
echo "export LAUNCH_V85_SCRIPT=./launch_test_master_base_v8_5_impact_GEMINI_TEST.sh"
echo "./launch_vortex_v2_collab_4h_binance.sh"
echo ""
echo "Ou: ./29$/REDEMARRER.sh lancer"
echo ""
echo "Boot attendu (15 sec):"
echo "  GEMINI_TEST ramp=gemini (x13 fixe dès cycle 1)"
echo "  Leverage ramp ON: start=13 end=13"
echo "  BETA Symbol=BTCUSDT Leverage=3"
echo "  ALPHA Symbol=BTCUSDT Leverage=13"
exit 0

#!/usr/bin/env bash
set -euo pipefail

cd /Users/christophe/ace777-test-day1

# Enchaine 3 runs de test sur la meme base V6.3
# Levier scout fixe a x5, levier hunter successif: x5 -> x8 -> x13
# Duree par run configurable (par defaut 10 minutes)

RUN_SEC_EACH="${RUN_SEC_EACH:-600}"
SCOUT_LEVERAGE="${SCOUT_LEVERAGE:-5}"
HUNTER_LEVERAGES="${HUNTER_LEVERAGES:-5 8 13}"

echo "=== TEST V6.3 LEVIERS HUNTER: ${HUNTER_LEVERAGES} ==="
echo "Run par levier: ${RUN_SEC_EACH}s"
echo "Scout leverage: x${SCOUT_LEVERAGE}"

for lev in ${HUNTER_LEVERAGES}; do
  echo ""
  echo "--- START HUNTER x${lev} ---"
  TEST_TAG="TEST_MODELE_14_V63_L${lev}_${RUN_SEC_EACH}s" \
  RUN_SEC="${RUN_SEC_EACH}" \
  SCOUT_LEVERAGE="${SCOUT_LEVERAGE}" \
  HUNTER_LEVERAGE="${lev}" \
  bash ./launch_modele_14_v63_30m_test.sh
  echo "--- END HUNTER x${lev} ---"
  sleep 2
done

echo ""
echo "=== FIN TEST LEVIERS 5/8/13 ==="

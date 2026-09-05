#!/usr/bin/env bash
# VARIANTE RADAR-ALIGNED — Beta suit le signal radar au lieu de FORCE_ENTRY_SIDE=SELL
# Patch temporaire du lanceur original, puis restauration automatique.
# NE MODIFIE PAS le champion.
#
# Usage :
#   BINANCE_MODE=testnet TEST_TAG_OVERRIDE=ACE_RADAR_ALIGNED_V1_15M ./launch_radar_aligned.sh

set -euo pipefail

PROJDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LAUNCHER="$PROJDIR/launch_test_master_base_v8_5_impact.sh"
BACKUP="$LAUNCHER.bak_radar_aligned"

if [ ! -f "$LAUNCHER" ]; then
  echo "PREFLIGHT_ERR: lanceur introuvable : $LAUNCHER"
  exit 1
fi

# Sauvegarde, patch, restauration garantie
cp "$LAUNCHER" "$BACKUP"
trap 'mv -f "$BACKUP" "$LAUNCHER" 2>/dev/null; rm -f "$BACKUP" 2>/dev/null' EXIT

# Patch : supprime FORCE_ENTRY_SIDE=SELL dans launch_beta
python3 -c "
import re
with open('$LAUNCHER') as f:
    c = f.read()
s = c.find('launch_beta()')
e = c.find(') &', s)
block = c[s:e]
c = c[:s] + re.sub(r'[ \t]*export FORCE_ENTRY_SIDE=\"SELL\"\n', '', block) + c[e:]
with open('$LAUNCHER', 'w') as f:
    f.write(c)
"

echo "=== VARIANTE RADAR-ALIGNED ==="
echo "Beta suit le signal radar (FORCE_ENTRY_SIDE=SELL supprimé)"
echo ""

# Exécute le lanceur patché (sans exec : le trap de restauration doit survivre)
bash "$LAUNCHER"

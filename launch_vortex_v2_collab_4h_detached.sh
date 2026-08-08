#!/usr/bin/env bash
# Run 4h Vortex v2 — mode DÉTACHÉ (survit fermeture terminal / Cursor)
# Usage: ./launch_vortex_v2_collab_4h_detached.sh
# Superviseur : auto-démarré par le master

set -euo pipefail
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

./stop_ace777.sh 2>/dev/null || true
sleep 2

export CAFFEINATE_RUN=TRUE
export TEST_TAG_OVERRIDE=MASTER_VORTEX_V2_COLLAB_4H

# shellcheck source=scripts/load_config.sh
source ./scripts/load_config.sh vortex_v2_collab

mkdir -p runs
nohup ./launch_vortex_v2_collab_4h_binance.sh >> runs/t1_launch.log 2>&1 &
echo $! > runs/t1_launcher.pid

echo "=== RUN DÉTACHÉ LANCÉ ==="
echo "launcher_pid=$(cat runs/t1_launcher.pid)"
echo "log: runs/t1_launch.log"
echo "Superviseur: auto-attache (vérifier runs/supervisor_v9_v2.pid)"
echo ""
echo "Vérif:"
echo "  tail -f runs/t1_launch.log"
echo "  tail -3 runs/MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv"

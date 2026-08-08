#!/bin/bash
# BONNET DE FORME CHAMPION — arrêt total
set -euo pipefail
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
exec ./stop_ace777_hard.sh

#!/bin/bash
# rebuild_graph.sh — régénère le graphe du cerveau (data.js/data.json) et le
# synchronise partout. Cadence : chaque jour 11h30 (plist com.ace777.graph-cerveau).
# Cause racine (09/08, question Christophe « l'app graph ne bouge pas ») :
# l'app est STATIQUE (lit data.js) — il faut rebuild après chaque changement.
set -uo pipefail
INDEX="$HOME/ace777-test-day1/Index_Maison"
VAULT="$HOME/Documents/Obsidian_ACE777/graph_cerveau"
OUTBOX="$INDEX/OUTBOX_OBSIDIAN/graph_cerveau"

cd "$INDEX" || exit 1
OUT=$(python3 scripts/build_cerveau_graph.py 2>&1 | tail -1)
cp graph_cerveau/data.js graph_cerveau/data.json "$VAULT/" 2>/dev/null
cp graph_cerveau/data.js graph_cerveau/data.json "$OUTBOX/" 2>/dev/null
echo "[$(date -u +%Y-%m-%dT%H:%MZ)] GRAPH: $OUT (sync vault + OUTBOX OK)"

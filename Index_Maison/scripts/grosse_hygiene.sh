#!/usr/bin/env bash
# Gros ménage froid — ne lance PAS ACE/Hulk
set -euo pipefail
ROOT="/Users/christophe/ace777-test-day1"
cd "$ROOT"

echo "=== GROSSE HYGIÈNE (froid) ==="

echo
echo "1) État Mac (lecture)"
bash "$ROOT/Index_Maison/scripts/etat_mac.sh" || true

echo
echo "2) Hygiène RAM WebKit (orphelins) — check puis purge"
bash "$ROOT/scripts/hygiene_mac_ram.sh" --check || true
bash "$ROOT/scripts/hygiene_mac_ram.sh" || true

echo
echo "3) Hygiène après arrêt ACE (rapports / orphelins)"
bash "$ROOT/scripts/hygiene_apres_arret.sh" --kill-orphans || true

echo
echo "4) Journal + console"
/usr/bin/python3 "$ROOT/Index_Maison/scripts/journal_auto.py" || true

echo
echo "5) Cockpit indicateurs (zone test — thermo + mission feed + pont)"
bash "$ROOT/Index_Maison/scripts/cockpit_hygiene_check.sh" || true

echo
echo "6) Sync OUTBOX → Obsidian (si TCC OK dans ce Terminal)"
bash "$ROOT/Index_Maison/OUTBOX_OBSIDIAN/_sync_now.sh" || true

echo
echo "=== HYGIÈNE FINIE — bots toujours OFF sauf si tu les as relancés toi-même ==="

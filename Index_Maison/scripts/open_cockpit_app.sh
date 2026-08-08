#!/usr/bin/env bash
# Cockpit fenêtre dédiée — HTTP local :17800 (évite écran noir file://)
set -uo pipefail
ROOT="/Users/christophe/ace777-test-day1"
cd "$ROOT"
exec /usr/bin/python3 Index_Maison/scripts/open_cockpit_app.py "$@"

#!/bin/bash
# Hygiène soir : console + journal → workspace + Obsidian
set -euo pipefail
ROOT="/Users/christophe/ace777-test-day1"
# shellcheck disable=SC1091
[[ -f "$ROOT/veille-punk/obsidian.env" ]] && source "$ROOT/veille-punk/obsidian.env"
exec /usr/bin/python3 "$ROOT/Index_Maison/scripts/journal_auto.py" --sync "$@"

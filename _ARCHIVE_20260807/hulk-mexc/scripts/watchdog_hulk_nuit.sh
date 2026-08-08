#!/usr/bin/env bash
# Compat: ancien nom « nuit/fantôme » → Ghost
exec "$(cd "$(dirname "$0")" && pwd)/watchdog_hulk_ghost.sh" "$@"
